import { useQuery } from '@triplit/svelte';

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
	/** Queries all plants in the garden and within the selected timeline. */
	const plantsQuery = $derived(
		useQuery(
			controller.triplit,
			controller.triplit
				.query('plants')
				.Where('gardenId', '=', garden.id)
				//.Where('beginDate', '>=', timeline.beginSelection)
				//.Where('endDate', '<=', timeline.endSelection)
				.Include('expectedLifespan', (rel) =>
					rel('expectedLifespan')
						.Include('geometryHistory', (rel) =>
							rel('geometryHistory').Include('geometries', (rel) =>
								rel('geometries').Include('linesCoordinates')
							)
						)
						.Include('locationHistory', (rel) =>
							rel('locationHistory').Include('locations')
						)
						.Include('observations')
				)
				.Include('recordedLifespan', (rel) =>
					rel('recordedLifespan')
						.Include('geometryHistory', (rel) =>
							rel('geometryHistory').Include('geometries', (rel) =>
								rel('geometries').Include('linesCoordinates')
							)
						)
						.Include('locationHistory', (rel) =>
							rel('locationHistory').Include('locations')
						)
						.Include('observations')
				)
		)
	);
	const plants = $derived(plantsQuery.results ?? []);
	/** The set of cultivar names used by all plants in the garden. */
	const plantsCultivarNames = $derived(
		plantsQuery.results?.map((plant) => plant.cultivarName) ?? []
	);
	/**
	 * Constructs a map of cultivar names included in the Plants query
	 * to the full cultivar object and attributes.
	*/
	let plantsCultivarMap: Map<string, Cultivar> = $state(new Map());
	$effect(() => {
		(async () => {
			const names = Array.from(plantsCultivarNames ?? []);
			if (names.length === 0) {
				plantsCultivarMap = new Map<string, Cultivar>();
				return
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
		const cultivar = plantsCultivarMap.get(cultivarName) ?? null;
		return cultivar;
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
