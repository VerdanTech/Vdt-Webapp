import { type Entity } from '@triplit/client';

/**
 * Defines the parent entity that the environment describes characteristics for.
 * - GARDEN: the environment applies to a garden.
 * - WORKSPACE: the environment applies to a workspace.
 * - PLANTING_AREA: the environment applies to a planting area.
 * - INDEPENDENT: the environment applies to an independent geometry.
 */
export declare const EnvironmentParentTypeEnumOptions: readonly [
	'GARDEN',
	'WORKSPACE',
	'PLANTING_AREA',
	'INDEPENDENT'
];
export declare const environmentSchema: {
	/** Environment schema. */
	environments: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				/** Non-unique name of the environment. */
				name: import('@triplit/client').StringType<{}>;
				/** Optional description. */
				description: import('@triplit/client').StringType<{
					default: string;
				}>;
				/** Type of the parent entity of the environment. */
				parentType: import('@triplit/client').StringType<{
					enum: ('GARDEN' | 'WORKSPACE' | 'PLANTING_AREA' | 'INDEPENDENT')[];
					default: string;
				}>;
				/** Garden the environment exists in. Defined regardless of parentType. */
				gardenId: import('@triplit/client').StringType<{}>;
				/** The workspaces the environment applies to. Defined only if parentType = 'WORKSPACE'. */
				workspaceIds: import('@triplit/client').TypeInterface<
					'set',
					{
						optional: true;
					}
				> &
					Omit<
						import('@triplit/client').SetType<
							import('@triplit/client').StringType<{}>,
							{}
						>,
						keyof import('@triplit/client').TypeInterface<string, {}>
					>;
				/** The planting areas the environment applies to. Defined only if parentType = 'PLANTING_AREA'. */
				plantingAreaIds: import('@triplit/client').TypeInterface<
					'set',
					{
						optional: true;
					}
				> &
					Omit<
						import('@triplit/client').SetType<
							import('@triplit/client').StringType<{}>,
							{}
						>,
						keyof import('@triplit/client').TypeInterface<string, {}>
					>;
				/** The geometry the environment applies to. Defined only if parentType = 'INDEPENDENT'. */
				geometryHistoryId: import('@triplit/client').TypeInterface<
					'string',
					{
						optional: true;
					}
				> &
					Omit<
						import('@triplit/client').StringType<{}>,
						keyof import('@triplit/client').TypeInterface<string, {}>
					>;
				/** The locations the environment geometry exists at. Defined only if parentType = 'INDEPENDENT'. */
				locationHistoryId: import('@triplit/client').TypeInterface<
					'string',
					{
						optional: true;
					}
				> &
					Omit<
						import('@triplit/client').StringType<{}>,
						keyof import('@triplit/client').TypeInterface<string, {}>
					>;
				/**
				 * If true, the environment will inherit the attributes of the environments
				 * defined at higher levels, eg., that of a planting area in a workspace.
				 */
				inherit: import('@triplit/client').BooleanType<{
					default: boolean;
				}>;
				attributes: import('@triplit/client').RecordType<
					{
						frostDates: import('@triplit/client').TypeInterface<
							'record',
							{
								optional: true;
							}
						> &
							Omit<
								import('@triplit/client').RecordType<
									{
										lastFrostDate: import('@triplit/client').TypeInterface<
											'date',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').DateType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
										firstFrostDate: import('@triplit/client').TypeInterface<
											'date',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').DateType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
									},
									{}
								>,
								keyof import('@triplit/client').TypeInterface<string, {}>
							>;
						annualTemperature: import('@triplit/client').TypeInterface<
							'record',
							{
								optional: true;
							}
						> &
							Omit<
								import('@triplit/client').RecordType<
									{
										minimum: import('@triplit/client').TypeInterface<
											'number',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').NumberType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
										maximum: import('@triplit/client').TypeInterface<
											'number',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').NumberType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
									},
									{}
								>,
								keyof import('@triplit/client').TypeInterface<string, {}>
							>;
					},
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
			workspaces: {
				query: {
					collectionName: 'workspaces';
				} & {
					where: ['id', string, string][];
				};
				cardinality: 'many';
			};
			plantingAreas: {
				query: {
					collectionName: 'plantingAreas';
				} & {
					where: ['id', string, string][];
				};
				cardinality: 'many';
			};
			geometriHistory: {
				query: {
					collectionName: 'geometryHistories';
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
					/** Allow new environments to be created by admins and editors. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				update: {
					/** Restrict environment updates to admins and editors. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				delete: {
					/** Restrict environment deletes to admins and editors. */
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
				gardenId: import('@triplit/client').StringType<{}>;
				x: import('@triplit/client').NumberType<{}>;
				y: import('@triplit/client').NumberType<{}>;
				z: import('@triplit/client').NumberType<{
					nullable: true;
					default: number;
				}>;
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
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				update: {
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				delete: {
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
				gardenId: import('@triplit/client').StringType<{}>;
				type: import('@triplit/client').StringType<{
					enum: ('RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES')[];
				}>;
				date: import('@triplit/client').DateType<{}>;
				scaleFactor: import('@triplit/client').NumberType<{
					default: number;
				}>;
				rotation: import('@triplit/client').NumberType<{
					default: number;
				}>;
				rectangleLength: import('@triplit/client').NumberType<{
					default: number;
				}>;
				rectangleWidth: import('@triplit/client').NumberType<{
					default: number;
				}>;
				polygonNumSides: import('@triplit/client').NumberType<{
					default: number;
				}>;
				polygonRadius: import('@triplit/client').NumberType<{
					default: number;
				}>;
				ellipseLength: import('@triplit/client').NumberType<{
					default: number;
				}>;
				ellipseWidth: import('@triplit/client').NumberType<{
					default: number;
				}>;
				linesCoordinateIds: import('@triplit/client').SetType<
					import('@triplit/client').StringType<{}>,
					{
						default: {
							func: string;
							args: null;
						};
					}
				>;
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
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				update: {
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				delete: {
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
				gardenId: import('@triplit/client').StringType<{}>;
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
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				update: {
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				delete: {
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
				gardenId: import('@triplit/client').StringType<{}>;
				workspaceId: import('@triplit/client').StringType<{}>;
				x: import('@triplit/client').NumberType<{}>;
				y: import('@triplit/client').NumberType<{}>;
				z: import('@triplit/client').NumberType<{
					nullable: true;
					default: number;
				}>;
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
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				update: {
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				delete: {
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
				gardenId: import('@triplit/client').StringType<{}>;
				locationIds: import('@triplit/client').SetType<
					import('@triplit/client').StringType<{}>,
					{}
				>;
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
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				update: {
					filter: {
						mod: 'or';
						filters: (
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
						)[];
					}[];
				};
				delete: {
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
				gardenId: import('@triplit/client').StringType<{}>;
				name: import('@triplit/client').StringType<{}>;
				geometryId: import('@triplit/client').StringType<{}>;
				locationHistoryId: import('@triplit/client').StringType<{}>;
				depth: import('@triplit/client').NumberType<{
					default: number;
				}>;
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
					filter: ['garden.adminIds', string, string][];
				};
				delete: {
					filter: ['garden.adminIds', string, string][];
				};
			};
		};
	};
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
				gardenId: import('@triplit/client').StringType<{}>;
				name: import('@triplit/client').StringType<{}>;
				slug: import('@triplit/client').StringType<{}>;
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
					filter: ['garden.adminIds', string, string][];
				};
				delete: {
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
export type Environment = Entity<typeof environmentSchema, 'environments'>;
export type EnvironmentParent = (typeof EnvironmentParentTypeEnumOptions)[number];
//# sourceMappingURL=schema.d.ts.map
