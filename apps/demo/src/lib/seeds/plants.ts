import { type BulkInsert } from '@triplit/client';

import { schema } from '@vdg-webapp/models';

import { garden } from './garden';
import { workspace } from './workspace';

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
			},
			{
				id: 'lettuce1-recorded',
				gardenId: garden.id,
				origin: 'DIRECT_SEED',
				geometryHistoryId: 'lettuce1-recorded-geometry',
				locationHistoryId: 'lettuce1-recorded-location'
			}
		],
		observations: [
			{
				id: 'lettuce1-obs1',
				gardenId: garden.id,
				type: 'plant-seed',
				entityIds: new Set(['lettuce1-expected']),
				date: new Date(2026, 2, 1)
			},
			{
				id: 'lettuce1-obs2',
				gardenId: garden.id,
				type: 'plant-expiry',
				entityIds: new Set(['lettuce1-expected']),
				date: new Date(2026, 6, 1)
			}
		],
		geometryHistories: [
			{
				id: 'lettuce1-expected-geometry',
				gardenId: garden.id,
				geometryIds: new Set([
					'lettuce1-expected-geometries1',
					'lettuce1-expected-geometries2',
					'lettuce1-expected-geometries3'
				])
			},
			{
				id: 'lettuce1-recorded-geometry',
				gardenId: garden.id,
				geometryIds: new Set([
				])
			}
		],
		geometries: [
			{
				id: 'lettuce1-expected-geometries1',
				gardenId: garden.id,
				type: 'ELLIPSE',
				date: new Date(2026, 1, 1),
				scaleFactor: 0.1,
				ellipseLength: 0.45,
				ellipseWidth: 0.45
			},
			{
				id: 'lettuce1-expected-geometries2',
				gardenId: garden.id,
				type: 'ELLIPSE',
				date: new Date(2026, 4, 1),
				scaleFactor: 0.5,
				ellipseLength: 0.45,
				ellipseWidth: 0.45
			},
			{
				id: 'lettuce1-expected-geometries3',
				gardenId: garden.id,
				type: 'ELLIPSE',
				date: new Date(2026, 9, 1),
				scaleFactor: 1,
				ellipseLength: 0.45,
				ellipseWidth: 0.45
			}
		],
		coordinates: [],
		locationHistories: [
			{
				id: 'lettuce1-expected-location',
				gardenId: garden.id,
				locationIds: new Set([
					'lettuce1-expected-locations1',
					'lettuce1-expected-locations2'
				]),
				workspaceIds: new Set([workspace.id])
			},
			{
				id: 'lettuce1-recorded-location',
				gardenId: garden.id,
				locationIds: new Set([
				]),
				workspaceIds: new Set([])
			}
		],
		locations: [
			{
				id: 'lettuce1-expected-locations1',
				gardenId: garden.id,
				workspaceId: workspace.id,
				x: 5,
				y: 5,
				date: new Date(2026, 1, 1)
			},
			{
				id: 'lettuce1-expected-locations2',
				gardenId: garden.id,
				workspaceId: workspace.id,
				x: -2,
				y: 8,
				date: new Date(2026, 6, 1)
			}
		]
	};
}
