
<script lang="ts">
    import { melt, createTreeView, type TreeView } from '@melt-ui/svelte';
    import { setContext } from 'svelte';
  
    type Props = {
        cultivar_collection_ref: string
    }

    let {cultivar_collection_ref}: Props = $props()

</script>