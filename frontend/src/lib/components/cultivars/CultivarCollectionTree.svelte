<script lang="ts">
	import { melt, createTreeView, type TreeView } from '@melt-ui/svelte';
	import Icon from '@iconify/svelte';
	import iconIds from '$lib/assets/icons';
	import { Separator } from '$lib/components/ui/separator';
	import * as Collapsible from '$lib/components/ui/collapsible';
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
		description:
			"this is the description. west coast seeds is a seed company that operaties here in british columbia. It's where I get all my seeds personally its really graet and everything thianks",
		name: '12345678901234567890123456789012345678901234567890',
		key: 'wcs',
		tags: ['canada', 'native_plants'],
		cultivars: [
			{
				id: 'iaosen',
				name: '12345678901234567890123456789012345678901234567890',
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
<div class="4xl:w-9/12 m-auto mt-8 flex w-10/12 w-full flex-col 2xl:w-10/12">
	<!-- Title -->
	<div class="flex w-full flex-row items-center justify-between">
		<div class="flex flex-row items-center overflow-hidden">
			<h1 class="truncate text-2xl font-bold">{collection.name}</h1>
		</div>
		<div class="rounded-lg bg-accent-4 p-2 ml-2">Options</div>
	</div>

	<!-- Details -->
	<div>
		<div class="my-2">
			<div class="mx-2 flex items-center justify-between text-sm text-neutral-12">
				<span> Description </span>
				<div class="h-[1px] w-full mx-2 rounded-lg bg-neutral-3"></div>
			</div>
			<p
				class="mx-2 mt-2 rounded-lg border border-neutral-4 bg-neutral-2 p-2 text-sm text-neutral-11"
			>
				{collection.description}
			</p>
		</div>
		<div class="my-2">
			<Collapsible.Root>
				<Collapsible.Trigger
					class="flex w-full items-center justify-between rounded-lg py-1 transition-colors hover:bg-neutral-3"
				>
					<span class="mx-2 text-sm text-neutral-12"> Details </span>
					<div class="h-[1px] w-full rounded-lg bg-neutral-3 mx-2"></div>
					<Icon icon={iconIds.chevronRight} width="1.5rem" class="mx-2" />
				</Collapsible.Trigger>
				<Collapsible.Content
					class="mx-2 mt-2 rounded-lg border border-neutral-4 bg-neutral-2 p-2 text-sm text-neutral-11"
				>
					Yes. Free to use for personal and commercial projects. No attribution
					required.
				</Collapsible.Content>
			</Collapsible.Root>
		</div>
	</div>

	<!-- Cultivars menu -->
	<div class="w-full bg-neutral-3 border border-neutral-8 h-8 rounded-2xl my-2">
		
	</div>

	<!-- Tree -->
	<ul class="overflow-none w-full" {...$tree}>
		<!-- Cultivar tree item. -->
		{#each collection.cultivars as cultivar}
			{@const hasProfiles = !!collection.cultivars?.length}

			<li class="w-full">
				<button use:melt={$item({ id: cultivar.id, hasChildren: hasProfiles })} class="w-full select-none flex w-full items-center justify-between rounded-lg py-1 transition-colors hover:bg-neutral-3">
					<div class="overflow-hidden flex items-center">
						<span class="mx-2 text-md font-bold text-neutral-12 truncate"> {cultivar.name} </span>
						{#if cultivar.key}
						<span class="mx-1 w-1 h-l text-neutral-12">&#183;</span>
						<span class="mx-2 text-sm italic">{cultivar.key}</span>
						{/if}
					</div>	
						<div class="h-[1px] w-full rounded-lg bg-neutral-3 mx-2"></div>
						<Icon icon={iconIds.chevronRight} width="1.5rem" class="mx-2" />
				</button>

				<!-- Cultivar tree item children. -->
				<ul use:melt={$group({ id: cultivar.id })} class="pl-2 w-full">
					<!-- Cultivar name tree item. -->
					<li class="ml-2 w-full">
						<div use:melt={$item({ id: cultivar.id + 'name' })}>
							<div class="flex items-center justify-between rounded-lg">
								<span class="text-sm font-light text-neutral-11"> Name </span>
								<span class="text-sm">{cultivar.name}</span>
							</div>
						</div>
					</li>
					<!-- Cultivar key tree item. -->
					<li class="ml-2 w-full">
						<div use:melt={$item({ id: cultivar.id + 'key' })}>
							<span class="text-sm font-light"> Key </span>
						</div>
					</li>
					<!-- Cultivar description tree item. -->
					<li class="ml-2 w-full">
						<div use:melt={$item({ id: cultivar.id + 'description' })}>
							<span class="text-sm font-light"> Description </span>
						</div>
					</li>

					<!-- Cultivar attribute profiles tree items. -->
					{#each Object.entries(cultivar.attributes) as [profileKey, profileValue]}
						{@const profileTreeId = cultivar.id + profileKey}
						{@const profileLabel = cultivarFields[profileKey].label}
						{@const profileDescription = cultivarFields[profileKey]?.description}
						{@const hasAttributes = true}

						<li class="ml-2">
							<button
								use:melt={$item({ id: profileTreeId, hasChildren: hasAttributes })}
							>
								<span class="text-sm">
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
