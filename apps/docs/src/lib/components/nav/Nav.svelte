<script lang="ts">
	import Icon from '@iconify/svelte';

	import { Button, DropdownMenu, Popover, Separator, iconIds } from '@vdg-webapp/ui';

	import env from '$lib/env';

	import MobileNav from './MobileNav.svelte';
	import Search from './Search.svelte';
	import ThemeSwitcher from './ThemeSwitcher.svelte';

	let navLinks = [
		{
			url: '/docs',
			label: 'Docs'
		},
		{ url: env.APP_URL, label: 'App' }
	];
</script>

<!--
@component Top header.
-->
<header
	class="border-neutral-6 sticky top-0 left-0 z-50 w-full border-b drop-shadow-md"
>
	<nav class="bg-neutral-2 flex items-center justify-between px-8 py-2">
		<!-- 
            Logo and Verdagraph text.
            Logo displayed always. Text displayed on larger screens.
        -->
		<div>
			<ul class="flex items-center gap-6 p-2 text-lg">
				<li>
					<a href="/" class="">
						<span class="font-bold">Verdagraph</span>
					</a>
				</li>
			</ul>
		</div>

		<!-- 
            Navigation links.
            Displayed within top horizontal menu on larger screens.
        -->
		<div class="flex items-center gap-8">
			<div class="w-max-[300px] w-1/2">
				<Search />
			</div>

			<ul class="hidden gap-4 md:flex md:gap-8 lg:gap-12">
				{#each navLinks as link}
					<li>
						<Button.Root href={link.url} variant="ghost">{link.label}</Button.Root>
					</li>
				{/each}
				<li>
					<ThemeSwitcher showLabel={false} />
				</li>
			</ul>

			<!-- 
				Navigation links.
				Displayed within dropdown menu on smaller screens.
			-->
			<div class="flex items-center md:hidden">
				<MobileNav />
			</div>
		</div>
	</nav>
</header>
