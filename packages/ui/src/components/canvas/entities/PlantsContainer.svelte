<script lang="ts">
	import { type Snippet, getContext } from 'svelte';

	import type { CanvasContext } from '../state';

	/** Props. */
	type Props = {
		canvasId: string;
		plantLayerId: string;
		children: Snippet<[]>;
	};
	let { canvasId, plantLayerId, children }: Props = $props();

	let canvas = getContext<CanvasContext>(canvasId);

	canvas.container.addLayer(plantLayerId);
</script>

{@render children()}
