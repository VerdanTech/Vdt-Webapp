import { schema as s } from 'jazz-tools';

import { cultivarSchema } from './cultivars/schema.js';
import { environmentSchema } from './environments/schema.js';
import { gardenSchema } from './gardens/schema.js';
import { observationSchema } from './observations/schema.js';
import { plantSchema } from './plants/schema.js';
import { workspaceSchema } from './workspaces/schema.js';

// TODO: Replace usersStub with the generated Better Auth schema once
// packages/models/schema-better-auth/schema.ts is generated via:
//   npx @better-auth/cli generate \
//     --config apps/web/src/lib/auth.ts \
//     --output packages/models/schema-better-auth/schema.ts
//
// Then:
//   import { schema as betterauthSchema } from '../schema-better-auth/schema.js';
//   import { permissions as betterauthPermissions } from '../schema-better-auth/schema.js';
//
// Merge betterauthSchema into appSchema and betterauthPermissions into permissions.ts.
// Add a public userProfiles table for display names (Better Auth users table is deny-all).
const usersStub = {
	users: s.table({
		username: s.string(),
		email: s.string()
	})
};

const appSchema = {
	...usersStub,
	...gardenSchema,
	...observationSchema,
	...workspaceSchema,
	...environmentSchema,
	...cultivarSchema,
	...plantSchema
};

export type JazzSchema = s.Schema<typeof appSchema>;
export type JazzApp = s.App<JazzSchema>;
export const jazz: JazzApp = s.defineApp(appSchema);
