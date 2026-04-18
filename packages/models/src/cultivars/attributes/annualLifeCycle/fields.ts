import z from 'zod';

/** Field specifications for annual lifecycle cultivar attribute commands. */
const annualLifeCycleFields = {
	sowToGermField: z
		.number()
		.min(0, 'May not be negative.')
		.describe('The expected amount of days from starting a seed to its germination.'),
	germToTransplantField: z.number().min(0, 'May not be negative.').describe(
		'The expected amount of days from the germination of a seed to when it will be ready for transplant. \
            For cultivars which are not able to be transplanted, this value is unused.'
	),
	germToFirstHarvestField: z
		.number()
		.min(0, 'May not be negative.')
		.describe(
			'The expected amount of days the germination of a seed to when it will be ready for a harvest.'
		),
	firstToLastHarvestField: z.number().min(0, 'May not be negative.').describe(
		'The expected amount of days the first and last harvest of a plant. \
            For plants which only have one harvest, this value is zero.'
	)
};
export default annualLifeCycleFields;
