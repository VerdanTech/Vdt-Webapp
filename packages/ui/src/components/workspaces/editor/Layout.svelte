<script lang="ts">
	import type { PlantingArea } from '@vdg-webapp/models';

	import { Canvas, Gridlines, PlantingAreas, TransformControls } from '$components';

	import { getWorkspaceContext } from '../../../state/context/workspacesContext.svelte';
	import CreatePlantingAreaContainer from './CreatePlantingAreaContainer.svelte';
	import EditablePlantingAreaContainer from './EditablePlantingAreaContainer.svelte';

	type Props = {
		plantingAreas: PlantingArea[];
	};
	let { plantingAreas }: Props = $props();

	const workspaceContext = getWorkspaceContext();
	const canvasContext = workspaceContext.layoutCanvasContext;
	const canvasId = canvasContext.canvasId;
	const plantingAreaLayerId = 'plantingAreas';
</script>

{#snippet overlay()}
	<TransformControls {canvasId} />
{/snippet}

<Canvas {canvasId} {overlay}>
	<Gridlines {canvasId} />

	<PlantingAreas {canvasId} {plantingAreaLayerId}>
		{#if workspaceContext.toolbox.isToolActive('plantingAreaCreate')}
			<CreatePlantingAreaContainer {plantingAreaLayerId} />
		{/if}

		{#each plantingAreas as plantingArea}
			<EditablePlantingAreaContainer {plantingArea} {plantingAreaLayerId} />
		{/each}
	</PlantingAreas>
</Canvas>
