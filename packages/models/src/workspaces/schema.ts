import { co, z } from 'jazz-tools';

import fields, { GeometryTypeEnumOptions } from './fields.js';

export type Coordinate = z.infer<typeof fields.coordinateField>;

/************************************
 * Physical primitives
 ************************************/

/**
 * @title Geometry.
 */
export const GeometrySchema = co.map({
	date: fields.geometryDateField,
	scaleFactor: fields.geometryScaleFactorField,
	rotation: fields.geometryRotationField,
	attributes: co.discriminatedUnion('type', [
		co.map({
			type: z.literal('RECTANGLE'),
			rectangleLength: fields.geometryRectangleLengthField,
			rectangleWidth: fields.geometryRectangleWidthField
		}),
		co.map({
			type: z.literal('ELLIPSE'),
			ellipseLength: fields.geometryEllipseLengthField,
			ellipseWidth: fields.geometryEllipseWidthField
		}),
		co.map({
			type: z.literal('POLYGON'),
			polygonNumSides: fields.geometryPolygonNumSidesField,
			polygonRadius: fields.geometryPolygonRadiusField
		}),
		co.map({
			type: z.literal('LINES'),
			linesCoordinates: z.array(fields.coordinateField),
			linesClosed: fields.geometryLinesClosedField
		})
	])
});
export type GeometryType = (typeof GeometryTypeEnumOptions)[number];
export type Geometry = co.loaded<typeof GeometrySchema, { attributes: true }>;
export type GeometryAttributes = Geometry['attributes'];

/**
 * @title Location.
 */
export const LocationSchema = co.map({
	date: fields.locationDateField,
	coordinate: fields.coordinateField,
	get workspace() {
		return WorkspaceSchema;
	}
});
export type Location = co.loaded<typeof LocationSchema>;

/************************************
 * History Containers
 ************************************/

/**
 * @title Geometry History.
 */
export const GeometryHistorySchema = co.list(GeometrySchema);
export type GeometryHistory = co.loaded<typeof GeometryHistorySchema>;

/**
 * @title Location History
 */
export const LocationHistorySchema = co.list(LocationSchema);
export type LocationHistory = co.loaded<typeof LocationHistorySchema>;

export const ObjectHistorySchema = co.map({
	geometries: GeometryHistorySchema,
	locations: LocationHistorySchema
});
export type ObjectHistory = co.loaded<
	typeof ObjectHistorySchema,
	{
		locations: { $each: true };
		geometries: { $each: { attributes: true } };
	}
>;

/************************************
 * Worskpace Objects
 ************************************/
/**
 * @title Planting Area.
 */
export const PlantingAreaSchema = co.map({
	name: fields.plantingAreaNameField,
	description: co.plainText(),
	history: ObjectHistorySchema,
	depth: fields.plantingAreaDepthField
});
export type PlantingArea = co.loaded<typeof PlantingAreaSchema>;

/************************************
 * Workspace
 ************************************/

/**
 * @title Workspace.
 */
export const WorkspaceSchema = co.map({
	name: fields.workspaceNameField,
	slug: z.string(),
	description: co.plainText(),
	plantingAreas: co.list(PlantingAreaSchema)
});
export type Workspace = co.loaded<typeof WorkspaceSchema>;










