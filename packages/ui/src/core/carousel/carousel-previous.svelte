<script lang="ts">
	import type { WithoutChildren } from 'bits-ui';

	import { Button, type Props } from '$core/button/index.js';
	import { cn } from '$utils';

	import { getEmblaContext } from './context.js';

	let {
		ref = $bindable(null),
		class: className,
		variant = 'outline',
		size = 'icon',
		...restProps
	}: WithoutChildren<Props> = $props();

	const emblaCtx = getEmblaContext('<Carousel.Previous/>');
</script>

<Button
	{variant}
	{size}
	class={cn(
		'absolute size-8 touch-manipulation rounded-full',
		emblaCtx.orientation === 'horizontal'
			? 'top-1/2 -left-12 -translate-y-1/2'
			: '-top-12 left-1/2 -translate-x-1/2 rotate-90',
		className
	)}
	disabled={!emblaCtx.canScrollPrev}
	onclick={emblaCtx.scrollPrev}
	onkeydown={emblaCtx.handleKeyDown}
	{...restProps}
	bind:ref
>
	left
	<span class="sr-only">Previous slide</span>
</Button>
