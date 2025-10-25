<script lang="ts">
	import type { Vector2d } from 'konva/lib/types';

	import {
		type GeometryUpdateCommand,
		type PlantingArea,
		geometryUpdate,
		historySelect,
		locationHistoryUpdate
	} from '@vdg-webapp/models';

	import { PlantingArea as PlantingAreaComponent } from '$components';
	import { getControllerContext } from '$state';
	import createCommandHandler from '$state/commandHandler.svelte';

	import { getWorkspaceContext } from '../../../state/context/workspacesContext.svelte';

	type Props = {
		plantingAreaLayerId: string;
		plantingArea: PlantingArea;
	};
	let { plantingAreaLayerId, plantingArea }: Props = $props();

	/** Contexts. */
	const controller = getControllerContext();
	const workspaceContext = getWorkspaceContext();
	const canvasContext = workspaceContext.layoutCanvasContext;
	const canvasId = canvasContext.canvasId;

	/** Handlers. */
	const translateCommandHandler = createCommandHandler(locationHistoryUpdate);
	const transformCommandHandler = createCommandHandler(geometryUpdate);

	/**
	 * Tracks the position in the location history at the
	 * focused time and in this workspace in the timeline selection.
	 */
	let position: Vector2d | null = $derived.by(() => {
		if (!plantingArea || !plantingArea.locationHistory) {
			return null;
		}

		const location = historySelect(
			plantingArea.locationHistory.locations,
			workspaceContext.timelineSelection.focusUtc,
			false
		);
		if (location && location.workspaceId === workspaceContext.id) {
			return { x: location.x, y: location.y };
		} else {
			return null;
		}
	});

	/** Editable only if editing is enabled and a new planting area isn't being created. */
	let editable: boolean = $derived(
		workspaceContext.editing &&
			!workspaceContext.toolbox.isToolActive('plantingAreaCreate')
	);

	/** Selected if included in the list of selected IDs. */
	let selected: boolean = $derived(
		workspaceContext.selections.has('plantingArea', plantingArea.id)
	);

	/** Update the location history on translation. */
	function onTranslate(newPos: Vector2d) {
		if (!plantingArea || !workspaceContext.id) {
			return;
		}

		translateCommandHandler.execute(
			{
				id: plantingArea.locationHistoryId,
				workspaceId: workspaceContext.id,
				coordinate: {
					x: canvasContext.transform.modelXPos(newPos.x),
					y: canvasContext.transform.modelYPos(newPos.y)
				},
				date: workspaceContext.timelineSelection.focusUtc
			},
			controller
		);
	}

	/** Update the geometry on transformation. */
	function onTransform(newGeometry: GeometryUpdateCommand) {
		if (!plantingArea) {
			return;
		}

		transformCommandHandler.execute(plantingArea.geometryId, newGeometry, controller);
	}
</script>

<!--
@component
Renders a planting area in the canvas for a planting
area in the workspace editor, ie., editable
-->
{#if plantingArea && plantingArea.geometry}
	<PlantingAreaComponent
		{canvasId}
		layerId={plantingAreaLayerId}
		name={plantingArea.name}
		showName={true}
		{position}
		geometry={plantingArea.geometry}
		{editable}
		{selected}
		{onTranslate}
		{onTransform}
		onClick={() => {
			if (workspaceContext.toolbox.isToolActive('plantingAreaCreate')) {
				return;
			}
			workspaceContext.selections.select('plantingArea', plantingArea.id);
		}}
	/>
{/if}
