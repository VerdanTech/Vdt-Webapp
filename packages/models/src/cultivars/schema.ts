import { type Entity, Schema as S, or } from '@triplit/client';

import { environmentSchema } from '../environments/schema.js';
import { CultivarAttributes } from './attributes/index.js';

/**
 * Controls the visibility of the collection.
 * HIDDEN: the collection is visible only to those who are members of the garden,
 * or only to the user if the collection is associated with a user.
 * UNLISTED: the collection is visibile to anyone but is not listed
 *     on any public page - a link is required.
 * PUBLIC: the collection is visible to anyone and may be searchable.
 */
export const CultivarCollectionVisibilityEnumOptions = [
	'HIDDEN',
	'UNLISTED',
	'PUBLIC'
] as const;

export const cultivarSchema = S.Collections({
	...environmentSchema,
	/** Collection schema. */
	cultivarCollections: {
		schema: S.Schema({
			/** URL-friendly shorthand - unique. */
			id: S.Id(),

			/** Non-unique name of the collection. */
			name: S.String(),

			/** Unique URL slug. */
			slug: S.String(),

			/** Visibility of the collection.  */
			visibility: S.String({ enum: [...CultivarCollectionVisibilityEnumOptions] }),

			/** If defined, the collection is owned by a user. */
			userId: S.String({ nullable: true, default: null }),

			/** If defined, the colletcion is owned by a garden. Overrides user ownership. */
			gardenId: S.String({ nullable: true, default: null }),

			/** Optional description. */
			description: S.String({ default: '' }),

			/** Optional parent collection to derive attributes from. */
			parentId: S.String({ nullable: true, default: null })
		}),
		relationships: {
			user: S.RelationById('profiles', 'userId'),
			garden: S.RelationById('gardens', '$gardenId'),
			parent: S.RelationById('cultivarCollections', '$parentId')
		},
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the collection is not hidden. */
					filter: [['visibility', '!=', 'HIDDEN']]
				}
			},
			user: {
				read: {
					/** Allow reads if the collection is not hidden,
					 *  the garden is defined and the user is a member,
					 *  or the user is defined and the user is the owner. */
					filter: [
						or([
							['visibility', '!=', 'HIDDEN'],
							['userId', '=', '$role.profileId'],
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId'],
							['garden.viewerIds', 'has', '$role.profileId']
						])
					]
				},
				insert: {
					/**
					 * Allow new collections to be created:
					 * if the garden is defined, the user must be an admin in the garden.
					 * Otherwise, the user can create their own collections.
					 */
					filter: [
						or([
							['userId', '=', '$role.profileId'],
							['garden.adminIds', 'has', '$role.profileId']
						])
					]
				},
				update: {
					/**
					 * Allow collections to be update:
					 * if the garden is defined, the user must be an admin in the garden.
					 * Otherwise, the user can update their own collections.
					 */
					filter: [
						or([
							['userId', '=', '$role.profileId'],
							['garden.adminIds', 'has', '$role.profileId']
						])
					]
				},
				delete: {
					/**
					 * Allow collections to be deleted:
					 * if the garden is defined, the user must be an admin in the garden.
					 * Otherwise, the user can deleted their own collections.
					 */
					filter: [
						or([
							['userId', '=', '$role.profileId'],
							['garden.adminIds', 'has', '$role.profileId']
						])
					]
				}
			}
		}
	},

	/** Cultivar schema. */
	cultivars: {
		schema: S.Schema({
			id: S.Id(),

			/** Collection the cultivar is in. */
			collectionId: S.String(),

			/** A list of common names. Used to match plants to cultivars. */
			names: S.Set(S.String()),

			/** Shorthand. */
			abbreviation: S.String(),

			/** Optional scientific name. */
			scientificName: S.Optional(S.String()),

			/** Optional description. */
			description: S.String({ default: '' }),

			/** Optional parent cultivar to derive attributes from. */
			parentId: S.String({ nullable: true, default: null }),

			/** Attributes which define this cultivar. */
			attributes: CultivarAttributes
		}),
		relationships: {
			collection: S.RelationById('cultivarCollections', '$collectionId'),
			parent: S.RelationById('cultivars', '$parentId')
		},
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the collection is not hidden. */
					filter: [['collection.visibility', '!=', 'HIDDEN']]
				}
			},
			user: {
				read: {
					/** Allow reads if the collection is not hidden,
					 *  the garden is defined and the user is a member,
					 *  or the user is defined and the user is the owner. */
					filter: [
						or([
							['collection.visibility', '!=', 'HIDDEN'],
							['collection.userId', '=', '$role.profileId'],
							['collection.garden.adminIds', 'has', '$role.profileId'],
							['collection.garden.editorIds', 'has', '$role.profileId'],
							['collection.garden.viewerIds', 'has', '$role.profileId']
						])
					]
				},
				insert: {
					/**
					 * Allow new cultivars to be created:
					 * if the garden is defined, the user must be an admin in the garden.
					 * Otherwise, the user can create their own collections.
					 */
					filter: [
						or([
							['collection.userId', '=', '$role.profileId'],
							['collection.garden.adminIds', 'has', '$role.profileId']
						])
					]
				},
				update: {
					/**
					 * Allow cultivars to be update:
					 * if the garden is defined, the user must be an admin in the garden.
					 * Otherwise, the user can update their own collections.
					 */
					filter: [
						or([
							['collection.userId', '=', '$role.profileId'],
							['collection.garden.adminIds', 'has', '$role.profileId']
						])
					]
				},
				delete: {
					/**
					 * Allow cultivars to be deleted:
					 * if the garden is defined, the user must be an admin in the garden.
					 * Otherwise, the user can deleted their own collections.
					 */
					filter: [
						or([
							['collection.userId', '=', '$role.profileId'],
							['collection.garden.adminIds', 'has', '$role.profileId']
						])
					]
				}
			}
		}
	}
});
export type Cultivar = Entity<typeof cultivarSchema, 'cultivars'>;
export type CultivarCollection = Entity<typeof cultivarSchema, 'cultivarCollections'>;
