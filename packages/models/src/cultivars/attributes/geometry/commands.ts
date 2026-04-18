import { z } from 'zod';

import workspaceFields from '../../../workspaces/fields.js';
import fields from './fields.js';

/** Update command. */
export const ExpectedGeometryUpdateCommandSchema = z
	.object({
		geometryType: workspaceFields.geometryTypeField,
		peakSize: fields.peakSizeField,
		seedlingScaleFactor: fields.seedlingScaleFactorField,
		firstHarvestScaleFactor: fields.firstHarvestScaleFactorField,
		lastHarvestScaleFactor: fields.lastHarvestScaleFactorField,
		expiryScaleFactor: fields.expiryScaleFactorField,
		exitDormancyScaleFactor: fields.exitDormancyScaleFactorField,
		enterDormancyScaleFactor: fields.enterDormancyScaleFactorField
	})
	.describe(
		'Determines the default geometric history when defining new instances of a cultivar.'
	);
export type ExpectedGeometryUpdateCommand = z.infer<
	typeof ExpectedGeometryUpdateCommandSchema
>;
