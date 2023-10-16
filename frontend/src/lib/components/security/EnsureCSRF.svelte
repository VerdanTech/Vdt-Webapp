<script lang="ts">
	import { onMount } from 'svelte';
	import { authCsrfRetrieve } from '$lib/api/codegen/auth/auth';
	import { csrftoken } from '$lib/stores';
	import { toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';

	//Request a valid CSRF token and store it in the svelte store
	onMount(() => {
		authCsrfRetrieve()
			.then((response) => {
				$csrftoken = response.data.csrftoken
				console.log(response.data.csrftoken)
			})
			.catch((error) => {
				console.log(error)
				if (error.response.status != 500) {
					const toast: ToastSettings = {
						message: 'Error: Server CSRF failed (HTTP ' + error.response.status + ')',
						background: 'bg-error-500',
						autohide: true,
						timeout: 3000
					};
					toastStore.trigger(toast);
				}
			});
	});
</script>
