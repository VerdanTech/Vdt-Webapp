<script lang="ts">
	import Icon from '@iconify/svelte';
	import { Button } from 'bits-ui';

	import type { PlantingArea, Workspace } from '@vdg-webapp/models';
	import { Menubar, iconIds } from '@vdg-webapp/ui';

	import { goto } from '$app/navigation';
	import { page } from '$app/state';
	import { getAppContext } from '$state';

	import { getWorkspaceEditorContext } from './workspaceEditorContext.svelte';

	type Props = {
		workspaces: Workspace[];
		plantingAreas: PlantingArea[];
		/** If true, the menu to navigate between workspaces is included. */
		includeWorkspacesMenu: boolean;
	};
	let {
		workspaces = [],
		plantingAreas = [],
		includeWorkspacesMenu = true
	}: Props = $props();

	/** Maximum amount of workspaces displayed in the dropdown. */
	const workspacesDropdownMaxItems = 10;

	/** Contexts. */
	const ctx = getAppContext();
	const workspaceEditor = getWorkspaceEditorContext();

	const selectedPlantingAreas = $derived(
		plantingAreas.filter((plantingArea) =>
			workspaceEditor.selections.has('plantingArea', plantingArea.id)
		)
	);
</script>

<!-- Workspaces toolbar -->
<Menubar.Root
	class="border-neutral-8 justify-center border-0 border-b md:justify-start"
>
	<!-- Workspaces Menu.-->
	{#if includeWorkspacesMenu}
		<Menubar.Menu>
			<Menubar.Trigger>Workspaces</Menubar.Trigger>
			<Menubar.Content>
				<Menubar.Group>
					{#if workspaces.length > 0}
						{#each Array.from({ length: Math.min(workspaces.length, workspacesDropdownMaxItems) }, (_, i) => i) as index}
							{@const workspace = workspaces[index]}
							<Menubar.Item>
								<Button.Root
									onclick={() => {
										goto(
											`/gardens/${page.params.gardenId}/workspaces/${workspace.slug}`
										);
									}}
									class="text-light h-full w-full italic"
								>
									{workspace.name}
								</Button.Root>
							</Menubar.Item>
						{/each}
					{/if}
					<Menubar.Item>
						<Button.Root
							href="/gardens/{page.params.gardenId}/workspaces"
							class="flex h-full w-full justify-between"
						>
							<span> See All </span>
							<Icon icon={iconIds.listIcon} width="1.25rem" class="text-neutral-10" />
						</Button.Root>
					</Menubar.Item>
				</Menubar.Group>
				{#if ctx.garden.authorize('WorkspaceCreate')}
					<Menubar.Separator />
					<Menubar.Item>
						<Button.Root
							href="//gardens/{page.params.gardenId}/workspaces/create"
							class="flex h-full w-full items-center justify-between"
						>
							<span> Create Workspace </span>
							<Icon icon={iconIds.addIcon} width="1.25rem" class="text-neutral-10" />
						</Button.Root>
					</Menubar.Item>
				{/if}
			</Menubar.Content>
		</Menubar.Menu>
	{/if}

	<!-- Workspace specific content. -->
	{#if workspaceEditor.id}
		<!-- Select menu. -->
		<Menubar.Menu>
			<Menubar.Trigger>Select</Menubar.Trigger>
			<Menubar.Content>
				<Menubar.Group>
					<Menubar.GroupHeading>Tools</Menubar.GroupHeading>
					<Menubar.Item>
						<Button.Root class="flex h-full w-full items-center justify-between">
							<span> Pointer </span>
							<Icon
								icon={iconIds.pointerSelectIcon}
								width="1.25rem"
								class="text-neutral-10"
							/>
						</Button.Root>
					</Menubar.Item>
					<Menubar.Item>
						<Button.Root class="flex h-full w-full items-center justify-between">
							<span> Group </span>
							<Icon
								icon={iconIds.groupSelectIcon}
								width="1.25rem"
								class="text-neutral-10"
							/>
						</Button.Root>
					</Menubar.Item>
				</Menubar.Group>
				<Menubar.Group>
					<Menubar.GroupHeading>Planting Areas</Menubar.GroupHeading>
					{#if selectedPlantingAreas.length > 0}
						{#each selectedPlantingAreas as plantingArea}
							<Menubar.Item class="flex justify-between px-2">
								<span class="text-sm">
									{plantingArea.name}
								</span>
								<Button.Root
									onclick={() => {
										workspaceEditor.selections.deselect(
											'plantingArea',
											plantingArea.id
										);
									}}
								>
									<Icon icon={iconIds.defaultClose} width="1.25rem" />
								</Button.Root>
							</Menubar.Item>
						{/each}
					{:else}
						<Menubar.Item>
							<span class="italic">None</span>
						</Menubar.Item>
					{/if}
				</Menubar.Group>
			</Menubar.Content>
		</Menubar.Menu>

		<!-- Edit Menu -->
		{#if ctx.garden.authorize('WorkspaceEdit')}
			<Menubar.Menu>
				<Menubar.Trigger>Edit</Menubar.Trigger>
				<Menubar.Content>
					{#if workspaceEditor.editing}
						<Menubar.Item>
							<Button.Root
								class="flex h-full w-full items-center justify-start"
								onclick={() => {
									workspaceEditor.editing = false;
								}}
							>
								<Icon
									icon={iconIds.endEditingIcon}
									width="1.25rem"
									class="text-neutral-11 mr-2"
								/>
								<span> End Editing </span>
							</Button.Root>
						</Menubar.Item>
						<Menubar.Item>
							<Button.Root
								class="flex h-full w-full items-center justify-start"
								onclick={() => {
									workspaceEditor.toolbox.activate('translate');
								}}
							>
								<Icon
									icon={iconIds.verdagraphTranslateIcon}
									width="1.25rem"
									class="text-neutral-11 mr-2"
								/>
								<span> Translate </span>
							</Button.Root>
						</Menubar.Item>
						<Menubar.Item class="flex items-center justify-start">
							<Icon
								icon={iconIds.deleteIcon}
								width="1.25rem"
								class="text-neutral-11 mr-2"
							/>
							<span> Delete </span>
						</Menubar.Item>
					{:else}
						<Menubar.Item>
							<Button.Root
								class="flex h-full w-full items-center justify-start"
								onclick={() => {
									workspaceEditor.editing = true;
								}}
							>
								<Icon
									icon={iconIds.startEditingIcon}
									width="1.25rem"
									class="text-neutral-11 mr-2"
								/>
								<span> Start Editing </span>
							</Button.Root>
						</Menubar.Item>
					{/if}
				</Menubar.Content>
			</Menubar.Menu>
		{/if}

		<!-- Add Menu -->
		{#if workspaceEditor.editing}
			<Menubar.Menu>
				<Menubar.Trigger>Add</Menubar.Trigger>
				<Menubar.Content>
					<Menubar.Item>
						<Button.Root
							class="flex h-full w-full items-center justify-between"
							onclick={() => {
								workspaceEditor.toolbox.activate('plantingAreaCreate');
							}}
						>
							<Icon
								icon={iconIds.plantingAreaIcon}
								width="1.25rem"
								class="text-neutral-11"
							/>
							<span> Add Planting Area </span>
						</Button.Root>
					</Menubar.Item>
				</Menubar.Content>
			</Menubar.Menu>
		{/if}

		<!-- View Menu -->
		<Menubar.Menu>
			<Menubar.Trigger>View</Menubar.Trigger>
			<Menubar.Content>
				<!-- Content pane toggles. -->
				<Menubar.Group>
					<Menubar.CheckboxItem
						checked={workspaceEditor.paneSettings.isEnabled('tree')}
						onCheckedChange={(newVal) => {
							if (newVal) {
								workspaceEditor.paneSettings.enable('tree');
							} else {
								workspaceEditor.paneSettings.disable('tree');
							}
						}}
						disabled={!workspaceEditor.paneSettings.isEnabled('layout')}
					>
						<div class="flex w-full items-center justify-between">
							<span> Tree </span>
							<Icon icon={iconIds.verdagraphTreeIcon} width="1rem" />
						</div>
					</Menubar.CheckboxItem>
					<Menubar.CheckboxItem
						checked={workspaceEditor.paneSettings.isEnabled('layout')}
						onCheckedChange={(newVal) => {
							if (newVal) {
								workspaceEditor.paneSettings.enable('layout');
							} else {
								workspaceEditor.paneSettings.disable('layout');
							}
						}}
						disabled={!workspaceEditor.paneSettings.isEnabled('tree')}
					>
						<div class="flex w-full items-center justify-between">
							<span> Layout </span>
							<Icon icon={iconIds.verdagraphLayoutIcon} width="1rem" />
						</div>
					</Menubar.CheckboxItem>
					<!-- Content pane direction. -->
					{#if workspaceEditor.paneSettings.isEnabled('layout') && workspaceEditor.paneSettings.isEnabled('tree')}
						<Menubar.Sub>
							<Menubar.SubTrigger>Direction</Menubar.SubTrigger>
							<Menubar.SubContent>
								<Menubar.RadioGroup bind:value={workspaceEditor.paneSettings.direction}>
									<Menubar.RadioItem value="horizontal">Horizontal</Menubar.RadioItem>
									<Menubar.RadioItem value="vertical">Vertical</Menubar.RadioItem>
								</Menubar.RadioGroup>
							</Menubar.SubContent>
						</Menubar.Sub>
					{/if}
				</Menubar.Group>

				<Menubar.Separator />

				<Menubar.Item
					onclick={() => {
						workspaceEditor.toolbox.activate('layoutConfig');
					}}
				>
					Layout Config
				</Menubar.Item>
			</Menubar.Content>
		</Menubar.Menu>
	{/if}
</Menubar.Root>
