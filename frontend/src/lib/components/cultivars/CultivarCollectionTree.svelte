<script lang="ts">
	import { melt, createTreeView, type TreeView } from '@melt-ui/svelte';
	import { Separator } from "$lib/components/ui/separator";
	import type {
		CultivarCollectionFullSchema,
		CultivarAttributeSet
	} from '$codegen/types';
	import cultivarFields from '$lib/backendSchema/specs/cultivar';

	/**https://www.charpeni.com/blog/properly-type-object-keys-and-object-entries*/

	type Props = {
		collectionRef: string;
	};

	let { collectionRef }: Props = $props();

	const treeView = createTreeView();

	const {
		elements: { tree, item, group }
	} = treeView;

	const collection: CultivarCollectionFullSchema = {
		id: 'iaesnrt',
		description: 'this is the description. west coast seeds is a seed company that operaties here in british columbia. It\'s where I get all my seeds personally its really graet and everything thianks',
		name: '1234567890132456789013245678901234567986012306504123/06054',
		key: 'wcs',
		tags: ['canada', 'native_plants'],
		cultivars: [
			{
				id: 'iaosen',
				name: 'cultivar1',
				key: 'keyyy',
				attributes: {
					frost_date_planting_window_profile: {
						last_frost_window_open: 40
					}
				}
			}
		]
	};

</script>

<!--
  @component
  
  The cultivar collection tree component displays a cultivar collection
  using Melt's nested tree view component.
  This involves rendering each cultivar as a list item, which has children
  elements of the cultivar's name, key, etc. and each  of its attributes,
  where the children elements are the attributes.
  Most descriptions and field names are taken from the backend schema.
  The exception is that the type of the attributes requires different 
  input components with different types.
-->
<div class="flex w-full flex-col">
	<div class="flex flex-col gap-1 px-4 pt-4 w-full">
		<div class="flex flex-row items-center justify-between w-full">
			<div class="flex flex-row items-center">
				<h1 class="text-2xl font-bold py-1">{collection.name}</h1>
				<span>
					{collection.key}
				</span>
			</div>
			<div>
				Menubar
			</div>
		</div>

		<div>
			<span>
				Description
			</span>
			<p class="text-sm rounded-lg bg-neutral-2 text-neutral-11 p-2 border border-neutral-4">{collection.description}</p>
		</div>
		<Separator class="bg-neutral-7 rounded-md my-1"/>
	</div>

	<ul class="overflow-auto px-4 pb-4 pt-2" {...$tree}>
		<!-- Cultivar tree item. -->
		{#each collection.cultivars as cultivar}
			{@const hasProfiles = !!collection.cultivars?.length}

			<li>
				<button use:melt={$item({ id: cultivar.id, hasChildren: hasProfiles })}>
					<span class="select-none">
						{cultivar.name}
					</span>
				</button>

				<!-- Cultivar tree item children. -->
				<ul use:melt={$group({ id: cultivar.id })}>
					<!-- Cultivar key tree item. -->
					<li>
						<button use:melt={$item({ id: cultivar.id + 'key' })}>
							<span> Key </span>
						</button>
					</li>
					<!-- Cultivar description tree item. -->
					<li>
						<button use:melt={$item({ id: cultivar.id + 'description' })}>
							<span> Description </span>
						</button>
					</li>

					<!-- Cultivar attribute profiles tree items. -->
					{#each Object.entries(cultivar.attributes) as [profileKey, profileValue]}
						{@const profileTreeId = cultivar.id + profileKey}
						{@const profileLabel = cultivarFields[profileKey].label}
						{@const profileDescription = cultivarFields[profileKey]?.description}
						{@const hasAttributes = true}

						<li>
							<button
								use:melt={$item({ id: profileTreeId, hasChildren: hasAttributes })}
							>
								<span>
									{profileLabel}
								</span>
							</button>

							<!-- Cultivar attributes tree items. -->
							<ul use:melt={$group({ id: profileTreeId })}>
								{#each Object.entries(profileValue) as [attributeKey, attributeValue]}
									{@const attributeTreeId = cultivar.id + profileKey + attributeKey}
									{@const attributeLabel = cultivarFields[attributeKey].label}
									{@const attributeDescription =
										cultivarFields[attributeKey]?.description}
									{@const attributeUnit = cultivarFields[attributeKey]?.unit}
									<li>
										<button use:melt={$item({ id: attributeTreeId })}>
											<span>
												{attributeLabel}
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
