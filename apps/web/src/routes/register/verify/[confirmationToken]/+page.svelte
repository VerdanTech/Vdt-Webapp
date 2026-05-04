<script lang="ts">
	import Icon from '@iconify/svelte';

	import { type UserConfirmEmailConfirmationCommand } from '@vdg-webapp/models';
	import { Card, iconIds } from '@vdg-webapp/ui';

	import { goto } from '$app/navigation';
	import { page } from '$app/state';
	import { userConfirmEmailConfirmation } from '$data/users/commands';
	import createCommandHandler from '$state/commandHandler.svelte';

	/* Initialize the mutation on page load with url parameter. */
	const confirmationToken = page.params.confirmationToken;

	let formHandler = createCommandHandler(userConfirmEmailConfirmation.mutation, {
		onSuccess: () => {
			goto('/login');
		}
	});
	formHandler.execute({
		token: confirmationToken
	} satisfies UserConfirmEmailConfirmationCommand);
</script>

<svelte:head>
	<title>Email Confirmed - Verdagraph</title>
</svelte:head>

<Card.Root class="m-auto mt-12 w-3/4 md:w-1/2 lg:w-1/3">
	{#if formHandler.isLoading}
		<Card.Header>
			<Card.Title
				>Confirming your email <Icon
					icon={iconIds.defaultSpinnerIcon}
					width="1.5rem"
					class="inline animate-spin"
				/></Card.Title
			>
		</Card.Header>
	{:else if formHandler.isError}
		<Card.Header>
			<Card.Title>Something went wrong...</Card.Title>
			<Card.Content class="text-md text-warning-11 w-full px-0 pt-4 pb-0 font-medium">
				<ul>
					{#each formHandler.fieldErrors?.token ?? [] as error}
						<li
							class="border-warning-7 bg-warning-3 border-x p-1 first:rounded-t-md first:border-t last:rounded-b-md last:border-b"
						>
							{error}
						</li>
					{/each}
				</ul>
			</Card.Content>
		</Card.Header>
	{:else if formHandler.isSuccess}
		<Card.Header>
			<Card.Title>Confirmed!</Card.Title>
			<Card.Description>Redirecting to the login page.</Card.Description>
		</Card.Header>
	{/if}
</Card.Root>
