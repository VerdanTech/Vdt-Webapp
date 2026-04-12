import { jsonb, pgTable, text, timestamp, uuid } from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';

import { gardens } from '../gardens/schema.js';
import { ObservationIds } from './ids.js';

export const observations = pgTable('observations', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** Garden the observation belongs to. */
	gardenId: text('garden_id')
		.notNull()
		.references(() => gardens.id, { onDelete: 'cascade' }),

	/** Type of observation — drives the shape of the data field. */
	type: text('type', { enum: ObservationIds as [string, ...string[]] }).notNull(),

	/** IDs of the primary entities this observation applies to. */
	entityIds: text('entity_ids').array().notNull().default([]),

	/** Date of the observation. */
	date: timestamp('date').notNull(),

	/**
	 * Flexible jsonb data store. Structure is determined by the type field.
	 * Typed via the generic Observation<TData> wrapper at the application layer.
	 */
	data: jsonb('data')
});

export const observationsRelations = relations(observations, ({ one }) => ({
	garden: one(gardens, { fields: [observations.gardenId], references: [gardens.id] })
}));

export type GenericObservation = typeof observations.$inferSelect;
export type Observation<TData> = Omit<GenericObservation, 'data'> & { data: TData };
