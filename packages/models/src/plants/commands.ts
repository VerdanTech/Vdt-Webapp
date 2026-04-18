import z from 'zod';

import { CultivarAttributesUpdateCommandSchema } from '../cultivars/attributes/index.js';
import {
	GeometryHistoryCreateCommandSchema,
	LocationHistoryCreateCommandSchema
} from '../workspaces/commands.js';
import fields from './fields.js';

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
	cultivarName: fields.plantCultivarNameField.default('undefined'),
	origin: fields.lifespanOriginField.default('DIRECT_SEED'),
	locationHistory: LocationHistoryCreateCommandSchema.default({
		gardenId: '',
		locations: []
	}),
	geometryHistory: GeometryHistoryCreateCommandSchema.default({
		gardenId: '',
		geometries: []
	}),
	cultivarOverride: CultivarAttributesUpdateCommandSchema,
	quantity: fields.plantQuantityField
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
	cultivarName: fields.plantCultivarNameField.optional(),
	quantity: fields.plantQuantityField.optional()
});
export type PlantUpdateCommand = z.infer<typeof PlantUpdateCommandSchema>;

/**
 * Updates a lifespan.
 */
export const LifespanUpdateCommandSchema = z.object({
	origin: fields.lifespanOriginField.optional()
});
export type LifespanUpdateCommand = z.infer<typeof LifespanUpdateCommandSchema>;
