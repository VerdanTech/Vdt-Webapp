import z from 'zod';

import { commonFields } from '../commands.js';
import { GeometryTypeEnumOptions } from './schema.js';

/** Field specifications. */

/** Workspaces. */
const workspaceNameSchema = commonFields.nameSchema.describe(
	'Name of the workspace. Must be unique within a garden.'
);
const workspaceDescriptionSchema = commonFields.descriptionSchema.describe(
	'Optional description.'
);

/** Planting areas. */
const plantingAreaNameSchema = commonFields.nameSchema.describe(
	'The name of the planting area.'
);
const plantingAreaDescriptionSchema = commonFields.descriptionSchema.describe(
	'Optional description.'
);
const plantingAreaDepthSchema = z
	.number()
	.min(0, 'May not be negative')
	.max(1000, 'May be at most 1000m.')
	.describe('The depth of the planting area.');

/** Geometries.  */
const coordinateXSchema = z
	.number()
	.min(-1000000, 'Limited to 1 000 000 meters.')
	.max(1000000, 'Limited to 1 000 000 meters.')
	.describe('The horizontal X component of the coordinate.');
const coordinateYSchema = z
	.number()
	.min(-1000000, 'Limited to 1 000 000 meters.')
	.max(1000000, 'Limited to 1 000 000 meters.')
	.describe('The vertical Y component of the coordinate.');
const coordinateSchema = z
	.object({
		x: coordinateXSchema,
		y: coordinateYSchema
	})
	.describe('A position relative to the origin of a workspace or a geometry.');
const locationDateSchema = z.date().describe('The date at which the location applies.');

const geometryTypeSchema = z
	.enum(GeometryTypeEnumOptions)
	.describe(
		'Describes the type of geometry. Each type has a unique set of attributes associated with it.'
	);
const geometryDateSchema = z
	.date()
	.describe('The date at which the geometry applies to the object.');
const geometryScaleFactorSchema = z
	.number()
	.min(0.01, 'Must be at least 1%.')
	.max(100, 'May be at most 10000%')
	.describe(
		'Factor used to scale the geometry up or down. Must be within 1 and 1000 percent.'
	);
const geometryRotationSchema = z
	.number()
	.min(-360, 'Must be at least negative 360 degrees.')
	.max(360, 'May be at most 360 degrees.')
	.describe(
		'The rotation of the geometry in degrees. Must be between 0 and 360 degrees.'
	);
const geometryRectangleLengthSchema = z
	.number()
	.min(0.01, 'May not be negative or zero.')
	.max(1000, 'May be at most 1000m')
	.describe('The horizontal, or x-axis length of the rectangle.');
const geometryRectangleWidthSchema = z
	.number()
	.min(0.01, 'May not be negative or zero.')
	.max(1000, 'May be at most 1000m')
	.describe('The vertical, or y-axis width of the rectangle.');
const geometryPolygonNumSidesSchema = z
	.number()
	.min(3, 'Must have at least 3 sides.')
	.max(20, 'May have at most 20 sides.')
	.describe('The amount of sides the polygon has.');
const geometryPolygonRadiusSchema = z
	.number()
	.min(0.01, 'May not be negative or zero.')
	.max(1000, 'May be at most 1000m')
	.describe('The distance from the center to any vertex of the polygon.');
const geometryEllipseLengthSchema = z
	.number()
	.min(0.01, 'May not be negative or zero.')
	.max(1000, 'May be at most 1000m.')
	.describe('The horizontal, or x-axis diameter of the ellipse.');
const geometryEllipseWidthSchema = z
	.number()
	.min(0.01, 'May not be negative or zero.')
	.max(1000, 'May be at most 1000m')
	.describe(
		'The vertical, or y-axis diameter of the ellipse. Must be between 0 and 1000 meters.'
	);
const geometryLinesCoordinatesSchema = z
	.array(coordinateSchema)
	.min(3, 'Must have at least 3 points.')
	.describe(
		'A list of coordinates relative to the position of the geometry which define an irregular polygonal.'
	);
const geometryLinesClosedSchema = z
	.boolean()
	.describe('If true, the line segments form a closed shape.');
export const workspaceFields = {
	workspaceNameSchema,
	workspaceDescriptionSchema,
	plantingAreaNameSchema,
	plantingAreaDescriptionSchema,
	plantingAreaDepthSchema,
	coordinateXSchema,
	coordinateYSchema,
	coordinateSchema,
	locationDateSchema,
	geometryTypeSchema,
	geometryDateSchema,
	geometryScaleFactorSchema,
	geometryRotationSchema,
	geometryRectangleLengthSchema,
	geometryRectangleWidthSchema,
	geometryPolygonNumSidesSchema,
	geometryPolygonRadiusSchema,
	geometryEllipseLengthSchema,
	geometryEllipseWidthSchema,
	geometryLinesCoordinatesSchema,
	geometryLinesClosedSchema
};

/** Commands. */

/**
 * Create a new location.
 */
export const LocationCreateCommandSchema = z.object({
	gardenId: z.string(),
	workspaceId: z.string(),
	coordinate: coordinateSchema,
	date: locationDateSchema
});
export type LocationCreateCommand = z.infer<typeof LocationCreateCommandSchema>;

/**
 * Creates a location history.
 */
export const LocationHistoryCreateCommandSchema = z.object({
	gardenId: z.string(),
	locations: z.array(LocationCreateCommandSchema)
});
export type LocationHistoryCreateCommand = z.infer<
	typeof LocationHistoryCreateCommandSchema
>;

/**
 * Updates a location history.
 */
export const LocationHistoryUpdateCommandSchema = z.object({
	id: z.string(),
	workspaceId: z.string(),
	coordinate: coordinateSchema,
	date: locationDateSchema
});
export type LocationHistoryUpdateCommand = z.infer<
	typeof LocationHistoryUpdateCommandSchema
>;

/**
 * Updates a location.
 */
export const LocationUpdateCommandSchema = z.object({
	coordinate: coordinateSchema.optional(),
	date: locationDateSchema.optional(),
	workspaceId: z.string().optional(),
	delete: z.boolean().optional()
});
export type LocationUpdateCommand = z.infer<typeof LocationUpdateCommandSchema>;

/**
 * Updates a location
 */

/**
 * Create a new geometry.
 */
export const GeometryCreateCommandSchema = z.object({
	type: geometryTypeSchema.default('RECTANGLE'),
	date: geometryDateSchema,
	scaleFactor: geometryScaleFactorSchema.default(1),
	rotation: geometryRotationSchema.default(0),
	rectangleLength: geometryRectangleLengthSchema.default(1),
	rectangleWidth: geometryRectangleWidthSchema.default(1),
	polygonNumSides: geometryPolygonNumSidesSchema.default(3),
	polygonRadius: geometryPolygonRadiusSchema.default(1),
	ellipseLength: geometryEllipseLengthSchema.default(1),
	ellipseWidth: geometryEllipseWidthSchema.default(1),
	linesCoordinates: geometryLinesCoordinatesSchema.default([
		{ x: -1, y: 0 },
		{ x: 0, y: 1 },
		{ x: 1, y: 0 }
	]),
	linesClosed: geometryLinesClosedSchema.default(true)
});
export type GeometryCreateCommand = z.infer<typeof GeometryCreateCommandSchema>;

/**
 * Update a geometry.
 */
export const GeometryUpdateCommandSchema = z.object({
	type: geometryTypeSchema.optional(),
	date: geometryDateSchema.optional(),
	scaleFactor: geometryScaleFactorSchema.optional(),
	rotation: geometryRotationSchema.optional(),
	rectangleLength: geometryRectangleLengthSchema.optional(),
	rectangleWidth: geometryRectangleWidthSchema.optional(),
	polygonNumSides: geometryPolygonNumSidesSchema.optional(),
	polygonRadius: geometryPolygonRadiusSchema.optional(),
	ellipseLength: geometryEllipseLengthSchema.optional(),
	ellipseWidth: geometryEllipseWidthSchema.optional(),
	linesCoordinates: geometryLinesCoordinatesSchema.optional(),
	linesClosed: geometryLinesClosedSchema.optional(),
	delete: z.boolean().optional()
});
export type GeometryUpdateCommand = z.infer<typeof GeometryUpdateCommandSchema>;

/**
 * Creates a geometry history.
 */
export const GeometryHistoryCreateCommandSchema = z.object({
	gardenId: z.string(),
	geometries: z.array(GeometryCreateCommandSchema)
});
export type GeometryHistoryCreateCommand = z.infer<
	typeof GeometryHistoryCreateCommandSchema
>;

/**
 * Create a new workspace.
 */
export const WorkspaceCreateCommandSchema = z.object({
	gardenId: z.string(),
	name: workspaceNameSchema,
	description: workspaceDescriptionSchema.optional()
});
export type WorkspaceCreateCommand = z.infer<typeof WorkspaceCreateCommandSchema>;

/**
 * Update a workspace.
 */
export const WorkspaceUpdateCommandSchema = z.object({
	name: workspaceNameSchema.optional(),
	description: workspaceDescriptionSchema.optional()
});
export type WorkspaceUpdateCommand = z.infer<typeof WorkspaceUpdateCommandSchema>;

/**
 * Create a new planting area.
 */
export const PlantingAreaCreateCommandSchema = z.object({
	gardenId: z.string(),
	workspaceId: z.string(),
	name: plantingAreaNameSchema,
	description: plantingAreaDescriptionSchema.default(''),
	location: LocationCreateCommandSchema,
	geometry: GeometryCreateCommandSchema,
	depth: plantingAreaDepthSchema.default(0)
});
export type PlantingAreaCreateCommand = z.infer<typeof PlantingAreaCreateCommandSchema>;

/**
 * Update a planting area.
 */
export const PlantingAreaUpdateCommandSchema = z.object({
	name: plantingAreaNameSchema.optional(),
	description: plantingAreaDescriptionSchema.optional(),
	depth: plantingAreaDepthSchema.optional()
});
export type PlantingAreaUpdateCommand = z.infer<typeof PlantingAreaUpdateCommandSchema>;
