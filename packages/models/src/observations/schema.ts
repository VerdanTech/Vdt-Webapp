import { type Entity, Schema as S, or } from '@triplit/client';

import { gardenSchema } from '../gardens/schema.js';

export const observationSchema = S.Collections({
	...gardenSchema,
	/** Observation schema. */
	observations: {
		schema: S.Schema({
			id: S.Id(),

			/** Garden the entity is located within - required for access control. */
			gardenId: S.String(),

			/** Type of observation - plant/harvest, environment/air_temperature, etc.. */
			type: S.String(),

			/** IDs of the primary entities which the observation applies to. */
			entityIds: S.Set(S.String(), { default: S.Default.Set }),

			/** Date of the observation. */
			date: S.Date(),

			/** Optional unstructured data. Structure depends on the observation type. */
			data: S.Optional(S.Json({}))
		}),
		relationships: {
			garden: S.RelationById('gardens', '$gardenId')
		},
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: [['garden.visibility', '!=', 'HIDDEN']]
				}
			},
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: [
						or([
							['garden.visibility', '!=', 'HIDDEN'],
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId'],
							['garden.viewerIds', 'has', '$role.profileId']
						])
					]
				},
				insert: {
					/** Allow new observations to be created by admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				update: {
					/** Restrict observation updates to admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				delete: {
					/** Restrict observation deletes to admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				}
			}
		}
	}
});
export type GenericObservation = Entity<typeof observationSchema, 'observations'>;
export type Observation<TId, TData> = Omit<GenericObservation, 'type' | 'data'> & {
	type: TId;
	data: TData;
};
