<script lang="ts">
	import { useQuery } from '@triplit/svelte';

	import { TabToolbox, TimelineSelector } from '$components';
	import { Resizable } from '$core';
	import { getAppContext } from '$state';

	import Layout from './Layout.svelte';
	import Toolbar from './Toolbar.svelte';
	import Tree from './Tree';
	import { getWorkspaceEditorContext } from './workspaceEditorContext.svelte';

	type Props = {
		includeWorkspacesMenu: boolean;
	};
	let { includeWorkspacesMenu = true }: Props = $props();

	/** Contexts. */
	const ctx = getAppContext();
	const workspaceEditor = getWorkspaceEditorContext();

	/** Force a re-render of the PaneGroup if the direction is changed. */
	let initialized = $state(true);
	$effect(() => {
		if (workspaceEditor.paneSettings.direction) {
			initialized = false;
			initialized = true;
		}
	});
</script>

<div class="relative flex h-full w-full flex-col">
	<div class="absolute top-0 h-8 w-full">
		<Toolbar
			workspaces={ctx.workspaces.workspaces}
			plantingAreas={ctx.workspaces.plantingAreas}
			{includeWorkspacesMenu}
		/>
	</div>
	<div class="absolute bottom-24 top-8 w-full grow overflow-hidden">
		{#if initialized}
			<Resizable.PaneGroup direction={workspaceEditor.paneSettings.direction}>
				{#if workspaceEditor.paneSettings.isEnabled('layout')}
					<Resizable.Pane defaultSize={70} order={1} minSize={10}>
						{#key workspaceEditor.id}
							<Layout plantingAreas={ctx.workspaces.plantingAreas} />
						{/key}
					</Resizable.Pane>
					<Resizable.Handle withHandle={false} />
				{/if}
				{#if workspaceEditor.toolbox.isActive}
					<Resizable.Pane defaultSize={20} order={2} minSize={10}>
						<TabToolbox toolbox={workspaceEditor.toolbox} />
					</Resizable.Pane>
					<Resizable.Handle withHandle={false} />
				{/if}
				{#if workspaceEditor.paneSettings.isEnabled('tree')}
					<Resizable.Pane defaultSize={30} order={3} minSize={10}>
						<Tree
							plantingAreas={ctx.workspaces.plantingAreas}
							workspaces={ctx.workspaces.workspaces}
						/>
					</Resizable.Pane>
				{/if}
			</Resizable.PaneGroup>
		{/if}
	</div>
	<div class="absolute bottom-0 h-24 w-full">
		<TimelineSelector selection={workspaceEditor.timelineSelection} />
	</div>
</div>
