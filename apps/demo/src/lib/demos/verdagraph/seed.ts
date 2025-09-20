import { type BulkInsert } from '@triplit/client';

import { schema } from '@vdg-webapp/models';

import { addToDate } from '$lib/utils';

import { user } from '../seed';

const earlyDate = new Date(2025, 1, 1);
const currentDay = new Date();

export const gardenId = 'garden';
export const workspaceId = 'workspace';
export default function seed(): BulkInsert<typeof schema> {
	return {
		profiles: [user.profile],
		accounts: [user.account],
		gardens: [
			{
				id: gardenId,
				name: 'Garden',
				visibility: 'PUBLIC',
				adminIds: [user.profile.id]
			}
		],
		workspaces: [
			{
				id: workspaceId,
				gardenId: gardenId,
				name: 'Workspace',
				slug: 'workspace'
			}
		],
		plantingAreas: [
			{
				gardenId: gardenId,
				name: 'Cedar 1',
				geometryId: 'rectangle1',
				locationHistoryId: 'rectangle1',
				description: ''
			},
			{
				gardenId: gardenId,
				name: 'Cedar 2',
				geometryId: 'rectangle2',
				locationHistoryId: 'rectangle2',
				description: ''
			},
			{
				gardenId: gardenId,
				name: 'Metal 1',
				geometryId: 'ellipse1',
				locationHistoryId: 'ellipse1',
				description: ''
			},
			{
				gardenId: gardenId,
				name: 'Metal 2',
				geometryId: 'ellipse2',
				locationHistoryId: 'ellipse2',
				description: ''
			},
			{
				gardenId: gardenId,
				name: 'Hexagonal Pot',
				geometryId: 'polygon1',
				locationHistoryId: 'polygon1',
				description: ''
			},
			{
				gardenId: gardenId,
				name: 'Corner',
				geometryId: 'lines1',
				locationHistoryId: 'lines1',
				description: ''
			}
		],
		geometries: [
			{
				gardenId: gardenId,
				id: 'rectangle1',
				type: 'RECTANGLE',
				date: earlyDate,
				rectangleLength: 1,
				rectangleWidth: 1 + 1 / 2
			},
			{
				gardenId: gardenId,
				id: 'rectangle2',
				type: 'RECTANGLE',
				date: earlyDate,
				rectangleLength: 1,
				rectangleWidth: 1 + 1 / 2
			},
			{
				gardenId: gardenId,
				id: 'ellipse1',
				type: 'ELLIPSE',
				date: earlyDate,
				ellipseLength: 1,
				ellipseWidth: 1 + 1 / 2,
				rotation: 90
			},
			{
				gardenId: gardenId,
				id: 'ellipse2',
				type: 'ELLIPSE',
				date: earlyDate,
				ellipseLength: 1,
				ellipseWidth: 1 + 1 / 2
			},
			{
				gardenId: gardenId,
				id: 'polygon1',
				type: 'POLYGON',
				date: earlyDate,
				polygonNumSides: 6,
				polygonRadius: 1 / 4
			},
			{
				gardenId: gardenId,
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
				gardenId: gardenId,
				id: 'lines1coord1',
				x: 0,
				y: 0
			},
			{
				gardenId: gardenId,
				id: 'lines1coord2',
				x: 0,
				y: 1
			},
			{
				gardenId: gardenId,
				id: 'lines1coord3',
				x: 1 / 2,
				y: 1
			},
			{
				gardenId: gardenId,
				id: 'lines1coord4',
				x: 1 / 2,
				y: 1 / 2
			},
			{
				gardenId: gardenId,
				id: 'lines1coord5',
				x: 1,
				y: 1 / 2
			},
			{
				gardenId: gardenId,
				id: 'lines1coord6',
				x: 1,
				y: 0
			}
		],
		locationHistories: [
			{
				gardenId: gardenId,
				workspaceIds: [workspaceId],
				id: 'rectangle1',
				locationIds: ['rectangle1pos1']
			},
			{
				gardenId: gardenId,
				workspaceIds: [workspaceId],
				id: 'rectangle2',
				locationIds: ['rectangle2pos1']
			},
			{
				gardenId: gardenId,
				workspaceIds: [workspaceId],
				id: 'ellipse1',
				locationIds: ['ellipse1pos1']
			},
			{
				gardenId: gardenId,
				workspaceIds: [workspaceId],
				id: 'ellipse2',
				locationIds: ['ellipse2pos1']
			},
			{
				gardenId: gardenId,
				workspaceIds: [workspaceId],
				id: 'polygon1',
				locationIds: ['polygon1pos1', 'polygon1pos2', 'polygon1pos3']
			},
			{
				gardenId: gardenId,
				workspaceIds: [workspaceId],
				id: 'lines1',
				locationIds: ['lines1pos1']
			}
		],
		locations: [
			{
				gardenId: gardenId,
				workspaceId: workspaceId,
				id: 'rectangle1pos1',
				date: earlyDate,
				x: 1 + 1 / 2,
				y: 3 + 1 / 2
			},
			{
				gardenId: gardenId,
				workspaceId: workspaceId,
				id: 'rectangle2pos1',
				date: earlyDate,
				x: 3,
				y: 3 + 1 / 2
			},
			{
				gardenId: gardenId,
				workspaceId: workspaceId,
				id: 'ellipse1pos1',
				date: earlyDate,
				x: 5,
				y: 4 + 1 / 2
			},
			{
				gardenId: gardenId,
				workspaceId: workspaceId,
				id: 'ellipse2pos1',
				date: earlyDate,
				x: 6 + 1 / 2,
				y: 3
			},
			{
				gardenId: gardenId,
				workspaceId: workspaceId,
				id: 'polygon1pos1',
				date: earlyDate,
				x: 4 + 1 / 2,
				y: 2
			},
			{
				gardenId: gardenId,
				workspaceId: workspaceId,
				id: 'polygon1pos2',
				date: addToDate(currentDay, -3),
				x: 4,
				y: 2
			},
			{
				gardenId: gardenId,
				workspaceId: workspaceId,
				id: 'polygon1pos3',
				date: addToDate(currentDay, 3),
				x: 6 + 1 / 2,
				y: 5
			},
			{
				gardenId: gardenId,
				workspaceId: workspaceId,
				id: 'lines1pos1',
				date: earlyDate,
				x: 1,
				y: 1
			}
		],
		cultivarCollections: [
			{
				id: "collection1",
				gardenId: gardenId,
				name: "West Coast Seeds",
				slug: "west-coast-seeds",
				visibility: "HIDDEN",
			}
		],
		cultivars: [
			{
				collectionId: "collection1",
				names: new Set(["Lettuce"]),
				abbreviation: "Le",
				attributes: {
					annualLifeCycle: {
						sowToGerm: 10,
						germToTransplant: 30,
						germToFirstHarvest: 120,
						firstToLastHarvest: 24
					},
					frostDatePlantingWindows: {
						firstFrostWindowOpen: 60,
						firstFrostWindowClose: 60,
						lastFrostWindowOpen: 60,
						lastFrostWindowClose: 60,
					},
					origin: {
						transplantable: true
					}
				}
			}
		]
	};
}
