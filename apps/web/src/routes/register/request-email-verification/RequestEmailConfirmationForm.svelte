<script lang="ts">
	import { defaults, superForm } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';

	import { userFields } from '@vdg-webapp/models';
	import { Form, Input } from '@vdg-webapp/ui';

	import { userRequestEmailConfirmation } from '$data/users/commands';
	import createCommandHandler from '$state/commandHandler.svelte';

	type Props = {
		/** Set to true once the form has been submitted and received a 200 response. */
		succeeded: boolean;
		/** Set to the registered email after success. */
		registeredEmail: string;
	};

	let { succeeded = $bindable(false), registeredEmail = $bindable('') }: Props =
		$props();

	let formHandler = createCommandHandler(userRequestEmailConfirmation.mutation, {
		onSuccess: () => {
			succeeded = true;
		}
	});
	const form = superForm(defaults(zod(userRequestEmailConfirmation.schema)), {
		SPA: true,
		validators: zod(userRequestEmailConfirmation.schema),
		onUpdate({ form }) {
			if (form.valid) {
				registeredEmail = form.data.email;
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

	<!-- Submit button -->
	<Form.Button
		disabled={false}
		loading={formHandler.isLoading}
		variant="default"
		class="mt-4 w-full">Submit</Form.Button
	>
</form>
