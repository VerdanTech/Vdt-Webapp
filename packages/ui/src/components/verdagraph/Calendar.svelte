<script lang="ts">
	import { CalendarDate } from '@internationalized/date';
	import { mode } from 'mode-watcher';

	import type { Cultivar, Plant, PlantingWindow } from '@vdg-webapp/models';

	import { iconIds } from '$assets';
	import { RangeCalendar, createCalendarContext } from '$components';
	import {
		plantCalendarItem,
		plantingWindowCalendarItem
	} from '$components/rangeCalendar/items';
	import { getColor } from '$utils';

	import TestComponent from './TestComponent.svelte';
	import { getVerdagraphContext } from './verdagraphContext.svelte';

	const plants: { plant: Plant; cultivar: Cultivar }[] = [
		{
			plant: {
				id: 'plant1',
				gardenId: 'garden',
				cultivarName: 'tomato',
				cultivarAttributes: {},
				expectedLifespanId: '',
				recordedLifespanId: '',
				expectedLifespan: {
					id: 'plant1l1',
					gardenId: 'garden',
					origin: 'DIRECT_SEED',
					locationHistory: {
						id: 'oiraent',
						gardenId: 'gardeno',
						workspaceIds: new Set([]),
						locationIds: new Set([]),
						locations: []
					},
					geometryHistory: {
						id: 'rat',
						gardenId: 'gardeno',
						geometryIds: new Set([]),
						geometries: []
					},
					observations: [
						{
							id: '',
							gardenId: '',
							type: 'plant-seed',
							entityIds: new Set([]),
							date: new Date(2026, 0, 1),
							data: undefined
						},
						{
							id: 'rttsrtrst',
							gardenId: '',
							type: 'plant-germ',
							entityIds: new Set([]),
							date: new Date(2026, 0, 18),
							data: undefined
						}
					]
				},
				recordedLifespan: {
					id: 'plant2l1',
					gardenId: 'garden',
					origin: 'DIRECT_SEED',
					locationHistory: {
						id: 'rastars',
						gardenId: 'gardeno',
						workspaceIds: new Set([]),
						locationIds: new Set([]),
						locations: []
					},
					geometryHistory: {
						id: 'oiraarstrent',
						gardenId: 'gardeno',
						geometryIds: new Set([]),
						geometries: []
					},
					observations: [
						{
							id: '',
							gardenId: '',
							type: 'plant-seed',
							entityIds: new Set([]),
							date: new Date(2026, 0, 1),
							data: undefined
						},
						{
							id: 'rttsrtrst',
							gardenId: '',
							type: 'plant-germ',
							entityIds: new Set([]),
							date: new Date(2026, 0, 18),
							data: undefined
						}
					]
				},
				quantity: 1
			},
			cultivar: {
				id: 'cultivar',
				collectionId: '',
				names: new Set([]),
				abbreviation: 'a',
				description: '',
				attributes: {},
				createdAt: new Date()
			}
		}
	];
	const windows: PlantingWindow[] = [
		{
			cultivarName: 'tomato',
			cultivar: {
				id: 'cultivar',
				collectionId: '',
				names: new Set([]),
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
			windows: [{ start: new Date(2026, 0, 1), end: new Date(2026, 0, 6) }]
		}
	];

	const plantItems = $derived(
		plants
			.map((plant) =>
				plantCalendarItem({ plant: plant.plant, cultivar: plant.cultivar })
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
		{ entityType: 'plants', items: () => plantItems },
		{
			entityType: 'plantingWindows',
			items: () => plantingWindowItems
		},
		{ entityType: 'actions', items: () => [] }
	]);
</script>

<RangeCalendar timeline={verdagraphContext.timeline} context={calendarContext} />
