import z from 'zod';

import fields from './fields.js';

/**
 * Command to create a new garden.
 */
export const GardenCreateCommandSchema = z.object({
	id: fields.gardenIdField,
	name: fields.gardenNameField,
	description: fields.gardenDescriptionField.default(''),
	visibility: fields.gardenVisibilityField.default('HIDDEN'),
	adminInvites: fields.usernameInvitesListField
		.describe(
			'A list of usernames to invite as admins. A maximum of 10 users can be invited at once.'
		)
		.default([]),
	editorInvites: fields.usernameInvitesListField
		.describe(
			'A list of usernames to invite as editors. A maximum of 10 users can be invited at once.'
		)
		.default([]),
	viewerInvites: fields.usernameInvitesListField
		.describe(
			'A list of usernames to invite as viewers. A maximum of 10 users can be invited at once.'
		)
		.default([])
});
export type GardenCreateCommand = z.infer<typeof GardenCreateCommandSchema>;

/**
 * Command to invite a user to a garden.
 */
export const GardenMembershipCreateCommandSchema = z.object({
	gardenId: z.string(),
	adminInvites: fields.usernameInvitesListField
		.describe('A list of usernames to invite as admins.')
		.default([]),
	editorInvites: fields.usernameInvitesListField
		.describe('A list of usernames to invite as editors.')
		.default([]),
	viewerInvites: fields.usernameInvitesListField
		.describe('A list of usernames to invite as viewers.')
		.default([])
});
export type GardenMembershipCreateCommand = z.infer<
	typeof GardenMembershipCreateCommandSchema
>;

/**
 * Command to accept a garden membership invite.
 */
export const GardenMembershipAcceptCommandSchema = z.object({
	gardenId: z.string()
});
export type GardenMembershipAcceptCommand = z.infer<
	typeof GardenMembershipAcceptCommandSchema
>;

/**
 * Command to leave a garden.
 */
export const GardenMembershipDeleteCommandSchema = z.object({
	gardenId: z.string()
});
export type GardenMembershipDeleteCommand = z.infer<
	typeof GardenMembershipDeleteCommandSchema
>;

/**
 * Command to revoke a user's membership.
 */
export const GardenMembershipRevokeCommandSchema = z.object({
	gardenId: z.string(),
	profileId: z.string()
});
export type GardenMembershipRevokeCommand = z.infer<
	typeof GardenMembershipRevokeCommandSchema
>;

/**
 * Command to change the role on a user's membership.
 */
export const GardenMembershipRoleChangeCommandSchema = z.object({
	gardenId: z.string(),
	profileId: z.string(),
	newRole: fields.gardenMembershipRoleField
});
export type GardenMembershipRoleChangeCommand = z.infer<
	typeof GardenMembershipRoleChangeCommandSchema
>;
