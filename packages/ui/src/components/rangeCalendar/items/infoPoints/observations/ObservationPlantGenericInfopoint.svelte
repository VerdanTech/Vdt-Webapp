<script lang="ts">
	import {
		type GenericObservation,
		type PlantObservation,
		PlantObservationDescriptions,
		PlantObservationLabels
	} from '@vdg-webapp/models';

	import ObservationGenericInfopoint from './ObservationGenericInfopoint.svelte';

	type Props = {
		observation: PlantObservation;
	};
	let { observation }: Props = $props();

	const label = $derived(
		PlantObservationLabels[observation.type] ?? 'Unknown Observation'
	);
	const description = $derived(
		PlantObservationDescriptions[observation.type] ?? 'Unknown Observation'
	);
</script>

{#snippet content(observation: GenericObservation)}
	<span class="text-sm">{description}</span>
{/snippet}

<ObservationGenericInfopoint {observation} {label} {content} />
