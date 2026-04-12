<script lang="ts">
	import Icon from '@iconify/svelte';

	import { type GeometryType } from '@vdg-webapp/models';

	import iconIds from '$assets/icons';
	import * as Select from '$core/select/index.js';

	type Props = {
		value: GeometryType;
		label?: string;
		onValueChange?: (value: GeometryType) => void;
	};
	let { value = $bindable(), label = $bindable(), onValueChange }: Props = $props();

	const geometryTypeOptions: { value: GeometryType; label: string; icon: string }[] = [
		{ value: 'RECTANGLE', label: 'Rectangle', icon: iconIds.rectangleIcon },
		{ value: 'POLYGON', label: 'Polygon', icon: iconIds.polygonIcon },
		{ value: 'ELLIPSE', label: 'Ellipse', icon: iconIds.ellipseIcon },
		{ value: 'LINES', label: 'Lines', icon: iconIds.linesIcon }
	];
	const geometryTypeSelectTrigger = $derived(
		geometryTypeOptions.find((option) => option.value === value) ?? {
			label: 'Select a type',
			icon: null
		}
	);
	$effect(() => {
		if (label) {
			label = geometryTypeSelectTrigger.label;
		}
	});
</script>

<Select.Root
	type="single"
	{value}
	items={geometryTypeOptions}
	onValueChange={(newValue) => {
		value = newValue as GeometryType;
		if (onValueChange) {
			onValueChange(value);
		}
	}}
>
	<Select.Trigger class="w-full">
		<div class="flex w-full items-center justify-between px-2">
			<span>
				{geometryTypeSelectTrigger.label}
			</span>
			{#if geometryTypeSelectTrigger.icon}
				<Icon
					icon={geometryTypeSelectTrigger.icon}
					width="1.5rem"
					class="text-neutral-11 ml-4"
				/>
			{/if}
		</div>
	</Select.Trigger>
	<Select.Content>
		<Select.Group>
			{#each geometryTypeOptions as option}
				<Select.Item value={option.value} label={option.label}>
					<div class="flex w-full items-center justify-between px-2">
						<span>
							{option.label}
						</span>
						{#if option.icon}
							<Icon icon={option.icon} width="1rem" class="text-neutral-11 ml-4" />
						{/if}
					</div>
				</Select.Item>
			{/each}
		</Select.Group>
	</Select.Content>
</Select.Root>
