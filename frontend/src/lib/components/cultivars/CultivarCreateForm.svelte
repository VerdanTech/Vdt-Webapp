<script lang="ts">
	import { useQueryClient } from '@sveltestack/svelte-query';
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import { superForm, defaults } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';
	import { cultivarCreate } from '$lib/data/cultivar/commands';
	import { createServerErrors } from '$state/formServerErrors.svelte';
	import TagsInput from '$components/ui/TagsInput.svelte';
	import cultivarFields from '$lib/backendSchema/specs/cultivar';
	import type { CultivarCreateCommand, CultivarSchema } from '$codegen/types';
	import CultivarParentCombobox from './CultivarParentCombobox.svelte';

	type Props = {
		collectionId: string;
		cultivars: CultivarSchema[];
		onSuccess?: Function | undefined;
	};

	let { collectionId, cultivars, onSuccess = undefined }: Props = $props();

	/* Form mutation. */
	const mutation = cultivarCreate.mutation();
	/* Server error state. */
	const serverErrors = createServerErrors();

	const queryClient = useQueryClient();

	/**
	 * Standard form configuration:
	 * - SPA: True disables server-side functionality.
	 * - validators: Zod schema specifies form validation.
	 * - onUpdate: Submission handler. Activates svelte-query mutation,
	 *  executes success task, and sets server errors on failure.
	 * - onChange: Reset server errors.
	 */
	const initialData: CultivarCreateCommand = {
		collection_ref: collectionId,
		names: []
	};
	const form = superForm(defaults(initialData, zod(cultivarCreate.schema)), {
		SPA: true,
		validators: zod(cultivarCreate.schema),
		onUpdate({ form }) {
			if (form.valid) {
				// @ts-ignore
				$mutation.mutate(form.data, {
					onSuccess: () => {
						queryClient.invalidateQueries(['cultivarCollections', [collectionId]]);
						if (onSuccess) {
							onSuccess();
						}
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
	<!-- Cultivar names -->
	<Form.Field {form} name="names">
		<Form.Control let:attrs>
			<Form.Label
				description={cultivarCreate.schema.shape.names.description}
				optional={cultivarCreate.schema.shape.names.isOptional()}>Names</Form.Label
			>
			<TagsInput
				bind:tagsInput={$formData.names}
				placeholder="Enter a name"
				maxTags={cultivarFields.cultivar_names.max_length.value}
				onChange={() => {}}
				formAttrs={attrs}
			/>
		</Form.Control>
		<Form.Description>Common names of the plant species.</Form.Description>
		<Form.FieldErrors serverErrors={serverErrors.errors['names']} />
	</Form.Field>

	<!-- Cultivar key -->
	<Form.Field {form} name="key">
		<Form.Control let:attrs>
			<Form.Label
				description={cultivarCreate.schema.shape.key.description}
				optional={cultivarCreate.schema.shape.key.isOptional()}>Key</Form.Label
			>
			<Input {...attrs} type="text" placeholder="Ex. Le" bind:value={$formData.key} />
		</Form.Control>
		<Form.Description
			>Short abbreviation used for visual identification. If not defined, one will be
			generated.</Form.Description
		>
		<Form.FieldErrors serverErrors={serverErrors.errors['key']} />
	</Form.Field>

	<!-- Cultivar scientific name -->
	<Form.Field {form} name="scientific_name">
		<Form.Control let:attrs>
			<Form.Label
				description={cultivarCreate.schema.shape.scientific_name.description}
				optional={cultivarCreate.schema.shape.scientific_name.isOptional()}
				>Scientific Name</Form.Label
			>
			<Input {...attrs} type="text" bind:value={$formData.scientific_name} />
		</Form.Control>
		<Form.FieldErrors serverErrors={serverErrors.errors['scientific_name']} />
	</Form.Field>

	<!-- Cultivar description -->
	<Form.Field {form} name="description">
		<Form.Control let:attrs>
			<Form.Label
				description={cultivarCreate.schema.shape.description.description}
				optional={cultivarCreate.schema.shape.description.isOptional()}
				>Description</Form.Label
			>
			<Textarea {...attrs} bind:value={$formData.description} />
		</Form.Control>
		<Form.FieldErrors serverErrors={serverErrors.errors['description']} />
	</Form.Field>

	<!-- Cultivar parent-->
	<Form.Field {form} name="parent_id">
		<Form.Control let:attrs>
			<Form.Label optional={cultivarCreate.schema.shape.parent_id.isOptional()}
				>Parent</Form.Label
			>
			<CultivarParentCombobox
				{collectionId}
				{cultivars}
				bind:value={$formData.parent_id}
			/>
		</Form.Control>
		<Form.Description
			>A cultivar may choose a parent, from which it will inherit its attributes. This
			allows to compose and override varieties.</Form.Description
		>
		<Form.FieldErrors serverErrors={serverErrors.errors['parent_id']} />
	</Form.Field>

	<!-- Submit button -->
	<Form.Button
		disabled={false}
		loading={$mutation.isLoading}
		variant="default"
		class="mt-4 w-full">Create</Form.Button
	>
</form>
