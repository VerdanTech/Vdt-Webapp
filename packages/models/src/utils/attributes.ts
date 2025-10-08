/**
 * Determines if a value is an Object for the purposes
 * of implementing deeply nested per-attribute merge.
 * @param value The value to check.
 * @returns If true, the value is an Object and has keys.
 */
function isObjectType(value: any): boolean {
	return value !== null && typeof value === 'object' && !Array.isArray(value);
}

/**
 * Using a set of parent attributes as a base
 * that is overwritten by a set of child attributes,
 * produces the resulting attributes.
 * @param parent The inherited-from attributes that
 * is being overwritten by the child attributes.
 * @param child The child that is inheriting attributes.
 * @returns The resulting attributes.
 */
export function mergeAttributes(parent: any, child: any): any {
	/** Inherit unset attributes. */
	if (child === undefined || child === null) {
		return parent;
	}

	/** If the child is an object (has keys that nest into the next layer), continue. */
	if (!isObjectType(child)) {
		return child;
	}

	/** Start with the parent attributes. */
	const result: Record<string, any> = isObjectType(parent) ? { ...parent } : {};

	/** Loop over all child keys. */
	for (const key of Object.keys(child)) {
		/** Skip unset attributes. */
		const childValue = child[key];
		if (childValue === undefined || childValue === null) {
			continue;
		}

		/** If both values are objects, nest the merge. */
		if (isObjectType(childValue) && isObjectType(result[key])) {
			result[key] = mergeAttributes(result[key], childValue);

			/** Otherwise child attributes override. */
		} else {
			result[key] = childValue;
		}
	}
	return result;
}
