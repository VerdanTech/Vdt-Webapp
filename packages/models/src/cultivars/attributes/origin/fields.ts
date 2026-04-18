import z from 'zod';

/** Field specifications for origin cultivar attribute commands. */
const originFields = {
	transplantableField: z.boolean().describe(
		"Defines whether a plant may be started as a seed in one location and transplanted to another. \
			Some plants, such as carrots, don't tolerate transplants, and so must be started directly."
	)
};
export default originFields;
