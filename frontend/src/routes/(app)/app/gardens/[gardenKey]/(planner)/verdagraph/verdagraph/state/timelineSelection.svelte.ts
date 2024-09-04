import { today, getLocalTimeZone } from '@internationalized/date';
import type { DateValue, DateDuration } from '@internationalized/date';

/** Consants. */
/** Default selected/focused day. */
const defaultFocusedDay: () => DateValue = () => today(getLocalTimeZone());
/** Default offset between selected day and upper and lower selection ranges. */
export const selectionOffset: DateDuration = { months: 1 };
/** Default offset between upper and lower selection and range displayed on the slider. */
export const sliderDisplayOffset: DateDuration = { months: 1 };
/** Minimum offset between the focused day and the selection bounds. */
export const minSelectOffset: DateDuration = { days: 1 };
/* Maximum offset between the focused day and the selection bounds. */
export const maxSelectOffset: DateDuration = { years: 4 };

export type TimelineSelection = {
	/** Controls the view of the Layout. */
	focusedDay: DateValue;
	/** Day which marks the start of the timeline selection. */
	beginSelectedDays: DateValue;
	/** Day which marks the end of the timeline selection. */
	endSelectedDays: DateValue;
	/** Day which marks the start of the timeline displayed on the slider graphic. */
	beginSliderDisplayedDays: DateValue;
	/** Day which marks the end of the timeline displayed on the slider graphic. */
	endSliderDisplayedDays: DateValue;
};

type SliderTickType = 'currentDay' | 'firstOfWeek' | 'firstOfMonth' | 'firstOfYear';

/** State. */
const focusedDay = defaultFocusedDay();
let _rune = $state<TimelineSelection>({
	focusedDay: focusedDay,
	beginSelectedDays: focusedDay.subtract(selectionOffset),
	endSelectedDays: focusedDay.add(selectionOffset),
	beginSliderDisplayedDays: focusedDay
		.subtract(selectionOffset)
		.subtract(sliderDisplayOffset),
	endSliderDisplayedDays: focusedDay.add(selectionOffset).add(sliderDisplayOffset)
});
/** The difference in days between the first and last slider displayed dates. */
let _numSliderDisplayedDays: number = $derived(
	calculateDeltaDays(_rune.endSliderDisplayedDays, _rune.beginSliderDisplayedDays)
);
//let _sliderDisplayedTickTypes: SliderTickType[] = $derived()

export const timelineSelection = {
	/** Getters. */
	get value(): TimelineSelection {
		return _rune;
	},
	get numSliderDisplayedDays(): number {
		return _numSliderDisplayedDays;
	},

	focusedDayOnValueChange(newFocusedDay: DateValue) {
		/* Calculate the difference between two dates in days.  */
		const deltaDays = calculateDeltaDays(newFocusedDay, _rune.focusedDay);

		/** Apply delta to selection range. */
		_rune.beginSelectedDays = _rune.beginSelectedDays.add({ days: deltaDays });
		_rune.endSelectedDays = _rune.endSelectedDays.add({ days: deltaDays });
		_rune.beginSliderDisplayedDays = _rune.beginSliderDisplayedDays.add({
			days: deltaDays
		});
		_rune.endSliderDisplayedDays = _rune.endSliderDisplayedDays.add({
			days: deltaDays
		});

		/** Update focused day. */
		_rune.focusedDay = newFocusedDay;
	},

	pushSelectionForward(translation: DateDuration) {
		_rune.focusedDay = _rune.focusedDay.add(translation);
		_rune.beginSelectedDays = _rune.beginSelectedDays.add(translation);
		_rune.endSelectedDays = _rune.endSelectedDays.add(translation);
		_rune.beginSliderDisplayedDays = _rune.beginSliderDisplayedDays.add(translation);
		_rune.endSliderDisplayedDays = _rune.endSliderDisplayedDays.add(translation);
	},

	pushSelectionBackward(translation: DateDuration) {
		_rune.focusedDay = _rune.focusedDay.subtract(translation);
		_rune.beginSelectedDays = _rune.beginSelectedDays.subtract(translation);
		_rune.endSelectedDays = _rune.endSelectedDays.subtract(translation);
		_rune.beginSliderDisplayedDays =
			_rune.beginSliderDisplayedDays.subtract(translation);
		_rune.endSliderDisplayedDays = _rune.endSliderDisplayedDays.subtract(translation);
	}
};
export default timelineSelection;

export function calculateDeltaDays(current: DateValue, prev: DateValue): number {
	const currentTimeMs = current.toDate(getLocalTimeZone());
	const prevTimeMs = prev.toDate(getLocalTimeZone());
	return Math.round(
		(currentTimeMs.getTime() - prevTimeMs.getTime()) / (1000 * 3600 * 24)
	);
}

export function dateToSliderDisplayIndex(date: DateValue): number {
	return calculateDeltaDays(date, timelineSelection.value.beginSliderDisplayedDays);
}

export function sliderDisplayIndexToDate(index: number): DateValue {
	return timelineSelection.value.beginSliderDisplayedDays.add({ days: index });
}
