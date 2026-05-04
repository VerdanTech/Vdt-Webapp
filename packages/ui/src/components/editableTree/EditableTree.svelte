<script lang="ts">
	import Icon from '@iconify/svelte';

	import iconIds from '$assets/icons';
	import FormErrorsPopover from '$components/misc/FormErrorsPopover.svelte';
	import FormInfoPopover from '$components/misc/FormInfoPopover.svelte';

	import type { EditableTreeContext } from './tree.svelte';
	import { fromTreeId } from './utils';

	type Props = {
		/** The tree. */
		editableTree: EditableTreeContext;
		/** Field errors. */
		fieldErrors: Record<string, string[]>;
		/** If true the tree may be edited. */
		editing: boolean;
	};
	let { editableTree, fieldErrors, editing }: Props = $props();

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
</script>

<!-- Snippet for rendering a tree item. Allows arbitrary nesting. -->
{#snippet treeItems(items: (typeof editableTree.tree)['children'], depth: number = 0)}
	{#each items as item (item.id)}
		<!-- Item element. -->
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
			class="cursor-pointer py-3"
		>
			<!-- Item row. -->
			<div
				class="flex justify-between gap-4 rounded-md py-2 pr-2 {depth == 0
					? ''
					: 'pl-2'}"
				style="margin-left: {depth * 1}rem"
			>
				<!-- Left of the item row. -->
				<div class="flex items-center gap-2 pl-2">
					<!-- Selection button. Only allow for entity root items. -->
					{#if !fromTreeId(item.id).field}
						<button
							onclick={(e: MouseEvent) => {
								e.stopPropagation();
								if (!isControlOrMeta(e) && !e.shiftKey) item.tree.clearSelection();
								if (isControlOrMeta(e)) item.toggleSelect();
								else item.tree.select(item.id);
								if (e.shiftKey) item.tree.selectUntil(item.id);
								item.focus();
							}}
							aria-label="select"
							class="border-accent-8 mr-1 flex h-5 w-5 items-center justify-center rounded-[4px] border-2"
						>
							{#if item.selected}
								<span class="bg-accent-7 h-3 w-3 rounded-[4px]"> </span>
							{/if}
						</button>
					{/if}
					{#if item.item.icon}
						<Icon icon={item.item.icon} width="1.25rem" />
					{/if}
					<span>
						{item.item.label}
					</span>
					{#if item.item.description}
						<FormInfoPopover description={item.item.description} />
					{/if}
				</div>

				<!-- Right of the item row. -->
				<!-- Open/close chevron. -->
				{#if item.children?.length}
					<div class="flex grow items-center">
						<div class="bg-neutral-3 mx-3 h-[1px] w-full"></div>
						<Icon
							icon={iconIds.chevronRight}
							width="1rem"
							class="{item.expanded
								? 'rotate-90'
								: ''} ml-2 h-6 w-8 rounded-md p-1  {item.selected
								? 'hover:bg-accent-5'
								: 'hover:bg-neutral-3'}"
						/>
					</div>

					<!-- Editable value. -->
				{:else if item.item.valueComponent && item.item.onChange}
					<div
						onclick={(e) => e.stopPropagation()}
						onkeydown={(e) => e.stopPropagation()}
						role="none"
						class="flex w-1/2 items-center"
					>
						<div class="mr-1 flex items-center">
							{#if Object.keys(fieldErrors).includes(item.id)}
								<FormErrorsPopover errors={fieldErrors[item.id]} />
							{/if}
						</div>
						<item.item.valueComponent
							value={item.item.value}
							{editing}
							onChange={item.item.onChange}
							errors={Object.keys(fieldErrors).includes(item.id)}
						/>
					</div>
				{/if}
			</div>

			<!-- Item children. -->
			{#if item.children?.length && !item.item.value}
				<ul
					{...editableTree.tree.group}
					class="{item.expanded
						? 'h-auto opacity-100'
						: 'pointer-events-none h-0 opacity-0'} relative origin-left"
				>
					<div
						class="bg-neutral-5 absolute top-4 bottom-4 w-[1px]"
						style="left: {0.5 + depth * 1}rem"
					></div>
					{@render treeItems(item.children, depth + 1)}
				</ul>
			{/if}
		</li>
	{/each}
{/snippet}

<ul {...editableTree.tree.root} class="px-2">
	{@render treeItems(editableTree.tree.children)}
</ul>
