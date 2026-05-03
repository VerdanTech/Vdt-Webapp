import { z } from 'zod';

/** Field specifications. */
const transplantableSchema = z.boolean().describe(
	"Defines whether a plant may be started as a seed in one location and transplanted to another. \
		Some plants, such as carrots, don't tolerate transplants, and so must be started directly."
);
export const fields = { transplantableSchema };

/** Update command. */
export const OriginUpdateCommandSchema = z
	.object({
		transplantable: transplantableSchema.optional()
	})
	.describe('The origin refers to the method used to create plants.');
export type OriginUpdateCommand = z.infer<typeof OriginUpdateCommandSchema>;
export type OriginProfile = z.infer<typeof OriginUpdateCommandSchema>;
