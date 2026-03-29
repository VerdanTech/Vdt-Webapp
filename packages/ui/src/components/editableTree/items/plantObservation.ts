import {
	type GenericObservation,
	PlantHarvestObservationId,
	type PlantHarvestObservationData
} from '@vdg-webapp/models';

import {
	type Item,
	TreeNumber,
	TreeString,
	TreeTextarea,
	toTreeId
} from '$components';

import type { ObservationDataItemsMap, ObservationUpdateHandler } from './observation';
import type { FieldErrors } from '@vdg-webapp/models';

/**
 * Builds tree items for the harvest observation's data fields.
 */
function harvestDataItems(
	itemId: string,
	observation: GenericObservation,
	ctx: {
		observationUpdateHandler: ObservationUpdateHandler;
		fieldErrors: FieldErrors;
	}
): Item[] {
	const data = (observation.data ?? {}) as PlantHarvestObservationData;

	const massId = toTreeId(itemId, 'mass');
	const qualityId = toTreeId(itemId, 'quality');
	const descriptionId = toTreeId(itemId, 'description');

	const massItem: Item = {
		id: massId,
		label: 'Mass (kg)',
		description: 'The mass of the harvest in kilograms.',
		valueComponent: TreeNumber,
		value: data?.mass ?? 0,
		onChange: (newData: number) => {
			ctx.observationUpdateHandler({
				id: observation.id,
				data: { ...data, mass: newData }
			});
		}
	};

	const qualityItem: Item = {
		id: qualityId,
		label: 'Quality',
		description: 'The quality of the harvest.',
		valueComponent: TreeString,
		value: data?.quality ?? '',
		onChange: (newData: string) => {
			ctx.observationUpdateHandler({
				id: observation.id,
				data: { ...data, quality: newData }
			});
		}
	};

	const descriptionItem: Item = {
		id: descriptionId,
		label: 'Description',
		description: 'Optional description of the harvest.',
		valueComponent: TreeTextarea,
		value: data?.description ?? '',
		onChange: (newData: string) => {
			ctx.observationUpdateHandler({
				id: observation.id,
				data: { ...data, description: newData }
			});
		}
	};

	return [massItem, qualityItem, descriptionItem];
}

/**
 * Mapping from plant observation types to their data items builders.
 * Only observation types with variant data fields need entries here.
 */
export const plantObservationDataItemsMap: ObservationDataItemsMap = {
	[PlantHarvestObservationId]: harvestDataItems
};
