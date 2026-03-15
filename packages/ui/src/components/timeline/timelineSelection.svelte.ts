import {
	type DateDuration,
	type DateValue,
	fromDate,
	getLocalTimeZone,
	today
} from '@internationalized/date';

import { type TimelineContext } from '$state/application/timelineContext.svelte';

import { calculateDeltaDays, calendarDateToUtc } from './utils';

/** Default offset between upper and lower selection and range displayed on the slider. */
const defaultSliderDisplayOffset: DateDuration = {
	weeks: 2
};
/** Minimum offset between the focused day and the selection bounds. */
const minSelectOffset: DateDuration = { days: 1 };
/* Maximum offset between the focused day and the selection bounds. */
const maxSelectOffset: DateDuration = { years: 4 };

/**
 * The number of days the slider needs to be within the minimum or
 * maximum bounds before the slider range will be translated. */
const translateRangeThreshold = 2;
/** The number of miliseconds between range translations. */
const translateRangeInterval = 50;
/** The delta of each range translation. */
const forwardTranslateRange = { days: 3 };
const backwardTranslateRange = { days: -1 };

export function createTimelineSelection(timeline: TimelineContext) {
	/**
	 * Selection.
	 */
	/** Used to prevent changes, for example when an object is being moved around. */
	let disabled = $state(false);
	/** Controls the view of the Layout. */
	let focus: DateValue = $state(today(getLocalTimeZone()));
	/** 
	 * Day which marks the start of the timeline selection.
	 * the TimelineContext uses native JS dates to match the database, 
	 * whereas this component uses @internationalized/date dates for proper display.
	 */
	let beginSelection: DateValue = $state(
		fromDate(timeline.beginSelection, getLocalTimeZone())
	);
	/** Day which marks the end of the timeline selection. */
	let endSelection: DateValue = $state(
		fromDate(timeline.endSelection, getLocalTimeZone())
	);

	/** Update the timeline context. */
	$effect(() => {
		timeline.beginSelection = beginSelection.toDate(getLocalTimeZone());
	});
	$effect(() => {
		timeline.endSelection = endSelection.toDate(getLocalTimeZone());
	});

	/** Derived selection. */
	const focusUtc: Date = $derived(calendarDateToUtc(focus));
	//const beginSelectionUtc: Date = $derived(calendarDateToUtc(beginSelection));
	//const endSelectionUtc: Date = $derived(calendarDateToUtc(endSelection));

	/**
	 * Slider properties.
	 */
	/** Day which marks the start of the timeline displayed on the slider graphic. */
	let beginSlider: DateValue = $state(
		beginSelection.subtract(defaultSliderDisplayOffset)
	);
	/** Day which marks the end of the timeline displayed on the slider graphic. */
	let endSlider: DateValue = $state(endSelection.add(defaultSliderDisplayOffset));
	/** The value the slider starts with. Is a reference point for other values. */
	const minSliderValue = 0;
	/** The last value in the slider. Defines the end of the visible range. */
	const maxSliderValue = $derived(calculateDeltaDays(endSlider, beginSlider));
	/** The slider index value corresponding to the beginning of the timeline selection */
	//const beginSelectionValue = $derived(calculateDeltaDays(beginSelection, beginSlider))
	//const endSelectionValue = $derived(maxSliderValue - calculateDeltaDays(endSlider, endSelection))
	/** The values of the slider thumbs. */
	const sliderValue: Array<number> = $derived.by(() => {
		return [
			calculateDeltaDays(beginSelection, beginSlider),
			calculateDeltaDays(focus, beginSlider),
			calculateDeltaDays(endSelection, beginSlider)
		];
	});
	/** Store whether the slider is close enough to the edge to move the range. */
	const translateSliderForward: boolean = $derived(
		maxSliderValue - sliderValue[2] < translateRangeThreshold
	);
	const translateSliderBackward: boolean = $derived(
		sliderValue[0] - minSliderValue < translateRangeThreshold
	);
	let sliderExpandIntervalId: NodeJS.Timeout | null = null;
	$effect(() => {
		if (translateSliderForward) {
			if (sliderExpandIntervalId === null) {
				sliderExpandIntervalId = setInterval(() => {
					translate(forwardTranslateRange);
				}, translateRangeInterval);
			}
		} else {
			if (sliderExpandIntervalId) {
				clearInterval(sliderExpandIntervalId);
				sliderExpandIntervalId = null;
			}
		}
	});
	$effect(() => {
		if (translateSliderBackward) {
			if (sliderExpandIntervalId === null) {
				sliderExpandIntervalId = setInterval(() => {
					translate(backwardTranslateRange);
				}, translateRangeInterval);
			}
		} else {
			if (sliderExpandIntervalId) {
				clearInterval(sliderExpandIntervalId);
				sliderExpandIntervalId = null;
			}
		}
	});

	/**
	 * Resets the selection to the default.
	 */
	function reset() {
		if (disabled) {
			return;
		}

		timeline.reset();
		focus = today(getLocalTimeZone());
		beginSelection = fromDate(timeline.beginSelection, getLocalTimeZone());
		endSelection = fromDate(timeline.endSelection, getLocalTimeZone());
		beginSlider = beginSelection.subtract(defaultSliderDisplayOffset);
		endSlider = endSelection.add(defaultSliderDisplayOffset);
	}

	/**
	 * Resets the slider range back to the default.
	 */
	function resetSliderRange() {
		if (disabled) {
			return;
		}

		beginSlider = beginSelection.subtract(defaultSliderDisplayOffset);
		endSlider = endSelection.add(defaultSliderDisplayOffset);
	}

	/**
	 * Given a change in the focused day, move the selection along with it.
	 * @param newFocus The new focused day.
	 */
	function refocus(newFocus: DateValue) {
		if (disabled) {
			return;
		}

		/* Calculate the difference between two focused dates in days.  */
		const deltaDays = calculateDeltaDays(newFocus, focus);

		/** Apply delta to selection range. */
		beginSelection = beginSelection.add({
			days: deltaDays
		});
		endSelection = endSelection.add({
			days: deltaDays
		});
		beginSlider = beginSlider.add({
			days: deltaDays
		});
		endSlider = endSlider.add({
			days: deltaDays
		});

		/** Update focused day. */
		focus = newFocus;
	}

	/**
	 * Given a change in the begin selection date, move the slider range
	 * along with it if the new begin selection day surpasses it.
	 * @param newBeginSelection The new begin selection date.
	 */
	function changeBeginSelection(newBeginSelection: DateValue) {
		if (disabled) {
			return;
		}

		beginSelection = newBeginSelection;

		if (beginSlider > beginSelection) {
			beginSlider = beginSelection.subtract(defaultSliderDisplayOffset);
		}
	}

	/**
	 * Given a change in the end selection date, move the slider range
	 * along with it if the new end selection day surpasses it.
	 * @param newEndSelection The new end selection date.
	 */
	function changeEndSelection(newEndSelection: DateValue) {
		if (disabled) {
			return;
		}

		endSelection = newEndSelection;

		if (endSelection > endSlider) {
			endSlider = endSelection.add(defaultSliderDisplayOffset);
		}
	}

	/**
	 * Move the entire selection according to the translation.
	 * @param translation The time duration to translate the selection
	 */
	function translate(translation: DateDuration) {
		if (disabled) {
			return;
		}

		focus = focus.add(translation);
		beginSelection = beginSelection.add(translation);
		endSelection = endSelection.add(translation);
		beginSlider = beginSlider.add(translation);
		endSlider = endSlider.add(translation);
	}

	/**
	 * Given a slider thumb value, converts it to the equivalent DateValue
	 * @param sliderValue The slider value to convert.
	 * @returns The equivalent DateValue
	 */
	function sliderValueToDateValue(sliderValue: number): DateValue {
		return beginSlider.add({ days: sliderValue });
	}

	/**
	 * Updates the selection based on a change in the slider.
	 * @param newVal The new slider value.
	 */
	function updateSlider(newVal: number[]) {
		if (disabled) {
			return;
		}

		/** Drag the selection along with the focus. */
		if (newVal[1] != sliderValue[1]) {
			const deltaDays = newVal[1] - sliderValue[1];
			newVal[0] = Math.max(newVal[0] + deltaDays, minSliderValue);
			newVal[2] = Math.min(newVal[2] + deltaDays, maxSliderValue);
		}

		/** Update the selection. */
		beginSelection = sliderValueToDateValue(newVal[0]);
		focus = sliderValueToDateValue(newVal[1]);
		endSelection = sliderValueToDateValue(newVal[2]);
	}

	function disable() {
		disabled = true;
	}

	function enable() {
		disabled = false;
	}

	return {
		get focus() {
			return focus;
		},
		get beginSelection() {
			return beginSelection;
		},
		get endSelection() {
			return endSelection;
		},
		get focusUtc() {
			return focusUtc;
		},
		/** 
		get beginSelectionUtc() {
			return beginSelectionUtc;
		},
		get endSelectionUtc() {
			return endSelectionUtc;
		},
		*/
		get minSliderValue() {
			return minSliderValue;
		},
		get maxSliderValue() {
			return maxSliderValue;
		},
		get sliderValue() {
			return sliderValue;
		},
		get disabled() {
			return disabled;
		},
		minSelectOffset,
		maxSelectOffset,
		reset,
		resetSliderRange,
		refocus,
		changeBeginSelection,
		changeEndSelection,
		translate,
		sliderValueToDateValue,
		updateSlider,
		disable,
		enable
	};
}
export type TimelineSelection = ReturnType<typeof createTimelineSelection>;
