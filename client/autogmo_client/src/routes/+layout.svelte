<script>
	import '../theme-garden.postcss';
	import '@skeletonlabs/skeleton/styles/all.css';
    import { AppShell } from '@skeletonlabs/skeleton';
    import UnauthenticatedBar from '$lib/layout/UnauthenticatedBar.svelte';
	import '../app.postcss';
</script>
<slot />

<AppShell>
	<svelte:fragment slot="header">
        <UnauthenticatedBar/>
    </svelte:fragment>
	<svelte:fragment slot="sidebarLeft">Sidebar Left</svelte:fragment>
	<svelte:fragment slot="sidebarRight">Sidebar Right</svelte:fragment>
	<svelte:fragment slot="pageHeader">Page Header</svelte:fragment>
	<!-- Router Slot -->
	<slot />
	<!-- ---- / ---- -->
	<svelte:fragment slot="pageFooter">Page Footer</svelte:fragment>
	<svelte:fragment slot="footer">Footer</svelte:fragment>
</AppShell>
