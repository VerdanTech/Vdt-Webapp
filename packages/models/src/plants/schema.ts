import { type TableRow, schema as s } from 'jazz-tools';

import { CultivarAttributesUpdateCommandSchema } from '../cultivars/attributes/index.js';
import type { GeometryHistory, LocationHistory } from '../workspaces/schema.js';
import type { PlantObservation } from './observations.js';

/**
 * The origin method of a plant lifespan.
 */
export const OriginEnumOptions = [
	'DIRECT_SEED',
	'SEED_TO_TRANSPLANT',
	'SEEDLING_TO_TRANSPLANT'
] as const;

export const plantSchema = {
	/** Lifespan schema. */
	lifespans: s.table({
		/** Garden the entity is located within - required for access control. */
		gardenId: s.ref('gardens'),

		/** The origin of the lifespan. */
		origin: s.enum(...OriginEnumOptions),

		/** The geometries of the lifespan. */
		geometryHistoryId: s.ref('geometryHistories').optional(),

		/** The locations of the lifespan. */
		locationHistoryId: s.ref('locationHistories').optional()
	}),

	/** Plant schema. */
	plants: s.table({
		/** Garden the entity is located within - required for access control. */
		gardenId: s.ref('gardens'),

		/**
		 * The name correlating with one of the common names specified by a cultivar.
		 * Will match the plant with a cultivar in one of the garden's cultivar collections.
		 */
		cultivarName: s.string(),

		/** A set of cultivar attributes to override those from the collections. */
		cultivarAttributes: s.json(CultivarAttributesUpdateCommandSchema).optional(),

		/** Lifespan populated from the expected attributes based on the cultivar. */
		expectedLifespanId: s.ref('lifespans'),

		/** Lifespan populated by observations of users. */
		recordedLifespanId: s.ref('lifespans'),

		/**
		 * Range of dates encapsulating all dates applicable to this plant.
		 * Denormalized from lifespans; must be updated alongside lifespan updates.
		 */
		beginDate: s.timestamp(),
		endDate: s.timestamp(),

		/** The number of distinct plants managed together in this plant instance. */
		quantity: s.int().default(1)
	}),

	/** PlantGroup schema. */
	plantGroups: s.table({
		/** Garden the entity is located within - required for access control. */
		gardenId: s.ref('gardens'),

		/** Name. */
		name: s.string(),

		/** A set of plant IDs contained within the group. */
		plantIds: s.array(s.string()),

		/** Optional description. */
		description: s.string().default('')
	})
};

export type Origin = (typeof OriginEnumOptions)[number];
export type Lifespan = TableRow<typeof plantSchema, 'lifespans'> & {
	locationHistory?: LocationHistory | null;
	geometryHistory?: GeometryHistory | null;
	observations?: PlantObservation[] | null;
};
export type Plant = TableRow<typeof plantSchema, 'plants'> & {
	expectedLifespan?: Lifespan | null;
	recordedLifespan?: Lifespan | null;
};
export type PlantGroup = TableRow<typeof plantSchema, 'plantGroups'>;

export const OriginEnumLabels: Record<Origin, string> = {
	DIRECT_SEED: 'Direct Seed',
	SEEDLING_TO_TRANSPLANT: 'Seedling to Transplant',
	SEED_TO_TRANSPLANT: 'Seed to Transplant'
};
