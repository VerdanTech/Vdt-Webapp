<script lang="ts">
	import { Button, DropdownMenu, Popover } from '@vdg-webapp/ui';

	import { goto } from '$app/navigation';
	import { page } from '$app/state';
	import { demos } from '$demos';

	const selectedDemo = $derived(demos.find((demo) => demo.id === page.params.demoId));
</script>

<!--
@component Navigation to switch between demos.
Currently unused.
-->

<div
	class="border-neutral-8 bg-neutral-3 flex items-center justify-start gap-4 border-b px-8 py-2"
>
	<span class="text-neutral-11 px-2"> Verdagraph Demos </span>
	<DropdownMenu.Root>
		<DropdownMenu.Trigger
			>s
			{#snippet child({ props })}
				<Button.Root {...props} variant="ghost">Select</Button.Root>
			{/snippet}
		</DropdownMenu.Trigger>
		<DropdownMenu.Content>
			<DropdownMenu.RadioGroup
				value={selectedDemo ? selectedDemo.id : ''}
				onValueChange={(value) => goto('/demos/' + value)}
			>
				{#each demos as demo}
					<DropdownMenu.RadioItem value={demo.id}>
						{demo.title}
					</DropdownMenu.RadioItem>
				{/each}
			</DropdownMenu.RadioGroup>
		</DropdownMenu.Content>
	</DropdownMenu.Root>
	<Popover.Root>
		<Popover.Trigger>
			{#snippet child({ props })}
				<Button.Root {...props} variant="ghost">Description</Button.Root>
			{/snippet}
		</Popover.Trigger>
		<Popover.Content>
			<span class="text-neutral-11 text-italic text-sm">
				{selectedDemo ? selectedDemo.description : 'Demo not found...'}
			</span>
		</Popover.Content>
	</Popover.Root>
</div>
