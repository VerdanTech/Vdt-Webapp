import { z } from 'zod';

import fields from './fields.js';

/** Update command. */
export const FrostDatePlantingWindowsUpdateCommandSchema = z
	.object({
		lastFrostWindowOpen: fields.lastFrostWindowOpenField.optional(),
		lastFrostWindowClose: fields.lastFrostWindowCloseField.optional(),
		firstFrostWindowOpen: fields.firstFrostWindowOpenField.optional(),
		firstFrostWindowClose: fields.firstFrostWindowCloseField.optional()
	})
	.describe(
		'A planting window defines a period of time within an environment that a cultivar should be planted. \
		These attributes define an allowed planting window of time relative to the first and last frost dates. \
		These planting windows are used for incdicating within the Verdagraph when plants are suggested to be planted.'
	);
export type FrostDatePlantingWindowsUpdateCommand = z.infer<
	typeof FrostDatePlantingWindowsUpdateCommandSchema
>;
