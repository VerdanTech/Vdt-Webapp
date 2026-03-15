<script lang="ts">
	import type { PlantingArea } from '@vdg-webapp/models';

	import { Canvas, Gridlines, PlantingAreas, TransformControls } from '$components';

	import CreatePlantingAreaContainer from './CreatePlantingAreaContainer.svelte';
	import EditablePlantingAreaContainer from './EditablePlantingAreaContainer.svelte';
	import { getWorkspaceEditorContext } from './workspaceEditorContext.svelte';

	type Props = {
		plantingAreas: PlantingArea[];
	};
	let { plantingAreas }: Props = $props();

	const worskpaceEditor = getWorkspaceEditorContext();
	const canvasContext = worskpaceEditor.layoutCanvasContext;
	const canvasId = canvasContext.canvasId;
	const plantingAreaLayerId = 'plantingAreas';
</script>

{#snippet overlay()}
	<TransformControls {canvasId} />
{/snippet}

<Canvas {canvasId} {overlay}>
	<Gridlines {canvasId} />

	<PlantingAreas {canvasId} {plantingAreaLayerId}>
		{#if worskpaceEditor.toolbox.isToolActive('plantingAreaCreate')}
			<CreatePlantingAreaContainer {plantingAreaLayerId} />
		{/if}

		{#each plantingAreas as plantingArea}
			<EditablePlantingAreaContainer {plantingArea} {plantingAreaLayerId} />
		{/each}
	</PlantingAreas>
</Canvas>
