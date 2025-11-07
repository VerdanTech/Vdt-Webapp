import { z } from 'zod';

export declare const environmentFields: {
	minimumAnnualTempSchema: z.ZodNumber;
	maximumAnnualTempSchema: z.ZodNumber;
	lastFrostDateSchema: z.ZodDate;
	firstFrostDateSchema: z.ZodDate;
	environmentNameSchema: z.ZodString;
	environmentDescriptionSchema: z.ZodString;
	environmentParentTypeSchema: z.ZodEnum<
		['GARDEN', 'WORKSPACE', 'PLANTING_AREA', 'INDEPENDENT']
	>;
};
/**
 * Command to create a new environment.
 */
export declare const EnvironmentCreateCommandSchema: z.ZodObject<
	{
		gardenId: z.ZodString;
		parendId: z.ZodString;
		parentType: z.ZodDefault<
			z.ZodEnum<['GARDEN', 'WORKSPACE', 'PLANTING_AREA', 'INDEPENDENT']>
		>;
		name: z.ZodString;
		description: z.ZodDefault<z.ZodString>;
	},
	'strip',
	z.ZodTypeAny,
	{
		name: string;
		gardenId: string;
		description: string;
		parentType: 'GARDEN' | 'WORKSPACE' | 'PLANTING_AREA' | 'INDEPENDENT';
		parendId: string;
	},
	{
		name: string;
		gardenId: string;
		parendId: string;
		description?: string | undefined;
		parentType?: 'GARDEN' | 'WORKSPACE' | 'PLANTING_AREA' | 'INDEPENDENT' | undefined;
	}
>;
export type EnvironmentCreateCommand = z.infer<typeof EnvironmentCreateCommandSchema>;
//# sourceMappingURL=commands.d.ts.map
