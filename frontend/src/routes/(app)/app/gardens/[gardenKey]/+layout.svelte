<script>
	import {page} from '$app/stores'
	import GardenContext from './GardenContext.svelte'
	import activeGardenKey from '$state/activeGarden.svelte';

	/** Update the active garden upon loading a new garden. */
	if (activeGardenKey.value != $page.params.gardenKey) {
		activeGardenKey.value = $page.params.gardenKey
	}

	let { children } = $props()
</script>

<div class="flex h-full flex-col">
	<div class="grow">
		{@render children()}
	</div>
	<GardenContext />
</div>
