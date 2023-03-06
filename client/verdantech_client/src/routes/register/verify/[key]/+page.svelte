<script lang="ts">
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import EnsureCsrf from '$lib/components/security/EnsureCSRF.svelte';
	import { csrftoken } from '$lib/stores/csrftoken';
	import { accountsRegistrationVerifyEmailCreate } from '$lib/api/codegen/accounts/accounts';
	import type { VerifyEmailRequest } from '$lib/api/codegen/verdanTechAPI.schemas';

	onMount(() => {
		const verification_key = $page.params.key as string;

		const verify_email: VerifyEmailRequest = {
			key: verification_key as string
		};

		accountsRegistrationVerifyEmailCreate(verify_email, {
			withCredentials: true,
			headers: { 'X-CSRFToken': $csrftoken }
		})
			.then((response) => {
				console.log(response);
				goto('/login');
			})
			.catch((error) => {
				console.log(error);
			});
	});
</script>

<EnsureCsrf />
