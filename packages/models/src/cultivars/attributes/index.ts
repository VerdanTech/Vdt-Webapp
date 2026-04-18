import { Schema as S } from '@triplit/client';
import { z } from 'zod';

import * as AnnualLifeCycle from './annualLifeCycle/index.js';
import * as Color from './color/index.js';
import * as FrostDatePlantingWindows from './frostDatePlantingWindows/index.js';
import * as ExpectedGeometry from './geometry/index.js';
import * as Origin from './origin/index.js';

export const CultivarAttributes = S.Record({
	annualLifeCycle: S.Optional(AnnualLifeCycle.AnnualLifeCycleProfile),
	color: S.Optional(Color.ColorProfile),
	frostDatePlantingWindows: S.Optional(
		FrostDatePlantingWindows.FrostDatePlantingWindowsProfile
	),
	expectedGeometry: S.Optional(ExpectedGeometry.ExpectedGeometryProfile),
	origin: S.Optional(Origin.OriginProfile)
});

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
