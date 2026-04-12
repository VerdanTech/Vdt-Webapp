import {
	boolean,
	jsonb,
	pgEnum,
	pgTable,
	real,
	text,
	timestamp,
	uuid
} from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';

import { gardens } from '../gardens/schema.js';

/**
 * Specifies a type of geometry.
 * RECTANGLE: closed shape specified by width and height.
 * POLYGON: closed shape specified by number of sides and radius.
 * ELLIPSE: closed shape specified by major and minor radius.
 * LINES: open or closed shape specified by inline coordinate points.
 */
export const GeometryTypeEnumOptions = [
	'RECTANGLE',
	'POLYGON',
	'ELLIPSE',
	'LINES'
] as const;

export const geometryTypeEnum = pgEnum('geometry_type', GeometryTypeEnumOptions);

/** Inline coordinate type used by LINES geometries. */
export type LinesCoordinate = { x: number; y: number };

export const workspaces = pgTable('workspaces', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** Garden the workspace belongs to. */
	gardenId: text('garden_id')
		.notNull()
		.references(() => gardens.id, { onDelete: 'cascade' }),

	/** Name of the workspace. */
	name: text('name').notNull(),

	/** URL-friendly shorthand of the name. */
	slug: text('slug').notNull(),

	/** Optional description. */
	description: text('description').default('').notNull()
});

export const locations = pgTable('locations', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** Garden the entity is located within. */
	gardenId: text('garden_id')
		.notNull()
		.references(() => gardens.id, { onDelete: 'cascade' }),

	/** The workspace the location is in. */
	workspaceId: uuid('workspace_id')
		.notNull()
		.references(() => workspaces.id, { onDelete: 'cascade' }),

	/** Horizontal X component in meters. */
	x: real('x').notNull(),

	/** Vertical Y component in meters. */
	y: real('y').notNull(),

	/** Depth/altitude in meters. */
	z: real('z').default(0),

	/** The date at which the location applies. */
	date: timestamp('date').notNull()
});

export const locationHistories = pgTable('location_histories', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** Garden the entity is located within. */
	gardenId: text('garden_id')
		.notNull()
		.references(() => gardens.id, { onDelete: 'cascade' }),

	/**
	 * Ordered set of location IDs describing a history of positional change.
	 * Locations are ordered by their date column when queried.
	 * Note: workspaceIds is intentionally omitted — derive with a JOIN query when needed.
	 */
	locationIds: text('location_ids').array().notNull().default([])
});

export const geometries = pgTable('geometries', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** Garden the entity is located within. */
	gardenId: text('garden_id')
		.notNull()
		.references(() => gardens.id, { onDelete: 'cascade' }),

	/**
	 * Type of the geometry. Determines which attribute columns are used.
	 */
	type: geometryTypeEnum('type').notNull(),

	/** The date at which this geometry applies. */
	date: timestamp('date').notNull(),

	/** Scalar size multiplier. */
	scaleFactor: real('scale_factor').default(1).notNull(),

	/** Rotation about center in degrees. */
	rotation: real('rotation').default(0).notNull(),

	/** RECTANGLE: horizontal length in meters. */
	rectangleLength: real('rectangle_length').default(1).notNull(),

	/** RECTANGLE: vertical width in meters. */
	rectangleWidth: real('rectangle_width').default(1).notNull(),

	/** POLYGON: number of sides. */
	polygonNumSides: real('polygon_num_sides').default(3).notNull(),

	/** POLYGON: radius from center to vertex in meters. */
	polygonRadius: real('polygon_radius').default(1).notNull(),

	/** ELLIPSE: horizontal diameter in meters. */
	ellipseLength: real('ellipse_length').default(1).notNull(),

	/** ELLIPSE: vertical diameter in meters. */
	ellipseWidth: real('ellipse_width').default(1).notNull(),

	/**
	 * LINES: inline coordinate points.
	 * Stored as jsonb rather than a separate table — coordinates are private
	 * to a single geometry and always fetched together with it.
	 */
	linesCoordinates: jsonb('lines_coordinates')
		.$type<LinesCoordinate[]>()
		.default([])
		.notNull(),

	/** LINES: if true, the first and last points are connected. */
	linesClosed: boolean('lines_closed').default(true).notNull()
});

export const geometryHistories = pgTable('geometry_histories', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** Garden the entity is located within. */
	gardenId: text('garden_id')
		.notNull()
		.references(() => gardens.id, { onDelete: 'cascade' }),

	/**
	 * Ordered set of geometry IDs describing a history of geometric change.
	 * Geometries are ordered by their date column when queried.
	 */
	geometryIds: text('geometry_ids').array().notNull().default([])
});

export const plantingAreas = pgTable('planting_areas', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** Garden the entity is located within. */
	gardenId: text('garden_id')
		.notNull()
		.references(() => gardens.id, { onDelete: 'cascade' }),

	/** Name. */
	name: text('name').notNull(),

	/** The geometry of the planting area. */
	geometryId: uuid('geometry_id')
		.notNull()
		.references(() => geometries.id),

	/** The location history of the planting area. */
	locationHistoryId: uuid('location_history_id')
		.notNull()
		.references(() => locationHistories.id),

	/** Depth in meters — used to calculate volume. */
	depth: real('depth').default(0).notNull(),

	/** Optional description. */
	description: text('description').default('').notNull()
});

/** Relations. */

export const workspacesRelations = relations(workspaces, ({ one }) => ({
	garden: one(gardens, { fields: [workspaces.gardenId], references: [gardens.id] })
}));

export const locationsRelations = relations(locations, ({ one }) => ({
	garden: one(gardens, { fields: [locations.gardenId], references: [gardens.id] }),
	workspace: one(workspaces, {
		fields: [locations.workspaceId],
		references: [workspaces.id]
	})
}));

export const locationHistoriesRelations = relations(locationHistories, ({ one }) => ({
	garden: one(gardens, {
		fields: [locationHistories.gardenId],
		references: [gardens.id]
	})
}));

export const geometriesRelations = relations(geometries, ({ one }) => ({
	garden: one(gardens, { fields: [geometries.gardenId], references: [gardens.id] })
}));

export const geometryHistoriesRelations = relations(geometryHistories, ({ one }) => ({
	garden: one(gardens, {
		fields: [geometryHistories.gardenId],
		references: [gardens.id]
	})
}));

export const plantingAreasRelations = relations(plantingAreas, ({ one }) => ({
	garden: one(gardens, { fields: [plantingAreas.gardenId], references: [gardens.id] }),
	geometry: one(geometries, {
		fields: [plantingAreas.geometryId],
		references: [geometries.id]
	}),
	locationHistory: one(locationHistories, {
		fields: [plantingAreas.locationHistoryId],
		references: [locationHistories.id]
	})
}));

export type Workspace = typeof workspaces.$inferSelect;
export type Location = typeof locations.$inferSelect;
export type LocationHistory = typeof locationHistories.$inferSelect;
export type Geometry = typeof geometries.$inferSelect;
export type GeometryHistory = typeof geometryHistories.$inferSelect;
export type PlantingArea = typeof plantingAreas.$inferSelect;
export type GeometryType = (typeof GeometryTypeEnumOptions)[number];
export type Position = Pick<Location, 'x' | 'y'>;
