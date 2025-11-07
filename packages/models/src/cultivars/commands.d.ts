import { z } from 'zod';

export declare const cultivarFields: {
	transplantableSchema: z.ZodBoolean;
	lastFrostWindowOpenSchema: z.ZodNumber;
	lastFrostWindowCloseSchema: z.ZodNumber;
	firstFrostWindowOpenSchema: z.ZodNumber;
	firstFrostWindowCloseSchema: z.ZodNumber;
	sowToGermSchema: z.ZodNumber;
	germToTransplantSchema: z.ZodNumber;
	germToFirstHarvestSchema: z.ZodNumber;
	firstToLastHarvestSchema: z.ZodNumber;
	cultivarNameSchema: z.ZodString;
	cultivarNamesSchema: z.ZodArray<z.ZodString, 'many'>;
	cultivarAbbreviationSchema: z.ZodString;
	cultivarScientificNameSchema: z.ZodString;
	cultivarDescriptionSchema: z.ZodString;
	cultivarCollectionNameSchema: z.ZodString;
	cultivarCollectionDescriptionSchema: z.ZodString;
	cultivarCollectionVisibilitySchema: z.ZodEnum<['HIDDEN', 'UNLISTED', 'PUBLIC']>;
	cultivarCollectionTagSchema: z.ZodString;
	cultivarCollectionTagsSchema: z.ZodArray<z.ZodString, 'many'>;
};
/**
 * Command to create a new cultivar.
 */
export declare const CultivarCreateCommand: z.ZodObject<
	{
		collectionId: z.ZodString;
		names: z.ZodArray<z.ZodString, 'many'>;
		abbreviation: z.ZodString;
		scientificName: z.ZodOptional<z.ZodString>;
		description: z.ZodDefault<z.ZodString>;
		parentId: z.ZodOptional<z.ZodString>;
	},
	'strip',
	z.ZodTypeAny,
	{
		description: string;
		collectionId: string;
		names: string[];
		abbreviation: string;
		parentId?: string | undefined;
		scientificName?: string | undefined;
	},
	{
		collectionId: string;
		names: string[];
		abbreviation: string;
		description?: string | undefined;
		parentId?: string | undefined;
		scientificName?: string | undefined;
	}
>;
/**
 * Command to create a new cultivar collection.
 */
export declare const CultivarCollectionCreateCommand: z.ZodEffects<
	z.ZodObject<
		{
			name: z.ZodString;
			visibility: z.ZodDefault<z.ZodEnum<['HIDDEN', 'UNLISTED', 'PUBLIC']>>;
			description: z.ZodDefault<z.ZodString>;
			tags: z.ZodDefault<z.ZodArray<z.ZodString, 'many'>>;
			parentId: z.ZodOptional<z.ZodString>;
			gardenId: z.ZodOptional<z.ZodString>;
			userId: z.ZodOptional<z.ZodString>;
		},
		'strip',
		z.ZodTypeAny,
		{
			name: string;
			description: string;
			tags: string[];
			visibility: 'HIDDEN' | 'UNLISTED' | 'PUBLIC';
			gardenId?: string | undefined;
			userId?: string | undefined;
			parentId?: string | undefined;
		},
		{
			name: string;
			gardenId?: string | undefined;
			description?: string | undefined;
			tags?: string[] | undefined;
			visibility?: 'HIDDEN' | 'UNLISTED' | 'PUBLIC' | undefined;
			userId?: string | undefined;
			parentId?: string | undefined;
		}
	>,
	{
		name: string;
		description: string;
		tags: string[];
		visibility: 'HIDDEN' | 'UNLISTED' | 'PUBLIC';
		gardenId?: string | undefined;
		userId?: string | undefined;
		parentId?: string | undefined;
	},
	{
		name: string;
		gardenId?: string | undefined;
		description?: string | undefined;
		tags?: string[] | undefined;
		visibility?: 'HIDDEN' | 'UNLISTED' | 'PUBLIC' | undefined;
		userId?: string | undefined;
		parentId?: string | undefined;
	}
>;
//# sourceMappingURL=commands.d.ts.map
