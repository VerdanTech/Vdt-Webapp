import {
    plantFields,
    type FieldErrors,
    type Lifespan,
    type LifespanUpdateCommand,
    type Origin,
    OriginEnumLabels,
    PlantObservationLabels,
    PlantObservationDescriptions
} from '@vdg-webapp/models';

import {
    type DynamicSelectValue,
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

import { type GeometryUpdateHandler, type GeometryHistoryExtendHandler, geometryHistoryTreeItem } from './geometry';
import {
    type LocationHistoryExtendHandler,
    type LocationUpdateHandler
} from './locations';
import {
    type ObservationUpdateHandler,
    type ObservationDeleteHandler,
    observationsTreeItem
} from './observation';
import { plantObservationDataItemsMap } from './plantObservation';
import DynamicSelect from '../attributes/DynamicSelect.svelte';

export type LifespanUpdateHandler = (
    id: string,
    data: LifespanUpdateCommand
) => void;

export function lifespanTreeItem(
    itemId: string,
    itemLabel: string,
    value: { lifespan: Lifespan | null, workspaces: { id: string; name: string }[] },
    ctx: {
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
	if (!value.lifespan) {
		return {
			id: itemId,
			label: 'Failed to resolve lifespan.'
		};
	}

    const originId = toTreeId(itemId, 'origin');
    const geometryHistoryId = toTreeId(itemId, 'geometryHistory');
    const locationHistoryId = toTreeId(itemId, 'locationHistory');
    const observationsId = toTreeId(itemId, 'observations');

    const originItem: Item = {
        id: originId,
        label: 'Origin',
        description: plantFields.lifespanOriginSchema.description,
        valueComponent: DynamicSelect,
        value: {id: value.lifespan.origin, 
            options: Object.entries(OriginEnumLabels).map(
                ([id, label]) => ({ id, label })
                )
        },
        onChange: (newData: DynamicSelectValue) => {
            if (value.lifespan) {
                ctx.lifespanUpdateHandler(value.lifespan.id, { origin: newData.id as Origin });
            }
        }
    } 

    const geometryHistoryItem = geometryHistoryTreeItem(
        geometryHistoryId,
        { geometryHistory: value.lifespan.geometryHistory },
        {   geometryItemOptions: {
            includeIndex: false,
            includeDate: true,
            includeDelete: true,
            includeLinesClosed: false}
        },
        {
            geometryUpdateHandler: ctx.geometryUpdateHandler,
            geometryHistoryExtendHandler: ctx.geometryHistoryExtendHandler,
            fieldErrors: ctx.fieldErrors
        }
    );

    const locationHistoryItem = locationHistoryTreeItem(
        locationHistoryId,
        {
            locationHistory: value.lifespan.locationHistory,
            workspaces: value.workspaces
        },
        {
            locationUpdateHandler: ctx.locationUpdateHandler,
            locationHistoryExtendHandler: ctx.locationHistoryExtendHandler,
            fieldErrors: ctx.fieldErrors
        }
    );

    const observationsItem = observationsTreeItem(
        observationsId,
        {
            observations: value.lifespan.observations,
            labels: PlantObservationLabels,
            descriptions: PlantObservationDescriptions
        },
        {
            observationUpdateHandler: ctx.observationUpdateHandler,
            observationDeleteHandler: ctx.observationDeleteHandler,
            dataItemsMap: plantObservationDataItemsMap,
            fieldErrors: ctx.fieldErrors
        }
    );

    return {
        id: itemId,
        label: itemLabel,
        children: [
            originItem,
            geometryHistoryItem,
            locationHistoryItem,
            observationsItem
        ]
    };
}
