<script lang="ts">
	import Icon from '@iconify/svelte';
	import { Button } from 'bits-ui';
	import { slide } from 'svelte/transition';
	import { Separator } from '$lib/components/ui/separator/index.js';
	import { Tooltip } from 'bits-ui';
	import type { PrimaryTabSpec } from './primaryNavTabs';

	type Props = {
		spec: PrimaryTabSpec /* Describes the content of the tab. */;
		flipped?: boolean /* If true, the tab is rendered bottom to top. */;
	};
	let { spec, flipped = false }: Props = $props();
</script>

<!--
@component
Single tab for navigating between feature domains on the main sideba	r.
-->
<Tooltip.Root group="primaryNavSidebarTabs" openDelay={0} closeDelay={0}>
	<!-- Large icon button which links to the feature domain and on hover, opens a submenu. -->
	<Tooltip.Trigger asChild let:builder>
		<a
			use:builder.action
			{...builder}
			href={spec.url}
			class="ring-offset-background inline-flex h-16
			w-full items-center justify-center whitespace-nowrap rounded-none bg-neutral-3
			transition-colors hover:bg-primary-4
			hover:text-primary-12 focus-visible:ring-2
			focus-visible:ring-primary-6 focus-visible:ring-offset-2"
		>
			<Icon icon={spec.iconId} width="3rem" />
		</a>
	</Tooltip.Trigger>

	<!-- Submenu content. Contains one header and variable items. -->
	<Tooltip.Content
		side={flipped ? 'top' : 'bottom'}
		transition={slide}
		transitionConfig={{
			delay: 20,
			duration: 400,
			axis: 'y'
		}}
		avoidCollisions={false}
		class="{flipped
			? 'translate-y-16'
			: '-translate-y-16'} shadow-xsm z-50 h-auto w-auto max-w-96 translate-x-14 overflow-hidden rounded-none rounded-r-md border-y border-r border-neutral-7 bg-neutral-3 p-0 outline-none"
	>
		<ul class:flex-col-reverse={flipped} class="flex flex-col items-center p-0">
			<!-- Header. -->
			<li class="flex w-full items-center bg-neutral-4">
				<Button.Root
					href={spec.url}
					class="flex w-full justify-center px-4 py-2 transition-colors hover:bg-primary-5"
					>{spec.label}</Button.Root
				>
			</li>

			<!-- Separator between header and items. -->
			{#if spec.submenuItems && spec.submenuItems.length > 0}
				<li class="w-full">
					<Separator class="m-0 bg-neutral-8 p-0 opacity-75" />
				</li>
			{/if}

			<!-- Submenu items. -->
			{#each spec.submenuItems ?? [] as item, index}
				<li class="w-full">
					<Button.Root
						href={item.url}
						class="flex w-full items-center px-4 py-3 transition-colors hover:bg-primary-6"
					>
						{#if item.iconId}
							<Icon icon={item.iconId} width="1.5rem" class="mr-3" />
						{/if}
						<span class="truncate">{item.label}</span></Button.Root
					>
				</li>
			{/each}
		</ul>
	</Tooltip.Content>
</Tooltip.Root>
