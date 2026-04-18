import { co, z } from 'jazz-tools';
import fields from './fields.js';

export const GLOBAL_COVAL_ID_PUBLIC_GARDEN_INDEX = 'global-public-gardens'

export const GardenContextSchema = co.map({});

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
	gardens: co.record(fields.gardenIdField, GardenSchema),
})

export type Garden = co.loaded<typeof GardenSchema>
export type GardenMembership = co.loaded<typeof GardenMembershipSchema>
export type GardenIndex = co.loaded<typeof GardenIndexSchema>