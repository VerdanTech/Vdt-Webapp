import z from 'zod';

import { commonFields } from '../commands.js';
import { EnvironmentParentTypeEnumOptions } from './schema.js';

/** Field specifications for environment domain commands. */
const environmentFields = {
	environmentNameField: commonFields.nameSchema.describe(
		'Name of the environment. Must be unique.'
	),
	environmentDescriptionField: commonFields.descriptionSchema.describe(
		'Optional description.'
	),
	environmentParentTypeField: z.enum(EnvironmentParentTypeEnumOptions)
};
export default environmentFields;
