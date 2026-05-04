import { z } from 'zod';

/** Field specifications. */
const lastFrostDateSchema = z
	.date()
	.describe(
		'The date within the environment when the last frost of the year is expected to occur.'
	);
const firstFrostDateSchema = z
	.date()
	.describe(
		'The date within the environment when the first frost of the year is expected to occur.'
	);
export const fields = { lastFrostDateSchema, firstFrostDateSchema };

/** Update command. */
export const FrostDatesUpdateCommandSchema = z
	.object({
		lastFrostDate: lastFrostDateSchema.optional(),
		firstFrostDate: firstFrostDateSchema.optional()
	})
	.describe(
		'Defines when the first and last frost are expected to occur within a year.'
	);
export type FrostDatesUpdateCommand = z.infer<typeof FrostDatesUpdateCommandSchema>;
export type FrostDateProfile = z.infer<typeof FrostDatesUpdateCommandSchema>;
