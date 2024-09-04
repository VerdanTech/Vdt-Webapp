<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import Icon from '@iconify/svelte';
	import iconIds from '$lib/assets/icons';
	import { Button } from '$lib/components/ui/button';
	import { Separator } from '$lib/components/ui/separator';
	import * as Popover from '$components/ui/popover';
	import { flyAndScale } from '$lib/utils/shadcn';
	import authentication from '$state/authentication.svelte';
	import type { GardenPartialSchema } from '$codegen/types';
	import GardenThumbnailScrollable from './GardenThumbnailScrollable.svelte';
	import GardenInviteScrollable from './GardenInviteScrollable.svelte';
	import {
		gardenAssociatedPartialsQuery,
		gardenPendingInvitesQuery
	} from '$data/garden/queries';

	/** Queries */
	const associatedPartials = gardenAssociatedPartialsQuery();
	const pendingInvites = gardenPendingInvitesQuery();

	/**
	 * If a non-authenticated user access this page,
	 * redirect to public discovery page.
	 */
	onMount(() => {
		if (!authentication.value.isAuthenticated) {
			goto('gardens/discover');
		}
	});
</script>

<svelte:head>
	<title>Gardens - VerdanTech</title>
</svelte:head>

<!-- Top bar -->
<div
	class="sticky top-0 z-50 flex h-10 w-full flex-row items-center justify-between overflow-hidden border-b border-neutral-5 bg-neutral-1"
>
	<span class="ml-8">Gardens</span>
	<ul class="flex h-full flex-row items-center">
		<!-- Discovery page link. -->
		<li class="h-full">
			<Button variant="ghost" href="gardens/discover" class="rounded-none">
				<Icon icon={iconIds.gardensDiscoverIcon} width="1.5rem" class="mx-2" />
				<span class="mx-2 hidden sm:block">Discovery</span>
			</Button>
		</li>
		<li class="h-full">
			<Popover.Root>
				<Popover.Trigger>
					<Button variant="ghost" class="rounded-none">
						<Icon icon={iconIds.gardensInviteIcon} width="1.5rem" class="mx-2" />
						<span class="mx-2 hidden sm:block">Invites</span>
						<div class="h-6 w-6 rounded-2xl border border-neutral-9">
							{#if $pendingInvites.status === 'loading'}
								?
							{:else if $pendingInvites.status === 'success'}
								{$pendingInvites.data.pending_invites.length}
							{/if}
						</div>
					</Button>
				</Popover.Trigger>
				<Popover.Content
					transition={flyAndScale}
					transitionConfig={{
						duration: 150,
						y: 10,
						start: 1
					}}
					class="translate-y-2"
				>
					{#if $pendingInvites.status === 'loading'}
						<Icon
							icon={iconIds.defaultSpinnerIcon}
							width="1.5rem"
							class="animate-spin"
						/>
					{:else if $pendingInvites.status === 'success'}
						<GardenInviteScrollable invites={$pendingInvites.data.pending_invites} />
					{/if}
				</Popover.Content>
			</Popover.Root>
		</li>
		<li class="h-full">
			<Button variant="default" href="gardens/create" class="rounded-none">
				<Icon icon={iconIds.gardensCreateIcon} width="1.5rem" class="mx-2" />
				<span class="mx-2 hidden sm:block">Create</span>
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
	<!-- TODO: Add skeleton loading -->
	<div class="m-auto my-8">Loading...</div>
{:else if $associatedPartials.status === 'success'}
	<!-- Content -->
	<div class="h-full w-full bg-neutral-1 p-8">
		{#if $associatedPartials.data.favorites.length > 0}
			{@render gardenCategory(
				'Favorites',
				$associatedPartials.data.gardens.filter((garden) => {
					return $associatedPartials.data.favorites.includes(garden.id);
				})
			)}
		{/if}
		{#if $associatedPartials.data.admin_memberships.length > 0}
			{@render gardenCategory(
				'Admins',
				$associatedPartials.data.gardens.filter((garden) => {
					return $associatedPartials.data.admin_memberships.includes(garden.id);
				})
			)}
		{/if}
		{#if $associatedPartials.data.edit_memberships.length > 0}
			{@render gardenCategory(
				'Editable',
				$associatedPartials.data.gardens.filter((garden) => {
					return $associatedPartials.data.edit_memberships.includes(garden.id);
				})
			)}
		{/if}
		{#if $associatedPartials.data.view_memberships.length > 0}
			{@render gardenCategory(
				'Viewable',
				$associatedPartials.data.gardens.filter((garden) => {
					return $associatedPartials.data.view_memberships.includes(garden.id);
				})
			)}
		{/if}
	</div>
{/if}
