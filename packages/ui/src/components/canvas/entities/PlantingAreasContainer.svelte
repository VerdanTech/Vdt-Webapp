<script lang="ts">
	import { type Snippet, getContext } from 'svelte';

	import type { CanvasContext } from '../state';

	/** Props. */
	type Props = {
		canvasId: string;
		plantingAreaLayerId: string;
		children: Snippet<[]>;
	};
	let { canvasId, plantingAreaLayerId, children }: Props = $props();

	let canvas = getContext<CanvasContext>(canvasId);

	canvas.container.addLayer(plantingAreaLayerId);
</script>

{@render children()}
