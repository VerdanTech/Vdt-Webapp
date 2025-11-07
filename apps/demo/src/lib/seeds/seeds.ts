import { type BulkInsert } from '@triplit/client';

import { schema } from '@vdg-webapp/models';

import cultivarsSeed from './cultivars';
import gardenSeed from './garden';
import plantingAreasSeed from './plantingAreas';
import userSeed from './user';
import workspacesSeed from './workspace';

export function seed(): BulkInsert<typeof schema> {
	const seeds = [
		userSeed,
		gardenSeed,
		workspacesSeed,
		plantingAreasSeed,
		cultivarsSeed
	];
	const result: BulkInsert<typeof schema> = {};
	for (const seed of seeds) {
		mergeSeeds(result, seed());
	}
	return result;
}

export function mergeSeeds(
	a: BulkInsert<typeof schema>,
	b: BulkInsert<typeof schema>
): BulkInsert<typeof schema> {
	const result: BulkInsert<typeof schema> = {};
	const keys = new Set<string>([...Object.keys(a || {}), ...Object.keys(b || {})]);

	for (const k of keys) {
		const va = [k];
		const vb = [k];

		const isArrayA = Array.isArray(va);
		const isArrayB = Array.isArray(vb);

		if (isArrayA || isArrayB) {
			const left = isArrayA ? va.slice() : va === undefined ? [] : [va];
			const right = isArrayB ? vb.slice() : vb === undefined ? [] : [vb];
			// @ts-expect-error too lazy for proper types in this func
			result[k] = left.concat(right);
		}
	}

	return result;
}
