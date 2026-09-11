<script lang="ts">
	import {
		type Geometry,
		type GeometryUpdateCommand,
		type Position,
		historySelect
	} from '@vdg-webapp/models';

	import { Plant } from '$components';

	import { getVerdagraphContext } from './verdagraphContext.svelte';

	type Props = {
		workspaceId: string;
		plantLayerId: string;
		plantIdx: number;
	};
	let { workspaceId, plantLayerId, plantIdx }: Props = $props();

	/** Contexts.*/
	const verdagraphContext = getVerdagraphContext();
	const canvas = verdagraphContext.layoutCanvasContext;
	const { form: formData } = verdagraphContext.plantsCreateForm.form;

	let plant = $derived($formData.plants[plantIdx]);
	let location = $derived.by(() => {
		if (!plant || !plant.locationHistory) {
			return null;
		}

		return historySelect(
			plant.locationHistory.locations,
			verdagraphContext.timeline.focusUtc,
			true
		);
	});
	let geometry = $derived.by(() => {
		if (!plant || !plant.geometryHistory) {
			return null;
		}

		return historySelect(
			plant.geometryHistory.geometries,
			verdagraphContext.timeline.focusUtc,
			true
		);
	});

	/**
	 * Tracks the position in the location history at the
	 * focused time and in this workspace in the timeline selection.
	 */
	let position: Position | null = $derived.by(() => {
		if (!location || location.workspaceId !== workspaceId) {
			return null;
		}

		return { x: location.coordinate.x, y: location.coordinate.y };
	});

	function onTranslate(newPos: Position) {
		if (!location) {
			return;
		}

		location.coordinate = {
			x: canvas.transform.modelXPos(newPos.x),
			y: canvas.transform.modelYPos(newPos.y)
		};
	}

	function onTransform(newGeometry: GeometryUpdateCommand) {
		if (!geometry) {
			return;
		}

		if (newGeometry.rectangleLength) {
			geometry.rectangleLength = newGeometry.rectangleLength;
		}
		if (newGeometry.rectangleWidth) {
			geometry.rectangleWidth = newGeometry.rectangleWidth;
		}
		if (newGeometry.polygonNumSides) {
			geometry.polygonNumSides = newGeometry.polygonNumSides;
		}
		if (newGeometry.polygonRadius) {
			geometry.polygonRadius = newGeometry.polygonRadius;
		}
		if (newGeometry.ellipseLength) {
			geometry.ellipseLength = newGeometry.ellipseLength;
		}
		if (newGeometry.ellipseWidth) {
			geometry.ellipseWidth = newGeometry.ellipseWidth;
		}

		if (newGeometry.linesCoordinates) {
			if (newGeometry.linesCoordinates) {
				geometry.linesCoordinates = newGeometry.linesCoordinates;
			}
		}
	}
</script>

<!--
@component
Renders a plant in the canvas representing 
a plant in the plants creation form.
-->
{#if geometry}
	<Plant
		canvasId={canvas.canvasId}
		layerId={plantLayerId}
		name={plant.cultivarName}
		showName={true}
		{position}
		geometry={geometry as Geometry}
		editable={true}
		selected={true}
		{onTranslate}
		{onTransform}
	/>
{/if}
