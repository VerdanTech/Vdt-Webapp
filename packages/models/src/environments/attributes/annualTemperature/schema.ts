import { z } from 'jazz-tools';

/** Schema. */
export const AnnualTemperatureProfileSchema = z.object({
	minimum: z
		.optional(z.number())
		.describe(
			'The minimum temperature that is expected to occur within a year in the environment.'
		),
	maximum: z
		.optional(z.number())
		.describe(
			'The maximum temperature that is expected to occur within a year in the environment.'
		)
});
