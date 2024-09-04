<script lang="ts">
	import { getContext } from 'svelte'
	import Icon from '@iconify/svelte'
	import { Separator, Toolbar } from 'bits-ui'
	import * as Menubar from '$components/ui/menubar/index.js'
	import iconIds from '$lib/assets/icons'
	import type { VerdagraphViewSettings } from './state/viewSettings.svelte'
	import forms from './state/forms.svelte'

	let viewSettings: { value: VerdagraphViewSettings } = getContext('viewSettings')
</script>

{#snippet menuButton(label: string, iconId: string, onclick: () => void)}
	<Menubar.Item on:click={onclick}>
		<div class="flex w-full items-center justify-between">
			<span> {label} </span>
			<Icon icon={iconId} width="1rem" />
		</div>
	</Menubar.Item>
{/snippet}
<Menubar.Root class="justify-center md:justify-start border-0 border-b border-neutral-8">
	<!-- Select Menu -->
	<Menubar.Menu>
		<Menubar.Trigger>Select</Menubar.Trigger>
		<Menubar.Content>
			{@render menuButton('Filter', iconIds.verdagraphFilterSelectIcon, () => forms.activateForm('filter'))}
		</Menubar.Content>
	</Menubar.Menu>

	<!-- Edit Menu -->
	<Menubar.Menu>
		<Menubar.Trigger>Edit</Menubar.Trigger>
		<Menubar.Content>
			<Menubar.Group>
				{@render menuButton('Add', iconIds.verdagraphAddIcon, () => forms.activateForm('add'))}
			</Menubar.Group>
			<Menubar.Group>
				{@render menuButton('Group', iconIds.verdagraphGroupIcon, () => {})}
				{@render menuButton('Ungroup', iconIds.verdagraphUngroupIcon, () => {})}
			</Menubar.Group>
			{@render menuButton('Translate', iconIds.verdagraphTranslateIcon, () => forms.activateForm('translate'))}
			{@render menuButton('Delete', iconIds.verdagraphDeleteIcon, () => forms.activateForm('delete'))}
		</Menubar.Content>
	</Menubar.Menu>

	<!-- Observe Menu -->
	<Menubar.Menu>
		<Menubar.Trigger>Observe</Menubar.Trigger>
		<Menubar.Content>
			{@render menuButton('Seed', iconIds.verdagraphRecordSeedIcon, () => forms.activateForm('observe'))}
			{@render menuButton('Germination', iconIds.verdagraphRecorcGerminationicon, () => forms.activateForm('observe'))}
			{@render menuButton('Harvest', iconIds.verdagraphRecordHarvestIcon, () => forms.activateForm('observe'))}
			{@render menuButton('Expire', iconIds.verdagraphRecordExpireIcon, () => forms.activateForm('observe'))}
			{@render menuButton('Transplant', iconIds.verdagraphRecordTransplantIcon, () => forms.activateForm('observe'))}
			{@render menuButton('Note', iconIds.verdagraphRecordNoteIcon, () => forms.activateForm('observe'))}
		</Menubar.Content>
	</Menubar.Menu>

	<!-- Tools Menu -->
	<Menubar.Menu>
		<Menubar.Trigger>Tools</Menubar.Trigger>
		<Menubar.Content>
			{@render menuButton('Plans', iconIds.verdagraphPlansIcon,  () => forms.activateForm('plans'))}
			{@render menuButton('Patterns', iconIds.verdagraphPatternsIcon, () => forms.activateForm('patterns'))}
			{@render menuButton('Generators', iconIds.verdagraphGeneratorsIcon, () => forms.activateForm('generators'))}
		</Menubar.Content>
	</Menubar.Menu>

	<!-- View Menu -->
	<Menubar.Menu>
		<Menubar.Trigger>View</Menubar.Trigger>
		<Menubar.Content>
			<Menubar.Group>
				<Menubar.CheckboxItem bind:checked={viewSettings.value.layoutEnabled}>
					<div class="flex w-full items-center justify-between">
						<span> Layout </span>
						<Icon icon={iconIds.verdagraphLayoutIcon} width="1rem" />
					</div>
				</Menubar.CheckboxItem>
				<Menubar.CheckboxItem bind:checked={viewSettings.value.calendarEnabled}>
					<div class="flex w-full items-center justify-between">
						<span> Calendar </span>
						<Icon icon={iconIds.verdagraphCalendarIcon} width="1rem" />
					</div>
				</Menubar.CheckboxItem>
				<Menubar.CheckboxItem bind:checked={viewSettings.value.treeEnabled}>
					<div class="flex w-full items-center justify-between">
						<span> Tree </span>
						<Icon icon={iconIds.verdagraphTreeIcon} width="1rem" />
					</div>
				</Menubar.CheckboxItem>
			</Menubar.Group>
		</Menubar.Content>
	</Menubar.Menu>
</Menubar.Root>
