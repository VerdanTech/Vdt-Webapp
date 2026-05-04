import type { Garden, GardenRole } from './schema.js';

/**
 * Returns a set of all profile IDs which are members of a garden.
 * @param garden The garden to extract IDs from.
 * @returns All profile IDs of garden members.
 */
export const getMemberIds = (garden: Garden): Set<string> => {
	return new Set([...garden.adminIds, ...garden.editorIds, ...garden.viewerIds]);
};

/**
 * Checks whether a profile is an existing member of a garden.
 * @param garden The garden to check membership of.
 * @param profileId The ID of the profile to check.
 * @returns True if the profile is a member of the garden.
 */
export const isProfileMember = (garden: Garden, profileId: string): boolean => {
	return (
		garden.adminIds.includes(profileId) ||
		garden.editorIds.includes(profileId) ||
		garden.viewerIds.includes(profileId)
	);
};

/**
 * Checks whether a user has a role in the garden.
 * Roles are upwards inclusive, meaning an admin user is authorized for editor activities.
 * @param garden The garden to check membership of.
 * @param profileId The ID of the profile to check.
 * @param role The role to check membership against.
 * @returns True if the user is authorized.
 */
export const isUserAuthorized = (
	garden: Garden,
	profileId: string,
	role: GardenRole
) => {
	switch (role) {
		case 'ADMIN':
			return garden.adminIds.includes(profileId);
		case 'EDITOR':
			return (
				garden.adminIds.includes(profileId) || garden.editorIds.includes(profileId)
			);
		case 'VIEWER':
			return (
				garden.adminIds.includes(profileId) ||
				garden.editorIds.includes(profileId) ||
				garden.viewerIds.includes(profileId)
			);
		default:
			return false;
	}
};
