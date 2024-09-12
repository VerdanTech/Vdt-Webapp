<script lang="ts">
	import { goto } from '$app/navigation';
	import { useQueryClient } from '@sveltestack/svelte-query';
	import type { AxiosResponse, AxiosError } from 'axios';
	import Icon from '@iconify/svelte';
	import * as Form from '$lib/components/ui/form';
	import * as Select from '$lib/components/ui/select';
	import { Button } from '$lib/components/ui/button';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import { superForm, defaults } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';
	import { gardenCreate } from '$lib/data/garden/commands';
	import { createServerErrors } from '$state/formServerErrors.svelte';
	import iconIds from '$lib/assets/icons';
	import { GardenCreateCommandVisibility } from '$codegen/types';
	import { gardenGenerateUniqueKeyQuery } from '$data/garden/queries';
	import GardenCreateFormUserTagsInput from './GardenCreateFormUserTagsInput.svelte';

	const queryClient = useQueryClient();

	/* Form mutation. */
	const mutation = gardenCreate.mutation();
	/* Server error state. */
	const serverErrors = createServerErrors();

	/** Key generation query.*/
	/** Manage the loading state ourselves as for some reason the svelte-query one doesn't work correctly with the form. */
	let keyGenerationLoading = $state(true);
	const gardenGenerateUniqueKey = gardenGenerateUniqueKeyQuery({
		onSuccess: (data) => {
			if (!data) {
				return;
			}
			keyGenerationLoading = false;
			// @ts-ignore
			$formData.key = data.key;
		},
		onError: (error) => {
			if (!error) {
				return;
			}
			keyGenerationLoading = false;
			// @ts-ignore
			serverErrors.setErrors(error);
		},
		/** Don't re-request keys. */
		staleTime: Infinity
	});
	/* Request the query. */
	$gardenGenerateUniqueKey;

	/* Defines the labels for the visibility enum options. */
	const visibilityOptions = [
		{ value: GardenCreateCommandVisibility.private, label: 'Private' },
		{ value: GardenCreateCommandVisibility.unlisted, label: 'Unlisted' },
		{ value: GardenCreateCommandVisibility.public, label: 'Public' }
	];
	const defaultVisibility = visibilityOptions[0];

	/**
	 * Used to update the visibility on the superforms when it changes on the form.
	 * Required as the value of the superform data can't be bound to the form value type.
	 */
	function onVisibilitySelectedChange(
		value: { value: GardenCreateCommandVisibility; label?: string } | undefined
	) {
		if (value) {
			$formData.visibility = value.value;
		}
	}

	/**
	 * Standard form configuration:
	 * - SPA: True disables server-side functionality.
	 * - validators: Zod schema specifies form validation.
	 * - onUpdate: Submission handler. Activates svelte-query mutation,
	 *  executes success task, and sets server errors on failure.
	 * - onChange: Reset server errors.
	 */
	const form = superForm(defaults(zod(gardenCreate.schema)), {
		SPA: true,
		validators: zod(gardenCreate.schema),
		onUpdate({ form }) {
			if (form.valid) {
				$mutation.mutate(form.data, {
					onSuccess: () => {
						/**
						 * TODO: Move this state update to the data layer.
						 * It is here because having both onSuccess callbacks
						 * caused only the first to be run.
						 */
						goto('/app/gardens/' + form.data.key);
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
</script>

<form method="POST" use:enhance>
	<!-- Garden name -->
	<Form.Field {form} name="name">
		<Form.Control let:attrs>
			<Form.Label
				description={gardenCreate.schema.shape.name.description}
				optional={gardenCreate.schema.shape.name.isOptional()}>Name</Form.Label
			>
			<Input
				{...attrs}
				type="text"
				placeholder="Gardens of Adonis"
				bind:value={$formData.name}
			/>
		</Form.Control>
		<Form.FieldErrors serverErrors={serverErrors.errors['name']} />
	</Form.Field>

	<!-- Garden key -->
	<Form.Field {form} name="key">
		<Form.Control let:attrs>
			<Form.Label
				description={gardenCreate.schema.shape.key.description}
				optional={gardenCreate.schema.shape.key.isOptional()}>Key</Form.Label
			>
			<span class="flex">
				<!--
				-->
				<Input
					{...attrs}
					type="text"
					placeholder="lettuce123"
					class="rounded-r-none"
					bind:value={$formData.key}
				/>
				<Button
					variant="outline"
					on:click={() => {
						queryClient.invalidateQueries('uniqueGardenKey');
						keyGenerationLoading = true;
					}}
					class="flex items-center rounded-l-none border-l-0 bg-neutral-1 hover:bg-neutral-2 dark:border-neutral-12"
				>
					<Icon
						icon={iconIds.defaultRefreshIcon}
						width="1.5rem"
						class={keyGenerationLoading ? 'animate-spin' : ''}
					/>
				</Button>
			</span>
		</Form.Control>
		<Form.Description>Readable identifier, used in URLs.</Form.Description>
		<Form.FieldErrors serverErrors={serverErrors.errors['key']} />
	</Form.Field>

	<!-- Garden visibility -->
	<Form.Field {form} name="visibility">
		<Form.Control let:attrs>
			<Form.Label
				description={gardenCreate.schema.shape.visibility.description}
				optional={gardenCreate.schema.shape.visibility.isOptional()}
				>Visibility</Form.Label
			>
			<Select.Root
				portal={null}
				loop={true}
				onSelectedChange={onVisibilitySelectedChange}
				required={true}
				items={visibilityOptions}
				selected={defaultVisibility}
			>
				<Select.Trigger>
					<Select.Value {...attrs} placeholder="Private" />
				</Select.Trigger>
				<Select.Content>
					<Select.Group>
						<Select.Label>Garden Visibility</Select.Label>
						{#each visibilityOptions as visibilityOption}
							<Select.Item value={visibilityOption.value} label={visibilityOption.label}
								>{visibilityOption.label}</Select.Item
							>
						{/each}
					</Select.Group>
				</Select.Content>
				<Select.Input {...attrs} name="gardenVisibility" />
			</Select.Root>
		</Form.Control>
		<Form.Description
			>Private gardens can only be viewed by members. Unlisted gardens can be viewed by
			anyone with a link. Public gardens are searchable.</Form.Description
		>
		<Form.FieldErrors serverErrors={serverErrors.errors['visibility']} />
	</Form.Field>

	<!-- Garden description -->
	<Form.Field {form} name="description">
		<Form.Control let:attrs>
			<Form.Label
				description={gardenCreate.schema.shape.description.description}
				optional={gardenCreate.schema.shape.description.isOptional()}
				>Description</Form.Label
			>
			<Textarea {...attrs} bind:value={$formData.description} />
		</Form.Control>
		<Form.FieldErrors serverErrors={serverErrors.errors['description']} />
	</Form.Field>

	<!-- Admins to invite -->
	<Form.Field {form} name="admin_usernames">
		<Form.Control let:attrs>
			<Form.Label
				description={gardenCreate.schema.shape.admin_usernames.description}
				optional={gardenCreate.schema.shape.admin_usernames.isOptional()}
				>Admin Invites</Form.Label
			>
			<GardenCreateFormUserTagsInput
				bind:tagsInput={$formData.admin_usernames}
				formAttrs={attrs}
			/>
		</Form.Control>
		<Form.Description>Admins have full control over the garden.</Form.Description>
		<Form.FieldErrors serverErrors={serverErrors.errors['admin_usernames']} />
	</Form.Field>

	<!-- Editors to invite -->
	<Form.Field {form} name="editor_usernames">
		<Form.Control let:attrs>
			<Form.Label
				description={gardenCreate.schema.shape.editor_usernames.description}
				optional={gardenCreate.schema.shape.editor_usernames.isOptional()}
				>Editor Invites</Form.Label
			>
			<GardenCreateFormUserTagsInput
				bind:tagsInput={$formData.editor_usernames}
				formAttrs={attrs}
			/>
		</Form.Control>
		<Form.Description
			>Editors have limited write access but cannot change garden configuration.</Form.Description
		>
		<Form.FieldErrors serverErrors={serverErrors.errors['editor_usernames']} />
	</Form.Field>

	<!-- Viewers to invite -->
	<Form.Field {form} name="viewer_usernames">
		<Form.Control let:attrs>
			<Form.Label
				description={gardenCreate.schema.shape.viewer_usernames.description}
				optional={gardenCreate.schema.shape.viewer_usernames.isOptional()}
				>Viewer Invites</Form.Label
			>
			<GardenCreateFormUserTagsInput
				bind:tagsInput={$formData.viewer_usernames}
				formAttrs={attrs}
			/>
		</Form.Control>
		<Form.Description
			>Viewers can make no changes but can view everything.</Form.Description
		>
		<Form.FieldErrors serverErrors={serverErrors.errors['viewer_usernames']} />
	</Form.Field>

	<!-- Submit button -->
	<Form.Button
		disabled={false}
		loading={$mutation.isLoading}
		variant="default"
		class="mt-4 w-full">Create</Form.Button
	>
</form>
