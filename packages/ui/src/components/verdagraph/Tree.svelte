<script lang="ts">
	import type { CultivarPlantingWindow } from '@vdg-webapp/models';

	import { ScrollArea, Tabs } from '$core';
	import { getAppContext } from '$state';

	import ActionTree from './ActionTree.svelte';
	import PlantTree from './PlantTree.svelte';
	import PlantingWindowTree from './PlantingWindowTree.svelte';
	import { getVerdagraphContext } from './verdagraphContext.svelte';

	/** Contexts. */
	const ctx = getAppContext();
	const verdagraphContext = getVerdagraphContext();

	/** Data injection. */
	const plants = $derived(ctx.plants.plants);
	const workspaces = $derived(
		ctx.workspaces.workspaces.map((w) => ({ id: w.id, name: w.name }))
	);

	/** Planting windows - currently uses placeholder data. */
	const plantingWindows: CultivarPlantingWindow[] = $derived([]);
</script>

<Tabs.Root value="plants" class="bg-neutral-1 flex h-full flex-col">
	<Tabs.List class="h-8 shadow-none">
		<Tabs.Trigger
			value="plants"
			class="border-neutral-5 text-neutral-11 flex w-full items-center justify-between border-b p-0 px-4 py-1"
			>Plants
		</Tabs.Trigger>
		<Tabs.Trigger
			value="plantingWindows"
			class="border-neutral-5 text-neutral-11 flex w-full items-center justify-between border-b p-0 px-4 py-1"
			>Planting Windows
		</Tabs.Trigger>
		<Tabs.Trigger
			value="actions"
			class="border-neutral-5 text-neutral-11 flex w-full items-center justify-between border-b p-0 px-4 py-1"
			>Actions
		</Tabs.Trigger>
	</Tabs.List>
	<Tabs.Content value="plants">
		<ScrollArea.Root class="w-full px-2">
			<PlantTree {plants} {workspaces} />
		</ScrollArea.Root>
	</Tabs.Content>
	<Tabs.Content value="plantingWindows">
		<ScrollArea.Root class="w-full px-2">
			<PlantingWindowTree {plantingWindows} />
		</ScrollArea.Root>
	</Tabs.Content>
	<Tabs.Content value="actions">
		<ScrollArea.Root class="w-full px-2">
			<ActionTree />
		</ScrollArea.Root>
	</Tabs.Content>
</Tabs.Root>
