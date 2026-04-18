import z from 'zod';

import { CultivarAttributesUpdateCommandSchema } from '../cultivars/attributes/index.js';
import { OriginEnumOptions } from './schema.js';

/** Field specifications for plant domain commands. */
const plantFields = {
	lifespanOriginField: z.enum(OriginEnumOptions).describe(
		'The origin stores how the plant was created. \
        Options are: directSeed: A seed is sown directly \
        into the area it will reach maturity in. \
        seedToTransplant: A seed is sown in one area and \
        then transplanted into the area it will reach maturity in. \
        seedlingToTransplant: A seedling is transplanted directly \
        into the area it will reach maturity in.'
	),
	lifespanDateField: z.date(),
	lifespanDatesField: z.object({
		seedDate: z.date().describe('The date at which the plant is seeded.'),
		germDate: z.date().describe('The date at which the seed germinated.'),
		expiryDate: z
			.date()
			.describe('The date at which the plant is removed from the space.'),
		dormancyDates: z.array(z.date()).describe(''),
		growthDates: z.array(z.date()).describe('')
	}),
	plantCultivarNameField: z.string(),
	plantCultivarAttributesField: CultivarAttributesUpdateCommandSchema,
	plantQuantityField: z
		.number()
		.describe('The number of distinct plants this plant entity represents.')
		.default(1)
};
export default plantFields;
