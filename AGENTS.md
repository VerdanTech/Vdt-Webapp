# Verdagraph Webapp

Garden productivity tool and IoT platform. Users create **Gardens** (collaborative spaces), manage **Workspaces** (spatial containers), track **Plants** (physical instances of **Cultivars**), record **Observations**, use the **Verdagraph** planner, and eventually connect **Devices/Sensors**.

## Working With This Project — Agent Autonomy

This is a project the maintainer has developed for years, with architectural decisions already made deliberately (Triplit, the Fastify/Triplit split, the Jazz v2 migration plan, etc.) based on hands-on experience about what will get it to its goals. It is **explicitly not meant to become an LLM-driven project** — LLMs are here to accelerate execution, not to steer direction.

Practical effect: default to essentially **no independent architectural or dependency decision-making**. Anything beyond the narrow task at hand — new dependencies, schema/data-model changes, cross-cutting refactors, migrations, or deviating from a pattern already established in the code — should be raised with the maintainer rather than decided unilaterally, even when a "better" alternative seems obvious. When in doubt, ask.

## Project Context

- **Mission, values, and background**: `apps/docs/src/routes/about/+page.svx` is the canonical statement of what Verdagraph is and why it exists (agro-ecology, sentientist values, collaborative labor organization, IoT automation) — it's the source for the live [verdagraph.org/about](https://verdagraph.org/about) page, so read it directly here for "why" questions before inferring intent from code.
- **Feature-level intent**: `design/<area>/README.md` and `design/<area>/models.md` describe the intended domain model per feature area (see below); these are more granular than the about page but can drift from implementation (see `status` frontmatter).

## Repo Structure

Turbo + PNPM monorepo.

```
apps/
  web/        SvelteKit frontend (Svelte 5, Vite, Tailwind, bits-ui, shadcn-svelte) — the production application; not yet deployed publicly, still being brought up to a usable/up-to-date state
  server/     Fastify backend (Node.js, JWT, Argon2, Nodemailer) — currently scoped to user auth/account flows only
  docs/       Marketing/documentation site (verdagraph.org)
  demo/       Pared-down version of the application, focused on core components — this is the one deployed as the public demo
packages/
  models/     Shared domain: Triplit schemas, Zod commands, controllers
  ui/         Shared Svelte component library (core primitives + composed feature components)
  eslint-config/
  tailwind-config/
  typescript-config/
design/       High-level domain model docs and wireframes (Excalidraw), organized by feature category
```

## Architecture Notes

The data layer is split across two systems — worth keeping straight since both "backend"s exist for different reasons:

- **Triplit** (`packages/models/triplit/schema.ts`) is the primary application database. The `web` client talks to it directly for real-time sync of domain data (Gardens, Workspaces, Plants, Cultivars, Observations, the Planner, etc.) via `apps/web/src/lib/data/triplit.ts`. Triplit itself is unmaintained upstream but still does everything the project currently needs. The plan is to migrate to **Jazz v2** (a similar sync engine) once it's more stable — either near public release or sooner if something comes up that Triplit can't do. This isn't in progress; it's a deliberate future step, not a signal to start abstracting away from Triplit now.
- **The Fastify server** (`apps/server`) currently only handles things Triplit doesn't: authentication (JWT + Argon2), account/email flows (verification, password reset), and transactional email (Nodemailer). It exposes a REST API; `apps/web` calls it through a generated client (Orval, config at `apps/web/orval.config.ts`) built from the OpenAPI spec at `apps/web/server.json` (regenerate via the server's `schema` script).

## Tech Stack

| Layer          | Technology                                     |
| -------------- | ----------------------------------------------- |
| Frontend       | SvelteKit, Svelte 5, Vite                       |
| Backend (auth) | Fastify, Node.js, JWT, Argon2, Awilix (DI)      |
| Database       | Triplit (real-time full-stack sync)             |
| API codegen    | Orval (REST client generated from OpenAPI spec) |
| Validation     | Zod                                             |
| Styling        | Tailwind CSS, bits-ui, shadcn-svelte            |
| Canvas         | Konva                                           |

## Code Style

### Naming Conventions

- **Files/functions/variables**: camelCase
- **Components/types/classes**: PascalCase
- **Enum option arrays**: `FooEnumOptions` (const array), derive the type with `(typeof FooEnumOptions)[number]`
- **Commands (Zod schemas)**: `FooActionCommandSchema` / `FooActionCommand` (inferred type)
- **Schema collections**: defined in `schema.ts`, exported as `Entity<>` types

Additionally, variable names are to be verbose and self-documenting at all times. No vague 1 to 3 letter variable names. Use the full english word, shortening when possible. A name should convey what the value is and, where relevant, why it exists, so a reader rarely needs a comment just to understand what a variable holds.

### TypeScript

- Strict mode; shared tsconfig from `packages/typescript-config`
- Prefer explicit return types on exported functions
- Use `z.infer<typeof Schema>` for command types rather than duplicating

## Comments

- JSDoc on exported/public functions with `@param` descriptions
- Comment syntax uses /\*\* \*/.
- Comments are to be as plain and precise as possible.
- Focus comments on non-obvious details and helpful context — a hidden constraint, a subtle invariant, the reason behind a workaround, something that would surprise a reader — not on over-explaining what well-named code already makes clear. If a comment just restates what the code does, delete it instead.
- Before writing a comment, look at existing comments nearby (or in a similar domain area) as the reference for tone, length, and what's worth noting — match that style rather than introducing a new one.

### Domain Model Pattern (`packages/models`)

Each domain area has:

- `schema.ts` — Triplit `S.Collections(...)` with permissions
- `commands.ts` — Zod schemas for mutations (create/update/delete)
- `controller.ts` — async functions that validate, authorize, and mutate via Triplit
- `index.ts` — re-exports

Commands use shared field schemas from `commands.ts` at the domain root. Controllers receive a `ControllerContext` (from `createController`) for auth and Triplit access.

### Svelte Components

- Co-locate page-specific components alongside their `+page.svelte`
- Reusable components go in `packages/ui/src/components/`

### Design Docs (`design/`)

Domain specs live in `design/<area>/models.md`. Each has a `status` frontmatter field indicating whether the doc is **behind**, **in sync with**, or **ahead of** (describing planned/future work not yet built) the implementation. Wireframes are Excalidraw PNGs.

When a change alters a domain model or plans a future addition, update the relevant `models.md` (content and `status`) as part of that change — these docs are meant to be kept live, not written once and left to drift.

## Key Scripts

```bash
pnpm dev          # Start all apps (Turbo)
pnpm build        # Build all
pnpm lint         # Lint all
pnpm check-types  # TypeScript checks
pnpm format       # Prettier format
pnpm clean        # Remove node_modules, dist, .svelte-kit, .d.ts files
```

There is no `pnpm test` — no automated test suite or CI pipeline exists in this repo yet, simply for lack of time rather than a decision against testing. Don't assume a test runner exists; verify changes via `check-types`, `lint`, and manual/browser testing instead. If you do add tests, keep the footprint small and targeted at the highest-value spots (e.g. tricky domain logic in `packages/models`) — the goal is a handful of genuinely useful tests, not broad coverage, and specifically not a suite that itself becomes something requiring agent effort to maintain.

## Workspace Package Names

- `@vdg-webapp/models`
- `@vdg-webapp/ui`
- `@vdg-webapp/eslint-config`
- `@vdg-webapp/tailwind-config`
- `@vdg-webapp/typescript-config`

## Git Workflow & Deployment

- **Branches**: `main` tracks the most recent merged changes. `prod` is what's built and deployed to the public demo (`apps/demo`, hand-maintained on Cloudflare). Feature branches get merged into `main`.
- **No commit message convention is enforced** — short imperative present-tense (as seen in history, e.g. "Adds X", "Fixes Y") is fine but not required.
- **Deployment today**: only `apps/demo` and `apps/docs` are deployed (Cloudflare, maintained by hand — no need to change or automate this). `apps/web` (the production app) and `apps/server` are not deployed publicly yet; getting `apps/web` up to date and usable is future work, not something in progress now.
- **Env/secrets**: everything is currently maintained by hand on Cloudflare; `contributing.md`'s reference to a `.env.default` in `./common` is stale (that path doesn't exist in the repo) — don't rely on it, check the relevant `env.ts`/config files directly instead.

## Current State & Caveats

- **Pre-1.0, solo-maintained, actively evolving.** Treat conventions here as current best understanding, not frozen law.
- **No CI/CD is configured** (no `.github/workflows`). Nothing gates merges automatically today.
- **Many stale/parked branches exist on the remote** (e.g. `migrate-data-layer-jazz`, `migrate-arktype-hono`, `triplit-schema-confusion`) representing paused or abandoned experiments, not active work. Don't treat them as signals of current direction or revive/merge ideas from them without checking first — see the Jazz v2 note above for the one exception that *is* an intended future direction (just not active yet).
