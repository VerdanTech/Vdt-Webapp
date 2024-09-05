<script lang="ts">
	type Props = {
		editing: boolean;
		value: any;
	};

	let { editing = $bindable(), value }: Props = $props();
</script>

{#if editing}
	value
{:else}
	not edeting
{/if}
