<script lang="ts">
	import type { Label as LabelPrimitive } from 'bits-ui'
	import { getFormControl } from 'formsnap'
	import { cn } from '$lib/utils.js'
	import { Label } from '$lib/components/ui/label/index.js'

	import Icon from '@iconify/svelte'
	import iconIds from '$lib/assets/icons'
	import * as Popover from '$components/ui/popover'

	type $$Props = LabelPrimitive.Props & {
		description?: string
	}

	let className: $$Props['class'] = undefined
	export let description: string | undefined = undefined
	export { className as class }

	const { labelAttrs } = getFormControl()
</script>

<Label
	{...$labelAttrs}
	class={cn(
		'flex items-center decoration-destructive-8 underline-offset-4 data-[fs-error]:underline',
		className
	)}
	{...$$restProps}
>
	<slot {labelAttrs} />
	{#if description}
		<Popover.Root>
			<Popover.Trigger class="w-8">
				<Icon
					icon={iconIds.formFieldDescriptionIcon}
					width="1rem"
					class="ml-2 text-neutral-11 hover:text-neutral-10 data-[fs-error]:text-neutral-8"
				/>
			</Popover.Trigger>
			<Popover.Content class="max-w-2xl">
				{description}
			</Popover.Content>
		</Popover.Root>
	{/if}
</Label>
