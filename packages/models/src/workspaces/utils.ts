import type { Geometry } from './schema.js';

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
export function historySelect<T extends { date: Date }>(
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
export function historySelectCopy<T extends { date: Date }>(
	items: Array<T>,
	date: Date
): T | null {
	if (items.length === 0) {
		return null;
	}

	const time = date.getTime();

	/** Sort items in ascending order. */
	const sortedItems = [...items].sort((a, b) => a.date.getTime() - b.date.getTime());

	/** If the requested date is before the earliest item, return null. */
	if (time < sortedItems[0].date.getTime()) {
		return null;
	}

	/** If the requested date is after the latest item, return the latest item. */
	if (time >= sortedItems[sortedItems.length - 1].date.getTime()) {
		return sortedItems[sortedItems.length - 1];
	}

	/** Find the item where the date falls between it and the next. */
	for (let i = 0; i < sortedItems.length - 1; i++) {
		const currentTime = sortedItems[i].date.getTime();
		const nextTime = sortedItems[i + 1].date.getTime();

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
export function historySelectReference<T extends { date: Date }>(
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
		(a, b) => items[a].date.getTime() - items[b].date.getTime()
	);

	/** If the requested date is before the earliest item, return null. */
	if (time < items[indices[0]].date.getTime()) {
		return null;
	}

	/** If the requested date is after the latest item, return the latest item (original reference). */
	if (time >= items[indices[indices.length - 1]].date.getTime()) {
		return items[indices[indices.length - 1]];
	}

	/** Find the item where the date falls between it and the next. */
	for (let i = 0; i < indices.length - 1; i++) {
		const current = items[indices[i]];
		const currentTime = current.date.getTime();
		const nextTime = items[indices[i + 1]].date.getTime();

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
export function historySelectDay<T extends { date: Date }>(
	items: Array<T>,
	date: Date
): T | null {
	return [...items].find((item) => isSameDay(item.date, date)) || null;
}

/**
 * Given a history, ex. a geometric or location history,
 * find the two items with the lowest and highest date.
 * @param items a list of items to search. Assumed to be unsorted.
 * @returns The items at the minimum and maximum dates.
 */
export function historyGetRange<T extends { date: Date }>(
	items: Array<T> | null | undefined
): { min: T; max: T } | null {
	if (!items || items.length === 0) {
		return null;
	}

	return items.reduce(
		(acc, current) => ({
			min: current.date < acc.min.date ? current : acc.min,
			max: current.date > acc.max.date ? current : acc.max
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
	geometry: Geometry
): number {
	switch (geometry.attributes.type) {
		case 'RECTANGLE':
			return (geometry.attributes.rectangleWidth / 2) * geometry.scaleFactor;

		case 'POLYGON':
			return geometry.attributes.polygonRadius * geometry.scaleFactor;

		case 'ELLIPSE':
			return (geometry.attributes.ellipseWidth / 2) * geometry.scaleFactor;

		case 'LINES':
			return (
				Math.max(...geometry.attributes.linesCoordinates.map((coordinate) => coordinate.y)) *
				geometry.scaleFactor
			);
	}
}
