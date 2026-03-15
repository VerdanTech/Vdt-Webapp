<script lang="ts">
	import { CalendarDate } from '@internationalized/date';
	import { mode } from 'mode-watcher';

	import type { Cultivar, CultivarPlantingWindow, Plant, PlantingWindow } from '@vdg-webapp/models';

	import { iconIds } from '$assets';
	import { RangeCalendar, createCalendarContext } from '$components';
	import {
		plantCalendarItem,
		plantingWindowCalendarItem
	} from '$components/rangeCalendar/items';
	import { getColor } from '$utils';

	import TestComponent from './TestComponent.svelte';
	import { getVerdagraphContext } from './verdagraphContext.svelte';

	import { getAppContext } from '$state';

	const ctx = getAppContext()

	const windows: CultivarPlantingWindow[] = [
		{
			cultivar: {
				id: 'cultivar',
				collectionId: '',
				name: '',
				abbreviation: 'a',
				description: '',
				attributes: {},
				createdAt: new Date()
			},
			environment: {
				id: '',
				name: '',
				gardenId: '',
				description: '',
				parentType: 'GARDEN',
				inherit: false,
				attributes: {}
			},
			windows: [
				{
					range: { start: new Date(2026, 0, 1), end: new Date(2026, 0, 6) }, suitability: 1
				}
			]
		}
	];
	const plantItems = $derived(
		ctx.plants.plants
		.map((plant) =>
		{
			return plantCalendarItem({ plant: plant, cultivar: ctx.plants.getCultivar(plant.cultivarName) })
		}
	)
	.filter((item) => item !== null)
);
	const plantingWindowItems = $derived(
		windows
			.map((window) => plantingWindowCalendarItem({ plantingWindow: window }))
			.filter((item) => item !== null)
	);

	const verdagraphContext = getVerdagraphContext();
	const calendarContext = createCalendarContext(verdagraphContext.timeline, [
		{ entityType: 'plants', items: () => plantItems, defaultExpanded: true },
		{
			entityType: 'plantingWindows',
			items: () => plantingWindowItems, defaultExpanded: true 
		},
		{ entityType: 'actions', items: () => [], defaultExpanded: true  }
	]);
</script>

<RangeCalendar timeline={verdagraphContext.timeline} context={calendarContext} />
