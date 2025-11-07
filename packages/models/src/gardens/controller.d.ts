import { type ControllerContext } from '../controller.js';
import {
	type Garden,
	type GardenCreateCommand,
	type GardenMembershipAcceptCommand,
	type GardenMembershipCreateCommand,
	type GardenMembershipDeleteCommand,
	type GardenMembershipRevokeCommand,
	type GardenMembershipRoleChangeCommand
} from '../index.js';

/** Commands. */
/**
 * Creates a new garden.
 */
export declare function gardenCreate(
	data: GardenCreateCommand,
	ctx: ControllerContext
): Promise<Garden>;
/**
 * Invites users to an existing garden.
 */
export declare function gardenMembershipCreate(
	data: GardenMembershipCreateCommand,
	ctx: ControllerContext
): Promise<void>;
/**
 * Sends a garden membership acceptance request.
 */
export declare function gardenMembershipAccept(
	data: GardenMembershipAcceptCommand,
	ctx: ControllerContext
): Promise<void>;
/**
 * Deletes a user's own membership in a garden.
 */
export declare function gardenMembershipDelete(
	data: GardenMembershipDeleteCommand,
	ctx: ControllerContext
): Promise<void>;
/**
 * Revokes a membership of a different user.
 */
export declare function gardenMembershipRevoke(
	data: GardenMembershipRevokeCommand,
	ctx: ControllerContext
): Promise<void>;
/**
 * Revokes a membership of a different user.
 */
export declare function gardenMembershipRoleChange(
	data: GardenMembershipRoleChangeCommand,
	ctx: ControllerContext
): Promise<void>;
//# sourceMappingURL=controller.d.ts.map
