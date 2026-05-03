import type { Geometry } from './schema.js';

/** Normalizes a Jazz timestamp (number | Date) to milliseconds since epoch. */
function toMs(date: Date | number): number {
	return typeof date === 'number' ? date : date.getTime();
}

/**
 * Checks whether two dates are on the same day or not.
 * Dates must be in the same timezone.
 * @param date1 The first date.
 * @param date2 The second date.
 * @returns If true, the two dates take place on the same day.
 */
export function isSameDay(date1: Date, date2: Date): boolean {
	return (
		date1.getFullYear() === date2.getFullYear() &&
		date1.getMonth() === date2.getMonth() &&
		date1.getDate() === date2.getDate()
	);
}

/**
 * Given a history, ex. a geometric or location history,
 * return the item at a given date.
 * Matching: The date need not be the exact date of an item, an item
 * is matched at a given date as long as it is before the next item.
 * @param items a list of items to search. Assumed to be unsorted.
 * @param date The date at which to retrieve the item at.
 * @param returnOriginalReferences If true, this function will return
 * a reference to the item in the list passed as an argument.
 * Using this reference will modify the original list.
 * @returns The item at the given date.
 */
export function historySelect<T extends { date: Date | number }>(
	items: Array<T>,
	date: Date,
	returnOriginalReferences: boolean
): T | null {
	if (returnOriginalReferences) {
		return historySelectReference(items, date);
	} else {
		return historySelectCopy(items, date);
	}
}

/**
 * Given a history, ex. a geometric or location history,
 * return the item at a given date.
 * Matching: The date need not be the exact date of an item, an item
 * is matched at a given date as long as it is before the next item.
 * @param items a list of items to search. Assumed to be unsorted.
 * @param date The date at which to retrieve the item at.
 * @returns The item at the given date.
 */
export function historySelectCopy<T extends { date: Date | number }>(
	items: Array<T>,
	date: Date
): T | null {
	if (items.length === 0) {
		return null;
	}

	const time = date.getTime();

	/** Sort items in ascending order. */
	const sortedItems = [...items].sort((a, b) => toMs(a.date) - toMs(b.date));

	/** If the requested date is before the earliest item, return null. */
	if (time < toMs(sortedItems[0].date)) {
		return null;
	}

	/** If the requested date is after the latest item, return the latest item. */
	if (time >= toMs(sortedItems[sortedItems.length - 1].date)) {
		return sortedItems[sortedItems.length - 1];
	}

	/** Find the item where the date falls between it and the next. */
	for (let i = 0; i < sortedItems.length - 1; i++) {
		const currentTime = toMs(sortedItems[i].date);
		const nextTime = toMs(sortedItems[i + 1].date);

		if (time >= currentTime && time < nextTime) {
			return sortedItems[i];
		}
	}

	/** Fallback to null. */
	return null;
}

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
export function historySelectReference<T extends { date: Date | number }>(
	items: Array<T>,
	date: Date
): T | null {
	if (items.length === 0) {
		return null;
	}

	const time = date.getTime();

	/** Build an array of indices and sort those indices by item date ascending.
	 *  Sorting indices preserves original item references. */
	const indices = [...items.keys()].sort(
		(a, b) => toMs(items[a].date) - toMs(items[b].date)
	);

	/** If the requested date is before the earliest item, return null. */
	if (time < toMs(items[indices[0]].date)) {
		return null;
	}

	/** If the requested date is after the latest item, return the latest item (original reference). */
	if (time >= toMs(items[indices[indices.length - 1]].date)) {
		return items[indices[indices.length - 1]];
	}

	/** Find the item where the date falls between it and the next. */
	for (let i = 0; i < indices.length - 1; i++) {
		const current = items[indices[i]];
		const currentTime = toMs(current.date);
		const nextTime = toMs(items[indices[i + 1]].date);

		if (time >= currentTime && time < nextTime) {
			return current;
		}
	}

	/** Fallback to null. */
	return null;
}

/**
 * Given a history, ex. a geometric or location history,
 * return the item at a given date.
 * An item will only be returned if one exists at the same
 * day as the given date.
 * @param items a list of items to search. Assumed to be unsorted.
 * @param date The date at which to retrieve the item at.
 * @returns The item at the given date.
 */
export function historySelectDay<T extends { date: Date | number }>(
	items: Array<T>,
	date: Date
): T | null {
	return [...items].find((item) => isSameDay(new Date(item.date), date)) || null;
}

/**
 * Given a history, ex. a geometric or location history,
 * find the two items with the lowest and highest date.
 * @param items a list of items to search. Assumed to be unsorted.
 * @returns The items at the minimum and maximum dates.
 */
export function historyGetRange<T extends { date: Date | number }>(
	items: Array<T> | null | undefined
): { min: T; max: T } | null {
	if (!items || items.length === 0) {
		return null;
	}

	return items.reduce(
		(acc, current) => ({
			min: toMs(current.date) < toMs(acc.min.date) ? current : acc.min,
			max: toMs(current.date) > toMs(acc.max.date) ? current : acc.max
		}),
		{ min: items[0], max: items[0] }
	);
}

/**
 * Given a geometry, returns the coordinate (in meters)
 * of its vertical extent, relative to the origin of the shape.
 * @param geometry The geometry to find the height for.
 * @returns The height, in meters, of the vertical extent of the shape.
 */
export function getGeometryHeight(
	geometry: Omit<Geometry, 'id' | 'gardenId' | 'linesCoordinateIds' | 'date'>
): number {
	switch (geometry.type) {
		case 'RECTANGLE':
			return (geometry.rectangleWidth / 2) * geometry.scaleFactor;

		case 'POLYGON':
			return geometry.polygonRadius * geometry.scaleFactor;

		case 'ELLIPSE':
			return (geometry.ellipseWidth / 2) * geometry.scaleFactor;

		case 'LINES':
			return (
				Math.max(
					...(geometry.linesCoordinates ?? []).map((coordinate) => coordinate.y)
				) * geometry.scaleFactor
			);
	}
}
