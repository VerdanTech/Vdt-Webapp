<script lang="ts">
	import { Combobox } from 'bits-ui';
	import Icon from '@iconify/svelte';
	import iconIds from '$lib/assets/icons';
	import { flyAndScale } from '$lib/utils/index.js';
	import type { CultivarSchema } from '$codegen/types';
	type Props = {
		collectionId: string;
		cultivars: CultivarSchema[];
		value: string | undefined;
	};

	let { collectionId, cultivars = [], value = $bindable() }: Props = $props();

	let inputValue = $state('');
	let touchedInput = $state(false);

	let filteredOptions = $derived.by(() => {
		let cultivarOptions = cultivars.map((cultivar) => {
			return { value: cultivar.name, label: cultivar.name };
		});
		if (inputValue && touchedInput) {
			return cultivarOptions.filter((option) =>
				option.label.toLowerCase().includes(inputValue.toLowerCase())
			);
		} else {
			return cultivarOptions;
		}
	});
</script>

<Combobox.Root
	bind:inputValue
	bind:touchedInput
	onSelectedChange={(selected) => {
		if (selected) {
			value = cultivars.find((cultivar) => {
				return cultivar.name === selected.value;
			}).id;
		}
	}}
>
	<div class="relative">
		<Combobox.Input
			class="h-10 w-full rounded-md border border-neutral-11 bg-neutral-1 px-3 py-2 placeholder:text-neutral-11 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary-6 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
			placeholder="Search a Cultivar"
			aria-label="Search a Cultivar"
		/>
		<Icon
			icon={iconIds.caretUpDownIcon}
			width="1.5rem"
			class="absolute end-3 top-1/2 size-6 -translate-y-1/2 text-neutral-11"
		/>
	</div>

	<Combobox.Content
		class="w-full rounded-xl border border-neutral-10 bg-neutral-2 px-1 py-3 shadow-md outline-none"
		transition={flyAndScale}
		sideOffset={8}
	>
		{#each filteredOptions as cultivar (cultivar.value)}
			<Combobox.Item
				class="flex h-8 w-full select-none items-center rounded-md py-3 pl-5 pr-1.5 text-sm capitalize outline-none transition-all duration-75 data-[highlighted]:bg-neutral-3"
				value={cultivar.label}
				label={cultivar.label}
			>
				{cultivar.label}
				<Combobox.ItemIndicator class="ml-auto" asChild={false}>
					<Icon icon={iconIds.dotIcon} width="0.5rem" />
				</Combobox.ItemIndicator>
			</Combobox.Item>
		{:else}
			<span class="block px-5 py-2 text-sm text-neutral-11"> No results found </span>
		{/each}
	</Combobox.Content>
	<Combobox.HiddenInput name="favoriteFruit" />
</Combobox.Root>
