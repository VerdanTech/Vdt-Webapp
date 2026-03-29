import {
	type FieldErrors,
	type Plant,
	type PlantUpdateCommand,
	plantFields
} from '@vdg-webapp/models';

import {
	type Item,
	TreeNumber,
	TreeString,
	fieldValid,
	toTreeBaseId,
	toTreeId
} from '$components';

import {
	type GeometryHistoryExtendHandler,
	type GeometryUpdateHandler
} from './geometry';
import { type LifespanUpdateHandler, lifespanTreeItem } from './lifespan';
import {
	type LocationHistoryExtendHandler,
	type LocationUpdateHandler
} from './locations';
import {
	type ObservationUpdateHandler,
	type ObservationDeleteHandler
} from './observation';

export type PlantUpdateHandler = (id: string, data: PlantUpdateCommand) => void;

export function plantTreeItem(
	value: { plant: Plant; workspaces: { id: string; name: string }[] },
	ctx: {
		plantUpdateHandler: PlantUpdateHandler;
		lifespanUpdateHandler: LifespanUpdateHandler;
		geometryUpdateHandler: GeometryUpdateHandler;
		locationUpdateHandler: LocationUpdateHandler;
		locationHistoryExtendHandler: LocationHistoryExtendHandler;
		geometryHistoryExtendHandler: GeometryHistoryExtendHandler;
		observationUpdateHandler: ObservationUpdateHandler;
		observationDeleteHandler: ObservationDeleteHandler;
		fieldErrors: FieldErrors;
	}
): Item {
	const baseId = toTreeBaseId('plant', value.plant.id);
	const cultivarNameId = toTreeId(baseId, 'cultivarName');
	const quantityId = toTreeId(baseId, 'quantity');

	const cultivarNameItem: Item = {
		id: cultivarNameId,
		label: 'Cultivar',
		description: plantFields.plantCultivarNameSchema.description,
		valueComponent: TreeString,
		value: value.plant.cultivarName,
		onChange: (newData: string) => {
			if (
				!fieldValid(
					cultivarNameId,
					newData,
					plantFields.plantCultivarNameSchema,
					ctx.fieldErrors
				)
			) {
				return;
			}
			ctx.plantUpdateHandler(value.plant.id, { cultivarName: newData });
		}
	};

	const quantityItem: Item = {
		id: quantityId,
		label: 'Quantity',
		description: plantFields.plantQuantitySchema.description,
		valueComponent: TreeNumber,
		value: value.plant.quantity,
		onChange: (newData: number) => {
			if (
				!fieldValid(
					quantityId,
					newData,
					plantFields.plantQuantitySchema,
					ctx.fieldErrors
				)
			) {
				return;
			}
			ctx.plantUpdateHandler(value.plant.id, { quantity: newData });
		}
	};

	const expectedLifespanItem = lifespanTreeItem(
		toTreeId(baseId, 'expectedLifespan'),
		'Expected Lifespan',
		{ lifespan: value.plant.expectedLifespan, workspaces: value.workspaces },
		{
			lifespanUpdateHandler: ctx.lifespanUpdateHandler,
			geometryUpdateHandler: ctx.geometryUpdateHandler,
			locationUpdateHandler: ctx.locationUpdateHandler,
			locationHistoryExtendHandler: ctx.locationHistoryExtendHandler,
			geometryHistoryExtendHandler: ctx.geometryHistoryExtendHandler,
			observationUpdateHandler: ctx.observationUpdateHandler,
			observationDeleteHandler: ctx.observationDeleteHandler,
			fieldErrors: ctx.fieldErrors
		}
	);

	const recordedLifespanItem = lifespanTreeItem(
		toTreeId(baseId, 'recordedLifespan'),
		'Recorded Lifespan',
		{ lifespan: value.plant.recordedLifespan, workspaces: value.workspaces },
		{
			lifespanUpdateHandler: ctx.lifespanUpdateHandler,
			geometryUpdateHandler: ctx.geometryUpdateHandler,
			locationUpdateHandler: ctx.locationUpdateHandler,
			locationHistoryExtendHandler: ctx.locationHistoryExtendHandler,
			geometryHistoryExtendHandler: ctx.geometryHistoryExtendHandler,
			observationUpdateHandler: ctx.observationUpdateHandler,
			observationDeleteHandler: ctx.observationDeleteHandler,
			fieldErrors: ctx.fieldErrors
		}
	);

	return {
		id: baseId,
		label: value.plant.cultivarName,
		children: [
			cultivarNameItem,
			quantityItem,
			expectedLifespanItem,
			recordedLifespanItem
		]
	};
}
