
<script lang="ts">
    import { melt, createTreeView, type TreeView } from '@melt-ui/svelte';
    import { setContext } from 'svelte';
    import CultivarCollection from './CultivarCollection.svelte';
    import type {CultivarCollectionFullSchema} from '$codegen/types'

    type Props = {
        collectionRef: string
    }

    let {collectionRef}: Props = $props()

    const treeView = createTreeView()
    setContext(collectionRef, treeView)

    const {elements: {tree}} = treeView

    const cultivarCollectionFullSchema: CultivarCollectionFullSchema = {
        id: "iaesnrt",
        description: "this is the description",
        name: "einstra",
        key: "keykye",
        tags: ["canada", "native_plants"],
        cultivars: [{
            id: "iaosen",
            name: "cultivar1",
            key: "keyyy",
            attributes: {
                frost_date_planting_windows: {
                    first_frost_window_close: 30,
                    first_frost_window_open: 50,
                    last_frost_window_close: 20,
                    last_frost_window_open: 40,
                }
            }
        }]
    }

</script>

<div
  class="flex w-full flex-col rounded-xl bg-neutral-2 text-neutral-12 "
>
  <div class="flex flex-col gap-1 px-4 pt-4">
    <h3 class="text-lg font-bold">Project Structure</h3>
    <hr />
  </div>

  <div class="overflow-auto px-4 pb-4 pt-2" {...$tree}>
    <CultivarCollection treeView={treeView} collection={cultivarCollectionFullSchema}></CultivarCollection>
  </div>
</div>