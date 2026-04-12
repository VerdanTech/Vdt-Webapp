import { arrayContains, eq, sql } from 'drizzle-orm';

import {
	AppError,
	type Garden,
	type GardenCreateCommand,
	type GardenMembershipAcceptCommand,
	type GardenMembershipCreateCommand,
	type GardenMembershipDeleteCommand,
	type GardenMembershipRevokeCommand,
	type GardenMembershipRoleChangeCommand,
	gardenMemberships,
	gardens,
	isProfileMember,
	profiles
} from '@vdg-webapp/models';

import { type Db } from '../db/index.js';
import { type ServerContext, requireGardenRole } from './context.js';

/** Helper — resolve usernames to profile IDs, filtering out existing members. */
async function getNewMemberIds(
	db: Db,
	usernames: string[] | undefined,
	garden?: Garden
): Promise<string[]> {
	if (!usernames || usernames.length === 0) return [];

	const rows = await db.query.profiles.findMany({
		where: (p, { inArray }) => inArray(p.username, usernames),
		columns: { id: true }
	});

	return rows
		.map((r) => r.id)
		.filter((id) => garden === undefined || !isProfileMember(garden, id));
}

/** Creates a new garden with optional initial memberships. */
export async function gardenCreate(
	data: GardenCreateCommand,
	ctx: ServerContext
): Promise<{ id: string; txid: number }> {
	const existing = await ctx.db.query.gardens.findFirst({
		where: eq(gardens.id, data.id),
		columns: { id: true }
	});
	if (existing) {
		throw new AppError('Garden ID already exists.', {
			fieldErrors: { id: ['Key already exists.'] }
		});
	}

	const adminIds = await getNewMemberIds(ctx.db, data.adminInvites);
	const editorIds = await getNewMemberIds(ctx.db, data.editorInvites);
	const viewerIds = await getNewMemberIds(ctx.db, data.viewerInvites);

	/** Creator is always an admin. */
	if (!adminIds.includes(ctx.userId)) {
		adminIds.push(ctx.userId);
	}

	return ctx.db.transaction(async (tx) => {
		await tx.insert(gardens).values({
			id: data.id,
			name: data.name,
			visibility: data.visibility,
			description: data.description,
			creatorId: ctx.userId,
			adminIds,
			editorIds,
			viewerIds
		});

		/** Creator membership. */
		await tx.insert(gardenMemberships).values({
			gardenId: data.id,
			userId: ctx.userId,
			role: 'ADMIN',
			inviterId: null,
			status: 'ACCEPTED'
		});

		/** Invited memberships. */
		const pendingMemberships = [
			...adminIds
				.filter((id) => id !== ctx.userId)
				.map((id) => ({ gardenId: data.id, userId: id, role: 'ADMIN' as const, inviterId: ctx.userId, status: 'CREATED' as const })),
			...editorIds.map((id) => ({
				gardenId: data.id,
				userId: id,
				role: 'EDITOR' as const,
				inviterId: ctx.userId,
				status: 'CREATED' as const
			})),
			...viewerIds.map((id) => ({
				gardenId: data.id,
				userId: id,
				role: 'VIEWER' as const,
				inviterId: ctx.userId,
				status: 'CREATED' as const
			}))
		];
		if (pendingMemberships.length > 0) {
			await tx.insert(gardenMemberships).values(pendingMemberships);
		}

		/** Default workspace and environment are created by their own controllers
		 *  when called from the route handler after garden creation. */

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { id: data.id, txid: parseInt(txid) };
	});
}

/** Invites users to an existing garden. */
export async function gardenMembershipCreate(
	data: GardenMembershipCreateCommand,
	ctx: ServerContext
): Promise<{ txid: number }> {
	const garden = await requireGardenRole(ctx, data.gardenId, 'MembershipCreate');

	const adminIds = await getNewMemberIds(ctx.db, data.adminInvites, garden);
	const editorIds = await getNewMemberIds(ctx.db, data.editorInvites, garden);
	const viewerIds = await getNewMemberIds(ctx.db, data.viewerInvites, garden);

	return ctx.db.transaction(async (tx) => {
		await tx
			.update(gardens)
			.set({
				adminIds: sql`array_cat(${gardens.adminIds}, ${sql.raw(`ARRAY[${adminIds.map((id) => `'${id}'`).join(',')}]::text[]`)})`,
				editorIds: sql`array_cat(${gardens.editorIds}, ${sql.raw(`ARRAY[${editorIds.map((id) => `'${id}'`).join(',')}]::text[]`)})`,
				viewerIds: sql`array_cat(${gardens.viewerIds}, ${sql.raw(`ARRAY[${viewerIds.map((id) => `'${id}'`).join(',')}]::text[]`)})`
			})
			.where(eq(gardens.id, data.gardenId));

		const newMemberships = [
			...adminIds.map((id) => ({ gardenId: data.gardenId, userId: id, role: 'ADMIN' as const, inviterId: ctx.userId, status: 'CREATED' as const })),
			...editorIds.map((id) => ({ gardenId: data.gardenId, userId: id, role: 'EDITOR' as const, inviterId: ctx.userId, status: 'CREATED' as const })),
			...viewerIds.map((id) => ({ gardenId: data.gardenId, userId: id, role: 'VIEWER' as const, inviterId: ctx.userId, status: 'CREATED' as const }))
		];
		if (newMemberships.length > 0) {
			await tx.insert(gardenMemberships).values(newMemberships);
		}

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}

/** Accepts a garden membership invite. */
export async function gardenMembershipAccept(
	data: GardenMembershipAcceptCommand,
	ctx: ServerContext
): Promise<{ txid: number }> {
	const membership = await ctx.db.query.gardenMemberships.findFirst({
		where: (m, { and, eq }) =>
			and(eq(m.gardenId, data.gardenId), eq(m.userId, ctx.userId))
	});
	if (!membership) {
		throw new AppError('Membership does not exist.', {
			nonFormErrors: ['The invite to this garden does not exist.']
		});
	}
	if (membership.status === 'ACCEPTED') {
		throw new AppError('Membership already accepted.', {
			nonFormErrors: ['The invite to this garden is already accepted.']
		});
	}

	return ctx.db.transaction(async (tx) => {
		await tx
			.update(gardenMemberships)
			.set({ status: 'ACCEPTED', acceptedAt: new Date() })
			.where(eq(gardenMemberships.id, membership.id));

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}

/** Deletes the calling user's own membership. */
export async function gardenMembershipDelete(
	data: GardenMembershipDeleteCommand,
	ctx: ServerContext
): Promise<{ txid: number }> {
	const membership = await ctx.db.query.gardenMemberships.findFirst({
		where: (m, { and, eq }) =>
			and(eq(m.gardenId, data.gardenId), eq(m.userId, ctx.userId))
	});
	if (!membership) {
		throw new AppError('Membership does not exist.', {
			nonFormErrors: ['The membership in this garden does not exist.']
		});
	}

	return ctx.db.transaction(async (tx) => {
		await tx.delete(gardenMemberships).where(eq(gardenMemberships.id, membership.id));

		/** Remove the user's ID from the garden's role arrays. */
		await tx
			.update(gardens)
			.set({
				adminIds: sql`array_remove(${gardens.adminIds}, ${ctx.userId})`,
				editorIds: sql`array_remove(${gardens.editorIds}, ${ctx.userId})`,
				viewerIds: sql`array_remove(${gardens.viewerIds}, ${ctx.userId})`
			})
			.where(eq(gardens.id, data.gardenId));

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}

/** Revokes another user's membership. */
export async function gardenMembershipRevoke(
	data: GardenMembershipRevokeCommand,
	ctx: ServerContext
): Promise<{ txid: number }> {
	await requireGardenRole(ctx, data.gardenId, 'MembershipRevoke');

	if (ctx.userId === data.profileId) {
		throw new AppError('Cannot revoke own membership — use leave instead.', {
			nonFormErrors: ['Cannot revoke own membership - leave instead.']
		});
	}

	const membership = await ctx.db.query.gardenMemberships.findFirst({
		where: (m, { and, eq }) =>
			and(eq(m.gardenId, data.gardenId), eq(m.userId, data.profileId))
	});
	if (!membership) {
		throw new AppError('Membership does not exist.', {
			nonFormErrors: ['The membership in this garden does not exist.']
		});
	}

	return ctx.db.transaction(async (tx) => {
		await tx.delete(gardenMemberships).where(eq(gardenMemberships.id, membership.id));

		await tx
			.update(gardens)
			.set({
				adminIds: sql`array_remove(${gardens.adminIds}, ${data.profileId})`,
				editorIds: sql`array_remove(${gardens.editorIds}, ${data.profileId})`,
				viewerIds: sql`array_remove(${gardens.viewerIds}, ${data.profileId})`
			})
			.where(eq(gardens.id, data.gardenId));

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}

/** Changes the role of another user's membership. */
export async function gardenMembershipRoleChange(
	data: GardenMembershipRoleChangeCommand,
	ctx: ServerContext
): Promise<{ txid: number }> {
	const garden = await requireGardenRole(ctx, data.gardenId, 'MembershipRoleChange');

	if (ctx.userId === data.profileId) {
		throw new AppError('Cannot change own membership role.', {
			nonFormErrors: ['You cannot change the role of your own membership.']
		});
	}
	if (data.profileId === garden.creatorId) {
		throw new AppError("Creator's role cannot be changed.", {
			nonFormErrors: ["You cannot change the role of the garden's creator."]
		});
	}

	const membership = await ctx.db.query.gardenMemberships.findFirst({
		where: (m, { and, eq }) =>
			and(eq(m.gardenId, data.gardenId), eq(m.userId, data.profileId))
	});
	if (!membership) {
		throw new AppError('Membership does not exist.', {
			nonFormErrors: ['The membership in this garden does not exist.']
		});
	}
	if (data.newRole === membership.role) {
		throw new AppError('Role is not different.', {
			fieldErrors: { newRole: ['The user already has this role.'] }
		});
	}

	return ctx.db.transaction(async (tx) => {
		/** Remove from all arrays, then add to the new one. */
		await tx
			.update(gardens)
			.set({
				adminIds: sql`array_remove(${gardens.adminIds}, ${data.profileId})`,
				editorIds: sql`array_remove(${gardens.editorIds}, ${data.profileId})`,
				viewerIds: sql`array_remove(${gardens.viewerIds}, ${data.profileId})`
			})
			.where(eq(gardens.id, data.gardenId));

		const addColumn = {
			ADMIN: gardens.adminIds,
			EDITOR: gardens.editorIds,
			VIEWER: gardens.viewerIds
		}[data.newRole];

		await tx
			.update(gardens)
			.set({
				[addColumn.name]: sql`array_append(${addColumn}, ${data.profileId})`
			})
			.where(eq(gardens.id, data.gardenId));

		await tx
			.update(gardenMemberships)
			.set({ role: data.newRole })
			.where(eq(gardenMemberships.id, membership.id));

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}
