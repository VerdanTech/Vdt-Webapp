<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import * as Resizable from "$lib/components/ui/resizable/index.js";
	import activeWorkspace from '../activeWorkspace.svelte';

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
			WorkspaceTree
		</Resizable.Pane>
	{/if}
	<Resizable.Handle withHandle={false} />
	{#if activeWorkspace.value.layoutEnabled}
	<Resizable.Pane defaultSize={70} order={1}>
			WorkspaceLayout
		</Resizable.Pane>
	{/if}
  </Resizable.PaneGroup>