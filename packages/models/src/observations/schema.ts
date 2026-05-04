import { type TableRow, schema as s } from 'jazz-tools';

import { ObservationIds } from './ids.js';

export const observationSchema = {
	/** Observation schema. */
	observations: s.table({
		/** Garden the entity is located within - required for access control. */
		gardenId: s.ref('gardens'),

		/** Type of observation - plant/harvest, environment/air_temperature, etc.. */
		type: s.enum(...ObservationIds),

		/** IDs of the primary entities which the observation applies to. Polymorphic - no ref. */
		entityIds: s.array(s.string()).default([]),

		/** Date of the observation. */
		date: s.timestamp(),

		/** Optional unstructured data. Structure depends on the observation type. */
		data: s.json().optional()
	})
};

export type GenericObservation = TableRow<typeof observationSchema, 'observations'>;
export type Observation<TData> = Omit<GenericObservation, 'data'> & {
	data: TData;
};
