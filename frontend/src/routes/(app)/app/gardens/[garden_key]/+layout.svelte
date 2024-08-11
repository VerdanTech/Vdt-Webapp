<script>
	import GardenContext from './GardenContext.svelte'

	let { children } = $props()
</script>

<div class="flex h-full flex-col">
	<div class="grow">
		{@render children()}
	</div>
	<GardenContext />
</div>
