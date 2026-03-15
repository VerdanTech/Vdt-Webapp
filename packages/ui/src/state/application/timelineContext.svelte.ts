import { type DateDuration, getLocalTimeZone, today } from '@internationalized/date';

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
	let beginSelection = $state(startDate.toDate(tz))
	let endSelection = $state(endDate.toDate(tz))

	function reset() {
		const tz = getLocalTimeZone();
		const todayDate = today(tz);
		const startDate = todayDate.subtract(defaultLowerSelectionOffset);
		const endDate = todayDate.add(defaultUpperSelectionOffset);
		beginSelection = startDate.toDate(tz);
		endSelection = endDate.toDate(tz);
	}

	return {
		get beginSelection() {
			return new Date(beginSelection);
		},
		set beginSelection(newVal) {
			beginSelection = newVal;
		},
		get endSelection() {
			return new Date(endSelection);
		},
		set endSelection(newVal) {
			endSelection= newVal;
		},
		reset
	};
}
export type TimelineContext = ReturnType<typeof createTimelineContext>;
