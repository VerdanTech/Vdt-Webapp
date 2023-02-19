<script>
	function validate() {
		console.log("I'm the validate() function");
	}
</script>

<form on:submit|preventDefault={validate}>
	<ul>
		<li class="p-4">
			<label class="label">
				<span>Email</span>
				<input class="input" type="email" required />
			</label>
		</li>
		<li class="p-4">
			<label class="label">
				<span>Username</span>
				<input class="input" type="text" required />
			</label>
		</li>
		<li class="p-4">
			<label class="label">
				<span>Password</span>
				<input class="input" type="password" required />
			</label>
		</li>
		<li class="p-4">
			<label class="flex items-center space-x-2">
				<input class="checkbox" type="checkbox" />
				<span>I agree to the <a href="#" class="!no-underline">Terms of Use</a></span>
			</label>
		</li>
		<li class="p-4 mt-4">
			<button class="btn variant-filled-primary w-full">Register</button>
		</li>
	</ul>
</form>
