import { type BulkInsert } from '@triplit/client';

import { schema } from '@vdg-webapp/models';

import { garden } from './garden';

export default function plantsSeed(): BulkInsert<typeof schema> {
	return {
		plants: [
			{
				id: 'lettuce1',
				gardenId: garden.id,
				cultivarName: 'lettuce',
				cultivarAttributes: {},
				expectedLifespanId: 'lettuce1-expected',
				recordedLifespanId: 'lettuce1-recorded',
				beginDate: new Date(2026, 1, 1),
				endDate: new Date(2026, 12, 31)
			}
		],
		lifespans: [
			{
				id: 'lettuce1-expected',
				gardenId: garden.id,
				origin: 'DIRECT_SEED',
				geometryHistoryId: 'lettuce1-expected-geometry',
				locationHistoryId: 'lettuce1-expected-location'
			}
		],
		observations: [
			{
				id: 'lettuce1-obs1',
				gardenId: garden.id,
				type: 'plant-seed',
				entityIds: new Set(['lettuce1']),
				date: new Date(2026, 2, 1)
			}
		],
		geometryHistories: [],
		geometries: [],
		coordinates: [],
		locationHistories: [],
		locations: []
	};
}
