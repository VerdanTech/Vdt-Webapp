import { type DateValue, fromDate, getLocalTimeZone } from '@internationalized/date';

import {
	type FieldErrors,
	type Location,
	type LocationHistory,
	type LocationUpdateCommand,
	type Position,
	workspaceFields
} from '@vdg-webapp/models';

import {
	type DynamicSelectValue,
	type Item,
	TreeAddButton,
	TreeCoordinate,
	TreeDate,
	TreeDeleteButton,
	TreeDynamicSelect,
	fieldValid,
	toTreeId
} from '..';

export type LocationUpdateHandler = (id: string, data: LocationUpdateCommand) => void;
export type LocationHistoryExtendHandler = (id: string) => void;

/**
 * Constructs an editable tree item for a location.
 * @param itemId The item ID of the returned tree item.
 * @param value Data required to construct the items.
 * @param options Options for how to construct the tree items.
 * @param ctx Tree context.
 * @returns The tree items that represent the location.
 */
export function locationTreeItem(
	itemId: string,
	value: {
		/** Location to represent. */
		location: Location;
		/**
		 * The workspaces the location may be located in.
		 * Required for changing the workspace of a location.
		 */
		workspaces: { id: string; name: string }[];
		/** Index of the location within the results. */
		index: number;
	},
	options: { includeDelete: boolean },
	ctx: { updateHandler: LocationUpdateHandler; fieldErrors: FieldErrors }
): Item {
	if (!value.location) {
		return {
			id: itemId,
			label: 'Failed to resolve location.'
		};
	}

	const dateId = toTreeId(itemId, 'date');
	const coordinateId = toTreeId(itemId, 'coordinate');
	const workspaceId = toTreeId(itemId, 'workspace');
	const deleteId = toTreeId(itemId, 'delete');

	const dateItem: Item = {
		id: dateId,
		label: 'Date',
		description: workspaceFields.locationDateSchema.description,
		valueComponent: TreeDate,
		value: fromDate(value.location.date, getLocalTimeZone()),
		onChange: (newData: DateValue) => {
			if (
				!fieldValid(
					dateId,
					newData,
					workspaceFields.locationDateSchema,
					ctx.fieldErrors
				)
			) {
				return;
			}
			ctx.updateHandler(value.location.id, {
				date: newData.toDate(getLocalTimeZone())
			});
		}
	};
	const coordinateItem: Item = {
		id: coordinateId,
		label: 'Position',
		description: workspaceFields.coordinateSchema.description,
		valueComponent: TreeCoordinate,
		value: { x: value.location.x, y: value.location.y },
		onChange: (newData: Position) => {
			if (
				!fieldValid(
					coordinateId,
					newData,
					workspaceFields.coordinateSchema,
					ctx.fieldErrors
				)
			) {
				return;
			}
			ctx.updateHandler(value.location.id, { coordinate: newData });
		}
	};
	const workspaceItem: Item = {
		id: workspaceId,
		label: 'Workspace',
		description: 'The workspace the location is located in.',
		valueComponent: TreeDynamicSelect,
		value: {
			id: value.location.workspaceId,
			options: value.workspaces.map((workspace) => {
				return { id: workspace.id, label: workspace.name };
			})
		},
		onChange: (newData: DynamicSelectValue) => {
			ctx.updateHandler(value.location.id, { workspaceId: newData.id });
		}
	};
	const deleteItem: Item = {
		id: deleteId,
		label: 'Delete',
		description: 'Deletes the geometry from the history.',
		valueComponent: TreeDeleteButton,
		value: undefined,
		onChange: () => {
			ctx.updateHandler(value.location.id, { delete: true });
		}
	};

	const children: Item[] = [dateItem, coordinateItem, workspaceItem];
	if (options.includeDelete) {
		children.push(deleteItem);
	}

	return {
		id: itemId,
		label: `Location ${value.index + 1}`,
		children: children
	};
}

/**
 * Constructs a tree item for a location history.
 * @param itemId The item ID of the returned tree item.
 * @param value Data required to construct the items.
 * @param ctx Tree context.
 * @returns The tree item.
 */
export function locationHistoryTreeItem(
	itemId: string,
	value: {
		locationHistory: LocationHistory | null | undefined;
		workspaces: { id: string; name: string }[];
	},
	ctx: {
		locationUpdateHandler: LocationUpdateHandler;
		locationHistoryExtendHandler: LocationHistoryExtendHandler;
		fieldErrors: FieldErrors;
	}
): Item {
	if (!value.locationHistory) {
		return {
			id: itemId,
			label: 'Failed to resolve locations.'
		};
	}

	const addLocationId = toTreeId(itemId, 'locationAdd');

	const locationItems = value.locationHistory.locations.map((location, index) => {
		const locationId = toTreeId(itemId, `locations[${index}]`);
		const numLocations = value.locationHistory?.locations.length;
		const includeDelete = numLocations && numLocations > 1 ? true : false;

		return locationTreeItem(
			locationId,
			{ location, workspaces: value.workspaces, index },
			{ includeDelete: includeDelete },
			{ updateHandler: ctx.locationUpdateHandler, fieldErrors: ctx.fieldErrors }
		);
	});

	const addLocationItem: Item = {
		id: addLocationId,
		label: 'Add',
		description: 'Adds a new location to the history.',
		valueComponent: TreeAddButton,
		value: undefined,
		/**
		 * The callback here is just used to register the add
		 * button has been pressed, so no need for data.
		 */
		onChange: () => {
			if (!value.locationHistory) {
				return;
			}

			ctx.locationHistoryExtendHandler(value.locationHistory.id);
		}
	};

	return {
		id: itemId,
		label: 'Locations',
		children: [...locationItems, addLocationItem]
	};
}
