<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Button } from '$components/ui/button';
	import * as Dialog from '$components/ui/dialog';
	import { externalLinks } from '$lib/assets/links';
	import RequestEmailConfirmationForm from './RequestEmailConfirmationForm.svelte';
	/** Set to true on form success. */
	let succeeded = $state<boolean>(false);

	/** Stores the email the form sent to. */
	let registeredEmail = $state<string>('');
</script>

<svelte:head>
	<title>Verify Email - VerdanTech</title>
</svelte:head>

<Card.Root class="m-auto mt-12 w-3/4 md:w-1/2 lg:w-1/3">
	<Card.Header>
		<Card.Title>Request an email confirmation</Card.Title>
	</Card.Header>
	<Card.Content>
		<RequestEmailConfirmationForm bind:succeeded bind:registeredEmail />
	</Card.Content>

	<Dialog.Root
		open={succeeded}
		closeOnEscape={true}
		closeOnOutsideClick={true}
		onOpenChange={(open) => {
			if (!open) {
				succeeded = false;
			}
		}}
	>
		<Dialog.Content>
			<Dialog.Header>
				<Dialog.Title
					>An email confirmation has been sent to {registeredEmail}</Dialog.Title
				>
				<Dialog.Description>
					If the email remains unsent, <Button
						variant="link"
						class="inline p-0 text-neutral-11"
						href={externalLinks.discord}>try reaching out to our community.</Button
					>
				</Dialog.Description>
			</Dialog.Header>
		</Dialog.Content>
	</Dialog.Root>
</Card.Root>
