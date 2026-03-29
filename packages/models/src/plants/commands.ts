import z, { string } from 'zod';

import { commonFields } from '../commands.js';
import { CultivarAttributesUpdateCommandSchema } from '../cultivars/attributes/index.js';
import { cultivarFields } from '../cultivars/commands.js';
import {
	GeometryHistoryCreateCommandSchema,
	LocationHistoryCreateCommandSchema
} from '../workspaces/commands.js';
import { OriginEnumOptions } from './schema.js';

/** Field specifications. */

/** Lifespans. */
const lifespanOriginSchema = z.enum(OriginEnumOptions).describe(
	'The origin stores how the plant was created. \
        Options are: directSeed: A seed is sown directly \
        into the area it will reach maturity in. \
        seedToTransplant: A seed is sown in one area and \
        then transplanted into the area it will reach maturity in. \
        seedlingToTransplant: A seedling is transplanted directly \
        into the area it will reach maturity in.'
);
const lifespanDateSchema = z.date();
const lifespanDatesSchema = z.object({
	seedDate: lifespanDateSchema.describe('The date at which the plant is seeded.'),
	germDate: lifespanDateSchema.describe('The date at which the seed germinated.'),
	expiryDate: lifespanDateSchema.describe(
		'The date at which the plant is removed from the space.'
	),
	dormancyDates: z.array(lifespanDateSchema).describe(''),
	growthDates: z.array(lifespanDateSchema).describe('')
});

/** Plants. */
const plantCultivarNameSchema = z.string();
const plantCultivarAttributesSchema = CultivarAttributesUpdateCommandSchema;
const plantQuantitySchema = z
	.number()
	.describe('The number of distinct plants this plant entity represents.')
	.default(1);

/** PlantGroups. */
export const plantFields = {
	lifespanOriginSchema,
	lifespanDateSchema,
	lifespanDatesSchema,
	plantCultivarNameSchema,
	plantCultivarAttributesSchema,
	plantQuantitySchema
};

/** Commands. */
export const PlantsCreateFormModeOptions = [
	'SINGLE',
	'GROUP',
	'PATTERN',
	'COMBINED'
] as const;
export type PlantsCreateFormMode = (typeof PlantsCreateFormModeOptions)[number];

/**
 * Adds a plant to the model.
 */
export const plantsCreateCommandSinglePlantSchema = z.object({
	cultivarName: plantCultivarNameSchema.default('undefined'),
	origin: lifespanOriginSchema.default('DIRECT_SEED'),
	locationHistory: LocationHistoryCreateCommandSchema.default({
		gardenId: '',
		locations: []
	}),
	geometryHistory: GeometryHistoryCreateCommandSchema.default({
		gardenId: '',
		geometries: []
	}),
	cultivarOverride: CultivarAttributesUpdateCommandSchema,
	quantity: plantQuantitySchema
});

export const plantsCreateFormModeSchema = z
	.enum(PlantsCreateFormModeOptions)
	.default('SINGLE');
export const PlantsCreateCommandSchema = z.object({
	gardenId: z.string(),
	mode: plantsCreateFormModeSchema.default('SINGLE'),
	plants: z.array(plantsCreateCommandSinglePlantSchema)
});
export type PlantsCreateCommand = z.infer<typeof PlantsCreateCommandSchema>;

/**
 * Updates a plant.
 */
export const PlantUpdateCommandSchema = z.object({
	cultivarName: cultivarFields.cultivarNameSchema.optional(),
	quantity: plantQuantitySchema.optional()
});
export type PlantUpdateCommand = z.infer<typeof PlantUpdateCommandSchema>;

/**
 * Updates a lifespan.
 */
export const LifespanUpdateCommandSchema = z.object({
	origin: lifespanOriginSchema.optional()
});
export type LifespanUpdateCommand = z.infer<typeof LifespanUpdateCommandSchema>;
