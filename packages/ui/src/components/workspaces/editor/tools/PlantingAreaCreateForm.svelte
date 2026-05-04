<script lang="ts">
	import Icon from '@iconify/svelte';
	import { toast } from 'svelte-sonner';

	import { AppError, workspaceFields } from '@vdg-webapp/models';

	import { page } from '$app/state';
	import { iconIds } from '$assets';
	import { CoordinateInput, GeometrySelect, UnitAwareInput } from '$components';
	import { Button, Form, Input, Separator, Textarea } from '$core';
	import { getAppContext } from '$state';

	import { getWorkspaceEditorContext } from '../workspaceEditorContext.svelte';

	const ctx = getAppContext();
	const workspaceEditor = getWorkspaceEditorContext();
	const form = workspaceEditor.plantingAreaCreateForm.form;
	const handler = workspaceEditor.plantingAreaCreateForm.handler;
	const { form: formData, enhance } = form;

	$effect(() => {
		if (!workspaceEditor.id) {
			toast.error('Error retrieving workspace context.');
			throw new AppError('Error retrieving workspace context.');
		}

		$formData.gardenId = ctx.garden.id;
		$formData.workspaceId = workspaceEditor.id;
		$formData.location.gardenId = ctx.garden.id;
		$formData.location.workspaceId = workspaceEditor.id;
		$formData.geometry.date = workspaceEditor.timelineSelection.focusUtc;
		$formData.location.date = workspaceEditor.timelineSelection.focusUtc;
	});
</script>

<form method="POST" autocomplete="off" use:enhance class="mx-4 mt-4 mb-8">
	<!-- Name. -->
	<Form.Field {form} name="name">
		<Form.Control>
			{#snippet children({ props })}
				<Form.Label
					description={workspaceFields.plantingAreaNameSchema.description}
					optional={false}>Name</Form.Label
				>
				<Input.Root
					{...props}
					type="text"
					placeholder="Big Bed"
					bind:value={$formData.name}
				/>
			{/snippet}
		</Form.Control>
		<Form.FieldErrors handlerErrors={handler.fieldErrors?.name} />
	</Form.Field>

	<!-- Description. -->
	<Form.Field {form} name="description">
		<Form.Control>
			{#snippet children({ props })}
				<Form.Label
					description={workspaceFields.plantingAreaDescriptionSchema.description}
					optional={true}>Description</Form.Label
				>
				<Textarea.Root {...props} bind:value={$formData.description} />
			{/snippet}
		</Form.Control>
		<Form.FieldErrors handlerErrors={handler.fieldErrors?.description} />
	</Form.Field>

	<!-- Position. -->
	<Form.Field {form} name="location">
		<Form.Control>
			{#snippet children({ props })}
				<Form.Label
					description={workspaceFields.coordinateSchema.description}
					optional={false}>Position</Form.Label
				>
				<CoordinateInput
					{...props}
					initialUnitSystem={ctx.settings.units['distance']}
					bind:x={$formData.location.coordinate.x}
					bind:y={$formData.location.coordinate.y}
				/>
			{/snippet}
		</Form.Control>
	</Form.Field>

	<!-- Geometry. -->
	<fieldset>
		<div class="my-2 flex items-center">
			<span class="text-neutral-11 mr-2"> Geometry </span>
			<span class="w-full">
				<Separator.Root class="w-full" />
			</span>
		</div>

		<!-- Type. -->
		<Form.Field {form} name="geometry.type">
			<Form.Control>
				{#snippet children({ props })}
					<Form.Label
						description={workspaceFields.geometryTypeSchema.description}
						optional={false}>Type</Form.Label
					>
					<GeometrySelect {...props} bind:value={$formData.geometry.type} />
				{/snippet}
			</Form.Control>
			<Form.FieldErrors handlerErrors={handler.fieldErrors?.['geometry.type']} />
		</Form.Field>

		<!-- Rotation. -->
		<Form.Field {form} name="geometry.rotation">
			<Form.Control>
				{#snippet children({ props })}
					<Form.Label
						description={workspaceFields.geometryRotationSchema.description}
						optional={true}>Rotation</Form.Label
					>
					<Input.Root
						{...props}
						type="number"
						bind:value={$formData.geometry.rotation}
					/>
				{/snippet}
			</Form.Control>
			<Form.FieldErrors handlerErrors={handler.fieldErrors?.['geometry.rotation']} />
		</Form.Field>

		<!-- RECTANGLE GEOMETRY. -->
		{#if $formData.geometry.type === 'RECTANGLE'}
			<!-- Length. -->
			<Form.Field {form} name="geometry.rectangleLength">
				<Form.Control>
					{#snippet children({ props })}
						<Form.Label
							description={workspaceFields.geometryRectangleLengthSchema.description}
							optional={false}>Length</Form.Label
						>
						<UnitAwareInput
							{...props}
							min={0}
							quantityType="distance"
							initialUnitSystem={ctx.settings.units['distance']}
							bind:value={$formData.geometry.rectangleLength}
						/>
					{/snippet}
				</Form.Control>
				<Form.FieldErrors
					handlerErrors={handler.fieldErrors?.['geometry.rectangleLength']}
				/>
			</Form.Field>

			<!-- Width. -->
			<Form.Field {form} name="geometry.rectangleWidth">
				<Form.Control>
					{#snippet children({ props })}
						<Form.Label
							description={workspaceFields.geometryRectangleWidthSchema.description}
							optional={false}>Width</Form.Label
						>
						<UnitAwareInput
							{...props}
							min={0}
							quantityType="distance"
							initialUnitSystem={ctx.settings.units['distance']}
							bind:value={$formData.geometry.rectangleWidth}
						/>
					{/snippet}
				</Form.Control>
				<Form.FieldErrors
					handlerErrors={handler.fieldErrors?.['geometry.rectangleWidth']}
				/>
			</Form.Field>

			<!-- POLYGON GEOMETRY. -->
		{:else if $formData.geometry.type === 'POLYGON'}
			<!-- Side count. -->
			<Form.Field {form} name="geometry.polygonNumSides">
				<Form.Control>
					{#snippet children({ props })}
						<Form.Label
							description={workspaceFields.geometryPolygonNumSidesSchema.description}
							optional={false}>Side Count</Form.Label
						>
						<Input.Root
							{...props}
							type="number"
							min={3}
							bind:value={$formData.geometry.polygonNumSides}
						/>
					{/snippet}
				</Form.Control>
				<Form.FieldErrors
					handlerErrors={handler.fieldErrors?.['geometry.polygonNumSides']}
				/>
			</Form.Field>

			<!-- Radius. -->
			<Form.Field {form} name="geometry.polygonRadius">
				<Form.Control>
					{#snippet children({ props })}
						<Form.Label
							description={workspaceFields.geometryPolygonRadiusSchema.description}
							optional={false}>Radius</Form.Label
						>
						<UnitAwareInput
							{...props}
							min={0}
							quantityType="distance"
							initialUnitSystem={ctx.settings.units['distance']}
							bind:value={$formData.geometry.polygonRadius}
						/>
					{/snippet}
				</Form.Control>
				<Form.FieldErrors
					handlerErrors={handler.fieldErrors?.['geometry.polygonRadius']}
				/>
			</Form.Field>

			<!-- ELLIPSE GEOMETRY. -->
		{:else if $formData.geometry.type === 'ELLIPSE'}
			<!-- Length diameter. -->
			<Form.Field {form} name="geometry.ellipseLength">
				<Form.Control>
					{#snippet children({ props })}
						<Form.Label
							description={workspaceFields.geometryEllipseLengthSchema.description}
							optional={false}>Length Diameter</Form.Label
						>
						<UnitAwareInput
							{...props}
							min={0}
							quantityType="distance"
							initialUnitSystem={ctx.settings.units['distance']}
							bind:value={$formData.geometry.ellipseLength}
						/>
					{/snippet}
				</Form.Control>
				<Form.FieldErrors
					handlerErrors={handler.fieldErrors?.['geometry.ellipseLength']}
				/>
			</Form.Field>

			<!-- Width diameter. -->
			<Form.Field {form} name="geometry.ellipseWidth">
				<Form.Control>
					{#snippet children({ props })}
						<Form.Label
							description={workspaceFields.geometryEllipseWidthSchema.description}
							optional={false}>Width Diameter</Form.Label
						>
						<UnitAwareInput
							{...props}
							min={0}
							quantityType="distance"
							initialUnitSystem={ctx.settings.units['distance']}
							bind:value={$formData.geometry.ellipseWidth}
						/>
					{/snippet}
				</Form.Control>
				<Form.FieldErrors
					handlerErrors={handler.fieldErrors?.['geometry.ellipseWidth']}
				/>
			</Form.Field>

			<!-- LINES GEOMETRY. -->
		{:else if $formData.geometry.type === 'LINES'}
			<!-- Coordinate. -->
			<!-- eslint-disable-next-line @typescript-eslint/no-unused-vars -->
			{#each $formData.geometry.linesCoordinates as _, index}
				<Form.Field {form} name={`geometry.linesCoordinates[${index}]`}>
					<Form.Control>
						{#snippet children({ props })}
							<Form.Label
								description={workspaceFields.coordinateSchema.description}
								optional={false}>Coordinate {index}</Form.Label
							>
							<CoordinateInput
								{...props}
								initialUnitSystem={ctx.settings.units['distance']}
								bind:x={$formData.geometry.linesCoordinates[index].x}
								bind:y={$formData.geometry.linesCoordinates[index].y}
							/>
						{/snippet}
					</Form.Control>
					<Form.FieldErrors
						handlerErrors={handler.fieldErrors?.[`geometry.linesCoordinates[${index}]`]}
					/>
				</Form.Field>
			{/each}

			<!-- Coordinate add button. -->
			<Button.Root
				onclick={() => {
					$formData.geometry.linesCoordinates = [
						...$formData.geometry.linesCoordinates,
						{ x: 0, y: 0 }
					];
				}}
				variant="outline"
				class="mb-4 flex w-full items-center justify-between"
			>
				<span> Add Point </span>
				<Icon icon={iconIds.addIcon} width="1.5rem" />
			</Button.Root>
		{/if}
	</fieldset>

	<!-- Other. -->
	<fieldset>
		<div class="my-2 flex items-center">
			<span class="text-neutral-11 mr-2"> Other </span>
			<span class="w-full">
				<Separator.Root class="w-full" />
			</span>
		</div>

		<!-- Depth. -->
		<Form.Field {form} name={`depth`}>
			<Form.Control>
				{#snippet children({ props })}
					<Form.Label
						description={workspaceFields.plantingAreaDepthSchema.description}
						optional={true}>Depth</Form.Label
					>
					<UnitAwareInput
						{...props}
						min={0}
						quantityType="distance"
						initialUnitSystem={ctx.settings.units['distance']}
						bind:value={$formData.depth}
					/>
				{/snippet}
			</Form.Control>
			<Form.FieldErrors handlerErrors={handler.fieldErrors?.['depth']} />
		</Form.Field>
	</fieldset>

	<!-- Submit button -->
	<Form.Button
		disabled={false}
		loading={handler.isLoading}
		variant="default"
		class="mt-4 w-full">Create</Form.Button
	>
</form>
