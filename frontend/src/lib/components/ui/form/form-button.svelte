<script lang="ts">
	import * as Button from '$lib/components/ui/button/index.js';
	import Icon from '@iconify/svelte';
	import iconIds from '$lib/assets/icons';

	type $$Props = Button.Props & {
		disabled?: boolean;
		loading?: boolean;
	};
	type $$Events = Button.Events;

	export let disabled: boolean = false;
	export let loading: boolean = false;
</script>

<Button.Root {disabled} type="submit" on:click on:keydown {...$$restProps}>
	{#if loading}
		<Icon icon={iconIds.defaultSpinnerIcon} width="1.5rem" class="animate-spin" />
	{:else}
		<slot />
	{/if}
</Button.Root>
