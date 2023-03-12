<script lang="ts">
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import EnsureCsrf from '$lib/components/security/EnsureCSRF.svelte';
	import type { PasswordResetConfirmRequest } from '$lib/api/codegen/verdanTechAPI.schemas';
	import { accountsPasswordResetConfirmCreate } from '$lib/api/codegen/accounts/accounts';
	import { useForm, validators, Hint, required } from 'svelte-use-form';
	import type { ErrorResponse } from '$lib/api/utils';
	import FormError from '$lib/components/forms/FormError.svelte';
	import { toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';

	const form = useForm();
	let errors: ErrorResponse = {};

	async function handleSubmit() {
		const password_reset_confirm: PasswordResetConfirmRequest = {
			new_password1: ($form.values.new_password1 as string) ?? '',
			new_password2: ($form.values.new_password2 as string) ?? '',
			uid: $page.params.user_id as string,
			token: $page.params.token as string
		};

		accountsPasswordResetConfirmCreate(password_reset_confirm)
			.then(() => {
				//Create password reset toast
				const toast: ToastSettings = {
					message: 'Password successfully reset',
					background: 'bg-success-500',
					autohide: true,
					timeout: 5000
				};
				toastStore.trigger(toast);

				//Redirect to app home page
				goto('../../');
			})
			.catch((error) => {
				errors = {
					...error.response.data,
					non_field_errors: error.response.data.non_field_errors ?? []
				};

				if (error.response.data.token) {
					errors.non_field_errors?.push('Invalid reset token (URL Parameter)');
				}
				if (error.response.data.uid) {
					errors.non_field_errors?.push('Invalid user ID (URL Parameter)');
				}
			});
	}
</script>

<EnsureCsrf />
<form use:form on:submit|preventDefault={handleSubmit}>
	<ul>
		<li class="p-4">
			<label class="label">
				<span>Password</span>
				<input name="new_password1" type="password" class="input" use:validators={[required]} />
			</label>
			<Hint on="required"><FormError text={'Password is required'} /></Hint>
			{#each errors.new_password1 ?? [] as error}
				<FormError text={error} />
			{/each}
		</li>
		<li class="px-4 pt-4 pb-8">
			<label class="label">
				<span>Re-type password</span>
				<input name="new_password2" type="password" class="input" use:validators={[required]} />
			</label>
			<Hint on="required"><FormError text={'Password check is required'} /></Hint>
			{#each errors.new_password2 ?? [] as error}
				<FormError text={error} />
			{/each}
		</li>
		<li class="px-4 pt-4">
			{#each errors.non_field_errors ?? [] as error}
				<FormError text={error} />
			{/each}
		</li>
		<li class="px-4">
			<button disabled={!$form.valid} class="btn variant-filled-primary w-full"
				>Reset Password</button
			>
		</li>
		<li class="px-4 pt-2">
			<span><a href="login/reset" class="!no-underline">Forgot password?</a></span>
		</li>
	</ul>
</form>
