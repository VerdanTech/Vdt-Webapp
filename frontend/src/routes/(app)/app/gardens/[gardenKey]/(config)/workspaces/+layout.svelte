<script lang="ts">
	import { page } from '$app/stores';
	import Icon from '@iconify/svelte';
	import iconIds from '$lib/assets/icons';
	import * as Menubar from '$components/ui/menubar';
	import type { WorkspacePartialSchema } from '$codegen/types';
	import activeWorkspace from './activeWorkspace.svelte';

	let { children } = $props();

	/** Maximum amount of workspaces displayed in the dropdown. */
	const workspacesDropdownMaxItems = 10;

	let workspaces: WorkspacePartialSchema[] = [
		{
			garden_ref: { id: 'f4b3b1b0-0b3b-4b3b-8b3b-0b3b1b0b3b1b' },
			id: 'f4b3b1b0-0b3b-4b3b-8b3b-0b3b1b0b3b1b',
			name: 'Workspace 1',
			slug: 'workspace-1'
		}
	];
</script>

<!-- Workspaces toolbar -->
<Menubar.Root
	class="justify-center border-0 border-b border-neutral-8 md:justify-start"
>
	<Menubar.Menu>
		<Menubar.Trigger>Workspaces</Menubar.Trigger>
		<Menubar.Content>
			<Menubar.Group>
				<Menubar.Label>Workspaces</Menubar.Label>
				{#each workspaces as workspace, index}
					{#if index <= workspacesDropdownMaxItems}
						<Menubar.Item
							href="/app/gardens/{$page.params.gardenKey}/workspaces/{workspace.slug}"
							class="text-light">{workspace.name}</Menubar.Item
						>
					{/if}
				{/each}
				<Menubar.Item
					href="/app/gardens/{$page.params.gardenKey}/workspaces"
					class="flex items-center justify-between"
				>
					<span> See All </span>
					<Icon icon={iconIds.listIcon} width="1.25rem" class="text-neutral-10" />
				</Menubar.Item>
			</Menubar.Group>
			<Menubar.Separator />
			<Menubar.Item
				href="/app/gardens/{$page.params.gardenKey}/workspaces/create"
				class="flex items-center justify-between"
			>
				<span> Create Workspace </span>
				<Icon icon={iconIds.addIcon} width="1.25rem" class="text-neutral-10" />
			</Menubar.Item>
		</Menubar.Content>
	</Menubar.Menu>

	{#if activeWorkspace.value.activeWorkspaceId}
		<Menubar.Menu>
			<Menubar.Trigger>Edit</Menubar.Trigger>
			<Menubar.Content>
				{#if activeWorkspace.value.editing}
					<Menubar.Item
						class="flex items-center justify-start"
						on:click={() => {
							activeWorkspace.value.editing = false;
						}}
					>
						<Icon
							icon={iconIds.endEditingIcon}
							width="1.25rem"
							class="mr-2 text-neutral-11"
						/>
						<span> End Editing </span>
					</Menubar.Item>
				{:else}
					<Menubar.Item
						class="flex items-center justify-start"
						on:click={() => {
							activeWorkspace.value.editing = true;
						}}
					>
						<Icon
							icon={iconIds.startEditingIcon}
							width="1.25rem"
							class="mr-2 text-neutral-11"
						/>
						<span> Start Editing </span>
					</Menubar.Item>
				{/if}
			</Menubar.Content>
		</Menubar.Menu>
		<Menubar.Menu>
			<Menubar.Trigger>Add</Menubar.Trigger>
			<Menubar.Content>
				<Menubar.Item class="flex items-center justify-between">
					<Icon
						icon={iconIds.plantingAreaIcon}
						width="1.25rem"
						class="text-neutral-11"
					/>
					<span> Add Planting Area </span>
				</Menubar.Item>
			</Menubar.Content>
		</Menubar.Menu>
	{/if}
</Menubar.Root>

{@render children()}
