<script lang="ts">
	import { goto } from '$app/navigation';
	import EnsureCsrf from '$lib/components/security/EnsureCSRF.svelte';
	import { is_authenticated } from '$lib/stores';
	import type { LoginRequest } from '$lib/api/codegen/verdanTechAPI.schemas';
	import { authLoginCreate } from '$lib/api/codegen/auth/auth';
	import { useForm, validators, Hint, HintGroup, email, required } from 'svelte-use-form';
	import type { ErrorResponse } from '$lib/api/utils';
	import FormError from '$lib/components/forms/FormError.svelte';

	const form = useForm();
	let errors: ErrorResponse = {};

	async function handleSubmit() {
		const login: LoginRequest = {
			email: ($form.values.email as string) ?? '',
			password: ($form.values.password as string) ?? ''
		};

		authLoginCreate(login)
			.then(() => {
				//Set application state
				$is_authenticated = true;

				//Redirect to app home page
				goto('app');
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
		<li class="px-4 pt-4 pb-8">
			<label class="label">
				<span>Password</span>
				<input name="password" type="password" class="input" use:validators={[required]} />
			</label>
			<Hint on="required"><FormError text={'Password is required'} /></Hint>
			{#each errors.password ?? [] as error}
				<FormError text={error} />
			{/each}
		</li>
		<li class="px-4 pt-4">
			{#each errors.non_field_errors ?? [] as error}
				<FormError text={error} />
			{/each}
		</li>
		<li class="px-4">
			<button disabled={!$form.valid} class="btn variant-filled-primary w-full">Login</button>
		</li>
		<li class="px-4 pt-2">
			<span><a href="login/reset" class="!no-underline">Forgot password?</a></span>
		</li>
	</ul>
</form>
