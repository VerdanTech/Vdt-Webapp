<script>
	import Icon from '@iconify/svelte';
	import * as Popover from '$lib/components/ui/popover/index';
	import { Separator } from '$lib/components/ui/separator/index';
	import { Button } from '$lib/components/ui/button';
	import Logo from '$lib/assets/logo.svelte';
	import { externalLinks } from '$lib/assets/links';
	import iconIds from '$lib/assets/icons';

	let navLinks = [
		{
			url: '/app/gardens',
			label: 'Gardens'
		},
		{
			url: '/guides',
			label: 'Guides'
		},
		{
			url: externalLinks.project,
			label: 'Project'
		}
	];
</script>

<!--
@component
Primary navigation between static pages app resources.

Shown to un-authenticated users everywhere in the app that
isn't within the context of a Garden.
-->
<header
	class="sticky left-0 top-0 w-full rounded-none border-b-2 border-neutral-7
		drop-shadow-md"
>
	<nav class="flex items-center justify-around bg-neutral-2 py-4">
		<!-- 
            Logo and VerdanTech text.
            Logo displayed always. Text displayed on larger screens.
        -->
		<div>
			<ul class="flex items-center gap-6 p-2 text-lg">
				<li>
					<a href="/">
						<Logo size="4rem"></Logo>
					</a>
				</li>
				<li>
					<a href="/" class="hidden lg:block">
						<span class="font-semibold">VerdanTech</span>
					</a>
				</li>
			</ul>
		</div>

		<!-- 
            Navigation links.
            Displayed within top horizontal menu on larger screens.
        -->
		<ul class="hidden gap-4 md:flex md:gap-8 lg:gap-12">
			{#each navLinks as link}
				<li class="">
					<Button href={link.url} variant="ghost">{link.label}</Button>
				</li>
			{/each}
		</ul>

		<!-- 
            Navigation links.
            Displayed within dropdown menu on smaller screens.
        -->
		<div class="flex md:hidden">
			<Popover.Root>
				<Popover.Trigger>
					<Icon icon={iconIds.dropdownMenuIcon} width="3rem" />
				</Popover.Trigger>
				<Popover.Content class="w-auto">
					<ul class="flex flex-col">
						<!-- 
							Navigation menu link snippet.
						-->
						{#snippet menuLink(url, label)}
							<Button href={url} variant="link">
								{label}
							</Button>
						{/snippet}

						{#each navLinks as link}
							<li>
								{@render menuLink(link.url, link.label)}
							</li>
						{/each}
						<Separator class="w-full bg-neutral-6 opacity-50" />
						<li>
							{@render menuLink('/login', 'Login')}
						</li>
						<li>
							{@render menuLink('/register', 'Get Started')}
						</li>
					</ul>
				</Popover.Content>
			</Popover.Root>
		</div>

		<!-- 
        Login and registration links.
        Displayed with a top horizontal menu on larger screens.
    	-->
		<ul class="hidden gap-8 text-lg md:flex">
			<li class="hidden lg:block">
				<Button href="/login" variant="default">Login</Button>
			</li>
			<li>
				<Button href="/register" variant="outline">Get Started</Button>
			</li>
		</ul>
	</nav>
</header>
