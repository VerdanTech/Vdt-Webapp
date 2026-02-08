import { type GenericObservation, type PlantObservationId } from '@vdg-webapp/models';
import type { Component } from 'svelte';
import ObservationPlantSeedInfopoint from './ObservationPlantSeedInfopoint.svelte'

export const PlantObservationPopupContentComponents: Record<PlantObservationId, Component<{observation: GenericObservation}>> = {
	'plant-seed': ObservationPlantSeedInfopoint,
	//'plant-germ': 'Germination',
	//'plant-harvest': 'Harvest',
	//'plant-expiry': 'Expiry',
	//'plant-dormancy-enter': 'Dormancy',
	//'plant-growth-enter': 'Growth',
	//'plant-flower': 'Flower'
};
