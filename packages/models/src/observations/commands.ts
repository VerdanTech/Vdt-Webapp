import z, { string } from 'zod';

import { commonFields } from '../commands.js';

/** Field specifications. */

/** Observations. */
//const workspaceNameSchema = commonFields.nameSchema.describe(
//    'Name of the workspace. Must be unique within a garden.'
//);
export const observationFields = {
    
};

/** Commands. */

/**
 * Update an observation's date.
 */
export const ObservationUpdateCommandSchema = z.object({
    id: z.string(),
    entityIds: z.set(z.string()).optional(),
    date: z.date().optional(),
    data: z.record(z.string(), z.any()).optional()
})
export type ObservationUpdateCommand = z.infer<typeof ObservationUpdateCommandSchema>;