import { integer, jsonb, pgEnum, pgTable, text, timestamp, uuid } from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';

import { gardens } from '../gardens/schema.js';
import type { CultivarAttributesUpdateCommand } from '../cultivars/attributes/index.js';
import { geometryHistories, locationHistories } from '../workspaces/schema.js';

export const OriginEnumOptions = [
	'DIRECT_SEED',
	'SEED_TO_TRANSPLANT',
	'SEEDLING_TO_TRANSPLANT'
] as const;

export const originEnum = pgEnum('origin', OriginEnumOptions);

export const lifespans = pgTable('lifespans', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** Garden the lifespan belongs to. */
	gardenId: text('garden_id')
		.notNull()
		.references(() => gardens.id, { onDelete: 'cascade' }),

	/** How the plant was started. */
	origin: originEnum('origin').notNull(),

	/** Geometry history for this lifespan. */
	geometryHistoryId: uuid('geometry_history_id').references(() => geometryHistories.id),

	/** Location history for this lifespan. */
	locationHistoryId: uuid('location_history_id').references(() => locationHistories.id)
});

export const plants = pgTable('plants', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** Garden the plant belongs to. */
	gardenId: text('garden_id')
		.notNull()
		.references(() => gardens.id, { onDelete: 'cascade' }),

	/**
	 * Cultivar name matching one of the common names in the garden's cultivar collections.
	 * Resolved at query time via resolveCultivar — not stored as a FK.
	 */
	cultivarName: text('cultivar_name').notNull(),

	/** Cultivar attribute overrides specific to this plant instance. */
	cultivarAttributes: jsonb('cultivar_attributes')
		.$type<CultivarAttributesUpdateCommand>()
		.notNull(),

	/** Expected lifespan, derived from cultivar attributes. */
	expectedLifespanId: uuid('expected_lifespan_id')
		.notNull()
		.references(() => lifespans.id),

	/** Recorded lifespan, built from observations. */
	recordedLifespanId: uuid('recorded_lifespan_id')
		.notNull()
		.references(() => lifespans.id),

	/**
	 * Denormalized date range spanning all dates applicable to this plant.
	 * Updated alongside lifespan changes to avoid complex date range queries.
	 */
	beginDate: timestamp('begin_date').notNull(),
	endDate: timestamp('end_date').notNull(),

	/** Number of distinct plants managed together in this instance. */
	quantity: integer('quantity').default(1).notNull()
});

export const plantGroups = pgTable('plant_groups', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** Garden the group belongs to. */
	gardenId: text('garden_id')
		.notNull()
		.references(() => gardens.id, { onDelete: 'cascade' }),

	/** Name. */
	name: text('name').notNull(),

	/** Plant IDs in this group. */
	plantIds: text('plant_ids').array().notNull().default([]),

	/** Optional description. */
	description: text('description').default('').notNull()
});

/** Relations. */

export const lifespansRelations = relations(lifespans, ({ one }) => ({
	garden: one(gardens, { fields: [lifespans.gardenId], references: [gardens.id] }),
	geometryHistory: one(geometryHistories, {
		fields: [lifespans.geometryHistoryId],
		references: [geometryHistories.id]
	}),
	locationHistory: one(locationHistories, {
		fields: [lifespans.locationHistoryId],
		references: [locationHistories.id]
	})
}));

export const plantsRelations = relations(plants, ({ one }) => ({
	garden: one(gardens, { fields: [plants.gardenId], references: [gardens.id] }),
	expectedLifespan: one(lifespans, {
		fields: [plants.expectedLifespanId],
		references: [lifespans.id],
		relationName: 'expected_lifespan'
	}),
	recordedLifespan: one(lifespans, {
		fields: [plants.recordedLifespanId],
		references: [lifespans.id],
		relationName: 'recorded_lifespan'
	})
}));

export const plantGroupsRelations = relations(plantGroups, ({ one }) => ({
	garden: one(gardens, { fields: [plantGroups.gardenId], references: [gardens.id] })
}));

export type Origin = (typeof OriginEnumOptions)[number];
export type Lifespan = typeof lifespans.$inferSelect;
export type Plant = typeof plants.$inferSelect;
export type PlantGroup = typeof plantGroups.$inferSelect;

export const OriginEnumLabels: Record<Origin, string> = {
	DIRECT_SEED: 'Direct Seed',
	SEEDLING_TO_TRANSPLANT: 'Seedling to Transplant',
	SEED_TO_TRANSPLANT: 'Seed to Transplant'
};
