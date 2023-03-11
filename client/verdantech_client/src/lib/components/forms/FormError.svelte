<script>
	import ErrorCircleRoundedOutline from 'virtual:icons/material-symbols/error-circle-rounded-outline';
	export let text = '';
</script>

<div class="bg-error-700 rounded-token border-error-500 flex items-center">
	<span class="p-1">
		<ErrorCircleRoundedOutline style="font-size: 2em" />
	</span>
	<span class="ml-2">
		{text}
	</span>
</div>
