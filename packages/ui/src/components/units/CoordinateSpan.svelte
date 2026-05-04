<script lang="ts">
	import Icon from '@iconify/svelte';
	import { Button } from 'bits-ui';

	import { type UnitSystem, createUnitAwareValues } from './units.svelte';

	type Props = {
		/** The output X value. Guarnteed to be in metric. */
		x: number;
		/** The output Y value. Guarnteed to be in metric. */
		y: number;
		/** The initial unit system of the component. */
		initialUnitSystem: UnitSystem;
		/** The number of decimal places to prefer for conversions. */
		decimalPlaces?: number;
	};
	let {
		x = $bindable(),
		y = $bindable(),
		initialUnitSystem,
		decimalPlaces = 2,
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
			<span
				class="border-neutral-7 bg-neutral-1 flex w-full items-center justify-center rounded-l-none rounded-r-none rounded-tr-md border border-b-0 @xs:rounded-tr-none @xs:border-b"
				>{x}</span
			>
		</div>
		<div class="flex w-full">
			<span
				class="bg-neutral-2 border-neutral-7 @xs:border-x-neutral-5 flex h-10 w-8 items-center justify-center rounded-none border border-r-0 border-b-0 px-3 text-sm @xs:border-b @xs:border-l-0"
			>
				Y
			</span>
			<span
				class="border-neutral-7 bg-neutral-1 flex w-full items-center justify-center rounded-l-none rounded-r-none border border-b-0 @xs:border-b"
				>{y}</span
			>
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
