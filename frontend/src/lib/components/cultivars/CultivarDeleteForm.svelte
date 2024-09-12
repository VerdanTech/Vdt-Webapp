<script lang="ts">
	import { useQueryClient } from '@sveltestack/svelte-query';
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import { superForm, defaults } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';
	import { cultivarDelete } from '$lib/data/cultivar/commands';
	import { createServerErrors } from '$state/formServerErrors.svelte';
	import TagsInput from '$components/ui/TagsInput.svelte';
	import cultivarFields from '$lib/backendSchema/specs/cultivar';
	import type { CultivarSchema } from '$codegen/types';
	import CultivarParentCombobox from './CultivarParentCombobox.svelte';

	type Props = {
		collectionId: string;
		cultivarId: string;
		onSuccess?: Function | undefined;
	};

	let { collectionId, cultivarId, onSuccess = undefined }: Props = $props();

	/* Form mutation. */
	const mutation = cultivarDelete.mutation();
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
	const initialData = { collection_ref: collectionId, cultivar_id: cultivarId };
	const form = superForm(defaults(initialData, zod(cultivarDelete.schema)), {
		SPA: true,
		validators: zod(cultivarDelete.schema),
		onUpdate({ form }) {
			if (form.valid) {
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
	<!-- Submit button -->
	<Form.Button
		disabled={false}
		loading={$mutation.isLoading}
		variant="destructive"
		class="mt-4 w-full">Delete</Form.Button
	>
</form>
