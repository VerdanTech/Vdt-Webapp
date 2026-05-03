import { type TableRow, schema as s } from 'jazz-tools';

import { CultivarAttributesUpdateCommandSchema } from './attributes/index.js';

/**
 * Controls the visibility of the collection.
 * HIDDEN: the collection is visible only to those who are members of the garden,
 * or only to the user if the collection is associated with a user.
 * UNLISTED: the collection is visible to anyone but is not listed on any public page.
 * PUBLIC: the collection is visible to anyone and may be searchable.
 */
export const CultivarCollectionVisibilityEnumOptions = [
	'HIDDEN',
	'UNLISTED',
	'PUBLIC'
] as const;

export const cultivarSchema = {
	/** CultivarCollection schema. */
	cultivarCollections: s.table({
		/** Non-unique name of the collection. */
		name: s.string(),

		/** Unique URL slug. */
		slug: s.string(),

		/** Visibility of the collection. */
		visibility: s.enum(...CultivarCollectionVisibilityEnumOptions),

		/** If defined, the collection is owned by a user. */
		userId: s.ref('users').optional(),

		/** If defined, the collection is owned by a garden. Overrides user ownership. */
		gardenId: s.ref('gardens').optional(),

		/** Optional priority flag used to decide between collections in a garden. */
		priority: s.int().default(0),

		/** Optional description. */
		description: s.string().default(''),

		/** Optional parent collection to derive attributes from. */
		parentId: s.ref('cultivarCollections').optional(),

		/**
		 * Optional list of ancestor IDs (parent and their parent, up to fixed depth).
		 * Denormalized data maintained on update to support reactive querying.
		 */
		ancestorIds: s.array(s.string()).default([])
	}),

	/** Cultivar schema. */
	cultivars: s.table({
		/** Collection the cultivar is in. */
		collectionId: s.ref('cultivarCollections'),

		/** A common name. Used to match plants to cultivars. */
		name: s.string(),

		/** Shorthand. */
		abbreviation: s.string(),

		/** Optional scientific name. */
		scientificName: s.string().optional(),

		/** Optional description. */
		description: s.string().default(''),

		/** Optional parent cultivar to derive attributes from. */
		parentId: s.ref('cultivars').optional(),

		/** Attributes which define this cultivar. */
		attributes: s.json(CultivarAttributesUpdateCommandSchema).optional(),

		/** Creation timestamp used for newest-first resolution of duplicate names. */
		createdAt: s.timestamp()
	})
};

export type Cultivar = TableRow<typeof cultivarSchema, 'cultivars'>;
export type CultivarCollection = TableRow<typeof cultivarSchema, 'cultivarCollections'>;
export type CultivarCollectionVisibility =
	(typeof CultivarCollectionVisibilityEnumOptions)[number];
