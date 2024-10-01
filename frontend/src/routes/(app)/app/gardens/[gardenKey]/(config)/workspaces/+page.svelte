<script lang="ts">
	import { onMount } from 'svelte';
	import activeWorkspace from './activeWorkspace.svelte';
	import UnderConstructionPage from '$components/misc/UnderConstructionPage.svelte';

	onMount(() => {
		/** CLear the active workspace. */
		if (activeWorkspace.value.activeWorkspaceId) {
			activeWorkspace.value.activeWorkspaceId = null;
			activeWorkspace.value.editing = false;
		}
	});
</script>

<svelte:head>
	<title>Workspaces - VerdanTech</title>
</svelte:head>

worskpace list
