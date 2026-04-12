# Architecture Context

This document captures the reasoning, design decisions, and architectural explanations
behind the ElectricSQL + TanStack DB + Drizzle migration. It is a reference for
returning to this work and understanding *why* things are structured the way they are.

---

## Stack overview

- **Drizzle ORM** — write path to Postgres; schema definitions; relational queries
- **ElectricSQL** — sync layer that streams Postgres changes to clients via HTTP shapes
- **TanStack DB** — client-side collection management with optimistic updates and live queries
- **`pg_current_xact_id()`** — Postgres function that returns the transaction ID of the current transaction, used to tie the optimistic state lifecycle in with the sync machinery

---

## How the controllers work

The controllers are plain async functions — no classes, no decorators. Each one accepts
typed arguments and a `ServerContext` (which carries `db` and `userId`), performs
authorization, then writes to Postgres via Drizzle.

```ts
export async function observationUpdate(
    id: string,
    data: ObservationUpdateCommand,
    ctx: ServerContext
): Promise<{ txid: number }> {
    // 1. fetch the row to get its gardenId
    // 2. authorize the calling user against that garden
    // 3. run the write inside a transaction
    // 4. return the txid
}
```

The two-step fetch-then-authorize pattern is intentional: Drizzle doesn't have row-level
guards built in, so controllers manually load the row, extract its `gardenId`, and pass
that to `requireGardenRole` before touching anything.

`requireGardenRole` in `apps/server/src/controllers/context.ts` is the shared
authorization primitive all garden-scoped controllers delegate to. It fetches the garden,
runs `isUserAuthorized(garden, ctx.userId, role)` (which checks the
`adminIds`/`editorIds`/`viewerIds` arrays), and throws an `AppError` if the check fails —
so authorization is never something a controller can accidentally skip.

---

## `pg_current_xact_id()` — what it is and why

Every write returns `{ txid: number }`. That number is PostgreSQL's internal transaction
ID for the transaction that just committed.

```sql
SELECT pg_current_xact_id()::xid::text AS txid
```

**Why it exists:** ElectricSQL's sync engine streams a change feed from Postgres to
clients. Each change in that feed carries the transaction ID that produced it. On the
client side, TanStack DB lets you make *optimistic* mutations — you update local state
immediately before the server confirms. When the server's response comes back with a
`txid`, the client can watch the Electric change stream and know exactly when its write
has been synced back ("my mutation with txid 4231 has arrived — I can retire the
optimistic update"). Without this, you'd be guessing based on timestamps or polling.

**Why raw SQL instead of the ORM:** Drizzle doesn't have a query builder method for
`pg_current_xact_id()` — it's a Postgres-specific system function with no abstraction.
The `sql` tagged template is Drizzle's escape hatch for anything the query builder
doesn't cover. It's still safe (parameterized, type-checked at the call site) — it just
can't be expressed through the fluent API.

The cast chain `::xid::text` is needed because the raw return type is a 64-bit
transaction ID (`xid8`), which doesn't serialize cleanly over the wire. Casting to `xid`
(32-bit for backwards compat) then `text` gives a plain decimal string that `parseInt`
can consume.

---

## Data flow: API layer → controller layer

The intended flow once route handlers are written:

```
HTTP request
    ↓
Fastify route handler
    - parse & validate body (Zod command schema)
    - pull db from DI container  (container.resolve('db'))
    - pull userId from request scope  (request.diScope.resolve('client').id)
    - build ServerContext = { db, userId }
    ↓
Controller function
    - authorize (requireGardenRole checks garden membership)
    - write to Postgres inside db.transaction(...)
    - return { txid }
    ↓
Route handler returns { txid } (or { id, txid }) as JSON
    ↓
Client receives txid, applies optimistic update,
watches Electric sync stream for the matching txid to arrive
```

`ServerContext` is the seam. The route handler is responsible for building it — the
controller never touches the HTTP request. This keeps controllers fully testable without
standing up Fastify: you can call `observationUpdate(id, data, { db: testDb, userId: 'abc' })`
directly in a test.

---

## Individual endpoints vs generic ingest endpoint

### The two architectures

**What we have — individual endpoints:**
```
POST /observations/:id      → observationUpdate()   → { txid }
POST /gardens               → gardenCreate()        → { id, txid }
POST /planting-areas        → plantingAreaCreate()  → { id, txid }
```

**Generic ingest — single endpoint:**
```
POST /ingest   { mutations: [...] }   → one Postgres transaction → { txid }
```

The mutations payload the guide describes looks like:
```ts
{
  mutations: [
    { type: 'update', key: 'obs-123',  original: {...}, changes: { date: '2025-04-12' } },
    { type: 'insert', key: 'geo-456',  original: null,  changes: { type: 'RECTANGLE', ... } },
    { type: 'delete', key: 'loc-789',  original: {...}, changes: {} }
  ]
}
```

The server receives whatever the client decided to batch and applies it all in one
transaction.

### The core tradeoff

With individual endpoints the **server** controls what operations exist and what they
mean. With generic ingest the **client** controls what data gets written and the server
just validates and applies it. This one difference cascades into everything else.

### Authorization

**Individual endpoints:** Authorization is operation-aware. `observationUpdate` fetches
the observation, gets its `gardenId`, checks the caller's role against that garden. The
check is semantically correct because it knows what the operation is doing.

**Generic ingest:** You get a list of mutations across arbitrary tables. To authorize
them you have to identify which table each mutation targets, then for row-level checks
fetch the parent row to get `gardenId` — for every mutation, per table, and apply the
correct role check per table type. You'd end up writing a dispatch table:

```ts
const authorizers: Record<string, (mutation, ctx) => Promise<void>> = {
  observations: async (m, ctx) => {
    const obs = await db.query.observations.findFirst(...)
    await requireGardenRole(ctx, obs.gardenId, 'ObservationUpdate')
  },
  geometries: async (m, ctx) => { ... },
  // one per table
}
```

At that point you've reinvented the controller layer inside the ingest handler, just
with a less clear call path.

### Business logic and invariants

**Individual endpoints:** `gardenCreate` always adds the creator to `adminIds`.
`workspaceCreate` generates the slug and checks uniqueness. `gardenMembershipRoleChange`
prevents self-role changes and protects the creator. These rules live naturally in the
controller.

**Generic ingest:** A payload containing `{ type: 'insert', table: 'gardens', changes: { id: 'x', adminIds: [] } }`
has no natural place for "always include creator." The server either trusts the client
(fragile), runs Postgres triggers (correct but hard to surface as user-facing validation
errors), or post-processes each mutation per table (same complexity as individual
controllers, worse structure).

Operations like cultivar attribute merging or slug generation fundamentally require
server-side computation that can't be expressed as a raw data write. A generic ingest
can't handle them cleanly.

### The txid / awaitTxId problem — where generic ingest wins clearly

This is the real tension with our current approach. Consider a client-side action that
touches multiple collections:

```ts
const createPlantingArea = createOptimisticAction({
  action: (data) => {
    geometryCollection.insert({ id: geoId, ... })
    locationCollection.insert({ id: locId, ... })
    plantingAreaCollection.insert({ id: areaId, ... })
  },
  mutationFn: async (data, { transaction }) => {
    // transaction.mutations has 3 entries across 3 collections
  }
})
```

**With individual endpoints:**

The `mutationFn` can call the compound `POST /planting-areas` endpoint, which runs one
Postgres transaction covering all three tables and returns one txid. Then:

```ts
mutationFn: async (data, { transaction }) => {
  const { txid } = await api.post('/planting-areas', data)
  // All three collections await the same txid — works fine
  await Promise.all([
    geometryCollection.utils.awaitTxId(txid),
    locationCollection.utils.awaitTxId(txid),
    plantingAreaCollection.utils.awaitTxId(txid)
  ])
}
```

This works because `plantingAreaCreate` is already a compound operation internally.
One endpoint, one txid, three collections all awaiting it.

But if a client action needs to call multiple independent endpoints:

```ts
mutationFn: async (_vars, { transaction }) => {
  const r1 = await api.post('/observations', ...)      // txid: 4231
  const r2 = await api.patch('/workspaces/:id', ...)   // txid: 4232
  // Two different txids — not atomic, can partially succeed
}
```

Two separate transactions means they can partially succeed. That's a correctness problem
if the action is supposed to be atomic.

**With generic ingest:**

```ts
mutationFn: async (_vars, { transaction }) => {
  const mutations = transaction.mutations
  const collections = new Set(mutations.map(m => m.collection))
  const { txid } = await api.post('/ingest', {
    mutations: mutations.map(({ collection, ...m }) => m)
  })
  // One txid covers everything — always
  await Promise.all([...collections].map(c => c.utils.awaitTxId(txid)))
}
```

One call, one Postgres transaction, one txid regardless of how many collections the
action touched. This is the model TanStack DB's `createOptimisticAction` is designed
around.

### Comparison table

| Concern | Individual endpoints | Generic ingest |
|---|---|---|
| Authorization | Operation-aware, natural | Requires per-table dispatch |
| Business logic | Enforced in controllers | Requires triggers or hooks |
| Computed server state (slugs, merges) | Easy | Not possible without hooks |
| Atomicity of cross-collection actions | Only if you have a compound endpoint | Always — one POST = one transaction |
| `awaitTxId` with `createOptimisticAction` | Works cleanly only for pre-defined compound ops | Works uniformly for any action |
| API surface | Explicit contract, self-documenting | Implicit, driven by client shape |
| Error messages | Per-field validation, domain-specific | Generic unless you add per-table rules |
| Client coupling | Knows which endpoint to call | Just POSTs mutations, doesn't care |

### What a hybrid looks like in practice

**Good candidates for generic ingest** — pure data writes with no server-side
computation and authorization maps to a simple role check:
- `observationUpdate` / `observationDelete`
- `geometryUpdate`, `locationUpdate`
- `plantUpdate`, `lifespanUpdate`
- `environmentAttributesUpdate`

**Must stay as individual endpoints** — have business logic that can't be expressed as
raw data:
- `gardenCreate` (adds creator to adminIds, creates membership)
- `gardenMembershipRoleChange` (self-change guard, creator guard, array manipulation)
- `workspaceCreate` / `workspaceUpdate` (slug generation and uniqueness check)
- `plantingAreaCreate` (compound, creates 4 rows atomically)
- All cultivar resolver functions (recursive CTE logic is read-path, not writes)

The cost of a hybrid is that you now have two mutation patterns on the client and need
to decide per-operation which one applies.

---

## How the Electric TypeScript client fits in

### Two levels

```
@electric-sql/client  (ShapeStream, Shape)
        ↑
        wraps
        ↑
@tanstack/electric-db-collection  (electricCollectionOptions)
```

When using TanStack DB you mostly never touch `ShapeStream` or `Shape` directly —
`electricCollectionOptions` uses them internally. The one piece of `@electric-sql/client`
you *do* use on the server is `ELECTRIC_PROTOCOL_QUERY_PARAMS`.

### The proxy route — what the Fastify server needs

The recommended pattern means the client never talks to Electric directly. Instead:

```
TanStack DB collection  →  GET /api/shapes/observations  →  Electric  →  Postgres WAL
```

The Fastify server needs shape proxy routes alongside the write controllers. A proxy
route looks like:

```ts
// apps/server/src/shapes/observations.ts
import { ELECTRIC_PROTOCOL_QUERY_PARAMS } from '@electric-sql/client'
import { FastifyInstance } from 'fastify'
import env from 'env.js'
import { requireAuth } from '../plugins/auth.js'

export function registerObservationsShape(app: FastifyInstance) {
  app.get('/api/shapes/observations', async (req, reply) => {
    const client = requireAuth(req.diScope.resolve('client'))

    const electricUrl = new URL(`${env.ELECTRIC_URL}/v1/shape`)

    // Forward Electric's own protocol params (offset, handle, live, etc.)
    // so streaming/resumption works correctly
    ELECTRIC_PROTOCOL_QUERY_PARAMS.forEach((param) => {
      const value = (req.query as Record<string, string>)[param]
      if (value) electricUrl.searchParams.set(param, value)
    })

    // Server controls table — never exposed to client
    electricUrl.searchParams.set('table', 'observations')

    // Server controls authorization — user only gets their gardens' data
    const gardenIds = await getUserGardenIds(app.db, client.profileId)
    if (gardenIds.length === 0) {
      reply.send([])
      return
    }
    electricUrl.searchParams.set(
      'where',
      `garden_id IN (${gardenIds.map((id) => `'${id}'`).join(',')})`
    )

    // Stream the response — don't buffer it, Electric uses long-poll or SSE
    const upstream = await fetch(electricUrl.toString())
    reply.status(upstream.status as number)
    upstream.headers.forEach((value, key) => reply.header(key, value))
    reply.send(upstream.body)
  })
}
```

`ELECTRIC_PROTOCOL_QUERY_PARAMS` is the list of Electric's internal
pagination/streaming params (`offset`, `handle`, `live`, `cursor`, etc.). The client
sends these on subsequent requests to resume a stream from where it left off. The proxy
must forward them verbatim — if you drop them the client restarts the stream from
scratch on every reconnect.

### What `getUserGardenIds` looks like

The WHERE clause in the proxy is the authorization boundary. For our schema, since
garden membership is stored as arrays on the `gardens` table:

```ts
export async function getUserGardenIds(db: Db, profileId: string): Promise<string[]> {
  const rows = await db.query.gardens.findMany({
    where: (g, { or, arrayContains }) => or(
      arrayContains(g.adminIds, [profileId]),
      arrayContains(g.editorIds, [profileId]),
      arrayContains(g.viewerIds, [profileId])
    ),
    columns: { id: true }
  })
  return rows.map(r => r.id)
}
```

### How the client side uses the proxy

On the client, `electricCollectionOptions` points at the proxy URL, not at Electric
directly:

```ts
import { electricCollectionOptions } from '@tanstack/electric-db-collection'
import { createCollection } from '@tanstack/react-db'

const observationCollection = createCollection(
  electricCollectionOptions({
    id: 'observations',
    shapeOptions: {
      url: 'http://localhost:3001/api/shapes/observations',
      // No table, no where — server controls those
    },
    getKey: (item) => item.id,
    schema: ObservationSchema,
  })
)
```

The client treats it like any API endpoint. It has no idea Electric is involved.

### Full read + write path together

```
READ PATH

Client (electricCollectionOptions)
  → GET /api/shapes/observations?offset=...&handle=...
  → Fastify proxy: adds table='observations', where='garden_id IN (...)'
  → Electric HTTP API (long-poll or SSE)
  → Electric reads Postgres WAL
  ← streams back change messages tagged with txid
  ← Fastify forwards stream to client
  ← TanStack DB materializes changes into the collection
  ← useLiveQuery rerenders components

WRITE PATH

User action → collection.update(id, draft => { draft.date = '...' })
  → TanStack DB applies to optimistic state immediately (UI updates)
  → mutationFn fires
  → POST /api/observations/:id   { date: '...' }
  → Fastify route → observationUpdate() controller
  → Drizzle writes to Postgres inside a transaction
  ← { txid: 4231 }
  → mutationFn calls observationCollection.utils.awaitTxId(4231)
  → Electric picks up the committed WAL entry (tagged txid 4231)
  → change arrives in the shape stream
  → awaitTxId(4231) resolves
  → TanStack DB discards optimistic state (synced data matches)
```

### Server structure

The server ends up with two parallel concerns for each domain:

```
apps/server/src/
  controllers/          ← write path (implemented)
    observations.ts
    gardens.ts
    workspaces.ts
    environments.ts
    cultivars.ts
    plants.ts
    users.ts
    context.ts
  shapes/               ← read path (still needed)
    observations.ts     proxy route: table + where authorization
    gardens.ts
    workspaces.ts
    environments.ts
    plants.ts
    cultivars.ts
```

The shapes routes are simpler than controllers — mostly just `getUserGardenIds`, set the
WHERE clause, and pipe the stream. Controllers are about verifying intent and writing
data safely; shape proxies are about controlling what data each user is allowed to read.
They are distinct concerns that happen to live side by side.
