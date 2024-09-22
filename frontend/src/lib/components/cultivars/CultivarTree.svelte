<script lang="ts">
	import { melt, createTreeView, type TreeView } from '@melt-ui/svelte';
	import Icon from '@iconify/svelte';
	import iconIds from '$lib/assets/icons';
	import { Field, Control, Label, FieldErrors, Description } from 'formsnap';
	import cultivarFields from '$lib/backendSchema/specs/cultivar';
	import { superForm, defaults } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';
	import type { CultivarSchema, CultivarUpdateCommand } from '$codegen/types';
	import { cultivarUpdate } from '$data/cultivar/commands';
	import { createServerErrors } from '$state/formServerErrors.svelte';
	import FormInfoPopover from '$components/misc/FormInfoPopover.svelte';
	import FormErrorPopover from '$components/misc/FormErrorPopover.svelte';
	import * as Dialog from '$lib/components/ui/dialog';
	import { Textarea } from '$lib/components/ui/textarea/index.js';
	import TagsInput from '$components/ui/TagsInput.svelte';
	import CultivarDeleteForm from './CultivarDeleteForm.svelte';
	import debounce from '$lib/utils/debounce';
	import { attributeKeyToComponent } from './attributes';

	type Props = {
		collectionId: string;
		cultivar: CultivarSchema;
		treeView: TreeView;
		editing: boolean;
	};

	let { collectionId, cultivar = $bindable(), treeView, editing }: Props = $props();

	/** State. */
	let cultivarDeleteFormOpen =
		$state(false); /** Controls the open state of the cultivar deletion form. */

	/** Form mutations. */
	const collectionUpdateMutation = cultivarUpdate.mutation();
	/** Server errors. */
	const serverErrors = createServerErrors();

	/**
	 * Standard form configuration:
	 * - SPA: True disables server-side functionality.
	 * - validators: Zod schema specifies form validation.
	 * - onUpdate: Submission handler. Activates svelte-query mutation,
	 *  executes success task, and sets server errors on failure.
	 * - onChange: Reset server errors.
	 */
	const initialData: CultivarUpdateCommand = {
		collection_ref: collectionId,
		cultivar_id: cultivar.id
	};
	const form = superForm(defaults(initialData, zod(cultivarUpdate.schema)), {
		SPA: true,
		id: 'cultivarUpdateForm/' + cultivar.id,
		dataType: 'json',
		resetForm: true,
		validators: zod(cultivarUpdate.schema),
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
	const { form: formData, errors, enhance } = form;

	let debounceFormSubmit = debounce(() => {
		form.submit();
	}, 1000);

	const {
		elements: { item, group },
		helpers: { isExpanded }
	} = treeView;
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

{#snippet inlineAttributeErrors(profileKey: string, attributeKey: string)}
	<FieldErrors let:errorAttrs class="flex items-center">
		{#each $errors.attributes?.[profileKey]?.[attributeKey] as err}
			<FormErrorPopover description={err} {errorAttrs} />
		{/each}
		<!-- TODO: If the errors returned by the backend are nested, change this. -->
		{#each serverErrors.errors[attributeKey] as err}
			<FormErrorPopover description={err} {errorAttrs} />
		{/each}
	</FieldErrors>
{/snippet}

<div class="flex items-center">
	<button
		use:melt={$item({ id: cultivar.id, hasChildren: true })}
		class="flex w-full select-none items-center justify-between rounded-lg py-1 transition-colors hover:bg-neutral-3"
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
			class="ml-2 {$isExpanded(cultivar.id) ? 'rotate-90' : ''}"
		/>
	</button>

	{#if editing}
		<Dialog.Root bind:open={cultivarDeleteFormOpen}>
			<Dialog.Trigger class="ml-2">
				<Icon
					icon={iconIds.deleteIcon}
					width="1.25rem"
					class="text-destructive-9 hover:text-destructive-10"
				/>
			</Dialog.Trigger>
			<Dialog.Content>
				<Dialog.Header>
					<Dialog.Title>
						<span> Deleting </span>
						<span class="font-bold italic">
							{cultivar.name}
						</span>
					</Dialog.Title>
					<Dialog.Description
						>Make sure you want to proceed. This action is irreversible.</Dialog.Description
					>
					<CultivarDeleteForm
						{collectionId}
						cultivarId={cultivar.id}
						onSuccess={() => {
							cultivarDeleteFormOpen = false;
						}}
					/>
				</Dialog.Header>
			</Dialog.Content>
		</Dialog.Root>
	{/if}
</div>

<!-- Cultivar tree item children. -->
<form method="POST" use:enhance>
	<ul use:melt={$group({ id: cultivar.id })} class="w-full">
		<!-- Details tree item -->
		<li class="my-2 w-full">
			<button
				use:melt={$item({ id: cultivar.id + 'details', hasChildren: true })}
				class="flex w-full items-center justify-between rounded-lg py-1 transition-colors hover:bg-neutral-3"
			>
				<span class="text-md ml-6 truncate font-medium text-neutral-12"> Details </span>
				<div class="ml-4 h-[1px] flex-grow rounded-lg bg-neutral-3"></div>
				<Icon
					icon={iconIds.chevronRight}
					width="1.5rem"
					class="ml-2 {$isExpanded(cultivar.id + 'details') ? 'rotate-90' : ''}"
				/>
			</button>

			<ul use:melt={$group({ id: cultivar.id + 'details' })} class="w-full">
				<!-- Cultivar names tree item. -->
				<li class="my-2 w-full">
					<div>
						{#if editing}
							<Field {form} name="names">
								<Control let:attrs>
									<div class="flex items-center justify-between">
										<div class="flex items-center">
											<Label class="ml-10 text-sm font-light text-neutral-11"
												>Names</Label
											>
											<Description class="flex items-center">
												<FormInfoPopover
													description={cultivarFields.cultivar_names.description}
												/>
											</Description>
											{@render inlineErrors('cultivar_names')}
										</div>
										<TagsInput
											bind:tagsInput={cultivar.names}
											maxTags={cultivarFields.cultivar_names.max_length.value}
											placeholder="Enter a name"
											onChange={() => {
												console.log(cultivar.names);
												$formData.names = cultivar.names;
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
									<span class="ml-10 text-sm font-light text-neutral-11">Names</span>
									<FormInfoPopover
										description={cultivarFields.cultivar_names.description}
									/>
								</div>
								<div
									class="rounded-lg border border-neutral-4 bg-neutral-1 p-2 text-right text-sm"
								>
									{#each cultivar.names as name}
										<span class="first:hidden"> , </span>
										<span>
											{name}
										</span>
									{/each}
								</div>
							</div>
						{/if}
					</div>
				</li>
				<!-- Cultivar key tree item. -->
				<li class="my-2 w-full">
					<div>
						{#if editing}
							<Field {form} name="key">
								<Control let:attrs>
									<div class="flex items-center justify-between">
										<div class="flex items-center">
											<Label class="ml-10 text-sm font-light text-neutral-11">Key</Label
											>
											<Description class="flex items-center">
												<FormInfoPopover
													description={cultivarFields.cultivar_key.description}
												/>
											</Description>
											{@render inlineErrors('cultivar_key')}
										</div>
										<input
											{...attrs}
											type="text"
											bind:value={cultivar.key}
											oninput={() => {
												$formData.key = cultivar.key;
												debounceFormSubmit();
											}}
											class="rounded-md border bg-neutral-1 px-3 py-2 text-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary-6 focus-visible:ring-offset-2 data-[fs-error]:border-destructive-7 data-[fs-error]:outline-destructive-6"
										/>
									</div>
								</Control></Field
							>
						{:else}
							<div class="flex items-center justify-between">
								<div class="flex items-center">
									<span class="ml-10 text-sm font-light text-neutral-11">Key</span>
									<FormInfoPopover
										description={cultivarFields.cultivar_key.description}
									/>
								</div>
								<div class="p-2 text-right text-sm">
									<span
										class="w-auto py-2 text-right text-sm data-[fs-error]:outline-destructive-7"
										>{cultivar.key}</span
									>
								</div>
							</div>
						{/if}
					</div>
				</li>
				<!-- Cultivar scientific name tree item. -->
				<li class="my-2 w-full">
					{#if editing}
						<Field {form} name="scientific_name">
							<Control let:attrs>
								<div class="flex items-center justify-between">
									<div class="flex items-center">
										<Label class="ml-10 text-sm font-light text-neutral-11"
											>Scientific Name</Label
										>
										<Description class="flex items-center">
											<FormInfoPopover
												description={cultivarFields.cultivar_scientific_name
													.description}
											/>
										</Description>
										{@render inlineErrors('cultivar_scientific_name')}
									</div>
									<input
										{...attrs}
										type="text"
										bind:value={cultivar.scientific_name}
										oninput={() => {
											$formData.scientific_name = cultivar.scientific_name;
											debounceFormSubmit();
										}}
										placeholder="None"
										class="rounded-md border bg-neutral-1 px-3 py-2 text-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary-6 focus-visible:ring-offset-2 data-[fs-error]:border-destructive-7 data-[fs-error]:outline-destructive-6"
									/>
								</div>
							</Control></Field
						>
					{:else}
						<div class="flex items-center justify-between">
							<div class="flex items-center">
								<span class="ml-10 text-sm font-light text-neutral-11"
									>Scientific Name</span
								>
								<FormInfoPopover
									description={cultivarFields.cultivar_scientific_name.description}
								/>
							</div>
							<div class="rounded-lg p-2 text-right text-sm">
								{#if cultivar.scientific_name}
									<span
										class="w-auto py-2 text-right text-sm data-[fs-error]:outline-destructive-7"
										>{cultivar.scientific_name}</span
									>
								{:else}
									<span class="font-light italic text-neutral-11"> None </span>
								{/if}
							</div>
						</div>
					{/if}
				</li>
				<!-- Cultivar description tree item. -->
				<li class="my-2 w-full">
					{#if editing}
						<Field {form} name="description">
							<Control let:attrs>
								<div class="flex items-center justify-between">
									<div class="flex items-center">
										<Label class="ml-10 text-sm font-light text-neutral-11"
											>Description</Label
										>
										<Description class="flex items-center">
											<FormInfoPopover
												description={cultivarFields.cultivar_description.description}
											/>
										</Description>
										{@render inlineErrors('cultivar_description')}
									</div>
									<Textarea
										{...attrs}
										bind:value={cultivar.description}
										oninput={() => {
											$formData.description = cultivar.description;
											debounceFormSubmit();
										}}
										placeholder="None"
										class="rounded-md border bg-neutral-1 px-3 py-2 text-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary-6 focus-visible:ring-offset-2 data-[fs-error]:border-destructive-7 data-[fs-error]:outline-destructive-6"
									/>
								</div>
							</Control></Field
						>
					{:else}
						<div class="flex items-center justify-between">
							<div class="flex items-center">
								<span class="ml-10 text-sm font-light text-neutral-11">Description</span
								>
								<FormInfoPopover
									description={cultivarFields.cultivar_description.description}
								/>
							</div>
							<div class="rounded-lg border border-neutral-4 p-2 text-right text-sm">
								{#if cultivar.description}
									<span
										class="w-auto py-2 text-right text-sm data-[fs-error]:outline-destructive-7"
										>{cultivar.description}</span
									>
								{:else}
									<span class="font-light italic text-neutral-11"> None </span>
								{/if}
							</div>
						</div>
					{/if}
				</li>
				<!-- Cultivar parent tree item. -->
				<li class="my-2 w-full">
					<div
						use:melt={$item({ id: cultivar.id + 'parent' })}
						class="flex items-center justify-between"
					>
						<span class="ml-10 text-sm font-light text-neutral-11">Inherits from</span>
						<span
							class="text-md ml-8 text-wrap rounded-lg border border-neutral-4 bg-neutral-2 p-2 md:ml-16 lg:ml-64"
							>todo</span
						>
					</div>
				</li>
			</ul>
		</li>

		<!-- Cultivar attribute profiles tree items. -->
		{#if cultivar.attributes}
			{#each Object.entries(cultivar.attributes) as [profileKey, profileValue]}
				{@const profileTreeId = cultivar.id + profileKey}
				{@const profileLabel =
					cultivarFields[profileKey as keyof typeof cultivarFields]?.label}
				{@const profileDescription =
					cultivarFields[profileKey as keyof typeof cultivarFields]?.description}
				{@const hasAttributes = true}

				<li class="my-1">
					<button
						use:melt={$item({ id: profileTreeId, hasChildren: hasAttributes })}
						class="flex w-full items-center justify-between rounded-lg py-1 transition-colors hover:bg-neutral-3"
					>
						<span class="text-md ml-6 truncate font-medium text-neutral-12">
							{profileLabel}
						</span>
						<FormInfoPopover description={profileDescription} />
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
							{#each Object.entries(cultivar.attributes[profileKey]) as [attributeKey, attributeValue]}
								{@const attributeLabel =
									cultivarFields[attributeKey as keyof typeof cultivarFields]?.label}
								{@const attributeDescription =
									cultivarFields[attributeKey as keyof typeof cultivarFields]
										?.description}
								<li class="my-2 flex w-full items-center">
									{#if editing}
										<Field {form} name={attributeKey}>
											<Control let:attrs>
												<div class="flex w-full items-center justify-between text-sm">
													<div class="flex items-center">
														<Label class="ml-10 text-sm font-light text-neutral-11"
															>{attributeLabel}</Label
														>
														<Description class="flex items-center">
															<FormInfoPopover description={attributeDescription} />
														</Description>
														{@render inlineAttributeErrors(profileKey, attributeKey)}
													</div>
													<svelte:component
														this={attributeKeyToComponent(attributeKey)}
														formAttrs={attrs}
														{attributeKey}
														bind:value={cultivar.attributes[profileKey][attributeKey]}
														{editing}
														onChange={() => {
															$formData.attributes[profileKey][attributeKey] =
																cultivar.attributes[profileKey][attributeKey];
															debounceFormSubmit();
															console.log(profileKey);
															console.log(attributeKey);
															console.log($formData);
														}}
													/>
												</div>
											</Control></Field
										>
									{:else}
										<div class="flex w-full items-center justify-between">
											<div class="flex items-center">
												<span class="ml-10 text-sm font-light text-neutral-11"
													>{attributeLabel}</span
												>
												<FormInfoPopover description={attributeDescription} />
											</div>
											<div class="p-2 text-right text-sm">
												<svelte:component
													this={attributeKeyToComponent(attributeKey)}
													{attributeKey}
													bind:value={cultivar.attributes[profileKey][attributeKey]}
													{editing}
												/>
											</div>
										</div>
									{/if}
								</li>
							{/each}
						</ul>
					{/if}
				</li>
			{/each}
		{/if}
	</ul>
</form>
