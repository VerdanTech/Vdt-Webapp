import z from 'zod';

export declare const workspaceFields: {
	workspaceNameSchema: z.ZodString;
	workspaceDescriptionSchema: z.ZodString;
	plantingAreaNameSchema: z.ZodString;
	plantingAreaDescriptionSchema: z.ZodString;
	plantingAreaDepthSchema: z.ZodNumber;
	coordinateXSchema: z.ZodNumber;
	coordinateYSchema: z.ZodNumber;
	coordinateSchema: z.ZodObject<
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
	locationDateSchema: z.ZodDate;
	geometryTypeSchema: z.ZodEnum<['RECTANGLE', 'POLYGON', 'ELLIPSE', 'LINES']>;
	geometryDateSchema: z.ZodDate;
	geometryScaleFactorSchema: z.ZodNumber;
	geometryRotationSchema: z.ZodNumber;
	geometryRectangleLengthSchema: z.ZodNumber;
	geometryRectangleWidthSchema: z.ZodNumber;
	geometryPolygonNumSidesSchema: z.ZodNumber;
	geometryPolygonRadiusSchema: z.ZodNumber;
	geometryEllipseLengthSchema: z.ZodNumber;
	geometryEllipseWidthSchema: z.ZodNumber;
	geometryLinesCoordinatesSchema: z.ZodArray<
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
	>;
	geometryLinesClosedSchema: z.ZodBoolean;
};
/** Commands. */
/**
 * Create a new location.
 */
export declare const LocationCreateCommandSchema: z.ZodObject<
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
>;
export type LocationCreateCommand = z.infer<typeof LocationCreateCommandSchema>;
/**
 * Creates a location history.
 */
export declare const LocationHistoryCreateCommandSchema: z.ZodObject<
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
>;
export type LocationHistoryCreateCommand = z.infer<
	typeof LocationHistoryCreateCommandSchema
>;
/**
 * Updates a location history.
 */
export declare const LocationHistoryUpdateCommandSchema: z.ZodObject<
	{
		id: z.ZodString;
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
		id: string;
		date: Date;
		coordinate: {
			x: number;
			y: number;
		};
		workspaceId: string;
	},
	{
		id: string;
		date: Date;
		coordinate: {
			x: number;
			y: number;
		};
		workspaceId: string;
	}
>;
export type LocationHistoryUpdateCommand = z.infer<
	typeof LocationHistoryUpdateCommandSchema
>;
/**
 * Updates a location.
 */
export declare const LocationUpdateCommandSchema: z.ZodObject<
	{
		coordinate: z.ZodOptional<
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
			>
		>;
		date: z.ZodOptional<z.ZodDate>;
		workspaceId: z.ZodOptional<z.ZodString>;
		delete: z.ZodOptional<z.ZodBoolean>;
	},
	'strip',
	z.ZodTypeAny,
	{
		date?: Date | undefined;
		delete?: boolean | undefined;
		coordinate?:
			| {
					x: number;
					y: number;
			  }
			| undefined;
		workspaceId?: string | undefined;
	},
	{
		date?: Date | undefined;
		delete?: boolean | undefined;
		coordinate?:
			| {
					x: number;
					y: number;
			  }
			| undefined;
		workspaceId?: string | undefined;
	}
>;
export type LocationUpdateCommand = z.infer<typeof LocationUpdateCommandSchema>;
/**
 * Updates a location
 */
/**
 * Create a new geometry.
 */
export declare const GeometryCreateCommandSchema: z.ZodObject<
	{
		type: z.ZodDefault<z.ZodEnum<['RECTANGLE', 'POLYGON', 'ELLIPSE', 'LINES']>>;
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
>;
export type GeometryCreateCommand = z.infer<typeof GeometryCreateCommandSchema>;
/**
 * Update a geometry.
 */
export declare const GeometryUpdateCommandSchema: z.ZodObject<
	{
		type: z.ZodOptional<z.ZodEnum<['RECTANGLE', 'POLYGON', 'ELLIPSE', 'LINES']>>;
		date: z.ZodOptional<z.ZodDate>;
		scaleFactor: z.ZodOptional<z.ZodNumber>;
		rotation: z.ZodOptional<z.ZodNumber>;
		rectangleLength: z.ZodOptional<z.ZodNumber>;
		rectangleWidth: z.ZodOptional<z.ZodNumber>;
		polygonNumSides: z.ZodOptional<z.ZodNumber>;
		polygonRadius: z.ZodOptional<z.ZodNumber>;
		ellipseLength: z.ZodOptional<z.ZodNumber>;
		ellipseWidth: z.ZodOptional<z.ZodNumber>;
		linesCoordinates: z.ZodOptional<
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
		linesClosed: z.ZodOptional<z.ZodBoolean>;
		delete: z.ZodOptional<z.ZodBoolean>;
	},
	'strip',
	z.ZodTypeAny,
	{
		type?: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES' | undefined;
		date?: Date | undefined;
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
		delete?: boolean | undefined;
	},
	{
		type?: 'RECTANGLE' | 'POLYGON' | 'ELLIPSE' | 'LINES' | undefined;
		date?: Date | undefined;
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
		delete?: boolean | undefined;
	}
>;
export type GeometryUpdateCommand = z.infer<typeof GeometryUpdateCommandSchema>;
/**
 * Creates a geometry history.
 */
export declare const GeometryHistoryCreateCommandSchema: z.ZodObject<
	{
		gardenId: z.ZodString;
		geometries: z.ZodArray<
			z.ZodObject<
				{
					type: z.ZodDefault<z.ZodEnum<['RECTANGLE', 'POLYGON', 'ELLIPSE', 'LINES']>>;
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
>;
export type GeometryHistoryCreateCommand = z.infer<
	typeof GeometryHistoryCreateCommandSchema
>;
/**
 * Updates a geometry history.
 */
export declare const GeometryHistoryUpdateCommandSchema: z.ZodObject<
	{
		id: z.ZodString;
		geometry: z.ZodObject<
			{
				type: z.ZodDefault<z.ZodEnum<['RECTANGLE', 'POLYGON', 'ELLIPSE', 'LINES']>>;
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
		>;
		date: z.ZodDate;
	},
	'strip',
	z.ZodTypeAny,
	{
		id: string;
		date: Date;
		geometry: {
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
		};
	},
	{
		id: string;
		date: Date;
		geometry: {
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
		};
	}
>;
export type GeometryHistoryUpdateCommand = z.infer<
	typeof GeometryHistoryUpdateCommandSchema
>;
/**
 * Create a new workspace.
 */
export declare const WorkspaceCreateCommandSchema: z.ZodObject<
	{
		gardenId: z.ZodString;
		name: z.ZodString;
		description: z.ZodOptional<z.ZodString>;
	},
	'strip',
	z.ZodTypeAny,
	{
		name: string;
		gardenId: string;
		description?: string | undefined;
	},
	{
		name: string;
		gardenId: string;
		description?: string | undefined;
	}
>;
export type WorkspaceCreateCommand = z.infer<typeof WorkspaceCreateCommandSchema>;
/**
 * Update a workspace.
 */
export declare const WorkspaceUpdateCommandSchema: z.ZodObject<
	{
		name: z.ZodOptional<z.ZodString>;
		description: z.ZodOptional<z.ZodString>;
	},
	'strip',
	z.ZodTypeAny,
	{
		name?: string | undefined;
		description?: string | undefined;
	},
	{
		name?: string | undefined;
		description?: string | undefined;
	}
>;
export type WorkspaceUpdateCommand = z.infer<typeof WorkspaceUpdateCommandSchema>;
/**
 * Create a new planting area.
 */
export declare const PlantingAreaCreateCommandSchema: z.ZodObject<
	{
		gardenId: z.ZodString;
		workspaceId: z.ZodString;
		name: z.ZodString;
		description: z.ZodDefault<z.ZodString>;
		location: z.ZodObject<
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
		>;
		geometry: z.ZodObject<
			{
				type: z.ZodDefault<z.ZodEnum<['RECTANGLE', 'POLYGON', 'ELLIPSE', 'LINES']>>;
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
		>;
		depth: z.ZodDefault<z.ZodNumber>;
	},
	'strip',
	z.ZodTypeAny,
	{
		name: string;
		gardenId: string;
		geometry: {
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
		};
		description: string;
		location: {
			gardenId: string;
			date: Date;
			coordinate: {
				x: number;
				y: number;
			};
			workspaceId: string;
		};
		depth: number;
		workspaceId: string;
	},
	{
		name: string;
		gardenId: string;
		geometry: {
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
		};
		location: {
			gardenId: string;
			date: Date;
			coordinate: {
				x: number;
				y: number;
			};
			workspaceId: string;
		};
		workspaceId: string;
		description?: string | undefined;
		depth?: number | undefined;
	}
>;
export type PlantingAreaCreateCommand = z.infer<typeof PlantingAreaCreateCommandSchema>;
/**
 * Update a planting area.
 */
export declare const PlantingAreaUpdateCommandSchema: z.ZodObject<
	{
		name: z.ZodOptional<z.ZodString>;
		description: z.ZodOptional<z.ZodString>;
		depth: z.ZodOptional<z.ZodNumber>;
	},
	'strip',
	z.ZodTypeAny,
	{
		name?: string | undefined;
		description?: string | undefined;
		depth?: number | undefined;
	},
	{
		name?: string | undefined;
		description?: string | undefined;
		depth?: number | undefined;
	}
>;
export type PlantingAreaUpdateCommand = z.infer<typeof PlantingAreaUpdateCommandSchema>;
//# sourceMappingURL=commands.d.ts.map
