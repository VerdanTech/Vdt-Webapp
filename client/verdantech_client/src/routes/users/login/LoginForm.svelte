<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

	onMount(() => {
		fetch('http://localhost:5173/api/accounts/csrf/', {
			method: 'GET',
            credentials: 'include',
		});
	});

    function getCookie(name: string) {
    // Split cookie string and get all individual name=value pairs in an array
    var cookieArr = document.cookie.split(";");

    // Loop through the array elements
    for(var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=");

        /* Removing whitespace at the beginning of the cookie name
        and compare it with the given string */
        if(name == cookiePair[0].trim()) {
            // Decode the cookie value and return
            return decodeURIComponent(cookiePair[1]);
        }
    }

    // Return null if not found
    return null;
}

	async function handleSubmit(event: SubmitEvent) {
		const formData = new FormData(event.target as HTMLFormElement);

		const data: { [key: string]: any } = {};
		for (const [key, value] of formData.entries()) {
			data[key] = value;
		}

        fetch('http://localhost:5173/api/accounts/csrf/', {
			method: 'GET',
            credentials: 'include',
		});

		await fetch('http://localhost:5173/api/accounts/login/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
                //"X-CSRF-Token": getCookie("csrftoken")
			},
			body: JSON.stringify(data),
            credentials: 'same-origin',
		}).then((response) => {
			if (response.ok) {
                console.log("atok response")
                //goto('/app/dashboard')
			} else {
                console.log("non- ok response")
                console.log(document.cookie)
                console.log(getCookie("csrftoken"))
            }
		});
	}
</script>

<form on:submit|preventDefault={handleSubmit}>
	<ul>
		<li class="p-4">
			<label class="label">
				<span>Email</span>
				<input class="input" type="email" required />
			</label>
		</li>
		<li class="p-4">
			<label class="label">
				<span>Password</span>
				<input class="input" type="password" required />
			</label>
		</li>
		<li class="p-4 mt-4">
			<button class="btn variant-filled-primary w-full">Login</button>
		</li>
	</ul>
</form>
