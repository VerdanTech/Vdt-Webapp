<script lang="ts">
    import { melt, type TreeView } from '@melt-ui/svelte';
	import { CultivarSchema } from "$codegen/types"

    type Props = {
        treeView: TreeView
      cultivar: CultivarSchema   
    }

    let {treeView, cultivar}: Props = $props()
</script>

<li>
    
</li>