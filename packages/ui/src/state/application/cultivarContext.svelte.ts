import { useQuery } from '@triplit/svelte';

import {
	type ControllerContext,
	type Cultivar,
	resolveCultivar
} from '@vdg-webapp/models';

import type { GardenContext } from './gardenContext.svelte';

/**
 * Holds context for a garden's cultivar collections.
 */
export function createCultivarContext(
	controller: ControllerContext,
	garden: GardenContext
) {
	/** Queries all collections in the garden. */
	const gardenCollectionsQuery = $derived(
		useQuery(
			controller.triplit,
			controller.triplit.query('cultivarCollections').Where('gardenId', '=', garden.id)
		)
	);
	const gardenCollections = $derived(gardenCollectionsQuery.results ?? []);
	const gardenCollectionsIds = $derived(
		gardenCollections.map((collection) => collection.id)
	);
	/** Collects IDs of all the ancestors of collections in the garden. */
	const ancestorCollectionsIds = $derived.by(() => {
		const uniqueAncestorIds = new Set<string>([]);

		for (const collection of gardenCollections) {
			if (!collection.ancestorIds) {
				continue;
			}

			for (const id of collection.ancestorIds) {
				uniqueAncestorIds.add(id);
			}
		}

		return uniqueAncestorIds;
	});
	const allCollectionIds = $derived([
		...gardenCollectionsIds,
		...ancestorCollectionsIds
	]);
	const allCultivarsQuery = $derived(
		useQuery(
			controller.triplit,
			controller.triplit
				.query('cultivars')
				.Where('collectionId', 'in', allCollectionIds)
		)
	);
	const allCultivars = $derived(allCultivarsQuery.results ?? []);
	const cultivarNames = $derived(
		new Set(allCultivars.map((cultivar) => cultivar.name))
	);

	/** Collects all resolves cultivar objects in the garden. */
	let cultivars: Set<Cultivar> = $state(new Set([]));
	$effect(() => {
		(async () => {
			if (cultivarNames.size === 0) {
				cultivars = new Set([]);
			}

			const promises: Promise<Cultivar | null>[] = [];
			cultivarNames.forEach((name) =>
				promises.push(resolveCultivar(garden.id, name, controller))
			);

			const results = await Promise.all(promises);

			return new Set(results.filter((cultivar) => cultivar !== null));
		})();
	});

	return {
		get cultivarNames() {
			return cultivarNames;
		},
		get cultivars() {
			return cultivars;
		}
	};
}
export type CultivarContext = ReturnType<typeof createCultivarContext>;
