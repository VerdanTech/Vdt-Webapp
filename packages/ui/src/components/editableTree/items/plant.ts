import {
	type FieldErrors,
	type Plant,
	type PlantUpdateCommand,
	workspaceFields
} from '@vdg-webapp/models';

import {
	type Item,
	TreeDistance,
	TreeString,
	TreeTextarea,
	fieldValid,
	geometryTreeItem,
	locationHistoryTreeItem,
	toTreeBaseId,
	toTreeId
} from '$components';

import { type GeometryUpdateHandler } from './geometry';
import {
	type LocationHistoryExtendHandler,
	type LocationUpdateHandler
} from './locations';

export type PlantUpdateHandler = (id: string, data: PlantUpdateCommand) => void;

export function plantTreeItem(
	value: { plant: Plant; workspaces: { id: string; name: string }[] },
	ctx: {
		plantUpdateHandler: PlantUpdateHandler;
		geometryUpdateHandler: GeometryUpdateHandler;
		locationUpdateHandler: LocationUpdateHandler;
		locationHistoryExtendHandler: LocationHistoryExtendHandler;
		fieldErrors: FieldErrors;
	}
): Item {
	const baseId = toTreeBaseId('plant', value.plant.id);
	const cultivarNameId = toTreeId(baseId, 'cultivarName');
	const quantityId = toTreeId(baseId, 'quantity');
	const attributesId = toTreeId(baseId, 'attributes');

	const geometryItem = geometryTreeItem(
		toTreeId(baseId, 'geometry'),
		{ geometry: value.plantingArea.geometry, index: 0 },
		{
			includeIndex: false,
			includeDate: false,
			includeDelete: false,
			includeLinesClosed: false
		},
		{
			updateHandler: ctx.geometryUpdateHandler,
			fieldErrors: ctx.fieldErrors
		}
	);

	const locationHistoryItem = locationHistoryTreeItem(
		baseId,
		{
			locationHistory: value.plantingArea.locationHistory,
			workspaces: value.workspaces
		},
		{
			locationUpdateHandler: ctx.locationUpdateHandler,
			onLocationHistoryExtend: ctx.locationHistoryExtendHandler,
			fieldErrors: ctx.fieldErrors
		}
	);

	const nameItem: Item = {
		id: nameId,
		label: 'Name',
		description: workspaceFields.plantingAreaNameSchema.description,
		valueComponent: TreeString,
		value: value.plantingArea.name,
		onChange: (newData: string) => {
			if (
				!fieldValid(
					nameId,
					newData,
					workspaceFields.plantingAreaNameSchema,
					ctx.fieldErrors
				)
			) {
				return;
			}
			ctx.plantingAreaUpdateHandler(value.plantingArea.id, { name: newData });
		}
	};

	const descriptionItem: Item = {
		id: descriptionId,
		label: 'Description',
		description: workspaceFields.plantingAreaDescriptionSchema.description,
		valueComponent: TreeTextarea,
		value: value.plantingArea.description,
		onChange: (newData: string) => {
			if (
				!fieldValid(
					descriptionId,
					newData,
					workspaceFields.plantingAreaDescriptionSchema,
					ctx.fieldErrors
				)
			) {
				return;
			}
			ctx.plantingAreaUpdateHandler(value.plantingArea.id, {
				description: newData
			});
		}
	};

	const depthItem: Item = {
		id: depthId,
		label: 'Depth',
		description: workspaceFields.plantingAreaDepthSchema.description,
		valueComponent: TreeDistance,
		value: value.plantingArea.depth,
		onChange: (newData: number) => {
			if (
				!fieldValid(
					depthId,
					newData,
					workspaceFields.plantingAreaDepthSchema,
					ctx.fieldErrors
				)
			) {
				return;
			}
			ctx.plantingAreaUpdateHandler(value.plantingArea.id, { depth: newData });
		}
	};

	return {
		id: baseId,
		label: value.plantingArea.name,
		children: [
			nameItem,
			/** Details. */
			{
				id: toTreeId(baseId, 'details'),
				label: 'Details',
				children: [descriptionItem, depthItem]
			},
			geometryItem,
			locationHistoryItem
		]
	};
}
