import { boolean, pgEnum, pgTable, text, timestamp, uuid } from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';

import { profiles } from '../users/schema.js';

/**
 * Controls the visibility of the garden.
 * HIDDEN: visible only to members.
 * UNLISTED: visible to anyone but not listed on public pages.
 * PUBLIC: visible to anyone and may be searchable.
 */
export const GardenVisibilityEnumOptions = ['HIDDEN', 'UNLISTED', 'PUBLIC'] as const;

/**
 * Controls the level of access of a garden membership.
 * ADMIN: all actions are supported.
 * EDITOR: routine changes are supported; configuration changes are not.
 * VIEWER: read-only access.
 */
export const GardenMembershipRoleEnumOptions = ['ADMIN', 'EDITOR', 'VIEWER'] as const;

/**
 * Indicates the acceptance status of a garden membership.
 * CREATED: invite created but no notification sent.
 * PENDING: notification sent, pending acceptance.
 * ACCEPTED: membership accepted.
 */
export const GardenMembershipStatusEnumOptions = [
	'CREATED',
	'PENDING',
	'ACCEPTED'
] as const;

export const gardenVisibilityEnum = pgEnum('garden_visibility', GardenVisibilityEnumOptions);
export const gardenMembershipRoleEnum = pgEnum(
	'garden_membership_role',
	GardenMembershipRoleEnumOptions
);
export const gardenMembershipStatusEnum = pgEnum(
	'garden_membership_status',
	GardenMembershipStatusEnumOptions
);

export const gardens = pgTable('gardens', {
	/** URL-friendly shorthand — user-defined, unique. */
	id: text('id').primaryKey(),

	/** Non-unique name of the garden. */
	name: text('name').notNull(),

	/** Controls which non-members may view the garden. */
	visibility: gardenVisibilityEnum('visibility').notNull(),

	/** Optional description. */
	description: text('description'),

	/** Set to false for inactive gardens. */
	isActive: boolean('is_active').default(true).notNull(),

	/**
	 * User who created the garden.
	 * If null, the original creator has left.
	 */
	creatorId: uuid('creator_id'),

	/** Profile IDs which have admin access. */
	adminIds: text('admin_ids').array().notNull().default([]),

	/** Profile IDs which have editing access. */
	editorIds: text('editor_ids').array().notNull().default([]),

	/** Profile IDs which have viewing access. */
	viewerIds: text('viewer_ids').array().notNull().default([]),

	/** Date of garden creation. */
	createdAt: timestamp('created_at').defaultNow().notNull()
});

export const gardenMemberships = pgTable('garden_memberships', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** Garden the membership is in. */
	gardenId: text('garden_id')
		.notNull()
		.references(() => gardens.id, { onDelete: 'cascade' }),

	/** Profile ID of the member. */
	userId: uuid('user_id')
		.notNull()
		.references(() => profiles.id),

	/** Role of the membership. */
	role: gardenMembershipRoleEnum('role').notNull(),

	/** Profile ID of who created the membership. */
	inviterId: uuid('inviter_id'),

	/** Acceptance status. */
	status: gardenMembershipStatusEnum('status').notNull(),

	/** Date the membership was accepted. */
	acceptedAt: timestamp('accepted_at'),

	/** Allows marking a garden as a favourite in the menu. */
	favorite: boolean('favorite').default(false).notNull()
});

export const gardensRelations = relations(gardens, ({ one, many }) => ({
	creator: one(profiles, { fields: [gardens.creatorId], references: [profiles.id] }),
	memberships: many(gardenMemberships)
}));

export const gardenMembershipsRelations = relations(gardenMemberships, ({ one }) => ({
	garden: one(gardens, {
		fields: [gardenMemberships.gardenId],
		references: [gardens.id]
	}),
	user: one(profiles, {
		fields: [gardenMemberships.userId],
		references: [profiles.id]
	}),
	inviter: one(profiles, {
		fields: [gardenMemberships.inviterId],
		references: [profiles.id]
	})
}));

export type Garden = typeof gardens.$inferSelect;
export type GardenMembership = typeof gardenMemberships.$inferSelect;
export type GardenVisibility = (typeof GardenVisibilityEnumOptions)[number];
export type GardenRole = (typeof GardenMembershipRoleEnumOptions)[number];
export type GardenMembershipStatus = (typeof GardenMembershipStatusEnumOptions)[number];
