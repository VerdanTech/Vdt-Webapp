export type DateRange = {
	start: Date;
	end: Date;
};

/**
 * Finds the absolute start and end dates that bound an array of ranges.
 */
export function getBoundingDateRange(ranges: DateRange[]): DateRange | null {
	if (ranges.length === 0) return null;

	const minStart = Math.min(...ranges.map((r) => r.start.getTime()));
	const maxEnd = Math.max(...ranges.map((r) => r.end.getTime()));

	return {
		start: new Date(minStart),
		end: new Date(maxEnd)
	};
}
