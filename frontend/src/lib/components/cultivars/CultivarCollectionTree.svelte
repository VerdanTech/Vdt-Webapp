<script lang="ts">
	import { melt, createTreeView, type TreeView } from '@melt-ui/svelte';
	import Icon from '@iconify/svelte';
	import iconIds from '$lib/assets/icons';
	import * as DropdownMenu from "$lib/components/ui/dropdown-menu";
	import * as Popover from '$lib/components/ui/popover';
	import * as Collapsible from '$lib/components/ui/collapsible';
	import cultivarFields from '$lib/backendSchema/specs/cultivar';
	import { cultivarCollectionQuery } from '$data/cultivar/queries';
	import InPlaceEdit from '$components/InPlaceEdit.svelte';

	/**https://www.charpeni.com/blog/properly-type-object-keys-and-object-entries*/

	/** Props. */
	type Props = {
		collectionId: string;
	};
	let { collectionId }: Props = $props();

	/** Queries. */
	const collectionQuery = cultivarCollectionQuery(
		{ ids: [collectionId] },
		{
			onSuccess: (data) => {
				console.log(data);
			}
		}
	);

	const treeView = createTreeView();

	const {
		elements: { tree, item, group },
		helpers: { isExpanded }
	} = treeView;

	const collection = {
		id: 'iaesnrt',
		description:
			"this is the description. west coast seeds is a seed company that operaties here in british columbia. It's where I get all my seeds personally its really graet and everything thianks",
		name: 'West Coast Seeds',
		slug: 'west-coast-seeds',
		tags: ['west coast', 'canada', 'native_plants'],
		visibility: "private",
		cultivars: [
			{
				id: 'iaosen',
				name: 'Lettuce',
				names: ['Lettuce', 'The green shit'],
				key: 'Le',
				description:
					'Lettuce is a pretty good plant, I like making wraps with it.',
				attributes: {
					frost_date_planting_window_profile: {
						last_frost_window_open: 40,
						last_frost_window_close: null,
						first_frost_window_open: 20,
						first_frost_window_close: 30,
					},
					origin_profile: {
						transplantable: true
					},
					annual_lifecycle_profile: {
						seed_to_germ: null,
						germ_to_transplant: 0,
						germ_to_first_harvest: null,
						first_to_last_harvest: 100
					}
				}
			}
		]
	};

	let detailsOpen = $state(false);
	let editingCollection = $state(false);
</script>

{#snippet infoPopover(description: string)}
	<Popover.Root>
		<Popover.Trigger class="w-8">
			<Icon
				icon={iconIds.formFieldDescriptionIcon}
				width="1rem"
				class="ml-2 text-neutral-11 hover:text-neutral-10"
			/>
		</Popover.Trigger>
		<Popover.Content class="max-w-2xl">
			{description}
		</Popover.Content>
	</Popover.Root>
{/snippet}

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
{#if $collectionQuery.status === 'loading'}
	<!-- TODO: Add skeleton loading -->
{:else if $collectionQuery.status === 'success'}
	<div class="4xl:w-7/12 m-auto mt-8 flex w-11/12 flex-col 2xl:w-7/12">
		<!-- Title -->
		<div class="flex w-full flex-row items-center justify-between">
			<div class="flex flex-row items-center overflow-hidden">
				<h1 class="truncate text-2xl font-bold">{collection.name}</h1>
			</div>
			<DropdownMenu.Root>
				<DropdownMenu.Trigger class="ml-2 rounded-lg border border-accent-6 bg-accent-4 p-2">
					Options
				</DropdownMenu.Trigger>
				<DropdownMenu.Content>
					{#if editingCollection}
					<DropdownMenu.Item on:click={() => {editingCollection=false}}>
						<Icon icon={iconIds.endEditingIcon} width="1.25rem" />
						<span class="mx-2">
							End Editing
						</span>
					</DropdownMenu.Item>
					{:else}
					<DropdownMenu.Item on:click={()=>{editingCollection=true}}>
						<Icon icon={iconIds.startEditingIcon} width="1.25rem" />
						<span class="mx-2">
							Edit Collection
						</span>
					</DropdownMenu.Item>
					{/if}
					<DropdownMenu.Item>
						<Icon icon={iconIds.inheritCultivarCollectionIcon} width="1.25rem" />
						<span class="mx-2">
							Change Inheritance
						</span>
					</DropdownMenu.Item>
					<DropdownMenu.Item>
						<Icon icon={iconIds.mergeCultivarCollectionIcon} width="1.25rem" />
						<span class="mx-2">
							Merge Collection
						</span>
					</DropdownMenu.Item>
					<DropdownMenu.Item>
						<Icon icon={iconIds.duplicateCultivarCollectionIcon} width="1.25rem" />
						<span class="mx-2">
							Duplicate Collection
						</span>
					</DropdownMenu.Item>
					<DropdownMenu.Item>
						<Icon icon={iconIds.deleteIcon} width="1.25rem" />
						<span class="mx-2">
							Delete Collection
						</span>
					</DropdownMenu.Item>
				</DropdownMenu.Content>
			</DropdownMenu.Root>
		</div>

		<!-- Details -->
		<div>
			<div class="my-2">
				<div class="mx-2 flex items-center justify-between text-sm text-neutral-12">
					<span>Description</span>
					{#if editingCollection}
					{@render infoPopover(cultivarFields.cultivar_collection_description.description)}
					{/if}
					<div class="ml-4 h-[1px] flex-grow rounded-lg bg-neutral-3"></div>
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
						<div class="ml-4 h-[1px] flex-grow rounded-lg bg-neutral-3"></div>
						<Icon
							icon={iconIds.chevronRight}
							width="1.5rem"
							class="ml-2 {detailsOpen ? 'rotate-90' : ''}"
						/>
					</Collapsible.Trigger>
					<Collapsible.Content class="mx-2 mt-2 text-neutral-11">
						<ul class="flex w-full flex-col">
							<!-- Collection visibility. -->
							<li class="my-2 w-full">
								<div class="flex items-center justify-between">
									<div class="flex items-center">
										<span class="ml-2 text-sm font-light text-neutral-11">Visibility</span
										>
										{#if editingCollection}
										{@render infoPopover(cultivarFields.cultivar_collection_visibility.description)}
										{/if}
									</div>
									<InPlaceEdit editing={editingCollection} value={collection.visibility}></InPlaceEdit>
									<!--
										<span
										class="text-md rounded-lg border border-neutral-4 bg-neutral-2 p-2"
										>tags</span
										>
									-->
								</div>
							</li>
							<!-- Collection tags. -->
							<li class="my-2 w-full">
								<div class="flex items-center justify-between">
									<div class="flex items-center">
										<span class="ml-2 text-sm font-light text-neutral-11">Tags</span>
										{#if editingCollection}
										{@render infoPopover(cultivarFields.cultivar_collection_tags.description)}
										{/if}
									</div>
									<span
										class="text-md rounded-lg border border-neutral-4 bg-neutral-2 p-2"
										>tags</span
									>
								</div>
							</li>
							<!-- Collection inheritance - inherited from. -->
							<li class="my-2 w-full">
								<div class="flex items-center justify-between">
									<span class="ml-2 text-sm font-light text-neutral-11"
										>Inherits from</span
									>
									<span
										class="text-md rounded-lg border border-neutral-4 bg-neutral-2 p-2"
										>TODO</span
									>
								</div>
							</li>
							<!-- Collection creator. -->
							<li class="my-2 w-full">
								<div class="flex items-center justify-between">
									<span class="ml-2 text-sm font-light text-neutral-11">Creator</span>
									<span
										class="text-md rounded-lg border border-neutral-4 bg-neutral-2 p-2"
										>TODO</span
									>
								</div>
							</li>
							<!-- Collection created at. -->
							<li class="my-2 w-full">
								<div class="flex items-center justify-between">
									<span class="ml-2 text-sm font-light text-neutral-11">Created at</span
									>
									<span
										class="text-md rounded-lg border border-neutral-4 bg-neutral-2 p-2"
										>tags</span
									>
								</div>
							</li>
						</ul>
					</Collapsible.Content>
				</Collapsible.Root>
			</div>
		</div>

		<!-- Cultivars menu -->
		<div class="my-3 h-8 w-full rounded-2xl border border-neutral-8 bg-neutral-3"></div>

		<!-- Tree -->
		<ul class="overflow-none w-full" {...$tree}>
			<!-- Cultivar tree item. -->
			{#each collection.cultivars as cultivar}
				{@const hasProfiles = !!collection.cultivars?.length}
				{@const cultivarTreeId = cultivar.id}

				<li class="w-full">
					<button
						use:melt={$item({ id: cultivarTreeId, hasChildren: hasProfiles })}
						class="flex w-full w-full select-none items-center justify-between rounded-lg py-1 transition-colors hover:bg-neutral-3"
					>
						<div class="flex items-center overflow-hidden">
							<span class="mx-2 truncate text-lg font-bold text-neutral-12">
								{cultivar.name}
							</span>
							{#if cultivar.key}
								<span class="h-l w-1 text-neutral-12">&#183;</span>
								<span class="text-md mx-2 italic">{cultivar.key}</span>
							{/if}
						</div>
						<div class="h-[1px] flex-grow rounded-lg bg-neutral-3"></div>
						<Icon
							icon={iconIds.chevronRight}
							width="1.5rem"
							class="ml-2 {$isExpanded(cultivarTreeId) ? 'rotate-90' : ''}"
						/>
					</button>

					<!-- Cultivar tree item children. -->
					<ul use:melt={$group({ id: cultivar.id })} class="w-full">
						<!-- Details tree item -->
						<li class="my-2 w-full">
							<button
								use:melt={$item({ id: cultivar.id + 'details', hasChildren: true })}
								class="flex w-full items-center justify-between rounded-lg py-1 transition-colors hover:bg-neutral-3"
							>
								<span class="text-md ml-6 truncate font-medium text-neutral-12">
									Details
								</span>
								<div class="ml-4 h-[1px] flex-grow rounded-lg bg-neutral-3"></div>
								<Icon
									icon={iconIds.chevronRight}
									width="1.5rem"
									class="ml-2 {$isExpanded(cultivar.id + 'details') ? 'rotate-90' : ''}"
								/>
							</button>

							<ul use:melt={$group({ id: cultivar.id + 'details' })} class="w-full">
								<!-- Cultivar name tree item. -->
								<li class="my-2 w-full">
									<div
										use:melt={$item({ id: cultivar.id + 'name' })}
										class="flex items-center justify-between"
									>
										<span class="ml-10 text-sm font-light text-neutral-11">Name</span>
										<span
											class="text-md rounded-lg border border-neutral-4 bg-neutral-2 p-2"
											>{cultivar.names}</span
										>
									</div>
								</li>
								<!-- Cultivar key tree item. -->
								<li class="my-2 w-full">
									<div
										use:melt={$item({ id: cultivar.id + 'key' })}
										class="flex items-center justify-between"
									>
										<span class="ml-10 text-sm font-light text-neutral-11">Key</span>
										<span
											class="text-md rounded-lg border border-neutral-4 bg-neutral-2 p-2"
											>{cultivar.key}</span
										>
									</div>
								</li>
								<!-- Cultivar description tree item. -->
								<li class="my-2 w-full">
									<div
										use:melt={$item({ id: cultivar.id + 'description' })}
										class="flex items-center justify-between"
									>
										<span class="ml-10 text-sm font-light text-neutral-11"
											>Description</span
										>
										<span
											class="text-md ml-8 text-wrap rounded-lg border border-neutral-4 bg-neutral-2 p-2 md:ml-16 lg:ml-64"
											>{cultivar.description}</span
										>
									</div>
								</li>
							</ul>
						</li>

						<!-- Cultivar attribute profiles tree items. -->
						{#if cultivar.attributes}
							{#each Object.entries(cultivar.attributes) as [profileKey, profileValue]}
								{@const profileTreeId = cultivar.id + profileKey}
								{@const profileLabel = cultivarFields[profileKey as keyof typeof cultivarFields]?.label}
								{@const profileDescription = cultivarFields[profileKey as keyof typeof cultivarFields]?.description}
								{@const hasAttributes = true}

								<li class="my-1">
									<button
										use:melt={$item({ id: profileTreeId, hasChildren: hasAttributes })}
										class="flex w-full items-center justify-between rounded-lg py-1 transition-colors hover:bg-neutral-3"
									>
										<span class="text-md ml-6 truncate font-medium text-neutral-12">
											{profileLabel}
										</span>
										{@render infoPopover(profileDescription)}
										<div class="ml-4 h-[1px] flex-grow rounded-lg bg-neutral-3"></div>
										<Icon
											icon={iconIds.chevronRight}
											width="1.5rem"
											class="ml-2 {$isExpanded(profileTreeId) ? 'rotate-90' : ''}"
										/>
									</button>

									<!-- Cultivar attributes tree items. -->
									{#if profileValue}
										<ul use:melt={$group({ id: profileTreeId })}>
											{#each Object.entries(profileValue) as [attributeKey, attributeValue]}
												{@const attributeTreeId =
													cultivar.id + profileKey + attributeKey}
												{@const attributeLabel = cultivarFields[attributeKey as keyof typeof cultivarFields]?.label}
												{@const attributeDescription =
													cultivarFields[attributeKey as keyof typeof cultivarFields]?.description}
												{@const attributeUnit = cultivarFields[attributeKey as keyof typeof cultivarFields]?.unit}
												<li class="my-2 flex w-full items-center justify-between">
													<button
														use:melt={$item({ id: attributeTreeId })}
														class="flex w-auto items-center"
													>
														<span class="ml-10 text-sm text-neutral-11">
															{attributeLabel}
														</span>
														{@render infoPopover(attributeDescription)}
													</button>
													<div class="flex items-center">
														<span
															class="mx-2 rounded-lg border border-neutral-4 bg-neutral-2 px-4 py-2"
														>
															20
														</span>
														<span>
															{attributeUnit}
														</span>
													</div>
												</li>
											{/each}
										</ul>
									{/if}
								</li>
							{/each}
						{/if}
					</ul>
				</li>
			{/each}
		</ul>
	</div>
{/if}
