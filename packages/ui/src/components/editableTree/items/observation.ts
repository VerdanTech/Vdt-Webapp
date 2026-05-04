import { type DateValue, fromDate, getLocalTimeZone } from '@internationalized/date';

import {
	type FieldErrors,
	type GenericObservation,
	type ObservationUpdateCommand
} from '@vdg-webapp/models';

import { type Item, TreeDate, TreeDeleteButton, toTreeId } from '$components';

export type ObservationUpdateHandler = (data: ObservationUpdateCommand) => void;
export type ObservationDeleteHandler = (id: string) => void;

/**
 * A function which returns additional tree items for an observation's
 * variant data fields. This allows different observation types to define
 * their own editable data fields.
 */
export type ObservationDataItemsBuilder = (
	itemId: string,
	observation: GenericObservation,
	ctx: {
		observationUpdateHandler: ObservationUpdateHandler;
		fieldErrors: FieldErrors;
	}
) => Item[];

/**
 * A mapping from observation type to a function which returns
 * tree items for the observation's variant data fields.
 */
export type ObservationDataItemsMap = Record<string, ObservationDataItemsBuilder>;

/**
 * Constructs an editable tree item for a single observation.
 * @param itemId The item ID of the returned tree item.
 * @param value Data required to construct the items.
 * @param ctx Tree context.
 * @returns The tree item that represents the observation.
 */
export function observationTreeItem(
	itemId: string,
	value: {
		observation: GenericObservation;
		index: number;
		label: string;
		description?: string;
	},
	ctx: {
		observationUpdateHandler: ObservationUpdateHandler;
		observationDeleteHandler: ObservationDeleteHandler;
		dataItemsMap: ObservationDataItemsMap;
		fieldErrors: FieldErrors;
	}
): Item {
	const dateId = toTreeId(itemId, 'date');
	const deleteId = toTreeId(itemId, 'delete');

	const dateItem: Item = {
		id: dateId,
		label: 'Date',
		description: value.description,
		valueComponent: TreeDate,
		value: fromDate(value.observation.date, getLocalTimeZone()),
		onChange: (newData: DateValue) => {
			ctx.observationUpdateHandler({
				id: value.observation.id,
				date: newData.toDate(getLocalTimeZone())
			});
		}
	};

	const deleteItem: Item = {
		id: deleteId,
		label: 'Delete',
		description: 'Deletes this observation.',
		valueComponent: TreeDeleteButton,
		value: undefined,
		onChange: () => {
			ctx.observationDeleteHandler(value.observation.id);
		}
	};

	const children: Item[] = [dateItem];

	/** Build variant data items if a builder is registered for this observation type. */
	const dataItemsBuilder = ctx.dataItemsMap[value.observation.type];
	if (dataItemsBuilder) {
		const dataItems = dataItemsBuilder(itemId, value.observation, {
			observationUpdateHandler: ctx.observationUpdateHandler,
			fieldErrors: ctx.fieldErrors
		});
		children.push(...dataItems);
	}

	children.push(deleteItem);

	return {
		id: itemId,
		label: value.label,
		children: children
	};
}

/**
 * Constructs a tree item containing all observations.
 * @param itemId The item ID of the returned tree item.
 * @param value Data required to construct the items.
 * @param ctx Tree context.
 * @returns The tree item containing the observations list.
 */
export function observationsTreeItem(
	itemId: string,
	value: {
		observations: GenericObservation[] | null;
		labels: Record<string, string>;
		descriptions: Record<string, string>;
	},
	ctx: {
		observationUpdateHandler: ObservationUpdateHandler;
		observationDeleteHandler: ObservationDeleteHandler;
		dataItemsMap: ObservationDataItemsMap;
		fieldErrors: FieldErrors;
	}
): Item {
	if (!value.observations) {
		return {
			id: itemId,
			label: 'Failed to resolve observations.'
		};
	}

	const observationItems = value.observations.map((observation, index) => {
		const observationId = toTreeId(itemId, `observations[${index}]`);
		const label = value.labels[observation.type] ?? observation.type;
		const description = value.descriptions[observation.type];

		return observationTreeItem(
			observationId,
			{ observation, index, label, description },
			ctx
		);
	});

	return {
		id: itemId,
		label: 'Observations',
		children: observationItems
	};
}
