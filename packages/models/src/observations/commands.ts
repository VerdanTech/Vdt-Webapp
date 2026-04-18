import z from 'zod';

/** Commands. */

/**
 * Update an observation's date.
 */
export const ObservationUpdateCommandSchema = z.object({
	id: z.string(),
	entityIds: z.set(z.string()).optional(),
	date: z.date().optional(),
	data: z.record(z.string(), z.any()).optional()
});
export type ObservationUpdateCommand = z.infer<typeof ObservationUpdateCommandSchema>;
