<script lang="ts">
	let { children } = $props();
</script>

<div class="flex h-screen w-screen flex-col overflow-clip">
	{@render children()}
</div>
