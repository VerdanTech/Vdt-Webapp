<script lang="ts">
	import EnsureCsrf from '$lib/components/security/EnsureCSRF.svelte';
	import type { PasswordResetRequest } from '$lib/api/codegen/verdanTechAPI.schemas';
	import { accountsPasswordResetCreate } from '$lib/api/codegen/accounts/accounts';
	import { useForm, validators, Hint, HintGroup, email, required } from 'svelte-use-form';
	import type { ErrorResponse } from '$lib/api/utils';
	import FormError from '$lib/components/forms/FormError.svelte';
	import { toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';

	const form = useForm();
	let errors: ErrorResponse = {};

	async function handleSubmit() {
		const password_reset: PasswordResetRequest = {
			email: ($form.values.email as string) ?? ''
		};

		accountsPasswordResetCreate(password_reset)
			.then(() => {
				//Create password reset toast
				const toast: ToastSettings = {
					message: 'Password reset email sent to ' + password_reset.email,
					background: 'bg-success-500',
					autohide: true,
					timeout: 15000
				};
				toastStore.trigger(toast);
			})
			.catch((error) => {
				errors = {
					...error.response.data,
					non_field_errors: error.response.data.non_field_errors ?? []
				};
			});
	}
</script>

<EnsureCsrf />
<form use:form on:submit|preventDefault={handleSubmit}>
	<ul>
		<li class="px-4 pt-4 pb-8">
			<label class="label">
				<span>Email</span>
				<input name="email" type="email" class="input" use:validators={[required, email]} />
			</label>
			<HintGroup for="email">
				<Hint on="required"><FormError text={'Email is required'} /></Hint>
				<Hint on="email"><FormError text={'Invalid email'} /></Hint>
			</HintGroup>
			{#each errors.email ?? [] as error}
				<FormError text={error} />
			{/each}
		</li>
		<li class="px-4 pt-4">
			{#each errors.non_field_errors ?? [] as error}
				<FormError text={error} />
			{/each}
		</li>
		<li class="px-4">
			<button disabled={!$form.valid} class="btn variant-filled-primary w-full">Send Email</button>
		</li>
	</ul>
</form>
