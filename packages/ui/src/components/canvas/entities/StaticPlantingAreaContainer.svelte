<script lang="ts">
	import { type PlantingArea, type Position, historySelect } from '@vdg-webapp/models';

	import {
		type CanvasContext,
		PlantingArea as PlantingAreaComponent,
		type TimelineSelection
	} from '$components';

	type Props = {
		plantingArea: PlantingArea;
		canvasContext: CanvasContext;
		timelineSelection: TimelineSelection;
	};
	let { plantingArea, canvasContext, timelineSelection }: Props = $props();

	/** Contexts. */
	const canvasId = canvasContext.canvasId;

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
			timelineSelection.focusUtc,
			false
		);
		if (location) {
			return { x: location.x, y: location.y };
		} else {
			return null;
		}
	});
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
		editable={false}
		selected={false}
	/>
{/if}
