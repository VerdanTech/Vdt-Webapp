import { z } from 'jazz-tools';

import { commonFields } from '../commands.js';

/**
 * Defines the parent entity that the environment describes characteristics for.
 * - GARDEN: the environment applies to a garden.
 * - WORKSPACE: the environment applies to a workspace.
 * - PLANTING_AREA: the environment applies to a planting area.
 * - INDEPENDENT: the environment applies to an independent geometry.
 */
export const EnvironmentParentTypeEnumOptions = [
	'GARDEN',
	'WORKSPACE',
	'PLANTING_AREA',
	'INDEPENDENT'
] as const;

/** Field specifications for environment domain commands. */
const environmentFields = {
	environmentNameField: commonFields.nameSchema.describe(
		'Name of the environment. Must be unique.'
	),
	environmentDescriptionField: commonFields.descriptionSchema.describe(
		'Optional description.'
	),
	environmentParentTypeField: z.literal(EnvironmentParentTypeEnumOptions)
};
export default environmentFields;
