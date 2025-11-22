import { type Entity, type QueryResult, Schema as S, or } from '@triplit/client';

import { CultivarAttributes } from '../cultivars/attributes/index.js';
import { cultivarSchema } from '../cultivars/schema.js';
import { GeometryHistory, LocationHistory } from '../workspaces/schema.js';

/**
 *
 */
export const OriginEnumOptions = [
	'DIRECT_SEED',
	'SEED_TO_TRANSPLANT',
	'SEEDLING_TO_TRANSPLANT'
] as const;

export const LifespanDatesOptions = [
	'SEED',
	'GERMINATION',
	'MATURE',
	'DORMANCY',
	'GROWTH',
	'EXPIRY',
] as const

export const HarvestQualityEnumOptions = [
	'COMPOST',
	'LOW',
	'MEDIUM',
	'HIGH',
	'PERFECT'
] as const;

export const plantSchema = S.Collections({
	...cultivarSchema,
	/** Harvest schema. */
	harvests: {
		schema: S.Schema({
			id: S.Id(),

			/** Garden the entity is located within - required for access control. */
			gardenId: S.String(),

			/** Lifespans which are included in the harvest. */
			lifespanIds: S.Set(S.String(), { default: S.Default.Set.empty() }),

			/** The date of the harvest. */
			date: S.Date(),

			/** The mass of the harvest in kilograms. */
			mass: S.Optional(S.Number()),

			/** The quality of the harvest. */
			quality: S.Optional(S.String({ enum: [...HarvestQualityEnumOptions] })),

			/** Optional description. */
			description: S.String({ default: '' })
		}),
		relationships: {
			garden: S.RelationById('gardens', '$gardenId'),
			lifespans: S.RelationMany('lifespans', { where: [['id', 'in', '$lifespanIds']] })
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
					/** Allow new harvests to be created by admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				update: {
					/** Restrict harvest updates to admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				delete: {
					/** Restrict harvest deletes to admins and editors. */
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
	/** Lifespan date schema. */
	lifespanDates: {
		schema: S.Schema({
			id: S.Id(),

			/** Garden the entity is located within - required for access control. */
			gardenId: S.String(),

			/** Type of date that the value represents. */
			dateId: S.String(),

			/** Date value. */
			value: S.Date(),

			/** Optional unstructured data. */
			extra: S.Optional(S.Json({})),
		}),
		relationships: {
			garden: S.RelationById('gardens', '$gardenId'),
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
					/** Allow new lifespan dates to be created by admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				update: {
					/** Restrict lifespan date updates to admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				delete: {
					/** Restrict lifespan date deletes to admins and editors. */
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

			/** The locations of the lifespan& */
			locationHistoryId: S.Optional(S.String()),

			/** The dates of the lifespan. */
			dates: S.Record({

			})
		}),
		relationships: {
			garden: S.RelationById('gardens', '$gardenId'),
			geometryHistory: S.RelationById('geometryHistories', '$geometryHistoryId'),
			locationHistory: S.RelationById('locationHistories', '$locationHistoryId'),
			harvests: S.RelationMany('harvests', { where: [['id', 'in', '$harvestIds']] })
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

			/** The number of distinct plants which are managed together in this plant instance. */
			quantity: S.Number({ default: 1 })
		}),
		relationships: {
			garden: S.RelationById('gardens', '$gardenId'),
			expectedLifespan: S.RelationById('lifespans', '$expectedLifespanId'),
			recordedLifespan: S.RelationById('lifespans', '$recordedLifespanId')
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
export type Harvest = Entity<typeof plantSchema, 'harvests'>;
export type Lifespan = Entity<typeof plantSchema, 'lifespans'> & {
	locationHistory: LocationHistory | null;
	geometryHistory: GeometryHistory | null;
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
