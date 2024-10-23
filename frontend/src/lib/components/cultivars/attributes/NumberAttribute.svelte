<script lang="ts">
	import { Input } from '$lib/components/ui/input';

	type Props = {};

	let {
		formAttrs = undefined,
		attributeKey,
		value = $bindable(),
		editing,
		onChange
	} = $props();
</script>

{#if editing && formAttrs}
	<Input
		{...formAttrs}
		type="number"
		bind:value
		oninput={onChange}
		placeholder="None"
		class="w-auto"
	/>
{:else if value}
	<span class="rounded-lg border border-neutral-4 bg-neutral-2 px-4 py-2">
		{value}
	</span>
{:else}
	<span class="px-4 py-2 font-light italic text-neutral-11"> None </span>
{/if}
