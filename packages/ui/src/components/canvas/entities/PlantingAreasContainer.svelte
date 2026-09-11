<script lang="ts">
	import type { Snippet } from 'svelte';

	/** Props. */
	type Props = {
		canvasId: string;
		plantingAreaLayerId: string;
		children: Snippet<[]>;
	};
	let { plantingAreaLayerId, children }: Props = $props();
</script>

<g data-layer-id={plantingAreaLayerId}>
	{@render children()}
</g>
