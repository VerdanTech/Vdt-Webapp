<script lang="ts">
	import type { Vector2d } from 'konva/lib/types';

	import type { Geometry, GeometryUpdateCommand } from '@vdg-webapp/models';

	import { PlantingArea, getWorkspaceEditorContext } from '$components';

	type Props = {
		plantingAreaLayerId: string;
	};
	let { plantingAreaLayerId }: Props = $props();

	/** Contexts.*/
	const workspaceEditor = getWorkspaceEditorContext();
	const canvas = workspaceEditor.layoutCanvasContext;
	const { form: formData } = workspaceEditor.plantingAreaCreateForm.form;

	function onTranslate(newPos: Vector2d) {
		$formData.location.coordinate = {
			x: canvas.transform.modelXPos(newPos.x),
			y: canvas.transform.modelYPos(newPos.y)
		};
	}

	function onTransform(newGeometry: GeometryUpdateCommand) {
		if (newGeometry.rectangleLength) {
			$formData.geometry.rectangleLength = newGeometry.rectangleLength;
		}
		if (newGeometry.rectangleWidth) {
			$formData.geometry.rectangleWidth = newGeometry.rectangleWidth;
		}
		if (newGeometry.polygonNumSides) {
			$formData.geometry.polygonNumSides = newGeometry.polygonNumSides;
		}
		if (newGeometry.polygonRadius) {
			$formData.geometry.polygonRadius = newGeometry.polygonRadius;
		}
		if (newGeometry.ellipseLength) {
			$formData.geometry.ellipseLength = newGeometry.ellipseLength;
		}
		if (newGeometry.ellipseWidth) {
			$formData.geometry.ellipseWidth = newGeometry.ellipseWidth;
		}

		if (newGeometry.linesCoordinates) {
			if (newGeometry.linesCoordinates) {
				$formData.geometry.linesCoordinates = newGeometry.linesCoordinates;
			}
		}
	}
</script>

<!--
@component
Renders a planting area in the canvas representing the
planting area creation form.

Should only render this component if the planting area
creation tool is active.
-->
<PlantingArea
	canvasId={canvas.canvasId}
	layerId={plantingAreaLayerId}
	name={$formData.name}
	showName={true}
	position={$formData.location.coordinate}
	geometry={$formData.geometry as Geometry}
	editable={true}
	selected={true}
	{onTranslate}
	{onTransform}
/>
