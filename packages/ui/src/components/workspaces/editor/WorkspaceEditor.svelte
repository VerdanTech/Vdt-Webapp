<script lang="ts">
	import { useQuery } from '@triplit/svelte';

	import { TabToolbox, TimelineSelector } from '$components';
	import { Resizable } from '$core';
	import { getControllerContext } from '$state';

	import { getWorkspaceContext } from '../../../state/context/workspacesContext.svelte';
	import Layout from './Layout.svelte';
	import Toolbar from './Toolbar.svelte';
	import Tree from './Tree';

	type Props = {
		gardenId: string;
		includeWorkspacesMenu: boolean;
	};
	let { gardenId, includeWorkspacesMenu = true }: Props = $props();

	/** Contexts. */
	const controller = getControllerContext();
	const workspaceContext = getWorkspaceContext();

	/** Queries. */
	const plantingAreasQuery = $derived(
		useQuery(
			controller.triplit,
			controller.triplit
				.query('plantingAreas')
				.Where('locationHistory.workspaceIds', 'has', workspaceContext.id)
				.Include('geometry', (rel) => rel('geometry').Include('linesCoordinates'))
				.Include('locationHistory', (rel) =>
					rel('locationHistory').Include('locations')
				)
		)
	);
	const plantingAreas = $derived(plantingAreasQuery.results || []);

	let workspacesInGardenQuery = $derived(
		useQuery(
			controller.triplit,
			controller.triplit.query('workspaces').Where(['gardenId', '=', gardenId])
		)
	);
	const workspacesInGarden = $derived(workspacesInGardenQuery.results || []);

	/** Force a re-render of the PaneGroup if the direction is changed. */
	let initialized = $state(true);
	$effect(() => {
		if (workspaceContext.paneSettings.direction) {
			initialized = false;
			initialized = true;
		}
	});
</script>

<div class="relative flex h-full w-full flex-col">
	<div class="absolute top-0 h-8 w-full">
		<Toolbar workspaces={workspacesInGarden} {plantingAreas} {includeWorkspacesMenu} />
	</div>
	<div class="absolute bottom-24 top-8 w-full grow overflow-hidden">
		{#if initialized}
			<Resizable.PaneGroup direction={workspaceContext.paneSettings.direction}>
				{#if workspaceContext.paneSettings.isEnabled('layout')}
					<Resizable.Pane defaultSize={70} order={1} minSize={10}>
						{#key workspaceContext.id}
							<Layout {plantingAreas} />
						{/key}
					</Resizable.Pane>
					<Resizable.Handle withHandle={false} />
				{/if}
				{#if workspaceContext.toolbox.isActive}
					<Resizable.Pane defaultSize={20} order={2} minSize={10}>
						<TabToolbox toolbox={workspaceContext.toolbox} />
					</Resizable.Pane>
					<Resizable.Handle withHandle={false} />
				{/if}
				{#if workspaceContext.paneSettings.isEnabled('tree')}
					<Resizable.Pane defaultSize={30} order={3} minSize={10}>
						<Tree {plantingAreas} {workspacesInGarden} />
					</Resizable.Pane>
				{/if}
			</Resizable.PaneGroup>
		{/if}
	</div>
	<div class="absolute bottom-0 h-24 w-full">
		<TimelineSelector selection={workspaceContext.timelineSelection} />
	</div>
</div>
