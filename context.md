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

---

## Presence and locking with Durable Streams

### What Durable Streams are

Durable Streams (durablestreams.com) are persistent, addressable, resumable real-time
streams. Each stream has a URL, an append-only log, and an offset-based protocol
identical to Electric's. Clients can reconnect and catch up rather than starting from
scratch. They have a Yjs wrapper protocol built in, making them a natural transport for
CRDT-based collaborative editing.

### Workspace presence streams

Each workspace gets a presence stream — a persistent channel all connected clients read
and write to:

```
stream address: /streams/workspaces/{workspaceId}/presence
```

The Durable Streams approach is better than WebSockets for presence because reconnecting
clients resume from their last offset rather than requiring a fresh broadcast of all
current state. No sticky sessions, no shared presence server.

The event type covers everything presence needs:

```ts
type PresenceEvent = {
  userId: string
  username: string
  color: string          // deterministic per-user color for cursors
  type: 'join' | 'leave' | 'cursor' | 'viewport' | 'lock' | 'unlock' | 'heartbeat'
  timestamp: number
  payload: {
    entityType?: 'plantingArea' | 'geometry' | 'observation'
    entityId?: string
    x?: number           // canvas coordinates
    y?: number
    viewportX?: number
    viewportY?: number
    zoom?: number
  }
}
```

### Lock semantics

Locks cannot rely on clients to release themselves — a crash or tab close leaves them
dangling. The solution is TTL-based advisory locks with a heartbeat:

```ts
const LOCK_TTL_MS = 3000        // lock expires if not renewed
const HEARTBEAT_INTERVAL = 1000  // renew every second while holding

const locks = new Map<string, { userId: string; username: string; expiresAt: number }>()

presenceStream.subscribe((events) => {
  for (const event of events) {
    if (event.type === 'lock') {
      locks.set(event.payload.entityId!, {
        userId: event.userId,
        username: event.username,
        expiresAt: event.timestamp + LOCK_TTL_MS
      })
    } else if (event.type === 'unlock') {
      locks.delete(event.payload.entityId!)
    }
  }
  const now = Date.now()
  for (const [id, lock] of locks) {
    if (lock.expiresAt < now) locks.delete(id)
  }
})
```

On drag start: write a `lock` event, then write `heartbeat` events every second.
On drop: write `unlock`, then commit final position to Postgres.

### Yjs Awareness as an alternative to raw events

Durable Streams has a Yjs wrapper protocol. `Y.Awareness` is Yjs's built-in presence
primitive and handles TTL automatically — when a client disconnects, Yjs removes their
awareness state after a timeout:

```ts
const awareness = new Y.Awareness(ydoc)
awareness.setLocalStateField('user', { id: userId, name: username, color })
awareness.setLocalStateField('cursor', { x: 142, y: 87 })
awareness.setLocalStateField('lock', { entityId: 'pa-123', entityType: 'plantingArea' })

awareness.on('change', () => {
  const states = awareness.getStates()  // Map<clientId, AwarenessState>
  // derive lock map, render cursors, show collaborator list
})
```

This removes the need to build heartbeat and TTL machinery manually.

### Advisory vs hard enforcement

Advisory locks (UI warns, doesn't block) are sufficient for collaborative tools. If hard
enforcement is needed, the controller can check the presence system before accepting a
write — but this requires a server-side Durable Streams client and is usually overkill.

---

## Optimizing Postgres sync for smooth shape editing

### The fundamental principle

Postgres is not the right path for 60fps cursor drag. Two channels with different latency
profiles:

```
High-frequency (during drag):    Presence stream → other clients in <50ms
Low-frequency (on drop):         Postgres → Electric → other clients in ~150ms with SSE
```

During drag, position updates flow through the presence stream only — no Postgres write.
On drop, the final position commits to Postgres and Electric syncs it back. Other clients
show a ghost/preview from the presence stream during drag, then transition cleanly to the
committed Electric position on drop.

```ts
canvas.on('dragmove', (entityId, x, y) => {
  // Presence stream only — no Postgres write
  presenceStream.write({ type: 'cursor', payload: { entityId, x, y }, ... })
})

canvas.on('dragend', (entityId, x, y) => {
  releaseLock(entityId)
  locationUpdate(locationId, { coordinate: { x, y } })
    .then(({ txid }) => locationCollection.utils.awaitTxId(txid))
})

// Receiving client: show ghost from presence, clear on Electric sync
presenceStream.subscribe((events) => {
  for (const e of events) {
    if (e.type === 'cursor' && e.userId !== currentUserId) {
      setGhostPosition(e.payload.entityId, { x: e.payload.x, y: e.payload.y })
    }
  }
})
locationCollection.on('change', (id) => clearGhostPosition(id))
```

### SSE mode

Enable SSE on shape streams to push committed changes immediately rather than waiting
for the next long-poll cycle. With SSE, WAL → Electric → client is typically 50–150ms:

```ts
const locationStream = new ShapeStream({
  url: '/api/shapes/locations',
  params: { workspaceId },
  liveSse: true
})
```

Electric's client automatically falls back to long-polling if SSE is not working (e.g.,
due to proxy buffering) after 3 consecutive failures within 1 second.

### Column projection

The canvas view only needs spatial data. Project down to what the renderer needs:

```ts
electricUrl.searchParams.set('columns', 'id,x,y,workspace_id,date')
```

Electric's `replica: 'default'` (the default) already sends only changed columns on
updates — a position change sends only `x` and `y`, not the full row.

### Workspace-scoped shapes

Move from garden-scoped to workspace-scoped shapes to reduce the data set for a single
editing session:

```ts
// Proxy: workspace-scoped locations
where = `garden_id = '${gardenId}' AND workspace_id = '${workspaceId}'`

// Proxy: workspace-scoped geometries via subquery
where = `id IN (
  SELECT geometry_id FROM planting_areas WHERE workspace_id = '${workspaceId}'
)`
```

When the user switches workspaces, the collection ID changes, TanStack DB discards the
old collection, and a fresh workspace-scoped shape starts. Smaller initial sync, faster
live query results.

---

## Offline and local-first

### What the stack gives for free

Electric shapes are resumable from an offset. On reconnect — whether after 5 seconds or
5 days — the client sends its last known offset:

```
GET /api/shapes/locations?offset=<lastSeen>&handle=<shapeHandle>
```

Electric responds with only changes since that offset. No full re-fetch. The client
catches up efficiently regardless of how long it was offline. TanStack DB collections
hold synced data in memory and serve reads even while offline.

### What needs to be added for full offline support

**1. Persist shape state to IndexedDB**

Store the collection snapshot and the Electric offset/handle in IndexedDB. On load,
hydrate the collection from the snapshot first (instant data from cache), then resume the
shape from the stored offset (catch-up sync of only what changed while offline).

**2. Persist the mutation queue to IndexedDB**

Writes made offline need to survive a page refresh. Queue pending mutation payloads in
IndexedDB and flush them in order on reconnect. TanStack DB's optimistic state persists
these visually until the queued mutations resolve.

### The offline reconciliation problem

When reconnecting after offline edits, queued mutations fire against the current server
state, which may have changed. Electric's shape catch-up delivers concurrent changes from
other clients. For most garden planning operations — edits to independent objects, adding
observations to different dates — LWW is acceptable in practice because conflict rate is
naturally low.

Concurrent edits to the same object (two users moving the same planting area while one
was offline) require CRDT semantics to merge correctly. This is where the Yjs layer
becomes necessary rather than optional.

### Yjs for offline spatial editing

The Yjs IndexedDB provider persists the Yjs document locally. Offline Yjs updates
accumulate in the local document and survive page refresh. On reconnect, the Durable
Streams Yjs provider syncs by exchanging update vectors — each side sends what the other
missed. Because Yjs updates are CRDTs, offline edits to `linesCoordinates` (Y.Array of
points) merge with online edits from other clients without either side losing work.

### The Electric offset as the key primitive

The offset mechanism is what makes reconnection viable without full CRDT semantics on
the main data path. The delta sync from a stored offset is cheap enough that most offline
scenarios (minutes to hours) result in fast catch-up rather than a full re-fetch.
Paired with IndexedDB persistence of the snapshot and offset, the app can serve data
instantly on load from local cache and sync updates in the background — the core
local-first experience even without full CRDT conflict resolution everywhere.

### Summary of the full offline picture

```
                    ONLINE                         OFFLINE
Reading:    Electric shape stream              IndexedDB snapshot (stale by offline duration)
                    ↓                                  ↓
              TanStack DB collection  ←————————  Hydrated on load, then catch-up sync on reconnect

Writing:    mutationFn → API → Postgres        Queued in IndexedDB, flush on reconnect
                    ↓                                  ↓
              Optimistic state (memory)         Optimistic state (persisted in IndexedDB)

Spatial:    Yjs doc ← Durable Streams          Yjs doc (IndexedDB provider)
            CRDT merge in real-time             CRDT merge on reconnect

Presence:   Presence stream (live)              Resumed from offset on reconnect
```

---

## Alternative architectures: conflict resolution and real-time

### What Triplit gave that we lost

Triplit's CRDT foundation provided:

- **Commutative set operations** — two clients adding different items to a set both win;
  neither overwrites the other
- **Per-field vector clocks** — concurrent writes to different fields of the same record
  both apply; only writes to the exact same field at the exact same time conflict
- **Offline accumulation** — operations queue locally and merge cleanly on reconnect
  regardless of how long offline
- **Unified simplicity** — one package, schema defined once, real-time sync happened
  automatically, permissions declared alongside schema

What we now have instead is row-level last-write-wins (the last Postgres transaction to
commit wins entirely), with a significantly more complex stack of moving parts:
Drizzle schema, Zod command schemas, controllers, shape proxy routes, TanStack DB
collections, Electric service, and a separate presence layer still needed.

---

### Zero (Rocicorp)

Zero is the closest direct alternative to Triplit with a better conflict story. It is
Postgres-backed, TypeScript-first, and designed explicitly for collaborative data-intensive
applications.

**How it works:**

Zero maintains a client-side cache (backed by SQLite in the browser) synced from
Postgres. Queries run against the local cache — sub-millisecond, reactive. Mutations are
defined as TypeScript functions called "mutators" that run twice: once optimistically on
the client (instant UI) and once authoritatively on the server. The server result
replaces the client's optimistic result; if they differ, the client reconciles.

```ts
// Mutator defined once, runs on both client and server
const mutators = {
  async updateLocation(tx, { id, x, y }: { id: string; x: number; y: number }) {
    await tx.update('locations', { x, y }, { id })
  }
}

// Client usage — instant, optimistic
await zero.mutate.updateLocation({ id: 'loc-123', x: 142, y: 87 })
```

**Conflict model:** deterministic mutators mean the client's optimistic state is always
consistent with what the server will produce. Snap-back only happens if the server
rejects the mutation entirely (authorization failure, constraint violation) — not from
concurrent writes landing in a different order. Two concurrent writes to different rows
both succeed. Two concurrent writes to the same field still have one winner, but the
losing client's optimistic state was already correct (the mutator function is
deterministic), so the reconciliation is invisible rather than a visual snap-back.

**Compared to our stack:**

| | Our stack | Zero |
|---|---|---|
| Read path | Electric shapes → proxy → TanStack DB | Zero cache (SQLite) → reactive queries |
| Write path | Controller per operation | Mutator per operation (runs client + server) |
| Real-time | Electric WAL streaming | Zero's own sync protocol |
| Conflict | Row-level LWW | Deterministic mutators (less snap-back) |
| Offline | Needs IndexedDB adapter | Built-in |
| Schema | Drizzle (server) + Zod commands | Zero schema (shared) |
| Presence | Needs Durable Streams separately | Needs separately |
| Complexity | High — many distinct layers | Medium — more unified |
| Postgres fidelity | Full (Drizzle, migrations, raw SQL) | Full (Zero syncs from Postgres) |
| Status | Electric stable, TanStack DB new | Zero newer, less battle-tested |

Zero does not have CRDTs. Its advantage over our stack is the deterministic mutator
model which eliminates most visible snap-backs, not true merge semantics.

---

### Convex

Convex is a reactive backend platform where the database, real-time sync, and server
functions are a unified service.

**How it works:**

Queries are TypeScript functions that subscribe to data — they re-run automatically
when underlying data changes. Mutations are TypeScript functions that run in a
transaction on the server. The client calls them like local functions; Convex handles
optimistic updates, real-time propagation to all subscribed clients, and consistency.

```ts
// Query — automatically reactive across all clients
export const getPlantingAreas = query({
  args: { workspaceId: v.string() },
  handler: async (ctx, { workspaceId }) => {
    return ctx.db.query('plantingAreas')
      .withIndex('by_workspace', (q) => q.eq('workspaceId', workspaceId))
      .collect()
  }
})

// Mutation — transactional, optimistic, automatically propagated
export const moveArea = mutation({
  args: { locationId: v.string(), x: v.number(), y: v.number() },
  handler: async (ctx, { locationId, x, y }) => {
    await ctx.db.patch(locationId, { x, y })
  }
})
```

**Conflict model:** all mutations run inside transactions on Convex's servers. Concurrent
mutations are serialized. The optimistic update on the client uses the exact same
mutation function (run locally in a sandbox), so the optimistic and authoritative results
are always consistent.

**Compared to our stack:**

| | Our stack | Convex |
|---|---|---|
| Simplicity | Low (many layers) | Very high (one service, one client) |
| Real-time | Electric WAL streaming | WebSocket, built-in |
| Conflict | Row-level LWW | Serialized transactions |
| Offline | Needs IndexedDB adapter | Limited |
| Postgres | Full control | Not Postgres (Convex DB) |
| Migrations | Drizzle migrations | Schema evolution via functions |
| Raw SQL | Yes (Drizzle) | No |
| CRDTs | No (Yjs separately) | No |
| Self-hosted | Yes (Electric + Postgres) | Convex Cloud or self-hosted |
| Vendor lock-in | Low | High |

The fundamental cost of Convex is leaving Postgres. Recursive CTEs for cultivar
inheritance, jsonb operations for attributes, array columns for membership — all of these
require Postgres specifically. Convex has its own database with its own query model.

---

### InstantDB

InstantDB is a triple-store database (entity-attribute-value) inspired by Datomic, with
real-time sync built in from the start.

**How it works:**

Data is stored as triples: `(entity-id, attribute, value)`. Each attribute update is an
independent fact. Two clients updating different attributes of the same entity both win
because they're separate triples — not a row-level replacement. This gives CRDT-like
semantics for attribute-level writes without an explicit CRDT implementation.

```ts
const { data } = db.useQuery({
  plantingAreas: {
    $: { where: { workspaceId: workspaceId } },
    location: {},     // joined relation
    geometry: {}
  }
})

db.transact([
  tx.locations[locationId].update({ x: 142, y: 87 })
])
```

**Conflict model:** last-write-wins per attribute, not per row. Two concurrent edits to
`location.x` and `location.y` independently both apply. Two concurrent edits to the same
attribute still have one winner, but attribute-level granularity means conflicts at the
semantic level are rarer.

**Compared to our stack:**

| | Our stack | InstantDB |
|---|---|---|
| Conflict granularity | Row-level LWW | Attribute-level LWW |
| Simplicity | Low | High |
| Real-time | Electric WAL streaming | WebSocket, built-in |
| Query model | SQL (Drizzle) + TanStack DB | Datalog-inspired, graph queries |
| Postgres | Yes | No (triple-store) |
| Offline | Needs work | Built-in |
| CRDTs | No | Partial (attribute independence) |
| Schema | Explicit (Drizzle) | Flexible (declared schema) |

The triple-store model is a different mental model than relational. Complex queries
involving date ranges, aggregates across the geometry history structure, and the
cultivar inheritance chain don't map as naturally as SQL.

---

### PowerSync

PowerSync syncs a Postgres (or other SQL) backend to a client-side SQLite database.

**How it works:**

The client has a real SQLite database — full SQL queries, indexes, the works. A
PowerSync service layer sits between Postgres and the client, managing sync rules and
change propagation. Writes go back to Postgres via your API (similar to our controllers).

**Conflict model:** server wins. Identical to our current stack. No CRDTs.

**Where it differs:** the client query layer is real SQLite rather than TanStack DB's
in-memory store. This gives recursive queries, complex joins, and aggregates that run
client-side with full SQL expressiveness — including the cultivar inheritance resolution
via recursive CTEs, which would run client-side against the synced data naturally.

**Compared to our stack:**

| | Our stack | PowerSync |
|---|---|---|
| Client query | TanStack DB (in-memory, differential) | SQLite (full SQL) |
| Conflict | LWW | LWW (server wins) |
| Offline | Needs IndexedDB adapter | Built-in (SQLite is local) |
| Real-time latency | Electric (very fast) | PowerSync (slightly slower) |
| Postgres | Yes | Yes |
| Write path | Our controllers | Your API (same pattern) |
| Cultivar resolution | Client needs reimplementation | Recursive CTE runs in client SQLite |

PowerSync is an honest alternative if full offline and client-side SQL are more important
than the fastest possible real-time sync. It would not solve the CRDT/conflict problem.

---

### Livestore

Livestore is a new (2025) local-first framework from Johannes Schickling (Prisma
co-founder) based on event sourcing.

**How it works:**

All state changes are represented as immutable events appended to a log. State is derived
by replaying the event log. Events replicate across clients. Because events are
append-only, there's no write conflict at the data level — every client eventually has
the same event log and derives the same state. Conflicts are semantic (two events
representing contradictory intent) rather than structural.

```ts
// All writes are events
store.commit(events.movePlantingArea({ id: 'pa-123', x: 142, y: 87 }))
store.commit(events.addObservation({ entityIds: ['pa-123'], date: '2025-04-14', data: {} }))

// State is a live query over the event log
const areas = store.query(PlantingAreaState.forWorkspace(workspaceId))
```

**Conflict model:** structurally conflict-free (events always append). Semantically,
"last event wins" for derived scalar state — but at event granularity, not row granularity.
Two offline clients both adding different observations produce two events that both
persist when they sync.

**Compared to our stack:**

| | Our stack | Livestore |
|---|---|---|
| Conflict | Row-level LWW | Event-level (semantically richer) |
| Offline | Needs IndexedDB adapter | Built-in (event log is local) |
| Real-time | Electric WAL | Livestore sync |
| Postgres | Yes | Event log in SQLite / Postgres |
| Schema evolution | Drizzle migrations | Event schema versioning |
| Complexity | High (many layers) | Medium (new mental model) |
| Maturity | Electric stable, TanStack DB new | Very new |
| Cultivar resolution | Client reimplementation or API | Derived state from events |

Event sourcing is a genuine shift in how you model the domain — instead of "what is the
current position of planting area 123" you think "what events have happened to planting
area 123." This maps well to a garden management domain (planting, observation, harvest
events) but requires rebuilding the data model around events.

---

### Honest recommendation

**If staying on this stack (Electric + TanStack DB + Drizzle):** augment with Yjs via
Durable Streams for the spatial canvas layer. Accept LWW for non-spatial data. Add the
IndexedDB persistence adapter for offline. The result is the best Postgres fidelity and
the most control, at the cost of the most complexity.

**If starting fresh prioritizing simplicity and conflict resolution:** Zero is the
closest to the Triplit experience with better real-time and a cleaner conflict model, while
keeping Postgres as the backend. The mutator model (deterministic functions run on both
client and server) eliminates most visible snap-backs without requiring CRDTs.

**If prioritizing true CRDT semantics throughout:** Livestore's event sourcing approach
is the most principled solution, at the cost of a significant mental model shift and
early-stage maturity risk.

**If prioritizing simplicity above all else and willing to leave Postgres:** Convex is
the simplest full-stack real-time option with serialized transactions giving clean
consistency guarantees. The cost is vendor lock-in and losing the SQL/Postgres toolchain.

The honest assessment of our current migration: we gained Postgres fidelity, scalability
via Electric's CDN-cacheable shapes, and a clean separation between read and write paths.
We lost Triplit's unified simplicity and CRDT-based conflict resolution. The augmentation
path (Yjs for spatial, IndexedDB for offline) recovers most of what was lost for the
highest-value cases, without replacing the stack again.
