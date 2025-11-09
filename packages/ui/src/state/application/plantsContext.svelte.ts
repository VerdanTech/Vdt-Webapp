import { useQuery } from '@triplit/svelte';

import { type ControllerContext, resolveCultivar } from '@vdg-webapp/models';
import { AppError, type Cultivar } from '@vdg-webapp/models';

import type { GardenContext } from './gardenContext.svelte';

const MAX_CULTIVAR_COLLECTION_INHERITANCE_DEPTH = 16;
const MAX_CULTIVAR_INHERITANCE_DEPTH = 16;

/**
 * Holds context for a garden's plants.
 */
export function createPlantsContext(
	controller: ControllerContext,
	garden: GardenContext
) {
	/** Queries all plants in the garden. */
	const plantsQuery = $derived(
		useQuery(
			controller.triplit,
			controller.triplit
				.query('plants')
				.Where('gardenId', '=', garden.id)
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
			if (names.length === 0) return new Map<string, Cultivar>();

			const promises = names.map((name) =>
				resolveCultivar(
					garden.id,
					name,
					MAX_CULTIVAR_COLLECTION_INHERITANCE_DEPTH,
					MAX_CULTIVAR_INHERITANCE_DEPTH,
					controller
				)
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
	function getCultivar(cultivarName: string): Cultivar {
		const cultivar = plantsCultivarMap.get(cultivarName);
		if (!cultivar) {
			throw new AppError('Error retrieving plant cultivar.', {
				nonFormErrors: ['Error retrieving plant cultivar.']
			});
		}
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
