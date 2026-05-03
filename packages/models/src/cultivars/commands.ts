import { z } from 'zod';

import { commonFields } from '../commands.js';
import { attributesSchemas } from './attributes/index.js';
import { CultivarCollectionVisibilityEnumOptions } from './schema.js';

/** Field specifications. */
const cultivarNameSchema = z
	.string()
	.trim()
	.min(3, 'Must be at least 3 characters.')
	.max(30, 'May be at most 30 characters.')
	.regex(
		/^[0-9A-Za-z _-]+$/,
		'Must contain only letters, numbers, spaces, hyphens, and underscores.'
	)
	.describe('A common name of this plant species.');
const cultivarNamesSchema = z
	.array(cultivarNameSchema)
	.min(1, 'Must contain at least 1 name.')
	.max(10, 'May contain at most 10 names.')
	.describe('A set of common names associated with this plant species.');
const cultivarAbbreviationSchema = z
	.string()
	.trim()
	.min(1, 'Must be at least 1 character.')
	.max(6, 'May be at most 6 characters.')
	.regex(/^[0-9A-Za-z]+$/, 'Must contain only alphanumeric characters.')
	.describe('A very short abbreviation for this plant species.');

const cultivarScientificNameSchema = z
	.string()
	.trim()
	.max(60, 'May be at most 60 characters.')
	.describe('The scientific name of this plant species.');

const cultivarDescriptionSchema = commonFields.descriptionSchema.describe(
	'Optional description.'
);

const cultivarCollectionNameSchema = commonFields.descriptionSchema.describe(
	'The name of the collection.'
);

const cultivarCollectionDescriptionSchema = commonFields.descriptionSchema.describe(
	'Optional description.'
);

const cultivarCollectionVisibilitySchema = z
	.enum(CultivarCollectionVisibilityEnumOptions)
	.describe(
		'Public collections may be viewed by anyone and are publicly searchable. \
            Unlisted collections may be viewed by anyone with the link. \
            Private collections may only be accessed by the creator or members of the associated garden.'
	);

const cultivarCollectionTagSchema = z
	.string()
	.trim()
	.max(150, 'Must be at most 150 characters.')
	.regex(/^[0-9A-Za-z ]+$/, 'Must contain only alphanumeric characters and spaces.')
	.describe('A metadata tag.');

const cultivarCollectionTagsSchema = z
	.array(cultivarCollectionTagSchema)
	.max(150, 'Must contain at most 150 tags.')
	.describe('A set of metadata tags.');
export const cultivarFields = {
	cultivarNameSchema,
	cultivarNamesSchema,
	cultivarAbbreviationSchema,
	cultivarScientificNameSchema,
	cultivarDescriptionSchema,
	cultivarCollectionNameSchema,
	cultivarCollectionDescriptionSchema,
	cultivarCollectionVisibilitySchema,
	cultivarCollectionTagSchema,
	cultivarCollectionTagsSchema,
	...attributesSchemas
};

/**
 * Command to create a new cultivar.
 */
export const CultivarCreateCommand = z.object({
	collectionId: z.string(),
	names: cultivarNamesSchema,
	abbreviation: cultivarAbbreviationSchema,
	scientificName: cultivarScientificNameSchema.optional(),
	description: cultivarDescriptionSchema.default(''),
	parentId: z.string().optional()
});

/**
 * Command to create a new cultivar collection.
 */
export const CultivarCollectionCreateCommand = z
	.object({
		name: cultivarCollectionNameSchema,
		visibility: cultivarCollectionVisibilitySchema.default('HIDDEN'),
		description: cultivarCollectionDescriptionSchema.default(''),
		tags: cultivarCollectionTagsSchema.default([]),
		parentId: z.string().optional(),
		gardenId: z.string().optional(),
		userId: z.string().optional()
	})
	.refine((data) => data.gardenId && data.parentId, {
		message: 'A cultivar collection must be connected to a garden or a user..',
		path: ['gardenId', 'userId']
	});
