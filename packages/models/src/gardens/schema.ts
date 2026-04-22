import { co, z } from 'jazz-tools';

import fields, { GardenMembershipRoleEnumOptions } from './fields.js';
import { WorkspaceSchema } from '../workspaces/schema.js';
import { EnvironmentSchema } from '../environments/schema.js';
import { CultivarCollectionSchema } from '../cultivars/schema.js';
import { PlantSchema } from '../plants/schema.js';

/************************************
 * Garden
 ************************************/

/**
 * @title Garden Context.
 */
export const GardenContextSchema = co.map({
	workspaces: co.list(WorkspaceSchema),
	environments: co.list(EnvironmentSchema),
	cultivarCollections: co.list(CultivarCollectionSchema),
	plants: co.list(PlantSchema)
});

/** Default empty initializer for GardenContextSchema, used when creating a new garden. */
export const defaultGardenContextInit = {
	workspaces: [],
	environments: [],
	cultivarCollections: [],
	plants: []
} satisfies Parameters<typeof GardenContextSchema.create>[0];

/**
 * @title Garden Membership.
 */
export const GardenMembershipSchema = co.map({
	user: co.account(),
	role: fields.gardenMembershipRoleField,
	status: fields.gardenMembershipStatusField,
	acceptedAt: z.date(),
	favorite: z.boolean()
});

/**
 * @title Garden.
 */
export const GardenSchema = co.map({
	context: GardenContextSchema,
	id: fields.gardenIdField,
	name: z.string(),
	description: co.plainText(),
	visibility: fields.gardenVisibilityField,
	memberships: co.list(GardenMembershipSchema)
});

/************************************
 * Global Index
 ************************************/

export const GLOBAL_COVAL_ID_PUBLIC_GARDEN_INDEX = 'global-public-gardens';

/**
 * @title Garden Index.
 */
export const GardenIndexSchema = co.map({
	gardens: co.record(fields.gardenIdField, GardenSchema)
});

export type Garden = co.loaded<typeof GardenSchema>;
export type GardenWithMemberships = co.loaded<
	typeof GardenSchema,
	{ memberships: { $each: { user: true } } }
>;
export type GardenMembership = co.loaded<typeof GardenMembershipSchema>;
export type GardenIndex = co.loaded<typeof GardenIndexSchema>;
export type GardenRole = (typeof GardenMembershipRoleEnumOptions)[number];
