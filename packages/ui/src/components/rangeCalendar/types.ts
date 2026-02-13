import { type DateValue } from '@internationalized/date';
import { type TreeItem } from 'melt/builders';
import { type Component } from 'svelte';

/**
 * Describes an indicator with custom popup located on a calendar item.
 * Any is necessary to allow us to pass anything to our popup components.
 */
// eslint-disable-next-line @typescript-eslint/no-explicit-any
export type CalendarItemInfoPoint<
	TProps extends Record<string, any> = Record<string, any>
> = {
	/** Label, visible beside info point. */
	label: string;
	/** Date of the point. */
	date: DateValue;
	/** Icon to display. Defaults to a circle. */
	icon?: string;
	/** Optional popup component. */
	popup?: Component<TProps>;
	popupProps?: TProps;
};

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function createInfoPoint<T extends Record<string, any>>(
	point: CalendarItemInfoPoint<T>
) {
	return point;
}

/** Describes a row on the calendar. */
export type CalendarItem = TreeItem & {
	id: string;
	/** Label, always visible at the top. */
	label: string;
	/** If true, the item height only is big enough for the label, no info points are displayed. */
	labelOnly: boolean;
	/** Optional description beside label. */
	description?: string;
	/** Start date the item is rendered at. */
	startDate: DateValue;
	/** End date the item is rendered at. Inclusive. */
	endDate: DateValue;
	/** Colors of the item. TODO: change to match naming in cultivar attributes. */
	fillColor: string;
	borderColor: string;
	itemColor: string;
	/** The number of pixels for the bottom margin when the item is collapsed. */
	bottomMargin: number;
	/** The number of pixels for the bottom margin when the item is expanded. */
	bottomMarginChild?: number;
	/** Classes to apply to the item when collapsed. */
	itemStyleCollapsed?: string;
	/** Classes to apply to the item when expanded. */
	itemStyleExpanded?: string;
	/** Info points located on the item. */
	// eslint-disable-next-line @typescript-eslint/no-explicit-any
	infoPoints?: CalendarItemInfoPoint<any>[];
	/** Optional children displayed under this one as a collapsible. */
	children?: CalendarItem[];
};
