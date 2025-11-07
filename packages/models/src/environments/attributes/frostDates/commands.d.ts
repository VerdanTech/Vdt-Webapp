import { z } from 'zod';

export declare const fields: {
	lastFrostDateSchema: z.ZodDate;
	firstFrostDateSchema: z.ZodDate;
};
/** Update command. */
export declare const FrostDatesUpdateCommandSchema: z.ZodObject<
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
>;
export type FrostDatesUpdateCommand = z.infer<typeof FrostDatesUpdateCommandSchema>;
//# sourceMappingURL=commands.d.ts.map
