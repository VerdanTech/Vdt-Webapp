<script lang="ts">
	import type { Plant, PlantingArea } from '@vdg-webapp/models';

	import {
		Canvas,
		Gridlines,
		PlantingAreas,
		PlantsContainer,
		StaticPlantingAreaContainer,
		TransformControls
	} from '$components';

	import CreatePlantsContainer from './CreatePlantsContainer.svelte';
	import { getVerdagraphContext } from './verdagraphContext.svelte';

	const verdagraphContext = getVerdagraphContext();

	type Props = {
		plantingAreas: PlantingArea[];
		plants: Plant[];
		workspaceId: string;
	};
	let { plantingAreas, plants, workspaceId }: Props = $props();

	const canvasContext = verdagraphContext.layoutCanvasContext;
	const canvasId = canvasContext.canvasId;
	const plantingAreaLayerId = 'plantingAreas';
	const plantLayerId = 'plants';
</script>

{#snippet overlay()}
	<TransformControls {canvasId} />
{/snippet}

<Canvas {canvasId} {overlay}>
	<Gridlines {canvasId} />

	<PlantingAreas {canvasId} {plantingAreaLayerId}>
		{#each plantingAreas as plantingArea}
			<StaticPlantingAreaContainer
				{plantingArea}
				layerId={plantingAreaLayerId}
				canvasContext={verdagraphContext.layoutCanvasContext}
				timelineSelection={verdagraphContext.timeline}
			/>
		{/each}
	</PlantingAreas>

	<PlantsContainer {canvasId} {plantLayerId}>
		<CreatePlantsContainer {workspaceId} {plantLayerId}></CreatePlantsContainer>
	</PlantsContainer>
</Canvas>
