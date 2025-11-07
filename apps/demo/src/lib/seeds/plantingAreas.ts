import { type BulkInsert } from '@triplit/client';

import { schema } from '@vdg-webapp/models';

import { addToDate } from '$lib/utils';

import { currentDay, earlyDate } from './dates';
import { garden } from './garden';
import { workspace } from './workspace';

export default function plantingAreasSeed(): BulkInsert<typeof schema> {
	return {
		plantingAreas: [
			{
				gardenId: garden.id,
				name: 'Cedar 1',
				geometryId: 'rectangle1',
				locationHistoryId: 'rectangle1',
				description: ''
			},
			{
				gardenId: garden.id,
				name: 'Cedar 2',
				geometryId: 'rectangle2',
				locationHistoryId: 'rectangle2',
				description: ''
			},
			{
				gardenId: garden.id,
				name: 'Metal 1',
				geometryId: 'ellipse1',
				locationHistoryId: 'ellipse1',
				description: ''
			},
			{
				gardenId: garden.id,
				name: 'Metal 2',
				geometryId: 'ellipse2',
				locationHistoryId: 'ellipse2',
				description: ''
			},
			{
				gardenId: garden.id,
				name: 'Hexagonal Pot',
				geometryId: 'polygon1',
				locationHistoryId: 'polygon1',
				description: ''
			},
			{
				gardenId: garden.id,
				name: 'Corner',
				geometryId: 'lines1',
				locationHistoryId: 'lines1',
				description: ''
			}
		],
		geometries: [
			{
				gardenId: garden.id,
				id: 'rectangle1',
				type: 'RECTANGLE',
				date: earlyDate,
				rectangleLength: 1,
				rectangleWidth: 1 + 1 / 2
			},
			{
				gardenId: garden.id,
				id: 'rectangle2',
				type: 'RECTANGLE',
				date: earlyDate,
				rectangleLength: 1,
				rectangleWidth: 1 + 1 / 2
			},
			{
				gardenId: garden.id,
				id: 'ellipse1',
				type: 'ELLIPSE',
				date: earlyDate,
				ellipseLength: 1,
				ellipseWidth: 1 + 1 / 2,
				rotation: 90
			},
			{
				gardenId: garden.id,
				id: 'ellipse2',
				type: 'ELLIPSE',
				date: earlyDate,
				ellipseLength: 1,
				ellipseWidth: 1 + 1 / 2
			},
			{
				gardenId: garden.id,
				id: 'polygon1',
				type: 'POLYGON',
				date: earlyDate,
				polygonNumSides: 6,
				polygonRadius: 1 / 4
			},
			{
				gardenId: garden.id,
				id: 'lines1',
				type: 'LINES',
				date: earlyDate,
				linesClosed: true,
				linesCoordinateIds: [
					'lines1coord1',
					'lines1coord2',
					'lines1coord3',
					'lines1coord4',
					'lines1coord5',
					'lines1coord6'
				]
			}
		],
		coordinates: [
			{
				gardenId: garden.id,
				id: 'lines1coord1',
				x: 0,
				y: 0
			},
			{
				gardenId: garden.id,
				id: 'lines1coord2',
				x: 0,
				y: 1
			},
			{
				gardenId: garden.id,
				id: 'lines1coord3',
				x: 1 / 2,
				y: 1
			},
			{
				gardenId: garden.id,
				id: 'lines1coord4',
				x: 1 / 2,
				y: 1 / 2
			},
			{
				gardenId: garden.id,
				id: 'lines1coord5',
				x: 1,
				y: 1 / 2
			},
			{
				gardenId: garden.id,
				id: 'lines1coord6',
				x: 1,
				y: 0
			}
		],
		locationHistories: [
			{
				gardenId: garden.id,
				workspaceIds: [workspace.id],
				id: 'rectangle1',
				locationIds: ['rectangle1pos1']
			},
			{
				gardenId: garden.id,
				workspaceIds: [workspace.id],
				id: 'rectangle2',
				locationIds: ['rectangle2pos1']
			},
			{
				gardenId: garden.id,
				workspaceIds: [workspace.id],
				id: 'ellipse1',
				locationIds: ['ellipse1pos1']
			},
			{
				gardenId: garden.id,
				workspaceIds: [workspace.id],
				id: 'ellipse2',
				locationIds: ['ellipse2pos1']
			},
			{
				gardenId: garden.id,
				workspaceIds: [workspace.id],
				id: 'polygon1',
				locationIds: ['polygon1pos1', 'polygon1pos2', 'polygon1pos3']
			},
			{
				gardenId: garden.id,
				workspaceIds: [workspace.id],
				id: 'lines1',
				locationIds: ['lines1pos1']
			}
		],
		locations: [
			{
				gardenId: garden.id,
				workspaceId: workspace.id,
				id: 'rectangle1pos1',
				date: earlyDate,
				x: 1 + 1 / 2,
				y: 3 + 1 / 2
			},
			{
				gardenId: garden.id,
				workspaceId: workspace.id,
				id: 'rectangle2pos1',
				date: earlyDate,
				x: 3,
				y: 3 + 1 / 2
			},
			{
				gardenId: garden.id,
				workspaceId: workspace.id,
				id: 'ellipse1pos1',
				date: earlyDate,
				x: 5,
				y: 4 + 1 / 2
			},
			{
				gardenId: garden.id,
				workspaceId: workspace.id,
				id: 'ellipse2pos1',
				date: earlyDate,
				x: 6 + 1 / 2,
				y: 3
			},
			{
				gardenId: garden.id,
				workspaceId: workspace.id,
				id: 'polygon1pos1',
				date: earlyDate,
				x: 4 + 1 / 2,
				y: 2
			},
			{
				gardenId: garden.id,
				workspaceId: workspace.id,
				id: 'polygon1pos2',
				date: addToDate(currentDay, -3),
				x: 4,
				y: 2
			},
			{
				gardenId: garden.id,
				workspaceId: workspace.id,
				id: 'polygon1pos3',
				date: addToDate(currentDay, 3),
				x: 6 + 1 / 2,
				y: 5
			},
			{
				gardenId: garden.id,
				workspaceId: workspace.id,
				id: 'lines1pos1',
				date: earlyDate,
				x: 1,
				y: 1
			}
		]
	};
}
