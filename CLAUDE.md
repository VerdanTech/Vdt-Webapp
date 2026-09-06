# Verdagraph Webapp

Garden productivity tool and IoT platform. Users create **Gardens** (collaborative spaces), manage **Workspaces** (spatial containers), track **Plants** (physical instances of **Cultivars**), record **Observations**, use the **Verdagraph** planner, and eventually connect **Devices/Sensors**.

## Project Context

See `apps/docs/src/routes/about/+page.svx` for a detailed introduction to the project goals.

## Repo Structure

Turbo + PNPM monorepo.

```
apps/
  web/        SvelteKit frontend (Svelte 5, Vite, Tailwind, bits-ui, shadcn-svelte)
  server/     Fastify backend (Node.js, JWT, Argon2, Nodemailer)
  docs/       Documentation site.
  demo/       Pared-down version of the application for demonstration.
packages/
  models/     Shared domain: Database schemas, Zod commands, controllers
  ui/         Shared Svelte component library
  eslint-config/
  tailwind-config/
  typescript-config/
design/       High-level domain model docs and wireframes (Excalidraw)
```

## Tech Stack

| Layer      | Technology                           |
| ---------- | ------------------------------------ |
| Frontend   | SvelteKit, Svelte 5, Vite            |
| Backend    | Fastify, Node.js                     |
| Database   | Triplit (real-time full-stack sync)  |
| Validation | Zod                                  |
| Styling    | Tailwind CSS, bits-ui, shadcn-svelte |
| Canvas     | Konva                                |

## Code Style

### Naming Conventions

- **Files/functions/variables**: camelCase
- **Components/types/classes**: PascalCase
- **Enum option arrays**: `FooEnumOptions` (const array), derive the type with `(typeof FooEnumOptions)[number]`
- **Commands (Zod schemas)**: `FooActionCommandSchema` / `FooActionCommand` (inferred type)
- **Schema collections**: defined in `schema.ts`, exported as `Entity<>` types

Additionally, variable names are to be verbose at all times. No vague 1 to 3 letter variable names. Use the full english word, shortening when possible.

### TypeScript

- Strict mode; shared tsconfig from `packages/typescript-config`
- Prefer explicit return types on exported functions
- Use `z.infer<typeof Schema>` for command types rather than duplicating

## Comments

- JSDoc on exported/public functions with `@param` descriptions
- Comment syntax uses /\*\* \*/.
- Comments are to be as plain and precise as possible.

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

Domain specs live in `design/<area>/models.md`. Each has a `status` frontmatter field indicating whether it's ahead/matching/behind implementation. Wireframes are Excalidraw PNGs.

## Key Scripts

```bash
pnpm dev          # Start all apps (Turbo)
pnpm build        # Build all
pnpm lint         # Lint all
pnpm check-types  # TypeScript checks
pnpm format       # Prettier format
pnpm clean        # Remove node_modules, dist, .svelte-kit, .d.ts files
```

## Workspace Package Names

- `@vdg-webapp/models`
- `@vdg-webapp/ui`
- `@vdg-webapp/eslint-config`
- `@vdg-webapp/tailwind-config`
- `@vdg-webapp/typescript-config`
