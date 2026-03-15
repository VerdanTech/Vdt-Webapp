<script lang="ts">
import { type GenericObservation, observationUpdate } from "@vdg-webapp/models";
	import type { Snippet } from "svelte";
	import DatePicker from '$core/datepicker';
	import { getLocalTimeZone, fromDate, type DateDuration } from "@internationalized/date";
	import createCommandHandler from "$state/commandHandler.svelte";
	import type { ButtonVariant } from '$core/button';
	import { getAppContext } from "$state";
	import { toDate } from "@melt-ui/svelte/internal/helpers/date";
	import * as Tooltip from '$core/tooltip';
	import iconIds from '$assets/icons';
	import { Button } from '$core/button';
	import Icon from '@iconify/svelte';


	type Props = {
		observation: GenericObservation,
		label: string,
        content: Snippet<[observation: GenericObservation]>
	};
	let { observation, label, content }: Props = $props();

	/** Handlers. */
	const ctx = getAppContext();
	const observationUpdateHandler = createCommandHandler(observationUpdate)

	const canEdit = false;

	const calendarDate = $derived(fromDate(observation.date, getLocalTimeZone()))

	function translateDate(duration: DateDuration) {
		const newVal = calendarDate.add(duration)
		observationUpdateHandler.execute({id: observation.id, date: toDate(newVal, getLocalTimeZone())}, ctx.controller)
	}
</script>

<!-- Date translate buttons. -->
{#snippet button(
	tooltipDescription: string,
	iconId: string,
	variant: ButtonVariant,
	onclick: () => void
)}
	<Tooltip.Root>
		<Tooltip.Trigger class="w-full px-2">
			<Button
				{variant}
				size="xsm"
				class="mx-1 flex h-fit w-full items-center rounded-2xl p-0 outline outline-1"
				disabled={false}
				{onclick}
			>
				<Icon icon={iconId} width="1rem" class="m-1" />
			</Button>
		</Tooltip.Trigger>
		<Tooltip.Content>
			{tooltipDescription}
		</Tooltip.Content>
	</Tooltip.Root>
{/snippet}

<div class="flex flex-col p-1">
	<!-- Label -->
	<div class="flex justify-between">
		<span class="font-semibold">
			{label}
		</span>
		<span class="italic text-neutral-8 text-sm">Observation</span>
	</div>

	<!-- Separator -->
	<div class="w-full h-[1px] bg-neutral-7 rounded-sm mt-1 mb-2"></div>

	<!-- Content -->
	<div class="pt-1 pb-2">
		{@render content(observation)}
	</div>
	
	<!-- Date -->
	<DatePicker
		value={calendarDate}
		compact={false}
		onValueChange={async (newVal) => {
			if (newVal) {
				observationUpdateHandler.execute({id: observation.id, date: toDate(newVal, getLocalTimeZone())}, ctx.controller)
			}
		}}
		disabled={canEdit}
	/>
	 
	<!-- Date translate buttons -->
	<div class="w-full flex justify-around pt-3 pb-2 my-2">
		<div class="flex justify-around w-full">
			{@render button(
				'Move observation to the past by 1 week',
				iconIds.verdagraphWeekReverseIcon,
				'default',
				() =>
				translateDate({weeks: -1})
			)}
			{@render button(
				'Move observation to the past by 1 day',
				iconIds.verdagraphDayReverseIcon,
				'default',
				() =>
				translateDate({days: -1})
			)}
		</div>
		<div class="flex justify-around w-full">
			{@render button(
				'Move observation to the future by 1 day',
				iconIds.verdagraphDayForwardIcon,
				'default',
				() =>
				translateDate({days: 1})
			)}
			{@render button(
				'Move observation to the future by 1 week',
				iconIds.verdagraphWeekForwardIcon,
				'default',
				() =>
				translateDate({weeks: 1})
			)}
		</div>
	</div>
</div>

