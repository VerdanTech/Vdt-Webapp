<script lang="ts">
	import { Button } from '$components/ui/button'

	type Props = {
		gardenKey: string
		gardenName: string
	}

	let { gardenKey, gardenName }: Props = $props()
</script>

<Button
	variant="outline"
	class="flex h-48 w-64 flex-col justify-around bg-neutral-2 text-xl hover:bg-neutral-3 mx-4"
>
	<p class="h-auto max-h-32 w-full max-w-full overflow-hidden text-wrap">
		{gardenName}
	</p>
	<span
		class="max-w-full truncate rounded-md bg-primary-3 p-1 text-sm text-neutral-10 text-primary-11"
	>
		{gardenKey}
	</span>
</Button>
