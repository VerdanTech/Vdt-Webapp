import { z } from 'jazz-tools';

/** Schema. */
export const FrostDatesProfileSchema = z.object({
	lastFrostDate: z
		.optional(z.date())
		.describe(
			'The date within the environment when the last frost of the year is expected to occur.'
		),
	firstFrostDate: z
		.optional(z.date())
		.describe(
			'The date within the environment when the first frost of the year is expected to occur.'
		)
});
