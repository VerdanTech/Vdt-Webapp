<script lang="ts">
	import Icon from '@iconify/svelte';

	import iconIds from '$assets/icons';
	import { Button } from '$core/button/index.js';

	import { type EditableAttributeProps } from './types';

	let { editing, onChange }: EditableAttributeProps<undefined> = $props();
</script>

{#if editing}
	<Button
		class="flex w-full items-center justify-center select-none"
		onclick={() => {
			onChange(undefined);
		}}
	>
		<Icon icon={iconIds.addIcon} width="1.5rem" class="text-neutral-11" />
	</Button>
{:else}
	<Button class="flex w-full items-center justify-center select-none" disabled={true}>
		<Icon icon={iconIds.addIcon} width="1.5rem" class="text-neutral-11" />
	</Button>
{/if}
