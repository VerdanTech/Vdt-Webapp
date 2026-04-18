import z from 'zod';

import { commonFields } from '../commands.js';
import userFields from '../users/fields.js';

/**
 * Controls the visibility of the garden.
 * HIDDEN: visible only to members.
 * UNLISTED: visible to anyone with a link.
 * PUBLIC: publicly searchable.
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

/** Field specifications for garden domain commands. */
const gardenFields = {
	gardenIdField: z
		.string()
		.trim()
		.toLowerCase()
		.min(4, 'Must be at least 4 characters.')
		.max(21, 'May be at most 21 characters.')
		.regex(/[0-9A-Za-z-]+/, 'Must contain only alphanumeric characters and hyphens.')
		.describe('Unique shorthand name for the garden used in URLs.'),
	gardenNameField: commonFields.nameSchema.describe('Name of the garden.'),
	gardenDescriptionField: commonFields.descriptionSchema.describe('Optional description.'),
	gardenVisibilityField: z.enum(GardenVisibilityEnumOptions),
	gardenMembershipRoleField: z.enum(GardenMembershipRoleEnumOptions),
	gardenMembershipStatusField: z.enum(GardenMembershipStatusEnumOptions),
	usernameInvitesListField: z
		.array(userFields.usernameField)
		.max(10, 'A maximum of 10 users can be invited at once.')
};
export default gardenFields;
