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

/** The delta of each begin/end edge expansion step (see beginSelectionAtEdge/endSelectionAtEdge below). */
const edgeExpandStep: DateDuration = { days: 3 };

/** Which slider thumb, if any, is the one currently being dragged. */
type SliderDragMode = 'focus' | 'begin' | 'end' | null;

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
	/** Which slider thumb is currently being dragged, if any. Set by
	 * updateSlider while dragging, cleared by endDrag once the drag
	 * commits. Gates the two auto-expand mechanisms below so each only
	 * reacts to the thumb that's actually being dragged, rather than to
	 * whichever selection bound happens to sit at the slider's edge. */
	let dragMode: SliderDragMode = $state(null);

	/** Store whether the slider is close enough to the edge to move the range. */
	const translateSliderForward: boolean = $derived(
		dragMode === 'focus' && maxSliderValue - sliderValue[2] < translateRangeThreshold
	);
	const translateSliderBackward: boolean = $derived(
		dragMode === 'focus' && sliderValue[0] - minSliderValue < translateRangeThreshold
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

	/** Whether the begin/end selection thumb is pinned at the slider's
	 * displayed edge while actually being dragged. Growing beginSlider/
	 * endSlider alone (without also moving beginSelection/endSelection)
	 * would just push the selection off this pinned state after one tick,
	 * which is what the two effects below rely on to keep re-triggering
	 * continuously for as long as the thumb is genuinely held at the edge. */
	const beginSelectionAtEdge: boolean = $derived(
		dragMode === 'begin' && sliderValue[0] <= minSliderValue
	);
	const endSelectionAtEdge: boolean = $derived(
		dragMode === 'end' && sliderValue[2] >= maxSliderValue
	);
	let edgeExpandIntervalId: NodeJS.Timeout | null = null;
	$effect(() => {
		if (beginSelectionAtEdge) {
			if (edgeExpandIntervalId === null) {
				edgeExpandIntervalId = setInterval(() => {
					/** Move beginSelection together with beginSlider so the
					 * selection actually grows, not just the displayed range.
					 * focus and endSelection are untouched - they're their
					 * own independent state, not derived from beginSlider,
					 * so they stay anchored automatically. */
					beginSelection = beginSelection.subtract(edgeExpandStep);
					beginSlider = beginSlider.subtract(edgeExpandStep);
				}, translateRangeInterval);
			}
		} else {
			if (edgeExpandIntervalId) {
				clearInterval(edgeExpandIntervalId);
				edgeExpandIntervalId = null;
			}
		}
	});
	$effect(() => {
		if (endSelectionAtEdge) {
			if (edgeExpandIntervalId === null) {
				edgeExpandIntervalId = setInterval(() => {
					endSelection = endSelection.add(edgeExpandStep);
					endSlider = endSlider.add(edgeExpandStep);
				}, translateRangeInterval);
			}
		} else {
			if (edgeExpandIntervalId) {
				clearInterval(edgeExpandIntervalId);
				edgeExpandIntervalId = null;
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

		const isFocusDrag = newVal[1] != sliderValue[1];
		if (isFocusDrag) {
			dragMode = 'focus';
		} else if (newVal[0] != sliderValue[0]) {
			dragMode = 'begin';
		} else if (newVal[2] != sliderValue[2]) {
			dragMode = 'end';
		}

		/** Drag the selection along with the focus. */
		if (isFocusDrag) {
			let deltaDays = newVal[1] - sliderValue[1];
			/** Reduce the delta once, rather than clamping each endpoint
			 * independently, so the whole range translates together and
			 * stops at the boundary instead of shrinking. */
			if (newVal[0] + deltaDays < minSliderValue) {
				deltaDays = minSliderValue - newVal[0];
			}
			if (newVal[2] + deltaDays > maxSliderValue) {
				deltaDays = maxSliderValue - newVal[2];
			}
			newVal[0] = newVal[0] + deltaDays;
			newVal[1] = sliderValue[1] + deltaDays;
			newVal[2] = newVal[2] + deltaDays;
		}

		/** Update the selection. Once a begin/end thumb is pinned at the
		 * edge, beginSelectionAtEdge/endSelectionAtEdge take over growing
		 * that side continuously via their own interval - this just keeps
		 * committing whatever bits-ui reports for the thumb being dragged. */
		beginSelection = sliderValueToDateValue(newVal[0]);
		focus = sliderValueToDateValue(newVal[1]);
		endSelection = sliderValueToDateValue(newVal[2]);
	}

	/** Called when a slider drag ends (onValueCommit), so the edge-pinned
	 * auto-expand effects stop rather than continuing to run based on a
	 * stale dragMode from the last drag. */
	function endDrag() {
		dragMode = null;
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
		endDrag,
		disable,
		enable
	};
}
export type TimelineSelection = ReturnType<typeof createTimelineSelection>;
