import type { Observation } from '../observations/schema.js';

/**
 * Used to record the date at which a seed was planted.
 *
 * entityIds type: Lifespan
 */
export const PlantSeedObservationId = 'plant-seed';
export type PlantSeedObservationData = undefined;
export type PlantSeedObservation = Observation<PlantSeedObservationData>;

/**
 * Used to record when a seed has successfully germinated (sprouted).
 *
 * entityIds type: Lifespan
 */
export const PlantGermObservationId = 'plant-germ';
export type PlantGermObservationData = undefined;
export type PlantGermObservation = Observation<PlantGermObservationData>;

/**
 * Used to record the harvest of a plant and its produce.
 *
 * entityIds type: Lifespan
 */
export const PlantHarvestObservationId = 'plant-harvest';
export type PlantHarvestObservationData = {
	/** The mass of the harvest in kilograms. */
	mass?: number;
	/** The quality of the harvest. */
	quality?: string;
	/** Optional description. */
	description?: string;
};
export type PlantHarvestObservation = Observation<PlantHarvestObservationData>;

/**
 * Used to record when a plant has reached the end of its life and has been removed.
 *
 * entityIds type: Lifespan
 */
export const PlantExpiryObservationId = 'plant-expiry';
export type PlantExpiryObservationData = undefined;
export type PlantExpiryObservation = Observation<PlantExpiryObservationData>;

/**
 * Used to record when a plant enters a dormant state (e.g., winter rest).
 *
 * entityIds type: Lifespan
 */
export const PlantDormancyEnterObservationId = 'plant-dormancy-enter';
export type PlantDormancyEnterObservationData = undefined;
export type PlantDormancyEnterObservation =
	Observation<PlantDormancyEnterObservationData>;

/**
 * Used to record when a plant has exited dormancy.
 *
 * entityIds type: Lifespan
 */
export const PlantDormancyExitObservationId = 'plant-growth-enter';
export type PlantDormancyExitObservationData = undefined;
export type PlantDormancyExitObservation =
	Observation<PlantDormancyExitObservationData>;

/**
 * Used to record when a plant has flowered.
 *
 * entityIds type: Lifespan
 */
export const PlantFlowerObservationId = 'plant-flower';
export type PlantFlowerObservationData = undefined;
export type PlantFlowerObservation = Observation<PlantFlowerObservationData>;

export type PlantObservation =
	| PlantSeedObservation
	| PlantHarvestObservation
	| PlantGermObservation
	| PlantExpiryObservation
	| PlantDormancyEnterObservation
	| PlantDormancyExitObservation
	| PlantFlowerObservation;

export const PlantObservationIds = [
	PlantSeedObservationId,
	PlantGermObservationId,
	PlantHarvestObservationId,
	PlantExpiryObservationId,
	PlantDormancyEnterObservationId,
	PlantDormancyExitObservationId,
	PlantFlowerObservationId
] as const;

export type PlantObservationId = (typeof PlantObservationIds)[number];

export const PlantObservationLabels: Record<PlantObservationId, string> = {
	'plant-seed': 'Seed',
	'plant-germ': 'Germination',
	'plant-harvest': 'Harvest',
	'plant-expiry': 'Expiry',
	'plant-dormancy-enter': 'Dormancy',
	'plant-growth-enter': 'Growth',
	'plant-flower': 'Flower'
};
export const PlantObservationDescriptions: Record<PlantObservationId, string> = {
	'plant-seed': 'The date at which the plant is sown as a seed.',
	'plant-germ': "The date at which the plant's seed germinates.",
	'plant-harvest': 'A date at which a harvest is made from the plant.',
	'plant-expiry':
		'The date at which the plant is removed or otherwise no longer considered in the model.',
	'plant-dormancy-enter': 'A date at which the plant enters a dormant stage.',
	'plant-growth-enter': 'A date at which the plant exits a dormant stage.',
	'plant-flower': 'A date at which the plant produces a flower.'
};
