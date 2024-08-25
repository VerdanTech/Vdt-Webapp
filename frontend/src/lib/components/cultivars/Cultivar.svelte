<script lang="ts">
	import { melt, type TreeView } from '@melt-ui/svelte'
	import type { CultivarSchema } from '$codegen/types'

	type Props = {
		treeView: TreeView
		cultivar: CultivarSchema
	}

	let { treeView, cultivar }: Props = $props()

	const {
		elements: { item, group },
		helpers: { isExpanded, isSelected }
	} = treeView
</script>

<ul use:melt={$group({ id: cultivar.id })}>
	<li use:melt={$item({ id: cultivar.id + 'key' })}>Key</li>
	<li use:melt={$item({ id: cultivar.id + 'description' })}>Description</li>
</ul>
