<script lang="ts">
	import { goto } from '$app/navigation';
	import type { AxiosResponse, AxiosError } from 'axios';
	import Icon from '@iconify/svelte';
    import {Combobox} from 'bits-ui';
    import { flyAndScale } from "$lib/utils/index.js";
	import * as Form from '$lib/components/ui/form';
	import * as Select from '$lib/components/ui/select';
	import { Button } from '$lib/components/ui/button';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import { superForm, defaults } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';
	import { cultivarCreate } from '$lib/data/cultivar/commands';
	import { createServerErrors } from '$state/formServerErrors.svelte';
	import iconIds from '$lib/assets/icons';
	import TagsInput from '$components/ui/TagsInput.svelte';
	import cultivarFields from '$lib/backendSchema/specs/cultivar';
    import type {CultivarSchema} from '$codegen/types';

    type Props = {
        collectionRef: string;
        cultivars: CultivarSchema[];
    };

    let { collectionRef, cultivars }: Props = $props();

	/* Form mutation. */
	const mutation = cultivarCreate.mutation();
	/* Server error state. */
	const serverErrors = createServerErrors();

	/**
	 * Standard form configuration:
	 * - SPA: True disables server-side functionality.
	 * - validators: Zod schema specifies form validation.
	 * - onUpdate: Submission handler. Activates svelte-query mutation,
	 *  executes success task, and sets server errors on failure.
	 * - onChange: Reset server errors.
	 */
	const form = superForm(defaults(zod(cultivarCreate.schema)), {
		SPA: true,
		validators: zod(cultivarCreate.schema),
		onUpdate({ form }) {
            form.data.collection_ref = collectionRef;
			if (form.valid) {
				$mutation.mutate(form.data, {
					onSuccess: () => {
						/** TODO: Invalidate collection. */
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
			<Form.Label description={cultivarCreate.schema.shape.names.description}
				>Names</Form.Label
			>
            <TagsInput
                bind:tagsInput={$formData.names}
                placeholder="Enter a name"
                maxTags={cultivarFields.cultivar_names.max_length.value}
                onChange={() => {}}
                formAttrs={attrs} />
		</Form.Control>
        <Form.Description
        >Common names of the plant species.</Form.Description
    >
		<Form.FieldErrors serverErrors={serverErrors.errors['names']} />
	</Form.Field>

	<!-- Cultivar key -->
	<Form.Field {form} name="key">
		<Form.Control let:attrs>
			<Form.Label description={cultivarCreate.schema.shape.key.description}
				>Key</Form.Label
			>
			<Input
				{...attrs}
				type="text"
				placeholder="Ex. Le"
				bind:value={$formData.key}
			/>
		</Form.Control>
        <Form.Description
        >Short abbreviation used for visual identification.</Form.Description
    >
		<Form.FieldErrors serverErrors={serverErrors.errors['key']} />
	</Form.Field>

	<!-- Cultivar scientific name -->
	<Form.Field {form} name="scientific_name">
		<Form.Control let:attrs>
			<Form.Label description={cultivarCreate.schema.shape.scientific_name.description}
				>Scientific Name</Form.Label
			>
			<Input
				{...attrs}
				type="text"
				bind:value={$formData.scientific_name}
			/>
		</Form.Control>
		<Form.FieldErrors serverErrors={serverErrors.errors['scientific_name']} />
	</Form.Field>

    <!-- Cultivar description -->
    <Form.Field {form} name="description">
        <Form.Control let:attrs>
            <Form.Label description={cultivarCreate.schema.shape.description.description}
                >Description</Form.Label
            >
            <Textarea {...attrs} bind:value={$formData.description} />
        </Form.Control>
        <Form.FieldErrors serverErrors={serverErrors.errors['description']} />
    </Form.Field>

	<!-- Submit button -->
	<Form.Button
		disabled={false}
		loading={$mutation.isLoading}
		variant="default"
		class="mt-4 w-full">Create</Form.Button
	>
</form>
