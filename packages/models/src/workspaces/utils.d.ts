import type { Geometry } from './schema.js';

/**
 * Checks whether two dates are on the same day or not.
 * Dates must be in the same timezone.
 * @param date1 The first date.
 * @param date2 The second date.
 * @returns If true, the two dates take place on the same day.
 */
export declare function isSameDay(date1: Date, date2: Date): boolean;
/**
 * Given a history, usually a geometric or location history,
 * return the item at a given date.
 * The date need not be the exact date of an item, an item
 * is considered valid at a given date as long as it is before
 * the next item.
 * @param items a list of items to search. Assumed to be unsorted.
 * @param date The date at which to retrieve the item at.
 * @param returnOriginalReferences If true, this function will return
 * a reference to the item in the list passed as an argument.
 * Using this reference will modify the original list.
 * @returns The item at the given date.
 */
export declare function historySelect<
	T extends {
		date: Date;
	}
>(items: Array<T>, date: Date, returnOriginalReferences: boolean): T | null;
/**
 * Given a history, usually a geometric or location history,
 * return the item at a given date.
 * The date need not be the exact date of an item, an item
 * is considered valid at a given date as long as it is before
 * the next item.
 * @param items a list of items to search. Assumed to be unsorted.
 * @param date The date at which to retrieve the item at.
 * @returns The item at the given date.
 */
export declare function historySelectCopy<
	T extends {
		date: Date;
	}
>(items: Array<T>, date: Date): T | null;
/**
 * Given a history, usually a geometric or location history,
 * return the item at a given date.
 * The date need not be the exact date of an item, an item
 * is considered valid at a given date as long as it is before
 * the next item.
 * This variant returns the actual item reference from the
 * original array so callers can mutate the returned object.
 * @param items a list of items to search. Assumed to be unsorted.
 * @param date The date at which to retrieve the item at.
 * @returns The item at the given date (reference into items) or null.
 */
export declare function historySelectReference<
	T extends {
		date: Date;
	}
>(items: Array<T>, date: Date): T | null;
/**
 * Given a history, usually a geometric or location history,
 * return the item at a given date.
 * An item will only be returned if one exists at the same
 * day as the given date.
 * @param items a list of items to search. Assumed to be unsorted.
 * @param date The date at which to retrieve the item at.
 * @returns The item at the given date.
 */
export declare function historySelectDay<
	T extends {
		date: Date;
	}
>(items: Array<T>, date: Date): T | null;
/**
 * Given a geometry, returns the coordinate (in meters)
 * of its vertical extent, relative to the origin of the shape.
 * @param geometry The geometry to find the height for.
 * @returns The height, in meters, of the vertical extent of the shape.
 */
export declare function getGeometryHeight(
	geometry: Omit<Geometry, 'id' | 'gardenId' | 'linesCoordinateIds' | 'date'>
): number;
//# sourceMappingURL=utils.d.ts.map
