<script lang="ts">
	import { createTableOfContents } from '@melt-ui/svelte';

	import { Collapsible, ScrollArea } from '@vdg-webapp/ui';

	import Nav from '$components/nav/Nav.svelte';

	import TableOfContents from './nav/TableOfContents.svelte';
	import Tree from './nav/Tree.svelte';

	let { children } = $props();

	const {
		elements: { item },
		states: { activeHeadingIdxs, headingsTree }
	} = createTableOfContents({
		selector: '#content-container',
		exclude: ['h1'],
		activeType: 'all',
		headingFilterFn: (heading) => !heading.hasAttribute('data-toc-ignore')
	});
</script>

<!--
@component Wraps the main content with the navigation menus.
-->

<div class="flex w-full flex-col">
	<Nav />

	<div class="mx-auto mt-0 mb-12 flex flex-row justify-center gap-8 px-0 md:mt-12">
		<div class="sticky top-20 hidden h-full md:block">
			<Tree />
		</div>
		<div>
			<div class="sticky top-14 z-50">
				<Collapsible.Root
					class="bg-neutral-2 border-neutral-6 mb-4 flex w-full flex-col border px-8 py-4 md:hidden"
				>
					<Collapsible.Trigger class="text-neutral-11 font-semibold"
						>On This Page</Collapsible.Trigger
					>
					<Collapsible.Content>
						{#key $headingsTree}
							<TableOfContents
								tree={$headingsTree}
								activeHeadingIdxs={$activeHeadingIdxs}
								{item}
							/>
						{/key}
					</Collapsible.Content>
				</Collapsible.Root>
			</div>
			<div id="content-container" class="prose dark:prose-invert px-2 md:px-0">
				<ScrollArea.Root class="h-full">
					{@render children()}
				</ScrollArea.Root>
			</div>
		</div>
		<div class="sticky top-20 hidden h-full w-[200px] md:block">
			<p class="text-neutral-11 font-semibold">On This Page</p>
			<nav>
				{#key $headingsTree}
					<TableOfContents
						tree={$headingsTree}
						activeHeadingIdxs={$activeHeadingIdxs}
						{item}
					/>
				{/key}
			</nav>
		</div>
	</div>
</div>
