import { type ControllerContext } from '../controller.js';
import { AppError } from '../errors.js';
import { type Cultivar, type CultivarCollection } from '../index.js';
import { mergeAttributes } from '../utils/index.js';

/** Stores an inheritance tree of cultivar collections. */
type CultivarCollectionInheritanceStructure = {
	collection: CultivarCollection;
	parent?: CultivarCollectionInheritanceStructure;
};
/**
 * Retrieves all cultivar collections in a garden.
 * @param gardenId Garden to retrieve collections in.
 * @param maxCultivarCollectionInheritanceDepth The maximum
 * cultivar collection inheritance depth to support.
 * @param ctx Controller context.
 * @returns The cultivar collections inheritance structures.
 */
export async function resolveCultivarCollections(
	gardenId: string,
	maxCultivarCollectionInheritanceDepth: number,
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
		for (let i = 0; i < maxCultivarCollectionInheritanceDepth; i++) {
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
 * @param gardenId The garden to search in.
 * @param cultivarName The cultivar name to search
 * @param maxCultivarCollectionInheritanceDepth The maximum
 * cultivar collection inheritance depth to support.
 * @param ctx Controller context.
 * @returns The matching cultivar ID.
 */
export async function resolveCultivarName(
	gardenId: string,
	cultivarName: string,
	maxCultivarCollectionInheritanceDepth: number,
	ctx: ControllerContext
): Promise<string | null> {
	/** Get all cultivar collections in the garden. */
	const collections = await resolveCultivarCollections(
		gardenId,
		maxCultivarCollectionInheritanceDepth,
		ctx
	);

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
					.Where(['names', 'has', cultivarName])
					.Select(['id', 'createdAt'])
			);
			if (matchedCultivars) {
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
 * @param cultivarId The cultivar ID to resolve
 * @param maxCultivarInheritanceDepth The maximum
 * cultivar inheritance depth to support.
 * @param ctx Controller context.
 * @returns The full cultivar object, with inherited attributes.
 */
async function resolveCultivarId(
	cultivarId: string,
	maxCultivarInheritanceDepth: number,
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
	for (let i = 0; i < maxCultivarInheritanceDepth; i++) {
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
 * @param maxCultivarCollectionInheritanceDepth The maximum
 * cultivar collection inheritance depth to support.
 * @param maxCultivarInheritanceDepth The maximum
 * cultivar inheritance depth to support.
 * @param ctx Controller context.
 * @returns The full cultivar object, with inherited attributes.
 */
export async function resolveCultivar(
	gardenId: string,
	cultivarName: string,
	maxCultivarCollectionInheritanceDepth: number,
	maxCultivarInheritanceDepth: number,
	ctx: ControllerContext
): Promise<Cultivar | null> {
	const cultivarId = await resolveCultivarName(
		gardenId,
		cultivarName,
		maxCultivarCollectionInheritanceDepth,
		ctx
	);
	if (!cultivarId) return null;

	return await resolveCultivarId(cultivarId, maxCultivarInheritanceDepth, ctx);
}
