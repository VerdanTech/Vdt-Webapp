# Migration Notes: `migrate-data-layer-jazz2`

Reference document for the Triplit → Jazz migration.

---

## Objectives

- All `packages/models` domain schemas converted from Triplit DSL to Jazz `s.table()` DSL.
- All domain permission files created (`gardens`, `observations`, `workspaces`, `environments`, `cultivars`, `plants`) using the Jazz `policy` API. This replaces the Triplit API which is defined inline with the schema. All role and permission structure should be functionally the same.
- All controllers updated from `ctx.triplit.*` to `ctx.db.*` / `ctx.jazz.*`.
- `triplit/schema.ts` deleted.
- `ControllerContextParams` changed from `{ triplit, getClient(triplit) }` to `{ db, jazz, getClient(db) }`.
- Cultivar and environment attribute `schema.ts` files removed — profile types are now `z.infer<>` from their command schemas; `s.json(CommandSchema)` is used on the relevant JSON columns in Jazz schemas.

All design decisions should be identified and reviewed by the user.

---

## Technical gotchas

### `RowOf<>` returns `never` on domain schema objects

`RowOf<T>` is defined as:
```typescript
type RowOf<TTable> = TTable extends { readonly _rowType: infer TRow } ? TRow : never;
```

`_rowType` is only present on a fully composed `Table` type — the kind returned by `app.tableName` after `s.defineApp(schema)`. Domain schemas defined in separate files produce `DefinedTable` from `s.table()`, which does not carry `_rowType`, so `RowOf<typeof localSchema.tableName>` always returns `never`.

Using `RowOf<typeof jazz.cultivars>` would technically work, but `jazz` is defined in `schema.ts` which imports all domain schemas — creating a circular import from any domain schema file back to `schema.ts`.

To solve this, a seperate types.ts file is required which imports the app and creates the types, similar to how the permissions files must work.

---

### Jazz timestamps are `Date | number`

Jazz timestamp columns (`s.timestamp()`) return `Date | number` at runtime, not `Date` alone. All functions in `workspaces/utils.ts` that previously used `T extends { date: Date }` were updated to `T extends { date: Date | number }` with a normalizer:

```typescript
function toMs(date: Date | number): number {
    return typeof date === 'number' ? date : date.getTime();
}
```

**TODO: Confirm this in the Jazz docs or by inspection.** It was inferred from TypeScript errors during the migration (`Date` was not assignable to `Date | number` union), not from explicit documentation. The runtime behaviour should be verified — it's possible that timestamps are always returned as one type and the union reflects what is *accepted* on insert rather than what is *returned* on read.

Answer: s.timestamp() is documented as Date | number. We would like to store things as date. We may still need the normalizer to make it type safe but it shouldn't be necessary at runtime.

---

### Jazz permissions: cross-table existence checks

The Jazz `policy` API requires inline `anyOf([...])` calls when checking membership across tables. A shared helper function with a typed row parameter does not work because TypeScript cannot narrow the row type through the helper boundary:

```typescript
// Does not work — TypeScript infers row as `unknown` inside the helper
function isAdminOrEditor(gardenId: string) {
    return (row: { gardenId: unknown }) => anyOf([
        policy.gardens.exists.where({ id: gardenId, adminIds: { contains: session.userId } }),
        ...
    ]);
}

// Works — row type is inferred correctly inline
policy.observations.allowInsert.where((row) =>
    anyOf([
        policy.gardens.exists.where({ id: row.gardenId, adminIds: { contains: session.userId } }),
        policy.gardens.exists.where({ id: row.gardenId, editorIds: { contains: session.userId } })
    ])
);
```

Investigate whether Jazz's permission API supports a typed helper via generics — or if another solution can be found.

---

### Jazz transaction API

The transaction API (from Jazz docs) is:

```typescript
const result = await db.transaction(async (tx) => {
    tx.insert(app.todos, { title: "Draft copy", done: false });
    const stagedDrafts = await tx.all(app.todos.where({ done: false }));
    tx.update(app.todos, todoId, { done: true });
});
await result.wait({ tier: "edge" });
```

---

### Garden IDs: user-supplied slugs

Gardens use a URL-friendly user-supplied slug as their ID (e.g. `"my-garden"`). Jazz's `insert` type (`InsertOf<T>`) does not include `id` in its input — IDs are auto-generated. One solution found was an `as any` cast:

```typescript
tx.insert(ctx.jazz.gardens, { id: data.id, ... } as any);
```

**How this was determined:** the TypeScript compiler rejected the `id` field in the insert payload with a type error. The cast was used to suppress this. It was described as a "known limitation pending a cleaner API" but this is speculation — it was not confirmed in any Jazz issue tracker or documentation.

**Before using this pattern on a new branch:** check the Jazz docs or source for an explicit way to supply a custom ID on insert. It is possible there is an option, or that the intended pattern is to generate a deterministic ID externally and pass it differently. The `as any` cast bypasses type safety in a way that could break silently if the underlying API changes. Confirmation is required via human intervention to ask this question on a discord if one cannot be obtained from the docs.

---

## Better Auth integration: blocked, needs direction

Schema generation for the Jazz adapter is currently blocked by a chicken-and-egg dependency:

1. `@better-auth/cli generate` needs `auth.ts` to configure `jazzAdapter({ schema: jazz.wasmSchema })`.
2. `jazz.wasmSchema` comes from `s.defineApp(appSchema)`.
3. `appSchema` must include the Better Auth tables (users, sessions, accounts, etc.).
4. Those tables are only known after the CLI generates the schema.

The function `buildJazzSchemaSourceTextFromTables` exists in `jazz-tools/dist/better-auth-adapter/schema.js` and could be called directly using `(await auth.$context).tables`, but it is not exported via the package's `exports` map — only `jazzAdapter` is public.

**Do not proceed with Better Auth integration without explicit direction on how to bootstrap the schema generation cycle.** The Jazz docs and Better Auth docs describe the end state but not the initial setup sequence.

### Alternative auth approach to consider

The existing `apps/server` already implements email/password auth with Argon2 password hashing, JWT signing, and Nodemailer for verification emails. Rather than replacing this with Better Auth's Jazz adapter:

1. Keep auth in `apps/server` (or migrate it to SvelteKit `+server.ts` routes without the Better Auth abstraction).
2. Use the existing JWT infrastructure to issue tokens.
3. Jazz accepts a JWT for connecting to a sync server — the token needs to be passed to the Jazz client initialisation.

This avoids the schema generation bootstrap problem entirely, keeps the user data and auth data separate by design (no Better Auth tables in the Jazz schema), and leverages already-working code. The tradeoff is that it doesn't get Better Auth's session management, OAuth provider support, or plugin ecosystem.

If Better Auth is still the desired path, the minimum viable scoping would be:
- Confirm the bootstrap sequence directly with the Jazz/Better Auth documentation or maintainers.
- Write the `schema-better-auth/schema.ts` file manually based on the known Better Auth core tables (user, session, account, verification, jwks) using the Jazz DSL — these are stable across Better Auth versions and do not require the CLI.

---

## Stylistic Notes

Do not make unecessary stylistic or commenting choices; a clean diff is preferred. Examples from a previous LLM session which brought disappointement include:

- `==` changed to `===` throughout controllers (e.g. `collections.length == 0`).
- Multi-line `if (!x) { break; }` collapsed to inline `if (!x) break;`.
- Inline step comments removed from controller functions (e.g. `/** Get all cultivar collections in the garden. */`, `/** Sort collections by priority. */`).
- JSDoc descriptions shortened in `resolveCultivarName` and other functions.
- `let garden: Garden | null = null` pattern removed in transaction callbacks.
- Return type of `getNewMembershipIdsFromUsernames` changed from `Set<string>` to `string[]` (the call site was updated, but the change was not requested).

On the new branch, preserve the existing code style exactly — only change what is necessary for the Triplit → Jazz API translation.
