<script lang="ts">
	import { today, getLocalTimeZone } from '@internationalized/date'
	import Icon from '@iconify/svelte'
	import type { DateValue, DateDuration } from '@internationalized/date'
	import DatePicker from './DatePicker.svelte'
	import { Button } from '$lib/components/ui/button'
	import * as Tooltip from '$lib/components/ui/tooltip'

	import iconIds from '$lib/assets/icons'

	import {
		timelineSelection,
		minSelectOffset,
		maxSelectOffset
	} from '../state/timelineSelection.svelte'
</script>

<!-- Timeline selection translation buttons. -->
{#snippet button(tooltipDescription: string, iconId: string, onclick: () => void)}
<Tooltip.Root group="timelineSelector">
    <Tooltip.Trigger> 
        <Button
            variant="secondary"
            class="p-0 rounded-2xl h-fit flex items-center mx-1 outline outline-1"
            on:click={onclick}
            >
                <Icon icon={iconId} width="1.5rem" class="m-1"/>
            </Button>
    </Tooltip.Trigger>
    <Tooltip.Content>
        {tooltipDescription}
    </Tooltip.Content>
  </Tooltip.Root>
{/snippet}

<div class="flex flex-row items-center justify-between px-4 py-2">
	<div class="">
		<Tooltip.Root group="timelineSelector">
			<Tooltip.Trigger>
				<DatePicker
					bind:value={timelineSelection.value.beginSelectedDays}
					minValue={timelineSelection.value.focusedDay.subtract(maxSelectOffset)}
					maxValue={timelineSelection.value.focusedDay.subtract(minSelectOffset)}
				/>
			</Tooltip.Trigger>
			<Tooltip.Content>Beginning date of timeline selection</Tooltip.Content>
		</Tooltip.Root>
	</div>
	<div class="flex flex-row items-center justify-center px-8">
		{@render button(
			'Rewind selection one month',
			iconIds.verdagraphMonthReverseIcon,
			() => timelineSelection.pushSelectionBackward({ months: 1 })
		)}
		{@render button(
			'Rewind selection one week',
			iconIds.verdagraphWeekReverseIcon,
			() => timelineSelection.pushSelectionBackward({ weeks: 1 })
		)}
		{@render button('Rewind selection one day', iconIds.verdagraphDayReverseIcon, () =>
			timelineSelection.pushSelectionBackward({ days: 1 })
		)}
		<div class="mx-4">
			<Tooltip.Root group="timelineSelector">
				<Tooltip.Trigger>
					<DatePicker
						bind:value={timelineSelection.value.focusedDay}
						onValueChange={(newDate: DateValue | undefined) => {
							if (newDate != undefined) {
								timelineSelection.focusedDayOnValueChange(newDate)
							}
						}}
					/>
				</Tooltip.Trigger>
				<Tooltip.Content>Focused date</Tooltip.Content>
			</Tooltip.Root>
		</div>
		{@render button('Forward selection one day', iconIds.verdagraphDayForwardIcon, () =>
			timelineSelection.pushSelectionForward({ days: 1 })
		)}
		{@render button(
			'Forward selection one week',
			iconIds.verdagraphWeekForwardIcon,
			() => timelineSelection.pushSelectionForward({ weeks: 1 })
		)}
		{@render button(
			'Forward selection one month',
			iconIds.verdagraphMonthForwardIcon,
			() => timelineSelection.pushSelectionForward({ months: 1 })
		)}
	</div>
	<div>
		<Tooltip.Root group="timelineSelector">
			<Tooltip.Trigger>
				<DatePicker
					bind:value={timelineSelection.value.endSelectedDays}
					onValueChange={(newDate: DateValue | undefined) => {
						if (newDate != undefined) {
							timelineSelection.endSelectedDaysOnValueChange(newDate)
						}
					}}
					minValue={timelineSelection.value.focusedDay.add(minSelectOffset)}
					maxValue={timelineSelection.value.focusedDay.add(maxSelectOffset)}
				/>
			</Tooltip.Trigger>
			<Tooltip.Content>Ending date of timeline selection</Tooltip.Content>
		</Tooltip.Root>
	</div>
</div>
