<script lang="ts">
	import { melt, createTreeView, type TreeView } from '@melt-ui/svelte';
	import Icon from '@iconify/svelte';
	import iconIds from '$lib/assets/icons';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import * as Popover from '$lib/components/ui/popover';
	import * as Collapsible from '$lib/components/ui/collapsible';
	import * as Select from '$lib/components/ui/select';
	import { Field, Control, Label, FieldErrors, Description } from 'formsnap';
	import cultivarFields from '$lib/backendSchema/specs/cultivar';
	import { cultivarCollectionQuery } from '$data/cultivar/queries';
	import InPlaceEdit from '$components/InPlaceEdit.svelte';
	import { superForm, defaults } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';
	import {
		CultivarCollectionCreateCommandVisibility,
		CultivarCollectionFullSchemaVisibility,
		CultivarCollectionUpdateCommandVisibility
	} from '$codegen/types';
	import type { CultivarSchema, CultivarCollectionFullSchema } from '$codegen/types';
	import { cultivarCollectionUpdate } from '$data/cultivar/commands';
	import { createServerErrors } from '$state/formServerErrors.svelte';
	import CultivarTree from './CultivarTree.svelte';
	import FormInfoPopover from '$components/misc/FormInfoPopover.svelte';
	import FormErrorPopover from '$components/misc/FormErrorPopover.svelte';


	/** Props. */
	type Props = {
		collectionId: string;
		gardenRef: string | undefined;
	};
	let { collectionId, gardenRef = undefined }: Props = $props();

	/** Form mutations. */
	const collectionUpdateMutation = cultivarCollectionUpdate.mutation();
	/** Server errors. */
	const serverErrors = createServerErrors();

	/** Queries. */
	const collectionQuery = cultivarCollectionQuery(
		{ ids: [collectionId] },
	);

	const treeView = createTreeView();

	const {
		elements: { tree, item, group },
		helpers: { isExpanded }
	} = treeView;

	const collection: CultivarCollectionFullSchema = {
		id: 'iaesnrt',
		description:
			"this is the description. west coast seeds is a seed company that operaties here in british columbia. It's where I get all my seeds personally its really graet and everything thianks",
		name: 'West Coast Seeds',
		slug: 'west-coast-seeds',
		tags: ['west coast', 'canada', 'native_plants'],
		visibility: CultivarCollectionFullSchemaVisibility.private,
		created_at: 'todo: figureout dt format',
		cultivars: [
			{
				id: 'iaosen',
				name: 'Lettuce',
				names: ['Lettuce', 'The green shit'],
				key: 'Le',
				description: 'Lettuce is a pretty good plant, I like making wraps with it.',
				attributes: {
					frost_date_planting_window_profile: {
						last_frost_window_open: 40,
						last_frost_window_close: null,
						first_frost_window_open: 20,
						first_frost_window_close: 30
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
		] as CultivarSchema[]
	};

	/**
	 * Standard form configuration:
	 * - SPA: True disables server-side functionality.
	 * - validators: Zod schema specifies form validation.
	 * - onUpdate: Submission handler. Activates svelte-query mutation,
	 *  executes success task, and sets server errors on failure.
	 * - onChange: Reset server errors.
	 */
	const form = superForm(defaults(zod(cultivarCollectionUpdate.schema)), {
		SPA: true,
		validators: zod(cultivarCollectionUpdate.schema),
		onUpdate({ form }) {
			if (form.valid) {
				$collectionUpdateMutation.mutate(form.data, {
					onSuccess: () => {
						/** TODO: Optimistic update. */
					},
					onError: (error) => {
						// @ts-ignore
						serverErrors.setErrors(error);
					}
				});
			}
		},
		onChange() {
			serverErrors.reset();
		}
	});
	const { form: formData, enhance } = form;

	/* Defines the labels for the visibility enum options. */
	const visibilityOptions = [
		{ value: CultivarCollectionFullSchemaVisibility.private, label: 'Private' },
		{ value: CultivarCollectionFullSchemaVisibility.unlisted, label: 'Unlisted' },
		{ value: CultivarCollectionFullSchemaVisibility.public, label: 'Public' }
	];

	function debounceFormSubmit() {}

	/**
	 * Used to update the visibility on the superforms when it changes on the form.
	 * Required as the value of the superform data can't be bound to the form value type.
	 */
	function onVisibilitySelectedChange(
		value: { value: CultivarCollectionFullSchemaVisibility; label?: string } | undefined
	) {
		if (value) {
			/** @ts-ignore */
			$formData.visibility = value.value;
			debounceFormSubmit();
		}
	}

	let detailsOpen = $state(false);
	let editingCollection = $state(false);
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
				<DropdownMenu.Trigger
					class="ml-2 rounded-lg border border-accent-6 bg-accent-4 p-2"
				>
					Options
				</DropdownMenu.Trigger>
				<DropdownMenu.Content>
					{#if editingCollection}
						<DropdownMenu.Item
							on:click={() => {
								editingCollection = false;
							}}
						>
							<Icon icon={iconIds.endEditingIcon} width="1.25rem" />
							<span class="mx-2"> End Editing </span>
						</DropdownMenu.Item>
					{:else}
						<DropdownMenu.Item
							on:click={() => {
								editingCollection = true;
							}}
						>
							<Icon icon={iconIds.startEditingIcon} width="1.25rem" />
							<span class="mx-2"> Edit Collection </span>
						</DropdownMenu.Item>
					{/if}
					<DropdownMenu.Item>
						<Icon icon={iconIds.inheritCultivarCollectionIcon} width="1.25rem" />
						<span class="mx-2"> Change Inheritance </span>
					</DropdownMenu.Item>
					<DropdownMenu.Item>
						<Icon icon={iconIds.mergeCultivarCollectionIcon} width="1.25rem" />
						<span class="mx-2"> Merge Collection </span>
					</DropdownMenu.Item>
					<DropdownMenu.Item>
						<Icon icon={iconIds.duplicateCultivarCollectionIcon} width="1.25rem" />
						<span class="mx-2"> Duplicate Collection </span>
					</DropdownMenu.Item>
					<DropdownMenu.Item>
						<Icon icon={iconIds.deleteIcon} width="1.25rem" />
						<span class="mx-2"> Delete Collection </span>
					</DropdownMenu.Item>
				</DropdownMenu.Content>
			</DropdownMenu.Root>
		</div>

		<!-- Collection info -->
		<form method="POST" use:enhance>
			<div>
				<div class="my-2">
					<div class="mx-2 flex items-center justify-between text-sm text-neutral-12">
						<span>Description</span>
						{#if editingCollection}
							<FormInfoPopover description={cultivarFields.cultivar_collection_description.description}/>
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
									<Field {form} name="visibility">
										<Control let:attrs>
											<div class="flex items-center justify-between">
												<div class="flex items-center">
													<span class="ml-2 text-sm font-light text-neutral-11"
														>Visibility</span
													>
													<FormInfoPopover description={cultivarFields.cultivar_collection_visibility.description} />
													<FieldErrors let:errors let:errorAttrs>
														{#each errors as err}
															<FormErrorPopover description={err} errorAttrs={errorAttrs}/>
														{/each}
														{#each serverErrors.errors['cultivar_collection_visibility'] as err}
															<FormErrorPopover description={err} errorAttrs={errorAttrs}/>
														{/each}
													</FieldErrors>
												</div>
												<Select.Root
													portal={null}
													loop={true}
													required={false}
													disabled={!editingCollection}
													items={visibilityOptions}
													onSelectedChange={onVisibilitySelectedChange}
													selected={{ value: collection.visibility, label: 'Private' }}
												>
													<Select.Trigger
														chevron={editingCollection}
														class="ml-2 w-28 text-sm font-light text-neutral-12 disabled:cursor-auto"
													>
														<Select.Value placeholder="Private" />
													</Select.Trigger>
													<Select.Content>
														<Select.Group>
															{#each visibilityOptions as visibilityOption}
																<Select.Item
																	value={visibilityOption.value}
																	label={visibilityOption.label}
																	>{visibilityOption.label}</Select.Item
																>
															{/each}
														</Select.Group>
													</Select.Content>
													<Select.Input
														{...attrs}
														name="cultivraCollectionVisibility"
													/>
												</Select.Root>
											</div>
										</Control>
									</Field>
								</li>
								<!-- Collection tags. -->
								<li class="my-2 w-full">
									<div class="flex items-center justify-between">
										<div class="flex items-center">
											<span class="ml-2 text-sm font-light text-neutral-11">Tags</span>
											<FormInfoPopover description={cultivarFields.cultivar_collection_tags.description} />
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
										<span class="ml-2 text-sm font-light text-neutral-11"
											>Created at</span
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
		</form>

		<!-- Cultivars menu -->
		<div class="my-3 h-8 w-full rounded-2xl border border-neutral-8 bg-neutral-3"></div>

		<!-- Tree -->
		<ul class="overflow-none w-full" {...$tree}>
			<!-- Cultivar tree item. -->
			{#each collection.cultivars as cultivar}
				<li class="w-full">
					<CultivarTree treeView={treeView} collectionRef={collection.id} cultivar={cultivar} />
				</li>
			{/each}
		</ul>
	</div>
{/if}
