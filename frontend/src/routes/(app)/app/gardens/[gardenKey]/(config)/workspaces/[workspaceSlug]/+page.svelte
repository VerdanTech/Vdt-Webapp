<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import activeWorkspace from '../activeWorkspace.svelte';

	onMount(() => {
		/** Update the active workspace upon loading a new workspace. */
		if (activeWorkspace.value.activeWorkspaceId != $page.params.workspaceSlug) {
			activeWorkspace.value.activeWorkspaceId = $page.params.workspaceSlug;
		}
	});
</script>
