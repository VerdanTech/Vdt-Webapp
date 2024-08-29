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
		elements: { tree, item, group },
		helpers: { isExpanded }
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
				description: 'This is thhe cultivar description. I want to handle what ahppent when it gets really long mk This is thhe cultivar description. I want to handle what ahppent when it gets really long mk This is thhe cultivar description. I want to handle what ahppent when it gets really long mk This is thhe cultivar description. I want to handle what ahppent when it gets really long mk This is thhe cultivar description. I want to handle what ahppent when it gets really long mk',
				attributes: {
					frost_date_planting_window_profile: {
						last_frost_window_open: 40
					}
				}
			}
		]
	};

	let detailsOpen = $state(false);
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
<div class="4xl:w-7/12 m-auto mt-8 flex w-11/12 flex-col 2xl:w-7/12">
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
				<span>Description</span>
				<div class="h-[1px] flex-grow ml-4 rounded-lg bg-neutral-3"></div>
			</div>
			<p
				class="mx-2 mt-2 rounded-lg border border-neutral-4 bg-neutral-2 p-2 text-sm text-neutral-11"
			>
				{collection.description}
			</p>
		</div>
		<div class="my-2">
			<Collapsible.Root bind:open={detailsOpen}>
				<Collapsible.Trigger
					class="flex w-full items-center justify-between rounded-lg py-1 transition-colors hover:bg-neutral-3"
				>
					<span class="mx-2 text-sm text-neutral-12">Details</span>
					<div class="h-[1px] flex-grow ml-4 rounded-lg bg-neutral-3"></div>
					<Icon icon={iconIds.chevronRight} width="1.5rem" class="ml-2 {detailsOpen ? 'rotate-90' : ''}" />
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
	<div class="w-full bg-neutral-3 border border-neutral-8 h-8 rounded-2xl my-3">
		
	</div>

	<!-- Tree -->
	<ul class="overflow-none w-full" {...$tree}>
		<!-- Cultivar tree item. -->
		{#each collection.cultivars as cultivar}
			{@const hasProfiles = !!collection.cultivars?.length}
			{@const cultivarTreeId = cultivar.id}

			<li class="w-full">
				<button use:melt={$item({ id: cultivarTreeId, hasChildren: hasProfiles })} class="w-full select-none flex w-full items-center justify-between rounded-lg py-1 transition-colors hover:bg-neutral-3">
					<div class="overflow-hidden flex items-center">
						<span class="mx-2 text-lg font-bold text-neutral-12 truncate"> {cultivar.name} </span>
						{#if cultivar.key}
						<span class="w-1 h-l text-neutral-12">&#183;</span>
						<span class="mx-2 text-md italic">{cultivar.key}</span>
						{/if}
					</div>	
					<div class="h-[1px] rounded-lg bg-neutral-3 ml-4 flex-grow"></div>
					<Icon icon={iconIds.chevronRight} width="1.5rem" class="ml-2 {$isExpanded(cultivarTreeId) ? 'rotate-90' : ''}" />
				</button>

				<!-- Cultivar tree item children. -->
				<ul use:melt={$group({ id: cultivar.id })} class="w-full">
					<!-- Cultivar name tree item. -->
					<li class="my-2 ml-4 w-full">
						<div use:melt={$item({ id: cultivar.id + 'name' })} class="flex items-center justify-between rounded-lg">
								<span class="text-md font-light text-neutral-11">Name</span>
								<span class="text-md bg-neutral-2 p-2 rounded-lg">{cultivar.name}</span>
						</div>
					</li>
					<!-- Cultivar key tree item. -->
					<li class="my-2 ml-4 w-full">
						<div use:melt={$item({ id: cultivar.id + 'key' })} class="flex items-center justify-between rounded-lg">
							<span class="text-md text-neutral-11 font-light">Key</span>
							<span class="text-md bg-neutral-2 p-2 rounded-lg">{cultivar.key}</span>
						</div>
					</li>
					<!-- Cultivar description tree item. -->
					<li class="my-2 ml-4 w-full">
						<div use:melt={$item({ id: cultivar.id + 'description' })} class="flex items-center justify-between rounded-lg">
							<span class="text-md text-neutral-11 font-light">Description</span>
							<span class="text-md bg-neutral-2 p-2 rounded-lg text-wrap ml-8 md:ml-16 lg:ml-64">{cultivar.description}</span>
						</div>
					</li>

					<!-- Cultivar attribute profiles tree items. -->
					{#each Object.entries(cultivar.attributes) as [profileKey, profileValue]}
						{@const profileTreeId = cultivar.id + profileKey}
						{@const profileLabel = cultivarFields[profileKey].label}
						{@const profileDescription = cultivarFields[profileKey]?.description}
						{@const hasAttributes = true}

						<li class="ml-2 my-1">
							<button
								use:melt={$item({ id: profileTreeId, hasChildren: hasAttributes })} class="w-full select-none flex w-full items-center justify-between rounded-lg py-1 transition-colors hover:bg-neutral-3"
							>
									<span class="ml-2 text-md font-bold text-neutral-12 truncate">
										{profileLabel}
									</span>
									<div class="h-[1px] rounded-lg bg-neutral-3 ml-4 flex-grow"></div>
									<Icon icon={iconIds.chevronRight} width="1.5rem" class="ml-2 {$isExpanded(profileTreeId) ? 'rotate-90' : ''}" />
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
											<span class="text-sm text-neutral-11">
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
