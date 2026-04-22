import { type Account } from 'jazz-tools';

import { AppError } from './errors.js';
import { type GardenRole, type GardenWithMemberships } from './gardens/schema.js';
import { findAcceptedMembershipForAccount, getGardenByKey } from './index/utils.js';

import { type ActionType, requiredRole } from './permissions.js';

/**
 * Checks whether a member's role meets the required access level.
 * Roles are upwards inclusive: ADMIN satisfies EDITOR and VIEWER requirements.
 * @param memberRole The role the user holds.
 * @param required The minimum role required.
 */
function isRoleSufficient(memberRole: GardenRole, required: GardenRole): boolean {
	const roleRank: Record<GardenRole, number> = { ADMIN: 3, EDITOR: 2, VIEWER: 1 };
	return roleRank[memberRole] >= roleRank[required];
}

/**
 * Creates a controller context bound to a Jazz account.
 * Provides authentication and authorization helpers for command functions.
 * @param me The authenticated Jazz account.
 */
export function createController(me: Account) {
	/**
	 * Returns the authenticated account, or throws if unavailable.
	 */
	async function getClientOrError(): Promise<Account> {
		if (!me) {
			throw new AppError('Authentication failed.', {
				nonFormErrors: ['Authentication failed. A login is required.']
			});
		}
		return me;
	}

	/**
	 * Loads a garden by key and verifies the account holds at least the required role.
	 * @param gardenId The unique ID of the garden.
	 * @param action The action being authorized.
	 * @returns The authenticated account and the loaded garden.
	 */
	async function requireRole(
		gardenId: string,
		action: ActionType
	): Promise<{ me: Account; garden: GardenWithMemberships }> {
		await getClientOrError();

		const garden = await getGardenByKey(gardenId);
		const role = requiredRole(action);
		const membership = findAcceptedMembershipForAccount(garden, me.$jazz.id);

		if (!membership || !isRoleSufficient(membership.role, role)) {
			throw new AppError(`Requires ${role} access.`, {
				nonFormErrors: [`This action requires the ${role} role.`]
			});
		}

		return { me, garden };
	}

	return {
		me,
		getClientOrError,
		requireRole
	};
}

export type ControllerContext = ReturnType<typeof createController>;
