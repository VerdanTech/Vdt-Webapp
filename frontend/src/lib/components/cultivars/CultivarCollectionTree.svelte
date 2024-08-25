<script lang="ts">
	import { melt, createTreeView, type TreeView } from '@melt-ui/svelte'
	import CultivarCollection from './CultivarCollection.svelte'
	import type { CultivarCollectionFullSchema } from '$codegen/types'

	type Props = {
		collectionRef: string
	}

	let { collectionRef }: Props = $props()

	const treeView = createTreeView()

	const {
		elements: { tree, item, group }
	} = treeView

	const collection: CultivarCollectionFullSchema = {
		id: 'iaesnrt',
		description: 'this is the description',
		name: 'einstra',
		key: 'keykye',
		tags: ['canada', 'native_plants'],
		cultivars: [
			{
				id: 'iaosen',
				name: 'cultivar1',
				key: 'keyyy',
				attributes: {
					frost_date_planting_windows: {
						first_frost_window_close: 30,
						first_frost_window_open: 50,
						last_frost_window_close: 20,
						last_frost_window_open: 40
					}
				}
			}
		]
	}
  const hasChildren=true
</script>

<div class="flex w-full flex-col rounded-xl bg-neutral-2 text-neutral-12">
	<div class="flex flex-col gap-1 px-4 pt-4">
		<h3 class="text-lg font-bold">Project Structure</h3>
		<hr />
	</div>

		<ul class="overflow-auto px-4 pb-4 pt-2" {...$tree}>
			{#each collection.cultivars as cultivar}
      {@const hasProfiles=!!collection.cultivars?.length}

				<li>
					<button use:melt={$item({ id: cultivar.id , hasChildren: hasProfiles })}>
						<span class="select-none">
							{cultivar.name}
						</span>
					</button>

					<ul use:melt={$group({ id: cultivar.id })}>
						<li>
              <button use:melt={$item({ id: cultivar.id + 'key' })}>
              <span>
                Key
              </span>
              </button>
            </li>
						<li>
              <button use:melt={$item({ id: cultivar.id + 'description' })} >
                <span>
                  Description
                </span>
              </button>
            </li>
            {#each Object.entries(cultivar.attributes) as [profileKey, profileValue]}
            {@const profileTreeId = cultivar.id + profileKey}
            {@const profileName = "frost_dats"}
            {@const profileDescription = "description"}
            {@const hasAttributes=true}

            <li>
              <button use:melt={$item({ id: profileTreeId, hasChildren: hasAttributes })} >
                <span>
                  {profileName}
                </span>
              </button>

              <ul use:melt={$group({ id: profileTreeId })}>
                {#each Object.entries(cultivar.attributes[profileKey]) as attributeKey, attributeValue}
                  {@const attributeTreeId = cultivar.id + profileKey + attributeKey}
                  {@const attributeName = "date1"}
                  {@const attributeDescription = "description"}
                  {@const hasChildren=false}
                  <li>
                    <button use:melt={$item({ id: attributeTreeId })} >
                      <span>
                        {attributeName}
                      </span>
                    </button>
                  </li>
                {/each}

              </ul>
            </li>
            {/each}
					</ul>
				</li>
			{/each}
		</ul>
</div>
