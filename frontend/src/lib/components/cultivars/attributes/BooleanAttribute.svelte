<script lang="ts">
	import * as Select from '$lib/components/ui/select';

	type Props = {};

	let {
		formAttrs = undefined,
		attributeKey,
		value = $bindable(),
		editing,
		onChange
	} = $props();

	const options = [
		{ value: true, label: 'True' },
		{ value: false, label: 'False' }
	];

	let selectedValue = $state(value ? options[0] : options[1]);
</script>

{#if editing && formAttrs}
	<Select.Root
		selected={selectedValue}
		onSelectedChange={(newSelected) => {
			console.log(newSelected);
			if (newSelected) {
				value = newSelected.value;
				selectedValue = newSelected;
			}
			if (onChange) {
				onChange();
			}
		}}
		{...formAttrs}
	>
		<Select.Trigger class="w-32">
			<Select.Value placeholder="None" />
		</Select.Trigger>
		<Select.Content>
			<Select.Group>
				{#each options as option}
					<Select.Item value={option.value} label={option.label}
						>{option.label}</Select.Item
					>
				{/each}
			</Select.Group>
		</Select.Content>
		<Select.Input name={attributeKey} />
	</Select.Root>
{:else if value}
	<span class="rounded-lg border border-neutral-4 bg-neutral-2 px-4 py-2">
		{value ? 'True' : 'False'}
	</span>
{:else}
	<span class="px-4 py-2 font-light italic text-neutral-11"> None </span>
{/if}
