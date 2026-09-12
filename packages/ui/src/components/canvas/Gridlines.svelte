<script lang="ts">
	import { getContext } from 'svelte';

	import type { CanvasContext } from './state/context.svelte';

	/** Props. */
	type Props = {
		canvasId: string;
	};
	let { canvasId }: Props = $props();

	let canvas = getContext<CanvasContext>(canvasId);
</script>

<g>
	{#each canvas.gridManager.visibleGridlines as line (line.key)}
		<line
			x1={line.x1}
			y1={line.y1}
			x2={line.x2}
			y2={line.y2}
			stroke={line.color}
			stroke-width={line.strokeWidth}
			vector-effect="non-scaling-stroke"
		/>
	{/each}
</g>
