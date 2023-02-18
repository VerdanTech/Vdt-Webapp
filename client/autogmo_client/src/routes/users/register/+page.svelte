<script>
	import RegisterForm from './RegisterForm.svelte';
</script>

<svelte:head>
	<title>Register | Verdantech</title>
</svelte:head>

<div class="card p-8 w-3/4 md:w-1/2 2xl:w-1/4 mx-auto mt-16 2xl:mt-24 rounded-container-token">
	<h2 class="p-4">
		Create an account or <span><a href="./login" class="!no-underline">log in</a></span>
	</h2>
	<hr />
	<RegisterForm />
</div>
