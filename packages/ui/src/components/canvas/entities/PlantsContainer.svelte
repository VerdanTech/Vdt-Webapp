<script lang="ts">
	import type { Snippet } from 'svelte';

	/** Props. */
	type Props = {
		canvasId: string;
		plantLayerId: string;
		children: Snippet<[]>;
	};
	let { plantLayerId, children }: Props = $props();
</script>

<g data-layer-id={plantLayerId}>
	{@render children()}
</g>
