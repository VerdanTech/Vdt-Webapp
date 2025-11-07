import { useQuery } from '@triplit/svelte';

import { type ControllerContext, type GardenRole } from '@vdg-webapp/models';
import { type ActionType, requiredRole as getRequiredRole } from '@vdg-webapp/models';

/**
 * Holds context for a garden,
 * allowing UI elements to be rendered based on a user's
 * level of permissions.
 */
export function createGardenContext(controller: ControllerContext) {
	let id = $state('');
	const clientQuery = $derived(
		useQuery(
			controller.triplit,
			controller.triplit.query('accounts').Id('$session.accountId').Include('profile')
		)
	);
	const gardenQuery = $derived(
		useQuery(controller.triplit, controller.triplit.query('gardens').Id(id))
	);
	const role: GardenRole | null = $derived.by(() => {
		if (
			!clientQuery.results ||
			!clientQuery.results[0] ||
			!clientQuery.results[0].profile ||
			!gardenQuery.results ||
			!gardenQuery.results[0]
		) {
			return null;
		}

		const client = clientQuery.results[0].profile;
		const garden = gardenQuery.results[0];

		if (garden.adminIds.has(client.id)) {
			return 'ADMIN';
		} else if (garden.editorIds.has(client.id)) {
			return 'EDITOR';
		} else if (garden.viewerIds.has(client.id)) {
			return 'VIEWER';
		}

		return null;
	});

	/**
	 * Returns whether the user can take an action on the active garden.
	 * @param action The action to check.
	 * @returns If true, the user is authorized.
	 */
	function authorize(action: ActionType): boolean {
		/** False for a null garden or user role. */
		if (id === null || role === null) {
			return false;
		}

		const requiredRole = getRequiredRole(action);
		if (requiredRole === 'ADMIN' && role === 'ADMIN') {
			return true;
		} else if (requiredRole === 'EDITOR' && (role === 'ADMIN' || role === 'EDITOR')) {
			return true;
		} else if (
			requiredRole === 'VIEWER' &&
			(role === 'ADMIN' || role === 'EDITOR' || role === 'VIEWER')
		) {
			return true;
		} else {
			return false;
		}
	}

	return {
		get id() {
			return id;
		},
		get role() {
			return role;
		},
		set id(newVal) {
			id = newVal;
		},
		authorize
	};
}
export type GardenContext = ReturnType<typeof createGardenContext>;
