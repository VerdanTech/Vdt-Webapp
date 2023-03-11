<script lang="ts">
	import EnsureCsrf from '$lib/components/security/EnsureCSRF.svelte';
	import { csrftoken } from '$lib/stores';
	import type { ResendEmailVerificationRequest } from '$lib/api/codegen/verdanTechAPI.schemas';
	import { accountsRegistrationResendEmailCreate } from '$lib/api/codegen/accounts/accounts';
	import { useForm, validators, Hint, HintGroup, email, required } from 'svelte-use-form';
	import type { ErrorResponse } from '$lib/api/utils';
	import FormError from '$lib/components/forms/FormError.svelte';
	import { toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';

	const form = useForm();
	let errors: ErrorResponse = {};

	async function handleSubmit() {
		const verification_resend: ResendEmailVerificationRequest = {
			email: ($form.values.email as string) ?? ''
		};

		accountsRegistrationResendEmailCreate(verification_resend, {
			withCredentials: true,
			headers: { 'X-CSRFToken': $csrftoken }
		})
			.then((response) => {
				console.log(response);

				//Create email verification toast
				const toast: ToastSettings = {
					message: 'Verification email sent to ' + verification_resend.email,
					background: 'bg-success-500',
					autohide: true,
					timeout: 15000
				};
				toastStore.trigger(toast);
			})
			.catch((error) => {
				console.log(error);

				if (error.response.status == 500) {
					//Server connection fail toast
					const toast: ToastSettings = {
						message: 'Error: server connection failed',
						background: 'bg-error-500',
						autohide: true,
						timeout: 5000
					};
					toastStore.trigger(toast);
				}

				errors = Object.assign({}, error.response.data);
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
