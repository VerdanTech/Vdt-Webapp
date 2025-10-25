import { useQuery } from '@triplit/svelte';
import { getContext, setContext } from 'svelte';

import type { ControllerContext } from '@vdg-webapp/models';

import type { GardenContext } from './gardenContext.svelte';

const cultivarContextKey = 'cultivarContext';

/**
 * Holds context for a garden's cultivar collections.
 */
export function createCultivarContext(
	controller: ControllerContext,
	garden: GardenContext
) {
	/** Queries all cultivar collections in the garden. */
	const gardenCollectionQuery = $derived(
		useQuery(
			controller.triplit,
			controller.triplit
				.query('cultivarCollections')
				.Where(['gardenId', '=', garden.id])
		)
	);
	/** Queries the parents of the cultivar collections. */
	const parentCollectionQuery = $derived.by(() => {
		const gardenCollectionParentIds: string[] =
			gardenCollectionQuery.results?.map((collection) => collection.parentId!) ?? [];

		return useQuery(
			controller.triplit,
			controller.triplit
				.query('cultivarCollections')
				.Where('id', 'in', gardenCollectionParentIds)
		);
	});
	/** Queries all applicable cultivar names within a garden. */
	const cultivarsNamesQuery = $derived.by(() => {
		const collections =
			gardenCollectionQuery.results?.concat(parentCollectionQuery.results ?? []) ?? [];
		const collectionIds = collections.map((collection) => collection.id);

		return useQuery(
			controller.triplit,
			controller.triplit.query('cultivars').Where('collectionId', 'in', collectionIds)
		);
	});
	const cultivarNames = $derived(new Set(cultivarsNamesQuery.results ?? []));

	return {
		gardenCollectionQuery,
		parentCollectionQuery,
		cultivarsNamesQuery,
		cultivarNames
	};
}
export type CultivarContext = ReturnType<typeof createCultivarContext>;

export function setCultivarContext(
	controller: ControllerContext,
	garden: GardenContext
) {
	return setContext(cultivarContextKey, createCultivarContext(controller, garden));
}

export function getCultivarContext() {
	return getContext<CultivarContext>(cultivarContextKey);
}
