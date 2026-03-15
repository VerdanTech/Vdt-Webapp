import { type Entity, Schema as S, or } from '@triplit/client';

import { CultivarAttributes } from '../cultivars/attributes/index.js';
import { type Cultivar, cultivarSchema } from '../cultivars/schema.js';
import { type Environment } from '../environments/schema.js';
import { type DateRange } from '../time/utils.js';
import { GeometryHistory, LocationHistory } from '../workspaces/schema.js';
import { PlantObservation } from './observations.js';

/**
 *
 */
export const OriginEnumOptions = [
	'DIRECT_SEED',
	'SEED_TO_TRANSPLANT',
	'SEEDLING_TO_TRANSPLANT'
] as const;

export const plantSchema = S.Collections({
	...cultivarSchema,
	/** Lifespan schema. */
	lifespans: {
		schema: S.Schema({
			id: S.Id(),

			/** Garden the entity is located within - required for access control. */
			gardenId: S.String(),

			/** The origin of the lifespan. */
			origin: S.String({ enum: [...OriginEnumOptions] }),

			/** The geometries of the lifespan. */
			geometryHistoryId: S.Optional(S.String()),

			/** The locations of the lifespan. */
			locationHistoryId: S.Optional(S.String())
		}),
		relationships: {
			garden: S.RelationById('gardens', '$gardenId'),
			geometryHistory: S.RelationById('geometryHistories', '$geometryHistoryId'),
			locationHistory: S.RelationById('locationHistories', '$locationHistoryId'),
			observations: S.RelationMany('observations', {
				where: [['entityIds', 'has', '$id']]
			})
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
					/** Allow new lifespans to be created by admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				update: {
					/** Restrict lifespans updates to admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				delete: {
					/** Restrict lifespans deletes to admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				}
			}
		}
	},
	/** Plant schema. */
	plants: {
		schema: S.Schema({
			id: S.Id(),

			/** Garden the entity is located within - required for access control. */
			gardenId: S.String(),

			/**
			 * The name correlating with one of the common names specified by a cultivar.
			 * Will match the plant with a cultivar in one of the garden's cultivar collections.
			 */
			cultivarName: S.String(),

			/** A set of cultivar attributes to override those from the collections. */
			cultivarAttributes: CultivarAttributes,

			/** Lifespan attributes populated from the expected attributes based on the cultivar. */
			expectedLifespanId: S.String(),

			/** Lifespan attributes populated by observations of users. */
			recordedLifespanId: S.String(),

			/**
			 * Range of dates which encapsulates all dates applicable to this plant.
			 * This data is denormalized and must be updated alongside the update of
			 * plant Lifespans.
			 * This is necessary in order to not rely on complex query logic of what
			 * time range a plant exists in.
			 */
			beginDate: S.Date(),
			endDate: S.Date(),

			/** The number of distinct plants which are managed together in this plant instance. */
			quantity: S.Number({ default: 1 })
		}),
		relationships: {
			garden: S.RelationById('gardens', '$gardenId'),
			expectedLifespan: S.RelationById('lifespans', '$expectedLifespanId'),
			recordedLifespan: S.RelationById('lifespans', '$recordedLifespanId'),
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
					/** Allow new location history to be created by admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				update: {
					/** Restrict location history updates to admins. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				delete: {
					/** Restrict location histories deletes to admins. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				}
			}
		}
	},
	/** Plant groups. */
	plantGroups: {
		schema: S.Schema({
			id: S.Id(),

			/** Garden the entity is located within - required for access control. */
			gardenId: S.String(),

			/** Name. */
			name: S.String(),

			/** A set of plants contained with the group. */
			plantIds: S.Set(S.String()),

			/** Optional description. */
			description: S.String({ default: '' })
		}),
		relationships: {
			garden: S.RelationById('gardens', '$gardenId'),
			plants: S.RelationMany('plants', { where: [['id', 'in', '$plantIds']] })
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
					/** Allow new location history to be created by admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				update: {
					/** Restrict location history updates to admins. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				delete: {
					/** Restrict location histories deletes to admins. */
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
export type Origin = (typeof OriginEnumOptions)[number];
export type Lifespan = Entity<typeof plantSchema, 'lifespans'> & {
	locationHistory: LocationHistory | null;
	geometryHistory: GeometryHistory | null;
	observations: PlantObservation[] | null;
};
export type Plant = Entity<typeof plantSchema, 'plants'> & {
	expectedLifespan: Lifespan | null;
	recordedLifespan: Lifespan | null;
};
export type PlantGroup = Entity<typeof plantSchema, 'plantGroups'>;

export const OriginEnumLabels: Record<Origin, string> = {
	DIRECT_SEED: 'Direct Seed',
	SEEDLING_TO_TRANSPLANT: 'Seedling to Transplant',
	SEED_TO_TRANSPLANT: 'Seed to Transplant'
};
