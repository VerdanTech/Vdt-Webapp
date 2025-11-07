import { type Entity, type QueryResult } from '@triplit/client';

/**
 * Specifies a type of geometry.
 * Each geometry type is associated with a different record type
 * describing its features.
 * RECTANGLE: a closed shape specified by width and height.
 * POLYGON: a closed shape specified by a number of sides and their length.
 * ELLIPSE: a closed shape specified by a major and minor radius.
 * LINES: a closed or open shape specified by a set of joined line segments.`
 */
export declare const GeometryTypeEnumOptions: readonly [
	'RECTANGLE',
	'POLYGON',
	'ELLIPSE',
	'LINES'
];
export declare const workspaceSchema: {
	/** Coordinate schema. */
	coordinates: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				/** Garden the entity is located within - required for access control. */
				gardenId: import('@triplit/client').StringType<{}>;
				/** The horizontal X component of the coordinate in meters. */
				x: import('@triplit/client').NumberType<{}>;
				/** The vertical Y component of the coordinate in meters. */
				y: import('@triplit/client').NumberType<{}>;
				/** The depth/altitude component of the coordinate in meters. */
				z: import('@triplit/client').NumberType<{
					nullable: true;
					default: number;
				}>;
				/** Used to maintain ordering in sets of coordinates. */
				createdAt: import('@triplit/client').DateType<{
					default: {
						func: string;
						args: null;
					};
				}>;
			},
			{}
		>;
		relationships: {
			garden: {
				query: {
					collectionName: 'gardens';
					where: any;
				};
				cardinality: 'one';
			};
		};
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: ['garden.visibility', string, string][];
				};
			};
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.visibility', string, string]
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
							| ['garden.viewerIds', string, string]
						)[];
					}[];
				};
				insert: {
					/** Allow new coordinates to be created by admins and editors. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				update: {
					/** Restrict coordinates updates to admins and editors. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				delete: {
					/** Restrict coordinates deletes to admins and editors. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
			};
		};
	};
	/** Geometries schema. */
	geometries: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				/** Garden the entity is located within - required for access control. */
				gardenId: import('@triplit/client').StringType<{}>;
				/**
				 * Describes the type of the geometry.
				 * Each geometry object may be of any type. The type determines
				 * which of the attributes objects is used in the application.
				 * For example, if the type is 'ELLIPSE', only the ellipseAttribute
				 * object is used and other attributes are ignored.
				 */
				type: import('@triplit/client').StringType<{
					enum: ('RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES')[];
				}>;
				/** The date at which this geometry applies. */
				date: import('@triplit/client').DateType<{}>;
				/** Scalar size multiplier. */
				scaleFactor: import('@triplit/client').NumberType<{
					default: number;
				}>;
				/** Rotation of the geometry about its center or location, in degrees. */
				rotation: import('@triplit/client').NumberType<{
					default: number;
				}>;
				/** Rectangular geometry attributes. */
				/** Horizontal length of the rectangle in meters. */
				rectangleLength: import('@triplit/client').NumberType<{
					default: number;
				}>;
				/** Vertical width of the rectangle in meters. */
				rectangleWidth: import('@triplit/client').NumberType<{
					default: number;
				}>;
				/** Polygon geometry attributes. */
				/** Number of sides to the polygon. */
				polygonNumSides: import('@triplit/client').NumberType<{
					default: number;
				}>;
				/** Polygon radius. */
				polygonRadius: import('@triplit/client').NumberType<{
					default: number;
				}>;
				/** Ellipe geometry attributes. */
				/** The length of the horizontal diameter in meters. */
				ellipseLength: import('@triplit/client').NumberType<{
					default: number;
				}>;
				/** The width of the vertical diameter in meters. */
				ellipseWidth: import('@triplit/client').NumberType<{
					default: number;
				}>;
				/** Lines geometry attributes. */
				/** A set of coordinates which describe an open or closed shape of line segments. */
				linesCoordinateIds: import('@triplit/client').SetType<
					import('@triplit/client').StringType<{}>,
					{
						default: {
							func: string;
							args: null;
						};
					}
				>;
				/** If true the lines form a closed shape. */
				linesClosed: import('@triplit/client').BooleanType<{
					default: boolean;
				}>;
			},
			{}
		>;
		relationships: {
			garden: {
				query: {
					collectionName: 'gardens';
					where: any;
				};
				cardinality: 'one';
			};
			linesCoordinates: {
				query: {
					collectionName: 'coordinates';
				} & {
					where: ['id', string, string][];
					order: ['createdAt', 'ASC'][];
				};
				cardinality: 'many';
			};
		};
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: ['garden.visibility', string, string][];
				};
			};
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.visibility', string, string]
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
							| ['garden.viewerIds', string, string]
						)[];
					}[];
				};
				insert: {
					/** Allow new geometries to be created by admins and editors. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				update: {
					/** Restrict geometry updates to admins and editors. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				delete: {
					/** Restrict geometry deletes to admins and editors. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
			};
		};
	};
	/** GeometricHistory schema. */
	geometryHistories: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				/** Garden the entity is located within - required for access control. */
				gardenId: import('@triplit/client').StringType<{}>;
				/** A set of geometries which describe a history of geometric change. */
				geometryIds: import('@triplit/client').SetType<
					import('@triplit/client').StringType<{}>,
					{}
				>;
			},
			{}
		>;
		relationships: {
			garden: {
				query: {
					collectionName: 'gardens';
					where: any;
				};
				cardinality: 'one';
			};
			geometries: {
				query: {
					collectionName: 'geometries';
				} & {
					where: ['id', string, string][];
					order: ['date', 'ASC'][];
				};
				cardinality: 'many';
			};
		};
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: ['garden.visibility', string, string][];
				};
			};
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.visibility', string, string]
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
							| ['garden.viewerIds', string, string]
						)[];
					}[];
				};
				insert: {
					/** Allow new geometry history to be created by admins and editors. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				update: {
					/** Restrict geometry history updates to admins and editors. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				delete: {
					/** Restrict geometry histories deletes to admins and editors. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
			};
		};
	};
	/** Location schema. */
	locations: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				/** Garden the entity is located within - required for access control. */
				gardenId: import('@triplit/client').StringType<{}>;
				/** The workspace the cordinate is located in. */
				workspaceId: import('@triplit/client').StringType<{}>;
				/** The horizontal X component of the location in meters. */
				x: import('@triplit/client').NumberType<{}>;
				/** The vertical Y component of the location in meters. */
				y: import('@triplit/client').NumberType<{}>;
				/** The depth/altitude component of the location in meters. */
				z: import('@triplit/client').NumberType<{
					nullable: true;
					default: number;
				}>;
				/** The date at which the location applies. */
				date: import('@triplit/client').DateType<{}>;
			},
			{}
		>;
		relationships: {
			garden: {
				query: {
					collectionName: 'gardens';
					where: any;
				};
				cardinality: 'one';
			};
			workspace: {
				query: {
					collectionName: 'workspaces';
					where: any;
				};
				cardinality: 'one';
			};
		};
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: ['garden.visibility', string, string][];
				};
			};
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.visibility', string, string]
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
							| ['garden.viewerIds', string, string]
						)[];
					}[];
				};
				insert: {
					/** Allow new locations to be created by admins and editors. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				update: {
					/** Restrict locations updates to admins and editors. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				delete: {
					/** Restrict locations deletes to admins and editors. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
			};
		};
	};
	/** Location history schema. */
	locationHistories: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				/** Garden the entity is located within - required for access control. */
				gardenId: import('@triplit/client').StringType<{}>;
				/** A set of locations which describe a history of locational change. */
				locationIds: import('@triplit/client').SetType<
					import('@triplit/client').StringType<{}>,
					{}
				>;
				/** Denormalized set of workspace IDs that are represented by the locations. */
				workspaceIds: import('@triplit/client').SetType<
					import('@triplit/client').StringType<{}>,
					{}
				>;
			},
			{}
		>;
		relationships: {
			garden: {
				query: {
					collectionName: 'gardens';
					where: any;
				};
				cardinality: 'one';
			};
			locations: {
				query: {
					collectionName: 'locations';
				} & {
					where: ['id', string, string][];
					order: ['date', 'ASC'][];
				};
				cardinality: 'many';
			};
		};
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: ['garden.visibility', string, string][];
				};
			};
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.visibility', string, string]
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
							| ['garden.viewerIds', string, string]
						)[];
					}[];
				};
				insert: {
					/** Allow new location history to be created by admins and editors. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				update: {
					/** Restrict location history updates to admins. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				delete: {
					/** Restrict location histories deletes to admins. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
			};
		};
	};
	/** Planting area schema. */
	plantingAreas: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				/** Garden the entity is located within - required for access control. */
				gardenId: import('@triplit/client').StringType<{}>;
				/** Name. */
				name: import('@triplit/client').StringType<{}>;
				/** The geometry of the planting area. */
				geometryId: import('@triplit/client').StringType<{}>;
				/** The location history of the planting area. */
				locationHistoryId: import('@triplit/client').StringType<{}>;
				/** The depth of the planting area in meters. Used to calculate volume. */
				depth: import('@triplit/client').NumberType<{
					default: number;
				}>;
				/** Optional description. */
				description: import('@triplit/client').StringType<{
					default: string;
				}>;
			},
			{}
		>;
		relationships: {
			garden: {
				query: {
					collectionName: 'gardens';
					where: any;
				};
				cardinality: 'one';
			};
			geometry: {
				query: {
					collectionName: 'geometries';
					where: any;
				};
				cardinality: 'one';
			};
			locationHistory: {
				query: {
					collectionName: 'locationHistories';
					where: any;
				};
				cardinality: 'one';
			};
		};
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: ['garden.visibility', string, string][];
				};
			};
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.visibility', string, string]
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
							| ['garden.viewerIds', string, string]
						)[];
					}[];
				};
				insert: {
					/** Allow new planting areas to be created by admins. */
					filter: ['garden.adminIds', string, string][];
				};
				update: {
					/** Restrict planting area updates to admins. */
					filter: ['garden.adminIds', string, string][];
				};
				delete: {
					/** Restrict planting area deletes to admins. */
					filter: ['garden.adminIds', string, string][];
				};
			};
		};
	};
	/** Workspace schema. */
	workspaces: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				/** Garden the entity is located within. */
				gardenId: import('@triplit/client').StringType<{}>;
				/** Name of the workspace. */
				name: import('@triplit/client').StringType<{}>;
				/** URL-friendly shorthand of the name. */
				slug: import('@triplit/client').StringType<{}>;
				/** Optional description. */
				description: import('@triplit/client').StringType<{
					default: string;
				}>;
			},
			{}
		>;
		relationships: {
			garden: {
				query: {
					collectionName: 'gardens';
					where: any;
				};
				cardinality: 'one';
			};
		};
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: ['garden.visibility', string, string][];
				};
			};
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.visibility', string, string]
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
							| ['garden.viewerIds', string, string]
						)[];
					}[];
				};
				insert: {
					/** Allow new workspaces to be created by admins. */
					filter: ['garden.adminIds', string, string][];
				};
				update: {
					/** Restrict workspace updates to admins. */
					filter: ['garden.adminIds', string, string][];
				};
				delete: {
					/** Restrict workspace deletes to admins. */
					filter: ['garden.adminIds', string, string][];
				};
			};
		};
	};
	gardens: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				name: import('@triplit/client').StringType<{}>;
				visibility: import('@triplit/client').StringType<{
					enum: ('HIDDEN' | 'UNLISTED' | 'PUBLIC')[];
				}>;
				description: import('@triplit/client').StringType<{
					nullable: true;
					default: null;
				}>;
				isActive: import('@triplit/client').BooleanType<{
					default: boolean;
				}>;
				creatorId: import('@triplit/client').StringType<{
					nullable: true;
				}>;
				adminIds: import('@triplit/client').SetType<
					import('@triplit/client').StringType<{}>,
					{}
				>;
				editorIds: import('@triplit/client').SetType<
					import('@triplit/client').StringType<{}>,
					{
						default: {
							func: string;
							args: null;
						};
					}
				>;
				viewerIds: import('@triplit/client').SetType<
					import('@triplit/client').StringType<{}>,
					{
						default: {
							func: string;
							args: null;
						};
					}
				>;
				createdAt: import('@triplit/client').DateType<{
					default: {
						func: string;
						args: null;
					};
				}>;
			},
			{}
		>;
		relationships: {
			creator: {
				query: {
					collectionName: 'profiles';
					where: any;
				};
				cardinality: 'one';
			};
			adminMemberships: {
				query: {
					collectionName: 'gardenMemberships';
				} & {
					where: ['userId', string, string][];
				};
				cardinality: 'many';
			};
			editorMemberships: {
				query: {
					collectionName: 'gardenMemberships';
				} & {
					where: ['userId', string, string][];
				};
				cardinality: 'many';
			};
			viewerMemberships: {
				query: {
					collectionName: 'gardenMemberships';
				} & {
					where: ['userId', string, string][];
				};
				cardinality: 'many';
			};
		};
		permissions: {
			anon: {
				read: {
					filter: ['visibility', string, string][];
				};
			};
			user: {
				read: {
					filter: {
						mod: 'or';
						filters: (
							| ['visibility', string, string]
							| ['adminIds', string, string]
							| ['editorIds', string, string]
							| ['viewerIds', string, string]
						)[];
					}[];
				};
				insert: {
					filter: ['creatorId', string, string][];
				};
				update: {
					filter: ['adminIds', string, string][];
				};
			};
		};
	};
	gardenMemberships: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				gardenId: import('@triplit/client').StringType<{}>;
				userId: import('@triplit/client').StringType<{}>;
				role: import('@triplit/client').StringType<{
					enum: ('ADMIN' | 'EDITOR' | 'VIEWER')[];
				}>;
				inviterId: import('@triplit/client').StringType<{
					nullable: true;
				}>;
				status: import('@triplit/client').StringType<{
					enum: ('CREATED' | 'PENDING' | 'ACCEPTED')[];
				}>;
				acceptedAt: import('@triplit/client').DateType<{
					nullable: true;
					default: null;
				}>;
				favorite: import('@triplit/client').BooleanType<{
					default: boolean;
				}>;
			},
			{}
		>;
		relationships: {
			garden: {
				query: {
					collectionName: 'gardens';
					where: any;
				};
				cardinality: 'one';
			};
			user: {
				query: {
					collectionName: 'profiles';
					where: any;
				};
				cardinality: 'one';
			};
			inviter: {
				query: {
					collectionName: 'profiles';
					where: any;
				};
				cardinality: 'one';
			};
		};
		permissions: {
			anon: {
				read: {
					filter: ['garden.visibility', string, string][];
				};
			};
			user: {
				read: {
					filter: {
						mod: 'or';
						filters: (
							| ['garden.visibility', string, string]
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
							| ['garden.viewerIds', string, string]
						)[];
					}[];
				};
				insert: {
					filter: ['garden.adminIds', string, string][];
				};
				update: {
					filter: {
						mod: 'or';
						filters: (
							| ['userId', string, string]
							| ['garden.adminIds', string, string]
						)[];
					}[];
				};
				delete: {
					filter: {
						mod: 'or';
						filters: (
							| ['userId', string, string]
							| ['garden.adminIds', string, string]
						)[];
					}[];
				};
			};
		};
	};
	profiles: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				username: import('@triplit/client').StringType<{}>;
				createdAt: import('@triplit/client').DateType<{
					default: {
						func: string;
						args: null;
					};
				}>;
			},
			{}
		>;
		permissions: {
			anon: {
				read: {
					filter: true[];
				};
			};
			user: {
				read: {
					filter: true[];
				};
			};
		};
	};
	accounts: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				profileId: import('@triplit/client').StringType<{}>;
				passwordHash: import('@triplit/client').StringType<{}>;
				verifiedEmail: import('@triplit/client').StringType<{
					nullable: true;
				}>;
				unverifiedEmail: import('@triplit/client').RecordType<
					{
						address: import('@triplit/client').StringType<{
							nullable: true;
							default: null;
						}>;
						token: import('@triplit/client').StringType<{
							nullable: true;
							default: null;
						}>;
					},
					{}
				>;
				passwordResetToken: import('@triplit/client').StringType<{
					nullable: true;
					default: null;
				}>;
				isActive: import('@triplit/client').BooleanType<{
					default: boolean;
				}>;
			},
			{}
		>;
		relationships: {
			profile: {
				query: {
					collectionName: 'profiles';
					where: any;
				};
				cardinality: 'one';
			};
		};
		permissions: {
			user: {
				read: {
					filter: ['id', string, string][];
				};
			};
		};
	};
};
export type Coordinate = Entity<typeof workspaceSchema, 'coordinates'>;
export type Position = Pick<Coordinate, 'x' | 'y'>;
export type Geometry = QueryResult<
	typeof workspaceSchema,
	{
		collectionName: 'geometries';
		include: {
			linesCoordinates: true;
		};
	}
>;
export type GeometryType = (typeof GeometryTypeEnumOptions)[number];
export type GeometryHistory = Entity<typeof workspaceSchema, 'geometryHistories'> & {
	geometries: Geometry[];
};
export type Location = Entity<typeof workspaceSchema, 'locations'>;
export type LocationHistory = QueryResult<
	typeof workspaceSchema,
	{
		collectionName: 'locationHistories';
		include: {
			locations: true;
		};
	}
>;
export type PlantingArea = Entity<typeof workspaceSchema, 'plantingAreas'> & {
	geometry: Geometry | null | undefined;
	locationHistory: LocationHistory | null | undefined;
};
export type Workspace = Entity<typeof workspaceSchema, 'workspaces'>;
//# sourceMappingURL=schema.d.ts.map
