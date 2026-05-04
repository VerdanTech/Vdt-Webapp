<script lang="ts">
	import { onMount } from 'svelte';

	import type { Workspace } from '@vdg-webapp/models';
	import { Button, ScrollArea, WorkspaceThumbnail } from '@vdg-webapp/ui';

	import { getWorkspaceContext } from './activeWorkspace.svelte';

	const workspaceContext = getWorkspaceContext();

	onMount(() => {
		/** CLear the active workspace. */
		if (workspaceContext.id) {
			workspaceContext.reset();
		}
	});

	/** TODO: Replace with query. */
	let workspaces: Workspace[] = [
		{
			gardenId: 'f4b3b1b0-0b3b-4b3b-8b3b-0b3b1b0b3b1b',
			id: 'f4b3b1b0-0b3b-4b3b-8b3b-0b3b1b0b3b1b',
			name: 'Workspace 1arstnoienrsienotarson',
			slug: 'workspace-1',
			description:
				"Jokester began sneaking into the castle in the middle of the night and leaving jokes all over the place: under the king's pillow, in his soup, even in the royal toilet. The king was furious, but he couldn't seem to stop Jokester. And then, one day, the people of the kingdom discovered that the jokes left by Jokester were so funny that they couldn't help but laugh. And once they started laughing, they couldn't stop."
		}
	];
</script>

<svelte:head>
	<title>Workspaces - Verdagraph</title>
</svelte:head>

<div
	class="mx-auto mt-0 grid w-full grid-cols-1 gap-0 md:mt-8 md:w-10/12 md:gap-8 lg:mt-16 lg:w-3/4 xl:w-1/2"
>
	{#each workspaces as workspace}
		<div
			class="bg-neutral-1 md:bg-neutral-3 flex h-auto w-auto flex-col items-center justify-around gap-4 rounded-none border-b p-8 shadow-lg md:rounded-md md:border lg:flex-row"
		>
			<Button.Root
				variant="outline"
				href={`workspaces/${workspace.slug}`}
				class="bg-neutral-2 hover:bg-neutral-1 relative mx-4 flex h-72 w-96 flex-col justify-around text-xl"
			>
				<p
					class="absolute inset-1/8 top-2 w-auto max-w-60 overflow-hidden rounded-sm px-2 py-1 text-center text-wrap"
				>
					{workspace.name}
				</p>
				<div class="flex h-full w-full items-center justify-center p-2">
					<WorkspaceThumbnail />
				</div>
			</Button.Root>
			<ScrollArea.Root
				class="bg-neutral-2 h-auto max-h-72 w-96 rounded-md border px-6 py-4 lg:h-72 lg:w-1/2"
			>
				{workspace.description || 'No description provided.'}
			</ScrollArea.Root>
		</div>
	{/each}
</div>
