import { boolean, jsonb, pgEnum, pgTable, text, uuid } from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';

import { gardens } from '../gardens/schema.js';
import { geometryHistories, locationHistories } from '../workspaces/schema.js';
import type { EnvironmentAttributesUpdateCommand } from './attributes/index.js';

/**
 * Defines the parent entity that the environment describes characteristics for.
 * GARDEN: the environment applies to a garden.
 * WORKSPACE: the environment applies to a workspace.
 * PLANTING_AREA: the environment applies to a planting area.
 * INDEPENDENT: the environment applies to an independent geometry.
 */
export const EnvironmentParentTypeEnumOptions = [
	'GARDEN',
	'WORKSPACE',
	'PLANTING_AREA',
	'INDEPENDENT'
] as const;

export const environmentParentTypeEnum = pgEnum(
	'environment_parent_type',
	EnvironmentParentTypeEnumOptions
);

export const environments = pgTable('environments', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** Non-unique name of the environment. */
	name: text('name').notNull(),

	/** Optional description. */
	description: text('description').default('').notNull(),

	/** Type of the parent entity the environment describes. */
	parentType: environmentParentTypeEnum('parent_type').default('GARDEN').notNull(),

	/** Garden the environment exists in — always set regardless of parentType. */
	gardenId: text('garden_id')
		.notNull()
		.references(() => gardens.id, { onDelete: 'cascade' }),

	/** Workspace IDs this environment applies to. Set when parentType = 'WORKSPACE'. */
	workspaceIds: text('workspace_ids').array(),

	/** Planting area IDs this environment applies to. Set when parentType = 'PLANTING_AREA'. */
	plantingAreaIds: text('planting_area_ids').array(),

	/** Geometry history ID. Set when parentType = 'INDEPENDENT'. */
	geometryHistoryId: uuid('geometry_history_id'),

	/** Location history ID. Set when parentType = 'INDEPENDENT'. */
	locationHistoryId: uuid('location_history_id'),

	/**
	 * If true, inherits attributes from environments defined at higher levels,
	 * e.g. a planting area environment inherits from the workspace environment.
	 */
	inherit: boolean('inherit').default(true).notNull(),

	/** Typed jsonb attribute store. Structure depends on parentType. */
	attributes: jsonb('attributes').$type<EnvironmentAttributesUpdateCommand>().notNull()
});

export const environmentsRelations = relations(environments, ({ one }) => ({
	garden: one(gardens, {
		fields: [environments.gardenId],
		references: [gardens.id]
	}),
	geometryHistory: one(geometryHistories, {
		fields: [environments.geometryHistoryId],
		references: [geometryHistories.id]
	}),
	locationHistory: one(locationHistories, {
		fields: [environments.locationHistoryId],
		references: [locationHistories.id]
	})
}));

export type Environment = typeof environments.$inferSelect;
export type EnvironmentParent = (typeof EnvironmentParentTypeEnumOptions)[number];
