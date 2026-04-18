import { z } from 'zod';

import fields from './fields.js';

/** Update command. */
export const AnnualTemperatureUpdateCommandSchema = z
	.object({
		minimum: fields.minimumAnnualTempField.optional(),
		maximum: fields.maximumAnnualTempField.optional()
	})
	.describe('Defines the expected range of temperatures over a year.');
export type AnnualTemperatureUpdateCommand = z.infer<
	typeof AnnualTemperatureUpdateCommandSchema
>;
