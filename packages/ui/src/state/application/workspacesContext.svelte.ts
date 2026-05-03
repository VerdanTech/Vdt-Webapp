import { QuerySubscription } from 'jazz-tools/svelte';

import type { ControllerContext } from '@vdg-webapp/models';

import type { GardenContext } from './gardenContext.svelte';

/**
 * Holds context for the workspaces in a garden.
 */
export function createWorkspacesContext(
	controller: ControllerContext,
	garden: GardenContext
) {
	const workspacesSub = $derived(
		new QuerySubscription(
			garden.id ? controller.jazz.workspaces.where({ gardenId: garden.id }) : undefined
		)
	);
	const workspaces = $derived(workspacesSub.current ?? []);

	/** TODO: Add geometry/locationHistory includes once Jazz2 include API is confirmed. */
	const plantingAreasSub = $derived(
		new QuerySubscription(
			garden.id
				? controller.jazz.plantingAreas.where({ gardenId: garden.id })
				: undefined
		)
	);
	const plantingAreas = $derived(plantingAreasSub.current ?? []);

	return {
		get workspaces() {
			return workspaces;
		},
		get plantingAreas() {
			return plantingAreas;
		}
	};
}
export type WorkspacesContext = ReturnType<typeof createWorkspacesContext>;
