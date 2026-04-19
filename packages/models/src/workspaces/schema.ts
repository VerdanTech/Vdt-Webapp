import { co, z } from 'jazz-tools';

import fields, { GeometryTypeEnumOptions } from './fields.js';

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

export const GeometryHistorySchema = co.list(GeometrySchema);

const LocationSchema = co.map({
	date: fields.locationDateField,
	coordinate: fields.coordinateField,
	get workspace() {
		return WorkspaceSchema;
	}
});

export const LocationHistorySchema = co.list(LocationSchema);

export const ObjectHistorySchema = co.map({
	geometry: GeometryHistorySchema,
	location: LocationHistorySchema
});

export const PlantingAreaSchema = co.map({
	name: fields.plantingAreaNameField,
	description: co.plainText(),
	history: ObjectHistorySchema,
	depth: fields.plantingAreaDepthField
});

export const WorkspaceSchema = co.map({
	name: fields.workspaceNameField,
	slug: z.string(),
	description: co.plainText(),
	plantingAreas: co.list(PlantingAreaSchema)
});

export type Coordinate = z.infer<typeof fields.coordinateField>;
export type Geometry = co.loaded<typeof GeometrySchema>;
export type GeometryAttributes = Geometry['attributes'];
export type GeometryType = (typeof GeometryTypeEnumOptions)[number];
export type GeometryHistory = co.loaded<typeof GeometryHistorySchema>;
export type Location = co.loaded<typeof LocationSchema>;
export type LocationHistory = co.loaded<typeof LocationHistorySchema>;
export type ObjectHistory = co.loaded<typeof ObjectHistorySchema>;
export type PlantingArea = co.loaded<typeof PlantingAreaSchema>;
export type Workspace = co.loaded<typeof WorkspaceSchema>;
