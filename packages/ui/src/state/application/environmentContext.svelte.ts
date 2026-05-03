import { QuerySubscription } from 'jazz-tools/svelte';

import { type ControllerContext } from '@vdg-webapp/models';

import type { GardenContext } from './gardenContext.svelte';

/**
 * Holds context for a garden's environments.
 */
export function createEnvironmentContext(
	controller: ControllerContext,
	garden: GardenContext
) {
	const environmentsSub = $derived(
		new QuerySubscription(
			garden.id
				? controller.jazz.environments.where({ gardenId: garden.id })
				: undefined
		)
	);
	const environments = $derived(environmentsSub.current ?? []);

	return {
		get environments() {
			return environments;
		}
	};
}
export type EnvironmentContext = ReturnType<typeof createEnvironmentContext>;
