# Jazz Migration Reference

Planning reference for migrating the Verdagraph data layer from Triplit to Jazz. Covers architectural decisions, patterns, and their tradeoffs as discussed.

---

## Table of Contents

1. [Key Architectural Differences](#1-key-architectural-differences)
2. [Authentication](#2-authentication)
3. [Schema and Naming Conventions](#3-schema-and-naming-conventions)
4. [Garden Role System vs Jazz Permissions](#4-garden-role-system-vs-jazz-permissions)
5. [Garden Visibility Enforcement](#5-garden-visibility-enforcement)
6. [Global Garden Index](#6-global-garden-index)
7. [Creator Succession](#7-creator-succession)
8. [Invite System vs Request-to-Join](#8-invite-system-vs-request-to-join)
9. [Graph Data Model Architecture](#9-graph-data-model-architecture)
10. [Temporal Filtering](#10-temporal-filtering)
11. [Observations and Polymorphic Entity References](#11-observations-and-polymorphic-entity-references)
12. [Attribute Schemas](#12-attribute-schemas)
13. [Command Schemas and Validation](#13-command-schemas-and-validation)
14. [Search and Discovery](#14-search-and-discovery)
15. [CoValue Size and Performance](#15-covalue-size-and-performance)

---

## 1. Key Architectural Differences

| Concern          | Triplit                                           | Jazz                                       |
| ---------------- | ------------------------------------------------- | ------------------------------------------ |
| Query model      | Server-side filtered queries (`WHERE`, `INCLUDE`) | Client-side graph traversal from known IDs |
| Permissions      | Server-enforced filter rules per role             | Cryptographic Group membership             |
| Offline          | Partial (server required for auth)                | Full offline after first login             |
| Discovery        | Query all entities matching a condition           | Requires an explicit index CoValue         |
| Pagination       | Native query cursors                              | Manual sharding; no built-in pagination    |
| Foreign keys     | `gardenId` on child entities                      | Parent holds list/record of children       |
| Schema evolution | Add fields to collections                         | Add fields to CoMaps only; never remove    |

**Jazz is a graph database, not a relational one.** All data is reachable by traversing CoValue references from a known root (the user's account). There is no equivalent of `SELECT * FROM plants WHERE gardenId = X`.

---

## 2. Authentication

### Offline behaviour

BetterAuth (and Clerk) are **not fully local-first**:

- **First login / signup**: Requires server. Jazz retrieves the user's account keys from BetterAuth.
- **After first login**: Account keys are cached locally. Full offline operation is available.
- **New users offline**: Blocked at signup. Cannot create an account without a server connection.

### Account recovery

Jazz uses a **BIP39-style passphrase** (wordlist-based) derived from the account's cryptographic keys as the universal recovery mechanism. It works regardless of the original auth method (passkey, BetterAuth, Clerk, etc.).

- The passphrase **cannot be changed** — it is derived from the private key.
- If compromised, there is no revocation mechanism.
- Users should be shown their recovery passphrase during onboarding and advised to store it securely.

### Multiple auth methods

Auth methods can be layered on a single account. Recommended priority order:

1. BetterAuth (email/password) — primary, online
2. Passkey — device-level, local-first
3. Recovery passphrase — offline fallback, permanent

If all methods are lost, the account's data is permanently inaccessible.

### BetterAuth compatibility matrix (Jazz plugin)

| Method                                                   | Jazz plugin |
| -------------------------------------------------------- | ----------- |
| Email/Password                                           | ✅          |
| Social Providers                                         | ✅          |
| Email OTP                                                | ✅          |
| Username, Anonymous, Phone, Magic Link, Passkey, One Tap | ❓ untested |

---

## 3. Schema and Naming Conventions

### CoValue class vs type

Jazz's `co.map()` etc. produce classes, not just schemas. The convention is:

```ts
// Class (the definition)
const UserProfileSchema = co.profile({ name: z.string() });

// Type (the loaded instance)
type UserProfile = co.loaded<typeof UserProfileSchema>;
```

`Schema` suffix on the class, bare name on the type. This mirrors existing Triplit convention and is consistent with `Entity<>` types.

### Single `z` import

Jazz re-exports Zod v4 from `jazz-tools`. Use this `z` everywhere — in CoValue schemas and in command schemas. Drop the `zod` v3 package dependency.

```ts
// In both schema.ts and commands.ts
import { z } from 'jazz-tools';
```

### Validation constraints

**Do not put validation constraints (`.min()`, `.max()`, `.regex()`) in CoValue schemas.** Jazz's runtime validation is opt-in and warns by default (as of 0.20.10) — it is not suitable as a form validation layer. CoValue schemas carry structural types only; commands carry constraints.

```ts
// schema.ts — structural only
const GardenSchema = co.map({
	name: z.string(),
	visibility: z.enum(GardenVisibilityEnumOptions)
});

// commands.ts — full validation
const gardenNameField = z.string().trim().min(1).max(100);
```

To opt into strict enforcement globally (throws on invalid writes):

```ts
import { setDefaultValidationMode } from 'jazz-tools';

setDefaultValidationMode('strict');
```

---

## 4. Garden Role System vs Jazz Permissions

### Role mapping

| App role | Jazz Group role | Description                                                    |
| -------- | --------------- | -------------------------------------------------------------- |
| Creator  | `admin`         | One per garden. Cannot be removed by others. Permanent.        |
| `ADMIN`  | `manager`       | Can add/remove writers and readers. Cannot add other managers. |
| `EDITOR` | `writer`        | Content changes. No membership management.                     |
| `VIEWER` | `reader`        | Read-only.                                                     |

### Key Jazz role constraints

- **Admins cannot be removed by others** — they must leave the group themselves.
- **Managers cannot add other managers** — only `admin` (the creator) can elevate to `manager`.
- **Managers can add/remove** `writer` and `reader` roles.

This means: if you want app ADMINs to be able to promote other members to ADMIN, that is not expressible in Jazz's role model. App ADMINs (`manager`) can manage EDITORs and VIEWERs only.

### GardenMembership CoValue

Jazz Group membership controls access. The `GardenMembershipSchema` CoValue stores supplementary app-level state alongside it. **Both must be kept in sync manually** — Jazz does not link them.

```ts
const GardenMembershipSchema = co.map({
	user: co.account(),
	role: z.enum(['ADMIN', 'EDITOR', 'VIEWER']),
	status: z.enum(['CREATED', 'PENDING', 'ACCEPTED']),
	acceptedAt: z.date(),
	favorite: z.boolean(),
	inviterId: z.string().nullable()
});
```

When a member is removed from the Jazz Group, the corresponding `GardenMembership` record must also be updated/deleted by the controller.

---

## 5. Garden Visibility Enforcement

### Two-layer model

Visibility is not a query filter in Jazz — it must be enforced at two independent layers:

**Layer 1 — Access control (Jazz Group membership):**

| Visibility | `"everyone"` on Group                   |
| ---------- | --------------------------------------- |
| `HIDDEN`   | Not added                               |
| `UNLISTED` | `group.addMember("everyone", "reader")` |
| `PUBLIC`   | `group.addMember("everyone", "reader")` |

**Layer 2 — Discoverability (Global Garden Index CoValue):**

| Visibility | In `GardenIndexSchema` |
| ---------- | ---------------------- |
| `HIDDEN`   | No                     |
| `UNLISTED` | No                     |
| `PUBLIC`   | Yes                    |

`UNLISTED` and `PUBLIC` are identical at the access control layer. The distinction is purely whether the garden appears in the discoverable index.

### Visibility transition matrix

When a user changes visibility, the controller must update both layers:

| From → To             | Group change               | Index change      |
| --------------------- | -------------------------- | ----------------- |
| `HIDDEN` → `UNLISTED` | Add `"everyone": "reader"` | —                 |
| `HIDDEN` → `PUBLIC`   | Add `"everyone": "reader"` | Add to index      |
| `UNLISTED` → `HIDDEN` | Remove `"everyone"`        | —                 |
| `UNLISTED` → `PUBLIC` | —                          | Add to index      |
| `PUBLIC` → `HIDDEN`   | Remove `"everyone"`        | Remove from index |
| `PUBLIC` → `UNLISTED` | —                          | Remove from index |

The `visibility` field on `GardenSchema` is the user-facing source of truth. The Group membership and index state are the enforcement mechanisms derived from it.

---

## 6. Global Garden Index

### Purpose

Because Jazz has no server-side query engine, public gardens cannot be discovered by querying. A `GardenIndexSchema` CoValue acts as an explicit directory of all `PUBLIC` gardens.

### Schema

```ts
const GardenIndexSchema = co.record(gardenIdField, GardenSchema);

export const GLOBAL_PUBLIC_GARDEN_INDEX_ID = 'global-public-gardens';
```

- Owned by the **server worker's group**.
- `"everyone": "reader"` on that group — publicly readable.
- Keyed by garden URL slug.
- Values are `GardenSchema` references (not copies).

Use `co.record()` (not `co.map()`) for dynamic string-keyed collections. The docs note `co.record()` supports fast lookup for up to tens of thousands of entries with a shallow load.

### Setup

The index CoValue is created once during server worker initialization using `getOrCreateUnique`:

```ts
// In server worker startup
const gardenIndex = await GardenIndexSchema.getOrCreateUnique(
	GLOBAL_PUBLIC_GARDEN_INDEX_ID,
	{},
	{ owner: serverWorkerGroup }
);
serverWorkerGroup.addMember('everyone', 'reader');
```

### Maintenance

The server worker maintains the index when garden visibility changes:

```ts
// On visibility change to PUBLIC
gardenIndex.$jazz.set(garden.id, garden);

// On visibility change away from PUBLIC
gardenIndex.$jazz.delete(garden.id);
```

### Storing summary metadata

For browsing without deep-loading every garden, store a `z.object()` summary instead of a direct CoValue reference:

```ts
const GardenIndexSchema = co.record(
	gardenIdField,
	z.object({
		name: z.string(),
		description: z.string().nullable(),
		memberCount: z.number(),
		createdAt: z.date()
	})
);
```

This trades navigability (can't follow a reference to the full garden) for load performance (no resolve depth needed).

---

## 7. Creator Succession

### The problem

Jazz `admin` users can only be removed by themselves. Only `admin` can add new `manager`s. If the creator's account becomes inactive, no new admins can be added to the garden.

### Solution: Server worker as permanent co-admin

Add the server worker account as a second `admin` at garden creation time:

```ts
const gardenGroup = Group.create();
gardenGroup.addMember(creatorAccount, 'admin');
gardenGroup.addMember(serverWorkerAccount, 'admin');
```

The server worker exposes a protected API endpoint. A `manager` calls it, the server worker verifies their role, and promotes the nominated account to `manager` on their behalf. The creator is no longer a single point of failure.

### Voluntary transfer

Prompt the creator to promote a trusted manager to `admin` before deactivating their account. This is a UX step, not a reliable safety net on its own.

### Garden fork (escape hatch)

If the creator is already gone and a `manager` needs to take ownership:

1. Create a new `GardenSchema` CoValue with the manager as `admin`.
2. Copy current data into new CoValues under the new Group.
3. The forker becomes the new creator/admin.

**What is lost:** Original CoValue IDs and CRDT history do not transfer. The fork is a snapshot of current state. Consider exposing this as a deliberate "take ownership" or "fork garden" feature.

---

## 8. Invite System vs Request-to-Join

### Jazz invite secrets

`createInviteLink(group, role)` generates a URL fragment:

```
https://yourapp.com/#/invite/[CoValueId]/[inviteSecret]
```

The secret is in the URL fragment and is never sent to the server. The recipient calls `acceptInvite(coValueId, inviteSecret, schema)`.

| Property      | Detail                               |
| ------------- | ------------------------------------ |
| Multi-use     | Yes — the same link works for anyone |
| Expiry        | Never                                |
| Revocable     | No                                   |
| Works offline | No (Group write requires server)     |
| Best for      | Trusted invites to known people      |

Generate per-role secrets: one for `manager`, one for `writer`, one for `reader`.

> **Warning:** Invite links cannot be revoked. If a writer invite link is shared publicly by accident, there is no way to invalidate it. Use request-to-join for public/semi-open gardens.

### Request-to-join

Uses the `writeOnly` role to create a one-way submission channel:

```ts
// Garden has a joinRequests list
// "everyone": "writeOnly" — can submit, cannot read other requests
// Managers: "reader"/"admin" — can review and approve
```

1. Non-member submits a join request (write-only, cannot see other requests).
2. Manager reviews the requests list.
3. Manager approves by calling `group.addMember(account, role)` and creating a `GardenMembership` record.

| Property      | Detail                                |
| ------------- | ------------------------------------- |
| Per-person    | Yes                                   |
| Revocable     | Yes (simply don't approve)            |
| Works offline | No                                    |
| Best for      | Open/semi-open gardens, public signup |

### When to use which

| Garden visibility | Recommended invite method          |
| ----------------- | ---------------------------------- |
| `HIDDEN`          | Invite secrets (known people only) |
| `UNLISTED`        | Invite secrets                     |
| `PUBLIC`          | Request-to-join                    |

---

## 9. Graph Data Model Architecture

### Fundamental shift

In Triplit, child entities reference their parent via a foreign key (`gardenId`). The server queries `WHERE gardenId = X`.

In Jazz, the parent holds references to its children. Navigation goes **downward** through the graph from a known root.

```
UserAccount.root.gardens  →  Garden  →  GardenContent  →  co.list(Workspace)
                                                       →  co.list(Observation)
                                                       →  (future features)
```

### Account root

The user's account root is the entry point for all their data:

```ts
const UserRootSchema = co.map({
	gardens: co.list(GardenSchema)
});
```

### GardenContent pattern

To keep `GardenSchema` stable as features expand, place all domain-specific content behind a `GardenContextSchema`:

```ts
const GardenContextSchema = co.map({
	workspaces: co.list(WorkspaceSchema),
	environments: co.list(EnvironmentSchema),
	cultivarCollections: co.list(CultivarCollectionSchema)
	// New features: add one field here
});

const GardenSchema = co.map({
	context: GardenContextSchema, // stable reference, content grows here
	name: z.string(),
	description: co.plainText(),
	memberships: co.list(GardenMembershipSchema)
});
```

**Adding a new domain:** add one field to `GardenContextSchema`. No changes to `GardenSchema`. No loading pattern changes.

### Schema evolution rules

- **Only ever add fields — never remove or rename them.**
- New fields must be nullable/optional so old CoValues without them remain valid.
- Initialize new fields at garden creation time.
- Handle `undefined` (field never set) vs `null` (intentionally empty) in application code.

---

## 10. Temporal Filtering

### The problem

Triplit supports server-side date range filtering: `WHERE beginDate >= X AND endDate <= Y`. Jazz has no equivalent. All filtering happens client-side after loading.

### Chosen approach: Summary fields + two-phase loading

Store denormalized activity date range fields as primitives on each entity. This enables cheap client-side filtering before any deep loading occurs.

```ts
const PlantSchema = co.map({
	// ... other fields
	firstActivityAt: z.date().nullable(), // maintained on every write to observations/histories
	lastActivityAt: z.date().nullable() // maintained on every write to observations/histories
});
```

**Loading pattern:**

```ts
// Phase 1: shallow load — all plants, primitive fields only (no nested CoValues)
const gardenState = new CoState(GardenSchema, gardenId, {
	resolve: { context: { plants: { $each: true } } }
});

// Filter client-side using summary fields
const matchingPlantIds = $derived(
	gardenState.current?.context.plants
		?.filter(
			(plant) =>
				plant.firstActivityAt != null &&
				plant.firstActivityAt <= timeline.endSelection &&
				(plant.lastActivityAt == null ||
					plant.lastActivityAt >= timeline.beginSelection)
		)
		.map((plant) => plant.$jazz.id) ?? []
);

// Phase 2: deep load — only matched plants, full nested data
// Managed via $effect + Map<id, CoState> (see plantsContext.svelte.ts pattern)
```

### Maintaining summary fields

`firstActivityAt` and `lastActivityAt` must be updated in the controller every time an observation, location history entry, or geometry history entry is added or removed:

```ts
async function addObservation(plant: Plant, observation: Observation) {
	plant.observations.$jazz.push(observation);
	if (!plant.firstActivityAt || observation.date < plant.firstActivityAt) {
		plant.$jazz.set('firstActivityAt', observation.date);
	}
	if (!plant.lastActivityAt || observation.date > plant.lastActivityAt) {
		plant.$jazz.set('lastActivityAt', observation.date);
	}
}
```

### Escape hatch: temporal buckets per entity

If a single entity accumulates enough history that its flat observation list becomes expensive to load:

```ts
const PlantSchema = co.map({
	firstActivityAt: z.date().nullable(), // summary field preserved
	lastActivityAt: z.date().nullable(),
	observationsByMonth: co.map({
		// 'YYYY-MM' → co.list(ObservationSchema)
		// dynamic month keys
	})
});
```

Load only the month buckets that overlap the selected date range. Apply this selectively to heavy entities only — not preemptively.

---

## 11. Observations and Polymorphic Entity References

### Polymorphic references via shared CoValue IDs

In Triplit, observations reference a generic `entityId`. In Jazz, CoValue references are pointers — the same Observation CoValue can appear in multiple entities' lists without data duplication:

```ts
// One Observation CoValue
const observation = ObservationSchema.create({ ... })

// Referenced from multiple entity lists — same CoValue ID in both
plant.observations.$jazz.push(observation)
workspace.observations.$jazz.push(observation)
```

This preserves the cross-entity observation pattern without a flat garden-level list.

### Entity-level observation lists

Each entity holds its own observation list. This avoids the "load all observations in the garden at once" problem:

```ts
const PlantSchema = co.map({
	firstActivityAt: z.date().nullable(),
	lastActivityAt: z.date().nullable(),
	observations: co.list(ObservationSchema),
	locationHistory: co.list(LocationEntrySchema),
	geometryHistory: co.list(GeometryEntrySchema)
});
```

Loading observations for a plant only loads that plant's observations — not all observations in the garden.

---

## 12. Attribute Schemas

### Chosen approach: `z.object()` inline JSON

Cultivar and environment attributes (e.g. `annualLifeCycle`, `color`, `frostDates`) are stored as plain JSON objects on the parent CoMap, not as nested CoValues.

```ts
const CultivarSchema = co.map({
    name:       z.string(),
    attributes: z.object({
        annualLifeCycle: z.object({
            sowToGerm:           z.number().nullable(),
            germToTransplant:    z.number().nullable(),
            germToFirstHarvest:  z.number().nullable(),
            firstToLastHarvest:  z.number().nullable(),
        }).nullable(),
        color: z.object({
            baseColor:    z.string().nullable(),
            outlineColor: z.string().nullable(),
            textColor:    z.string().nullable(),
        }).nullable(),
        frostDatePlantingWindows: z.object({
            lastFrostWindowOpen:  z.number().nullable(),
            lastFrostWindowClose: z.number().nullable(),
            firstFrostWindowOpen: z.number().nullable(),
            firstFrostWindowClose: z.number().nullable(),
        }).nullable(),
        expectedGeometry: z.object({ ... }).nullable(),
        origin:           z.object({ ... }).nullable(),
    })
})
```

### Why `z.object()` over nested CoMaps

| Concern                     | `z.object()`                        | nested `co.map()`                                                 |
| --------------------------- | ----------------------------------- | ----------------------------------------------------------------- |
| Extra CoValues per cultivar | 0                                   | 5 (one per attribute group)                                       |
| Resolve depth required      | None                                | Yes — each group must be resolved                                 |
| Concurrent edit conflicts   | Last-write-wins on `attributes` key | Per-field CRDT within each group                                  |
| Adding a new attribute type | Add one nullable key                | Add one `co.optional()` field + update resolve queries everywhere |

Concurrent per-field editing of attribute groups is not a realistic use case for cultivar data. The `z.object()` approach is simpler, cheaper, and more horizontally scalable.

### Horizontal scalability

Adding a new attribute type requires:

1. New file `cultivars/attributes/newAttribute/schema.ts` — the Zod shape.
2. One new nullable line in the `attributes` `z.object()`.
3. One new optional field in `CultivarAttributesUpdateCommandSchema`.

Old cultivars automatically have `null` for new attribute groups. No migration, no loading changes, no resolve query updates.

---

## 13. Command Schemas and Validation

### The commands pattern survives Jazz

Command schemas remain the primary validation layer. In Jazz there is no server-side validation — writing to a CoValue is immediate. Commands are the only guard before mutation.

```ts
// commands.ts — validation before CoValue mutation
const GardenCreateCommandSchema = z.object({
	name: gardenFields.gardenNameField,
	description: gardenFields.gardenDescriptionField.default(''),
	visibility: gardenFields.gardenVisibilityField.default('HIDDEN')
});

// controller
async function createGarden(input: unknown) {
	const command = GardenCreateCommandSchema.parse(input); // throws if invalid
	const garden = GardenSchema.create({ ...command }, { owner: gardenGroup });
}
```

### `applyDiff` simplifies update controllers

Instead of setting each field individually, pass the validated command to `applyDiff`:

```ts
// Before
if (validated.name !== undefined) cultivar.$jazz.set('name', validated.name);
if (validated.description !== undefined)
	cultivar.$jazz.set('description', validated.description);

// After
cultivar.$jazz.applyDiff(validated); // applies only provided keys
```

`applyDiff` accepts a partial plain object matching the CoValue schema shape — exactly what an update command produces after parsing.

### What changes from current commands

| Command                                    | Change                                                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| `GardenCreateCommandSchema`                | Remove `id` (Jazz assigns CoValue IDs). Garden slug becomes a regular field.                            |
| `GardenMembershipCreateCommandSchema`      | Replace username invite arrays with role-specific invite secret generation or direct account ID lookup. |
| `GardenMembershipDeleteCommandSchema`      | Becomes `group.removeMember(account)` + membership record deletion. No command schema needed.           |
| Attribute update commands                  | Unchanged — still replace the whole `z.object()` group.                                                 |
| Cross-field validation (password matching) | Unchanged — still only expressible in commands, not CoValue schemas.                                    |

---

## 14. Search and Discovery

Jazz has no server-side query engine. There is no `WHERE name LIKE '%query%'`.

### Option 1: Client-side filter (current scale)

The `GardenIndexSchema` is fully loaded on the client. Filter in memory:

```ts
const results = Object.values(gardenIndex).filter((g) =>
	g.name.toLowerCase().includes(query.toLowerCase())
);
```

Works immediately, works offline, zero extra infrastructure. Adequate for hundreds of public gardens.

### Option 2: CoVectors for semantic search

Jazz has a built-in `co.vector()` type for storing embedding vectors. Rank by cosine similarity on-device:

```ts
const GardenIndexEntrySchema = co.map({
	name: z.string(),
	description: z.string().nullable(),
	embedding: co.vector(384) // generated from name + description
});
```

Generate embeddings locally via Transformers.js (~23MB for `Xenova/all-MiniLM-L6-v2`) so search works offline. Regenerate when the garden name or description changes (CoVectors are immutable — create a new one and replace the reference).

### Option 3: External search index (large scale)

For fuzzy/ranked full-text search at scale: maintain a Meilisearch or Typesense index fed by the server worker. Search queries go to the external service; Jazz loads the CoValue once you have the ID back.

Breaks local-first for search only. Data lives in Jazz; only the search index lives externally.

### Recommended progression

| Scale                                  | Approach                                      |
| -------------------------------------- | --------------------------------------------- |
| < ~500 public gardens                  | Client-side filter on index                   |
| Hundreds–thousands                     | Add `co.vector()` embeddings to index entries |
| Thousands+ needing fuzzy/ranked search | External search service fed by server worker  |

---

## 15. CoValue Size and Performance

### CoValues are loaded as a unit

There is no partial load of keys within a CoMap or items within a CoList. Every client subscribing to a CoValue receives it entirely. Resolve depth controls which _nested CoValues_ are loaded, not which fields within a CoValue.

### Pagination

**There is no built-in pagination.** The workaround is manual sharding — splitting a large collection across multiple CoValues and loading them lazily:

```
GardenPublicIndexRoot  (always loaded, tiny)
  ├── recentShard      (last 100 entries)
  ├── alphabeticalShards: { 'a': CoRecord, 'b': CoRecord, ... }
  └── categoryShards:     { 'vegetables': CoRecord, ... }
```

Load the root eagerly; load individual shards lazily as the user navigates.

### Performance guidelines (from Jazz docs)

| Pattern                      | Recommendation                                                                           |
| ---------------------------- | ---------------------------------------------------------------------------------------- |
| Collaborative text fields    | `co.plainText()` for character-level collaboration; `z.string()` for names/URLs (faster) |
| Infrequently-updated objects | `z.object()` instead of nested `co.map()` — replaced atomically, no CoValue overhead     |
| Coordinate/position data     | `z.object({ x, y })` or `z.tuple([x, y])` — not a CoMap                                  |
| Group extension chains       | Keep shallow — deep chains slow permission resolution                                    |
| Crypto                       | Node-API crypto (server) > WASM crypto (edge/browser)                                    |

### Runtime validation mode

As of Jazz 0.20.10, Zod constraint validation on CoValue writes is opt-in:

```ts
import { setDefaultValidationMode } from 'jazz-tools';

setDefaultValidationMode('strict'); // throw on invalid writes
setDefaultValidationMode('warn'); // console.warn (default)
setDefaultValidationMode('loose'); // silent
```

Do not rely on `strict` mode as the primary validation layer for form input — validation runs on every keystroke during live editing. Use command schemas for form validation; use `strict` mode as a development-time safety net only.
