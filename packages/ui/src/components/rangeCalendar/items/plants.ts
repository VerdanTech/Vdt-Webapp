import { CalendarDate, fromDate, getLocalTimeZone } from '@internationalized/date';

import {
	type Cultivar,
	type FieldErrors,
	type Plant,
	historyGetRange,
	lifespanDates
} from '@vdg-webapp/models';

import type { CalendarItem } from '../types';

export function plantCalendarItem(
	value: { plant: Plant; cultivar: Cultivar },
	ctx: {
		fieldErrors: FieldErrors;
	}
): CalendarItem | null {
	const expectedLifespanDates = lifespanDates(value.plant.expectedLifespan);
	const recordedLifespanDates = lifespanDates(value.plant.recordedLifespan);
	const expectedRange = historyGetRange(expectedLifespanDates);
	const recordedRange = historyGetRange(recordedLifespanDates);
	let range: { min: Date | null; max: Date | null } = { min: null, max: null };
	if (expectedRange) {
		range.min = expectedRange.min.date;
		range.max = expectedRange.max.date;
	}
	if (recordedRange) {
		range.min = recordedRange.min.date;
		range.max = recordedRange.max.date;
	}

	if (!range.min || !range.max) return null;

	return {
		id: value.plant.id,
		label: value.plant.cultivarName,
		description: '',
		startDate: fromDate(range.min, getLocalTimeZone()),
		endDate: fromDate(range.max, getLocalTimeZone()),
		fillColor: value.cultivar.attributes.color?.baseColor,
		borderColor: value.cultivar.attributes.color?.outlineColor,
		itemColor: value.cultivar.attributes.color?.textColor
	};
}
