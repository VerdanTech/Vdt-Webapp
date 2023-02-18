<script>
	import LoginForm from './LoginForm.svelte';
</script>

<svelte:head>
	<title>Login | Verdantech</title>
</svelte:head>

<div class="card p-8 w-3/4 md:w-1/2 2xl:w-1/4 mx-auto mt-16 2xl:mt-24 rounded-container-token">
	<h2 class="p-4">
		Log in or <span><a href="./register" class="!no-underline">create an account</a></span>
	</h2>
	<hr />
	<LoginForm />
</div>
