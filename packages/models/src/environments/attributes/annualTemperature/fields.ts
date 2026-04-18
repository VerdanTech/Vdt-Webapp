import z from 'zod';

/** Field specifications for annual temperature environment attribute commands. */
const annualTemperatureFields = {
	minimumAnnualTempField: z
		.number()
		.describe(
			'The minimum temperature that is expected to occur within a year in the environment.'
		),
	maximumAnnualTempField: z
		.number()
		.describe(
			'The maxmium temperature that is expected to occur within a year in the environment.'
		)
};
export default annualTemperatureFields;
