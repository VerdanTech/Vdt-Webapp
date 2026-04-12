import type { Geometry, GeometryHistory, Location, LocationHistory } from '../workspaces/schema.js';
import { historySelect } from '../workspaces/utils.js';
import type { Lifespan, Plant } from './schema.js';

export type LifespanSource = 'recorded' | 'expected';

/**
 * A lifespan with its related histories pre-loaded by the caller.
 * The base Lifespan type only carries FK IDs; callers that need
 * history data must fetch and pass it explicitly.
 */
export type LifespanWithHistories = Lifespan & {
	locationHistory: (LocationHistory & { locations: Location[] }) | null;
	geometryHistory: (GeometryHistory & { geometries: Geometry[] }) | null;
};

/**
 * A plant with its related lifespans pre-loaded by the caller.
 */
export type PlantWithLifespans = Plant & {
	recordedLifespan: LifespanWithHistories | null;
	expectedLifespan: LifespanWithHistories | null;
};

/**
 * Wraps a value resolved from a plant's lifespan history
 * with the source lifespan it came from, so that callers
 * (e.g. update handlers) can target the correct history for mutations.
 */
export type Sourced<T> = {
	value: T;
	source: LifespanSource;
	lifespan: LifespanWithHistories;
};

function resolveFromLifespans<T>(
	plant: PlantWithLifespans,
	selector: (lifespan: LifespanWithHistories) => T | null
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
 * Recorded lifespan takes priority; expected lifespan is the fallback.
 */
export function resolveActiveLocation(
	plant: PlantWithLifespans,
	focusDate: Date
): Sourced<Location> | null {
	return resolveFromLifespans(plant, (lifespan) => {
		if (!lifespan.locationHistory) return null;
		return historySelect(lifespan.locationHistory.locations, focusDate, false);
	});
}

/**
 * Resolves the active geometry for a plant at a given point in time.
 * Recorded lifespan takes priority; expected lifespan is the fallback.
 */
export function resolveActiveGeometry(
	plant: PlantWithLifespans,
	focusDate: Date
): Sourced<Geometry> | null {
	return resolveFromLifespans(plant, (lifespan) => {
		if (!lifespan.geometryHistory) return null;
		return historySelect(lifespan.geometryHistory.geometries, focusDate, false);
	});
}
