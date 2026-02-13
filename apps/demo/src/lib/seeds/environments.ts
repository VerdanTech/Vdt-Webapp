import { type BulkInsert } from '@triplit/client';

import { type Environment, schema } from '@vdg-webapp/models';

import { garden } from './garden';

export const environment: Environment = {
	id: 'garden-environment',
	name: 'Garden',
	description: '',
	parentType: 'GARDEN',
	gardenId: garden.id,
	inherit: true,
	attributes: {
		frostDates: {
			lastFrostDate: new Date(2020, 4, 1),
			firstFrostDate: new Date(2020, 11, 1)
		},
		annualTemperature: {
			minimum: -10,
			maximum: 10
		}
	}
};

export default function environmentSeed(): BulkInsert<typeof schema> {
	return {
		environments: [environment]
	};
}
