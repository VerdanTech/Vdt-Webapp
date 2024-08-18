<script lang="ts">
	import { onMount } from 'svelte'
	import { goto } from '$app/navigation'
	import Icon from '@iconify/svelte'
	import iconIds from '$lib/assets/icons'
	import { Button } from '$lib/components/ui/button'
	import { Separator } from '$lib/components/ui/separator'
	import isAuthenticated from '$state/authenticated.svelte'
	import type { GardenPartialSchema } from '$codegen/types'
	import GardenThumbnailScrollable from './GardenThumbnailScrollable.svelte'
	import { gardenAssociatedPartialsQuery } from '$data/garden/queries'

	const associatedPartials = gardenAssociatedPartialsQuery()

	/**
	 * If a non-authenticated user access this page,
	 * redirect to public discovery page.
	 */
	onMount(() => {
		if (!isAuthenticated.value) {
			goto('gardens/discover')
		}
	})

	$associatedPartials.data?.gardens.filter(garden => {return $associatedPartials.data?.favorites.includes(garden.id)})
</script>

<svelte:head>
	<title>Gardens - VerdanTech</title>
</svelte:head>

<!-- Top bar -->
<div
	class="flex h-10 w-full flex-row items-center justify-between border-b border-neutral-5 bg-neutral-1"
>
	<span class="ml-8"> Gardens </span>
	<ul class="flex h-full flex-row items-center">
		<li class="h-full">
			<Button variant="ghost" href="gardens/discover" class="rounded-none">
				<Icon icon={iconIds.gardensDiscoverIcon} width="1.5rem" class="mx-2" />
				<span class="mx-2"> Discovery </span>
			</Button>
		</li>
		<li class="h-full">
			<Button variant="ghost" href="gardens/discover" class="rounded-none">
				<Icon icon={iconIds.gardensInviteIcon} width="1.5rem" class="mx-2" />
				<span class="mx-2"> Invites </span>
			</Button>
		</li>
		<li class="h-full">
			<Button variant="default" href="gardens/create" class="rounded-none">
				<Icon icon={iconIds.gardensCreateIcon} width="1.5rem" class="mx-2" />
				<span class="mx-2"> Create </span>
			</Button>
		</li>
	</ul>
</div>

{#snippet gardenCategory(label: string, gardens: GardenPartialSchema[])}
	<div>
		<!-- Label -->
		<span class="text-xl">
			{label}
		</span>
		<GardenThumbnailScrollable gardenPartials={gardens} />
		<Separator class="mb-4 mt-12 w-full bg-neutral-7" />
	</div>
{/snippet}

{#if $associatedPartials.status === 'loading'}
	loading
{:else if $associatedPartials.status === 'error'}
	error
{:else if $associatedPartials.status === 'success'}
	<!-- Content -->
	<div class="h-full w-full bg-neutral-1 p-8">
		{@render gardenCategory('Favorites', $associatedPartials.data.data.gardens)}
		{#if $associatedPartials.data.admin_memberships?.length > 0}
		{@render gardenCategory('Editors', $associatedPartials.data.gardens)}
		{/if}
		{#if $associatedPartials.data.edit_memberships?.length > 0}
			{@render gardenCategory('Editors', $associatedPartials.data.gardens)}
		{/if}
		{#if $associatedPartials.data.view_memberships?.length > 0}
			{@render gardenCategory('Viewers', $associatedPartials.data.gardens)}
		{/if}
	</div>
{/if}
