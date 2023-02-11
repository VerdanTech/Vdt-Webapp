<script>
	import '../theme-garden.postcss';
	import '@skeletonlabs/skeleton/styles/all.css';
    import { AppShell } from '@skeletonlabs/skeleton';
    import UnauthenticatedAppBar from '$lib/layout/UnauthenticatedAppBar.svelte';
	import '../app.postcss';
</script>

<AppShell>
	<svelte:fragment slot="header">
        <UnauthenticatedAppBar/>
    </svelte:fragment>
	<!-- Router Slot -->
	<slot />
	<!-- ---- / ---- -->
</AppShell>
