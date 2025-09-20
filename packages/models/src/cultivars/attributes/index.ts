import { Schema as S } from '@triplit/client';
import { z } from 'zod';

import * as AnnualLifeCycle from './annualLifeCycle/index.js';
import * as FrostDatePlantingWindows from './frostDatePlantingWindows/index.js';
import * as Origin from './origin/index.js';

export const attributesSchemas = {
	...AnnualLifeCycle.fields,
	...FrostDatePlantingWindows.fields,
	...Origin.fields
};

export const CultivarAttributes = S.Record({
	annualLifeCycle: S.Optional(AnnualLifeCycle.AnnualLifeCycleProfile),
	frostDatePlantingWindows: S.Optional(
		FrostDatePlantingWindows.FrostDatePlantingWindowsProfile
	),
	origin: S.Optional(Origin.OriginProfile)
});

export const CultivarAttributesUpdateCommandSchema = z.object({
	annualLifeCycle: AnnualLifeCycle.AnnualLifecycleUpdateCommandSchema.optional(),
	frostDatePlantingWindows:
		FrostDatePlantingWindows.FrostDatePlantingWindowsUpdateCommandSchema.optional(),
	origin: Origin.OriginUpdateCommandSchema.optional()
});
export type CultivarAttributesUpdateCommand = z.infer<
	typeof CultivarAttributesUpdateCommandSchema
>;
