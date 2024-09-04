<script>
	import PrimaryNav from '$components/primary_nav/PrimaryNav.svelte';

	let { children } = $props();
</script>

<!-- Wraps the primary nav to provide proper spacing between the nav and content. -->
<div class="flex h-screen w-screen flex-col overflow-clip lg:flex-row">
	<PrimaryNav />
	<div
		class="order-last mb-16 ml-0 h-auto w-full grow overflow-auto lg:order-first lg:mb-0 lg:ml-16"
	>
		{@render children()}
	</div>
</div>
