<script lang="ts">
	import 'tailwindcss/tailwind.css'
	import { QueryClientProvider } from '@sveltestack/svelte-query'
	import { QueryClient } from '@sveltestack/svelte-query'
	import '../app.pcss'
	import { onMount } from 'svelte'
	import { enableMocking } from '$lib/mocks'

	/* Provides access to Svelte Query's async state management. */
	const queryClient = new QueryClient()

	let { children } = $props()

	onMount(() => {
		enableMocking().then(() => {})
	})
</script>

<!-- QueryClient from Svelte Query provides an async state manager. -->
<QueryClientProvider client={queryClient}>
	<div class="bg-neutral-1 text-neutral-12">
		{@render children()}
	</div>
</QueryClientProvider>
