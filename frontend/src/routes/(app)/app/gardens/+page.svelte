<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import Icon from '@iconify/svelte'
	import iconIds from '$lib/assets/icons'
	import { Button } from '$lib/components/ui/button'
	import { Separator } from "$lib/components/ui/separator";
	import isAuthenticated from '$state/authenticated.svelte'
	import GardenThumbnailScrollable from './GardenThumbnailScrollable.svelte';

	/** 
	 * If a non-authenticated user access this page, 
	 * redirect to public discovery page. 
	 */
	onMount(() => {
		if (!isAuthenticated.value) {
			goto('gardens/discover')
		}
	});
</script>

<svelte:head>
	<title>Gardens - VerdanTech</title>
</svelte:head>

<!-- Top bar -->
<div class="w-full h-10 bg-neutral-1 flex flex-row justify-between items-center border-b border-neutral-5">
	<span class="ml-8">
		Gardens
	</span>
	<ul class="flex flex-row items-center h-full">
		<li class="h-full">
			<Button variant="ghost" href="gardens/discover" class="rounded-none"> 
				<Icon icon={iconIds.gardensDiscoverIcon} width="1.5rem" class="mx-2"/>
				<span class="mx-2">
					Discovery
				</span>
			</Button>
		</li>
		<li class="h-full">
			<Button variant="ghost" href="gardens/discover" class="rounded-none"> 
				<Icon icon={iconIds.gardensInviteIcon} width="1.5rem" class="mx-2"/>
				<span class="mx-2">
					Invites
				</span>
			</Button>
		</li>
		<li class="h-full">
			<Button variant="default" href="gardens/create" class="rounded-none"> 
				<Icon icon={iconIds.gardensCreateIcon} width="1.5rem" class="mx-2"/>
				<span class="mx-2">
					Create
				</span>
			</Button>
		</li>
	</ul>
</div>

{#snippet gardenCategory()}
<div>
	<!-- Label -->
	<span>
		Favorites
	</span>
	<Separator class="w-full bg-neutral-7" />
	<GardenThumbnailScrollable />
</div>
{/snippet}

<!-- Content -->
<div class="bg-neutral-1 w-full h-full">
	{@render gardenCategory()}
	{@render gardenCategory()}
	{@render gardenCategory()}
	{@render gardenCategory()}
</div>