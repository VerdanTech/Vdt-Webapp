import { defineConfig } from 'orval';

export default defineConfig({
	verdantech_client: {
		input: {
			target: './schema.yml'
			//validation: true
		},
		output: {
			mode: 'tags-split',
			client: 'svelte-query',
			target: 'src/lib/api/codegen/',
			//useDates: true,
			mock: true,
			override: {
				mutator: {
					path: './src/lib/api/customAxios.ts',
					name: 'customInstance'
				}
			}
		},
		hooks: {
			afterAllFilesWrite: 'npm run format'
		}
	}
});
