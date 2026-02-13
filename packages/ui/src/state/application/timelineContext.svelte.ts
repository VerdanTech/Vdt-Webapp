import { type DateDuration, getLocalTimeZone, today } from '@internationalized/date';

import { LocalStore } from '$state/localStore.svelte';

/** Default offset between selected day and the upper selection range. */
const defaultUpperSelectionOffset: DateDuration = { weeks: 3 };
/** Default offset between selected day lower selection range. */
const defaultLowerSelectionOffset: DateDuration = { weeks: 1 };

/**
 * Holds context for a timeline,
 * allowing queries to be scoped to
 * a selected date range.
 */
export function createTimelineContext() {
	const tz = getLocalTimeZone();
	const todayDate = today(tz);
	const startDate = todayDate.subtract(defaultLowerSelectionOffset);
	const endDate = todayDate.add(defaultUpperSelectionOffset);
	const beginSelection = new LocalStore<Date>(
		'timelineBeginSelection',
		startDate.toDate(tz)
	);
	const endSelection = new LocalStore<Date>('timelineEndSelection', endDate.toDate(tz));

	function reset() {
		const tz = getLocalTimeZone();
		const todayDate = today(tz);
		const startDate = todayDate.subtract(defaultLowerSelectionOffset);
		const endDate = todayDate.add(defaultUpperSelectionOffset);
		beginSelection.value = startDate.toDate(tz);
		endSelection.value = endDate.toDate(tz);
	}

	return {
		get beginSelection() {
			return beginSelection.value;
		},
		set beginSelection(newVal) {
			beginSelection.value = newVal;
		},
		get endSelection() {
			return endSelection.value;
		},
		set endSelection(newVal) {
			endSelection.value = newVal;
		},
		reset
	};
}
export type TimelineContext = ReturnType<typeof createTimelineContext>;
