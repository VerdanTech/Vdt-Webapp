<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

	onMount(() => {
		fetch('http://verdantech.io/api/accounts/csrf/', {
			method: 'GET'
		});
	});

	async function handleSubmit(event: SubmitEvent) {
		const formData = new FormData(event.target as HTMLFormElement);

		const data: { [key: string]: any } = {};
		for (const [key, value] of formData.entries()) {
			data[key] = value;
		}

		await fetch('http://verdantech.io/api/accounts/login/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(data)
		}).then((response) => {
			if (response.ok) {
                goto('/app/dashboard')
			} else if (response.status == 403) {

            }
		});
	}
</script>

<form on:submit|preventDefault={handleSubmit}>
	<ul>
		<li class="p-4">
			<label class="label">
				<span>Email</span>
				<input class="input" type="email" required />
			</label>
		</li>
		<li class="p-4">
			<label class="label">
				<span>Password</span>
				<input class="input" type="password" required />
			</label>
		</li>
		<li class="p-4 mt-4">
			<button class="btn variant-filled-primary w-full">Login</button>
		</li>
	</ul>
</form>
