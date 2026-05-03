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
	const gardenCollections = await ctx.db.all(
		ctx.jazz.cultivarCollections.where({ gardenId })
	);
	if (gardenCollections.length === 0) {
		return [];
	}

	const collections: CultivarCollectionInheritanceStructure[] = [];
	for (const collection of gardenCollections) {
		const branchStructure: CultivarCollectionInheritanceStructure = { collection };

		let currentBranch = branchStructure;
		for (let i = 0; i < MAX_CULTIVAR_COLLECTION_INHERITANCE_DEPTH; i++) {
			if (!currentBranch.collection.parentId) break;
			const parentCollection = await ctx.db.one(
				ctx.jazz.cultivarCollections.where({ id: currentBranch.collection.parentId })
			);
			if (!parentCollection) break;

			currentBranch.parent = { collection: parentCollection };
			currentBranch = currentBranch.parent;
		}

		collections.push(branchStructure);
	}

	return collections;
}

/**
 * Given a cultivar name, retrieves the matching cultivar ID in the garden.
 * Collections are sorted by priority. The first matching cultivar found
 * in a depth-first search of each collection and its parents is returned.
 * When multiple cultivars share a name in the same collection, the newest is chosen.
 * @param gardenId The garden to search in.
 * @param cultivarName The cultivar name to search.
 * @param ctx Controller context.
 * @returns The matching cultivar ID, or null if not found.
 */
export async function resolveCultivarName(
	gardenId: string,
	cultivarName: string,
	ctx: ControllerContext
): Promise<string | null> {
	const collections = await resolveCultivarCollections(gardenId, ctx);
	if (collections.length === 0) return null;

	collections.sort((a, b) => a.collection.priority - b.collection.priority);

	for (const collection of collections) {
		let currentBranch: CultivarCollectionInheritanceStructure | undefined = collection;

		while (currentBranch) {
			const matchedCultivars = await ctx.db.all(
				ctx.jazz.cultivars.where({
					collectionId: currentBranch.collection.id,
					name: cultivarName
				})
			);
			if (matchedCultivars.length > 0) {
				if (matchedCultivars.length > 1) {
					matchedCultivars.sort(
						(a, b) => new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime()
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
 * Given a cultivar ID, resolves the full cultivar object with inherited attributes.
 * @param cultivarId The cultivar ID to resolve.
 * @param ctx Controller context.
 * @returns The full cultivar object, with inherited attributes.
 */
async function resolveCultivarId(
	cultivarId: string,
	ctx: ControllerContext
): Promise<Cultivar | null> {
	const cultivar = await ctx.db.one(ctx.jazz.cultivars.where({ id: cultivarId }));
	if (cultivar == null) {
		throw new AppError('Failed to fetch cultivar - invalid ID.', {
			nonFormErrors: ['Failed to fetch cultivar.']
		});
	}

	if (cultivar.parentId == null) return cultivar;

	const cultivars = [cultivar];
	let parentCultivarId: string | null = cultivar.parentId;
	for (let i = 0; i < MAX_CULTIVAR_INHERITANCE_DEPTH; i++) {
		if (!parentCultivarId) break;
		const parentCultivar: Cultivar | null = await ctx.db.one(
			ctx.jazz.cultivars.where({ id: parentCultivarId })
		);
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

	let result = cultivars[cultivars.length - 1];
	for (let i = cultivars.length - 2; i >= 0; i--) {
		result = mergeAttributes(result, cultivars[i]);
	}
	return result;
}

/**
 * Given a cultivar name, resolve the full cultivar object with inherited attributes.
 * @param gardenId The garden to search.
 * @param cultivarName The cultivar name to match.
 * @param ctx Controller context.
 * @returns The full cultivar object, or null if not found.
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
 * Retrieve all unique cultivar names that are valid in a garden.
 * @param gardenId Garden to retrieve names in.
 * @param ctx Controller context.
 * @returns The cultivar names.
 */
export async function getAllCultivarNames(
	gardenId: string,
	ctx: ControllerContext
): Promise<string[]> {
	const collections = await resolveCultivarCollections(gardenId, ctx);
	if (collections.length === 0) return [];

	const collectionIds = new Set<string>();
	for (const collection of collections) {
		let currentBranch: CultivarCollectionInheritanceStructure | undefined = collection;
		while (currentBranch) {
			collectionIds.add(currentBranch.collection.id);
			currentBranch = currentBranch.parent;
		}
	}

	const cultivarNames = new Set<string>();
	for (const collectionId of collectionIds) {
		const cultivars = await ctx.db.all(ctx.jazz.cultivars.where({ collectionId }));
		for (const cultivar of cultivars) cultivarNames.add(cultivar.name);
	}
	return [...cultivarNames];
}
