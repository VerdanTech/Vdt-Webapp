import type { Observation } from '../observations/schema.js';

/**
 * Used to record the date at which a seed was planted.
 *
 * entityIds type: Lifespan
 */
export type PlantSeedObservationId = 'plant-seed';
export type PlantSeedObservationData = undefined;
export type PlantSeedObservation = Observation<
	PlantSeedObservationId,
	PlantSeedObservationData
>;

/**
 * Used to record when a seed has successfully germinated (sprouted).
 *
 * entityIds type: Lifespan
 */
export type PlantGermObservationId = 'plant-germ';
export type PlantGermObservationData = undefined;
export type PlantGermObservation = Observation<
	PlantGermObservationId,
	PlantGermObservationData
>;

/**
 * Used to record the harvest of a plant and its produce.
 *
 * entityIds type: Lifespan
 */
export type PlantHarvestObservationId = 'plant-harvest';
export type PlantHarvestObservationData = {
	/** The mass of the harvest in kilograms. */
	mass?: number;
	/** The quality of the harvest. */
	quality?: string;
	/** Optional description. */
	description?: string;
};
export type PlantHarvestObservation = Observation<
	PlantHarvestObservationId,
	PlantHarvestObservationData
>;

/**
 * Used to record when a plant has reached the end of its life and has been removed.
 *
 * entityIds type: Lifespan
 */
export type PlantExpiryObservationId = 'plant-expiry';
export type PlantExpiryObservationData = undefined;
export type PlantExpiryObservation = Observation<
	PlantExpiryObservationId,
	PlantExpiryObservationData
>;

/**
 * Used to record when a plant enters a dormant state (e.g., winter rest).
 *
 * entityIds type: Lifespan
 */
export type PlantDormancyEnterObservationId = 'plant-dormancy-enter';
export type PlantDormancyEnterObservationData = undefined;
export type PlantDormancyEnterObservation = Observation<
	PlantDormancyEnterObservationId,
	PlantDormancyEnterObservationData
>;

/**
 * Used to record when a plant has exited dormancy.
 *
 * entityIds type: Lifespan
 */
export type PlantDormancyExitObservationId = 'plant-growth-enter';
export type PlantDormancyExitObservationData = undefined;
export type PlantDormancyExitObservation = Observation<
	PlantDormancyExitObservationId,
	PlantDormancyExitObservationData
>;

/**
 * Used to record when a plant has flowered.
 *
 * entityIds type: Lifespan
 */
export type PlantFlowerObservationId = 'plant-flower';
export type PlantFlowerObservationData = undefined;
export type PlantFlowerObservation = Observation<
	PlantFlowerObservationId,
	PlantFlowerObservationData
>;

export type PlantObservation =
	| PlantSeedObservation
	| PlantHarvestObservation
	| PlantGermObservation
	| PlantExpiryObservation
	| PlantDormancyEnterObservation
	| PlantDormancyExitObservation
	| PlantFlowerObservation;

export type PlantObservationId =
	| PlantSeedObservationId
	| PlantGermObservationId
	| PlantHarvestObservationId
	| PlantExpiryObservationId
	| PlantDormancyEnterObservationId
	| PlantDormancyExitObservationId
	| PlantFlowerObservationId;

export const PlantObservationLabels: Record<PlantObservationId, string> = {
	'plant-seed': 'Seed',
	'plant-germ': 'Germination',
	'plant-harvest': 'Harvest',
	'plant-expiry': 'Expiry',
	'plant-dormancy-enter': 'Dormancy',
	'plant-growth-enter': 'Growth',
	'plant-flower': 'Flower'
};
