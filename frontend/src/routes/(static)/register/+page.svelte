<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Button } from '$components/ui/button';
	import * as Dialog from '$components/ui/dialog';
	import RegistrationForm from './RegistrationForm.svelte';
	/** Set to true on form success. */
	let succeeded = $state<boolean>(false);

	/** Stores the email the form sent to. */
	let registeredEmail = $state<string>('');
</script>

<svelte:head>
	<title>Register - VerdanTech</title>
</svelte:head>

<Card.Root class="m-auto mt-12 w-3/4 md:w-1/2 lg:w-1/3">
	<Card.Header>
		<Card.Title>Create an account</Card.Title>
		<Card.Description>
			<Button variant="link" class="p-0 text-neutral-11" href="/login"
				>Already have one?</Button
			>
		</Card.Description>
	</Card.Header>
	<Card.Content>
		<RegistrationForm bind:succeeded bind:registeredEmail />
	</Card.Content>

	<Dialog.Root open={succeeded} closeOnEscape={false} closeOnOutsideClick={false}>
		<Dialog.Content>
			<Dialog.Header>
				<Dialog.Title
					>An email confirmation has been sent to {registeredEmail}</Dialog.Title
				>
				<Dialog.Description>
					If you don't receive it, <Button
						variant="link"
						class="p-0 text-neutral-11"
						href="/register/request-email-verification"
						>request another through this link.</Button
					>
				</Dialog.Description>
			</Dialog.Header>
		</Dialog.Content>
	</Dialog.Root>
</Card.Root>
