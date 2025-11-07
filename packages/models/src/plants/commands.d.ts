import z from 'zod';

/** PlantGroups. */
export declare const plantFields: {
	harvestDateSchema: z.ZodDate;
	harvestMassSchema: z.ZodNumber;
	harvestUnitsSchema: z.ZodNumber;
	harvestQualitySchema: z.ZodEnum<['COMPOST', 'LOW', 'MEDIUM', 'HIGH', 'PERFECT']>;
	harvestDescriptionSchema: z.ZodString;
	lifespanOriginSchema: z.ZodEnum<
		['DIRECT_SEED', 'SEED_TO_TRANSPLANT', 'SEEDLING_TO_TRANSPLANT']
	>;
	LifespanDateSchema: z.ZodDate;
	plantCultivarNameSchema: z.ZodString;
	plantCultivarAttributesSchema: z.ZodObject<
		{
			annualLifeCycle: z.ZodOptional<
				z.ZodObject<
					{
						sowToGerm: z.ZodOptional<z.ZodNumber>;
						germToTransplant: z.ZodOptional<z.ZodNumber>;
						germToFirstHarvest: z.ZodOptional<z.ZodNumber>;
						firstToLastHarvest: z.ZodOptional<z.ZodNumber>;
					},
					'strip',
					z.ZodTypeAny,
					{
						sowToGerm?: number | undefined;
						germToTransplant?: number | undefined;
						germToFirstHarvest?: number | undefined;
						firstToLastHarvest?: number | undefined;
					},
					{
						sowToGerm?: number | undefined;
						germToTransplant?: number | undefined;
						germToFirstHarvest?: number | undefined;
						firstToLastHarvest?: number | undefined;
					}
				>
			>;
			frostDatePlantingWindows: z.ZodOptional<
				z.ZodObject<
					{
						lastFrostWindowOpen: z.ZodOptional<z.ZodNumber>;
						lastFrostWindowClose: z.ZodOptional<z.ZodNumber>;
						firstFrostWindowOpen: z.ZodOptional<z.ZodNumber>;
						firstFrostWindowClose: z.ZodOptional<z.ZodNumber>;
					},
					'strip',
					z.ZodTypeAny,
					{
						lastFrostWindowOpen?: number | undefined;
						lastFrostWindowClose?: number | undefined;
						firstFrostWindowOpen?: number | undefined;
						firstFrostWindowClose?: number | undefined;
					},
					{
						lastFrostWindowOpen?: number | undefined;
						lastFrostWindowClose?: number | undefined;
						firstFrostWindowOpen?: number | undefined;
						firstFrostWindowClose?: number | undefined;
					}
				>
			>;
			origin: z.ZodOptional<
				z.ZodObject<
					{
						transplantable: z.ZodOptional<z.ZodBoolean>;
					},
					'strip',
					z.ZodTypeAny,
					{
						transplantable?: boolean | undefined;
					},
					{
						transplantable?: boolean | undefined;
					}
				>
			>;
		},
		'strip',
		z.ZodTypeAny,
		{
			origin?:
				| {
						transplantable?: boolean | undefined;
				  }
				| undefined;
			annualLifeCycle?:
				| {
						sowToGerm?: number | undefined;
						germToTransplant?: number | undefined;
						germToFirstHarvest?: number | undefined;
						firstToLastHarvest?: number | undefined;
				  }
				| undefined;
			frostDatePlantingWindows?:
				| {
						lastFrostWindowOpen?: number | undefined;
						lastFrostWindowClose?: number | undefined;
						firstFrostWindowOpen?: number | undefined;
						firstFrostWindowClose?: number | undefined;
				  }
				| undefined;
		},
		{
			origin?:
				| {
						transplantable?: boolean | undefined;
				  }
				| undefined;
			annualLifeCycle?:
				| {
						sowToGerm?: number | undefined;
						germToTransplant?: number | undefined;
						germToFirstHarvest?: number | undefined;
						firstToLastHarvest?: number | undefined;
				  }
				| undefined;
			frostDatePlantingWindows?:
				| {
						lastFrostWindowOpen?: number | undefined;
						lastFrostWindowClose?: number | undefined;
						firstFrostWindowOpen?: number | undefined;
						firstFrostWindowClose?: number | undefined;
				  }
				| undefined;
		}
	>;
	plantAggregateSchema: z.ZodBoolean;
};
/** Commands. */
export declare const PlantsCreateFormModeOptions: readonly [
	'SINGLE',
	'GROUP',
	'PATTERN',
	'COMBINED'
];
export type PlantsCreateFormMode = (typeof PlantsCreateFormModeOptions)[number];
/**
 * Adds a plant to the model.
 */
export declare const plantsCreateCommandSinglePlantSchema: z.ZodObject<
	{
		cultivarName: z.ZodDefault<z.ZodString>;
		origin: z.ZodDefault<
			z.ZodEnum<['DIRECT_SEED', 'SEED_TO_TRANSPLANT', 'SEEDLING_TO_TRANSPLANT']>
		>;
		locationHistory: z.ZodDefault<
			z.ZodObject<
				{
					gardenId: z.ZodString;
					locations: z.ZodArray<
						z.ZodObject<
							{
								gardenId: z.ZodString;
								workspaceId: z.ZodString;
								coordinate: z.ZodObject<
									{
										x: z.ZodNumber;
										y: z.ZodNumber;
									},
									'strip',
									z.ZodTypeAny,
									{
										x: number;
										y: number;
									},
									{
										x: number;
										y: number;
									}
								>;
								date: z.ZodDate;
							},
							'strip',
							z.ZodTypeAny,
							{
								gardenId: string;
								date: Date;
								coordinate: {
									x: number;
									y: number;
								};
								workspaceId: string;
							},
							{
								gardenId: string;
								date: Date;
								coordinate: {
									x: number;
									y: number;
								};
								workspaceId: string;
							}
						>,
						'many'
					>;
				},
				'strip',
				z.ZodTypeAny,
				{
					gardenId: string;
					locations: {
						gardenId: string;
						date: Date;
						coordinate: {
							x: number;
							y: number;
						};
						workspaceId: string;
					}[];
				},
				{
					gardenId: string;
					locations: {
						gardenId: string;
						date: Date;
						coordinate: {
							x: number;
							y: number;
						};
						workspaceId: string;
					}[];
				}
			>
		>;
		geometryHistory: z.ZodDefault<
			z.ZodObject<
				{
					gardenId: z.ZodString;
					geometries: z.ZodArray<
						z.ZodObject<
							{
								type: z.ZodDefault<
									z.ZodEnum<['RECTANGLE', 'POLYGON', 'ELLIPSE', 'LINES']>
								>;
								date: z.ZodDate;
								scaleFactor: z.ZodDefault<z.ZodNumber>;
								rotation: z.ZodDefault<z.ZodNumber>;
								rectangleLength: z.ZodDefault<z.ZodNumber>;
								rectangleWidth: z.ZodDefault<z.ZodNumber>;
								polygonNumSides: z.ZodDefault<z.ZodNumber>;
								polygonRadius: z.ZodDefault<z.ZodNumber>;
								ellipseLength: z.ZodDefault<z.ZodNumber>;
								ellipseWidth: z.ZodDefault<z.ZodNumber>;
								linesCoordinates: z.ZodDefault<
									z.ZodArray<
										z.ZodObject<
											{
												x: z.ZodNumber;
												y: z.ZodNumber;
											},
											'strip',
											z.ZodTypeAny,
											{
												x: number;
												y: number;
											},
											{
												x: number;
												y: number;
											}
										>,
										'many'
									>
								>;
								linesClosed: z.ZodDefault<z.ZodBoolean>;
							},
							'strip',
							z.ZodTypeAny,
							{
								type: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES';
								date: Date;
								rectangleLength: number;
								rectangleWidth: number;
								polygonRadius: number;
								ellipseLength: number;
								ellipseWidth: number;
								linesCoordinates: {
									x: number;
									y: number;
								}[];
								rotation: number;
								polygonNumSides: number;
								linesClosed: boolean;
								scaleFactor: number;
							},
							{
								date: Date;
								type?: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES' | undefined;
								rectangleLength?: number | undefined;
								rectangleWidth?: number | undefined;
								polygonRadius?: number | undefined;
								ellipseLength?: number | undefined;
								ellipseWidth?: number | undefined;
								linesCoordinates?:
									| {
											x: number;
											y: number;
									  }[]
									| undefined;
								rotation?: number | undefined;
								polygonNumSides?: number | undefined;
								linesClosed?: boolean | undefined;
								scaleFactor?: number | undefined;
							}
						>,
						'many'
					>;
				},
				'strip',
				z.ZodTypeAny,
				{
					gardenId: string;
					geometries: {
						type: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES';
						date: Date;
						rectangleLength: number;
						rectangleWidth: number;
						polygonRadius: number;
						ellipseLength: number;
						ellipseWidth: number;
						linesCoordinates: {
							x: number;
							y: number;
						}[];
						rotation: number;
						polygonNumSides: number;
						linesClosed: boolean;
						scaleFactor: number;
					}[];
				},
				{
					gardenId: string;
					geometries: {
						date: Date;
						type?: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES' | undefined;
						rectangleLength?: number | undefined;
						rectangleWidth?: number | undefined;
						polygonRadius?: number | undefined;
						ellipseLength?: number | undefined;
						ellipseWidth?: number | undefined;
						linesCoordinates?:
							| {
									x: number;
									y: number;
							  }[]
							| undefined;
						rotation?: number | undefined;
						polygonNumSides?: number | undefined;
						linesClosed?: boolean | undefined;
						scaleFactor?: number | undefined;
					}[];
				}
			>
		>;
		cultivarOverride: z.ZodObject<
			{
				annualLifeCycle: z.ZodOptional<
					z.ZodObject<
						{
							sowToGerm: z.ZodOptional<z.ZodNumber>;
							germToTransplant: z.ZodOptional<z.ZodNumber>;
							germToFirstHarvest: z.ZodOptional<z.ZodNumber>;
							firstToLastHarvest: z.ZodOptional<z.ZodNumber>;
						},
						'strip',
						z.ZodTypeAny,
						{
							sowToGerm?: number | undefined;
							germToTransplant?: number | undefined;
							germToFirstHarvest?: number | undefined;
							firstToLastHarvest?: number | undefined;
						},
						{
							sowToGerm?: number | undefined;
							germToTransplant?: number | undefined;
							germToFirstHarvest?: number | undefined;
							firstToLastHarvest?: number | undefined;
						}
					>
				>;
				frostDatePlantingWindows: z.ZodOptional<
					z.ZodObject<
						{
							lastFrostWindowOpen: z.ZodOptional<z.ZodNumber>;
							lastFrostWindowClose: z.ZodOptional<z.ZodNumber>;
							firstFrostWindowOpen: z.ZodOptional<z.ZodNumber>;
							firstFrostWindowClose: z.ZodOptional<z.ZodNumber>;
						},
						'strip',
						z.ZodTypeAny,
						{
							lastFrostWindowOpen?: number | undefined;
							lastFrostWindowClose?: number | undefined;
							firstFrostWindowOpen?: number | undefined;
							firstFrostWindowClose?: number | undefined;
						},
						{
							lastFrostWindowOpen?: number | undefined;
							lastFrostWindowClose?: number | undefined;
							firstFrostWindowOpen?: number | undefined;
							firstFrostWindowClose?: number | undefined;
						}
					>
				>;
				origin: z.ZodOptional<
					z.ZodObject<
						{
							transplantable: z.ZodOptional<z.ZodBoolean>;
						},
						'strip',
						z.ZodTypeAny,
						{
							transplantable?: boolean | undefined;
						},
						{
							transplantable?: boolean | undefined;
						}
					>
				>;
			},
			'strip',
			z.ZodTypeAny,
			{
				origin?:
					| {
							transplantable?: boolean | undefined;
					  }
					| undefined;
				annualLifeCycle?:
					| {
							sowToGerm?: number | undefined;
							germToTransplant?: number | undefined;
							germToFirstHarvest?: number | undefined;
							firstToLastHarvest?: number | undefined;
					  }
					| undefined;
				frostDatePlantingWindows?:
					| {
							lastFrostWindowOpen?: number | undefined;
							lastFrostWindowClose?: number | undefined;
							firstFrostWindowOpen?: number | undefined;
							firstFrostWindowClose?: number | undefined;
					  }
					| undefined;
			},
			{
				origin?:
					| {
							transplantable?: boolean | undefined;
					  }
					| undefined;
				annualLifeCycle?:
					| {
							sowToGerm?: number | undefined;
							germToTransplant?: number | undefined;
							germToFirstHarvest?: number | undefined;
							firstToLastHarvest?: number | undefined;
					  }
					| undefined;
				frostDatePlantingWindows?:
					| {
							lastFrostWindowOpen?: number | undefined;
							lastFrostWindowClose?: number | undefined;
							firstFrostWindowOpen?: number | undefined;
							firstFrostWindowClose?: number | undefined;
					  }
					| undefined;
			}
		>;
		aggregate: z.ZodDefault<z.ZodBoolean>;
	},
	'strip',
	z.ZodTypeAny,
	{
		origin: 'DIRECT_SEED' | 'SEED_TO_TRANSPLANT' | 'SEEDLING_TO_TRANSPLANT';
		locationHistory: {
			gardenId: string;
			locations: {
				gardenId: string;
				date: Date;
				coordinate: {
					x: number;
					y: number;
				};
				workspaceId: string;
			}[];
		};
		geometryHistory: {
			gardenId: string;
			geometries: {
				type: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES';
				date: Date;
				rectangleLength: number;
				rectangleWidth: number;
				polygonRadius: number;
				ellipseLength: number;
				ellipseWidth: number;
				linesCoordinates: {
					x: number;
					y: number;
				}[];
				rotation: number;
				polygonNumSides: number;
				linesClosed: boolean;
				scaleFactor: number;
			}[];
		};
		cultivarName: string;
		aggregate: boolean;
		cultivarOverride: {
			origin?:
				| {
						transplantable?: boolean | undefined;
				  }
				| undefined;
			annualLifeCycle?:
				| {
						sowToGerm?: number | undefined;
						germToTransplant?: number | undefined;
						germToFirstHarvest?: number | undefined;
						firstToLastHarvest?: number | undefined;
				  }
				| undefined;
			frostDatePlantingWindows?:
				| {
						lastFrostWindowOpen?: number | undefined;
						lastFrostWindowClose?: number | undefined;
						firstFrostWindowOpen?: number | undefined;
						firstFrostWindowClose?: number | undefined;
				  }
				| undefined;
		};
	},
	{
		cultivarOverride: {
			origin?:
				| {
						transplantable?: boolean | undefined;
				  }
				| undefined;
			annualLifeCycle?:
				| {
						sowToGerm?: number | undefined;
						germToTransplant?: number | undefined;
						germToFirstHarvest?: number | undefined;
						firstToLastHarvest?: number | undefined;
				  }
				| undefined;
			frostDatePlantingWindows?:
				| {
						lastFrostWindowOpen?: number | undefined;
						lastFrostWindowClose?: number | undefined;
						firstFrostWindowOpen?: number | undefined;
						firstFrostWindowClose?: number | undefined;
				  }
				| undefined;
		};
		origin?:
			| 'DIRECT_SEED'
			| 'SEED_TO_TRANSPLANT'
			| 'SEEDLING_TO_TRANSPLANT'
			| undefined;
		locationHistory?:
			| {
					gardenId: string;
					locations: {
						gardenId: string;
						date: Date;
						coordinate: {
							x: number;
							y: number;
						};
						workspaceId: string;
					}[];
			  }
			| undefined;
		geometryHistory?:
			| {
					gardenId: string;
					geometries: {
						date: Date;
						type?: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES' | undefined;
						rectangleLength?: number | undefined;
						rectangleWidth?: number | undefined;
						polygonRadius?: number | undefined;
						ellipseLength?: number | undefined;
						ellipseWidth?: number | undefined;
						linesCoordinates?:
							| {
									x: number;
									y: number;
							  }[]
							| undefined;
						rotation?: number | undefined;
						polygonNumSides?: number | undefined;
						linesClosed?: boolean | undefined;
						scaleFactor?: number | undefined;
					}[];
			  }
			| undefined;
		cultivarName?: string | undefined;
		aggregate?: boolean | undefined;
	}
>;
export declare const plantsCreateFormModeSchema: z.ZodDefault<
	z.ZodEnum<['SINGLE', 'GROUP', 'PATTERN', 'COMBINED']>
>;
export declare const PlantsCreateCommandSchema: z.ZodObject<
	{
		gardenId: z.ZodString;
		mode: z.ZodDefault<
			z.ZodDefault<z.ZodEnum<['SINGLE', 'GROUP', 'PATTERN', 'COMBINED']>>
		>;
		plants: z.ZodArray<
			z.ZodObject<
				{
					cultivarName: z.ZodDefault<z.ZodString>;
					origin: z.ZodDefault<
						z.ZodEnum<['DIRECT_SEED', 'SEED_TO_TRANSPLANT', 'SEEDLING_TO_TRANSPLANT']>
					>;
					locationHistory: z.ZodDefault<
						z.ZodObject<
							{
								gardenId: z.ZodString;
								locations: z.ZodArray<
									z.ZodObject<
										{
											gardenId: z.ZodString;
											workspaceId: z.ZodString;
											coordinate: z.ZodObject<
												{
													x: z.ZodNumber;
													y: z.ZodNumber;
												},
												'strip',
												z.ZodTypeAny,
												{
													x: number;
													y: number;
												},
												{
													x: number;
													y: number;
												}
											>;
											date: z.ZodDate;
										},
										'strip',
										z.ZodTypeAny,
										{
											gardenId: string;
											date: Date;
											coordinate: {
												x: number;
												y: number;
											};
											workspaceId: string;
										},
										{
											gardenId: string;
											date: Date;
											coordinate: {
												x: number;
												y: number;
											};
											workspaceId: string;
										}
									>,
									'many'
								>;
							},
							'strip',
							z.ZodTypeAny,
							{
								gardenId: string;
								locations: {
									gardenId: string;
									date: Date;
									coordinate: {
										x: number;
										y: number;
									};
									workspaceId: string;
								}[];
							},
							{
								gardenId: string;
								locations: {
									gardenId: string;
									date: Date;
									coordinate: {
										x: number;
										y: number;
									};
									workspaceId: string;
								}[];
							}
						>
					>;
					geometryHistory: z.ZodDefault<
						z.ZodObject<
							{
								gardenId: z.ZodString;
								geometries: z.ZodArray<
									z.ZodObject<
										{
											type: z.ZodDefault<
												z.ZodEnum<['RECTANGLE', 'POLYGON', 'ELLIPSE', 'LINES']>
											>;
											date: z.ZodDate;
											scaleFactor: z.ZodDefault<z.ZodNumber>;
											rotation: z.ZodDefault<z.ZodNumber>;
											rectangleLength: z.ZodDefault<z.ZodNumber>;
											rectangleWidth: z.ZodDefault<z.ZodNumber>;
											polygonNumSides: z.ZodDefault<z.ZodNumber>;
											polygonRadius: z.ZodDefault<z.ZodNumber>;
											ellipseLength: z.ZodDefault<z.ZodNumber>;
											ellipseWidth: z.ZodDefault<z.ZodNumber>;
											linesCoordinates: z.ZodDefault<
												z.ZodArray<
													z.ZodObject<
														{
															x: z.ZodNumber;
															y: z.ZodNumber;
														},
														'strip',
														z.ZodTypeAny,
														{
															x: number;
															y: number;
														},
														{
															x: number;
															y: number;
														}
													>,
													'many'
												>
											>;
											linesClosed: z.ZodDefault<z.ZodBoolean>;
										},
										'strip',
										z.ZodTypeAny,
										{
											type: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES';
											date: Date;
											rectangleLength: number;
											rectangleWidth: number;
											polygonRadius: number;
											ellipseLength: number;
											ellipseWidth: number;
											linesCoordinates: {
												x: number;
												y: number;
											}[];
											rotation: number;
											polygonNumSides: number;
											linesClosed: boolean;
											scaleFactor: number;
										},
										{
											date: Date;
											type?: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES' | undefined;
											rectangleLength?: number | undefined;
											rectangleWidth?: number | undefined;
											polygonRadius?: number | undefined;
											ellipseLength?: number | undefined;
											ellipseWidth?: number | undefined;
											linesCoordinates?:
												| {
														x: number;
														y: number;
												  }[]
												| undefined;
											rotation?: number | undefined;
											polygonNumSides?: number | undefined;
											linesClosed?: boolean | undefined;
											scaleFactor?: number | undefined;
										}
									>,
									'many'
								>;
							},
							'strip',
							z.ZodTypeAny,
							{
								gardenId: string;
								geometries: {
									type: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES';
									date: Date;
									rectangleLength: number;
									rectangleWidth: number;
									polygonRadius: number;
									ellipseLength: number;
									ellipseWidth: number;
									linesCoordinates: {
										x: number;
										y: number;
									}[];
									rotation: number;
									polygonNumSides: number;
									linesClosed: boolean;
									scaleFactor: number;
								}[];
							},
							{
								gardenId: string;
								geometries: {
									date: Date;
									type?: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES' | undefined;
									rectangleLength?: number | undefined;
									rectangleWidth?: number | undefined;
									polygonRadius?: number | undefined;
									ellipseLength?: number | undefined;
									ellipseWidth?: number | undefined;
									linesCoordinates?:
										| {
												x: number;
												y: number;
										  }[]
										| undefined;
									rotation?: number | undefined;
									polygonNumSides?: number | undefined;
									linesClosed?: boolean | undefined;
									scaleFactor?: number | undefined;
								}[];
							}
						>
					>;
					cultivarOverride: z.ZodObject<
						{
							annualLifeCycle: z.ZodOptional<
								z.ZodObject<
									{
										sowToGerm: z.ZodOptional<z.ZodNumber>;
										germToTransplant: z.ZodOptional<z.ZodNumber>;
										germToFirstHarvest: z.ZodOptional<z.ZodNumber>;
										firstToLastHarvest: z.ZodOptional<z.ZodNumber>;
									},
									'strip',
									z.ZodTypeAny,
									{
										sowToGerm?: number | undefined;
										germToTransplant?: number | undefined;
										germToFirstHarvest?: number | undefined;
										firstToLastHarvest?: number | undefined;
									},
									{
										sowToGerm?: number | undefined;
										germToTransplant?: number | undefined;
										germToFirstHarvest?: number | undefined;
										firstToLastHarvest?: number | undefined;
									}
								>
							>;
							frostDatePlantingWindows: z.ZodOptional<
								z.ZodObject<
									{
										lastFrostWindowOpen: z.ZodOptional<z.ZodNumber>;
										lastFrostWindowClose: z.ZodOptional<z.ZodNumber>;
										firstFrostWindowOpen: z.ZodOptional<z.ZodNumber>;
										firstFrostWindowClose: z.ZodOptional<z.ZodNumber>;
									},
									'strip',
									z.ZodTypeAny,
									{
										lastFrostWindowOpen?: number | undefined;
										lastFrostWindowClose?: number | undefined;
										firstFrostWindowOpen?: number | undefined;
										firstFrostWindowClose?: number | undefined;
									},
									{
										lastFrostWindowOpen?: number | undefined;
										lastFrostWindowClose?: number | undefined;
										firstFrostWindowOpen?: number | undefined;
										firstFrostWindowClose?: number | undefined;
									}
								>
							>;
							origin: z.ZodOptional<
								z.ZodObject<
									{
										transplantable: z.ZodOptional<z.ZodBoolean>;
									},
									'strip',
									z.ZodTypeAny,
									{
										transplantable?: boolean | undefined;
									},
									{
										transplantable?: boolean | undefined;
									}
								>
							>;
						},
						'strip',
						z.ZodTypeAny,
						{
							origin?:
								| {
										transplantable?: boolean | undefined;
								  }
								| undefined;
							annualLifeCycle?:
								| {
										sowToGerm?: number | undefined;
										germToTransplant?: number | undefined;
										germToFirstHarvest?: number | undefined;
										firstToLastHarvest?: number | undefined;
								  }
								| undefined;
							frostDatePlantingWindows?:
								| {
										lastFrostWindowOpen?: number | undefined;
										lastFrostWindowClose?: number | undefined;
										firstFrostWindowOpen?: number | undefined;
										firstFrostWindowClose?: number | undefined;
								  }
								| undefined;
						},
						{
							origin?:
								| {
										transplantable?: boolean | undefined;
								  }
								| undefined;
							annualLifeCycle?:
								| {
										sowToGerm?: number | undefined;
										germToTransplant?: number | undefined;
										germToFirstHarvest?: number | undefined;
										firstToLastHarvest?: number | undefined;
								  }
								| undefined;
							frostDatePlantingWindows?:
								| {
										lastFrostWindowOpen?: number | undefined;
										lastFrostWindowClose?: number | undefined;
										firstFrostWindowOpen?: number | undefined;
										firstFrostWindowClose?: number | undefined;
								  }
								| undefined;
						}
					>;
					aggregate: z.ZodDefault<z.ZodBoolean>;
				},
				'strip',
				z.ZodTypeAny,
				{
					origin: 'DIRECT_SEED' | 'SEED_TO_TRANSPLANT' | 'SEEDLING_TO_TRANSPLANT';
					locationHistory: {
						gardenId: string;
						locations: {
							gardenId: string;
							date: Date;
							coordinate: {
								x: number;
								y: number;
							};
							workspaceId: string;
						}[];
					};
					geometryHistory: {
						gardenId: string;
						geometries: {
							type: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES';
							date: Date;
							rectangleLength: number;
							rectangleWidth: number;
							polygonRadius: number;
							ellipseLength: number;
							ellipseWidth: number;
							linesCoordinates: {
								x: number;
								y: number;
							}[];
							rotation: number;
							polygonNumSides: number;
							linesClosed: boolean;
							scaleFactor: number;
						}[];
					};
					cultivarName: string;
					aggregate: boolean;
					cultivarOverride: {
						origin?:
							| {
									transplantable?: boolean | undefined;
							  }
							| undefined;
						annualLifeCycle?:
							| {
									sowToGerm?: number | undefined;
									germToTransplant?: number | undefined;
									germToFirstHarvest?: number | undefined;
									firstToLastHarvest?: number | undefined;
							  }
							| undefined;
						frostDatePlantingWindows?:
							| {
									lastFrostWindowOpen?: number | undefined;
									lastFrostWindowClose?: number | undefined;
									firstFrostWindowOpen?: number | undefined;
									firstFrostWindowClose?: number | undefined;
							  }
							| undefined;
					};
				},
				{
					cultivarOverride: {
						origin?:
							| {
									transplantable?: boolean | undefined;
							  }
							| undefined;
						annualLifeCycle?:
							| {
									sowToGerm?: number | undefined;
									germToTransplant?: number | undefined;
									germToFirstHarvest?: number | undefined;
									firstToLastHarvest?: number | undefined;
							  }
							| undefined;
						frostDatePlantingWindows?:
							| {
									lastFrostWindowOpen?: number | undefined;
									lastFrostWindowClose?: number | undefined;
									firstFrostWindowOpen?: number | undefined;
									firstFrostWindowClose?: number | undefined;
							  }
							| undefined;
					};
					origin?:
						| 'DIRECT_SEED'
						| 'SEED_TO_TRANSPLANT'
						| 'SEEDLING_TO_TRANSPLANT'
						| undefined;
					locationHistory?:
						| {
								gardenId: string;
								locations: {
									gardenId: string;
									date: Date;
									coordinate: {
										x: number;
										y: number;
									};
									workspaceId: string;
								}[];
						  }
						| undefined;
					geometryHistory?:
						| {
								gardenId: string;
								geometries: {
									date: Date;
									type?: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES' | undefined;
									rectangleLength?: number | undefined;
									rectangleWidth?: number | undefined;
									polygonRadius?: number | undefined;
									ellipseLength?: number | undefined;
									ellipseWidth?: number | undefined;
									linesCoordinates?:
										| {
												x: number;
												y: number;
										  }[]
										| undefined;
									rotation?: number | undefined;
									polygonNumSides?: number | undefined;
									linesClosed?: boolean | undefined;
									scaleFactor?: number | undefined;
								}[];
						  }
						| undefined;
					cultivarName?: string | undefined;
					aggregate?: boolean | undefined;
				}
			>,
			'many'
		>;
	},
	'strip',
	z.ZodTypeAny,
	{
		gardenId: string;
		plants: {
			origin: 'DIRECT_SEED' | 'SEED_TO_TRANSPLANT' | 'SEEDLING_TO_TRANSPLANT';
			locationHistory: {
				gardenId: string;
				locations: {
					gardenId: string;
					date: Date;
					coordinate: {
						x: number;
						y: number;
					};
					workspaceId: string;
				}[];
			};
			geometryHistory: {
				gardenId: string;
				geometries: {
					type: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES';
					date: Date;
					rectangleLength: number;
					rectangleWidth: number;
					polygonRadius: number;
					ellipseLength: number;
					ellipseWidth: number;
					linesCoordinates: {
						x: number;
						y: number;
					}[];
					rotation: number;
					polygonNumSides: number;
					linesClosed: boolean;
					scaleFactor: number;
				}[];
			};
			cultivarName: string;
			aggregate: boolean;
			cultivarOverride: {
				origin?:
					| {
							transplantable?: boolean | undefined;
					  }
					| undefined;
				annualLifeCycle?:
					| {
							sowToGerm?: number | undefined;
							germToTransplant?: number | undefined;
							germToFirstHarvest?: number | undefined;
							firstToLastHarvest?: number | undefined;
					  }
					| undefined;
				frostDatePlantingWindows?:
					| {
							lastFrostWindowOpen?: number | undefined;
							lastFrostWindowClose?: number | undefined;
							firstFrostWindowOpen?: number | undefined;
							firstFrostWindowClose?: number | undefined;
					  }
					| undefined;
			};
		}[];
		mode: 'SINGLE' | 'GROUP' | 'PATTERN' | 'COMBINED';
	},
	{
		gardenId: string;
		plants: {
			cultivarOverride: {
				origin?:
					| {
							transplantable?: boolean | undefined;
					  }
					| undefined;
				annualLifeCycle?:
					| {
							sowToGerm?: number | undefined;
							germToTransplant?: number | undefined;
							germToFirstHarvest?: number | undefined;
							firstToLastHarvest?: number | undefined;
					  }
					| undefined;
				frostDatePlantingWindows?:
					| {
							lastFrostWindowOpen?: number | undefined;
							lastFrostWindowClose?: number | undefined;
							firstFrostWindowOpen?: number | undefined;
							firstFrostWindowClose?: number | undefined;
					  }
					| undefined;
			};
			origin?:
				| 'DIRECT_SEED'
				| 'SEED_TO_TRANSPLANT'
				| 'SEEDLING_TO_TRANSPLANT'
				| undefined;
			locationHistory?:
				| {
						gardenId: string;
						locations: {
							gardenId: string;
							date: Date;
							coordinate: {
								x: number;
								y: number;
							};
							workspaceId: string;
						}[];
				  }
				| undefined;
			geometryHistory?:
				| {
						gardenId: string;
						geometries: {
							date: Date;
							type?: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES' | undefined;
							rectangleLength?: number | undefined;
							rectangleWidth?: number | undefined;
							polygonRadius?: number | undefined;
							ellipseLength?: number | undefined;
							ellipseWidth?: number | undefined;
							linesCoordinates?:
								| {
										x: number;
										y: number;
								  }[]
								| undefined;
							rotation?: number | undefined;
							polygonNumSides?: number | undefined;
							linesClosed?: boolean | undefined;
							scaleFactor?: number | undefined;
						}[];
				  }
				| undefined;
			cultivarName?: string | undefined;
			aggregate?: boolean | undefined;
		}[];
		mode?: 'SINGLE' | 'GROUP' | 'PATTERN' | 'COMBINED' | undefined;
	}
>;
export type PlantsCreateCommand = z.infer<typeof PlantsCreateCommandSchema>;
//# sourceMappingURL=commands.d.ts.map
