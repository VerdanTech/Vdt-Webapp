import { type GardenRole } from './index.js';

/**
 * This file is a centralized location for mapping application actions to a required Garden role.
 */
declare const permissions: Readonly<{
	/** Gardens. */
	MembershipCreate: 'ADMIN';
	MembershipRevoke: 'ADMIN';
	MembershipRoleChange: 'ADMIN';
	/** Workspaces. */
	WorkspaceCreate: 'ADMIN';
	WorkspaceUpdate: 'ADMIN';
	WorkspaceEdit: 'EDITOR';
	PlantingAreaCreate: 'EDITOR';
	/** Plants. */
	PlantsCreate: 'EDITOR';
}>;
export type ActionType = keyof typeof permissions;
/**
 * Retrieves the required role of an action.
 * @param action The action to retrieve the required role for.
 * @returns The required role.
 */
export declare function requiredRole(action: ActionType): GardenRole;
export {};
//# sourceMappingURL=permissions.d.ts.map
