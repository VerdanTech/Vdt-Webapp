<script lang="ts">
	import Icon from '@iconify/svelte';
	import { Button } from '$lib/components/ui/button';
	import { Separator } from '$lib/components/ui/separator/index.js';
	import { Popover } from 'bits-ui';
	import { flyAndScale } from '$lib/utils/shadcn';
	import type { PrimaryTabSpec } from './primaryNavTabs';

	type Props = {
		spec: PrimaryTabSpec /* Describes the content of the tab. */;
	};
	let { spec }: Props = $props();

	let popover_open = $state(false);
</script>

<!--
@component
Single tab for navigating between feature domains on the main bottom bar.
-->

<Popover.Root bind:open={popover_open}>
	<Popover.Trigger
		class="flex h-full w-full justify-center text-neutral-12 transition-colors {popover_open
			? 'bg-neutral-3'
			: 'bg-neutral-2'}"
	>
		<Icon icon={spec.iconId} width="3rem" class="my-2" />
	</Popover.Trigger>
	<Popover.Content
		class="w-auto max-w-96 -translate-y-2 justify-evenly rounded-lg border border-neutral-6 bg-neutral-3 shadow-sm"
		transition={flyAndScale}
		transitionConfig={{
			duration: 150,
			y: 10,
			start: 1
		}}
	>
		<ul class="flex flex-col-reverse justify-center">
			<li class="w-full">
				<Button
					href={spec.url}
					class="w-full rounded-none rounded-b-lg bg-neutral-2 text-lg
						font-bold text-neutral-12 opacity-90 hover:bg-primary-5
						hover:text-primary-12 {spec.submenuItems === null || spec.submenuItems.length < 1
						? 'rounded-t-lg'
						: ''}">{spec.label}</Button
				>
			</li>
			<Separator class="w-full bg-neutral-6 opacity-50" />
			{#if spec.submenuItems}
				{#each spec.submenuItems ?? [] as item, index}
					<li class="flex items-center">
						<Button
							href={item.url}
							class="w-full justify-start truncate rounded-none bg-neutral-2 text-lg
								text-neutral-12 opacity-80 hover:bg-primary-5 hover:text-primary-12 {index ===
							spec.submenuItems.length - 1
								? 'rounded-t-lg'
								: ''}"
						>
							{#if item.iconId}
								<Icon
									icon={item.iconId}
									width="1.5rem"
									class="text-foreground my-2 mr-2 text-xl"
								/>
							{/if}
							<span class="truncate">
								{item.label}
							</span>
						</Button>
					</li>
				{/each}
			{/if}
			<li></li>
		</ul>
	</Popover.Content>
</Popover.Root>
