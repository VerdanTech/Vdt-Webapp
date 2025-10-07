import { type ControllerContext } from '../controller.js';
import { AppError } from '../errors.js';
import {
	type Cultivar,
	type GeometryCreateCommand,
	GeometryHistoryCreateCommand,
	type GeometryUpdateCommand,
	type LocationCreateCommand,
	type LocationHistory,
	type LocationHistoryUpdateCommand,
	type LocationUpdateCommand,
	type PlantingAreaCreateCommand,
	type PlantingAreaUpdateCommand,
	type TriplitTransaction,
	type Workspace,
	type WorkspaceCreateCommand,
	type WorkspaceUpdateCommand,
	historySelectDay
} from '../index.js';
import { slugify } from '../utils/index.js';

//export async function getCultivarNamesInGarden(gardenId: string, ctx: ControllerContext): Promise<string[]> {

//}

/**
 * Retrieves a cultivar given a cultivar name.
 * 
 * Matches the cultivar name against like names, searching
 * through all collections owned by the garden plus their
 * parent collections.
 * 
 * If multiple cultivars are matched from different collections,
 * cultivars from child collections are preferred.
 * 
 * If multiple cultivars are matched from the same collection,
 * the newest of the cultivars is returned.
 * 
 * Cultivars are resolved to inherit parent attributes.
 * 
 * @param gardenId The ID of the garden to search.
 * @param cultivarName The cultivar namen to match.
 * @param max_cultivar_inheritance_depth The maximum
 * amount of cultivars to support inherited attributes for.
 * @param ctx Controller context.
 * @returns The matched cultivar.
 */
export async function resolveCultivarName(
	gardenId: string,
	cultivarName: string,
	max_cultivar_inheritance_depth: number,
	ctx: ControllerContext
): Promise<Cultivar | null> {
	/** Get all cultivar collections in the garden. */
	const gardenCollections = await ctx.triplit.fetch(
		ctx.triplit.query('cultivarCollections').Where(['gardenId', '=', gardenId])
	);
	if (gardenCollections.length == 0) {
		return null;
	}

	/** Get all the parent collections of the garden collections. */
	const parentCollectionIds = gardenCollections.map(
		(collection) => collection.parentId
	);
	const parentCollections = await ctx.triplit.fetch(
		ctx.triplit.query('cultivarCollections').Where(['id', 'in', parentCollectionIds])
	);

	/** Search over all garden collections and their parents. */
	let collections = gardenCollections.concat(parentCollections);
	const collectionIds = collections.map((collection) => collection.id);

	/** Get all cultivars with names that match the string. */
	let matchedCultivars = await ctx.triplit.fetch(
		ctx.triplit
			.query('cultivars')
			.Where(['collectionId', 'in', collectionIds])
			.Where(['names', 'like', cultivarName])
			.Select(['id', 'collectionId', 'createdAt'])
	);

	/** Return none or a single match. */
	if (matchedCultivars.length == 0) return null;
	if (matchedCultivars.length == 1)
		return await resolveCultivar(
			matchedCultivars[0].id,
			max_cultivar_inheritance_depth,
			ctx
		);

	/** Determine the cultivar collection with the highest priority. */
	const matchedCollectionIds = new Set(
		matchedCultivars.map((cultivar) => cultivar.collectionId)
	);
	const matchedCollections = collections.filter((collection) =>
		matchedCollectionIds.has(collection.id)
	);

	/** Let child collections override inherited collections. */
	const childCollections = matchedCollections.filter(
		(collection) => collection.parentId != null
	);
	collections = childCollections.length > 0 ? childCollections : matchedCollections;

	/** Prefer newer collections. */
	if (collections.length > 0) {
		collections.sort((a, b) => {
			return b.createdAt.getTime() - a.createdAt.getTime();
		});
	}
	const collectionId = collections[0].id;

	/** Retrieve subset of matched cultivars in the selected collection. */
	matchedCultivars = matchedCultivars.filter(
		(cultivar) => cultivar.collectionId == collectionId
	);
	if (matchedCultivars.length == 0) {
		throw new AppError('Failed to fetch cultivar - no match when one was expected.', {
			nonFormErrors: ['Failed to fetch cultivar.']
		});

		/** Prefer newer cultivars. */
	} else if (matchedCultivars.length > 1) {
		matchedCultivars.sort((a, b) => {
			return b.createdAt.getTime() - a.createdAt.getTime();
		});
	}

	return resolveCultivar(matchedCultivars[0].id, max_cultivar_inheritance_depth, ctx);
}

async function resolveCultivar(
	cultivarId: string,
	max_inheritence_depth: number,
	ctx: ControllerContext
): Promise<Cultivar | null> {
	/** Retrieve cultivar. */
	const cultivar = await ctx.triplit.fetchById('cultivars', cultivarId);
	if (cultivar == null) {
		throw new AppError('Failed to fetch cultivar - invalid ID.', {
			nonFormErrors: ['Failed to fetch cultivar.']
		});
	}

	if (cultivar.parentId == null) return cultivar;

	/** Gather cultivar and all parents in a list. */
	let cultivars = [cultivar];
	let parentCultivarId: string | null = cultivar.parentId;
	let parentCultivar: Cultivar | null = null;
	for (let i = 0; i < max_inheritence_depth; i++) {
		parentCultivar = await ctx.triplit.fetchById('cultivars', parentCultivarId);
		if (parentCultivar) {
			cultivars.push(parentCultivar);

			if (parentCultivar.parentId) {
				parentCultivarId = parentCultivar.parentId;
			}
		}

		if (!parentCultivar || !parentCultivar.parentId) {
			break;
		}
	}

	/** Merge all cultivar values, letting children override parents. */
	return cultivar;
}
