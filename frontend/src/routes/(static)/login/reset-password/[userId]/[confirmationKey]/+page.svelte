<script lang="ts">
	import { page } from '$app/stores';
	import * as Card from '$lib/components/ui/card';
	import { Button } from '$components/ui/button';
	import * as Dialog from '$components/ui/dialog';
	import PasswordResetForm from './PasswordResetForm.svelte';

	/** Set to true on form success. */
	let succeeded = $state<boolean>(false);
</script>

<svelte:head>
	<title>Reset Password - VerdanTech</title>
</svelte:head>

<Card.Root class="m-auto mt-12 w-3/4 md:w-1/2 lg:w-1/3">
	<Card.Header>
		<Card.Title>Choose a new password</Card.Title>
	</Card.Header>
	<Card.Content>
		<PasswordResetForm bind:succeeded />
	</Card.Content>

	<Dialog.Root open={succeeded} closeOnEscape={false} closeOnOutsideClick={false}>
		<Dialog.Content>
			<Dialog.Header>
				<Dialog.Title>Password has been successfully reset</Dialog.Title>
				<Dialog.Description>
					<Button variant="link" class="p-0 text-neutral-11" href="/login"
						>Proceed to Login</Button
					>
				</Dialog.Description>
			</Dialog.Header>
		</Dialog.Content>
	</Dialog.Root>
</Card.Root>
