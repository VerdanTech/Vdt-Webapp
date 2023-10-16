<script lang="ts">
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import EnsureCsrf from '$lib/components/security/EnsureCSRF.svelte';
	import { accountsRegistrationVerifyEmailCreate } from '$lib/api/codegen/accounts/accounts';
	import type { VerifyEmailRequest } from '$lib/api/codegen/verdanTechAPI.schemas';

	onMount(() => {
		const verification_key = $page.params.key as string;

		const verify_email: VerifyEmailRequest = {
			key: verification_key as string
		};

		accountsRegistrationVerifyEmailCreate(verify_email).then(() => {
			goto('/login');
		});
	});
</script>

<EnsureCsrf />
