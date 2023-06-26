<script>
	import { AppBar } from '@skeletonlabs/skeleton';
	import Logo from '$lib/components/graphics/logo.svelte';
	import IconMenuRounded from 'virtual:icons/ic/round-menu';

	let navLinks = [
		{ url: '/guides', label: 'Guides' },
		{ url: 'https://github.com/nathanielarking/VerdanTech', label: 'Github' },
		{ url: '/project', label: 'Project' },
		{ url: '/donate', label: 'Donate' }
	];
</script>

<AppBar
	gridColumns="grid grid-cols-3"
	padding="p-0"
	shadow="shadow-lg"
	spacing="!space-y-0"
	slotLead="justify-self-start xl:justify-self-center order-1"
	slotDefault="justify-self-end self-stretch order-3 md:order-2 md:justify-self-center"
	slotTrail="justify-self-center md:justify-self-end xl:justify-self-center order-2 md:order-3"
	regionRowHeadline=""
>
	<svelte:fragment slot="lead">
		<!--Logo and brand name-->
		<nav class="font-semibold text-md lg:text-lg p-4">
			<ul class="flex items-center">
				<li class="mr-6">
					<a href="/">
						<Logo size="4rem" />
					</a>
				</li>
				<li>
					<a href="/" class="hidden sm:block">
						<span>VerdanTech</span>
					</a>
				</li>
			</ul>
		</nav>
	</svelte:fragment>
	<svelte:fragment slot="default">
		<!--Horizontal navigation menu-->
		<div class="h-full flex md:hidden mr-4">
			<label for="menu-toggle" class="self-center cursor-pointer"
				><IconMenuRounded style="font-size: 3em" /></label
			>
		</div>
		<nav class="h-full font-semibold text-md lg:text-lg hidden md:block">
			<ul class="h-full flex">
				{#each navLinks as link}
					<li class="p-2 lg:p-4 hover:bg-primary-700 hover:text-on-primary-token transition">
						<a href={link.url} class="h-full flex">
							<span class="self-center p-4"> {link.label} </span>
						</a>
					</li>
				{/each}
			</ul>
		</nav>
	</svelte:fragment>
	<svelte:fragment slot="trail">
		<!--Login and register links-->
		<nav class="h-full font-semibold mr-4 text-md lg:text-lg">
			<ul class="h-full flex items-center">
				<li>
					<a href="/login" class="btn">Log in</a>
				</li>
				<li>
					<a href="/register" class="btn variant-filled-primary">Get started</a>
				</li>
			</ul>
		</nav>
	</svelte:fragment>
</AppBar>
<!--Mobile vertical navigation menu-->
<div>
	<input type="checkbox" id="menu-toggle" name="menu-toggle" class="peer hidden" />
	<nav class="hidden peer-checked:block md:peer-checked:hidden bg-surface-700 text-xl">
		<ul>
			{#each navLinks as link}
				<li
					class="flex bg-surface-100-800-token odd:bg-surface-300-600-token hover:bg-surface-200-700-token odd:hover:bg-surface-400-500-token"
				>
					<a
						href={link.url}
						class="w-full flex justify-center !no-underline !text-surface-900-50-token"
					>
						<span class="p-4">{link.label}</span>
					</a>
				</li>
			{/each}
		</ul>
	</nav>
</div>
