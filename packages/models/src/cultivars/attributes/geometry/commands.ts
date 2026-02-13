import { z } from 'zod';

import { workspaceFields } from '../../../workspaces/index.js';

/** Field specifications. */
const peakSizeSchema = z.number().min(0, 'May not be negative.').describe(
	"The size of the plant's geometry at its highest point in meters.\
	For annuals, this is assumed to be between the first and last harvest.\
	For perennials, this is assumed to be between the between the first and last harves\
	and the exit and enter dormancy dates.\
	For ellipses, this is assumed to be the diameter.\
	For rectangles, this is assumed to be a width, forming a square.\
	For polygons, this is assumed to be the radius, forming a square.\
	For lines, this is assumed to be a width, forming a square."
);
const seedlingScaleFactorSchema = z
	.number()
	.min(0, 'May not be negative.')
	.describe('The scale factor applied to the peak size at the seedling stage.');
const firstHarvestScaleFactorSchema = z
	.number()
	.min(0, 'May not be negative.')
	.describe(
		'The scale factor applied to the peak size at the beginning harvest stage.'
	);
const lastHarvestScaleFactorSchema = z
	.number()
	.min(0, 'May not be negative.')
	.describe(
		'The scale factor applied to the peak size at the end of the harvest stage.'
	);
const expiryScaleFactorSchema = z
	.number()
	.min(0, 'May not be negative.')
	.describe('The scale factor applied to the peak size at the expiry point.');
const exitDormancyScaleFactorSchema = z
	.number()
	.min(0, 'May not be negative.')
	.describe(
		'The scale factor applied to the peak size of the perennial plant at the exit dormancy enter.'
	);
const enterDormancyScaleFactorSchema = z
	.number()
	.min(0, 'May not be negative.')
	.describe(
		'The scale factor applied to the peak size at the enter dormancy point stage.'
	);

export const fields = {
	peakSizeSchema,
	seedlingScaleFactorSchema,
	firstHarvestScaleFactorSchema,
	lastHarvestScaleFactorSchema,
	expiryScaleFactorSchema,
	exitDormancyScaleFactorSchema,
	enterDormancyScaleFactorSchema
};

/** Update command. */
export const ExpectedGeometryUpdateCommandSchema = z
	.object({
		geometryType: workspaceFields.geometryTypeSchema,
		peakSize: peakSizeSchema,
		seedlingScaleFactor: seedlingScaleFactorSchema,
		firstHarvestScaleFactor: firstHarvestScaleFactorSchema,
		lastHarvestScaleFactor: lastHarvestScaleFactorSchema,
		expiryScaleFactor: expiryScaleFactorSchema,
		exitDormancyScaleFactor: exitDormancyScaleFactorSchema,
		enterDormancyScaleFactor: enterDormancyScaleFactorSchema
	})
	.describe(
		'Determines the default geometric history when defining new instances of a cultivar.'
	);
export type ExpectedGeometryUpdateCommand = z.infer<
	typeof ExpectedGeometryUpdateCommandSchema
>;
