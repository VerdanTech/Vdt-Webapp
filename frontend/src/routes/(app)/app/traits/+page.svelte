<script lang="ts">
	import * as Card from '$components/ui/card';
	import Separator from '$components/ui/separator/separator.svelte';
</script>

<svelte:head>
	<title>Traits - VerdanTech</title>
</svelte:head>

<div class="m-auto mt-12 flex w-3/4 flex-col items-center">
	<h1 class="text-4xl">Traits</h1>
	<p>
		VerdanTech's flexible system for specifying model behavior and sharing data amongst
		gardens and users.
	</p>
</div>

<Card.Root class="m-auto mt-12 w-3/4 md:w-1/2 lg:w-1/3">
	<Card.Header class="m-auto flex flex-col items-center">
		<Card.Title>Cultivars</Card.Title>
		<Card.Description>Describes the behavior of plant species.</Card.Description>
		<Separator class="bg-neutral-7" />
	</Card.Header>
	<Card.Content>
		<div>Public Data - discover button</div>
		<div>Your Data</div>
		<Separator class="bg-neutral-7" />
	</Card.Content>
</Card.Root>
