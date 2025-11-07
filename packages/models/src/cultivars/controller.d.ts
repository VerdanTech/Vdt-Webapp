import { type ControllerContext } from '../controller.js';
import { type Cultivar, type CultivarCollection } from '../index.js';

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
export declare function resolveCultivarCollections(
	gardenId: string,
	maxCultivarCollectionInheritanceDepth: number,
	ctx: ControllerContext
): Promise<CultivarCollectionInheritanceStructure[]>;
/**
 * Given a cultivar name, retrieves the matching cultivar ID in the garden.
 * @param gardenId The garden to search in.
 * @param cultivarName The cultivar name to search
 * @param maxCultivarCollectionInheritanceDepth The maximum
 * cultivar collection inheritance depth to support.
 * @param ctx Controller context.
 * @returns The matching cultivar ID.
 */
export declare function resolveCultivarName(
	gardenId: string,
	cultivarName: string,
	maxCultivarCollectionInheritanceDepth: number,
	ctx: ControllerContext
): Promise<string | null>;
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
export declare function resolveCultivar(
	gardenId: string,
	cultivarName: string,
	maxCultivarCollectionInheritanceDepth: number,
	maxCultivarInheritanceDepth: number,
	ctx: ControllerContext
): Promise<Cultivar | null>;
export {};
//# sourceMappingURL=controller.d.ts.map
