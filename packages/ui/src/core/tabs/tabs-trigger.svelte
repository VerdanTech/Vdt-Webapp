<script lang="ts">
	import { Tabs as TabsPrimitive } from 'bits-ui';

	import { cn } from '$utils';

	let {
		ref = $bindable(null),
		class: className,
		...restProps
	}: TabsPrimitive.TriggerProps = $props();
</script>

<TabsPrimitive.Trigger
	bind:ref
	class={cn(
		'ring-offset-neutral-1 focus-visible:ring-neutral-11 data-[state=active]:bg-neutral-2 data-[state=active]:text-neutral-11 inline-flex items-center justify-center rounded-none px-3 py-1.5 text-sm font-medium whitespace-nowrap transition-all focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50 ',
		className
	)}
	{...restProps}
/>
