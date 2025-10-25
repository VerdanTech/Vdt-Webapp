<script lang="ts">
	import Icon from '@iconify/svelte';
	import { useId } from 'bits-ui';
	import { tick } from 'svelte';
	import { toast } from 'svelte-sonner';

	import {
		AppError,
		plantFields,
		plantsCreateCommandSinglePlantSchema
	} from '@vdg-webapp/models';

	import { page } from '$app/state';
	import { iconIds } from '$assets';
	import { CoordinateInput, GeometrySelect, UnitAwareInput } from '$components';
	import {
		Button,
		Checkbox,
		Command,
		Form,
		Input,
		Popover,
		Separator,
		Textarea
	} from '$core';
	import { buttonVariants } from '$core/button/button.svelte';
	import { getControllerContext, getSettingsContext } from '$state';
	import { cn } from '$utils';

	import { getVerdagraphContext } from '../verdagraphContext.svelte';
	import { useQuery } from '@triplit/svelte';

	import { getCultivarContext } from '$state/context/cultivarContext';

	const controller = getControllerContext()
	const verdagraphContext = getVerdagraphContext();
	const cultivarContext = getCultivarContext();
	const form = verdagraphContext.plantsCreateForm.form;
	const handler = verdagraphContext.plantsCreateForm.handler;
	const { form: formData, enhance } = form;

	let plant = $derived($formData.plants[0] || null);

	const cultivarNames: { value: string }[] = [{ value: 'one' }, { value: 'two' }];
	let cultivarNames = $derived(useQuery(controller.triplit, controller.triplit.query('cultivars').Include(['name']).Where()))

	let cultivarNameComboboxOpen = $state(false);

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

	/** Initialize geometry history when cultivar changes. */
	$effect(() => {
		/** Get cultivar object from cultivar name. */
		/** Get default geometry history from cultivar object. */
	});
</script>

{#if plant}
	<!-- Cultivar. -->
	<Form.Field {form} name="plants[0].cultivarName">
		<Popover.Root bind:open={cultivarNameComboboxOpen}>
			<Form.Control id={triggerId}>
				{#snippet children({ props })}
					<Form.Label>Cultivar</Form.Label>
					<Popover.Trigger
						class={cn(
							buttonVariants({ variant: 'outline' }),
							'w-full justify-between',
							!$formData.plants[0].cultivarName && 'text-neutral-11'
						)}
						role="combobox"
						{...props}
					>
						{cultivarNames.find(
							(name) => name.value === $formData.plants[0].cultivarName
						)?.value ?? 'Select a cultivar'}
						<Icon
							icon={iconIds.caretUpDownIcon}
							width="1.5rem"
							class="ml-2 size-4 shrink-0 opacity-50"
						/>
					</Popover.Trigger>
					<input hidden value={$formData.plants[0].cultivarName} name={props.name} />
				{/snippet}
			</Form.Control>
			<!-- TODO: Add handler errors -->
			<Form.FieldErrors />
			<Popover.Content class="w-full p-0">
				<Command.Root>
					<Command.Input autofocus placeholder="Search cultivars..." class="h-9" />
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
									icon={iconIds.checkmarkIconUnfilled}
									width="1.5rem"
									class="ml-auto {name.value !== $formData.plants[0].cultivarName &&
										'text-transparent'}"
								/>
							</Command.Item>
						{/each}
					</Command.Group>
				</Command.Root>
			</Popover.Content>
		</Popover.Root>
	</Form.Field>

	<!-- Aggregate. -->
	<Form.Field {form} name="plants[0].aggregate">
		<Form.Control>
			{#snippet children({ props })}
				<div class="flex w-full items-center justify-between">
					<Form.Label
						description={plantFields.plantAggregateSchema.description}
						optional={false}
						class="justify-start gap-4">Aggregate</Form.Label
					>
					<Checkbox.Root {...props} bind:checked={$formData.plants[0].aggregate} />
				</div>
			{/snippet}
		</Form.Control>
		<!-- TODO: Add handler errors -->
		<Form.FieldErrors />
	</Form.Field>

	<!-- Origin. -->
	<!-- Locations. -->
	<!-- Geometries. -->
	<!-- Cultivar Attributes. -->
{/if}
