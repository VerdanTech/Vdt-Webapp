import { type DateValue } from '@internationalized/date';
import { type TreeItem } from 'melt/builders';
import { type Component } from 'svelte';

/** Describes an indicator with custom popup located on a calendar item. */
export type CalendarItemInfoPoint = {
	label: string;
	date: DateValue;
	icon?: string;
	popup?: Component;
};

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
	/** Colors of the item. */
	fillColor: string;
	borderColor: string;
	itemColor: string;
	/** The number of pixels for the bottom margin when the item is collapsed. */
	bottomMargin: number;
	/** The number of pixels for the bottom margin when the item is expanded. */
	bottomMarginChild?: number;
	/** Whether to round and allow border for item sides. */
	//border?: 'full' | 'top' | 'bottom' | 'middle' ;
	/** Info points located on the item. */
	infoPoints?: CalendarItemInfoPoint[];
	/** Optional children displayed under this one as a collapsible. */
	children?: CalendarItem[];
};
