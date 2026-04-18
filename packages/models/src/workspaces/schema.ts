import {co, z} from "jazz-tools"

import fields from './fields.js'

const GeometrySchema = co.map({
	date: fields.geometryDateField,
	type: fields.geometryTypeField,
	scaleFactor: fields.geometryScaleFactorField,
	rotation: fields.geometryRotationField,
	rectangleLength: fields.geometryRectangleLengthField,
	rectangleWidth: fields.geometryRectangleWidthField,
	ellispeLength: fields.geometryEllipseLengthField,
	ellipseWidth: fields.geometryEllipseLengthField,
	polygonNumSides: fields.geometryPolygonNumSidesField,
	polygonRadius: fields.geometryPolygonRadiusField,
	linesCoordinates: co.list(fields.coordinateField),
	linesClosed: fields.geometryLinesClosedField
})

export const GeometryHistorySchema = co.record(z.string(), GeometrySchema)

const LocationSchema = co.map({
	date: fields.locationDateField,
	coordinate: fields.coordinateField,
	workspace: WorkspaceSchema,

})

export const LocationHistorySchema = co.record(z.string(), LocationSchema)

export const PlantingAreaSchema = co.map({
	name: fields.plantingAreaNameField,
	geometryHistory: GeometryHistorySchema,
	locationHistory: LocationHistorySchema,
	depth: fields.plantingAreaDepthField,
	description: co.plainText()
})

export const WorkspaceSchema = co.map({
	name: fields.workspaceNameField,
	slug: z.string(),
	description: co.plainText()
})



export type Coordinate = Entity<typeof workspaceSchema, 'coordinates'>;
export type Position = Pick<Coordinate, 'x' | 'y'>;
export type Geometry = QueryResult<
	typeof workspaceSchema,
	{ collectionName: 'geometries'; include: { linesCoordinates: true } }
>;
export type GeometryType = (typeof GeometryTypeEnumOptions)[number];
export type GeometryHistory = Entity<typeof workspaceSchema, 'geometryHistories'> & {
	geometries: Geometry[];
};
export type Location = Entity<typeof workspaceSchema, 'locations'>;
export type LocationHistory = QueryResult<
	typeof workspaceSchema,
	{ collectionName: 'locationHistories'; include: { locations: true } }
>;
export type PlantingArea = Entity<typeof workspaceSchema, 'plantingAreas'> & {
	geometry: Geometry | null | undefined;
	locationHistory: LocationHistory | null | undefined;
};
export type Workspace = Entity<typeof workspaceSchema, 'workspaces'>;
