import { z } from 'zod';

import fields from './fields.js';

/** Update command. */
export const FrostDatesUpdateCommandSchema = z
	.object({
		lastFrostDate: fields.lastFrostDateField.optional(),
		firstFrostDate: fields.firstFrostDateField.optional()
	})
	.describe(
		'Defines when the first and last frost are expected to occur within a year.'
	);
export type FrostDatesUpdateCommand = z.infer<typeof FrostDatesUpdateCommandSchema>;
