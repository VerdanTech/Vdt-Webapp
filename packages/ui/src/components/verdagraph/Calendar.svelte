<script lang="ts">
	import { CalendarDate } from '@internationalized/date';
	import { mode } from 'mode-watcher';

	import { iconIds } from '$assets';
	import { RangeCalendar, createCalendarContext } from '$components';
	import { getColor } from '$utils';

	import { getVerdagraphContext } from './verdagraphContext.svelte';
	import TestComponent from './TestComponent.svelte';

	const verdagraphContext = getVerdagraphContext();
	const calendarContext = createCalendarContext(verdagraphContext.timeline, [
		{ entityType: 'plants', items: () => [] },
		{
			entityType: 'plantingWindows',
			items: () => {
				return [
					{
						id: '1',
						label: 'Tomato',
						description: 'Garden - Planting Window',
						startDate: new CalendarDate(2025, 5, 10),
						endDate: new CalendarDate(2025, 12, 30),
						fillColor: getColor('tomato', 4, mode.current),
						borderColor: getColor('tomato', 7, mode.current),
						itemColor: getColor('tomato', 5, mode.current),
						infoPoints: [
							{
								label: 'this is really a mf label yes haha',
								date: new CalendarDate(2025, 8, 25),
								icon: iconIds.cultivarsIcon,
								popup: TestComponent
							},
							{ label: 'also a label', date: new CalendarDate(2025, 8, 18) },
						]
					},
					{
						id: '2',
						label: 'Lettuce',
						description: 'Planting Windows',
						startDate: new CalendarDate(2025, 5, 20),
						endDate: new CalendarDate(2025, 12, 30),
						fillColor: getColor('grass', 4, mode.current),
						borderColor: getColor('grass', 7, mode.current),
						itemColor: getColor('grass', 5, mode.current),
						children: [
							{
								id: '2a',
								label: 'Lettuce',
								description: 'Garden - Planting Window',
								startDate: new CalendarDate(2025, 5, 20),
								endDate: new CalendarDate(2025, 12, 28),
								fillColor: getColor('green', 4, mode.current),
								borderColor: getColor('green', 7, mode.current),
								itemColor: getColor('green', 5, mode.current)
							},
							{
								id: '2b',
								label: 'Lettuce',
								description: 'Environment 2 - Planting Window',
								startDate: new CalendarDate(2025, 2, 22),
								endDate: new CalendarDate(2025, 8, 30),
								fillColor: getColor('lime', 4, mode.current),
								borderColor: getColor('lime', 7, mode.current),
								itemColor: getColor('lime', 5, mode.current)
							}
						]
					},
					{
						id: '3',
						label: 'Beet',
						description: 'Garden - Planting Window',
						startDate: new CalendarDate(2025, 2, 5),
						endDate: new CalendarDate(2025, 2, 23),
						fillColor: getColor('purple', 4, mode.current),
						borderColor: getColor('purple', 7, mode.current),
						itemColor: getColor('purple', 5, mode.current)
					}
				];
			}
		},
		{ entityType: 'actions', items: () => [] }
	]);
</script>

<RangeCalendar timeline={verdagraphContext.timeline} context={calendarContext} />
