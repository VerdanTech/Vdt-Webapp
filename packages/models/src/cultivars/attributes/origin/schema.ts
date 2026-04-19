import { z } from 'jazz-tools';

/** Schema. */
export const OriginProfileSchema = z.object({
	transplantable: z.optional(z.boolean()).describe(
		"Defines whether a plant may be started as a seed in one location and transplanted to another. \
			Some plants, such as carrots, don't tolerate transplants, and so must be started directly."
	)
});
