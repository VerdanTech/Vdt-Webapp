import { z } from 'zod';

/** Field specifications. */
const minimumAnnualTempSchema = z
	.number()
	.describe(
		'The minimum temperature that is expected to occur within a year in the environment.'
	);
const maximumAnnualTempSchema = z
	.number()
	.describe(
		'The maxmium temperature that is expected to occur within a year in the environment.'
	);
export const fields = { minimumAnnualTempSchema, maximumAnnualTempSchema };

/** Update command. */
export const AnnualTemperatureUpdateCommandSchema = z
	.object({
		minimum: minimumAnnualTempSchema.optional(),
		maximum: maximumAnnualTempSchema.optional()
	})
	.describe('Defines the expected range of temperatures over a year.');
export type AnnualTemperatureUpdateCommand = z.infer<
	typeof AnnualTemperatureUpdateCommandSchema
>;
export type AnnualTemperatureProfile = z.infer<
	typeof AnnualTemperatureUpdateCommandSchema
>;
