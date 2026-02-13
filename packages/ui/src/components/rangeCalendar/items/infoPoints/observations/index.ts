import type { Component } from 'svelte';

import { type GenericObservation, type PlantObservationId } from '@vdg-webapp/models';

import ObservationPlantGenericInfopoint from './ObservationPlantGenericInfopoint.svelte';

export const PlantObservationPopupContentComponents: Record<
	PlantObservationId,
	Component<{ observation: GenericObservation }>
> = {
	'plant-seed': ObservationPlantGenericInfopoint,
	'plant-germ': ObservationPlantGenericInfopoint,
	'plant-harvest': ObservationPlantGenericInfopoint,
	'plant-expiry': ObservationPlantGenericInfopoint,
	'plant-dormancy-enter': ObservationPlantGenericInfopoint,
	'plant-growth-enter': ObservationPlantGenericInfopoint,
	'plant-flower': ObservationPlantGenericInfopoint
};
