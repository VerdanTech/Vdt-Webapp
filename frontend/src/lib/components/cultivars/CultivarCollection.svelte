<script lang="ts">
	import { melt, type TreeView } from '@melt-ui/svelte'
	import type { CultivarCollectionFullSchema } from '$codegen/types'
	import Cultivar from './Cultivar.svelte'

	type Props = {
		treeView: TreeView
		collection: CultivarCollectionFullSchema
	}

	let { treeView, collection }: Props = $props()

	const {
		elements: { item, group },
		helpers: { isExpanded, isSelected }
	} = treeView
</script>

<ul>
	{#each collection.cultivars as cultivar}
		<li>
			<button use:melt={$item({ id: cultivar.id })}>
				<span>
					{cultivar.name}
				</span>
			</button>

			<Cultivar {treeView} {cultivar} />
		</li>
	{/each}
</ul>
