import { QuerySubscription } from 'jazz-tools/svelte';

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
	const gardenCollectionsSub = $derived(
		new QuerySubscription(
			garden.id
				? controller.jazz.cultivarCollections.where({ gardenId: garden.id })
				: undefined
		)
	);
	const gardenCollections = $derived(gardenCollectionsSub.current ?? []);
	const gardenCollectionsIds = $derived(
		gardenCollections.map((collection) => collection.id)
	);

	const ancestorCollectionsIds = $derived.by(() => {
		const uniqueAncestorIds = new Set<string>();
		for (const collection of gardenCollections) {
			if (!collection.ancestorIds) continue;
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

	const allCultivarsSub = $derived(
		new QuerySubscription(
			allCollectionIds.length > 0
				? // eslint-disable-next-line @typescript-eslint/no-explicit-any
					controller.jazz.cultivars.where({
						collectionId: { in: allCollectionIds } as any
					})
				: undefined
		)
	);
	const allCultivars = $derived(allCultivarsSub.current ?? []);
	const cultivarNames = $derived(
		new Set(allCultivars.map((cultivar) => cultivar.name))
	);

	let cultivars: Set<Cultivar> = $state(new Set([]));
	$effect(() => {
		(async () => {
			if (cultivarNames.size === 0) {
				cultivars = new Set([]);
				return;
			}

			const promises: Promise<Cultivar | null>[] = [];
			cultivarNames.forEach((name) =>
				promises.push(resolveCultivar(garden.id, name, controller))
			);

			const results = await Promise.all(promises);
			cultivars = new Set(
				results.filter((cultivar): cultivar is Cultivar => cultivar !== null)
			);
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
