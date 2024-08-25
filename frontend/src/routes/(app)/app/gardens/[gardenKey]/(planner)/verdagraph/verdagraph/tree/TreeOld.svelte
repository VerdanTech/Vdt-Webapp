<script lang="ts">
	import * as Resizable from '$lib/components/generic/ui/resizable';
	import TreeToolbar from './TreeToolbar.svelte';
	import TreeWindowsScrollable from './TreeWindowsScrollable.svelte';
	import TreePlantsScrollable from './TreePlantsScrollable.svelte';
	import TreeActionsScrollable from './TreeActionsScrollable.svelte';

	let scrollable_pane_direction: Resizable.Direction = 'vertical';
	let scrollable_pane_view_options: string[] | undefined = [
		'Toggle Planting Windows',
		'Toggle Plants',
		'Toggle Actions'
	];
</script>

<div class="flex h-full w-full flex-col bg-neutral-1">
	<TreeToolbar bind:scrollable_pane_view_options />

	<div class="overflow-none grow">
		<Resizable.PaneGroup direction={scrollable_pane_direction} autoSaveId={'tree_pane'}>
			{#if scrollable_pane_view_options?.includes('Toggle Planting Windows')}
				<Resizable.Pane defaultSize={1 / 3} minSize={10} order={1}>
					<TreeWindowsScrollable />
				</Resizable.Pane>
				<Resizable.Handle />
			{/if}
			{#if scrollable_pane_view_options?.includes('Toggle Plants')}
				<Resizable.Pane defaultSize={1 / 3} minSize={10} order={2}>
					<TreePlantsScrollable />
				</Resizable.Pane>
				<Resizable.Handle />
			{/if}
			{#if scrollable_pane_view_options?.includes('Toggle Actions')}
				<Resizable.Pane defaultSize={1 / 3} minSize={10} order={3}>
					<TreeActionsScrollable />
				</Resizable.Pane>
			{/if}
		</Resizable.PaneGroup>
	</div>
</div>
