import { z } from 'zod';

import { CultivarAttributesUpdateCommandSchema } from './attributes/index.js';
import fields from './fields.js';

/**
 * Command to create a new cultivar.
 */
export const CultivarCreateCommand = z.object({
	collectionId: z.string(),
	names: fields.cultivarNamesField,
	abbreviation: fields.cultivarAbbreviationField,
	scientificName: fields.cultivarScientificNameField.optional(),
	description: fields.cultivarDescriptionField.default(''),
	parentId: z.string().optional()
});

/**
 * Command to create a new cultivar collection.
 */
export const CultivarCollectionCreateCommand = z
	.object({
		name: fields.cultivarCollectionNameField,
		visibility: fields.cultivarCollectionVisibilityField.default('HIDDEN'),
		description: fields.cultivarCollectionDescriptionField.default(''),
		tags: fields.cultivarCollectionTagsField.default([]),
		parentId: z.string().optional(),
		gardenId: z.string().optional(),
		userId: z.string().optional()
	})
	.refine((data) => data.gardenId && data.parentId, {
		message: 'A cultivar collection must be connected to a garden or a user.',
		path: ['gardenId', 'userId']
	});
