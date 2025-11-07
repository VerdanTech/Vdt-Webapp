<script lang="ts">
	import type { Vector2d } from 'konva/lib/types';

	import {
		type Cultivar,
		type Geometry,
		type GeometryUpdateCommand,
		type Location,
		type Plant,
		geometryHistoryUpdate,
		historySelect,
		locationHistoryUpdate
	} from '@vdg-webapp/models';

	import { Plant as PlantComponent, getVerdagraphContext } from '$components';
	import { getAppContext } from '$state';
	import createCommandHandler from '$state/commandHandler.svelte';

	type Props = {
		plantLayerId: string;
		plant: Plant;
	};
	let { plantLayerId, plant }: Props = $props();

	/** Contexts. */
	const ctx = getAppContext();
	const verdagraphContext = getVerdagraphContext();
	const canvasContext = verdagraphContext.layoutCanvasContext;
	const canvasId = canvasContext.canvasId;

	/** Handlers. */
	const translateCommandHandler = createCommandHandler(locationHistoryUpdate);
	const transformCommandHandler = createCommandHandler(geometryHistoryUpdate);

	/**
	 * Tracks the position in the location history at the
	 * focused time and in this workspace in the timeline selection.
	 */
	let position: Vector2d | null = $derived.by(() => {
		if (
			!plant ||
			(!plant.recordedLifespan?.locationHistory &&
				!plant.expectedLifespan?.locationHistory)
		) {
			return null;
		}

		let location: Location | null = null;
		if (plant.recordedLifespan && plant.recordedLifespan.locationHistory) {
			location = historySelect(
				plant.recordedLifespan.locationHistory.locations,
				verdagraphContext.timeline.focusUtc,
				false
			);
		}

		if (!location) {
			if (plant.expectedLifespan && plant.expectedLifespan.locationHistory) {
				location = historySelect(
					plant.expectedLifespan.locationHistory.locations,
					verdagraphContext.timeline.focusUtc,
					false
				);
			}
		}

		if (
			location &&
			location.workspaceId === verdagraphContext.layoutCanvasContext.workspaceId
		) {
			return { x: location.x, y: location.y };
		} else {
			return null;
		}
	});

	/**
	 * Tracks the geometry in the geometry history at the
	 * focused time and in this workspace in the timeline selection.
	 */
	let geometry: Geometry | null = $derived.by(() => {
		if (
			!plant ||
			(!plant.recordedLifespan?.geometryHistory &&
				!plant.expectedLifespan?.geometryHistory)
		) {
			return null;
		}

		let geometry: Geometry | null = null;
		if (plant.recordedLifespan && plant.recordedLifespan.geometryHistory) {
			geometry = historySelect(
				plant.recordedLifespan.geometryHistory.geometries,
				verdagraphContext.timeline.focusUtc,
				false
			);
		}

		if (!geometry) {
			if (plant.expectedLifespan && plant.expectedLifespan.geometryHistory) {
				geometry = historySelect(
					plant.expectedLifespan.geometryHistory.geometries,
					verdagraphContext.timeline.focusUtc,
					false
				);
			}
		}

		if (geometry) {
			return geometry;
		} else {
			return null;
		}
	});

	let cultivar: Cultivar | null = $derived(ctx.plants.getCultivar(plant.cultivarName));

	/** Editable only if editing is enabled and a new planting area isn't being created. */
	let editable: boolean = $derived(
		verdagraphContext.editing && !verdagraphContext.toolbox.isToolActive('plantsCreate')
	);

	/** Selected if included in the list of selected IDs. */
	let selected: boolean = $derived(
		verdagraphContext.selections.has('plants', plant.id)
	);

	/** Update the location history on translation. */
	function onTranslate(newPos: Vector2d) {
		//if (!plant || !workspaceContext.id) {
		//return;
		//}
		/* 
		translateCommandHandler.execute(
			{
				id: plant.expectedLifespan.locationHistoryId,
				workspaceId: verdagraphContext.layoutCanvasContext.workspaceId,
				coordinate: {
					x: canvasContext.transform.modelXPos(newPos.x),
					y: canvasContext.transform.modelYPos(newPos.y)
				},
				date: verdagraphContext.timeline.focusUtc
			},
			ctx.controller
		);
		*/
	}

	/** Update the geometry on transformation. */
	function onTransform(newGeometry: GeometryUpdateCommand) {
		if (!plant) {
			return;
		}

		//transformCommandHandler.execute(plantingArea.geometryId, newGeometry, controller);
	}
</script>

<!--
@component
Renders a planting area in the canvas for a planting
area in the workspace editor, ie., editable
-->
{#if plant && geometry}
	<PlantComponent
		{canvasId}
		layerId={plantLayerId}
		name={cultivar.abbreviation}
		showName={true}
		{position}
		{geometry}
		{editable}
		{selected}
		{onTranslate}
		{onTransform}
		onClick={() => {
			if (verdagraphContext.toolbox.isToolActive('plantsCreate')) {
				return;
			}
			verdagraphContext.selections.select('plants', plant.id);
		}}
	/>
{/if}
