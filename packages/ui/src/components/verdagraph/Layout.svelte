<script lang="ts">
	import type { PlantingArea } from '@vdg-webapp/models';

	import {
		Canvas,
		Gridlines,
		PlantingAreas,
		StaticPlantingAreaContainer,
		TransformControls
	} from '$components';

	import { getVerdagraphContext } from './verdagraphContext.svelte';

	const verdagraphContext = getVerdagraphContext();

	type Props = {
		plantingAreas: PlantingArea[];
	};
	let { plantingAreas }: Props = $props();

	const canvasContext = verdagraphContext.layoutCanvasContext;
	const canvasId = canvasContext.canvasId;
	const plantingAreaLayerId = 'plantingAreas';
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
				{plantingAreaLayerId}
				canvasContext={verdagraphContext.layoutCanvasContext}
				timelineSelection={verdagraphContext.timeline}
			/>
		{/each}
	</PlantingAreas>
</Canvas>
