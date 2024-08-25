<script lang="ts">
	import TreeScrollable from './TreeScrollable.svelte';
	import { Toolbar } from 'bits-ui';
	import { icons } from '$lib/icons';
</script>

<TreeScrollable>
	<Toolbar.Root class="flex items-center justify-center bg-neutral-2 p-1">
		<ul class="flex h-full items-center justify-center">
			<li class="flex items-center">
				<i>
					<svelte:component this={icons.windows} class="text-md text-neutral-11" />
				</i>
			</li>
			<li>
				<span class="ml-2 mr-4 text-sm text-neutral-11"> Planting Windows </span>
			</li>
		</ul>
	</Toolbar.Root>
</TreeScrollable>
