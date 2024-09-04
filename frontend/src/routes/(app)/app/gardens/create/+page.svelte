<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Button } from '$components/ui/button';
	import GardenCreateForm from './GardenCreateForm.svelte';
</script>

<svelte:head>
	<title>Create Garden - VerdanTech</title>
</svelte:head>

<Card.Root
	class="4xl:w-1/3 m-auto mt-0 h-full w-full border-0 md:mt-12 md:h-auto md:w-3/4 md:border lg:w-1/2"
>
	<Card.Header>
		<Card.Title>Create a Garden</Card.Title>
	</Card.Header>
	<Card.Content>
		<GardenCreateForm />
	</Card.Content>
</Card.Root>
