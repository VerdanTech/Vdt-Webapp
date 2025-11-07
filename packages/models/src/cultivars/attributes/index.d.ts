import { z } from 'zod';

export declare const attributesSchemas: {
	transplantableSchema: z.ZodBoolean;
	lastFrostWindowOpenSchema: z.ZodNumber;
	lastFrostWindowCloseSchema: z.ZodNumber;
	firstFrostWindowOpenSchema: z.ZodNumber;
	firstFrostWindowCloseSchema: z.ZodNumber;
	sowToGermSchema: z.ZodNumber;
	germToTransplantSchema: z.ZodNumber;
	germToFirstHarvestSchema: z.ZodNumber;
	firstToLastHarvestSchema: z.ZodNumber;
};
export declare const CultivarAttributes: import('@triplit/client').RecordType<
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
export declare const CultivarAttributesUpdateCommandSchema: z.ZodObject<
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
export type CultivarAttributesUpdateCommand = z.infer<
	typeof CultivarAttributesUpdateCommandSchema
>;
//# sourceMappingURL=index.d.ts.map
