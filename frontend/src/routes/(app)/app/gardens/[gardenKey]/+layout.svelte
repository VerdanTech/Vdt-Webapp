<script>
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import GardenContext from './GardenContext.svelte';
	import activeGardenKey from '$state/activeGarden.svelte';

	onMount(() => {
		/** Update the active garden upon loading a new garden. */
		if (activeGardenKey.value != $page.params.gardenKey) {
			activeGardenKey.value = $page.params.gardenKey;
		}
	});

	let { children } = $props();
</script>

<div class="flex h-full flex-col">
	<div class="grow">
		{@render children()}
	</div>
	<GardenContext />
</div>
