<script lang="ts">
	import type { PlantingArea, Workspace } from '@vdg-webapp/models';

	import { ScrollArea, Tabs } from '$core';

	import PlantingAreaTree from './PlantingAreaTree.svelte';

	type Props = {
		plantingAreas: PlantingArea[];
		workspaces: Pick<Workspace, 'id' | 'name'>[];
	};
	let { plantingAreas, workspaces }: Props = $props();
</script>

<Tabs.Root value="plantingAreas" class="bg-neutral-1 flex h-full flex-col">
	<Tabs.List class="h-8 shadow-none">
		<Tabs.Trigger
			value="plantingAreas"
			class="border-neutral-5 text-neutral-11 flex w-full items-center justify-between border-b p-0 px-4 py-1"
			>Planting Areas
		</Tabs.Trigger>
	</Tabs.List>
	<Tabs.Content value="plantingAreas">
		<ScrollArea.Root class="w-full px-2">
			<PlantingAreaTree {plantingAreas} {workspaces} />
		</ScrollArea.Root>
	</Tabs.Content>
</Tabs.Root>
