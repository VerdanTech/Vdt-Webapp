<script lang="ts">
	type Props = {
		value: unknown;
	};
	let { value }: Props = $props();
</script>

<!-- The default display for a value when it is not being edited. -->
<span
	class="{!value
		? 'italic'
		: ''} border-neutral-7 bg-neutral-1 ring-offset-neutral-1 focus-visible:ring-neutral-7 flex w-full rounded-md border px-3 py-2 text-sm focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:outline-none"
>
	{value || 'None'}
</span>
