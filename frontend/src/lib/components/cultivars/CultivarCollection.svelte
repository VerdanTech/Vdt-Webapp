
<script lang="ts">
    import { melt, createTreeView, type TreeView } from '@melt-ui/svelte';
    import { setContext } from 'svelte';
    import type {CultivarCollectionResult} from '$codegen/types/cultivarCollectionResult'

    type Props = {
        collectionRef: string
    }

    let {collectionRef}: Props = $props()

    const treeView = createTreeView()
    setContext(collectionRef, treeView)

    const {elements: {tree}} = treeView

    const CultivarCollectionResult = {
        description: "this is the description",
        key: "keykye",
        tags: ["canada", "native_plants"],
        cultivars: [{
            name: "cultivar1",
            key: "keyyy",
            attributes: [{
                frost_date_planting_windows: {
                    first_frost_window_close: 30,
                    first_frost_window_open: 50,
                    last_frost_window_close: 20,
                    last_frost_window_open: 40,
                }
            }]
        }]
    }

</script>

<div
  class="flex h-[18.75rem] w-[18.75rem] flex-col rounded-xl bg-white text-neutral-900 md:h-[350px]"
>
  <div class="flex flex-col gap-1 px-4 pt-4">
    <h3 class="text-lg font-bold">Project Structure</h3>
    <hr />
  </div>

  <ul class="overflow-auto px-4 pb-4 pt-2" {...$tree}>
  </ul>
</div>