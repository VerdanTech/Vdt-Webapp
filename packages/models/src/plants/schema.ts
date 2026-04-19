import { commonFields } from '../commands.js';
import { co, z } from 'jazz-tools';

import fields, {OriginEnumOptions} from './fields.js'
import { ObjectHistorySchema } from '../workspaces/schema.js';

import { PlantObservationSchema } from './observations.js';
import { CultivarAttributesSchema } from '../cultivars/attributes/index.js';

export const LifespanSchema = co.map({
	origin: fields.lifespanOriginField,
	history: ObjectHistorySchema,
	observations: co.list(PlantObservationSchema)
})


export const PlantSchema = co.map({
	cultivarName: z.string(),
	cultivarAttributes: CultivarAttributesSchema,
	expectedLifespan: LifespanSchema,
	recordedLifespan: LifespanSchema,
	quantity: fields.plantQuantityField
})

export const PlantGroupSchema = co.map({
	name: commonFields.nameSchema,
	description: co.plainText(),
	plants: co.list(PlantSchema)
})


export type Origin = (typeof OriginEnumOptions)[number];
export type Lifespan = co.loaded<typeof LifespanSchema>
export type Plant = co.loaded<typeof PlantSchema>
export type PlantGroup = co.loaded<typeof PlantGroupSchema>

