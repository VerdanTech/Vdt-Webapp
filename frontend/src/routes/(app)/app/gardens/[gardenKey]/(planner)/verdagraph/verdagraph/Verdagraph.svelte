<script lang="ts">
	import { setContext } from 'svelte';
	import * as Resizable from '$components/ui/resizable';
	import Toolbar from './Toolbar.svelte';
	import createViewSettings from './state/viewSettings.svelte';
	import Calendar from './calendar/Calendar.svelte';
	import Layout from './layout/Layout.svelte';
	import Tree from './tree/Tree.svelte';
	import TimelineSelector from './timelineSelector/TimelineSelector.svelte';
	import Form from './forms/Form.svelte';
	import forms from './state/forms.svelte';

	let viewSettings = createViewSettings();
	setContext('viewSettings', viewSettings);
</script>

<div class="flex h-full flex-col bg-neutral-1">
	<Toolbar />

	<div class="overflow-none grow">
		<!-- Content Panes / Form Pane group-->
		<Resizable.PaneGroup
			direction={viewSettings.value.formPaneDirection}
			autoSaveId={'formPaneState'}
		>
			<Resizable.Pane defaultSize={80} order={0}>
				<!-- Content Panes group-->
				<Resizable.PaneGroup
					direction={viewSettings.value.contentPaneDirection}
					autoSaveId={'verdagraphContentPaneState'}
				>
					{#if viewSettings.value.layoutEnabled}
						<Resizable.Pane
							defaultSize={40}
							minSize={viewSettings.value.minContentPaneSize}
							order={0}
						>
							<Layout />
						</Resizable.Pane>
						<Resizable.Handle withHandle={false} />
					{/if}
					{#if viewSettings.value.calendarEnabled}
						<Resizable.Pane
							defaultSize={40}
							minSize={viewSettings.value.minContentPaneSize}
							order={1}
						>
							<Calendar />
						</Resizable.Pane>
						<Resizable.Handle withHandle={false} />
					{/if}
					{#if viewSettings.value.treeEnabled}
						<Resizable.Pane
							defaultSize={20}
							minSize={viewSettings.value.minContentPaneSize}
							order={2}
						>
							<Tree />
						</Resizable.Pane>
					{/if}
				</Resizable.PaneGroup>
			</Resizable.Pane>
			<Resizable.Handle withHandle={false} />

			{#if forms.anyFormsActive}
				<Resizable.Pane defaultSize={20} minSize={10} order={1}>
					<Form />
				</Resizable.Pane>
			{/if}
		</Resizable.PaneGroup>
	</div>

	<div class="w-full">
		<TimelineSelector />
	</div>
</div>
