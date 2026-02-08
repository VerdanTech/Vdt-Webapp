<script lang="ts">
	import { PlantObservationLabels, type GenericObservation } from "@vdg-webapp/models";

    import ObservationGenericInfopoint from "./ObservationGenericInfopoint.svelte";

	type Props = {
		observation: PlantObservation
	};
	let { observation }: Props = $props();

    const label = PlantObservationLabels[observation.type] ?? 'Unknown Observation'
</script>

{#snippet content(observation: PlantObservation)}
Plant!!
{/snippet}

<ObservationGenericInfopoint {observation} {label} {content} />