import type { Garden, GardenRole } from './schema.js';

/**
 * Returns a set of all profile IDs which are members of a garden.
 * @param garden The garden to extract IDs from.
 * @returns All profile IDs of garden members.
 */
export declare const getMemberIds: (garden: Garden) => Set<string>;
/**
 * Checks whether a profile is an existing member of a garden.
 * @param garden The garden to check membership of.
 * @param profileId The ID of the profile to check.
 * @returns True if the profile is a member of the garden.
 */
export declare const isProfileMember: (garden: Garden, profileId: string) => boolean;
/**
 * Checks whether a user has a role in the garden.
 * Roles are upwards inclusive, meaning an admin user is authorized for editor activities.
 * @param garden The garden to check membership of.
 * @param profileId The ID of the profile to check.
 * @param role The role to check membership against.
 * @returns True if the user is authorized.
 */
export declare const isUserAuthorized: (
	garden: Garden,
	profileId: string,
	role: GardenRole
) => boolean;
//# sourceMappingURL=utils.d.ts.map
