import { z } from 'jazz-tools';

import fields from './fields.js';

/** Commands. */

/**
 * Create a new location.
 */
export const LocationCreateCommandSchema = z.object({
	gardenId: z.string(),
	workspaceId: z.string(),
	coordinate: fields.coordinateField,
	date: fields.locationDateField
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
	coordinate: fields.coordinateField,
	date: fields.locationDateField
});
export type LocationHistoryUpdateCommand = z.infer<
	typeof LocationHistoryUpdateCommandSchema
>;

/**
 * Updates a location.
 */
export const LocationUpdateCommandSchema = z.object({
	coordinate: fields.coordinateField.optional(),
	date: fields.locationDateField.optional(),
	workspaceId: z.string().optional(),
	delete: z.boolean().optional()
});
export type LocationUpdateCommand = z.infer<typeof LocationUpdateCommandSchema>;

/**
 * Create a new geometry.
 */
export const GeometryCreateCommandSchema = z.object({
	type: fields.geometryTypeField.default('RECTANGLE'),
	date: fields.geometryDateField,
	scaleFactor: fields.geometryScaleFactorField.default(1),
	rotation: fields.geometryRotationField.default(0),
	rectangleLength: fields.geometryRectangleLengthField.default(1),
	rectangleWidth: fields.geometryRectangleWidthField.default(1),
	polygonNumSides: fields.geometryPolygonNumSidesField.default(3),
	polygonRadius: fields.geometryPolygonRadiusField.default(1),
	ellipseLength: fields.geometryEllipseLengthField.default(1),
	ellipseWidth: fields.geometryEllipseWidthField.default(1),
	linesCoordinates: fields.geometryLinesCoordinatesField.default([
		{ x: -1, y: 0 },
		{ x: 0, y: 1 },
		{ x: 1, y: 0 }
	]),
	linesClosed: fields.geometryLinesClosedField.default(true)
});
export type GeometryCreateCommand = z.infer<typeof GeometryCreateCommandSchema>;

/**
 * Update a geometry.
 */
export const GeometryUpdateCommandSchema = z.object({
	type: fields.geometryTypeField.optional(),
	date: fields.geometryDateField.optional(),
	scaleFactor: fields.geometryScaleFactorField.optional(),
	rotation: fields.geometryRotationField.optional(),
	rectangleLength: fields.geometryRectangleLengthField.optional(),
	rectangleWidth: fields.geometryRectangleWidthField.optional(),
	polygonNumSides: fields.geometryPolygonNumSidesField.optional(),
	polygonRadius: fields.geometryPolygonRadiusField.optional(),
	ellipseLength: fields.geometryEllipseLengthField.optional(),
	ellipseWidth: fields.geometryEllipseWidthField.optional(),
	linesCoordinates: fields.geometryLinesCoordinatesField.optional(),
	linesClosed: fields.geometryLinesClosedField.optional(),
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
 * Updates a geometry history.
 */
export const GeometryHistoryUpdateCommandSchema = z.object({
	id: z.string(),
	geometry: GeometryCreateCommandSchema,
	date: fields.geometryDateField
});
export type GeometryHistoryUpdateCommand = z.infer<
	typeof GeometryHistoryUpdateCommandSchema
>;

/**
 * Create a new workspace.
 */
export const WorkspaceCreateCommandSchema = z.object({
	gardenId: z.string(),
	name: fields.workspaceNameField,
	description: fields.workspaceDescriptionField.optional()
});
export type WorkspaceCreateCommand = z.infer<typeof WorkspaceCreateCommandSchema>;

/**
 * Update a workspace.
 */
export const WorkspaceUpdateCommandSchema = z.object({
	name: fields.workspaceNameField.optional(),
	description: fields.workspaceDescriptionField.optional()
});
export type WorkspaceUpdateCommand = z.infer<typeof WorkspaceUpdateCommandSchema>;

/**
 * Create a new planting area.
 */
export const PlantingAreaCreateCommandSchema = z.object({
	gardenId: z.string(),
	workspaceId: z.string(),
	name: fields.plantingAreaNameField,
	description: fields.plantingAreaDescriptionField.default(''),
	location: LocationCreateCommandSchema,
	geometry: GeometryCreateCommandSchema,
	depth: fields.plantingAreaDepthField.default(0)
});
export type PlantingAreaCreateCommand = z.infer<typeof PlantingAreaCreateCommandSchema>;

/**
 * Update a planting area.
 */
export const PlantingAreaUpdateCommandSchema = z.object({
	name: fields.plantingAreaNameField.optional(),
	description: fields.plantingAreaDescriptionField.optional(),
	depth: fields.plantingAreaDepthField.optional()
});
export type PlantingAreaUpdateCommand = z.infer<typeof PlantingAreaUpdateCommandSchema>;
