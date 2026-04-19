import { z } from 'jazz-tools';

/** Schema. */
export const ColorProfileSchema = z.object({
	baseColor: z.optional(z.string()).describe('May be a hex value.'),
	outlineColor: z.optional(z.string()).describe('May be a hex value.'),
	textColor: z.optional(z.string()).describe('May be a hex value.')
});
