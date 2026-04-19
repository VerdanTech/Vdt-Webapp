import { z } from 'jazz-tools';

/** Schema. */
export const AnnualLifeCycleProfileSchema = z.object({
	sowToGerm: z
		.optional(z.number().min(0, 'May not be negative.'))
		.describe('The expected amount of days from starting a seed to its germination.'),
	germToTransplant: z
		.optional(z.number().min(0, 'May not be negative.'))
		.describe(
			'The expected amount of days from the germination of a seed to when it will be ready for transplant. \
				For cultivars which are not able to be transplanted, this value is unused.'
		),
	germToFirstHarvest: z
		.optional(z.number().min(0, 'May not be negative.'))
		.describe(
			'The expected amount of days the germination of a seed to when it will be ready for a harvest.'
		),
	firstToLastHarvest: z
		.optional(z.number().min(0, 'May not be negative.'))
		.describe(
			'The expected amount of days the first and last harvest of a plant. \
				For plants which only have one harvest, this value is zero.'
		)
});
