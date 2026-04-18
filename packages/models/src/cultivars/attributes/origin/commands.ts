import { z } from 'zod';

import fields from './fields.js';

/** Update command. */
export const OriginUpdateCommandSchema = z
	.object({
		transplantable: fields.transplantableField.optional()
	})
	.describe('The origin refers to the method used to create plants.');
export type OriginUpdateCommand = z.infer<typeof OriginUpdateCommandSchema>;
