import { z } from 'zod';

import * as AnnualTemperature from './annualTemperature/index.js';
import * as FrostDates from './frostDates/index.js';

export const attributesSchemas = { ...FrostDates.fields, ...AnnualTemperature.fields };

export const EnvironmentAttributesUpdateCommandSchema = z.object({
	frostDates: FrostDates.FrostDatesUpdateCommandSchema.optional(),
	annualTemperature: AnnualTemperature.AnnualTemperatureUpdateCommandSchema.optional()
});
export type EnvironmentAttributesUpdateCommand = z.infer<
	typeof EnvironmentAttributesUpdateCommandSchema
>;
export type EnvironmentAttributes = z.infer<
	typeof EnvironmentAttributesUpdateCommandSchema
>;
