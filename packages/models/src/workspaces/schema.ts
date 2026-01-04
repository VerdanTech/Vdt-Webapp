import { type Entity, type QueryResult, Schema as S, or } from '@triplit/client';

import { observationSchema } from '../observations/index.js';

/**
 * Specifies a type of geometry.
 * Each geometry type is associated with a different record type
 * describing its features.
 * RECTANGLE: a closed shape specified by width and height.
 * POLYGON: a closed shape specified by a number of sides and their length.
 * ELLIPSE: a closed shape specified by a major and minor radius.
 * LINES: a closed or open shape specified by a set of joined line segments.`
 */
export const GeometryTypeEnumOptions = [
	'RECTANGLE',
	'POLYGON',
	'ELLIPSE',
	'LINES'
] as const;

export const workspaceSchema = S.Collections({
	...observationSchema,
	/** Coordinate schema. */
	coordinates: {
		schema: S.Schema({
			id: S.Id(),

			/** Garden the entity is located within - required for access control. */
			gardenId: S.String(),

			/** The horizontal X component of the coordinate in meters. */
			x: S.Number(),

			/** The vertical Y component of the coordinate in meters. */
			y: S.Number(),

			/** The depth/altitude component of the coordinate in meters. */
			z: S.Number({ nullable: true, default: 0 }),

			/** Used to maintain ordering in sets of coordinates. */
			createdAt: S.Date({ default: S.Default.now() })
		}),
		relationships: {
			garden: S.RelationById('gardens', '$gardenId')
		},
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: [['garden.visibility', '!=', 'HIDDEN']]
				}
			},
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: [
						or([
							['garden.visibility', '!=', 'HIDDEN'],
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId'],
							['garden.viewerIds', 'has', '$role.profileId']
						])
					]
				},
				insert: {
					/** Allow new coordinates to be created by admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				update: {
					/** Restrict coordinates updates to admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				delete: {
					/** Restrict coordinates deletes to admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				}
			}
		}
	},
	/** Geometries schema. */
	geometries: {
		schema: S.Schema({
			id: S.Id(),

			/** Garden the entity is located within - required for access control. */
			gardenId: S.String(),

			/**
			 * Describes the type of the geometry.
			 * Each geometry object may be of any type. The type determines
			 * which of the attributes objects is used in the application.
			 * For example, if the type is 'ELLIPSE', only the ellipseAttribute
			 * object is used and other attributes are ignored.
			 */
			type: S.String({ enum: [...GeometryTypeEnumOptions] }),

			/** The date at which this geometry applies. */
			date: S.Date(),

			/** Scalar size multiplier. */
			scaleFactor: S.Number({ default: 1 }),

			/** Rotation of the geometry about its center or location, in degrees. */
			rotation: S.Number({ default: 0 }),

			/** Rectangular geometry attributes. */
			/** Horizontal length of the rectangle in meters. */
			rectangleLength: S.Number({ default: 1 }),

			/** Vertical width of the rectangle in meters. */
			rectangleWidth: S.Number({ default: 1 }),

			/** Polygon geometry attributes. */
			/** Number of sides to the polygon. */
			polygonNumSides: S.Number({ default: 3 }),

			/** Polygon radius. */
			polygonRadius: S.Number({ default: 1 }),

			/** Ellipe geometry attributes. */
			/** The length of the horizontal diameter in meters. */
			ellipseLength: S.Number({ default: 1 }),

			/** The width of the vertical diameter in meters. */
			ellipseWidth: S.Number({ default: 1 }),

			/** Lines geometry attributes. */
			/** A set of coordinates which describe an open or closed shape of line segments. */
			linesCoordinateIds: S.Set(S.String(), { default: S.Default.Set.empty() }),

			/** If true the lines form a closed shape. */
			linesClosed: S.Boolean({ default: true })
		}),
		relationships: {
			garden: S.RelationById('gardens', '$gardenId'),
			linesCoordinates: S.RelationMany('coordinates', {
				where: [['id', 'in', '$linesCoordinateIds']],
				order: [['createdAt', 'ASC']]
			})
		},
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: [['garden.visibility', '!=', 'HIDDEN']]
				}
			},
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: [
						or([
							['garden.visibility', '!=', 'HIDDEN'],
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId'],
							['garden.viewerIds', 'has', '$role.profileId']
						])
					]
				},
				insert: {
					/** Allow new geometries to be created by admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				update: {
					/** Restrict geometry updates to admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				delete: {
					/** Restrict geometry deletes to admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				}
			}
		}
	},
	/** GeometricHistory schema. */
	geometryHistories: {
		schema: S.Schema({
			id: S.Id(),

			/** Garden the entity is located within - required for access control. */
			gardenId: S.String(),

			/** A set of geometries which describe a history of geometric change. */
			geometryIds: S.Set(S.String())
		}),
		relationships: {
			garden: S.RelationById('gardens', '$gardenId'),
			geometries: S.RelationMany('geometries', {
				where: [['id', 'in', '$geometryIds']],
				order: [['date', 'ASC']]
			})
		},
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: [['garden.visibility', '!=', 'HIDDEN']]
				}
			},
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: [
						or([
							['garden.visibility', '!=', 'HIDDEN'],
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId'],
							['garden.viewerIds', 'has', '$role.profileId']
						])
					]
				},
				insert: {
					/** Allow new geometry history to be created by admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				update: {
					/** Restrict geometry history updates to admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				delete: {
					/** Restrict geometry histories deletes to admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				}
			}
		}
	},
	/** Location schema. */
	locations: {
		schema: S.Schema({
			id: S.Id(),

			/** Garden the entity is located within - required for access control. */
			gardenId: S.String(),

			/** The workspace the cordinate is located in. */
			workspaceId: S.String(),

			/** The horizontal X component of the location in meters. */
			x: S.Number(),

			/** The vertical Y component of the location in meters. */
			y: S.Number(),

			/** The depth/altitude component of the location in meters. */
			z: S.Number({ nullable: true, default: 0 }),

			/** The date at which the location applies. */
			date: S.Date()
		}),
		relationships: {
			garden: S.RelationById('gardens', '$gardenId'),
			workspace: S.RelationById('workspaces', '$workspaceId')
		},
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: [['garden.visibility', '!=', 'HIDDEN']]
				}
			},
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: [
						or([
							['garden.visibility', '!=', 'HIDDEN'],
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId'],
							['garden.viewerIds', 'has', '$role.profileId']
						])
					]
				},
				insert: {
					/** Allow new locations to be created by admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				update: {
					/** Restrict locations updates to admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				delete: {
					/** Restrict locations deletes to admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				}
			}
		}
	},
	/** Location history schema. */
	locationHistories: {
		schema: S.Schema({
			id: S.Id(),

			/** Garden the entity is located within - required for access control. */
			gardenId: S.String(),

			/** A set of locations which describe a history of locational change. */
			locationIds: S.Set(S.String()),

			/** Denormalized set of workspace IDs that are represented by the locations. */
			workspaceIds: S.Set(S.String())
		}),
		relationships: {
			garden: S.RelationById('gardens', '$gardenId'),
			locations: S.RelationMany('locations', {
				where: [['id', 'in', '$locationIds']],
				order: [['date', 'ASC']]
			})
		},
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: [['garden.visibility', '!=', 'HIDDEN']]
				}
			},
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: [
						or([
							['garden.visibility', '!=', 'HIDDEN'],
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId'],
							['garden.viewerIds', 'has', '$role.profileId']
						])
					]
				},
				insert: {
					/** Allow new location history to be created by admins and editors. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				update: {
					/** Restrict location history updates to admins. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				},
				delete: {
					/** Restrict location histories deletes to admins. */
					filter: [
						or([
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId']
						])
					]
				}
			}
		}
	},
	/** Planting area schema. */
	plantingAreas: {
		schema: S.Schema({
			id: S.Id(),

			/** Garden the entity is located within - required for access control. */
			gardenId: S.String(),

			/** Name. */
			name: S.String(),

			/** The geometry of the planting area. */
			geometryId: S.String(),

			/** The location history of the planting area. */
			locationHistoryId: S.String(),

			/** The depth of the planting area in meters. Used to calculate volume. */
			depth: S.Number({ default: 0 }),

			/** Optional description. */
			description: S.String({ default: '' })
		}),
		relationships: {
			garden: S.RelationById('gardens', '$gardenId'),
			geometry: S.RelationById('geometries', '$geometryId'),
			locationHistory: S.RelationById('locationHistories', '$locationHistoryId')
		},
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: [['garden.visibility', '!=', 'HIDDEN']]
				}
			},
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: [
						or([
							['garden.visibility', '!=', 'HIDDEN'],
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId'],
							['garden.viewerIds', 'has', '$role.profileId']
						])
					]
				},
				insert: {
					/** Allow new planting areas to be created by admins. */
					filter: [['garden.adminIds', 'has', '$role.profileId']]
				},
				update: {
					/** Restrict planting area updates to admins. */
					filter: [['garden.adminIds', 'has', '$role.profileId']]
				},
				delete: {
					/** Restrict planting area deletes to admins. */
					filter: [['garden.adminIds', 'has', '$role.profileId']]
				}
			}
		}
	},
	/** Workspace schema. */
	workspaces: {
		schema: S.Schema({
			id: S.Id(),

			/** Garden the entity is located within. */
			gardenId: S.String(),

			/** Name of the workspace. */
			name: S.String(),

			/** URL-friendly shorthand of the name. */
			slug: S.String(),

			/** Optional description. */
			description: S.String({ default: '' })
		}),
		relationships: {
			garden: S.RelationById('gardens', '$gardenId')
		},
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: [['garden.visibility', '!=', 'HIDDEN']]
				}
			},
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: [
						or([
							['garden.visibility', '!=', 'HIDDEN'],
							['garden.adminIds', 'has', '$role.profileId'],
							['garden.editorIds', 'has', '$role.profileId'],
							['garden.viewerIds', 'has', '$role.profileId']
						])
					]
				},
				insert: {
					/** Allow new workspaces to be created by admins. */
					filter: [['garden.adminIds', 'has', '$role.profileId']]
				},
				update: {
					/** Restrict workspace updates to admins. */
					filter: [['garden.adminIds', 'has', '$role.profileId']]
				},
				delete: {
					/** Restrict workspace deletes to admins. */
					filter: [['garden.adminIds', 'has', '$role.profileId']]
				}
			}
		}
	}
});

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
