<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import * as Resizable from "$lib/components/ui/resizable/index.js";
	import activeWorkspace from '../activeWorkspace.svelte';
	import forms from '../forms.svelte'
	import Forms from './Forms.svelte'
	import Tree from './Tree.svelte'
	import Layout from './Layout.svelte';

	onMount(() => {
		/** Update the active workspace upon loading a new workspace. */
		if (activeWorkspace.value.activeWorkspaceId != $page.params.workspaceSlug) {
			activeWorkspace.value.activeWorkspaceId = $page.params.workspaceSlug;
		}
	});
</script>

<Resizable.PaneGroup direction={activeWorkspace.value.contentPaneDirection} autoSaveId={"workspacesContentPaneState"}>
	{#if activeWorkspace.value.treeEnabled}
	<Resizable.Pane defaultSize={30} order={0}>
			<Tree />
		</Resizable.Pane>
	{/if}
	<Resizable.Handle withHandle={false} />
	{#if forms.anyFormsActive}
	<Resizable.Pane defaultSize={20} order={1}>
			<Forms />
	</Resizable.Pane>
	<Resizable.Handle withHandle={false} />
	{/if}
	{#if activeWorkspace.value.layoutEnabled}
	<Resizable.Pane defaultSize={70} order={2}>
			<Layout />
		</Resizable.Pane>
	{/if}
  </Resizable.PaneGroup>