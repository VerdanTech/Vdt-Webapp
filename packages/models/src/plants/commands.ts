import z from 'zod';

import { commonFields } from '../commands.js';
import { CultivarAttributesUpdateCommandSchema } from '../cultivars/attributes/index.js';
import {
	GeometryHistoryCreateCommandSchema,
	LocationHistoryCreateCommandSchema
} from '../workspaces/commands.js';
import { HarvestQualityEnumOptions, OriginEnumOptions } from './schema.js';

/** Field specifications. */

/** Harvests. */
const harvestDateSchema = z.date()
const harvestMassSchema = z.number()
const harvestUnitsSchema = z.number()
const harvestQualitySchema = z.enum(HarvestQualityEnumOptions)
const harvestDescriptionSchema = z.string()

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
const LifespanDateSchema = z.date()

/** Plants. */
const plantCultivarNameSchema = z.string()
const plantCultivarAttributesSchema = CultivarAttributesUpdateCommandSchema
const plantAggregateSchema = z
	.boolean()
	.describe(
		'If true, this plant entity represents multiple distinct plants which are managed as one.'
	);

/** PlantGroups. */
export const plantFields = {
	harvestDateSchema, harvestMassSchema, harvestUnitsSchema, harvestQualitySchema, harvestDescriptionSchema, lifespanOriginSchema, 
	LifespanDateSchema, plantCultivarNameSchema, plantCultivarAttributesSchema, plantAggregateSchema
}

/** Commands. */
export const PlantsCreateFormModeOptions = ['SINGLE', 'GROUP', 'PATTERN', 'COMBINED'] as const;
export type PlantsCreateFormMode = (typeof PlantsCreateFormModeOptions)[number]

/**
 * Adds a plant to the model.
 */
const PlantsCreateCommandSinglePlant = z.object({
	cultivarName: z.string(),
	origin: lifespanOriginSchema,
	locationHistory: LocationHistoryCreateCommandSchema,
	geometryHistory: GeometryHistoryCreateCommandSchema,
	cultivarOverride: CultivarAttributesUpdateCommandSchema,
	aggregate: plantAggregateSchema
});

export const plantsCreateFormModeSchema = z.enum(PlantsCreateFormModeOptions)
export const PlantsCreateCommandSchema = z.object({
	gardenId: z.string(),
	mode: plantsCreateFormModeSchema,
	plants: z.array(PlantsCreateCommandSinglePlant)
});
export type PlantsCreateCommand = z.infer<typeof PlantsCreateCommandSchema>;
