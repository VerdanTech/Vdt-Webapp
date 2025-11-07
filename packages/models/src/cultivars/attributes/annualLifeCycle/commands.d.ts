import { z } from 'zod';

export declare const fields: {
	sowToGermSchema: z.ZodNumber;
	germToTransplantSchema: z.ZodNumber;
	germToFirstHarvestSchema: z.ZodNumber;
	firstToLastHarvestSchema: z.ZodNumber;
};
/** Update command. */
export declare const AnnualLifecycleUpdateCommandSchema: z.ZodObject<
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
>;
export type AnnualLifecycleUpdateCommand = z.infer<
	typeof AnnualLifecycleUpdateCommandSchema
>;
//# sourceMappingURL=commands.d.ts.map
