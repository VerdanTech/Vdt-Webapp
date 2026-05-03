<script lang="ts">
	import { onMount } from 'svelte';
	import type { Snippet } from 'svelte';
	import { getContext } from 'svelte';

	import { type CanvasContext } from './state';

	/** Props. */
	type Props = {
		canvasId: string;

		children: Snippet<[]>;
		overlay: Snippet<[]>;
	};
	let { canvasId, children, overlay }: Props = $props();

	/** Create or retrieve the context. */
	const canvas = getContext<CanvasContext>(canvasId);

	let containerRef: HTMLDivElement;
	onMount(() => {
		canvas.initialize();

		const resizeObserver = new ResizeObserver(canvas.container.onResize);
		resizeObserver.observe(containerRef);

		return () => {
			resizeObserver.unobserve(containerRef);
			resizeObserver.disconnect();
		};
	});
</script>

<div
	bind:clientWidth={canvas.container.width}
	bind:clientHeight={canvas.container.height}
	class="relative h-full w-full"
>
	<div
		id={canvasId}
		bind:this={containerRef}
		class="absolute top-0 left-[0.5px] h-full w-full"
	>
		{#if canvas.container.initialized}
			{@render children()}
		{/if}
	</div>
	<div class="pointer-events-none absolute top-0 left-[0.5px] z-10 h-full w-full">
		{@render overlay()}
	</div>
</div>
