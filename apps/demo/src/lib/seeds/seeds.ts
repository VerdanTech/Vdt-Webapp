import { type BulkInsert } from '@triplit/client';

import { schema } from '@vdg-webapp/models';

import cultivarsSeed from './cultivars';
import environmentSeed from './environments';
import gardenSeed from './garden';
import plantingAreasSeed from './plantingAreas';
import userSeed from './user';
import workspacesSeed from './workspace';

const seeds: Array<() => Record<string, unknown[]>> = [
	userSeed,
	gardenSeed,
	environmentSeed,
	workspacesSeed,
	plantingAreasSeed,
	cultivarsSeed
];

export function seed(): BulkInsert<typeof schema> {
	let result: BulkInsert<typeof schema> = {};
	for (const seed of seeds) {
		result = mergeSeeds(result, seed());
	}
	return result;
}

/**
 * @returns the two bulk inserts merged, with all like
 * keys forming the sum of the individual list values.
 */
export function mergeSeeds(
	seedA: Record<string, unknown[]>,
	seedB: Record<string, unknown[]>
): Record<string, unknown[]> {
	const result: Record<string, unknown[]> = {};

	// Copy all from seedA
	for (const key of Object.keys(seedA)) {
		const val = seedA[key];
		result[key] = Array.isArray(val) ? val : [];
	}

	// Merge/append from seedB
	for (const key of Object.keys(seedB)) {
		const val = seedB[key];
		if (!Array.isArray(val)) continue;
		if (key in result) {
			result[key] = result[key].concat(val);
		} else {
			result[key] = val;
		}
	}

	return result;
}
