<script lang="ts">
	import { Tree } from 'melt/builders';

	import { localStore } from '@vdg-webapp/ui';

	import { page } from '$app/state';

	import { navItems } from './links';

	const expandedTreeItems = localStore('navigationExpanded', [
		'app',
		'project',
		'docs',
		'usage',
		'tutorials'
	]);
	const tree = new Tree({
		items: navItems,
		expanded: expandedTreeItems.value
	});
	$effect(() => {
		expandedTreeItems.value = [...tree.expanded];
	});

	/**
	 * Copied from Melt-ui's source as this is not exported.
	 */
	export function isMac(): boolean {
		return /mac/i.test(navigator.platform);
	}

	/**
	 * Copied from Melt-ui's source as this is not exported.
	 */
	export function isControlOrMeta(event: KeyboardEvent | MouseEvent): boolean {
		return isMac() ? event.metaKey : event.ctrlKey;
	}

	const url = new URL(page.url);
	const urlToken = url.pathname.split('/').pop();
	tree.clearSelection();
	if (urlToken) {
		tree.select(urlToken);
	}
</script>

<!--
@component The main navigation tree
-->

{#snippet treeItems(items: (typeof tree)['children'], depth: number = 0)}
	{#each items as item (item.id)}
		<li
			{...item.attrs}
			onclick={(e: MouseEvent) => {
				/**
				 * Because we don't want to select every
				 * item that we click, we need to override the
				 * onclick handler to seperate out the expanding
				 * and selecting of the item.
				 * This code is copied from Melt-ui's source and modified.
				 */

				e.stopPropagation();
				if (
					item.tree.expandOnClick &&
					item.canExpand &&
					(!item.tree.multiple || (!isControlOrMeta(e) && !e.shiftKey))
				) {
					item.toggleExpand();
				}
				item.focus();
			}}
			class="cursor-pointer rounded-sm !outline-none first:mt-0 [&:focus-visible>:first-child>div]:ring-4"
		>
			<div class="group py-1" style="padding-left: {depth * 1}rem">
				<a
					href={item.item.url}
					class="{item.selected ? '!bg-accent-5 !text-accent-12' : ''}
					ring-accent-6 ring-offset-neutral-12 group-hover:bg-neutral-3 flex h-full w-full items-center
					gap-2 rounded-xl px-3 py-1 transition"
				>
					<span class="select-none">
						{item.item.label}
					</span>
				</a>
			</div>
			{#if item.children?.length}
				<ul
					{...tree.group}
					class="relative list-none p-0 {!item.expanded
						? 'pointer-events-none h-0 opacity-0'
						: 'h-auto opacity-100'} origin-left"
				>
					<div
						class="absolute top-2 bottom-2 w-px bg-gray-200 dark:bg-gray-700"
						style="left: {0.5 + depth * 1}rem"
					></div>
					{@render treeItems(item.children, depth + 1)}
				</ul>
			{/if}
		</li>
	{/each}
{/snippet}

<ul class="mb-12 w-[200px] list-none" {...tree.root}>
	{@render treeItems(tree.children, 0)}
</ul>
