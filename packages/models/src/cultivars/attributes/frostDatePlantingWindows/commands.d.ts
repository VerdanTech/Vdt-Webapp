import { z } from 'zod';

export declare const fields: {
	lastFrostWindowOpenSchema: z.ZodNumber;
	lastFrostWindowCloseSchema: z.ZodNumber;
	firstFrostWindowOpenSchema: z.ZodNumber;
	firstFrostWindowCloseSchema: z.ZodNumber;
};
/** Update command. */
export declare const FrostDatePlantingWindowsUpdateCommandSchema: z.ZodObject<
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
>;
export type FrostDatePlantingWindowsUpdateCommand = z.infer<
	typeof FrostDatePlantingWindowsUpdateCommandSchema
>;
//# sourceMappingURL=commands.d.ts.map
