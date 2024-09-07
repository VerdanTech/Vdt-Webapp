<script lang="ts">
	type Props = {
		editing: boolean;
		nonEditingComponent: unknown;
		editingComponent: unknown;
	};

	let { editing, nonEditingComponent, editingComponent }: Props = $props();
</script>

{#if editing}
	{@render nonEditingComponent()}
{:else}
	{@render editingComponent()}
{/if}
