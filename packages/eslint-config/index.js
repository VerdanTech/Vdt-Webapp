import js from '@eslint/js';
import svelte from 'eslint-plugin-svelte';
import unusedImports from 'eslint-plugin-unused-imports';
import globals from 'globals';
import ts from 'typescript-eslint';

export const config = ts.config(
	js.configs.recommended,
	...ts.configs.recommended,
	...svelte.configs['flat/recommended'],
	{
		plugins: {
			'unused-imports': unusedImports
		},
		languageOptions: {
			globals: {
				...globals.browser,
				...globals.node
			}
		}
	},
	{
		files: ['**/*.svelte'],
		ignores: ['.svelte-kit/*'],
		languageOptions: {
			parserOptions: {
				parser: ts.parser
			}
		}
	}
);
