<script lang="ts">
	import Icon from '@iconify/svelte';
	import { type DateValue } from '@internationalized/date';

	import iconIds from '$assets/icons';
	import { calculateDeltaDays } from '$components/timeline/utils';
	import { Popover } from '$core';
	import { ScrollArea } from '$core/scroll-area/index.js';
	import { cn } from '$utils';

	import { type CalendarContext, type CalendarPaneContext } from './context.svelte';

	type Props = {
		context: CalendarContext<any>;
		pane: CalendarPaneContext;
	};
	let { context, pane }: Props = $props();

	/** 0-1 percentage that the section label takes of the section height. */
	const LABEL_SECTION_HEIGHT_PORTION = 0.4;

	/**
	 * Calculates the leftpoint of a section, in %.
	 * @param sectionIndex The index of the section from
	 */
	function calculateSectionLeft(sectionIndex: number): number {
		return (sectionIndex / (context.container.numSections + 1)) * 100;
	}

	function calculateItemleft(startDate: DateValue) {
		return (
			(calculateDeltaDays(startDate, context.timeline.beginSelection) /
				(context.container.numSections + 1)) *
			100
		);
	}

	function calculateItemWidth(endDate: DateValue, startDate: DateValue) {
		return (
			(Math.max(calculateDeltaDays(endDate, startDate) + 1, 0) /
				(context.container.numSections + 1)) *
			100
		);
	}

	function calculateInfoPointLeft(
		itemStartDate: DateValue,
		itemEndDate: DateValue,
		infoPointDate: DateValue
	) {
		return (
			(calculateDeltaDays(infoPointDate, itemStartDate) /
				(calculateDeltaDays(itemEndDate, itemStartDate) + 1)) *
			100
		);
	}

	let sectionWidthPx = $derived(
		context.container.width /
			(context.timeline.sliderValue[2] - context.timeline.sliderValue[0] + 1)
	);
</script>

<!-- Snippet for rendering a calendar item. Allows arbitrary nesting. -->
{#snippet calendarItems(items: (typeof pane.tree)['children'], depth: number = 0)}
	{#each items as item (item.id)}
		{@const itemLeft = calculateItemleft(item.item.startDate)}
		{@const itemWidth = calculateItemWidth(item.item.endDate, item.item.startDate)}
		{@const roundedStart = item.item.startDate < context.timeline.beginSelection}

		<!-- Item element. -->
		<li {...item.attrs}>
			<!-- Item row. -->
			<div
				style:left="{itemLeft}%"
				style:height="{item.item.labelOnly
					? context.container.sectionHeight * LABEL_SECTION_HEIGHT_PORTION
					: context.container.sectionHeight}px"
				style:width="{itemWidth}%"
				style:background-color={item.item.fillColor}
				style:border-color={item.item.borderColor}
				class={cn(
					'relative flex flex-col rounded-sm border-2',
					item.expanded ? item.item.itemStyleExpanded || '' : item.item.itemStyleCollapsed || '',
					item.expanded
						? `mb-${item.item.bottomMarginChild !== undefined ? item.item.bottomMarginChild : item.item.bottomMargin}`
						: `mb-${item.item.bottomMargin}`,
					roundedStart ? 'rounded-l-none' : ''
				)}
			>
				<!-- Top row - label-->
				<div
					class="flex w-full items-center {item.item.labelOnly
						? 'h-[100%]'
						: `h-[${LABEL_SECTION_HEIGHT_PORTION * 100}%]`}"
				>
					<span class="text-neutral-12 sticky left-0 flex items-center text-xs">
						<!-- Label. -->
						<span class="text-neutral-12 ml-2">
							{item.item.label}
						</span>

						<!-- Tree item expansion indicatator-->
						{#if item.children?.length}
							<Icon
								icon={iconIds.chevronRight}
								width="1.25rem"
								class={cn('text-neutral-9 mx-1', item.expanded ? 'rotate-90' : '')}
							/>
						{:else}
							<span class="bg-neutral-10 mx-2 h-[3px] w-[3px] rounded-lg"></span>
						{/if}

						<!-- Description. -->
						<span class="text-neutral-11 mr-2 truncate">
							{item.item.description || ''}
						</span>
					</span>
				</div>

				{#if item.item.labelOnly == false}
					<!-- Seperator. -->
					<div
						style:background-color={item.item.borderColor}
						class="h-[1px] w-full"
					></div>

					<!-- Info popups. -->
					<div class="relative flex h-full w-full">
						{#each item.item.infoPoints || [] as infoPoint}
							{@const infoPointLeft = calculateInfoPointLeft(
								item.item.startDate,
								item.item.endDate,
								infoPoint.date
							)}

							<div
								style:left="{infoPointLeft}%"
								style:width="{sectionWidthPx}px"
								class="absolute flex h-full items-center"
							>
								{#snippet infoPointIcon(icon?: string)}
									{#if icon}
										<Icon
											color={item.item.borderColor}
											width="1.4rem"
											{icon}
											class="mx-auto"
										/>
									{:else}
										<span
											style:background-color={item.item.itemColor}
											style:border-color={item.item.borderColor}
											class="mx-auto h-5 w-5 rounded-lg border"
										></span>
									{/if}
								{/snippet}

								{#if infoPoint.popup}
									<Popover.Root>
										<Popover.Trigger>
											{@render infoPointIcon(infoPoint.icon)}
										</Popover.Trigger>
										<Popover.Content>
											<infoPoint.popup></infoPoint.popup>
										</Popover.Content>
									</Popover.Root>
								{:else}
									{@render infoPointIcon(infoPoint.icon)}
								{/if}

								<span
									style:text-decoration-color={item.item.borderColor}
									class="text-neutral-12 text-md absolute ml-[40px] w-64 truncate text-xs underline underline-offset-[5px]"
									>{infoPoint.label}</span
								>
							</div>
						{/each}
					</div>
				{/if}
			</div>

			{#if item.children?.length}
				<ul
					{...pane.tree.group}
					class={item.expanded ? 'opacity-100' : 'pointer-events-none h-0 opacity-0'}
				>
					{@render calendarItems(item.children, depth + 1)}
				</ul>
			{/if}
		</li>
	{/each}
{/snippet}

<ScrollArea class="h-full w-full">
	<div bind:clientHeight={pane.height} class="relative h-full w-full overflow-hidden">
		{#each context.container.sections as section}
			{@const tickLeft = calculateSectionLeft(section)}
			{@const sectionEven = section % 2 == 0}
			<div
				style:left="{tickLeft}%"
				style="translate: -50%"
				class="{sectionEven ? 'bg-neutral-3' : 'bg-neutral-2'} absolute h-full w-[2px]"
			></div>
		{/each}

		<ul {...pane.tree.root} class="pt-2">
			{@render calendarItems(pane.tree.children)}
		</ul>
	</div>
</ScrollArea>
