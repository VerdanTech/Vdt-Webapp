import type { Garden, GardenRole } from './schema.js';

/**
 * Returns an array of all profile IDs which are members of a garden.
 */
export const getMemberIds = (garden: Garden): string[] => {
	return [...garden.adminIds, ...garden.editorIds, ...garden.viewerIds];
};

/**
 * Checks whether a profile is an existing member of a garden.
 */
export const isProfileMember = (garden: Garden, profileId: string): boolean => {
	return (
		garden.adminIds.includes(profileId) ||
		garden.editorIds.includes(profileId) ||
		garden.viewerIds.includes(profileId)
	);
};

/**
 * Checks whether a user has at least the given role in the garden.
 * Roles are upwards-inclusive: admin satisfies editor and viewer checks.
 */
export const isUserAuthorized = (
	garden: Garden,
	profileId: string,
	role: GardenRole
): boolean => {
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
