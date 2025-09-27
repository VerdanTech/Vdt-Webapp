<script lang="ts">
	import Icon from '@iconify/svelte';

	import { iconIds } from '$assets';
	import { Menubar } from '$core';

	import { getVerdagraphContext } from './verdagraphContext.svelte';

	const verdagraphContext = getVerdagraphContext();
</script>

{#snippet menuButton(label: string, iconId: string, onclick: () => void)}
	<Menubar.Item {onclick}>
		<div class="flex w-full items-center justify-between">
			<span> {label} </span>
			<Icon icon={iconId} width="1rem" />
		</div>
	</Menubar.Item>
{/snippet}
<Menubar.Root
	class="border-neutral-8 justify-center border-0 border-b md:justify-start"
>
	<!-- Select Menu -->
	<Menubar.Menu>
		<Menubar.Trigger>Select</Menubar.Trigger>
	</Menubar.Menu>

	<!-- Edit Menu -->
	<Menubar.Menu>
		<Menubar.Trigger>Edit</Menubar.Trigger>
		<Menubar.Content>
			{@render menuButton('Add', iconIds.verdagraphAddIcon, () =>
				verdagraphContext.toolbox.activate('plantsCreate')
			)}
			{@render menuButton('Translate', iconIds.verdagraphTranslateIcon, () =>
				verdagraphContext.toolbox.activate('translate')
			)}
			{@render menuButton('Delete', iconIds.verdagraphDeleteIcon, () =>
				verdagraphContext.toolbox.activate('delete')
			)}
		</Menubar.Content>
	</Menubar.Menu>

	<!-- Observe Menu -->
	<Menubar.Menu>
		<Menubar.Trigger>Observe</Menubar.Trigger>
		<Menubar.Content>
			{@render menuButton('Seed', iconIds.verdagraphRecordSeedIcon, () =>
				verdagraphContext.toolbox.activate('observe')
			)}
			{@render menuButton('Germination', iconIds.verdagraphRecorcGerminationicon, () =>
				verdagraphContext.toolbox.activate('observe')
			)}
			{@render menuButton('Harvest', iconIds.verdagraphRecordHarvestIcon, () =>
				verdagraphContext.toolbox.activate('observe')
			)}
			{@render menuButton('Expire', iconIds.verdagraphRecordExpireIcon, () =>
				verdagraphContext.toolbox.activate('observe')
			)}
			{@render menuButton('Transplant', iconIds.verdagraphRecordTransplantIcon, () =>
				verdagraphContext.toolbox.activate('observe')
			)}
			{@render menuButton('Note', iconIds.verdagraphRecordNoteIcon, () =>
				verdagraphContext.toolbox.activate('observe')
			)}
		</Menubar.Content>
	</Menubar.Menu>

	<!-- Tools Menu -->
	<Menubar.Menu>
		<Menubar.Trigger>Tools</Menubar.Trigger>
		<Menubar.Content>
			{@render menuButton('Groups', iconIds.verdagraphGroupIcon, () =>
				verdagraphContext.toolbox.activate('groups')
			)}
			{@render menuButton('Patterns', iconIds.verdagraphPatternsIcon, () =>
				verdagraphContext.toolbox.activate('patterns')
			)}
			{@render menuButton('Generators', iconIds.verdagraphGeneratorsIcon, () =>
				verdagraphContext.toolbox.activate('generators')
			)}
		</Menubar.Content>
	</Menubar.Menu>

	<!-- View Menu -->
	<Menubar.Menu>
		<Menubar.Trigger>View</Menubar.Trigger>
		<Menubar.Content>
			<!-- Content pane toggles. -->
			<Menubar.Group>
				<Menubar.CheckboxItem
					checked={verdagraphContext.paneSettings.isEnabled('layout')}
					onCheckedChange={(newVal) => {
						if (newVal) {
							verdagraphContext.paneSettings.enable('layout');
						} else {
							verdagraphContext.paneSettings.disable('layout');
						}
					}}
					disabled={!verdagraphContext.paneSettings.isEnabled('tree') &&
						!verdagraphContext.paneSettings.isEnabled('calendar')}
				>
					<div class="flex w-full items-center justify-between">
						<span> Layout </span>
						<Icon icon={iconIds.verdagraphLayoutIcon} width="1rem" />
					</div>
				</Menubar.CheckboxItem>
				<Menubar.CheckboxItem
					checked={verdagraphContext.paneSettings.isEnabled('calendar')}
					onCheckedChange={(newVal) => {
						if (newVal) {
							verdagraphContext.paneSettings.enable('calendar');
						} else {
							verdagraphContext.paneSettings.disable('calendar');
						}
					}}
					disabled={!verdagraphContext.paneSettings.isEnabled('tree') &&
						!verdagraphContext.paneSettings.isEnabled('layout')}
				>
					<div class="flex w-full items-center justify-between">
						<span> Calendar </span>
						<Icon icon={iconIds.verdagraphCalendarIcon} width="1rem" />
					</div>
				</Menubar.CheckboxItem>
				<Menubar.CheckboxItem
					checked={verdagraphContext.paneSettings.isEnabled('tree')}
					onCheckedChange={(newVal) => {
						if (newVal) {
							verdagraphContext.paneSettings.enable('tree');
						} else {
							verdagraphContext.paneSettings.disable('tree');
						}
					}}
					disabled={!verdagraphContext.paneSettings.isEnabled('layout') &&
						!verdagraphContext.paneSettings.isEnabled('calendar')}
				>
					<div class="flex w-full items-center justify-between">
						<span> Tree </span>
						<Icon icon={iconIds.verdagraphTreeIcon} width="1rem" />
					</div>
				</Menubar.CheckboxItem>
				<!-- Content pane direction. -->
				<Menubar.Sub>
					<Menubar.SubTrigger>Direction</Menubar.SubTrigger>
					<Menubar.SubContent>
						<Menubar.RadioGroup bind:value={verdagraphContext.paneSettings.direction}>
							<Menubar.RadioItem value="horizontal">Horizontal</Menubar.RadioItem>
							<Menubar.RadioItem value="vertical">Vertical</Menubar.RadioItem>
						</Menubar.RadioGroup>
					</Menubar.SubContent>
				</Menubar.Sub>
			</Menubar.Group>

			<Menubar.Separator />

			<Menubar.Item
				onclick={() => {
					verdagraphContext.toolbox.activate('layoutConfig');
				}}
			>
				Layout Config
			</Menubar.Item>
		</Menubar.Content>
	</Menubar.Menu>
</Menubar.Root>
