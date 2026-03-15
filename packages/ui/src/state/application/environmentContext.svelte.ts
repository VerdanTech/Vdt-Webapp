import { useQuery } from '@triplit/svelte';

import { type ControllerContext } from '@vdg-webapp/models';

import type { GardenContext } from './gardenContext.svelte';

/**
 * Holds context for a garden's environments.
 */
export function createEnvironmentContext(
	controller: ControllerContext,
	garden: GardenContext
) {
	/** Queries all environments in the garden. */
	const environmentsQuery = $derived(
		useQuery(
			controller.triplit,
			controller.triplit.query('environments').Where('gardenId', '=', garden.id)
		)
	);
	const environments = $derived(environmentsQuery.results ?? []);

	return {
		get environments() {
			return environments;
		}
	};
}
export type EnvironmentContext = ReturnType<typeof createEnvironmentContext>;
