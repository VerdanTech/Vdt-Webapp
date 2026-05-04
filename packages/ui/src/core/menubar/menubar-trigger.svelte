<script lang="ts">
	import { Menubar as MenubarPrimitive } from 'bits-ui';

	import { cn } from '$utils';

	let {
		ref = $bindable(null),
		class: className,
		...restProps
	}: MenubarPrimitive.TriggerProps = $props();
</script>

<MenubarPrimitive.Trigger
	bind:ref
	class={cn(
		'data-[highlighted]:bg-accent-5 data-[state=open]:bg-accent-5 data-[highlighted]:text-accent-12 data-[state=open]:text-accent-12 flex cursor-default items-center rounded-none border-b px-3 py-1.5 text-sm font-medium outline-none select-none',
		className
	)}
	{...restProps}
/>
