import { fromDate, getLocalTimeZone } from '@internationalized/date';
import { mode } from 'mode-watcher';

import { type CultivarPlantingWindow, getBoundingDateRange } from '@vdg-webapp/models';

import { getColor } from '$utils';

import type { CalendarItem } from '../types';

const defaultBaseColor = getColor('grass', 6, mode.current);
const defaultBorderColor = getColor('grass', 11, mode.current);
const defaultItemColor = getColor('grass', 8, mode.current);

export function plantingWindowCalendarItem(value: {
	plantingWindow: CultivarPlantingWindow;
}): CalendarItem | null {
	const ranges = value.plantingWindow.windows.map((window) => window.range) ?? [];
	if (!ranges) {
		return null;
	}
	console.log(ranges);
	const totalRange = getBoundingDateRange(ranges);
	if (!totalRange) {
		return null;
	}
	const startDate = fromDate(totalRange.start, getLocalTimeZone());
	const endDate = fromDate(totalRange.end, getLocalTimeZone());

	const fillColor =
		value.plantingWindow.cultivar.attributes.color?.baseColor || defaultBaseColor;
	const borderColor =
		value.plantingWindow.cultivar.attributes.color?.outlineColor || defaultBorderColor;
	const itemColor =
		value.plantingWindow.cultivar.attributes.color?.textColor || defaultItemColor;

	return {
		id: `${value.plantingWindow.cultivar.id}|${value.plantingWindow.environment.id}`,
		label: value.plantingWindow.cultivarName,
		labelOnly: false,
		description: '',
		startDate,
		endDate,
		fillColor,
		borderColor,
		itemColor,
		bottomMargin: 4
	};
}
