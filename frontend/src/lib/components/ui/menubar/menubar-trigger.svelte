<script lang="ts">
	import { Menubar as MenubarPrimitive } from 'bits-ui';
	import { cn } from '$lib/utils/shadcn.js';

	type $$Props = MenubarPrimitive.TriggerProps;
	type $$Events = MenubarPrimitive.TriggerEvents;

	let className: $$Props['class'] = undefined;
	export { className as class };
</script>

<MenubarPrimitive.Trigger
	class={cn(
		'data-[highlighted]:bg-accent-5-5 data-[state=open]:bg-accent-5-5 flex cursor-default select-none items-center rounded-sm px-3 py-1.5 text-sm outline-none hover:bg-neutral-3 data-[highlighted]:text-accent-12 data-[state=open]:text-accent-12',
		className
	)}
	on:click
	on:keydown
	on:pointerenter
	{...$$restProps}
>
	<slot />
</MenubarPrimitive.Trigger>
