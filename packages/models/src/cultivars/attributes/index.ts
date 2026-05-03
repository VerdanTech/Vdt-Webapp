import { z } from 'zod';

import * as AnnualLifeCycle from './annualLifeCycle/index.js';
import * as Color from './color/index.js';
import * as FrostDatePlantingWindows from './frostDatePlantingWindows/index.js';
import * as ExpectedGeometry from './geometry/index.js';
import * as Origin from './origin/index.js';

export const attributesSchemas = {
	...AnnualLifeCycle.fields,
	...Color,
	...FrostDatePlantingWindows.fields,
	...ExpectedGeometry.fields,
	...Origin.fields
};

export const CultivarAttributesUpdateCommandSchema = z
	.object({
		annualLifeCycle: AnnualLifeCycle.AnnualLifecycleUpdateCommandSchema.optional(),
		color: Color.ColorUpdateCommandSchema.optional(),
		frostDatePlantingWindows:
			FrostDatePlantingWindows.FrostDatePlantingWindowsUpdateCommandSchema.optional(),
		expectedGeometry: ExpectedGeometry.ExpectedGeometryUpdateCommandSchema.optional(),
		origin: Origin.OriginUpdateCommandSchema.optional()
	})
	.describe('Contains all cultivar attributes');
export type CultivarAttributesUpdateCommand = z.infer<
	typeof CultivarAttributesUpdateCommandSchema
>;
