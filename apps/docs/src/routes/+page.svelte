<script lang="ts">
	import Icon from '@iconify/svelte';

	import { Button, VdgLogo, cn } from '@vdg-webapp/ui';

	import LandingPageDemo from '$components/landingPage/LandingPageDemo.svelte';
	import Nav from '$components/nav/Nav.svelte';
	import env from '$lib/env';

	type Explainer = {
		title: string;
		points: string[];
		icon: string;
		iconContainerClass?: string;
		iconClass?: string;
	};
	const explainers: Explainer[] = [
		{
			title: 'A garden productivity tool and agro-ecological model',
			points: [
				'Maximize the use of space by simulating plants throughout space and time',
				'Tune recommendations for starting plants to local environmental conditions',
				'Compare multiple plans against estimated metrics of yield and eco benefit'
			],
			icon: 'mdi:plant-outline',
			iconContainerClass: 'bg-primary-8 border-primary-10',
			iconClass: 'text-primary-1'
		},
		{
			title:
				'A community hub for the coordination of labour and the distribution of produce',
			points: [
				'Edit gardens with other users in real time',
				'Generate tasks and assign responsibilities',
				'Record harvests and notify subscribers'
			],
			icon: 'mdi:handshake-outline',
			iconContainerClass: 'bg-secondary-8 border-secondary-10',
			iconClass: 'text-secondary-1'
		},
		{
			title:
				'An interface for external devices to send data to and receive commands from',
			points: [
				'Use environmental data to inform planning and update the model',
				'Use the model to intelligently control outputs such as irrigation'
			],
			icon: 'ant-design:control-outlined',
			iconContainerClass: 'bg-accent-8 border-accent-10',
			iconClass: 'text-accent-1'
		}
	];

	const developmentStatusClass = 'bg-crimson-5 border-crimson-6 text-crimson-12';
</script>

<svelte:head>
	<title
		>Verdagraph - Eco-modelling tools for collaboratively organized agriculture</title
	>
</svelte:head>

{#snippet explainerSnippet(explainer: Explainer)}
	<div class="mt-8 flex justify-between">
		<div class="flex h-full flex-col">
			<h3 class="text-neutral-12 w-full text-lg font-semibold">
				{explainer.title}
			</h3>
			<ul class="mt-4 flex list-disc flex-col gap-4 rounded-lg p-4">
				{#each explainer.points as point}
					<li class="text-neutral-11 text-sm">
						{point}
					</li>
				{/each}
			</ul>
		</div>
		<div
			class={cn(
				explainer.iconContainerClass,
				'ml-6 flex items-center justify-center rounded-lg border p-4'
			)}
		>
			<Icon icon={explainer.icon} width="6rem" class={explainer.iconClass || ''} />
		</div>
	</div>
{/snippet}

<div class="flex w-full flex-col">
	<Nav />
	<div class="mb-12 flex h-full w-full justify-center">
		<div class="flex w-11/12 flex-col md:w-5/6 lg:w-3/4 2xl:w-1/2">
			<div class="mt-12 flex w-full items-center justify-between">
				<h1 class="text-left text-xl font-extrabold md:text-2xl lg:text-4xl">
					Eco-modelling tools for collaboratively organized agriculture
				</h1>
				<div class="ml-8">
					<VdgLogo size="8rem" />
				</div>
			</div>

			<div class="mt-16 flex justify-between gap-4">
				<Button.Root variant="default" href={env.DEMO_URL} class="w-full"
					>Try the Demonstration</Button.Root
				>
				<Button.Root variant="default" href={env.APP_URL} class="w-full"
					>Get Started</Button.Root
				>
			</div>

			<LandingPageDemo />

			<div class="mt-8 flex w-full flex-col gap-6">
				<div class="flex items-center justify-between">
					<h2 class="text-neutral-11 font-semibold">Project status:</h2>
					<div class="bg-neutral-6 mx-8 h-[1px] grow rounded-lg"></div>
					<span
						class={cn(developmentStatusClass, 'rounded-lg border px-4 py-2 text-sm')}
					>
						Early development
					</span>
				</div>

				<div class="mt-4 flex flex-col gap-4">
					<Button.Root
						variant="secondary"
						href={env.NEWSLETTER_URL}
						class="w-full text-wrap"
						>Join the newsletter for new features and progress updates</Button.Root
					>
				</div>

				<div class="bg-neutral-6 mt-4 h-[1px] grow rounded-lg"></div>

				<div class="mt-4 flex flex-col gap-8">
					<p class="text-neutral-11 italic">
						Verdagraph is a collection of open source tools that seek to empower the
						collaborative planning, tracking, and automation of agro-ecological systems.
						It currently consists of a garden productivity application and a smart
						irrigation controller.
					</p>

					{#each explainers as explainer}
						{@render explainerSnippet(explainer)}
					{/each}
				</div>
			</div>

			<div class="mt-12 flex justify-between gap-4">
				<Button.Root variant="outline" href="/about" class="w-full"
					>Read More</Button.Root
				>
				<Button.Root variant="outline" href="/support" class="w-full"
					>Support the Project</Button.Root
				>
			</div>
		</div>
	</div>
</div>
