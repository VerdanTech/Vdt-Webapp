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
			controller.triplit.query('plants').Where('gardenId', '=', garden.id)
		)
	);
	/** The set of cultivar names used by all plants in the garden. */
	const plantsCultivarNames = $derived(
		new Set(plantsQuery.results?.map((plant) => plant.cultivarName) ?? [])
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
		plantsQuery,
		plantsCultivarNames,
		getCultivar
	};
}
export type PlantsContext = ReturnType<typeof createPlantsContext>;
