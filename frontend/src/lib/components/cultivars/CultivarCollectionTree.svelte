<script lang="ts">
	import { createTreeView } from '@melt-ui/svelte';
	import { getLocalTimeZone, DateFormatter } from '@internationalized/date';
	import { Button } from 'bits-ui';
	import Icon from '@iconify/svelte';
	import iconIds from '$lib/assets/icons';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import * as Collapsible from '$lib/components/ui/collapsible';
	import * as Select from '$lib/components/ui/select';
	import * as Dialog from '$lib/components/ui/dialog';
	import { Textarea } from '$lib/components/ui/textarea/index.js';
	import { Field, Control, Label, FieldErrors, Description } from 'formsnap';
	import cultivarFields from '$lib/backendSchema/specs/cultivar';
	import { cultivarCollectionQuery } from '$data/cultivar/queries';
	import { superForm, defaults } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';
	import { CultivarCollectionFullSchemaVisibility } from '$codegen/types';
	import type {
		CultivarSchema,
		CultivarCollectionFullSchema,
		CultivarCollectionUpdateCommand
	} from '$codegen/types';
	import { cultivarCollectionUpdate } from '$data/cultivar/commands';
	import { createServerErrors } from '$state/formServerErrors.svelte';
	import CultivarTree from './CultivarTree.svelte';
	import FormInfoPopover from '$components/misc/FormInfoPopover.svelte';
	import FormErrorPopover from '$components/misc/FormErrorPopover.svelte';
	import CultivarCreateForm from './CultivarCreateForm.svelte';
	import TagsInput from '$components/ui/TagsInput.svelte';
	import debounce from '$lib/utils/debounce';

	/** Props. */
	type Props = {
		collectionId: string;
		gardenRef?: string | undefined;
	};
	let { collectionId, gardenRef = undefined }: Props = $props();

	/** Form mutations. */
	const collectionUpdateMutation = cultivarCollectionUpdate.mutation();
	/** Server errors. */
	const serverErrors = createServerErrors();

	/** Queries. */
	const collectionQuery = cultivarCollectionQuery({ ids: [collectionId] });

	const treeView = createTreeView();

	const {
		elements: { tree }
	} = treeView;

	/**
	 * Standard form configuration:
	 * - SPA: True disables server-side functionality.
	 * - validators: Zod schema specifies form validation.
	 * - onUpdate: Submission handler. Activates svelte-query mutation,
	 *  executes success task, and sets server errors on failure.
	 * - onChange: Reset server errors.
	 */
	const initialData: CultivarCollectionUpdateCommand = { collection_ref: collectionId };
	const form = superForm(defaults(initialData, zod(cultivarCollectionUpdate.schema)), {
		SPA: true,
		resetForm: true,
		validators: zod(cultivarCollectionUpdate.schema),
		onUpdate({ form }) {
			if (form.valid) {
				$collectionUpdateMutation.mutate(form.data, {
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

	/** Form submit function. */
	let debounceFormSubmit = debounce(() => {
		form.submit();
	}, 700);

	/* Defines the labels for the visibility enum options. */
	const visibilityOptions = [
		{ value: CultivarCollectionFullSchemaVisibility.private, label: 'Private' },
		{ value: CultivarCollectionFullSchemaVisibility.unlisted, label: 'Unlisted' },
		{ value: CultivarCollectionFullSchemaVisibility.public, label: 'Public' }
	];
	function visibilityEnumToOption(visibility: CultivarCollectionFullSchemaVisibility) {
		switch (visibility) {
			case CultivarCollectionFullSchemaVisibility.private:
				return visibilityOptions[0];
			case CultivarCollectionFullSchemaVisibility.unlisted:
				return visibilityOptions[1];
			case CultivarCollectionFullSchemaVisibility.public:
				return visibilityOptions[2];
		}
	}
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

	/** Creation datetime formatter. */
	const dateFormatter = new DateFormatter('en-US', {
		dateStyle: 'full',
		timeStyle: 'short',
		timeZone: getLocalTimeZone()
	});

	/** State. */
	let detailsOpen = $state(false); /** Controls the state of the Details collapsible. */
	let editingCollection =
		$state(false); /** True if the collection is in the editing state. */
	let cultivarCreateFormOpen =
		$state(false); /** Controls the open state of the cultivar creation dialog. */
	let cultivarSearch = $state(''); /** Used to filter the displayed cultivars. */
	let cultivarSort =
		$state('alphabetical'); /** Used to sort the displayed cultivars. */

	/**
	 * Filters and sorts the displayed cultivars based on the cultivar search and sort.
	 * Returns an array of indices of the original cultivar collection store.
	 */
	const sortedCollectionIndices = $derived.by(() => {
		if ($collectionQuery.data && $collectionQuery.data[0]?.cultivars) {
			const originalCultivars = $collectionQuery.data[0].cultivars;

			/** Create an array of indices. */
			let indices = originalCultivars.map((_, index) => index);

			/** Sort the indices based on the cultivars they point to. */
			indices.sort((a, b) => {
				const cultivarA = originalCultivars[a];
				const cultivarB = originalCultivars[b];

				switch (cultivarSort) {
					case 'alphabetical':
						return cultivarA.name.localeCompare(cultivarB.name);
					case 'reverseAlphabetical':
						return cultivarB.name.localeCompare(cultivarA.name);
					default:
						return 0; // No sorting
				}
			});

			/** Filter the indices based on the search term. */
			if (cultivarSearch) {
				indices = indices.filter((index) => {
					const cultivar = originalCultivars[index];
					return cultivar.name.toLowerCase().includes(cultivarSearch.toLowerCase());
				});
			}

			return indices;
		} else {
			return [];
		}
	});
</script>

{#snippet inlineErrors(formFieldName: string)}
	<FieldErrors let:errors let:errorAttrs class="flex items-center">
		{#each errors as err}
			<FormErrorPopover description={err} {errorAttrs} />
		{/each}
		{#each serverErrors.errors[formFieldName] as err}
			<FormErrorPopover description={err} {errorAttrs} />
		{/each}
	</FieldErrors>
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
				<h1 class="truncate text-2xl font-bold">{$collectionQuery.data[0].name}</h1>
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
					{#if editingCollection}
						<Field {form} name="description">
							<Control let:attrs>
								<div
									class="mx-2 flex items-center justify-between text-sm text-neutral-12"
								>
									<Label>Description</Label>
									<Description class="items center flex">
										<FormInfoPopover
											description={cultivarFields.cultivar_collection_description
												.description}
										/>
									</Description>
									{@render inlineErrors('cultivar_collection_description')}
									<div class="ml-4 h-[1px] flex-grow rounded-lg bg-neutral-3"></div>
								</div>
								<Textarea
									{...attrs}
									bind:value={$collectionQuery.data[0].description}
									on:input={() => {
										$formData.description = $collectionQuery.data[0].description;
										debounceFormSubmit();
									}}
									class="mx-2 mt-2 min-h-12 rounded-lg border border-neutral-4 bg-neutral-2 p-2 text-sm text-neutral-11 data-[fs-error]:border-destructive-7 data-[fs-error]:outline-destructive-6"
								/>
							</Control></Field
						>
					{:else}
						<div class="mx-2 flex items-center justify-between text-sm text-neutral-12">
							<span>Description</span>
							<div class="ml-4 h-[1px] flex-grow rounded-lg bg-neutral-3"></div>
						</div>
						<div
							class="m-2 rounded-lg border border-neutral-4 bg-neutral-2 p-2 text-sm text-neutral-11"
						>
							{#if $collectionQuery.data[0].description}
								<p>
									{$collectionQuery.data[0].description}
								</p>
							{:else}
								<span class="font-light italic text-neutral-10"> None </span>
							{/if}
						</div>
					{/if}
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
								<!-- Collection name. -->
								<li class="my-2 w-full">
									{#if editingCollection}
										<Field {form} name="name">
											<Control let:attrs>
												<div class="flex items-center justify-between">
													<div class="flex items-center">
														<Label class="ml-2 text-sm font-light text-neutral-11"
															>Name</Label
														>
														<Description class="items center flex">
															<FormInfoPopover
																description={cultivarFields.cultivar_collection_name
																	.description}
															/>
														</Description>
														{@render inlineErrors('cultivar_collection_name')}
													</div>
													<input
														{...attrs}
														type="text"
														bind:value={$collectionQuery.data[0].name}
														oninput={() => {
															$formData.name = $collectionQuery.data[0].name;
															debounceFormSubmit();
														}}
														class="rounded-md border bg-neutral-1 px-3 py-2 text-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary-6 focus-visible:ring-offset-2 data-[fs-error]:border-destructive-7 data-[fs-error]:outline-destructive-6"
													/>
												</div>
											</Control>
										</Field>
									{:else}
										<div class="flex items-center justify-between">
											<div class="flex items-center">
												<span class="ml-2 text-sm font-light text-neutral-11">Name</span
												>
												<FormInfoPopover
													description={cultivarFields.cultivar_collection_name
														.description}
												/>
											</div>
											<span
												class="w-auto py-2 text-right text-sm data-[fs-error]:outline-destructive-7"
												>{$collectionQuery.data[0].name}</span
											>
										</div>
									{/if}
								</li>
								<!-- Collection visibility. -->
								<li class="my-2 w-full">
									{#if editingCollection}
										<Field {form} name="visibility">
											<Control let:attrs>
												<div class="flex items-center justify-between">
													<div class="flex items-center">
														<Label class="ml-2 text-sm font-light text-neutral-11"
															>Visibility</Label
														>
														<Description class="items center flex">
															<FormInfoPopover
																description={cultivarFields
																	.cultivar_collection_visibility.description}
															/>
														</Description>
														<FieldErrors
															let:errors
															let:errorAttrs
															class="flex items-center"
														>
															{#each errors as err}
																<FormErrorPopover description={err} {errorAttrs} />
															{/each}
															{#each serverErrors.errors['cultivar_collection_visibility'] as err}
																<FormErrorPopover description={err} {errorAttrs} />
															{/each}
														</FieldErrors>
													</div>
													<Select.Root
														portal={null}
														loop={true}
														required={false}
														items={visibilityOptions}
														onSelectedChange={onVisibilitySelectedChange}
														selected={visibilityEnumToOption(
															$collectionQuery.data[0].visibility
														)}
													>
														<Select.Trigger
															chevron={editingCollection}
															class="ml-2 w-32 text-sm font-light text-neutral-11 disabled:cursor-auto"
														>
															<Select.Value placeholder="Private" />
														</Select.Trigger>
														<Select.Content>
															<Select.Group>
																{#each visibilityOptions as visibilityOption}
																	<Select.Item
																		class="text-neutral-11"
																		value={visibilityOption.value}
																		label={visibilityOption.label}
																		>{visibilityOption.label}</Select.Item
																	>
																{/each}
															</Select.Group>
														</Select.Content>
														<Select.Input
															{...attrs}
															name="cultivarCollectionVisibility"
														/>
													</Select.Root>
												</div>
											</Control>
										</Field>
									{:else}
										<div class="flex items-center justify-between">
											<div class="flex items-center">
												<span class="ml-2 text-sm font-light text-neutral-11"
													>Visibility</span
												>
												<FormInfoPopover
													description={cultivarFields.cultivar_collection_visibility
														.description}
												/>
											</div>
											<span class="py-2 text-right text-sm"
												>{visibilityEnumToOption($collectionQuery.data[0].visibility)
													.label}</span
											>
										</div>
									{/if}
								</li>
								<!-- Collection tags. -->
								<li class="my-2 w-full">
									{#if editingCollection}
										<Field {form} name="tags">
											<Control let:attrs>
												<div class="flex items-center justify-between">
													<div class="flex items-center">
														<Label class="ml-2 text-sm font-light text-neutral-11"
															>Tags</Label
														>
														<Description class="flex items-center">
															<FormInfoPopover
																description={cultivarFields.cultivar_collection_tags
																	.description}
															/>
														</Description>
														{@render inlineErrors('cultivar_collection_tags')}
													</div>
													<TagsInput
														bind:tagsInput={$collectionQuery.data[0].tags}
														maxTags={cultivarFields.cultivar_collection_tags.max_length
															.value}
														placeholder="Enter a tag"
														onChange={() => {
															$formData.tags = $collectionQuery.data[0].tags;
															debounceFormSubmit();
														}}
														formAttrs={attrs}
													/>
												</div>
											</Control></Field
										>
									{:else}
										<div class="flex items-center justify-between">
											<div class="flex items-center">
												<span class="ml-2 text-sm font-light text-neutral-11">Tags</span
												>
												<FormInfoPopover
													description={cultivarFields.cultivar_collection_tags
														.description}
												/>
											</div>
											<div
												class="rounded-lg border border-neutral-4 bg-neutral-1 p-2 text-right text-sm"
											>
												{#if $collectionQuery.data[0].tags.length > 0}
													{#each $collectionQuery.data[0].tags as tag}
														<span class="first:hidden"> , </span>
														<span>
															{tag}
														</span>
													{/each}
												{:else}
													<span class="font-light italic text-neutral-11"> None </span>
												{/if}
											</div>
										</div>
									{/if}
								</li>
								<!-- Collection inheritance - inherited from. -->
								{#if $collectionQuery.data[0].parent_ref}
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
								{/if}
								<!-- Collection creator. -->
								{#if $collectionQuery.data[0].user_ref}
									<li class="my-2 w-full">
										<div class="flex items-center justify-between">
											<span class="ml-2 text-sm font-light text-neutral-11"
												>Creator</span
											>
											<span
												class="text-md rounded-lg border border-neutral-4 bg-neutral-2 p-2"
												>TODO</span
											>
										</div>
									</li>
								{/if}
								<!-- Collection created at. -->
								{#if $collectionQuery.data[0].created_at}
									<li class="my-2 w-full">
										<div class="flex items-center justify-between">
											<span class="ml-2 text-sm font-light text-neutral-11"
												>Created at</span
											>
											<span class="p-2 text-right text-sm"
												>{dateFormatter.format(
													new Date($collectionQuery.data[0].created_at)
												)}</span
											>
										</div>
									</li>
								{/if}
							</ul>
						</Collapsible.Content>
					</Collapsible.Root>
				</div>
			</div>
		</form>

		<!-- Cultivars menu -->
		<div
			class="my-3 flex h-8 w-full items-center justify-between rounded-2xl border border-neutral-8 bg-neutral-2"
		>
			<Dialog.Root bind:open={cultivarCreateFormOpen}>
				<Dialog.Trigger
					class="flex h-full w-auto items-center rounded-l-2xl border-r border-neutral-7 hover:bg-neutral-3"
				>
					<Icon icon={iconIds.addIcon} width="1rem" class="ml-4 mr-3 sm:ml-6" />
					<span class="mr-6 hidden sm:block">Add</span>
				</Dialog.Trigger>
				<Dialog.Content>
					<Dialog.Header>
						<Dialog.Title>Add a Cultivar</Dialog.Title>
						<CultivarCreateForm
							collectionId={$collectionQuery.data[0].id}
							cultivars={$collectionQuery.data[0].cultivars}
							onSuccess={() => {
								cultivarCreateFormOpen = false;
							}}
						/>
					</Dialog.Header>
				</Dialog.Content>
			</Dialog.Root>
			<div
				class="group flex h-full w-auto flex-grow items-center border-r border-neutral-7 hover:bg-neutral-3"
			>
				<Icon icon={iconIds.searchIcon} width="1.25rem" class="ml-6 mr-3" />
				<input
					bind:value={cultivarSearch}
					placeholder="Search"
					class="mr-6 w-full bg-neutral-2 group-hover:bg-neutral-3"
				/>
				<Button.Root
					on:click={() => {
						cultivarSearch = '';
					}}
					class="h-full hover:bg-neutral-4"
				>
					<Icon icon={iconIds.defaultClose} width="1rem" class="ml-3 mr-3" />
				</Button.Root>
			</div>
			<DropdownMenu.Root>
				<DropdownMenu.Trigger
					class="flex h-full w-auto items-center rounded-r-2xl border-l border-neutral-7 hover:bg-neutral-3"
				>
					<Icon icon={iconIds.sortIcon} width="1rem" class="ml-3 mr-3 sm:ml-6" />
					<span class="mr-6 hidden sm:block">Sort</span>
				</DropdownMenu.Trigger>
				<DropdownMenu.Content>
					<DropdownMenu.RadioGroup bind:value={cultivarSort}>
						<DropdownMenu.RadioItem value="alphabetical">
							<Icon icon={iconIds.sortAlphaIcon} width="1.25rem" class="mr-2" />
							<span class="">Alphabetical</span>
						</DropdownMenu.RadioItem>
						<DropdownMenu.RadioItem value="reverseAlphabetical">
							<Icon icon={iconIds.sortReverseAlphaIcon} width="1.25rem" class="mr-2" />
							<span class="">Reverse alphabetical</span>
						</DropdownMenu.RadioItem>
					</DropdownMenu.RadioGroup>
				</DropdownMenu.Content>
			</DropdownMenu.Root>
		</div>

		<!-- Tree -->
		<ul class="overflow-none w-full" {...$tree}>
			<!-- Cultivar tree item. -->
			{#each sortedCollectionIndices ?? [] as index}
				<li class="w-full">
					<CultivarTree
						{treeView}
						collectionId={$collectionQuery.data[0].id}
						bind:cultivar={$collectionQuery.data[0].cultivars[index]}
						editing={editingCollection}
					/>
				</li>
			{/each}
		</ul>
	</div>
{/if}
