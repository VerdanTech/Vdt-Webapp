<script lang="ts">
	import Icon from '@iconify/svelte';
	import { Button } from 'bits-ui';
	import * as Drawer from '$lib/components/ui/drawer';
	import iconIds from '$lib/assets/icons';
	import { Accordion } from 'bits-ui';
	import type { PrimaryTabSpec } from './primaryNavTabs';

	type Props = {
		specs: PrimaryTabSpec[] /* Describes the content of the tab. */;
	};
	let { specs }: Props = $props();

	let open = $state(false);
</script>

<!--
@component
Single tab for navigating between feature domains on the main bottom bar.
-->

<Drawer.Root direction="bottom" bind:open>
	<Drawer.Trigger class="flex h-full w-full justify-center bg-neutral-2">
		<Icon icon={iconIds.gardenDrawerIcon} width="3rem" class="my-2" />
	</Drawer.Trigger>
	<Drawer.Content class="flex items-center bg-neutral-3">
		<Accordion.Root class="w-full">
			{#each specs ?? [] as spec}
				{#if spec !== undefined}
					<Accordion.Item value={spec.label} class="mx-12 w-full">
						<Accordion.Trigger class="my-6 flex w-full items-center justify-start">
							<Icon icon={spec.iconId} width="1.5rem" class="mr-6" />
							<span>
								{spec.label}
							</span>
						</Accordion.Trigger>
						<Accordion.Content class="mx-4 border-l border-neutral-10">
							<ul class="px-4">
								{#if spec.submenuItems}
									{#each spec.submenuItems ?? [] as item}
										<li>
											<Button.Root
												href={item.url}
												class="my-4 flex items-center"
												on:click={() => {
													open = false;
												}}
											>
												{#if item.iconId}
													<Icon icon={item.iconId} width="1rem" class="mr-4" />
												{/if}
												<span>
													{item.label}
												</span>
											</Button.Root>
										</li>
									{/each}
								{/if}
							</ul>
						</Accordion.Content>
					</Accordion.Item>
				{/if}
			{/each}
		</Accordion.Root>
	</Drawer.Content>
</Drawer.Root>
