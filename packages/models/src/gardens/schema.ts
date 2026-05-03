import { type TableRow, schema as s } from 'jazz-tools';

/**
 * Controls the visibility of the garden.
 * HIDDEN: the garden is visible only to those who are members.
 * UNLISTED: the garden is visibile to anyone but is not listed
 *     on any public page - a link is required.
 * PUBLIC: the garden is visible to anyone and may be searchable.
 */
export const GardenVisibilityEnumOptions = ['HIDDEN', 'UNLISTED', 'PUBLIC'] as const;

/**
 * Controls the level of access of a garden membership.
 * ADMIN: all actions are supported.
 * EDITOR: routine changes in model state are supported, such as adding plant models,
 *     while configuration changes such as garden attributes are not.
 * VIEWER: Read-only access.
 */
export const GardenMembershipRoleEnumOptions = ['ADMIN', 'EDITOR', 'VIEWER'] as const;

/**
 * Indicates the acceptance status of a garden membership.
 * CREATED: the invite has been created but no notification has been sent.
 * PENDING: a notification has been sent and is pending acceptance.
 * ACCEPTED: the membership has been accepted.
 */
export const GardenMembershipStatusEnumOptions = [
	'CREATED',
	'PENDING',
	'ACCEPTED'
] as const;

export const gardenSchema = {
	/** Garden schema. */
	gardens: s.table({
		/** Non-unique name of the garden. */
		name: s.string(),
		/** Controls which non-users may view the garden. */
		visibility: s.enum(...GardenVisibilityEnumOptions),
		/** Optional description. */
		description: s.string().optional(),
		/** Set to false for inactive gardens. */
		isActive: s.boolean().default(true),
		/**
		 * User who created the garden.
		 * Note that the creator has access through an admin membership.
		 * If undefined, the original creator has left the garden.
		 */
		creatorId: s.ref('users').optional(),
		/** Set of users which have admin access. */
		adminIds: s.array(s.string()),
		/** Set of users which have editing access. */
		editorIds: s.array(s.string()).default([]),
		/** Set of users which have viewing access. */
		viewerIds: s.array(s.string()).default([])
	}),
	/** Garden membership schema. */
	gardenMemberships: s.table({
		/** Garden the membership is in. */
		gardenId: s.ref('gardens'),

		/** User who is the subject of the membership. */
		userId: s.ref('users'),

		/** Role of the membership. */
		role: s.enum(...GardenMembershipRoleEnumOptions),

		/** User who created the membership. */
		inviterId: s.ref('users').optional(),

		/** The acceptance status and acceptance date of the membership. */
		status: s.enum(...GardenMembershipStatusEnumOptions),
		acceptedAt: s.timestamp().optional(),

		/** Allows marking gardens as favorites in the menu. */
		favorite: s.boolean().default(false)
	})
};
export type Garden = TableRow<typeof gardenSchema, 'gardens'>;
export type GardenMembership = TableRow<typeof gardenSchema, 'gardenMemberships'>;
export type GardenVisibility = (typeof GardenVisibilityEnumOptions)[number];
export type GardenRole = (typeof GardenMembershipRoleEnumOptions)[number];
export type GardenMembershipStatus = (typeof GardenMembershipStatusEnumOptions)[number];
