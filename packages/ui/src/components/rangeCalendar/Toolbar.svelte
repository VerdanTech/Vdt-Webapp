<script lang="ts">
	import { Toolbar } from 'bits-ui';

	import * as Select from '$core/select/index.js';

	import { type CalendarContext } from './context.svelte';
	import { type ViewPanesOptions } from './context.svelte';

	type Props = {
		context: CalendarContext<any>;
	};
	let { context = $bindable() }: Props = $props();

	const viewSelectOptions: { value: ViewPanesOptions; label: string }[] = [
		{ value: 'plants', label: 'Plants' },
		{ value: 'plantingWindows', label: 'Planting Windows' },
		{ value: 'actions', label: 'Actions' }
	];
</script>

<Toolbar.Root
	class="border-neutral-8 justify-center border-0 border-b md:justify-start"
>
	<!-- View Menu -->
	<Select.Root
		type="multiple"
		name="calendarView"
		bind:value={context.config.value.viewPanesSelect}
	>
		<Select.Trigger class="w-1/4 rounded-none border-none">Panes</Select.Trigger>
		<Select.Content>
			<Select.Group>
				{#each viewSelectOptions as pane (pane.value)}
					<Select.Item value={pane.value} label={pane.label}>{pane.label}</Select.Item>
				{/each}
			</Select.Group>
		</Select.Content>
	</Select.Root>
</Toolbar.Root>
