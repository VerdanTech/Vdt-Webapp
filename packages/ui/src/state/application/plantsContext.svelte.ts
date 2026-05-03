import { QuerySubscription } from 'jazz-tools/svelte';

import { type ControllerContext, resolveCultivar } from '@vdg-webapp/models';
import { AppError, type Cultivar } from '@vdg-webapp/models';

import type { GardenContext } from './gardenContext.svelte';
import type { TimelineContext } from './timelineContext.svelte';

/**
 * Holds context for a garden's plants.
 */
export function createPlantsContext(
	controller: ControllerContext,
	timeline: TimelineContext,
	garden: GardenContext
) {
	/** Queries all plants in the garden. TODO: Add lifespan includes once Jazz2 include API is confirmed. */
	const plantsSub = $derived(
		new QuerySubscription(
			garden.id ? controller.jazz.plants.where({ gardenId: garden.id }) : undefined
		)
	);
	const plants = $derived(plantsSub.current ?? []);
	const plantsCultivarNames = $derived(plants.map((plant) => plant.cultivarName));

	let plantsCultivarMap: Map<string, Cultivar> = $state(new Map());
	$effect(() => {
		(async () => {
			const names = Array.from(plantsCultivarNames ?? []);
			if (names.length === 0) {
				plantsCultivarMap = new Map<string, Cultivar>();
				return;
			}

			const promises = names.map((name) =>
				resolveCultivar(garden.id, name, controller)
			);
			const results = await Promise.all(promises);

			const entries = names.reduce<Array<[string, Cultivar]>>((acc, name, i) => {
				const cultivar = results[i];
				if (cultivar) acc.push([name, cultivar]);
				return acc;
			}, []);
			plantsCultivarMap = new Map(entries);
		})();
	});

	/**
	 * Retrieves a cultivar from a cultivar name.
	 * @param cultivarName The name to retrieve.
	 * @returns The matched cultivar with all attributes.
	 */
	function getCultivar(cultivarName: string): Cultivar | null {
		return plantsCultivarMap.get(cultivarName) ?? null;
	}

	return {
		get plants() {
			return plants;
		},
		get plantsCultivarNames() {
			return plantsCultivarNames;
		},
		getCultivar
	};
}
export type PlantsContext = ReturnType<typeof createPlantsContext>;
