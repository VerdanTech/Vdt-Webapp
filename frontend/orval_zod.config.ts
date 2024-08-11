import { defineConfig } from 'orval'

export default defineConfig({
	vdt_frontend: {
		input: {
			// Path to the openapi specification.
			target: './schema.yaml',
			// Whether to apply IBM OpenAPI linter.
			validation: false
		},
		output: {
			// Path to the generated client code.
			workspace: 'src/lib/codegen/zod/',
			// Path relative to workspace to generated client code.
			target: './',
			/* Disables index.ts generation. */
			indexFiles: false,
			// What type of client to generate.
			client: 'zod',
			// Generates a file for every unique openapi tag
			mode: 'tags',
			// Whether to generate Mock Service Worker mocked code.
			mock: false,
			// Generates comment headers on client code.
			headers: true,
			// Formats generated code.
			prettier: true,
			override: {
				useNativeEnums: true
			}
		}
	}
})
