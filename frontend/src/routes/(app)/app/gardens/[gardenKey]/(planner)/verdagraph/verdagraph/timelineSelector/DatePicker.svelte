<script lang="ts">
	import {
		type DateValue,
		DateFormatter,
		getLocalTimeZone
	} from '@internationalized/date';
	import { cn } from '$lib/utils/shadcn.js';
	import { Calendar } from '$lib/components/ui/calendar';
	import * as Popover from '$lib/components/ui/popover/index.js';
	import { Button } from 'bits-ui';

	const df = new DateFormatter('en-US', {
		day: '2-digit',
		month: 'short',
		year: '2-digit'
	});

	type Props = {
		value: DateValue;
		minValue?: DateValue | undefined;
		maxValue?: DateValue | undefined;
		onValueChange?: (date: DateValue | undefined) => void;
	};
	let { value = $bindable(), minValue, maxValue, onValueChange }: Props = $props();
</script>

<Popover.Root openFocus>
	<Popover.Trigger asChild let:builder>
		<Button.Root
			class={cn('justify-start text-left font-normal', !value && 'text-neutral-11')}
			builders={[builder]}
		>
			{value ? df.format(value.toDate(getLocalTimeZone())) : 'Select a date'}
		</Button.Root>
	</Popover.Trigger>
	<Popover.Content class="w-auto p-0">
		<Calendar
			bind:value
			preventDeselect={true}
			initialFocus
			{onValueChange}
			{minValue}
			{maxValue}
		/>
	</Popover.Content>
</Popover.Root>
