<script lang="ts">
	import type { Snippet } from 'svelte';
	import { getContext, onMount } from 'svelte';

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

	/**
	 * The container div's width/height are already tracked reactively via
	 * `bind:clientWidth`/`bind:clientHeight` below, so no separate
	 * ResizeObserver is needed here the way Konva's imperative
	 * `stage.width()`/`stage.height()` push once required.
	 */
	onMount(() => {
		canvas.initialize();
	});

	/** Panning the canvas by dragging its background. */
	let isPanning = false;
	let lastPointerPosition: { x: number; y: number } | null = null;

	function handlePointerDown(event: PointerEvent) {
		if (!canvas.transform.draggable) return;
		(event.currentTarget as Element).setPointerCapture(event.pointerId);
		isPanning = true;
		lastPointerPosition = { x: event.clientX, y: event.clientY };
		document.body.style.cursor = 'grabbing';
	}

	function handlePointerMove(event: PointerEvent) {
		if (!isPanning || !lastPointerPosition) return;
		canvas.transform.translate({
			x: event.clientX - lastPointerPosition.x,
			y: event.clientY - lastPointerPosition.y
		});
		lastPointerPosition = { x: event.clientX, y: event.clientY };
	}

	function handlePointerUp(event: PointerEvent) {
		if (!isPanning) return;
		(event.currentTarget as Element).releasePointerCapture(event.pointerId);
		isPanning = false;
		lastPointerPosition = null;
		canvas.selectionGroup.setDocumentCursor();
	}

	function handlePointerEnter() {
		if (isPanning) return;
		canvas.selectionGroup.setDocumentCursor();
	}

	function handlePointerLeave() {
		if (isPanning) return;
		document.body.style.cursor = 'default';
	}
</script>

<div
	bind:clientWidth={canvas.container.width}
	bind:clientHeight={canvas.container.height}
	class="relative h-full w-full"
>
	<div id={canvasId} class="absolute top-0 left-[0.5px] h-full w-full">
		{#if canvas.container.initialized}
			<svg
				bind:this={canvas.container.stageElement}
				width={canvas.container.width}
				height={canvas.container.height}
				style:touch-action="none"
				onpointerdown={handlePointerDown}
				onpointermove={handlePointerMove}
				onpointerup={handlePointerUp}
				onpointerenter={handlePointerEnter}
				onpointerleave={handlePointerLeave}
			>
				<g transform={canvas.transform.stageTransform}>
					{@render children()}
				</g>
			</svg>
		{/if}
	</div>
	<div class="pointer-events-none absolute top-0 left-[0.5px] z-10 h-full w-full">
		{@render overlay()}
	</div>
</div>
