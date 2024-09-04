<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Button } from '$components/ui/button';
	import LoginForm from './LoginForm.svelte';
</script>

<svelte:head>
	<title>Login - VerdanTech</title>
</svelte:head>

<Card.Root class="m-auto mt-12 w-3/4 md:w-1/2 lg:w-1/3">
	<Card.Header>
		<Card.Title>Login</Card.Title>
		<Card.Description>
			<Button
				variant="link"
				class="p-0 text-neutral-11"
				href="/login/request-password-reset">Forgot your password?</Button
			>
		</Card.Description>
	</Card.Header>
	<Card.Content>
		<LoginForm />
	</Card.Content>
</Card.Root>
