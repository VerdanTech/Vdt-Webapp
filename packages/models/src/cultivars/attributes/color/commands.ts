import { z } from 'zod';

import fields from './fields.js';

/** Update command. */
export const ColorUpdateCommandSchema = z.object({
	baseColor: fields.colorField.optional(),
	outlineColor: fields.colorField.optional(),
	textColor: fields.colorField.optional()
});
export type ColorUpdateCommand = z.infer<typeof ColorUpdateCommandSchema>;
