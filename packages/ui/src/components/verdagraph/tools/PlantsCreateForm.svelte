<script lang="ts">
	import Icon from '@iconify/svelte';
	import { toast } from 'svelte-sonner';

	import {
		AppError,
		type PlantsCreateFormMode,
		plantFields,
		plantsCreateFormModeSchema
	} from '@vdg-webapp/models';

	import { page } from '$app/state';
	import { iconIds } from '$assets';
	import { CoordinateInput, GeometrySelect, UnitAwareInput } from '$components';
	import { Button, Form, Input, Select, Separator, Textarea } from '$core';
	import { getSettingsContext } from '$state';

	import { getVerdagraphContext } from '../verdagraphContext.svelte';
	import PlantsCreateFormModeSingle from './PlantsCreateFormModeSingle.svelte';

	const settings = getSettingsContext();
	const verdagraphContext = getVerdagraphContext();
	const form = verdagraphContext.plantsCreateForm.form;
	const handler = verdagraphContext.plantsCreateForm.handler;
	const { form: formData, enhance } = form;

	$effect(() => {
		if (!verdagraphContext) {
			toast.error('Error retrieving verdagraph context.');
			throw new AppError('Error retrieving verdagraph context.');
		}

		$formData.gardenId = page.params.gardenId;
	});

	/** Set default form data for the mode. */
	let previousFormMode = $state('None');
	$effect(() => {
		if ($formData.mode === previousFormMode) {
			return;
		}
		switch ($formData.mode) {
			case 'SINGLE':
				$formData.plants = [];
				$formData.plants[0] = {
					cultivarName: 'undefined',
					origin: 'DIRECT_SEED',
					aggregate: false,
					locationHistory: { gardenId: '', locations: [] },
					geometryHistory: { gardenId: '', geometries: [] },
					cultivarOverride: {}
				};
				break;
			case 'GROUP':
				break;
			case 'PATTERN':
				break;
			case 'COMBINED':
				break;
		}
		previousFormMode = $formData.mode;
	});

	/* Defines the labels for the mode enum options. */
	const modeOptions: {
		value: PlantsCreateFormMode;
		label: string;
	}[] = [
		{ value: 'SINGLE', label: 'Single' },
		{ value: 'GROUP', label: 'Group' },
		{ value: 'PATTERN', label: 'Pattern' },
		{ value: 'COMBINED', label: 'Combined' }
	];
	const modeSelectTrigger = $derived(
		modeOptions.find((option) => option.value === $formData.mode) ?? {
			label: 'Select a mode',
			icon: null
		}
	);
</script>

<form method="POST" autocomplete="off" use:enhance class="mx-4 mb-8 mt-4">
	<!-- Form mode -->
	<Form.Field {form} name="mode">
		<Form.Control>
			{#snippet children({ props })}
				<Form.Label
					description={plantsCreateFormModeSchema.description}
					optional={false}>Mode</Form.Label
				>
				<Select.Root
					{...props}
					type="single"
					items={modeOptions}
					bind:value={$formData.mode}
				>
					<Select.Trigger>
						<div class="item-center flex">
							<span>
								{modeSelectTrigger.label}
							</span>
						</div>
					</Select.Trigger>
					<Select.Content>
						<Select.Group>
							<Select.GroupHeading>Form Mode</Select.GroupHeading>
							{#each modeOptions as modeOption}
								<Select.Item value={modeOption.value} label={modeOption.label}
									>{modeOption.label}</Select.Item
								>
							{/each}
						</Select.Group>
					</Select.Content>
				</Select.Root>
			{/snippet}
		</Form.Control>
		<Form.FieldErrors handlerErrors={handler.errors?.fieldErrors?.mode} />
	</Form.Field>

	{#if $formData.mode === 'SINGLE'}
		<PlantsCreateFormModeSingle></PlantsCreateFormModeSingle>
	{:else if $formData.mode === 'GROUP'}{:else if $formData.mode === 'PATTERN'}{:else if $formData.mode === 'COMBINED'}{/if}

	<!-- Submit button -->
	<Form.Button
		disabled={false}
		loading={handler.isLoading}
		variant="default"
		class="mt-4 w-full">Create</Form.Button
	>
</form>
