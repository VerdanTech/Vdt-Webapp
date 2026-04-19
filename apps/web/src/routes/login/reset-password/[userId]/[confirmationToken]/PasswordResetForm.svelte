<script lang="ts">
	import { defaults, superForm } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';

	import { userFields } from '@vdg-webapp/models';
	import { Form, Input } from '@vdg-webapp/ui';

	import { page } from '$app/state';
	import { userConfirmPasswordReset } from '$data/users/commands';
	import createCommandHandler from '$state/commandHandler.svelte';

	type Props = {
		/** Set to true once the form has been submitted and received a 200 response. */
		succeeded: boolean;
	};
	let { succeeded = $bindable(false) }: Props = $props();

	let formHandler = createCommandHandler(userConfirmPasswordReset.mutation, {
		onSuccess: () => {
			succeeded = true;
		}
	});
	const initialData = {
		userId: page.params.userId,
		token: page.params.confirmationToken,
		password1: '',
		password2: ''
	};
	const form = superForm(defaults(initialData, zod(userConfirmPasswordReset.schema)), {
		SPA: true,
		validators: zod(userConfirmPasswordReset.schema),
		onUpdate({ form }) {
			if (form.valid) {
				formHandler.execute(form.data);
			}
		},
		onChange() {
			formHandler.reset();
		}
	});
	const { form: formData, enhance } = form;
</script>

<form method="POST" autocomplete="off" use:enhance>
	<!-- New Password1 -->
	<Form.Field {form} name="password1">
		<Form.Control>
			{#snippet children({ props })}
				<Form.Label description={userFields.passwordField.description}
					>New Password</Form.Label
				>
				<Input.Root {...props} type="password" bind:value={$formData.password1} />
			{/snippet}
		</Form.Control>
		<Form.FieldErrors handlerErrors={formHandler.fieldErrors?.password1} />
	</Form.Field>

	<!-- New Password2 -->
	<Form.Field {form} name="password2">
		<Form.Control>
			{#snippet children({ props })}
				<Form.Label description={userFields.passwordField.description}
					>Confirm Password</Form.Label
				>
				<Input.Root {...props} type="password" bind:value={$formData.password2} />
			{/snippet}
		</Form.Control>
		<Form.FieldErrors handlerErrors={formHandler.fieldErrors?.password2} />
	</Form.Field>

	<!-- Submit button -->
	<Form.Button
		disabled={false}
		loading={formHandler.isLoading}
		variant="default"
		class="mt-4 w-full">Submit</Form.Button
	>
</form>
