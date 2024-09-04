<script lang="ts">
	import Logo from '$lib/assets/logo.svelte';
	import { Separator } from '$lib/components/ui/separator/index';
	import { Button } from 'bits-ui';
	import PrimaryNavSidebarTab from './PrimaryNavSidebarTab.svelte';
	import PrimaryNavBottomTabDropdown from './PrimaryNavBottomTab.svelte';
	import PrimaryNavBottomDrawer from './PrimaryNavBottomDrawer.svelte';
	import activeGardenKey from '$state/activeGarden.svelte';
	import { gardenMostRelevantPartialsQuery } from '$data/garden/queries';

	import {
		getGardenSpecifcTabs,
		getGardensTab,
		getNonGardenSpecificTabs
	} from './primaryNavTabs';
	import type { PrimaryTabSpec } from './primaryNavTabs';

	/* Settings. */
	const MAX_GARDENS_IN_TAB_SIDEBAR = 10; /* The maximum amount of gardens listed on the Gardens tab. */

	/* Queries */
	const mostRelevantPartialGardens = gardenMostRelevantPartialsQuery(
		{ max_gardens: MAX_GARDENS_IN_TAB_SIDEBAR },
		{
			onSuccess: updateGardensTab
		}
	);

	/* Tab categories. */
	const nonGardenSpecificTabs: PrimaryTabSpec[] =
		getNonGardenSpecificTabs(); /* Points to static pages. */
	let gardensTab: PrimaryTabSpec = getGardensTab(
		[]
	); /* Gives quick access to other gardens. */
	let gardenTabs: PrimaryTabSpec[] =
		[]; /* Allows accessing all features in a Garden. */

	/* Get mobile specific tabs. */
	let traitsTab = nonGardenSpecificTabs.find((t) => t.id === 'traits');
	let profileTab = nonGardenSpecificTabs.find((t) => t.id === 'profile');
	let resourcesTab = nonGardenSpecificTabs.find((t) => t.id === 'resources');

	/* Retrieve the gardens tab if the associated partials query is complete. */
	function updateGardensTab() {
		if ($mostRelevantPartialGardens.data) {
			console.log($mostRelevantPartialGardens.data);
			gardensTab = getGardensTab(
				/* TODO: change store access when svelte-query is updated to Svelte 5. */
				$mostRelevantPartialGardens.data
			);
		}
	}
	updateGardensTab();

	/* Retrieve the garden tabs if there is an active garden. */
	if (activeGardenKey.value !== null) {
		gardenTabs = getGardenSpecifcTabs(activeGardenKey.value);
	}
</script>

<!--
@component
Primary navigation between different feature domains
in the Garden as well as non-garden related app resources.

Shown to authenticated users everywhere in the app, and non-authenticated
users in a Garden context.
-->

<!-- Small screens bottom bar. -->
<nav
	class="fixed bottom-0 flex h-16 w-full flex-row items-center justify-around border border-neutral-6 bg-neutral-3 lg:h-0 first:lg:hidden"
>
	{#if profileTab}
		<PrimaryNavBottomTabDropdown spec={profileTab} />
	{/if}
	{#if resourcesTab}
		<PrimaryNavBottomTabDropdown spec={resourcesTab} />
	{/if}
	{#if traitsTab}
		<PrimaryNavBottomTabDropdown spec={traitsTab} />
	{/if}
	<PrimaryNavBottomTabDropdown spec={gardensTab} />
	{#if activeGardenKey.value !== null}
		<PrimaryNavBottomDrawer specs={gardenTabs} />
	{/if}
</nav>

<!-- Large screens sidebar. -->
<nav
	class="fixed top-0 z-10 hidden h-full w-16 flex-col items-center justify-between border-r border-neutral-6 bg-neutral-3 lg:flex"
>
	<!-- Links displayed at the top. -->
	<ul class="flex w-full flex-col">
		<!-- VerdanTech logo. -->
		<li>
			<Button.Root
				href="/"
				class="inline-flex h-16 w-full items-center justify-center whitespace-nowrap rounded-none bg-neutral-3 transition-colors hover:bg-neutral-4"
			>
				<Logo size="3rem" />
			</Button.Root>
		</li>

		<!-- Gardens tab. -->
		<li class="flex items-center">
			<PrimaryNavSidebarTab spec={gardensTab} />
		</li>

		<Separator class="bg-neutral-6" />

		<!-- Garden specific links. -->
		{#each gardenTabs as tab}
			<li>
				<PrimaryNavSidebarTab spec={tab} />
			</li>
		{/each}
	</ul>

	<!-- Links displayed at the bottom. -->
	<ul class="flex w-full flex-col">
		{#each nonGardenSpecificTabs as tab}
			<li>
				<PrimaryNavSidebarTab spec={tab} flipped={true} />
			</li>
		{/each}
	</ul>
</nav>
