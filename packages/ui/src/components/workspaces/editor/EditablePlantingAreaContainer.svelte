<script lang="ts">
	import {
		type GeometryUpdateCommand,
		type PlantingArea,
		type Position,
		geometryUpdate,
		historySelect,
		locationHistoryUpdate
	} from '@vdg-webapp/models';

	import { PlantingArea as PlantingAreaComponent } from '$components';
	import { getAppContext } from '$state';
	import createCommandHandler from '$state/commandHandler.svelte';

	import { getWorkspaceEditorContext } from './workspaceEditorContext.svelte';

	type Props = {
		plantingArea: PlantingArea;
	};
	let { plantingArea }: Props = $props();

	/** Contexts. */
	const ctx = getAppContext();
	const workspaceEditor = getWorkspaceEditorContext();
	const canvasContext = workspaceEditor.layoutCanvasContext;
	const canvasId = canvasContext.canvasId;

	/** Handlers. */
	const translateCommandHandler = createCommandHandler(locationHistoryUpdate);
	const transformCommandHandler = createCommandHandler(geometryUpdate);

	/**
	 * Tracks the position in the location history at the
	 * focused time and in this workspace in the timeline selection.
	 */
	let position: Position | null = $derived.by(() => {
		if (!plantingArea || !plantingArea.locationHistory) {
			return null;
		}

		const location = historySelect(
			plantingArea.locationHistory.locations,
			workspaceEditor.timelineSelection.focusUtc,
			false
		);
		if (location && location.workspaceId === workspaceEditor.id) {
			return { x: location.x, y: location.y };
		} else {
			return null;
		}
	});

	/** Editable only if editing is enabled and a new planting area isn't being created. */
	let editable: boolean = $derived(
		workspaceEditor.editing &&
			!workspaceEditor.toolbox.isToolActive('plantingAreaCreate')
	);

	/** Selected if included in the list of selected IDs. */
	let selected: boolean = $derived(
		workspaceEditor.selections.has('plantingArea', plantingArea.id)
	);

	/** Update the location history on translation. */
	function onTranslate(newPos: Position) {
		if (!plantingArea || !workspaceEditor.id) {
			return;
		}

		translateCommandHandler.execute(
			{
				id: plantingArea.locationHistoryId,
				workspaceId: workspaceEditor.id,
				coordinate: {
					x: canvasContext.transform.modelXPos(newPos.x),
					y: canvasContext.transform.modelYPos(newPos.y)
				},
				date: workspaceEditor.timelineSelection.focusUtc
			},
			ctx.controller
		);
	}

	/** Update the geometry on transformation. */
	function onTransform(newGeometry: GeometryUpdateCommand) {
		if (!plantingArea) {
			return;
		}

		transformCommandHandler.execute(
			plantingArea.geometryId,
			newGeometry,
			ctx.controller
		);
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
		name={plantingArea.name}
		showName={true}
		{position}
		geometry={plantingArea.geometry}
		{editable}
		{selected}
		{onTranslate}
		{onTransform}
		onClick={() => {
			if (workspaceEditor.toolbox.isToolActive('plantingAreaCreate')) {
				return;
			}
			workspaceEditor.selections.select('plantingArea', plantingArea.id);
		}}
	/>
{/if}
