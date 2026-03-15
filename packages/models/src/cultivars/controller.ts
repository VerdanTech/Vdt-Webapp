import { type ControllerContext } from '../controller.js';
import { AppError } from '../errors.js';
import { type Cultivar, type CultivarCollection } from '../index.js';
import { mergeAttributes } from '../utils/index.js';

const MAX_CULTIVAR_COLLECTION_INHERITANCE_DEPTH = 16;
const MAX_CULTIVAR_INHERITANCE_DEPTH = 16;

/** Stores an inheritance tree of cultivar collections. */
type CultivarCollectionInheritanceStructure = {
	collection: CultivarCollection;
	parent?: CultivarCollectionInheritanceStructure;
};
/**
 * Retrieves all cultivar collections in a garden.
 * Collections are retrieved into an inheritance structure
 * which stores each collection in the garden as well as
 * its parent, with a fixed inheritance depth limit.
 * @param gardenId Garden to retrieve collections in.
 * @param ctx Controller context.
 * @returns The cultivar collections inheritance structures.
 */
export async function resolveCultivarCollections(
	gardenId: string,
	ctx: ControllerContext
): Promise<CultivarCollectionInheritanceStructure[]> {
	/** Get all cultivar collections in the garden. */
	const gardenCollections = await ctx.triplit.fetch(
		ctx.triplit.query('cultivarCollections').Where(['gardenId', '=', gardenId])
	);
	if (gardenCollections.length == 0) {
		return [];
	}

	/** Iteratively retrieve all collections and their parents. */
	const collections: CultivarCollectionInheritanceStructure[] = [];
	for (const collection of gardenCollections) {
		const branchStructure: CultivarCollectionInheritanceStructure = { collection };

		let currentBranch = branchStructure;
		for (let i = 0; i < MAX_CULTIVAR_COLLECTION_INHERITANCE_DEPTH; i++) {
			if (!currentBranch.collection.parentId) {
				break;
			}
			const parentCollection = await ctx.triplit.fetchById(
				'cultivarCollections',
				currentBranch.collection.parentId
			);
			if (!parentCollection) {
				break;
			}

			currentBranch.parent = { collection: parentCollection };
			currentBranch = currentBranch.parent;
		}

		collections.push(branchStructure);
	}

	return collections;
}

/**
 * Given a cultivar name, retrieves the matching cultivar ID in the garden.
 * Cultivar collections within the garden are queried, along with their parent collections.
 * Collections are sorted by priority.
 * The first cultivar with a set of cultivar names which includes the target name
 * to be found in a search of each collection and all its parents is returned.
 * In the case that multiple cultivars which match a name exist in the same collection,
 * the one with the newest creation date is chosen.
 * @param gardenId The garden to search in.
 * @param cultivarName The cultivar name to search
 * @param ctx Controller context.
 * @returns The matching cultivar ID.
 */
export async function resolveCultivarName(
	gardenId: string,
	cultivarName: string,
	ctx: ControllerContext
): Promise<string | null> {
	/** Get all cultivar collections in the garden. */
	const collections = await resolveCultivarCollections(gardenId, ctx);
	if (collections.length == 0) {
		return null;
	}

	/** Sort collections by priority. */
	collections.sort((a, b) => a.collection.priority - b.collection.priority);

	/** Return first matched cultivar ID, starting with children. */
	for (const collection of collections) {
		let currentBranch: CultivarCollectionInheritanceStructure | undefined = collection;

		while (currentBranch) {
			const matchedCultivars = await ctx.triplit.fetch(
				ctx.triplit
					.query('cultivars')
					.Where('collectionId', '=', currentBranch.collection.id)
					.Where(['name', '=', cultivarName])
					.Select(['id', 'createdAt'])
			);
			if (matchedCultivars.length > 0) {
				if (matchedCultivars.length > 1) {
					/** Choose newest cultivar. */
					matchedCultivars.sort(
						(a, b) => b.createdAt.getTime() - a.createdAt.getTime()
					);
				}
				return matchedCultivars[0].id;
			}

			currentBranch = currentBranch.parent;
		}
	}

	return null;
}

/**
 * Given a cultivar ID, resolves the full cultivar object.
 * For cultivars without parents, this is a simple ID query.
 * For cultivars with parents, all cultivars in the inheritance tree
 * up to a fixed depth are retrieved, with child cultivar attributes
 * overriding parent attributes.
 * @param cultivarId The cultivar ID to resolve
 * @param ctx Controller context.
 * @returns The full cultivar object, with inherited attributes.
 */
async function resolveCultivarId(
	cultivarId: string,
	ctx: ControllerContext
): Promise<Cultivar | null> {
	/** Retrieve base cultivar. */
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
	for (let i = 0; i < MAX_CULTIVAR_INHERITANCE_DEPTH; i++) {
		parentCultivar = await ctx.triplit.fetchById('cultivars', parentCultivarId);
		if (parentCultivar) {
			cultivars.push(parentCultivar);

			if (parentCultivar.parentId) {
				parentCultivarId = parentCultivar.parentId;
			} else {
				break;
			}
		} else {
			break;
		}
	}

	/** Merge all cultivar values, letting children override parents. */
	let result = cultivars[cultivars.length - 1];
	for (let i = cultivars.length - 2; i >= 0; i--) {
		result = mergeAttributes(result, cultivars[i]);
	}
	return result;
}

/**
 * Given a cultivar name, resolve the full cultivar.
 * @param gardenId The garden to search.
 * @param cultivarName The cultivar name to match.
 * @param ctx Controller context.
 * @returns The full cultivar object, with inherited attributes.
 */
export async function resolveCultivar(
	gardenId: string,
	cultivarName: string,
	ctx: ControllerContext
): Promise<Cultivar | null> {
	const cultivarId = await resolveCultivarName(gardenId, cultivarName, ctx);
	if (!cultivarId) return null;

	return await resolveCultivarId(cultivarId, ctx);
}

/**
 * Retrieve all the cultivar names that are valid in a garden.
 * This includes all unique names among all collections and parents
 * of collections in the garden up to a fixed inheritance level.
 * @param gardenId Garden to retrieve names in.
 * @param maxCultivarCollectionInheritanceDepth The maximum
 * cultivar collection inheritance depth to support.
 * @param ctx Controller context.
 * @returns The cultivar names.
 */
export async function getAllCultivarNames(
	gardenId: string,
	ctx: ControllerContext
): Promise<string[]> {
	/** Get all cultivar collections in the garden. */
	const collections = await resolveCultivarCollections(gardenId, ctx);
	if (collections.length == 0) {
		return [];
	}

	/** Collect all collection IDs. */
	const collectionIds = new Set<string>();
	for (const collection of collections) {
		let currentBranch: CultivarCollectionInheritanceStructure | undefined = collection;

		while (currentBranch) {
			collectionIds.add(currentBranch.collection.id);
			currentBranch = currentBranch.parent;
		}
	}

	/** Collect all names. */
	const cultivars = await ctx.triplit.fetch(
		ctx.triplit
			.query('cultivars')
			.Where('collectionId', 'in', collectionIds)
			.Select(['name'])
	);
	const names = new Set<string>(cultivars.map((cultivar) => cultivar.name));

	return Array.from(names);
}
