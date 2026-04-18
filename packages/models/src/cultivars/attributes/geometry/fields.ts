import z from 'zod';

/** Field specifications for geometry cultivar attribute commands. */
const geometryAttributeFields = {
	peakSizeField: z.number().min(0, 'May not be negative.').describe(
		"The size of the plant's geometry at its highest point in meters.\
		For annuals, this is assumed to be between the first and last harvest.\
		For perennials, this is assumed to be between the between the first and last harves\
		and the exit and enter dormancy dates.\
		For ellipses, this is assumed to be the diameter.\
		For rectangles, this is assumed to be a width, forming a square.\
		For polygons, this is assumed to be the radius, forming a square.\
		For lines, this is assumed to be a width, forming a square."
	),
	seedlingScaleFactorField: z
		.number()
		.min(0, 'May not be negative.')
		.describe('The scale factor applied to the peak size at the seedling stage.'),
	firstHarvestScaleFactorField: z
		.number()
		.min(0, 'May not be negative.')
		.describe(
			'The scale factor applied to the peak size at the beginning harvest stage.'
		),
	lastHarvestScaleFactorField: z
		.number()
		.min(0, 'May not be negative.')
		.describe(
			'The scale factor applied to the peak size at the end of the harvest stage.'
		),
	expiryScaleFactorField: z
		.number()
		.min(0, 'May not be negative.')
		.describe('The scale factor applied to the peak size at the expiry point.'),
	exitDormancyScaleFactorField: z
		.number()
		.min(0, 'May not be negative.')
		.describe(
			'The scale factor applied to the peak size of the perennial plant at the exit dormancy enter.'
		),
	enterDormancyScaleFactorField: z
		.number()
		.min(0, 'May not be negative.')
		.describe(
			'The scale factor applied to the peak size at the enter dormancy point stage.'
		)
};
export default geometryAttributeFields;
