import { z } from 'zod';

import fields from './fields.js';

/**
 * Command to create a new environment.
 */
export const EnvironmentCreateCommandSchema = z.object({
	gardenId: z.string(),
	parendId: z.string(),
	parentType: fields.environmentParentTypeField.default('GARDEN'),
	name: fields.environmentNameField,
	description: fields.environmentDescriptionField.default('')
});
export type EnvironmentCreateCommand = z.infer<typeof EnvironmentCreateCommandSchema>;
