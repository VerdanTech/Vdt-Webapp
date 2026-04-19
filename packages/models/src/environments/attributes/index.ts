import { z } from 'jazz-tools';

import * as AnnualTemperature from './annualTemperature/index.js';
import * as FrostDates from './frostDates/index.js';

export const EnvironmentAttributesSchema = z.object({
	frostDates: z.optional(FrostDates.FrostDatesProfileSchema),
	annualTemperature: z.optional(AnnualTemperature.AnnualTemperatureProfileSchema)
});
