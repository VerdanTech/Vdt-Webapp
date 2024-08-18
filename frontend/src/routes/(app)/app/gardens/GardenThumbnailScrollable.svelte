<script lang="ts">
	import type { GardenPartialSchema } from '$codegen/types'
	import { ScrollArea } from '$lib/components/ui/scroll-area/index.js'
	import GardenThumbnail from './GardenThumbnail.svelte'

	type Props = {
		gardenPartials: GardenPartialSchema[]
	}

	let { gardenPartials }: Props = $props()
    console.log(gardenPartials)
</script>

<ScrollArea type="hover" orientation="horizontal" class="mt-8 h-auto w-full">
    <div class="flex flex-row">
	{#each gardenPartials as garden}
			<GardenThumbnail gardenKey={garden.key} gardenName={garden.name} />
            {/each}
        </div>
        </ScrollArea>
