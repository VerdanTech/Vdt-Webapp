<script lang="ts">
	import { Calendar as CalendarPrimitive } from 'bits-ui';
	import { buttonVariants } from '$lib/components/ui/button/index.js';
	import { cn } from '$lib/utils/shadcn.js';

	type $$Props = CalendarPrimitive.DayProps;
	type $$Events = CalendarPrimitive.DayEvents;

	export let date: $$Props['date'];
	export let month: $$Props['month'];
	let className: $$Props['class'] = undefined;
	export { className as class };
</script>

<CalendarPrimitive.Day
	on:click
	{date}
	{month}
	class={cn(
		buttonVariants({ variant: 'ghost' }),
		'h-9 w-9 p-0 font-normal',
		// Current day
		'[&[data-today]:not([data-selected])]:outline [&[data-today]:not([data-selected])]:outline-1',
		// Selected
		'data-[selected]:bg-primary-5 data-[selected]:text-primary-12 data-[selected]:opacity-100 data-[selected]:hover:bg-primary-5 data-[selected]:hover:text-primary-12 data-[selected]:focus:bg-primary-5 data-[selected]:focus:text-primary-12',
		// Disabled
		'data-[disabled]:text-neutral-11 data-[disabled]:opacity-50',
		// Unavailable
		'data-[unavailable]:text-destructive-12 data-[unavailable]:line-through',
		// Outside months
		'[&[data-outside-month][data-selected]]:bg-accent-5/50 data-[outside-month]:pointer-events-none data-[outside-month]:text-neutral-11 data-[outside-month]:opacity-50 [&[data-outside-month][data-selected]]:text-neutral-11 [&[data-outside-month][data-selected]]:opacity-30',
		className
	)}
	{...$$restProps}
	let:selected
	let:disabled
	let:unavailable
	let:builder
>
	<slot {selected} {disabled} {unavailable} {builder}>
		{date.day}
	</slot>
</CalendarPrimitive.Day>
