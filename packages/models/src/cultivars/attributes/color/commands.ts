import { z } from 'zod';

/** Field specifications. */
const colorSchema = z.string().describe('May be a hex value');
export const fields = {
	colorSchema
};

/** Update command. */
export const ColorUpdateCommandSchema = z.object({
	baseColor: colorSchema.optional(),
	outlineColor: colorSchema.optional(),
	textColor: colorSchema.optional()
});
export type ColorUpdateCommand = z.infer<typeof ColorUpdateCommandSchema>;
export type ColorProfile = z.infer<typeof ColorUpdateCommandSchema>;
