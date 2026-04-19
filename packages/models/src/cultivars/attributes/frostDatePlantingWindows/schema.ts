import { z } from 'jazz-tools';

/** Schema. */
export const FrostDatePlantingWindowsProfileSchema = z.object({
	lastFrostWindowOpen: z.optional(z.number()).describe(
		'The amount of days between the last frost and the beginning of the planting window. \
			Positive values indicate the window begins after the last frost date. \
			For example, a value of -15 indicates the cultivar may be planted 15 days before the last frost date.'
	),
	lastFrostWindowClose: z.optional(z.number()).describe(
		'The amount of days between the last frost and the end of the planting window. \
			Positive values indicate the window begins after the last frost date. \
			For example, a value of 15 indicates the cultivar must be planted before 15 days after the last frost date.'
	),
	firstFrostWindowOpen: z.optional(z.number()).describe(
		'The amount of days between the first frost and the beginning of the planting window. \
			Positive values indicate the window begins after the first frost date. \
			For example, a value of -15 indicates the cultivar may be planted 15 days before the first frost date.'
	),
	firstFrostWindowClose: z.optional(z.number()).describe(
		'The amount of days between the first frost and the end of the planting window. \
			Positive values indicate the window begins after the first frost date. \
			For example, a value of 15 indicates the cultivar must be planted before 15 days after the first frost date.'
	)
});
