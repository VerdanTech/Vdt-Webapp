import { fromDate, getLocalTimeZone } from '@internationalized/date';

import {
	AppError,
	type Cultivar,
	type DateRange,
	type Environment,
	rangesOverlap
} from '@vdg-webapp/models';

import type { FrostDatePlantingWindowsProfile } from '../cultivars/attributes/frostDatePlantingWindows/index.js';
import type { FrostDateProfile } from '../environments/attributes/frostDates/index.js';

export type PlantingWindow = {
	range: DateRange;
	/**
	 * A number from 0-1, where 0 indicates a plant should not be planted under any circumstances
	 * and a 1 indicates the optimal conditions for planting.
	 */
	suitability: number;
};

export type CultivarPlantingWindow = {
	cultivar: Cultivar;
	environment: Environment;
	/**
	 * All suitability outside of defined ranges is set to 0.
	 * Overlap of ranges is invalid.
	 */
	windows: Array<PlantingWindow>;
};

type PlantingWindowGenerationStrategy = 'frostDates' | 'meanWeeklyTemp';

export function calculatePlantingWindow(
	cultivar: Cultivar,
	environment: Environment,
	range: DateRange,
	strategy: PlantingWindowGenerationStrategy
): CultivarPlantingWindow {
	switch (strategy) {
		case 'frostDates':
			return calculatePlantingWindowFrostDates(cultivar, environment, range);
		case 'meanWeeklyTemp':
			return calculatePlantingWindowMeanWeeklyTemp(cultivar, environment, range);
		default:
			throw new AppError(
				'Unknown value of PlantingWindowGenerationStrategy within calculatePlantingWindow',
				{ nonFormErrors: ['Failed to generate a planting window.'] }
			);
	}
}

/**
 * Calculates the planting windows around the first and last frost date.
 * @param cultivar The cultivar to generate the windows with.
 * @param environment The environment to generate the windows with.
 * @param range The resulting windows are guaranteed to intersect with this range.
 * @returns A planting window around the first and last frost date for all years contained in the range.
 */
function calculatePlantingWindowFrostDates(
	cultivar: Cultivar,
	environment: Environment,
	range: DateRange
): CultivarPlantingWindow {
	const windows: PlantingWindow[] = [];

	/** Retrieve attributes. */
	const cultivarAttrs = cultivar.attributes as {
		frostDatePlantingWindows?: FrostDatePlantingWindowsProfile;
	} | null;
	const envAttrs = environment.attributes as { frostDates?: FrostDateProfile } | null;
	const firstWindowOpen = cultivarAttrs?.frostDatePlantingWindows?.firstFrostWindowOpen;
	const firstWindowClose =
		cultivarAttrs?.frostDatePlantingWindows?.firstFrostWindowClose;
	const firstFrostDate = envAttrs?.frostDates?.firstFrostDate;
	const lastWindowOpen = cultivarAttrs?.frostDatePlantingWindows?.lastFrostWindowOpen;
	const lastWindowClose = cultivarAttrs?.frostDatePlantingWindows?.lastFrostWindowClose;
	const lastFrostDate = envAttrs?.frostDates?.lastFrostDate;

	/** Get all years in the range. */
	const startYear = range.start.getUTCFullYear();
	const endYear = range.end.getUTCFullYear();

	/** For each year, calculate planting windows. */
	for (let year = startYear; year <= endYear; year++) {
		/** Add first frost window. */
		if (firstWindowOpen && firstWindowClose && firstFrostDate) {
			firstFrostDate.setUTCFullYear(year);
			const calendarDate = fromDate(firstFrostDate, getLocalTimeZone());
			const startDate = calendarDate.add({ days: firstWindowOpen });
			const endDate = calendarDate.add({ days: firstWindowClose });
			const windowRange: DateRange = {
				start: startDate.toDate(),
				end: endDate.toDate()
			};

			/** If resulting range intersects with the range, add it to the windows */
			if (rangesOverlap(range, windowRange)) {
				windows.push({ range: windowRange, suitability: 1 });
			}
		}
		/** Add last frost window. */
		if (lastWindowOpen && lastWindowClose && lastFrostDate) {
			lastFrostDate.setUTCFullYear(year);
			const calendarDate = fromDate(lastFrostDate, getLocalTimeZone());
			const startDate = calendarDate.add({ days: lastWindowOpen });
			const endDate = calendarDate.add({ days: lastWindowClose });
			const windowRange: DateRange = {
				start: startDate.toDate(),
				end: endDate.toDate()
			};

			/** If resulting range intersects with the range, add it to the windows */
			if (rangesOverlap(range, windowRange)) {
				windows.push({ range: windowRange, suitability: 1 });
			}
		}
	}

	return {
		cultivar,
		environment,
		windows
	};
}

function calculatePlantingWindowMeanWeeklyTemp(
	cultivar: Cultivar,
	environment: Environment,
	range: DateRange
): CultivarPlantingWindow {
	return {
		cultivar,
		environment,
		windows: []
	};
}
