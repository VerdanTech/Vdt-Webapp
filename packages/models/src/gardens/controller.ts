import { type ControllerContext } from '../controller.js';
import {
	AppError,
	type Garden,
	type GardenCreateCommand,
	type GardenMembershipAcceptCommand,
	type GardenMembershipCreateCommand,
	type GardenMembershipDeleteCommand,
	type GardenMembershipRevokeCommand,
	type GardenMembershipRoleChangeCommand,
	isProfileMember
} from '../index.js';

/** Helpers. */

/**
 * Given a list of usernames, constructs an array of matching user IDs
 * that are not already members in the given garden.
 * @param usernames The usernames to retrieve user IDs for.
 * @param ctx Controller context.
 * @param garden The garden to check the users aren't already members in.
 * @returns An array of matching user IDs that aren't already members.
 *
 * TODO: Update query once Better Auth user schema is generated.
 * Currently stubs the user lookup since the users table schema comes from the Better Auth adapter.
 */
async function getNewMembershipIdsFromUsernames(
	usernames: string[] | undefined,
	ctx: ControllerContext,
	garden?: Garden
): Promise<string[]> {
	if (!usernames || usernames.length === 0) {
		return [];
	}

	/** TODO: Replace with Better Auth users table query once schema is generated. */
	const users = await ctx.db.all(
		(ctx.jazz as any).users.where({ username: { in: usernames } })
	);
	return users
		.filter((user: any) => garden === undefined || !isProfileMember(garden, user.id))
		.map((user: any) => user.id);
}

/** Commands. */

/**
 * Creates a new garden.
 */
export async function gardenCreate(
	data: GardenCreateCommand,
	ctx: ControllerContext
): Promise<Garden> {
	/** Retrieve client. */
	const client = await ctx.getClientOrError();

	/** Validate unique key constraint. */
	const existingGarden = await ctx.db.one(ctx.jazz.gardens.where({ id: data.id }));
	if (existingGarden) {
		throw new AppError('Garden ID already exists.', {
			fieldErrors: { id: ['Key already exists.'] }
		});
	}

	/** Retrieve all invitee IDs. */
	const adminInviteIds = await getNewMembershipIdsFromUsernames(data.adminInvites, ctx);
	const editorIds = await getNewMembershipIdsFromUsernames(data.editorInvites, ctx);
	const viewerIds = await getNewMembershipIdsFromUsernames(data.viewerInvites, ctx);

	/** Add creator's ID and deduplicate. */
	const adminIds = [...new Set([client.profile.id, ...adminInviteIds])];

	/** Persist to db and add memberships. */
	const tx = ctx.db.beginTransaction(ctx.jazz.gardens);

	/** Garden IDs are user-supplied slugs — cast to bypass auto-ID enforcement. */
	tx.insert(ctx.jazz.gardens, {
		id: data.id,
		name: data.name,
		visibility: data.visibility,
		description: data.description,
		creatorId: client.profile.id,
		adminIds,
		editorIds,
		viewerIds
	} as any);

	/** Add creator membership. */
	tx.insert(ctx.jazz.gardenMemberships, {
		gardenId: data.id,
		userId: client.profile.id,
		role: 'ADMIN',
		status: 'ACCEPTED'
	});

	/** Add admin memberships. */
	for (const userId of adminInviteIds) {
		if (userId === client.profile.id) continue;
		tx.insert(ctx.jazz.gardenMemberships, {
			gardenId: data.id,
			userId,
			role: 'ADMIN',
			inviterId: client.profile.id,
			status: 'CREATED'
		});
	}

	/** Add editor memberships. */
	for (const userId of editorIds) {
		tx.insert(ctx.jazz.gardenMemberships, {
			gardenId: data.id,
			userId,
			role: 'EDITOR',
			inviterId: client.profile.id,
			status: 'CREATED'
		});
	}

	/** Add viewer memberships. */
	for (const userId of viewerIds) {
		tx.insert(ctx.jazz.gardenMemberships, {
			gardenId: data.id,
			userId,
			role: 'VIEWER',
			inviterId: client.profile.id,
			status: 'CREATED'
		});
	}

	/** Add a default workspace. */
	tx.insert(ctx.jazz.workspaces, {
		gardenId: data.id,
		name: 'Default',
		slug: 'default'
	});

	/** Add a default environment. */
	tx.insert(ctx.jazz.environments, {
		gardenId: data.id,
		name: 'Default',
		parentType: 'GARDEN',
		inherit: true
	});

	tx.commit();

	const garden = await ctx.db.one(ctx.jazz.gardens.where({ id: data.id }));
	if (garden == null) {
		throw new AppError('Failed to create garden.');
	}
	return garden;
}

/**
 * Invites users to an existing garden.
 */
export async function gardenMembershipCreate(
	data: GardenMembershipCreateCommand,
	ctx: ControllerContext
) {
	const { client, garden } = await ctx.requireRole(data.gardenId, 'MembershipCreate');

	const adminIds = await getNewMembershipIdsFromUsernames(
		data.adminInvites,
		ctx,
		garden
	);
	const editorIds = await getNewMembershipIdsFromUsernames(
		data.editorInvites,
		ctx,
		garden
	);
	const viewerIds = await getNewMembershipIdsFromUsernames(
		data.viewerInvites,
		ctx,
		garden
	);

	const tx = ctx.db.beginTransaction(ctx.jazz.gardens);

	/** Update the garden's ID arrays, deduplicating. */
	tx.update(ctx.jazz.gardens, garden.id, {
		adminIds: [...new Set([...garden.adminIds, ...adminIds])],
		editorIds: [...new Set([...garden.editorIds, ...editorIds])],
		viewerIds: [...new Set([...garden.viewerIds, ...viewerIds])]
	});

	for (const userId of adminIds) {
		tx.insert(ctx.jazz.gardenMemberships, {
			gardenId: garden.id,
			userId,
			role: 'ADMIN',
			inviterId: client.profile.id,
			status: 'CREATED'
		});
	}
	for (const userId of editorIds) {
		tx.insert(ctx.jazz.gardenMemberships, {
			gardenId: garden.id,
			userId,
			role: 'EDITOR',
			inviterId: client.profile.id,
			status: 'CREATED'
		});
	}
	for (const userId of viewerIds) {
		tx.insert(ctx.jazz.gardenMemberships, {
			gardenId: garden.id,
			userId,
			role: 'VIEWER',
			inviterId: client.profile.id,
			status: 'CREATED'
		});
	}

	tx.commit();
}

/**
 * Sends a garden membership acceptance request.
 */
export async function gardenMembershipAccept(
	data: GardenMembershipAcceptCommand,
	ctx: ControllerContext
) {
	const client = await ctx.getClientOrError();

	const membership = await ctx.db.one(
		ctx.jazz.gardenMemberships.where({
			gardenId: data.gardenId,
			userId: client.profile.id
		})
	);
	if (!membership) {
		throw new AppError('Membership does not exist in the collection.', {
			nonFormErrors: ['The invite to this garden does not exist.']
		});
	}

	if (membership.status === 'ACCEPTED') {
		throw new AppError('Membership was already accepted.', {
			nonFormErrors: ['The invite to this garden is already accepted.']
		});
	}

	ctx.db.update(ctx.jazz.gardenMemberships, membership.id, {
		status: 'ACCEPTED',
		acceptedAt: new Date()
	});
}

/**
 * Deletes a user's own membership in a garden.
 */
export async function gardenMembershipDelete(
	data: GardenMembershipDeleteCommand,
	ctx: ControllerContext
) {
	const client = await ctx.getClientOrError();

	const membership = await ctx.db.one(
		ctx.jazz.gardenMemberships.where({
			gardenId: data.gardenId,
			userId: client.profile.id
		})
	);
	if (!membership) {
		throw new AppError('Membership does not exist in the collection.', {
			nonFormErrors: ['The membership in this garden does not exist.']
		});
	}

	ctx.db.delete(ctx.jazz.gardenMemberships, membership.id);
}

/**
 * Revokes a membership of a different user.
 */
export async function gardenMembershipRevoke(
	data: GardenMembershipRevokeCommand,
	ctx: ControllerContext
) {
	const { client } = await ctx.requireRole(data.gardenId, 'MembershipRevoke');

	if (client.profile.id === data.profileId) {
		throw new AppError(
			"Attempted to revoke one's own membership with the wrong command.",
			{ nonFormErrors: ['Cannot revoke own membership - leave instead.'] }
		);
	}

	const membership = await ctx.db.one(
		ctx.jazz.gardenMemberships.where({
			gardenId: data.gardenId,
			userId: data.profileId
		})
	);
	if (!membership) {
		throw new AppError('Membership does not exist in the collection.', {
			nonFormErrors: ['The membership in this garden does not exist.']
		});
	}

	ctx.db.delete(ctx.jazz.gardenMemberships, membership.id);
}

/**
 * Changes the role of an existing garden membership.
 */
export async function gardenMembershipRoleChange(
	data: GardenMembershipRoleChangeCommand,
	ctx: ControllerContext
) {
	const { client, garden } = await ctx.requireRole(
		data.gardenId,
		'MembershipRoleChange'
	);

	if (client.profile.id === data.profileId) {
		throw new AppError("Attempted to change the role of one's own membership.", {
			nonFormErrors: ['You cannot change the role of your own membership.']
		});
	}
	if (data.profileId === garden.creatorId) {
		throw new AppError("Creator's role cannot be changed.", {
			nonFormErrors: ["You cannot change the role of the garden's creator."]
		});
	}

	const membership = await ctx.db.one(
		ctx.jazz.gardenMemberships.where({
			gardenId: data.gardenId,
			userId: data.profileId
		})
	);
	if (!membership) {
		throw new AppError('Membership does not exist in the collection.', {
			nonFormErrors: ['The membership in this garden does not exist.']
		});
	}

	if (data.newRole === membership.role) {
		throw new AppError('Role to be changed is not different.', {
			fieldErrors: { newRole: ['The user already has this role.'] }
		});
	}

	/** Remove from old role array and add to new role array. */
	const newAdminIds = garden.adminIds.filter((id) => id !== data.profileId);
	const newEditorIds = garden.editorIds.filter((id) => id !== data.profileId);
	const newViewerIds = garden.viewerIds.filter((id) => id !== data.profileId);

	switch (data.newRole) {
		case 'ADMIN':
			newAdminIds.push(data.profileId);
			break;
		case 'EDITOR':
			newEditorIds.push(data.profileId);
			break;
		case 'VIEWER':
			newViewerIds.push(data.profileId);
			break;
		default:
			throw new AppError('New role not a valid role.', {
				nonFormErrors: ['Something went wrong.']
			});
	}

	const tx = ctx.db.beginTransaction(ctx.jazz.gardens);
	tx.update(ctx.jazz.gardens, garden.id, {
		adminIds: newAdminIds,
		editorIds: newEditorIds,
		viewerIds: newViewerIds
	});
	tx.update(ctx.jazz.gardenMemberships, membership.id, { role: data.newRole });
	tx.commit();
}
