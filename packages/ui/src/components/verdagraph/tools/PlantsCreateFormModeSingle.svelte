<script lang="ts">
	import Icon from '@iconify/svelte';
	import { toast } from 'svelte-sonner';

	import { AppError, plantFields } from '@vdg-webapp/models';

	import { page } from '$app/state';
	import { iconIds } from '$assets';
	import { CoordinateInput, GeometrySelect, UnitAwareInput } from '$components';
	import { Button, Form, Input, Separator, Textarea, Popover, Command } from '$core';
	import { tick } from "svelte";
	import { cn } from '$utils';
	import { getSettingsContext } from '$state';
	import { buttonVariants } from "$core/button/button.svelte";


	import { getVerdagraphContext } from '../verdagraphContext.svelte';
	import { useId } from "bits-ui";


	const verdagraphContext = getVerdagraphContext();
	const form = verdagraphContext.plantsCreateForm.form;
	const handler = verdagraphContext.plantsCreateForm.handler;
	const { form: formData, enhance } = form;

	const cultivarNames: {value: string}[] = []


	let cultivarNameComboboxOpen = false;

	// We want to refocus the trigger button when the user selects
	// an item from the list so users can continue navigating the
	// rest of the form with the keyboard.
	function closeAndFocusTrigger(triggerId: string) {
		cultivarNameComboboxOpen = false;
		tick().then(() => {
		document.getElementById(triggerId)?.focus();
		});
	}
	const triggerId = useId();

</script>

<form method="POST" autocomplete="off" use:enhance class="mx-4 mb-8 mt-4">
	<!-- Cultivar. -->
	<Form.Field {form} name="plants[0].cultivarName">
		<Popover.Root bind:open={cultivarNameComboboxOpen}>
		<Form.Control id={triggerId}>
			{#snippet children({ props })}
			<Form.Label>Language</Form.Label>
			<Popover.Trigger
				class={cn(
				buttonVariants({ variant: "outline" }),
				"w-[200px] justify-between",
				!$formData.plants[0].cultivarName && "text-neutral-11"
				)}
				role="combobox"
				{...props}
			>
				{cultivarNames.find((name) => name.value === $formData.plants[0].cultivarName)?.value ??
				"Select a cultivar"}
						<Icon
					icon={iconIds.caretUpDownIcon}
					width="1.5rem"
					class="text-neutral-11 absolute end-3 top-1/2 size-6 -translate-y-1/2"
				/>
			</Popover.Trigger>
			<input hidden value={$formData.plants[0].cultivarName} name={props.name} />
			{/snippet}
		</Form.Control>
		<Popover.Content class="w-[200px] p-0">
			<Command.Root>
			<Command.Input
				autofocus
				placeholder="Search cultivars..."
				class="h-9"
			/>
			<Command.Empty>No cultivar found.</Command.Empty>
			<Command.Group value="cultivarNames">
				{#each cultivarNames as name (name.value)}
				<Command.Item
					value={name.value}
					onSelect={() => {
					$formData.plants[0].cultivarName = name.value;
					closeAndFocusTrigger(triggerId);
					}}
				>
					{name.value}
											<Icon
					icon={iconIds.checkmarkIcon}
					width="1.5rem"
					class="text-neutral-11 absolute end-3 top-1/2 size-6 -translate-y-1/2"
				/>
				</Command.Item>
				{/each}
			</Command.Group>
			</Command.Root>
		</Popover.Content>
		</Popover.Root>
	</Form.Field>	
<!-- Aggregate. -->

	<!-- Origin. -->
	<!-- Locations. -->
	<!-- Geometries. -->
	<!-- Cultivar Attributes. -->

	<!-- Submit button -->
	<Form.Button
		disabled={false}
		loading={handler.isLoading}
		variant="default"
		class="mt-4 w-full">Create</Form.Button
	>
</form>
