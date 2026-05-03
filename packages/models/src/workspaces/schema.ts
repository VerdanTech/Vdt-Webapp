import { type TableRow, schema as s } from 'jazz-tools';

/**
 * Specifies a type of geometry.
 * RECTANGLE: a closed shape specified by width and height.
 * POLYGON: a closed shape specified by a number of sides and their length.
 * ELLIPSE: a closed shape specified by a major and minor radius.
 * LINES: a closed or open shape specified by a set of joined line segments.
 */
export const GeometryTypeEnumOptions = [
	'RECTANGLE',
	'POLYGON',
	'ELLIPSE',
	'LINES'
] as const;

export const workspaceSchema = {
	/** Coordinate schema. */
	coordinates: s.table({
		/** Garden the entity is located within - required for access control. */
		gardenId: s.ref('gardens'),

		/** The horizontal X component of the coordinate in meters. */
		x: s.float(),

		/** The vertical Y component of the coordinate in meters. */
		y: s.float(),

		/** The depth/altitude component of the coordinate in meters. */
		z: s.float().optional()
	}),

	/** Geometry schema. */
	geometries: s.table({
		/** Garden the entity is located within - required for access control. */
		gardenId: s.ref('gardens'),

		/** Describes the type of the geometry. */
		type: s.enum(...GeometryTypeEnumOptions),

		/** The date at which this geometry applies. */
		date: s.timestamp(),

		/** Scalar size multiplier. */
		scaleFactor: s.float().default(1),

		/** Rotation of the geometry about its center or location, in degrees. */
		rotation: s.float().default(0),

		/** Horizontal length of the rectangle in meters. */
		rectangleLength: s.float().default(1),

		/** Vertical width of the rectangle in meters. */
		rectangleWidth: s.float().default(1),

		/** Number of sides to the polygon. */
		polygonNumSides: s.int().default(3),

		/** Polygon radius. */
		polygonRadius: s.float().default(1),

		/** The length of the horizontal diameter in meters. */
		ellipseLength: s.float().default(1),

		/** The width of the vertical diameter in meters. */
		ellipseWidth: s.float().default(1),

		/** A set of coordinate IDs which describe an open or closed shape of line segments. */
		linesCoordinateIds: s.array(s.string()).default([]),

		/** If true the lines form a closed shape. */
		linesClosed: s.boolean().default(true)
	}),

	/** GeometryHistory schema. */
	geometryHistories: s.table({
		/** Garden the entity is located within - required for access control. */
		gardenId: s.ref('gardens'),

		/** A set of geometry IDs which describe a history of geometric change. */
		geometryIds: s.array(s.string())
	}),

	/** Location schema. */
	locations: s.table({
		/** Garden the entity is located within - required for access control. */
		gardenId: s.ref('gardens'),

		/** The workspace the location is in. */
		workspaceId: s.ref('workspaces'),

		/** The horizontal X component of the location in meters. */
		x: s.float(),

		/** The vertical Y component of the location in meters. */
		y: s.float(),

		/** The depth/altitude component of the location in meters. */
		z: s.float().optional(),

		/** The date at which the location applies. */
		date: s.timestamp()
	}),

	/** LocationHistory schema. */
	locationHistories: s.table({
		/** Garden the entity is located within - required for access control. */
		gardenId: s.ref('gardens'),

		/** A set of location IDs which describe a history of locational change. */
		locationIds: s.array(s.string()),

		/** Denormalized set of workspace IDs represented by the locations. */
		workspaceIds: s.array(s.string())
	}),

	/** PlantingArea schema. */
	plantingAreas: s.table({
		/** Garden the entity is located within - required for access control. */
		gardenId: s.ref('gardens'),

		/** Name. */
		name: s.string(),

		/** The geometry of the planting area. */
		geometryId: s.ref('geometries'),

		/** The location history of the planting area. */
		locationHistoryId: s.ref('locationHistories'),

		/** The depth of the planting area in meters. Used to calculate volume. */
		depth: s.float().default(0),

		/** Optional description. */
		description: s.string().default('')
	}),

	/** Workspace schema. */
	workspaces: s.table({
		/** Garden the entity is located within. */
		gardenId: s.ref('gardens'),

		/** Name of the workspace. */
		name: s.string(),

		/** URL-friendly shorthand of the name. */
		slug: s.string(),

		/** Optional description. */
		description: s.string().default('')
	})
};

export type Coordinate = TableRow<typeof workspaceSchema, 'coordinates'>;
export type Position = Pick<Coordinate, 'x' | 'y'>;
export type Geometry = TableRow<typeof workspaceSchema, 'geometries'> & {
	linesCoordinates?: Coordinate[];
};
export type GeometryType = (typeof GeometryTypeEnumOptions)[number];
export type GeometryHistory = TableRow<typeof workspaceSchema, 'geometryHistories'> & {
	geometries?: Geometry[];
};
export type Location = TableRow<typeof workspaceSchema, 'locations'>;
export type LocationHistory = TableRow<typeof workspaceSchema, 'locationHistories'> & {
	locations?: Location[];
};
export type PlantingArea = TableRow<typeof workspaceSchema, 'plantingAreas'> & {
	geometry?: Geometry | null;
	locationHistory?: LocationHistory | null;
};
export type Workspace = TableRow<typeof workspaceSchema, 'workspaces'>;
