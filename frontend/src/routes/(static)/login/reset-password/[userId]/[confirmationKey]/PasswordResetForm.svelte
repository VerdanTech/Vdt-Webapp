<script lang="ts">
	import { page } from '$app/stores';
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import { superForm, defaults } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';
	import { userConfirmPasswordReset } from '$lib/data/user/commands';
	import { createServerErrors } from '$state/formServerErrors.svelte';

	type Props = {
		/** Set to true once the form has been submitted and received a 200 response. */
		succeeded: boolean;
	};

	let { succeeded = $bindable(false) }: Props = $props();

	/* Form mutation. */
	const mutation = userConfirmPasswordReset.mutation();
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
	const initialData = {
		key: $page.params.confirmationKey,
		user_id: $page.params.userId,
		new_password1: '',
		new_password2: ''
	};
	const form = superForm(defaults(initialData, zod(userConfirmPasswordReset.schema)), {
		SPA: true,
		validators: zod(
			userConfirmPasswordReset.schema.refine(
				(data) => data.new_password1 == data.new_password2,
				{
					message: 'Passwords must match',
					path: ['password2']
				}
			)
		),
		onUpdate({ form }) {
			if (form.valid) {
				$mutation.mutate(form.data, {
					onSuccess: () => {
						succeeded = true;
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

<form method="POST" autocomplete="off" use:enhance>
	<!-- New Password1 -->
	<Form.Field {form} name="new_password1">
		<Form.Control let:attrs>
			<Form.Label
				description={userConfirmPasswordReset.schema.shape.new_password1.description}
				optional={userConfirmPasswordReset.schema.shape.new_password1.isOptional()}
				>New Password</Form.Label
			>
			<Input {...attrs} type="password" bind:value={$formData.new_password1} />
		</Form.Control>
		<Form.FieldErrors serverErrors={serverErrors.errors['password1']} />
	</Form.Field>

	<!-- Password2 -->
	<Form.Field {form} name="new_password2">
		<Form.Control let:attrs>
			<Form.Label
				description={userConfirmPasswordReset.schema.shape.new_password2.description}
				optoinal={userConfirmPasswordReset.schema.shape.new_password2.optional}
				>Confirm Password</Form.Label
			>
			<Input {...attrs} type="password" bind:value={$formData.new_password2} />
		</Form.Control>
		<Form.FieldErrors serverErrors={serverErrors.errors['new_password2']} />
	</Form.Field>

	<!-- Submit button -->
	<Form.Button
		disabled={false}
		loading={$mutation.isLoading}
		variant="default"
		class="mt-4 w-full">Submit</Form.Button
	>
</form>
