/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import type { CultivarCollectionCreateCommandGardenRef } from './cultivarCollectionCreateCommandGardenRef';
import type { CultivarCollectionCreateCommandParentRef } from './cultivarCollectionCreateCommandParentRef';
import type { CultivarCollectionCreateCommandVisibility } from './cultivarCollectionCreateCommandVisibility';

export interface CultivarCollectionCreateCommand {
	/**
	 * The description of the collection.Must be at most 1400 characters
	 * @maxLength 1400
	 */
	description?: string;
	garden_ref?: CultivarCollectionCreateCommandGardenRef;
	/**
	 * The name of the collection.Must be between 3 and 50 characters long and contain only alphanumeric characters, spaces, hyphens, and underscores.
	 * @minLength 3
	 * @maxLength 50
	 * @pattern [0-9A-Za-z _-]+
	 */
	name: string;
	parent_ref?: CultivarCollectionCreateCommandParentRef;
	/**
	 * A set of metadata tags.Each tag must be at most 150 characters and contain only alphanumeric characters and spaces. There may be at most 150 tags
	 * @maxLength 150
	 */
	tags?: string[];
	visibility?: CultivarCollectionCreateCommandVisibility;
}
