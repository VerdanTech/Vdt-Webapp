<script lang="ts">
	type Props = {};

	let { formAttrs = undefined, value = $bindable(), editing, onChange } = $props();
</script>

{#if editing && formAttrs}
	<input {...formAttrs} type="number" bind:value oninput={onChange} placeholder="None" />
{:else}
	<span class="mx-2 rounded-lg border border-neutral-4 bg-neutral-2 px-4 py-2">
		{value}
	</span>
{/if}
