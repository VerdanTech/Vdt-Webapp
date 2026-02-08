<script lang="ts">
import { type GenericObservation, observationUpdate } from "@vdg-webapp/models";
	import type { Snippet } from "svelte";
	import DatePicker from '$core/datepicker';
	import { getLocalTimeZone, fromDate } from "@internationalized/date";
	import createCommandHandler from "$state/commandHandler.svelte";
	import { getAppContext } from "$state";
	import { toDate } from "@melt-ui/svelte/internal/helpers/date";


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
</script>

<div class="flex flex-col p-1 gap-2">
	<!-- Label -->
	<div class="flex justify-between">
		<span>
			{label}
		</span>
		<span class="italic text-neutral-8 text-sm">Observation</span>
	</div>

	<!-- Separator -->
	<div class="w-full h-[1px] bg-neutral-7 rounded-sm"></div>

	<!-- Content -->
	{@render content(observation)}
	
	<!-- Date -->
	<DatePicker
		value={calendarDate}
		compact={false}
		onValueChange={async (newVal) => {
			if (newVal) {
				observationUpdateHandler.execute({date: toDate(newVal, getLocalTimeZone())}, ctx.controller)
			}
		}}
		disabled={canEdit}
	/>
	 
	<!-- Date translate buttons -->
</div>

