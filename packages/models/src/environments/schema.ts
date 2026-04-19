import { co, z } from 'jazz-tools';

import {
	ObjectHistorySchema,
	PlantingAreaSchema,
	WorkspaceSchema
} from '../workspaces/schema.js';
import { EnvironmentAttributesSchema } from './attributes/index.js';
import fields from './fields.js';

export const EnvironmentSchema = co.map({
	name: fields.environmentNameField,
	description: co.plainText(),
	parentType: fields.environmentParentTypeField,
	coverage: co.map({
		garden: z.boolean(),
		workspaces: co.list(WorkspaceSchema),
		plantingAreas: co.list(PlantingAreaSchema),
		history: ObjectHistorySchema
	}),
	attributes: EnvironmentAttributesSchema
});

export type EnvironmentAttributes = z.infer<typeof EnvironmentAttributesSchema>;
export type Environment = co.loaded<typeof EnvironmentSchema>;
