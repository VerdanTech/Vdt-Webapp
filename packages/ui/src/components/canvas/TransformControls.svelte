<script lang="ts">
	import Icon from '@iconify/svelte';
	import { getContext } from 'svelte';

	import { Button } from '$core/button/index.js';
	import * as Collapsible from '$core/collapsible/index.js';
	import * as Tooltip from '$core/tooltip/index.js';

	import type { CanvasContext } from './state';

	type Direction = 'horizontal' | 'vertical';

	/** Props. */
	type Props = {
		canvasId: string;
	};
	let { canvasId }: Props = $props();

	let canvas = getContext<CanvasContext>(canvasId);

	/** The width of the container to switch between vertical and horizontal buttons. */
	const buttonDirectionBreakpoint = 400;

	let buttonsDirection = $derived<Direction>(
		canvas.container.width < buttonDirectionBreakpoint ? 'vertical' : 'horizontal'
	);

	/**
	 * Controls the position of the toolbar within the layout container.
	 */
	let collapsibleFlexPositioning = $derived.by(() => {
		switch (canvas.transform.config.buttonsPosition) {
			case 'bl':
				return 'justify-start items-end';
			case 'br':
				return 'justify-end items-end';
			case 'tl':
				return 'justify-start items-start';
			case 'tr':
				return 'justify-end items-start';
		}
	});

	/** Controls the order of items in the toolbar. */
	let collapsibleFlexDirection = $derived.by(() => {
		switch (buttonsDirection) {
			case 'horizontal':
				switch (canvas.transform.config.buttonsPosition) {
					case 'bl':
						return 'flex-row';
					case 'br':
						return 'flex-row-reverse';
					case 'tl':
						return 'flex-row';
					case 'tr':
						return 'flex-row-reverse';
				}
				break;
			case 'vertical':
				switch (canvas.transform.config.buttonsPosition) {
					case 'bl':
						return 'flex-col-reverse';
					case 'br':
						return 'flex-col-reverse';
					case 'tl':
						return 'flex-col';
					case 'tr':
						return 'flex-col';
				}
				break;
		}
	});

	/** Controls the alignment of the toolbar to the edge of the container. */
	let collapsibleFlexAlignment = $derived.by(() => {
		switch (buttonsDirection) {
			case 'horizontal':
				switch (canvas.transform.config.buttonsPosition) {
					case 'bl':
						return 'items-end';
					case 'br':
						return 'items-end';
					case 'tl':
						return 'items-start';
					case 'tr':
						return 'items-start';
				}
				break;
			case 'vertical':
				switch (canvas.transform.config.buttonsPosition) {
					case 'bl':
						return 'items-start';
					case 'br':
						return 'items-end';
					case 'tl':
						return 'items-start';
					case 'tr':
						return 'items-end';
				}
				break;
		}
	});

	/** Controls the rotation of the collapsible trigger. */
	let collapsibleTriggerRotation = $derived.by(() => {
		switch (buttonsDirection) {
			case 'horizontal':
				switch (canvas.transform.config.buttonsPosition) {
					case 'bl':
						return canvas.transform.config.buttonsExpanded ? 'rotate-180' : 'rotate-10';
					case 'br':
						return canvas.transform.config.buttonsExpanded ? 'rotate-0' : 'rotate-180';
					case 'tl':
						return canvas.transform.config.buttonsExpanded ? 'rotate-180' : 'rotate-0';
					case 'tr':
						return canvas.transform.config.buttonsExpanded ? 'rotate-0' : 'rotate-180';
				}
				break;
			case 'vertical':
				switch (canvas.transform.config.buttonsPosition) {
					case 'bl':
						return canvas.transform.config.buttonsExpanded ? '-rotate-90' : 'rotate-90';
					case 'br':
						return canvas.transform.config.buttonsExpanded ? '-rotate-90' : 'rotate-90';
					case 'tl':
						return canvas.transform.config.buttonsExpanded ? 'rotate-90' : '-rotate-90';
					case 'tr':
						return canvas.transform.config.buttonsExpanded ? 'rotate-90' : '-rotate-90';
				}
				break;
		}
	});
</script>

<!--
@component
Renders a toolbar for manipulating the canvas above the canvas.
Note that pointer events must be enabled on each button individually,
this is because they are disabled on the overlay container div to allow
the events to hit the canvas underneath.
-->
<div class="flex h-full w-full p-2 {collapsibleFlexPositioning}">
	<Tooltip.Root delayDuration={800}>
		<Collapsible.Root
			bind:open={canvas.transform.config.buttonsExpanded}
			class="z-50 flex {collapsibleFlexDirection} {collapsibleFlexAlignment} justify-start gap-2"
		>
			<Tooltip.Trigger class="order-last">
				<Collapsible.Trigger>
					<Button
						variant="outline"
						size="xsm"
						class="hover:bg-secondary-5 bg-neutral-1 hover:text-secondary-12 pointer-events-auto flex items-center justify-center"
					>
						<Icon
							icon={'material-symbols:double-arrow'}
							width="3rem"
							class="{collapsibleTriggerRotation} text-neutral-11 transition-transform"
						/>
					</Button>
				</Collapsible.Trigger>
			</Tooltip.Trigger>
			<Tooltip.Content>Toggle Layout Controls</Tooltip.Content>
			<Collapsible.Content>
				<div class="flex {collapsibleFlexDirection} {collapsibleFlexAlignment} gap-2">
					<!-- Zoom controls. -->
					<div class="flex items-center">
						<!-- Zoom out.-->
						<Tooltip.Root>
							<Tooltip.Trigger>
								<Button
									onclick={() => {
										canvas.transform.addScale(-0.1);
									}}
									variant="outline"
									size="xsm"
									class="hover:bg-secondary-5 bg-neutral-1 hover:text-secondary-12 border-r-neutral-4 pointer-events-auto flex items-center justify-center rounded-r-none"
								>
									<Icon
										icon={'material-symbols:zoom-out'}
										width="3rem"
										class="text-neutral-11"
									/>
								</Button>
							</Tooltip.Trigger>
							<Tooltip.Content>Zoom out</Tooltip.Content>
						</Tooltip.Root>
						<!-- Current zoom indicator. -->
						<Tooltip.Root>
							<Tooltip.Trigger>
								<span
									class="bg-neutral-1 text-neutral-11 border-neutral-6 flex h-6 w-auto items-center justify-center border-t border-b px-1 py-0.5 text-sm"
								>
									{Math.trunc(canvas.transform.scaleFactor.x * 100)}
									%
								</span>
							</Tooltip.Trigger>
							<Tooltip.Content>Current zoom percentage</Tooltip.Content>
						</Tooltip.Root>
						<!-- Zoom in. -->
						<Tooltip.Root>
							<Tooltip.Trigger>
								<Button
									onclick={() => {
										canvas.transform.addScale(0.1);
									}}
									variant="outline"
									size="xsm"
									class="hover:bg-secondary-5 bg-neutral-1 hover:text-secondary-12 border-l-neutral-4 pointer-events-auto flex items-center justify-center rounded-l-none"
								>
									<Icon
										icon={'material-symbols:zoom-in'}
										width="3rem"
										class="text-neutral-11"
									/>
								</Button>
							</Tooltip.Trigger>
							<Tooltip.Content>Zoom in</Tooltip.Content>
						</Tooltip.Root>
					</div>

					<!-- Pan controls. -->
					<div
						class="grid gap-1 {buttonsDirection === 'horizontal'
							? 'grid-cols-3 grid-rows-2'
							: 'grid-cols-2 grid-rows-3'}"
					>
						<!-- Left arrow. -->
						<div
							class={buttonsDirection === 'horizontal'
								? 'order-1 row-span-2 self-center'
								: 'order-2'}
						>
							<Tooltip.Root>
								<Tooltip.Trigger>
									<Button
										onclick={() => {
											canvas.transform.translate({ x: 120, y: 0 });
										}}
										variant="outline"
										size="xsm"
										class="hover:bg-secondary-5 bg-neutral-1 hover:text-secondary-12 pointer-events-auto flex items-center justify-center"
									>
										<Icon
											icon={'material-symbols:arrow-back-2'}
											width="3rem"
											class="text-neutral-11"
										/>
									</Button>
								</Tooltip.Trigger>
								<Tooltip.Content>Move Left</Tooltip.Content>
							</Tooltip.Root>
						</div>

						<!-- Up arrow. -->
						<div
							class={buttonsDirection === 'horizontal'
								? 'order-2'
								: 'order-1 col-span-2 justify-self-center'}
						>
							<Tooltip.Root>
								<Tooltip.Trigger>
									<Button
										onclick={() => {
											canvas.transform.translate({ x: 0, y: 120 });
										}}
										variant="outline"
										size="xsm"
										class="hover:bg-secondary-5 bg-neutral-1 hover:text-secondary-12 pointer-events-auto flex items-center justify-center"
									>
										<Icon
											icon={'material-symbols:arrow-back-2'}
											width="3rem"
											class="text-neutral-11 rotate-90"
										/>
									</Button>
								</Tooltip.Trigger>
								<Tooltip.Content>Move up</Tooltip.Content>
							</Tooltip.Root>
						</div>

						<!-- Right arrow. -->
						<div
							class={buttonsDirection === 'horizontal'
								? 'order-3 row-span-2 self-center'
								: 'order-3'}
						>
							<Tooltip.Root>
								<Tooltip.Trigger>
									<Button
										onclick={() => {
											canvas.transform.translate({ x: -120, y: 0 });
										}}
										variant="outline"
										size="xsm"
										class="hover:bg-secondary-5 bg-neutral-1 hover:text-secondary-12 pointer-events-auto flex items-center justify-center"
									>
										<Icon
											icon={'material-symbols:arrow-back-2'}
											width="3rem"
											class="text-neutral-11 rotate-180"
										/>
									</Button>
								</Tooltip.Trigger>
								<Tooltip.Content>Move right</Tooltip.Content>
							</Tooltip.Root>
						</div>

						<!-- Down arrow. -->
						<div
							class={buttonsDirection === 'horizontal'
								? 'order-4'
								: 'order-4 col-span-2 justify-self-center'}
						>
							<Tooltip.Root>
								<Tooltip.Trigger>
									<Button
										onclick={() => {
											canvas.transform.translate({ x: 0, y: -120 });
										}}
										variant="outline"
										size="xsm"
										class="hover:bg-secondary-5 bg-neutral-1 hover:text-secondary-12 pointer-events-auto flex items-center justify-center"
									>
										<Icon
											icon={'material-symbols:arrow-back-2'}
											width="3rem"
											class="text-neutral-11 -rotate-90"
										/>
									</Button>
								</Tooltip.Trigger>
								<Tooltip.Content>Move down</Tooltip.Content>
							</Tooltip.Root>
						</div>
					</div>

					<!-- Home button. -->
					<div>
						<Tooltip.Root>
							<Tooltip.Trigger>
								<Button
									onclick={canvas.transform.reset}
									variant="outline"
									size="xsm"
									class="hover:bg-secondary-5 bg-neutral-1 hover:text-secondary-12 pointer-events-auto flex items-center justify-center"
								>
									<Icon
										icon={'material-symbols:home'}
										width="3rem"
										class="text-neutral-11"
									/>
								</Button>
							</Tooltip.Trigger>
							<Tooltip.Content>Reset layout position</Tooltip.Content>
						</Tooltip.Root>
					</div>

					<!-- Snap to grid button. -->
					<div>
						<Tooltip.Root>
							<Tooltip.Trigger>
								<Button
									onclick={() => {
										canvas.gridManager.config.snapToGrid =
											!canvas.gridManager.config.snapToGrid;
									}}
									variant="outline"
									size="xsm"
									class="{canvas.gridManager.config.snapToGrid
										? 'bg-secondary-5 border-secondary-6 hover:bg-neutral-3 hover:border-neutral-8'
										: 'bg-neutral-1 hover:bg-secondary-5'} hover:text-secondary-12 pointer-events-auto flex rotate-180 items-center justify-center transition-colors"
								>
									<Icon
										icon={'iconoir:magnet-solid'}
										width="3rem"
										class="text-neutral-11"
									/>
								</Button>
							</Tooltip.Trigger>
							<Tooltip.Content>Toggle snap to grid</Tooltip.Content>
						</Tooltip.Root>
					</div>

					<!-- Toggle vertical and horizontal line constraint. -->
					<div>
						<Tooltip.Root>
							<Tooltip.Trigger>
								<Button
									onclick={() => {
										canvas.gridManager.config.rightAngleConstraint =
											!canvas.gridManager.config.rightAngleConstraint;
									}}
									variant="outline"
									size="xsm"
									class="{canvas.gridManager.config.rightAngleConstraint
										? 'bg-secondary-5 border-secondary-6 hover:bg-neutral-3 hover:border-neutral-8'
										: 'bg-neutral-1 hover:bg-secondary-5'} hover:text-secondary-12 pointer-events-auto flex items-center justify-center transition-colors"
								>
									<Icon icon={'mdi:parallel'} width="3rem" class="text-neutral-11" />
								</Button>
							</Tooltip.Trigger>
							<Tooltip.Content>Toggle right angle constraint</Tooltip.Content>
						</Tooltip.Root>
					</div>
				</div>
			</Collapsible.Content>
		</Collapsible.Root>
	</Tooltip.Root>
</div>
