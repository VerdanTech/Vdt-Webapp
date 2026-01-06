import { Tree } from 'melt/builders';

import { LocalStore, localStore } from '$state/localStore.svelte';

import { type TimelineSelection } from '../timeline';
import { type CalendarItem } from './types';

/** Calendar config persisted to local storage. */
export type ViewPanesOptions = 'plants' | 'plantingWindows' | 'actions';
export type CalendarConfig = {
	viewPanesSelect: ViewPanesOptions[];
	/** Height of the calendar sections in % of X pixels. */
	sectionHeight: number;
};

const DEFAULT_SECTION_HEIGHT = 64;

type CalendarPaneSpec = {
	entityType: string;
	items: () => CalendarItem[];
	defaultExpanded?: boolean;
};

/**
 * Holds context for the calendar.
 *
 * @param timeline Reference to the timeline selection.
 * @param entityTypes Creates a calendar pane for each type of entity.
 */
export function createCalendarContext<const EntityTypes extends readonly string[]>(
	timeline: TimelineSelection,
	paneSpecs: CalendarPaneSpec[]
) {
	type EntityType = EntityTypes[number];

	/** Persisted config. */
	let config = localStore<CalendarConfig>('verdagraphCalendarConfig', {
		viewPanesSelect: ['plants', 'plantingWindows'],
		sectionHeight: 100
	});

	/** Sub context. */
	const container = createCalendarContainerContext(timeline, config);

	/**
	 * Stores each of the panes in its own key.
	 */
	const panes: Record<EntityType, CalendarPaneContext> = Object.fromEntries(
		paneSpecs.map((pane) => [pane.entityType, createCalendarPaneContext(pane)])
	) as Record<EntityType, CalendarPaneContext>;

	/**
	 * Returns the selected entity IDs.
	 * @param entityType The type of entity to return the selection for.
	 * @returns The selected entity IDs.
	 */
	function getPane(entityType: EntityType): CalendarPaneContext {
		return panes[entityType];
	}

	return {
		/* Getters. */
		get config() {
			return config;
		},
		getPane,
		container,
		timeline,

		/** Setters. */
		set config(newVal) {
			if (newVal.value.viewPanesSelect.length <= 1) {
				return;
			}
			config = newVal;
		}
	};
}
export type CalendarContext<EntityTypes extends readonly string[]> = ReturnType<
	typeof createCalendarContext<EntityTypes>
>;

/**
 * Holds context for the calendar container characteristics.
 *
 * @param timeline Reference to the timeline selection.
 * @param config Reference to the configuration store.
 */
export function createCalendarContainerContext(
	timeline: TimelineSelection,
	config: LocalStore<CalendarConfig>
) {
	/** Calendar width in pixels. */
	let width: number = $state(0);
	/** The number of days in the selected range. */
	const numSections = $derived(timeline.sliderValue[2] - timeline.sliderValue[0]);
	/** The height of the sections in the calendar. */
	const sectionHeight = $derived(
		DEFAULT_SECTION_HEIGHT * (config.value.sectionHeight / 100)
	);
	/** Array representing the sections as they need to be rendered as ticks on the calendar. */
	const sections = $derived(
		Array.from({ length: numSections + 1 }, (_, index) => index)
	);

	return {
		/* Getters. */
		get width() {
			return width;
		},
		get numSections() {
			return numSections;
		},
		get sectionHeight() {
			return sectionHeight;
		},
		get sections() {
			return sections;
		},

		/** Setters. */
		set width(newVal) {
			width = newVal;
		}
	};
}
export type CalendarContainerContext = ReturnType<
	typeof createCalendarContainerContext
>;

/**
 * Holds context for each calendar pane.
 *
 * @param paneId The ID of the pane in the context.
 */
export function createCalendarPaneContext(spec: CalendarPaneSpec) {
	let height = $state(0);

	/** The Melt-UI builder. */
	const tree = new Tree({
		items: spec.items,
		expandOnClick: true,
		multiple: true
		//onSelectedChange: onSelectedChangeHandler
	});

	if (spec.defaultExpanded) {
		tree.expandAll();
	}

	return {
		/** Getters. */
		get height() {
			return height;
		},
		tree,

		/** Setters. */
		set height(newVal) {
			height = newVal;
		}
	};
}
export type CalendarPaneContext = ReturnType<typeof createCalendarPaneContext>;
