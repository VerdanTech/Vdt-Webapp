<script lang="ts">
	import { Tabs as TabsPrimitive } from 'bits-ui';
	import { cn } from '$lib/utils/shadcn.js';

	type $$Props = TabsPrimitive.ListProps;

	let className: $$Props['class'] = undefined;
	export { className as class };
</script>

<TabsPrimitive.List
	class={cn(
		'inline-flex h-10 items-center justify-center rounded-md bg-neutral-3 p-1 text-neutral-11',
		className
	)}
	{...$$restProps}
>
	<slot />
</TabsPrimitive.List>
