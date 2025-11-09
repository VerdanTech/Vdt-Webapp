import { useQuery } from '@triplit/svelte';

import type { ControllerContext } from '@vdg-webapp/models';

import type { GardenContext } from './gardenContext.svelte';

/**
 * Holds context for the workspaces in a garden.
 */
export function createWorkspacesContext(
	controller: ControllerContext,
	garden: GardenContext
) {
	const workspacesQuery = $derived(
		useQuery(
			controller.triplit,
			controller.triplit.query('workspaces').Where(['gardenId', '=', garden.id])
		)
	);
	const workspaces = $derived(workspacesQuery.results ?? []);
	const plantingAreasQuery = $derived(
		useQuery(
			controller.triplit,
			controller.triplit
				.query('plantingAreas')
				.Where('gardenId', '=', garden.id)
				.Include('geometry', (rel) => rel('geometry').Include('linesCoordinates'))
				.Include('locationHistory', (rel) =>
					rel('locationHistory').Include('locations')
				)
		)
	);
	const plantingAreas = $derived(plantingAreasQuery.results ?? []);

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
