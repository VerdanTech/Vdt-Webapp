<script lang="ts">
	import Icon from '@iconify/svelte';
	import { Button } from 'bits-ui';

	import { type Position } from '@vdg-webapp/models';

	import { Input } from '$core/input/index.js';

	import { type UnitSystem, createUnitAwareValues } from './units.svelte';

	type Props = {
		/** The output X value. Guarnteed to be in metric. */
		x: number;
		/** The output Y value. Guarnteed to be in metric. */
		y: number;
		/** The initial unit system of the component. */
		initialUnitSystem: UnitSystem;
		/** Change handler. */
		onValueChange?: (value: Position) => void;
		/** The number of decimal places to prefer for conversions. */
		decimalPlaces?: number;
		/** The input properties, in meters. */
		step?: number;
		min?: number;
		max?: number;
	};
	let {
		x = $bindable(),
		y = $bindable(),
		initialUnitSystem,
		onValueChange,
		decimalPlaces = 2,
		step = 0.01,
		min,
		max,
		...restProps
	}: Props = $props();

	const unitAwareValues = createUnitAwareValues(
		'distance',
		[x, y],
		initialUnitSystem,
		decimalPlaces
	);

	/** Track external value changes. */
	$effect(() => {
		unitAwareValues.setDisplayValues([x, y]);
	});

	/** The input properties, in the unit system. */
	let unitAwareMin = $derived.by(() => {
		if (min) {
			return unitAwareValues.metricToCurrentUnit(min);
		} else {
			return '';
		}
	});
	let unitAwareMax = $derived.by(() => {
		if (max) {
			return unitAwareValues.metricToCurrentUnit(max);
		} else {
			return '';
		}
	});
</script>

<div {...restProps} class="@container h-full w-full">
	<div
		class="flex w-full grid-cols-3 grid-rows-2 flex-col justify-between @xs:flex-row"
	>
		<div class="flex w-full">
			<span
				class="bg-neutral-2 border-neutral-7 border-r-neutral-5 flex h-10 w-8 items-center justify-center rounded-l-md rounded-bl-none border border-r-0 border-b-0 px-3 text-sm @xs:rounded-bl-md @xs:border-b"
			>
				X
			</span>
			<Input
				value={unitAwareValues.displayValues[0]}
				type="number"
				{step}
				min={unitAwareMin}
				max={unitAwareMax}
				oninput={(event) => {
					unitAwareValues.handleInput(event, 0);
					x = unitAwareValues.metricValues[0];
					if (onValueChange) {
						onValueChange({
							x: unitAwareValues.metricValues[0],
							y: unitAwareValues.metricValues[1]
						});
					}
				}}
				class="w-full rounded-l-none rounded-r-none rounded-tr-md border-b-0 @xs:rounded-tr-none @xs:border-b"
			/>
		</div>
		<div class="flex w-full">
			<span
				class="bg-neutral-2 border-neutral-7 @xs:border-x-neutral-5 flex h-10 w-8 items-center justify-center rounded-none border border-r-0 border-b-0 px-3 text-sm @xs:border-b @xs:border-l-0"
			>
				Y
			</span>
			<Input
				value={unitAwareValues.displayValues[1]}
				type="number"
				{step}
				min={unitAwareMin}
				max={unitAwareMax}
				oninput={(event) => {
					unitAwareValues.handleInput(event, 1);
					y = unitAwareValues.metricValues[1];
					if (onValueChange) {
						onValueChange({
							x: unitAwareValues.metricValues[0],
							y: unitAwareValues.metricValues[1]
						});
					}
				}}
				class="rounded-l-none rounded-r-none border-b-0 @xs:border-b"
			/>
		</div>
		<span
			class="border-x-neutral-7 @xs:border-x-neutral-5 bg-neutral-2 border-neutral-7 flex h-8 w-full min-w-10 items-center justify-center border-x border-y border-b-0 px-3 @xs:h-10 @xs:w-8 @xs:border-b @xs:border-l-0 {unitAwareValues.unitSystem ===
			'metric'
				? 'text-lg'
				: 'text-md'} text-neutral-11">{unitAwareValues.unitSymbol}</span
		>
		<Button.Root
			onclick={unitAwareValues.swapUnits}
			type="button"
			class="border-x-neutral-7 @xs:border-x-neutral-5 bg-neutral-2 hover:bg-neutral-3 flex h-8 w-full items-center justify-center rounded-b-md border px-2 @xs:h-10 @xs:w-8 @xs:rounded-none @xs:rounded-r-md"
		>
			<Icon icon="material-symbols:swap-horiz-rounded" width="1rem" />
		</Button.Root>
	</div>
</div>
