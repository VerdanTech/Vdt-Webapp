import z from 'zod';

/** Field specifications for frost dates environment attribute commands. */
const frostDatesFields = {
	lastFrostDateField: z
		.date()
		.describe(
			'The date within the environment when the last frost of the year is expected to occur.'
		),
	firstFrostDateField: z
		.date()
		.describe(
			'The date within the environment when the first frost of the year is expected to occur.'
		)
};
export default frostDatesFields;
