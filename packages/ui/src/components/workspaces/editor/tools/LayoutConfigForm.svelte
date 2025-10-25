<script lang="ts">
	import { FormInfoPopover } from '$components';
	import { Select } from '$core';

	// import { UnitAwareInput } from '$components/units/';
	import { getWorkspaceContext } from '../../../../state/context/workspacesContext.svelte';

	const workspaceContext = getWorkspaceContext();
	const layoutCanvas = workspaceContext.layoutCanvasContext;

	const buttonsPositionOptions = [
		{ value: 'tl', label: 'Top Left' },
		{ value: 'tr', label: 'Top Right' },
		{ value: 'bl', label: 'Bottom Left' },
		{ value: 'br', label: 'Bottom Right' }
	];
	const currentButtonsPositionLabel = $derived(
		buttonsPositionOptions.find(
			(option) => option.value === layoutCanvas.transform.config.buttonsPosition
		)?.label ?? 'Select a corner'
	);
</script>

<div class="mx-4 mt-6 flex flex-col gap-4">
	<div class="flex flex-col gap-2">
		<div class="flex items-center justify-between">
			<span class="text-neutral-11">Controls Position</span>
			<FormInfoPopover
				description="Controls the corner of the layout that the control buttons are positioned."
			/>
		</div>
		<Select.Root
			type="single"
			bind:value={layoutCanvas.transform.config.buttonsPosition}
		>
			<Select.Trigger>{currentButtonsPositionLabel}</Select.Trigger>
			<Select.Content>
				{#each buttonsPositionOptions as option}
					<Select.Item value={option.value}>{option.label}</Select.Item>
				{/each}
			</Select.Content>
		</Select.Root>
	</div>

	<!--
		<div class="flex flex-col gap-2">
			<div class="flex items-center justify-between">
				<span class="text-neutral-11">Background Grid Spacing</span>
				<FormInfoPopover
				description="Sets the distance between gridlines on the background grid."
				/>
			</div>
			<UnitAwareInput bind:value quantityType="distance"></UnitAwareInput>
		</div>
	-->
</div>
