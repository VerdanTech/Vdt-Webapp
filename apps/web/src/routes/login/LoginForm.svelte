<script lang="ts">
	import { defaults, superForm } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';

	import { userFields } from '@vdg-webapp/models';
	import { Form, Input } from '@vdg-webapp/ui';

	import { goto } from '$app/navigation';
	import { userLogin } from '$data/users/auth';
	import createCommandHandler from '$state/commandHandler.svelte';

	let formHandler = createCommandHandler(userLogin.mutation, {
		onSuccess: () => {
			goto('/');
		}
	});
	const form = superForm(defaults(zod(userLogin.schema)), {
		SPA: true,
		resetForm: false,
		validators: zod(userLogin.schema),
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

<form method="POST" use:enhance>
	<!-- Email address -->
	<Form.Field {form} name="email">
		<Form.Control>
			{#snippet children({ props })}
				<Form.Label description={userFields.emailField.description}>Email</Form.Label>
				<Input.Root
					{...props}
					type="email"
					placeholder="email@example.com"
					bind:value={$formData.email}
				/>
			{/snippet}
		</Form.Control>
		<Form.FieldErrors handlerErrors={formHandler.fieldErrors?.email} />
	</Form.Field>

	<!-- Password -->
	<Form.Field {form} name="password">
		<Form.Control>
			{#snippet children({ props })}
				<Form.Label description={userFields.passwordField.description}
					>Password</Form.Label
				>
				<Input.Root {...props} type="password" bind:value={$formData.password} />
			{/snippet}
		</Form.Control>
		<Form.FieldErrors handlerErrors={formHandler.fieldErrors?.password} />
	</Form.Field>

	<!-- Non-field errors. -->
	<Form.NonFieldErrors handlerErrors={formHandler.nonFieldErrors} />

	<!-- Submit button -->
	<Form.Button
		disabled={false}
		loading={formHandler.isLoading}
		variant="default"
		class="mt-2 w-full">Submit</Form.Button
	>
</form>
