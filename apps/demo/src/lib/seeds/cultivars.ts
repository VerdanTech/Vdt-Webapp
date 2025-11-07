import { type BulkInsert } from '@triplit/client';

import { schema } from '@vdg-webapp/models';

import { garden } from './garden';

export default function cultivarsSeed(): BulkInsert<typeof schema> {
	return {
		cultivarCollections: [
			{
				id: 'collection1',
				gardenId: garden.id,
				name: 'West Coast Seeds',
				slug: 'west-coast-seeds',
				visibility: 'HIDDEN'
			}
		],
		cultivars: [
			{
				collectionId: 'collection1',
				names: new Set(['Lettuce']),
				abbreviation: 'Le',
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
						lastFrostWindowClose: 60
					},
					origin: {
						transplantable: true
					}
				}
			}
		]
	};
}
