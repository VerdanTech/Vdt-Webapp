import type { Geometry, Location } from '../workspaces/schema.js';
import { historySelect } from '../workspaces/utils.js';
import type { Lifespan, Plant } from './schema.js';

export type LifespanSource = 'recorded' | 'expected';

/**
 * Wraps a value resolved from a plant's lifespan history
 * with the source lifespan it came from, so that callers
 * (e.g. update handlers) can target the correct history for mutations.
 */
export type Sourced<T> = {
	value: T;
	source: LifespanSource;
	lifespan: Lifespan;
};

/**
 * Resolves a value from a plant's lifespans using a selector function.
 * The recorded lifespan is checked first. If no value is found,
 * the expected lifespan is used as a fallback.
 * @param plant The plant whose lifespans to search.
 * @param selector A function that extracts a value from a lifespan,
 * returning null if the lifespan does not contain a match.
 * @returns The resolved value with its source lifespan, or null
 * if neither lifespan produced a match.
 */
function resolveFromLifespans<T>(
	plant: Plant,
	selector: (lifespan: Lifespan) => T | null
): Sourced<T> | null {
	if (plant.recordedLifespan) {
		const value = selector(plant.recordedLifespan);
		if (value) {
			return { value, source: 'recorded', lifespan: plant.recordedLifespan };
		}
	}

	if (plant.expectedLifespan) {
		const value = selector(plant.expectedLifespan);
		if (value) {
			return { value, source: 'expected', lifespan: plant.expectedLifespan };
		}
	}

	return null;
}

/**
 * Resolves the active location for a plant at a given point in time.
 * A plant may have both a recorded and expected lifespan, each with
 * its own location history. The recorded lifespan takes priority;
 * the expected lifespan is used as a fallback.
 * @param plant The plant to resolve the location for.
 * @param focusDate The point in time to resolve the location at.
 * @returns The location with its source lifespan, or null if no
 * location exists at the given time in either lifespan.
 */
export function resolveActiveLocation(
	plant: Plant,
	focusDate: Date
): Sourced<Location> | null {
	return resolveFromLifespans(plant, (lifespan) => {
		if (!lifespan.locationHistory) {
			return null;
		}
		return historySelect(lifespan.locationHistory.locations ?? [], focusDate, false);
	});
}

/**
 * Resolves the active geometry for a plant at a given point in time.
 * A plant may have both a recorded and expected lifespan, each with
 * its own geometry history. The recorded lifespan takes priority;
 * the expected lifespan is used as a fallback.
 * @param plant The plant to resolve the geometry for.
 * @param focusDate The point in time to resolve the geometry at.
 * @returns The geometry with its source lifespan, or null if no
 * geometry exists at the given time in either lifespan.
 */
export function resolveActiveGeometry(
	plant: Plant,
	focusDate: Date
): Sourced<Geometry> | null {
	return resolveFromLifespans(plant, (lifespan) => {
		if (!lifespan.geometryHistory) {
			return null;
		}
		return historySelect(lifespan.geometryHistory.geometries ?? [], focusDate, false);
	});
}
