<script lang="ts">
	import { goto } from '$app/navigation';
	import EnsureCsrf from '$lib/components/security/EnsureCSRF.svelte';
	import { csrftoken } from '$lib/stores/csrftoken';
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

		authLoginCreate(login, { withCredentials: true, headers: { 'X-CSRFToken': $csrftoken } })
			.then((response) => {
				console.log(response);
			})
			.catch((error) => {
				console.log(error);

				if (error.response.status == 500) {
					//Server connection fail toast
				}

				errors = Object.assign({}, error.response.data);
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
				<HintGroup for="email">
					<Hint on="required"><FormError text={'Email is required'} /></Hint>
					<Hint on="email"><FormError text={'Invalid email'} /></Hint>
				</HintGroup>
			</label>
			{#each errors.email ?? [] as error}
				<FormError text={error} />
			{/each}
		</li>
		<li class="p-4">
			<label class="label">
				<span>Password</span>
				<input name="password" type="password" class="input" use:validators={[required]} />
				<Hint on="required"><FormError text={'Password is required'} /></Hint>
			</label>
			{#each errors.password ?? [] as error}
				<FormError text={error} />
			{/each}
		</li>
		<li class="p-4">
			{#each errors.non_field_errors ?? [] as error}
				<FormError text={error} />
			{/each}
		</li>
		<li class="p-4 mt-4">
			<button disabled={!$form.valid} class="btn variant-filled-primary w-full">Login</button>
		</li>
	</ul>
</form>
