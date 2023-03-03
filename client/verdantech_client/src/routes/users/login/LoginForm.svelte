<script lang="ts">
	import { goto } from '$app/navigation';
	import EnsureCsrf from '$lib/components/security/EnsureCSRF.svelte';
	import type { LoginRequest } from '$lib/api/codegen/verdanTechAPI.schemas';
	import { authLoginCreate } from '$lib/api/codegen/auth/auth';
	import { csrftoken } from '$lib/stores/csrftoken';

	function getCookie(name: string) {
		// Split cookie string and get all individual name=value pairs in an array
		var cookieArr = document.cookie.split(';');

		// Loop through the array elements
		for (var i = 0; i < cookieArr.length; i++) {
			var cookiePair = cookieArr[i].split('=');

			/* Removing whitespace at the beginning of the cookie name
        and compare it with the given string */
			if (name == cookiePair[0].trim()) {
				// Decode the cookie value and return
				return decodeURIComponent(cookiePair[1]);
			}
		}

		// Return null if not found
		return null;
	}

	async function handleSubmit(event: SubmitEvent) {
		const formData = new FormData(event.target as HTMLFormElement);

		const login: LoginRequest = {
			email: formData.get('email') as string,
			password: formData.get('password') as string
		};

		try {
			const response = await authLoginCreate(login);
			console.log(response);
		} catch (error) {}
	}
</script>

<EnsureCsrf />
<form on:submit|preventDefault={handleSubmit}>
	<ul>
		<li class="p-4">
			<label class="label">
				<span>Email</span>
				<input class="input" type="email" name="email" required />
			</label>
		</li>
		<li class="p-4">
			<label class="label">
				<span>Password</span>
				<input class="input" type="password" name="password" required />
			</label>
		</li>
		<li class="p-4 mt-4">
			<button class="btn variant-filled-primary w-full">Login</button>
		</li>
	</ul>
</form>
