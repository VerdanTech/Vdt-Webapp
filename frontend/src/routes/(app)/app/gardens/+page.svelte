<script lang="ts">
	import isAuthenticated from '$state/authenticated.svelte'
	import UnderConstructionPage from '$components/misc/UnderConstructionPage.svelte'
</script>

<svelte:head>
	<title>Gardens - VerdanTech</title>
</svelte:head>

<UnderConstructionPage />

{#if isAuthenticated.value}
	a
{:else}
	b
{/if}
