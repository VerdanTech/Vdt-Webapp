<script lang="ts">
	import {
		type Cultivar,
		type GeometryHistoryUpdateCommand,
		type GeometryUpdateCommand,
		type Plant,
		type Position,
		geometryHistoryUpdate,
		locationHistoryUpdate,
		resolveActiveGeometry,
		resolveActiveLocation
	} from '@vdg-webapp/models';

	import { Plant as PlantComponent, getVerdagraphContext } from '$components';
	import { getAppContext } from '$state';
	import createCommandHandler from '$state/commandHandler.svelte';

	type Props = {
		plant: Plant;
	};
	let { plant }: Props = $props();

	/** Contexts. */
	const ctx = getAppContext();
	const verdagraphContext = getVerdagraphContext();
	const canvasContext = verdagraphContext.layoutCanvasContext;
	const canvasId = canvasContext.canvasId;

	/** Handlers. */
	const translateCommandHandler = createCommandHandler(locationHistoryUpdate);
	const transformCommandHandler = createCommandHandler(geometryHistoryUpdate);

	/** Resolve the active location and geometry across both lifespans. */
	let activeLocation = $derived(
		plant ? resolveActiveLocation(plant, verdagraphContext.timeline.focusUtc) : null
	);
	let activeGeometry = $derived(
		plant ? resolveActiveGeometry(plant, verdagraphContext.timeline.focusUtc) : null
	);

	let position: Position | null = $derived.by(() => {
		if (
			activeLocation &&
			activeLocation.value.workspaceId === canvasContext.workspaceId
		) {
			return { x: activeLocation.value.x, y: activeLocation.value.y };
		}
		return null;
	});

	let geometry = $derived(activeGeometry?.value ?? null);

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
	function onTranslate(newPos: Position, movementOver: boolean) {
		if (!movementOver) {
			return;
		}

		if (!activeLocation?.lifespan.locationHistoryId) {
			return;
		}

		const command = {
			id: activeLocation.lifespan.locationHistoryId,
			workspaceId: canvasContext.workspaceId,
			coordinate: {
				x: canvasContext.transform.modelXPos(newPos.x),
				y: canvasContext.transform.modelYPos(newPos.y)
			},
			date: verdagraphContext.timeline.focusUtc
		};
		console.log('[EditablePlantContainer] onTranslate', command);
		translateCommandHandler.execute(command, ctx.controller);
	}

	/** Update the geometry history on transformation. */
	function onTransform(newGeometry: GeometryUpdateCommand, transformOver: boolean) {
		if (!transformOver) {
			return;
		}

		if (!activeGeometry?.lifespan.geometryHistoryId || !geometry) {
			return;
		}

		const command = {
			id: activeGeometry.lifespan.geometryHistoryId,
			geometry: {
				type: newGeometry.type ?? geometry.type,
				date: verdagraphContext.timeline.focusUtc,
				scaleFactor: newGeometry.scaleFactor ?? geometry.scaleFactor,
				rotation: newGeometry.rotation ?? geometry.rotation,
				rectangleLength: newGeometry.rectangleLength ?? geometry.rectangleLength,
				rectangleWidth: newGeometry.rectangleWidth ?? geometry.rectangleWidth,
				polygonNumSides: newGeometry.polygonNumSides ?? geometry.polygonNumSides,
				polygonRadius: newGeometry.polygonRadius ?? geometry.polygonRadius,
				ellipseLength: newGeometry.ellipseLength ?? geometry.ellipseLength,
				ellipseWidth: newGeometry.ellipseWidth ?? geometry.ellipseWidth,
				linesCoordinates: newGeometry.linesCoordinates ?? [],
				linesClosed: newGeometry.linesClosed ?? geometry.linesClosed
			},
			date: verdagraphContext.timeline.focusUtc
		} satisfies GeometryHistoryUpdateCommand;
		console.log('[EditablePlantContainer] onTransform', command);
		transformCommandHandler.execute(command, ctx.controller);
	}
</script>

<!--
@component
Renders a planting area in the canvas for a planting
area in the workspace editor, ie., editable
-->
{#if plant && geometry && cultivar}
	<PlantComponent
		{canvasId}
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
