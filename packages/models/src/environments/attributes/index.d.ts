import { z } from 'zod';

export declare const attributesSchemas: {
	minimumAnnualTempSchema: z.ZodNumber;
	maximumAnnualTempSchema: z.ZodNumber;
	lastFrostDateSchema: z.ZodDate;
	firstFrostDateSchema: z.ZodDate;
};
export declare const EnvironmentAttributes: import('@triplit/client').RecordType<
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
export declare const EnvironmentAttributesUpdateCommandSchema: z.ZodObject<
	{
		frostDates: z.ZodOptional<
			z.ZodObject<
				{
					lastFrostDate: z.ZodOptional<z.ZodDate>;
					firstFrostDate: z.ZodOptional<z.ZodDate>;
				},
				'strip',
				z.ZodTypeAny,
				{
					lastFrostDate?: Date | undefined;
					firstFrostDate?: Date | undefined;
				},
				{
					lastFrostDate?: Date | undefined;
					firstFrostDate?: Date | undefined;
				}
			>
		>;
		annualTemperature: z.ZodOptional<
			z.ZodObject<
				{
					minimum: z.ZodOptional<z.ZodNumber>;
					maximum: z.ZodOptional<z.ZodNumber>;
				},
				'strip',
				z.ZodTypeAny,
				{
					minimum?: number | undefined;
					maximum?: number | undefined;
				},
				{
					minimum?: number | undefined;
					maximum?: number | undefined;
				}
			>
		>;
	},
	'strip',
	z.ZodTypeAny,
	{
		frostDates?:
			| {
					lastFrostDate?: Date | undefined;
					firstFrostDate?: Date | undefined;
			  }
			| undefined;
		annualTemperature?:
			| {
					minimum?: number | undefined;
					maximum?: number | undefined;
			  }
			| undefined;
	},
	{
		frostDates?:
			| {
					lastFrostDate?: Date | undefined;
					firstFrostDate?: Date | undefined;
			  }
			| undefined;
		annualTemperature?:
			| {
					minimum?: number | undefined;
					maximum?: number | undefined;
			  }
			| undefined;
	}
>;
export type EnvironmentAttributesUpdateCommand = z.infer<
	typeof EnvironmentAttributesUpdateCommandSchema
>;
//# sourceMappingURL=index.d.ts.map
