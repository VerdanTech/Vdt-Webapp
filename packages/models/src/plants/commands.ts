import z, { string } from 'zod';

import { commonFields } from '../commands.js';
import { CultivarAttributesUpdateCommandSchema } from '../cultivars/attributes/index.js';
import {
	GeometryHistoryCreateCommandSchema,
	LocationHistoryCreateCommandSchema
} from '../workspaces/commands.js';
import { HarvestQualityEnumOptions, OriginEnumOptions } from './schema.js';

/** Field specifications. */

/** Harvests. */
const harvestDateSchema = z.date();
const harvestMassSchema = z.number();
const harvestUnitsSchema = z.number();
const harvestQualitySchema = z.enum(HarvestQualityEnumOptions);
const harvestDescriptionSchema = z.string();

/** Lifespans. */
const lifespanOriginSchema = z.enum(OriginEnumOptions).describe(
	'The origin stores how the plant was created. \
        Options are: directSeed: A seed is sown directly \
        into the area it will reach maturity in. \
        seedToTransplant: A seed is sown in one area and \
        then transplanted into the area it will reach maturity cin. \
        seedlingToTransplant: A seedling is transplanted directly \
        into the area it will reach maturity in.'
);
const LifespanDateSchema = z.date();

/** Plants. */
const plantCultivarNameSchema = z.string();
const plantCultivarAttributesSchema = CultivarAttributesUpdateCommandSchema;
const plantAggregateSchema = z
	.boolean()
	.describe(
		'If true, this plant entity represents multiple distinct plants which are managed as one.'
	);

/** PlantGroups. */
export const plantFields = {
	harvestDateSchema,
	harvestMassSchema,
	harvestUnitsSchema,
	harvestQualitySchema,
	harvestDescriptionSchema,
	lifespanOriginSchema,
	LifespanDateSchema,
	plantCultivarNameSchema,
	plantCultivarAttributesSchema,
	plantAggregateSchema
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
	aggregate: plantAggregateSchema.default(false)
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
