<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Button } from '$components/ui/button';
	import * as Dialog from '$components/ui/dialog';
	import { externalLinks } from '$lib/assets/links';
	import RequestPasswordResetForm from './RequestPasswordResetForm.svelte';

	/** Set to true on form success. */
	let succeeded = $state<boolean>(false);
</script>

<svelte:head>
	<title>Request Password Reset - VerdanTech</title>
</svelte:head>

<Card.Root class="m-auto mt-12 w-3/4 md:w-1/2 lg:w-1/3">
	<Card.Header>
		<Card.Title>Request a password reset</Card.Title>
	</Card.Header>
	<Card.Content>
		<RequestPasswordResetForm bind:succeeded />
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
					>If the email exists, an email confirmation has been sent to it</Dialog.Title
				>
				<Dialog.Description>
					If the email remains unsent, try again or <Button
						variant="link"
						class="inline p-0 text-neutral-11"
						href={externalLinks.discord}>try reaching out to our community.</Button
					>
				</Dialog.Description>
			</Dialog.Header>
		</Dialog.Content>
	</Dialog.Root>
</Card.Root>
