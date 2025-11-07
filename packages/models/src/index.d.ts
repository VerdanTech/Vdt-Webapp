import type { DBTransaction } from '@triplit/client';

import { roles } from './users/schema.js';

/** Export common modules. */
export * from './users/index.js';
export * from './gardens/index.js';
export * from './workspaces/index.js';
export * from './cultivars/index.js';
export * from './environments/index.js';
export * from './plants/index.js';
export * from './utils.js';
export * from './errors.js';
export * from './controller.js';
export * from './permissions.js';
export * from './utils/index.js';
/**
 * Export Triplit schemas.
 * Note that only plantSchema is exported because currently
 * schemas are included into eachother sequentially,
 * ie., workspaceSchema includes gardenSchema which includes userSchema.
 * This is required to maintain typing across the S.Collections()
 */
export declare const schema: {
	harvests: {
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
				lifespanIds: import('@triplit/client').SetType<
					import('@triplit/client').StringType<{}>,
					{
						default: {
							func: string;
							args: null;
						};
					}
				>;
				date: import('@triplit/client').DateType<{}>;
				mass: import('@triplit/client').TypeInterface<
					'number',
					{
						optional: true;
					}
				> &
					Omit<
						import('@triplit/client').NumberType<{}>,
						keyof import('@triplit/client').TypeInterface<string, {}>
					>;
				quality: import('@triplit/client').TypeInterface<
					'string',
					{
						enum: ('COMPOST' | 'LOW' | 'MEDIUM' | 'HIGH' | 'PERFECT')[];
					} & {
						optional: true;
					}
				> &
					Omit<
						import('@triplit/client').StringType<{
							enum: ('COMPOST' | 'LOW' | 'MEDIUM' | 'HIGH' | 'PERFECT')[];
						}>,
						keyof import('@triplit/client').TypeInterface<string, {}>
					>;
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
			lifespans: {
				query: {
					collectionName: 'lifespans';
				} & {
					where: ['id', string, string][];
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
	lifespans: {
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
				origin: import('@triplit/client').StringType<{
					enum: ('DIRECT_SEED' | 'SEED_TO_TRANSPLANT' | 'SEEDLING_TO_TRANSPLANT')[];
				}>;
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
				dates: import('@triplit/client').RecordType<
					{
						seedDate: import('@triplit/client').TypeInterface<
							'date',
							{
								optional: true;
							}
						> &
							Omit<
								import('@triplit/client').DateType<{}>,
								keyof import('@triplit/client').TypeInterface<string, {}>
							>;
						germDate: import('@triplit/client').TypeInterface<
							'date',
							{
								optional: true;
							}
						> &
							Omit<
								import('@triplit/client').DateType<{}>,
								keyof import('@triplit/client').TypeInterface<string, {}>
							>;
						expiryDate: import('@triplit/client').TypeInterface<
							'date',
							{
								optional: true;
							}
						> &
							Omit<
								import('@triplit/client').DateType<{}>,
								keyof import('@triplit/client').TypeInterface<string, {}>
							>;
						dormancyDates: import('@triplit/client').TypeInterface<
							'set',
							{
								optional: true;
							}
						> &
							Omit<
								import('@triplit/client').SetType<
									import('@triplit/client').DateType<{}>,
									{}
								>,
								keyof import('@triplit/client').TypeInterface<string, {}>
							>;
						growthDates: import('@triplit/client').TypeInterface<
							'set',
							{
								optional: true;
							}
						> &
							Omit<
								import('@triplit/client').SetType<
									import('@triplit/client').DateType<{}>,
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
			geometryHistory: {
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
			harvests: {
				query: {
					collectionName: 'harvests';
				} & {
					where: ['id', string, string][];
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
	plants: {
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
				cultivarName: import('@triplit/client').StringType<{}>;
				cultivarAttributes: import('@triplit/client').RecordType<
					{
						annualLifeCycle: import('@triplit/client').TypeInterface<
							'record',
							{
								optional: true;
							}
						> &
							Omit<
								import('@triplit/client').RecordType<
									{
										sowToGerm: import('@triplit/client').TypeInterface<
											'number',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').NumberType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
										germToTransplant: import('@triplit/client').TypeInterface<
											'number',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').NumberType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
										germToFirstHarvest: import('@triplit/client').TypeInterface<
											'number',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').NumberType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
										firstToLastHarvest: import('@triplit/client').TypeInterface<
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
						frostDatePlantingWindows: import('@triplit/client').TypeInterface<
							'record',
							{
								optional: true;
							}
						> &
							Omit<
								import('@triplit/client').RecordType<
									{
										lastFrostWindowOpen: import('@triplit/client').TypeInterface<
											'number',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').NumberType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
										lastFrostWindowClose: import('@triplit/client').TypeInterface<
											'number',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').NumberType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
										firstFrostWindowOpen: import('@triplit/client').TypeInterface<
											'number',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').NumberType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
										firstFrostWindowClose: import('@triplit/client').TypeInterface<
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
						origin: import('@triplit/client').TypeInterface<
							'record',
							{
								optional: true;
							}
						> &
							Omit<
								import('@triplit/client').RecordType<
									{
										transplantable: import('@triplit/client').TypeInterface<
											'boolean',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').BooleanType<{}>,
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
				expectedLifespanId: import('@triplit/client').StringType<{}>;
				recordedLifespanId: import('@triplit/client').StringType<{}>;
				aggregate: import('@triplit/client').BooleanType<{
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
			expectedLifespan: {
				query: {
					collectionName: 'lifespans';
					where: any;
				};
				cardinality: 'one';
			};
			recordedLifespan: {
				query: {
					collectionName: 'lifespans';
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
	plantGroups: {
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
				plantIds: import('@triplit/client').SetType<
					import('@triplit/client').StringType<{}>,
					{}
				>;
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
			plants: {
				query: {
					collectionName: 'plants';
				} & {
					where: ['id', string, string][];
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
	cultivarCollections: {
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
				slug: import('@triplit/client').StringType<{}>;
				visibility: import('@triplit/client').StringType<{
					enum: ('HIDDEN' | 'UNLISTED' | 'PUBLIC')[];
				}>;
				userId: import('@triplit/client').StringType<{
					nullable: true;
					default: null;
				}>;
				gardenId: import('@triplit/client').StringType<{
					nullable: true;
					default: null;
				}>;
				priority: import('@triplit/client').NumberType<{
					default: number;
				}>;
				description: import('@triplit/client').StringType<{
					default: string;
				}>;
				parentId: import('@triplit/client').StringType<{
					nullable: true;
					default: null;
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
			user: {
				query: {
					collectionName: 'profiles';
					where: any;
				};
				cardinality: 'one';
			};
			garden: {
				query: {
					collectionName: 'gardens';
					where: any;
				};
				cardinality: 'one';
			};
			parent: {
				query: {
					collectionName: 'cultivarCollections';
					where: any;
				};
				cardinality: 'one';
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
							| ['userId', string, string]
							| ['visibility', string, string]
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
							| ['userId', string, string]
							| ['garden.adminIds', string, string]
						)[];
					}[];
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
	cultivars: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				collectionId: import('@triplit/client').StringType<{}>;
				names: import('@triplit/client').SetType<
					import('@triplit/client').StringType<{}>,
					{}
				>;
				abbreviation: import('@triplit/client').StringType<{}>;
				scientificName: import('@triplit/client').TypeInterface<
					'string',
					{
						optional: true;
					}
				> &
					Omit<
						import('@triplit/client').StringType<{}>,
						keyof import('@triplit/client').TypeInterface<string, {}>
					>;
				description: import('@triplit/client').StringType<{
					default: string;
				}>;
				parentId: import('@triplit/client').StringType<{
					nullable: true;
					default: null;
				}>;
				attributes: import('@triplit/client').RecordType<
					{
						annualLifeCycle: import('@triplit/client').TypeInterface<
							'record',
							{
								optional: true;
							}
						> &
							Omit<
								import('@triplit/client').RecordType<
									{
										sowToGerm: import('@triplit/client').TypeInterface<
											'number',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').NumberType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
										germToTransplant: import('@triplit/client').TypeInterface<
											'number',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').NumberType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
										germToFirstHarvest: import('@triplit/client').TypeInterface<
											'number',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').NumberType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
										firstToLastHarvest: import('@triplit/client').TypeInterface<
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
						frostDatePlantingWindows: import('@triplit/client').TypeInterface<
							'record',
							{
								optional: true;
							}
						> &
							Omit<
								import('@triplit/client').RecordType<
									{
										lastFrostWindowOpen: import('@triplit/client').TypeInterface<
											'number',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').NumberType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
										lastFrostWindowClose: import('@triplit/client').TypeInterface<
											'number',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').NumberType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
										firstFrostWindowOpen: import('@triplit/client').TypeInterface<
											'number',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').NumberType<{}>,
												keyof import('@triplit/client').TypeInterface<string, {}>
											>;
										firstFrostWindowClose: import('@triplit/client').TypeInterface<
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
						origin: import('@triplit/client').TypeInterface<
							'record',
							{
								optional: true;
							}
						> &
							Omit<
								import('@triplit/client').RecordType<
									{
										transplantable: import('@triplit/client').TypeInterface<
											'boolean',
											{
												optional: true;
											}
										> &
											Omit<
												import('@triplit/client').BooleanType<{}>,
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
			collection: {
				query: {
					collectionName: 'cultivarCollections';
					where: any;
				};
				cardinality: 'one';
			};
			parent: {
				query: {
					collectionName: 'cultivars';
					where: any;
				};
				cardinality: 'one';
			};
		};
		permissions: {
			anon: {
				read: {
					filter: ['collection.visibility', string, string][];
				};
			};
			user: {
				read: {
					filter: {
						mod: 'or';
						filters: (
							| ['collection.visibility', string, string]
							| ['collection.userId', string, string]
							| ['collection.garden.adminIds', string, string]
							| ['collection.garden.editorIds', string, string]
							| ['collection.garden.viewerIds', string, string]
						)[];
					}[];
				};
				insert: {
					filter: {
						mod: 'or';
						filters: (
							| ['collection.userId', string, string]
							| ['collection.garden.adminIds', string, string]
						)[];
					}[];
				};
				update: {
					filter: {
						mod: 'or';
						filters: (
							| ['collection.userId', string, string]
							| ['collection.garden.adminIds', string, string]
						)[];
					}[];
				};
				delete: {
					filter: {
						mod: 'or';
						filters: (
							| ['collection.userId', string, string]
							| ['collection.garden.adminIds', string, string]
						)[];
					}[];
				};
			};
		};
	};
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
				name: import('@triplit/client').StringType<{}>;
				description: import('@triplit/client').StringType<{
					default: string;
				}>;
				parentType: import('@triplit/client').StringType<{
					enum: ('GARDEN' | 'WORKSPACE' | 'PLANTING_AREA' | 'INDEPENDENT')[];
					default: string;
				}>;
				gardenId: import('@triplit/client').StringType<{}>;
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
/** Export Triplit roles. */
export { roles };
export type TriplitTransaction = DBTransaction<typeof schema>;
//# sourceMappingURL=index.d.ts.map
