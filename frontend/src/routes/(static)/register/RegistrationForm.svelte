<script lang="ts">
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import { superForm, defaults } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';
	import { userCreate } from '$lib/data/user/commands';
	import { createServerErrors } from '$state/formServerErrors.svelte';

	type Props = {
		/** Set to true once the form has been submitted and received a 200 response. */
		succeeded: boolean;
		/** Set to the registered email after success. */
		registeredEmail: string;
	};

	let { succeeded = $bindable(false), registeredEmail = $bindable('') }: Props =
		$props();

	/* Form mutation. */
	const mutation = userCreate.mutation();
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
	const form = superForm(defaults(zod(userCreate.schema)), {
		SPA: true,
		validators: zod(
			userCreate.schema.refine((data) => data.password1 == data.password2, {
				message: 'Passwords must match',
				path: ['password2']
			})
		),
		onUpdate({ form }) {
			if (form.valid) {
				registeredEmail = form.data.email_address;
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
	<!-- Username -->
	<Form.Field {form} name="username">
		<Form.Control let:attrs>
			<Form.Label
				description={userCreate.schema.shape.username.description}
				optional={userCreate.schema.shape.username.isOptional()}>Username</Form.Label
			>
			<Input
				{...attrs}
				type="text"
				autocomplete="false"
				placeholder="username"
				bind:value={$formData.username}
			/>
		</Form.Control>
		<Form.FieldErrors serverErrors={serverErrors.errors['username']} />
	</Form.Field>

	<!-- Email address -->
	<Form.Field {form} name="email_address">
		<Form.Control let:attrs>
			<Form.Label
				description={userCreate.schema.shape.email_address.description}
				optional={userCreate.schema.shape.email_address.isOptional()}>Email</Form.Label
			>
			<Input
				{...attrs}
				type="email"
				placeholder="email@example.com"
				bind:value={$formData.email_address}
			/>
		</Form.Control>
		<Form.FieldErrors serverErrors={serverErrors.errors['email_address']} />
	</Form.Field>

	<!-- Password1 -->
	<Form.Field {form} name="password1">
		<Form.Control let:attrs>
			<Form.Label
				description={userCreate.schema.shape.password1.description}
				optional={userCreate.schema.shape.password1.isOptional()}>Password</Form.Label
			>
			<Input {...attrs} type="password" bind:value={$formData.password1} />
		</Form.Control>
		<Form.FieldErrors serverErrors={serverErrors.errors['password1']} />
	</Form.Field>

	<!-- Password2 -->
	<Form.Field {form} name="password2">
		<Form.Control let:attrs>
			<Form.Label
				description={userCreate.schema.shape.password2.description}
				optional={userCreate.schema.shape.password2.isOptional()}
				>Confirm Password</Form.Label
			>
			<Input {...attrs} type="password" bind:value={$formData.password2} />
		</Form.Control>
		<Form.FieldErrors serverErrors={serverErrors.errors['password2']} />
	</Form.Field>

	<!-- Submit button -->
	<Form.Button
		disabled={false}
		loading={$mutation.isLoading}
		variant="default"
		class="mt-4 w-full">Submit</Form.Button
	>
</form>
