<script lang="ts">
	import type { Label as LabelPrimitive } from 'bits-ui';
	import { getFormControl } from 'formsnap';
	import { cn } from '$lib/utils/shadcn.js';
	import { Label } from '$lib/components/ui/label/index.js';

	import FormInfoPopover from '$components/misc/FormInfoPopover.svelte';

	type $$Props = LabelPrimitive.Props & {
		description?: string;
		optional?: boolean;
	};

	let className: $$Props['class'] = undefined;
	export let description: string | undefined = undefined;
	export let optional: boolean = false;
	export { className as class };

	const { labelAttrs } = getFormControl();
</script>

<Label
	{...$labelAttrs}
	class={cn(
		'flex items-center decoration-destructive-8 underline-offset-4 data-[fs-error]:underline data-[fs-error]:decoration-wavy',
		className
	)}
	{...$$restProps}
>
	<slot {labelAttrs} />
	{#if !optional}
		<span class="mx-1 translate-y-[2px]">*</span>
	{/if}
	{#if description}
		<FormInfoPopover {description} />
	{/if}
</Label>
