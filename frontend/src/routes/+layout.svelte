<script lang="ts">
	import 'tailwindcss/tailwind.css';
	import { onMount } from 'svelte';
	import { Toaster } from '$lib/components/ui/sonner';
	import { QueryClientProvider } from '@sveltestack/svelte-query';
	import { QueryClient } from '@sveltestack/svelte-query';
	import { ModeWatcher } from 'mode-watcher';
	import { enableMocking } from '$lib/mocks';
	import '../app.pcss';

	const mswEnabled = process.env.NODE_ENV === 'development';
	let isReady = $state(!mswEnabled);

	/* Provides access to Svelte Query's async state management. */
	const queryClient = new QueryClient();

	let { children } = $props();

	onMount(() => {
		if (mswEnabled) {
			enableMocking().then(() => {
				isReady = true;
			});
		}
	});
</script>

{#if isReady}
	<ModeWatcher />

	<!-- QueryClient from Svelte Query provides an async state manager. -->
	<QueryClientProvider client={queryClient}>
		<!-- Sonner toaster from Shadcn-svelte -->
		<Toaster richColors />

		<div class="bg-neutral-1 text-neutral-12">
			{@render children()}
		</div>
	</QueryClientProvider>
{/if}
