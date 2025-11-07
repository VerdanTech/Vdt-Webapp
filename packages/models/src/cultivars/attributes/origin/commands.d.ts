import { z } from 'zod';

export declare const fields: {
	transplantableSchema: z.ZodBoolean;
};
/** Update command. */
export declare const OriginUpdateCommandSchema: z.ZodObject<
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
>;
export type OriginUpdateCommand = z.infer<typeof OriginUpdateCommandSchema>;
//# sourceMappingURL=commands.d.ts.map
