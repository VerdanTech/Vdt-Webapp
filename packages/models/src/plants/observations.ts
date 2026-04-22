import { co, z } from 'jazz-tools';

import { ObservationSchema } from '../observations/schema.js';

/** Used to record the date at which a seed was planted. */
export const PlantSeedObservationId = 'plant-seed' as const;
export const PlantSeedObservationDetailsSchema = co.map({
	type: z.literal(PlantSeedObservationId)
});

/** Used to record when a seed has successfully germinated (sprouted). */
export const PlantGermObservationId = 'plant-germ' as const;
export const PlantGermObservationDetailsSchema = co.map({
	type: z.literal(PlantGermObservationId)
});

/** Used to record the harvest of a plant and its produce. */
export const PlantHarvestObservationId = 'plant-harvest' as const;
export const PlantHarvestObservationDetailsSchema = co.map({
	type: z.literal(PlantHarvestObservationId),
	mass: z.optional(z.number()),
	quality: z.optional(z.string()),
	description: z.optional(z.string())
});

/** Used to record when a plant has reached the end of its life and has been removed. */
export const PlantExpiryObservationId = 'plant-expiry' as const;
export const PlantExpiryObservationDetailsSchema = co.map({
	type: z.literal(PlantExpiryObservationId)
});

/** Used to record when a plant enters a dormant state (e.g., winter rest). */
export const PlantDormancyEnterObservationId = 'plant-dormancy-enter' as const;
export const PlantDormancyEnterObservationDetailsSchema = co.map({
	type: z.literal(PlantDormancyEnterObservationId)
});

/** Used to record when a plant has exited dormancy. */
export const PlantDormancyExitObservationId = 'plant-growth-enter' as const;
export const PlantDormancyExitObservationDetailsSchema = co.map({
	type: z.literal(PlantDormancyExitObservationId)
});

/** Used to record when a plant has flowered. */
export const PlantFlowerObservationId = 'plant-flower' as const;
export const PlantFlowerObservationDetailsSchema = co.map({
	type: z.literal(PlantFlowerObservationId)
});

const plantObservationRegistry = {
	[PlantSeedObservationId]: {
		label: 'Seed',
		description: 'The date at which the plant is sown as a seed.',
		schema: PlantSeedObservationDetailsSchema
	},
	[PlantGermObservationId]: {
		label: 'Germination',
		description: "The date at which the plant's seed germinates.",
		schema: PlantGermObservationDetailsSchema
	},
	[PlantHarvestObservationId]: {
		label: 'Harvest',
		description: 'A date at which a harvest is made from the plant.',
		schema: PlantHarvestObservationDetailsSchema
	},
	[PlantExpiryObservationId]: {
		label: 'Expiry',
		description:
			'The date at which the plant is removed or otherwise no longer considered in the model.',
		schema: PlantExpiryObservationDetailsSchema
	},
	[PlantDormancyEnterObservationId]: {
		label: 'Dormancy',
		description: 'A date at which the plant enters a dormant stage.',
		schema: PlantDormancyEnterObservationDetailsSchema
	},
	[PlantDormancyExitObservationId]: {
		label: 'Growth',
		description: 'A date at which the plant exits a dormant stage.',
		schema: PlantDormancyExitObservationDetailsSchema
	},
	[PlantFlowerObservationId]: {
		label: 'Flower',
		description: 'A date at which the plant produces a flower.',
		schema: PlantFlowerObservationDetailsSchema
	}
} as const;

export type PlantObservationId = keyof typeof plantObservationRegistry;

export const PlantObservationIds = Object.keys(
	plantObservationRegistry
) as PlantObservationId[];

export const PlantObservationLabels = Object.fromEntries(
	Object.entries(plantObservationRegistry).map(([id, { label }]) => [id, label])
) as Record<PlantObservationId, string>;

export const PlantObservationDescriptions = Object.fromEntries(
	Object.entries(plantObservationRegistry).map(([id, { description }]) => [id, description])
) as Record<PlantObservationId, string>;

export const PlantObservationSchema = ObservationSchema.extend({
	details: co.discriminatedUnion('type', [
		PlantSeedObservationDetailsSchema,
		PlantGermObservationDetailsSchema,
		PlantHarvestObservationDetailsSchema,
		PlantExpiryObservationDetailsSchema,
		PlantDormancyEnterObservationDetailsSchema,
		PlantDormancyExitObservationDetailsSchema,
		PlantFlowerObservationDetailsSchema
	])
});
export type PlantObservation = co.loaded<typeof PlantObservationSchema>;
