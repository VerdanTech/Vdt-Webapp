import { z } from 'jazz-tools';

import * as AnnualLifeCycle from './annualLifeCycle/index.js';
import * as Color from './color/index.js';
import * as FrostDatePlantingWindows from './frostDatePlantingWindows/index.js';
import * as ExpectedGeometry from './geometry/index.js';
import * as Origin from './origin/index.js';

export const CultivarAttributesSchema = z.object({
	annualLifeCycle: z.optional(AnnualLifeCycle.AnnualLifeCycleProfileSchema),
	color: z.optional(Color.ColorProfileSchema),
	frostDatePlantingWindows: z.optional(
		FrostDatePlantingWindows.FrostDatePlantingWindowsProfileSchema
	),
	expectedGeometry: z.optional(ExpectedGeometry.ExpectedGeometryProfileSchema),
	origin: z.optional(Origin.OriginProfileSchema)
});
