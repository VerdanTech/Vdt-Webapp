<script lang="ts">
	import Icon from '@iconify/svelte';
	import { useQuery } from '@triplit/svelte';

	import type { Garden } from '@vdg-webapp/models';
	import { Button, Popover, Separator, iconIds } from '@vdg-webapp/ui';

	import { goto } from '$app/navigation';
	import {
		acceptancePendingMembershipsQuery,
		adminGardensQuery,
		editorGardensQuery,
		favoriteMembershipsQuery,
		viewerGardensQuery
	} from '$data/gardens/queries';
	import triplit from '$data/triplit';
	import auth from '$state/auth.svelte';

	import GardenInviteScrollable from './GardenInviteScrollable.svelte';
	import GardenThumbnailScrollable from './GardenThumbnailScrollable.svelte';

	/**
	 * If a non-authenticated user accesses this page,
	 * redirect to public discovery page.
	 */
	if (!auth.isAuthenticated) {
		goto('gardens/discover');
	}

	/** Queries */
	let favoriteMemberships = useQuery(triplit, favoriteMembershipsQuery);
	let adminGardens = useQuery(triplit, adminGardensQuery);
	let editorGardens = useQuery(triplit, editorGardensQuery);
	let viewerGardens = useQuery(triplit, viewerGardensQuery);
	let pendingAcceptanceMemberships = useQuery(
		triplit,
		acceptancePendingMembershipsQuery
	);
</script>

<svelte:head>
	<title>Gardens - Verdagraph</title>
</svelte:head>

<!-- Top bar -->
<div
	class="border-neutral-5 bg-neutral-1 sticky top-0 z-50 flex h-10 w-full flex-row items-center justify-between overflow-hidden border-b"
>
	<span class="ml-8">Gardens</span>
	<ul class="flex h-full flex-row items-center">
		<!-- Discovery page link. -->
		<li class="h-full">
			<Button.Root variant="ghost" href="gardens/discover" class="rounded-none">
				<Icon icon={iconIds.gardensDiscoverIcon} width="1.5rem" class="mx-2" />
				<span class="mx-2 hidden sm:block">Discovery</span>
			</Button.Root>
		</li>
		<li class="h-full">
			<Popover.Root>
				<Popover.Trigger>
					<Button.Root variant="ghost" class="rounded-none">
						<Icon icon={iconIds.gardensInviteIcon} width="1.5rem" class="mx-2" />
						<span class="mx-2 hidden sm:block">Invites</span>
						<div class="border-neutral-9 h-6 w-6 rounded-2xl border">
							{#if pendingAcceptanceMemberships.fetching}
								?
							{:else if pendingAcceptanceMemberships.error}
								?
							{:else if pendingAcceptanceMemberships.results}
								{pendingAcceptanceMemberships.results.length}
							{/if}
						</div>
					</Button.Root>
				</Popover.Trigger>
				<Popover.Content>
					{#if pendingAcceptanceMemberships.fetching}
						<Icon
							icon={iconIds.defaultSpinnerIcon}
							width="1.5rem"
							class="animate-spin"
						/>
					{:else if pendingAcceptanceMemberships.results}
						<GardenInviteScrollable invites={pendingAcceptanceMemberships.results} />
					{/if}
				</Popover.Content>
			</Popover.Root>
		</li>
		<li class="h-full">
			<Button.Root variant="default" href="gardens/create" class="rounded-none">
				<Icon icon={iconIds.gardensCreateIcon} width="1.5rem" class="mx-2" />
				<span class="mx-2 hidden sm:block">Create</span>
			</Button.Root>
		</li>
	</ul>
</div>

{#snippet gardenCategory(label: string, gardens: Garden[])}
	{#if gardens.length > 0}
		<div>
			<!-- Label -->
			<span class="text-xl">
				{label}
			</span>
			<GardenThumbnailScrollable {gardens} />
			<Separator.Root class="bg-neutral-7 mt-12 mb-4 w-full" />
		</div>
	{/if}
{/snippet}

<!-- Content -->
<div class="bg-neutral-1 h-full w-full p-8">
	<!-- Favorite gardens. -->
	{#if favoriteMemberships.fetching}
		<!-- TODO: Skeleton loading. -->
		Loading...
	{:else if favoriteMemberships.error}
		Error!
	{:else if favoriteMemberships.results}
		{@render gardenCategory(
			'Favorites',
			favoriteMemberships.results
				.map((membership) => membership.garden)
				.filter((garden) => garden != null)
		)}
	{/if}

	<!-- Admin gardens. -->
	{#if adminGardens.fetching}
		<!-- TODO: Skeleton loading. -->
		Loading...
	{:else if adminGardens.error}
		Error!
	{:else if adminGardens.results}
		{@render gardenCategory('Admins', adminGardens.results)}
	{/if}

	<!-- Editor gardens. -->
	{#if editorGardens.fetching}
		<!-- TODO: Skeleton loading. -->
		Loading...
	{:else if editorGardens.error}
		Error!
	{:else if editorGardens.results}
		{@render gardenCategory('Editors', editorGardens.results)}
	{/if}

	<!-- Viewer gardens. -->
	{#if viewerGardens.fetching}
		<!-- TODO: Skeleton loading. -->
		Loading...
	{:else if viewerGardens.error}
		Error!
	{:else if viewerGardens.results}
		{@render gardenCategory('Viewers', viewerGardens.results)}
	{/if}
</div>
