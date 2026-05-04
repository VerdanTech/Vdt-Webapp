<script lang="ts">
	import { Menubar as MenubarPrimitive, type WithoutChild } from 'bits-ui';
	import ChevronRight from 'lucide-svelte/icons/chevron-right';

	import { cn } from '$utils';

	let {
		ref = $bindable(null),
		class: className,
		inset = undefined,
		children,
		...restProps
	}: WithoutChild<MenubarPrimitive.SubTriggerProps> & {
		inset?: boolean;
	} = $props();
</script>

<MenubarPrimitive.SubTrigger
	bind:ref
	class={cn(
		'data-[highlighted]:bg-accent-5 data-[state=open]:bg-accent-5 data-[highlighted]:text-accent-12 data-[state=open]:text-accent-12 flex cursor-default items-center rounded-sm px-2 py-1.5 text-sm outline-none select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50',
		inset && 'pl-8',
		className
	)}
	{...restProps}
>
	{@render children?.()}
	<ChevronRight class="ml-auto size-4" />
</MenubarPrimitive.SubTrigger>
