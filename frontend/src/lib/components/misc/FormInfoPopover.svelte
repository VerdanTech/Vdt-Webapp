<script lang="ts">
	import Icon from '@iconify/svelte';
	import iconIds from '$lib/assets/icons';
	import * as Popover from '$components/ui/popover';

	type Props = { description: string };

	let { description }: Props = $props();
</script>

<Popover.Root>
	<Popover.Trigger class="w-8">
		<Icon
			icon={iconIds.formFieldDescriptionIcon}
			width="1rem"
			class="ml-2 text-neutral-11 hover:text-neutral-10"
		/>
	</Popover.Trigger>
	<Popover.Content class="max-w-2xl">
		{description}
	</Popover.Content>
</Popover.Root>
