import { z, Account, Group } from 'jazz-tools';

import fields from './fields.js';
import { GardenSchema, defaultGardenContextInit, type Garden } from './schema.js';
import { getGlobalIndex } from '../index/utils.js';
import { AppError, zodErrorToAppErrors } from '../errors.js';

/**
 * Command to create a new garden.
 */
export const GardenCreateCommandSchema = z.object({
	id: fields.gardenIdField,
	name: fields.gardenNameField,
	description: fields.gardenDescriptionField,
	visibility: fields.gardenVisibilityField,
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
 * Creates a new garden with a unique key, per-garden group, and registers it in the global index.
 * @param command The validated garden creation command.
 * @param me The account of the user creating the garden.
 */
export async function gardenCreate(
	command: GardenCreateCommand,
	me: Account
): Promise<Garden> {
	const validated = GardenCreateCommandSchema.safeParse(command);
	if (!validated.success) {
		throw new AppError('Invalid garden command.', zodErrorToAppErrors(validated.error));
	}
	const data = validated.data;

	/** Check for duplicate garden ID in the global index. */
	const index = await getGlobalIndex();
	if (index.gardens[data.id]) {
		throw new AppError('Garden ID already exists.', {
			fieldErrors: { id: ['Key already exists.'] }
		});
	}

	/**
	 * Create a per-garden group. The creator is automatically an admin.
	 * Public and unlisted gardens may be viewed by anyone.
	 */
	const gardenGroup = Group.create(me);
	if (data.visibility === 'PUBLIC' || data.visibility === 'UNLISTED') {
		gardenGroup.makePublic();
	}

	/**
	 * Create the garden. Nested CoValues (context lists, memberships) are
	 * initialized inline — Jazz creates them with gardenGroup as owner.
	 */
	const settled = await GardenSchema.getOrCreateUnique({
		unique: data.id,
		owner: gardenGroup,
		value: {
			id: data.id,
			name: data.name,
			description: data.description,
			visibility: data.visibility,
			context: defaultGardenContextInit,
			memberships: [
				{
					user: me,
					role: 'ADMIN',
					status: 'ACCEPTED',
					acceptedAt: new Date(),
					favorite: false
				}
			]
		}
	});

	if (!settled.$isLoaded) {
		throw new AppError('Failed to create garden.');
	}

	/** TODO: Add a write via RPC to the garden index. Warn if offline and the garden is public, the garden will not be publicly searchable. */

	return settled;
}


/**
 * Command to invite a user to a garden.
 */
export const GardenMembershipCreateCommandSchema = z.object({
	gardenId: z.string(),
	adminInvites: fields.usernameInvitesListField
		.describe(
			'A list of usernames to invite as admins. A maximum of 10 users can be invited at once.'
		),
	editorInvites: fields.usernameInvitesListField
		.describe(
			'A list of usernames to invite as editors. A maximum of 10 users can be invited at once.'
		),
	viewerInvites: fields.usernameInvitesListField
		.describe(
			'A list of usernames to invite as viewers. A maximum of 10 users can be invited at once.'
		),
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
