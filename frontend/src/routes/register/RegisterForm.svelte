<script lang="ts">
	import { goto } from '$app/navigation';
	import EnsureCsrf from '$lib/components/security/EnsureCSRF.svelte';
	import type { RegisterRequest } from '$lib/api/codegen/verdanTechAPI.schemas';
	import { accountsRegistrationCreate } from '$lib/api/codegen/accounts/accounts';
	import { useForm, validators, Hint, HintGroup, email, required } from 'svelte-use-form';
	import type { ErrorResponse } from '$lib/api/utils';
	import FormError from '$lib/components/forms/FormError.svelte';
	import { toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';

	const form = useForm();
	let errors: ErrorResponse = {};

	async function handleSubmit() {
		const register: RegisterRequest = {
			username: ($form.values.username as string) ?? '',
			email: ($form.values.email as string) ?? '',
			password1: ($form.values.password1 as string) ?? '',
			password2: ($form.values.password2 as string) ?? ''
		};

		accountsRegistrationCreate(register)
			.then(() => {
				//Create email verification toast
				const toast: ToastSettings = {
					message:
						'Verification email sent to ' + register.email + '. Verification required to log in',
					background: 'bg-success-500',
					autohide: true,
					timeout: 15000
				};
				toastStore.trigger(toast);

				//Redirect to login page
				goto('login');
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
		<li class="p-4">
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
		<li class="p-4">
			<label class="label">
				<span>Username</span>
				<input name="username" type="text" class="input" use:validators={[required]} />
			</label>
			<HintGroup for="username">
				<Hint on="required"><FormError text={'Username is required'} /></Hint>
			</HintGroup>
			{#each errors.username ?? [] as error}
				<FormError text={error} />
			{/each}
		</li>
		<li class="p-4">
			<label class="label">
				<span>Password</span>
				<input name="password1" type="password" class="input" use:validators={[required]} />
			</label>
			<Hint on="required"><FormError text={'Password is required'} /></Hint>
			{#each errors.password1 ?? [] as error}
				<FormError text={error} />
			{/each}
		</li>
		<li class="px-4 pt-4 pb-8">
			<label class="label">
				<span>Re-type password</span>
				<input name="password2" type="password" class="input" use:validators={[required]} />
			</label>
			<Hint on="required"><FormError text={'Password check is required'} /></Hint>
			{#each errors.password2 ?? [] as error}
				<FormError text={error} />
			{/each}
		</li>
		<li class="px-4 pt-4">
			{#each errors.non_field_errors ?? [] as error}
				<FormError text={error} />
			{/each}
		</li>
		<li class="px-4 pt-1">
			<label class="label">
				<span>Email verification is required to log in</span>
				<button disabled={!$form.valid} class="btn variant-filled-primary w-full">Register</button>
			</label>
		</li>
		<li class="px-4 pt-2">
			<span><a href="register/resend" class="!no-underline">Resend verification email</a></span>
		</li>
	</ul>
</form>
