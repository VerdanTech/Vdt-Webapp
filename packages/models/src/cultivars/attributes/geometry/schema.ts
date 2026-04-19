import { z } from 'jazz-tools';

import { GeometryTypeEnumOptions } from '../../../workspaces/schema.js';

/** Schema. */
export const ExpectedGeometryProfileSchema = z.object({
	geometryType: z
		.optional(z.literal(GeometryTypeEnumOptions))
		.describe(
			'Describes the type of geometry. Each type has a unique set of attributes associated with it.'
		),
	peakSize: z.optional(z.number().min(0, 'May not be negative.')).describe(
		"The size of the plant's geometry at its highest point in meters.\
		For annuals, this is assumed to be between the first and last harvest.\
		For perennials, this is assumed to be between the between the first and last harvest\
		and the exit and enter dormancy dates.\
		For ellipses, this is assumed to be the diameter.\
		For rectangles, this is assumed to be a width, forming a square.\
		For polygons, this is assumed to be the radius, forming a square.\
		For lines, this is assumed to be a width, forming a square."
	),
	seedlingScaleFactor: z
		.optional(z.number().min(0, 'May not be negative.'))
		.describe('The scale factor applied to the peak size at the seedling stage.'),
	firstHarvestScaleFactor: z
		.optional(z.number().min(0, 'May not be negative.'))
		.describe('The scale factor applied to the peak size at the beginning harvest stage.'),
	lastHarvestScaleFactor: z
		.optional(z.number().min(0, 'May not be negative.'))
		.describe('The scale factor applied to the peak size at the end of the harvest stage.'),
	expiryScaleFactor: z
		.optional(z.number().min(0, 'May not be negative.'))
		.describe('The scale factor applied to the peak size at the expiry point.'),
	exitDormancyScaleFactor: z
		.optional(z.number().min(0, 'May not be negative.'))
		.describe(
			'The scale factor applied to the peak size of the perennial plant at the exit dormancy point.'
		),
	enterDormancyScaleFactor: z
		.optional(z.number().min(0, 'May not be negative.'))
		.describe('The scale factor applied to the peak size at the enter dormancy point.')
});
