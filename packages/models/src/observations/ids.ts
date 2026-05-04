import { PlantObservationIds } from '../plants/observations.js';

export const ObservationIds = [...PlantObservationIds] as const;
export type ObservationId = (typeof ObservationIds)[number];
