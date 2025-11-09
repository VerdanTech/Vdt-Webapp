import { useQuery } from '@triplit/svelte';

import { type ControllerContext, type GardenRole } from '@vdg-webapp/models';
import { type ActionType, requiredRole as getRequiredRole } from '@vdg-webapp/models';

import { type ClientContext, type ClientContextParams } from './client.svelte';

/**
 * Holds context for a garden,
 * allowing UI elements to be rendered based on a user's
 * level of permissions.
 */
export function createGardenContext(
	controller: ControllerContext,
	client: ClientContext
) {
	let id = $state('');
	const gardenQuery = $derived(
		useQuery(controller.triplit, controller.triplit.query('gardens').Id(id))
	);
	const garden = $derived(gardenQuery.results ? gardenQuery.results[0] : null);
	const role: GardenRole | null = $derived.by(() => {
		if (!client.profile || !garden) {
			return null;
		}

		if (garden.adminIds.has(client.profile.id)) {
			return 'ADMIN';
		} else if (garden.editorIds.has(client.profile.id)) {
			return 'EDITOR';
		} else if (garden.viewerIds.has(client.profile.id)) {
			return 'VIEWER';
		}

		return null;
	});
	$inspect(client.profile);
	$inspect(role);

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
