import { PlantObservationIds } from '../plants/observations.js';

export const ObservationIds = [...PlantObservationIds];
export type ObservationId = (typeof ObservationIds)[number];
