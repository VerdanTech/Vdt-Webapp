import z from 'zod';

/** Field specifications for color cultivar attribute commands. */
const colorFields = {
	colorField: z.string().describe('May be a hex value')
};
export default colorFields;
