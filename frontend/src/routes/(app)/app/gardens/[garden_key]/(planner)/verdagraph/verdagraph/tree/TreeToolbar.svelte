<script lang="ts">
	import { DatePicker, type DateRange } from 'bits-ui';
	import { Separator, Toolbar } from 'bits-ui';
	import { Combobox } from 'bits-ui';
	import { Input } from '$lib/components/generic/ui/input/index.js';
	import { cn, flyAndScale } from '$lib/utils';
	import CaretLeftIcon from 'virtual:icons/material-symbols/arrow-back-ios-rounded';
	import CaretRightIcon from 'virtual:icons/material-symbols/arrow-forward-ios-rounded';
	import CalendarBlankIcon from 'virtual:icons/material-symbols/calendar-today-outline';
	import { icons } from '$lib/icons';
	import ToolbarButton from '$lib/components/generic/ui/toolbar/ToolbarButton.svelte';
	import ToolbarGroupItem from '$lib/components/generic/ui/toolbar/ToolbarGroupItem.svelte';
	import type { ToolSpec } from '$lib/components/generic/ui/toolbar/types';
	let value: DateRange | undefined = undefined;
	export let scrollable_pane_view_options: string[] | undefined;

	let content_toggles: ToolSpec[] = [
		{ label: 'Toggle Planting Windows', on_click: () => {}, icon: icons.windows },
		{ label: 'Toggle Plants', on_click: () => {}, icon: icons.plants },
		{ label: 'Toggle Actions', on_click: () => {}, icon: icons.actions }
	];

	let options: ToolSpec[] = [{ label: 'Filter', on_click: () => activate_form(), icon: undefined }];
</script>

<Toolbar.Root class="flex items-center justify-center bg-neutral-3">
	<ul class="flex h-full items-center justify-center">
		<li class="flex items-center">
			<i>
				<svelte:component this={icons.verdagraph_tree} class="text-md text-primary-10" />
			</i>
			<span class="text-md ml-2 mr-4 text-neutral-11"> Tree </span>
		</li>

		<Separator.Root orientation={'vertical'} class="h-full w-[1px] self-stretch bg-neutral-7" />

		<!-- Content pane (calendar, layout, list) toggles -->
		<Toolbar.Group
			type="multiple"
			bind:value={scrollable_pane_view_options}
			class="flex h-full items-center"
		>
			{#each content_toggles as content_toggle}
				<ToolbarGroupItem spec={content_toggle} size="text-sm" padding="p-3" />
			{/each}
		</Toolbar.Group>
	</ul>
</Toolbar.Root>
