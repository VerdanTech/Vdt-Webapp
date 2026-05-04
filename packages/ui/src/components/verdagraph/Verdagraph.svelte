<script lang="ts">
	import { onMount } from 'svelte';

	import { TabToolbox, TimelineSelector } from '$components';
	import { Resizable } from '$core';
	import { getAppContext } from '$state/application';

	import Calendar from './Calendar.svelte';
	import Layout from './Layout.svelte';
	import Toolbar from './Toolbar.svelte';
	import Tree from './Tree.svelte';
	import {
		type VerdagraphContextParams,
		setVerdagraphContext
	} from './verdagraphContext.svelte';

	type Props = {
		contextParams: VerdagraphContextParams;
	};
	let { contextParams }: Props = $props();

	/** Contexts. */
	const ctx = getAppContext();
	const verdagraphContext = setVerdagraphContext(contextParams);

	/** Force a re-render of the PaneGroup if the direction is changed. */
	let initialized = $state(true);
	$effect(() => {
		if (verdagraphContext.paneSettings.direction) {
			initialized = false;
			initialized = true;
		}
	});

	onMount(() => {});
</script>

<div class="relative flex h-full w-full flex-col">
	<div class="absolute top-0 h-8 w-full">
		<Toolbar />
	</div>

	<div class="absolute top-8 bottom-24 w-full grow overflow-hidden">
		{#if initialized}
			<Resizable.PaneGroup direction={verdagraphContext.paneSettings.direction}>
				{#if verdagraphContext.paneSettings.isEnabled('layout')}
					<!-- TODO: Make one layout per selected workspace. -->
					{@const workspaceId = verdagraphContext.selections
						.get('workspace')
						.values()
						.next().value}
					{#if workspaceId}
						<Resizable.Pane defaultSize={30} minSize={5} order={0}>
							<Layout
								{workspaceId}
								plantingAreas={ctx.workspaces.plantingAreas}
								plants={ctx.plants.plants}
							/>
						</Resizable.Pane>
						<Resizable.Handle withHandle={false} />
					{/if}
				{/if}
				{#if verdagraphContext.paneSettings.isEnabled('calendar')}
					<Resizable.Pane defaultSize={30} minSize={5} order={1}>
						<Calendar />
					</Resizable.Pane>
					<Resizable.Handle withHandle={false} />
				{/if}
				{#if verdagraphContext.toolbox.isActive}
					<Resizable.Pane defaultSize={15} minSize={5} order={2}>
						<TabToolbox toolbox={verdagraphContext.toolbox} />
					</Resizable.Pane>
					<Resizable.Handle withHandle={false} />
				{/if}
				{#if verdagraphContext.paneSettings.isEnabled('tree')}
					<Resizable.Pane defaultSize={25} minSize={5} order={3}>
						<Tree />
					</Resizable.Pane>
				{/if}
			</Resizable.PaneGroup>
		{/if}
	</div>
	<div class="absolute bottom-0 h-24 w-full">
		<TimelineSelector selection={verdagraphContext.timeline} />
	</div>
</div>
