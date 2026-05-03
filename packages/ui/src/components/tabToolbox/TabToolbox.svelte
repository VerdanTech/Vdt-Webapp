<script lang="ts">
	import Icon from '@iconify/svelte';
	import { ScrollArea } from 'bits-ui';

	import iconIds from '$assets/icons';
	import { Button } from '$core/button';
	import * as Tabs from '$core/tabs';

	import createToolbox from './tools.svelte';

	type Props = {
		// eslint-disable-next-line @typescript-eslint/no-explicit-any
		toolbox: ReturnType<typeof createToolbox<any>>;
	};
	let { toolbox }: Props = $props();

	/** For some reason, need to calculate tab height manually or it extends its parent. */
	let root: HTMLElement | null = $state(null);
	let list: HTMLElement | null = $state(null);
	let contentHeight = $derived.by(() => {
		if (root && list) {
			return root.offsetHeight - list.offsetHeight;
		} else {
			return 0;
		}
	});
</script>

<Tabs.Root
	bind:ref={root}
	bind:value={toolbox.lastActivatedId}
	class="bg-neutral-1 flex h-full flex-col"
>
	<Tabs.List bind:ref={list} class="h-8 shadow-none">
		{#each toolbox.activeTools as tool}
			<Tabs.Trigger
				value={tool.id}
				class="border-neutral-5 text-neutral-11 flex w-full items-center justify-between border-b p-0 px-4 py-1 {toolbox.lastActivatedId ===
				tool.id
					? 'bg-neutral-2 hover:bg-neutral-3'
					: 'bg-neutral-1 hover:bg-neutral-2'}"
			>
				<span class="truncate">
					{tool.label}
				</span>
				<Button
					variant="ghost"
					class="hover:bg-accent-5 h-auto rounded-md p-1"
					onclick={() => toolbox.deactivate(tool.id)}
				>
					<Icon icon={iconIds.defaultClose} width="1rem" />
				</Button>
			</Tabs.Trigger>
		{/each}
	</Tabs.List>
	{#each toolbox.activeTools as tool}
		<Tabs.Content
			value={tool.id}
			class="mt-0 overflow-hidden"
			style="height: {contentHeight}px"
		>
			<ScrollArea.Root class="relative h-full">
				<ScrollArea.Viewport class="h-full max-h-full w-full">
					<tool.ToolComponent />
				</ScrollArea.Viewport>
				<ScrollArea.Scrollbar
					orientation="vertical"
					class="bg-neutral-2 hover:bg-dark-10 data-[state=visible]:animate-in data-[state=hidden]:animate-out data-[state=hidden]:fade-out-0 data-[state=visible]:fade-in-0 flex w-2.5 touch-none rounded-none border-l border-l-transparent p-px transition-all duration-200 select-none hover:w-3"
				>
					<ScrollArea.Thumb class="bg-neutral-5 flex-1 rounded-full" />
				</ScrollArea.Scrollbar>
			</ScrollArea.Root>
		</Tabs.Content>
	{/each}
</Tabs.Root>
