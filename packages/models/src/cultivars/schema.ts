import { jsonb, pgEnum, pgTable, real, text, timestamp, uuid } from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';

import { gardens } from '../gardens/schema.js';
import { profiles } from '../users/schema.js';
import type { CultivarAttributesUpdateCommand } from './attributes/index.js';

/**
 * Controls the visibility of the collection.
 * HIDDEN: visible only to garden members or the owning user.
 * UNLISTED: visible to anyone with a link.
 * PUBLIC: visible to anyone and may be searchable.
 */
export const CultivarCollectionVisibilityEnumOptions = [
	'HIDDEN',
	'UNLISTED',
	'PUBLIC'
] as const;

export const cultivarCollectionVisibilityEnum = pgEnum(
	'cultivar_collection_visibility',
	CultivarCollectionVisibilityEnumOptions
);

export const cultivarCollections = pgTable('cultivar_collections', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** Non-unique name of the collection. */
	name: text('name').notNull(),

	/** Unique URL slug. */
	slug: text('slug').notNull().unique(),

	/** Visibility of the collection. */
	visibility: cultivarCollectionVisibilityEnum('visibility').notNull(),

	/** If set, the collection is owned by a user. */
	userId: uuid('user_id').references(() => profiles.id),

	/** If set, the collection is owned by a garden. Overrides user ownership. */
	gardenId: text('garden_id').references(() => gardens.id),

	/** Priority used to resolve which collection wins when multiple match in a garden. */
	priority: real('priority').default(0).notNull(),

	/** Optional description. */
	description: text('description').default('').notNull(),

	/**
	 * Optional parent collection to derive attributes from.
	 * Ancestor traversal uses a recursive CTE — no ancestorIds denormalization needed.
	 */
	parentId: uuid('parent_id'),

	createdAt: timestamp('created_at').defaultNow().notNull()
});

export const cultivars = pgTable('cultivars', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** Collection the cultivar belongs to. */
	collectionId: uuid('collection_id')
		.notNull()
		.references(() => cultivarCollections.id, { onDelete: 'cascade' }),

	/** Common name. Used to match plants to cultivars. */
	name: text('name').notNull(),

	/** Short abbreviation. */
	abbreviation: text('abbreviation').notNull(),

	/** Optional scientific name. */
	scientificName: text('scientific_name'),

	/** Optional description. */
	description: text('description').default('').notNull(),

	/** Optional parent cultivar for attribute inheritance. */
	parentId: uuid('parent_id'),

	/** Typed jsonb attribute store. */
	attributes: jsonb('attributes').$type<CultivarAttributesUpdateCommand>().notNull(),

	createdAt: timestamp('created_at').defaultNow().notNull()
});

export const cultivarCollectionsRelations = relations(
	cultivarCollections,
	({ one, many }) => ({
		user: one(profiles, {
			fields: [cultivarCollections.userId],
			references: [profiles.id]
		}),
		garden: one(gardens, {
			fields: [cultivarCollections.gardenId],
			references: [gardens.id]
		}),
		parent: one(cultivarCollections, {
			fields: [cultivarCollections.parentId],
			references: [cultivarCollections.id],
			relationName: 'collection_parent'
		}),
		children: many(cultivarCollections, { relationName: 'collection_parent' }),
		cultivars: many(cultivars)
	})
);

export const cultivarsRelations = relations(cultivars, ({ one }) => ({
	collection: one(cultivarCollections, {
		fields: [cultivars.collectionId],
		references: [cultivarCollections.id]
	}),
	parent: one(cultivars, {
		fields: [cultivars.parentId],
		references: [cultivars.id],
		relationName: 'cultivar_parent'
	})
}));

export type Cultivar = typeof cultivars.$inferSelect;
export type CultivarCollection = typeof cultivarCollections.$inferSelect;
export type CultivarCollectionVisibility =
	(typeof CultivarCollectionVisibilityEnumOptions)[number];
