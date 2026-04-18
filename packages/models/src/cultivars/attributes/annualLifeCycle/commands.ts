import { z } from 'zod';

import fields from './fields.js';

/** Update command. */
export const AnnualLifecycleUpdateCommandSchema = z
	.object({
		sowToGerm: fields.sowToGermField.optional(),
		germToTransplant: fields.germToTransplantField.optional(),
		germToFirstHarvest: fields.germToFirstHarvestField.optional(),
		firstToLastHarvest: fields.firstToLastHarvestField.optional()
	})
	.describe(
		'The annual lifecycle defines the length of the stages of life for annual plants.'
	);
export type AnnualLifecycleUpdateCommand = z.infer<
	typeof AnnualLifecycleUpdateCommandSchema
>;
