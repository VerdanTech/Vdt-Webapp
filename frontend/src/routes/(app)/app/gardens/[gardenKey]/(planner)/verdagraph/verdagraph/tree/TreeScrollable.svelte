<script lang="ts">
	import { ScrollArea } from 'bits-ui';
</script>

<ScrollArea.Root>
	<ScrollArea.Viewport>
		<ScrollArea.Content>
			<slot />
		</ScrollArea.Content>
	</ScrollArea.Viewport>
	<ScrollArea.Scrollbar orientation="vertical">
		<ScrollArea.Thumb />
	</ScrollArea.Scrollbar>
	<ScrollArea.Scrollbar orientation="horizontal">
		<ScrollArea.Thumb />
	</ScrollArea.Scrollbar>
	<ScrollArea.Corner />
</ScrollArea.Root>
