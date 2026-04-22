import { co, z } from 'jazz-tools';

import { GardenSchema, gardenFields } from '../gardens/index.js';

/************************************
 * Global Index
 ************************************/

export const GLOBAL_COVAL_ID_PUBLIC_INDEX = 'global-public-index';

/**
 * @title Global Index.
 */
export const GlobalIndexSchema = co.map({
	gardens: co.record(gardenFields.gardenIdField, GardenSchema)
});

export type GlobalIndex = co.loaded<typeof GlobalIndexSchema, { gardens: true }>;
