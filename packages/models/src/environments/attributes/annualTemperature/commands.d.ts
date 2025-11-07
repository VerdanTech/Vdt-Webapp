import { z } from 'zod';

export declare const fields: {
	minimumAnnualTempSchema: z.ZodNumber;
	maximumAnnualTempSchema: z.ZodNumber;
};
/** Update command. */
export declare const AnnualTemperatureUpdateCommandSchema: z.ZodObject<
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
>;
export type AnnualTemperatureUpdateCommand = z.infer<
	typeof AnnualTemperatureUpdateCommandSchema
>;
//# sourceMappingURL=commands.d.ts.map
