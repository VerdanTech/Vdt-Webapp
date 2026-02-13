import { type BulkInsert } from '@triplit/client';

import { schema } from '@vdg-webapp/models';

import { garden } from './garden';

const cultivarCollectionId = 'cultivar-collection';

export default function cultivarsSeed(): BulkInsert<typeof schema> {
	return {
		cultivarCollections: [
			{
				id: cultivarCollectionId,
				gardenId: garden.id,
				name: 'West Coast Seeds',
				slug: 'west-coast-seeds',
				visibility: 'HIDDEN'
			}
		],
		cultivars: [
			{
				collectionId: cultivarCollectionId,
				names: new Set(['Lettuce']),
				abbreviation: 'Le',
				attributes: {
					annualLifeCycle: {
						sowToGerm: 10,
						germToTransplant: 30,
						germToFirstHarvest: 120,
						firstToLastHarvest: 24
					},
					color: {
						baseColor: '#46A758',
						outlineColor: '#71D083',
						textColor: '#C2F0C2'
					},
					frostDatePlantingWindows: {
						firstFrostWindowOpen: 60,
						firstFrostWindowClose: 60,
						lastFrostWindowOpen: 60,
						lastFrostWindowClose: 60
					},
					origin: {
						transplantable: true
					},
					expectedGeometry: {
						geometryType: 'ELLIPSE',
						peakSize: 0.45,
						seedlingScaleFactor: 0.1,
						firstHarvestScaleFactor: 0.9,
						lastHarvestScaleFactor: 1,
						expiryScaleFactor: 1
					}
				}
			}
		]
	};
}
