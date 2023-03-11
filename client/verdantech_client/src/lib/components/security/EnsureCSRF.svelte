<script lang="ts">
	import { onMount } from 'svelte';
	import { authCsrfRetrieve } from '$lib/api/codegen/auth/auth';
	import { csrftoken } from '$lib/stores';

	//Request a valid CSRF token and store it in the svelte store
	onMount(async () => {
		let response = await authCsrfRetrieve({ withCredentials: true });
		$csrftoken = response.data.csrftoken;
	});
</script>
