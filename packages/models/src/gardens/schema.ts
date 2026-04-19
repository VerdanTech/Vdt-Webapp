import { co, z } from 'jazz-tools';

import fields from './fields.js';
import { WorkspaceSchema } from '../workspaces/schema.js';
import { EnvironmentSchema } from '../environments/schema.js';
import { CultivarCollectionSchema } from '../cultivars/schema.js';
import { PlantSchema } from '../plants/schema.js';

export const GLOBAL_COVAL_ID_PUBLIC_GARDEN_INDEX = 'global-public-gardens';

export const GardenContextSchema = co.map({
	workspaces: co.list(WorkspaceSchema),
	environments: co.list(EnvironmentSchema),
	cultivarCollections: co.list(CultivarCollectionSchema),
	plants: co.list(PlantSchema)
});

export const GardenMembershipSchema = co.map({
	user: co.account(),
	role: fields.gardenMembershipRoleField,
	status: fields.gardenMembershipStatusField,
	acceptedAt: z.date(),
	favorite: z.boolean()
});

export const GardenSchema = co.map({
	context: GardenContextSchema,
	id: fields.gardenIdField,
	name: z.string(),
	description: co.plainText(),
	memberships: co.list(GardenMembershipSchema)
});

export const GardenIndexSchema = co.map({
	gardens: co.record(fields.gardenIdField, GardenSchema)
});

export type Garden = co.loaded<typeof GardenSchema>;
export type GardenMembership = co.loaded<typeof GardenMembershipSchema>;
export type GardenIndex = co.loaded<typeof GardenIndexSchema>;
