import { betterAuth } from 'better-auth';
import { jwt } from 'better-auth/plugins';

// TODO: Add jazzAdapter once schema-better-auth/schema.ts is generated.
//
// Step 1 — generate the schema (run once, commit the output):
//   npx @better-auth/cli generate \
//     --config apps/web/src/lib/auth.ts \
//     --output packages/models/schema-better-auth/schema.ts
//
// Step 2 — wire up the adapter:
//   import { jazzAdapter } from 'jazz-tools/better-auth-adapter';
//   import { createJazzContext } from 'jazz-tools/backend';
//   import { jazz } from '@vdg-webapp/models';
//
//   const jazzCtx = await createJazzContext({
//     appId: process.env.JAZZ_APP_ID!,
//     serverUrl: process.env.JAZZ_SYNC_SERVER_URL, // omit for local-only dev
//     backendSecret: process.env.JAZZ_BACKEND_SECRET!,
//   });
//
//   database: jazzAdapter({
//     db: () => jazzCtx.asBackend(jazz),
//     schema: jazz.wasmSchema,
//   }),

export const auth = betterAuth({
	emailAndPassword: { enabled: true },
	plugins: [
		jwt({
			jwks: { keyPairConfig: { alg: 'ES256' } },
			jwt: {
				issuer: process.env.JAZZ_JWT_ISSUER ?? 'http://localhost:5173'
			}
		})
	]
});
