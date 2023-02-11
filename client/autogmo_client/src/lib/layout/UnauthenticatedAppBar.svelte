<script>
    import { AppBar } from '@skeletonlabs/skeleton';
</script>

    <!--<AppBar gridColumns="grid-cols-3" gap="" padding="p-0" shadow="shadow-lg" slotLead="place-content-center" slotDefault="justify-self-center self-stretch" slotTrail="justify-self-stretch place-content-center">-->
<AppBar gridColumns="grid-cols-3" padding="p-0" shadow="shadow-lg" slotLead="justify-self-center" slotDefault="justify-self-center self-stretch" slotTrail="justify-self-center">
    <svelte:fragment slot="lead">
        <nav class="font-semibold text-lg p-4">
            <ul class="flex items-center">
                <li>
                    <a href="#">
                        <img class="w-16 mr-4" src="/autogmo_logo.png" alt="Logo" />
                    </a>
                </li>
                <li>
                    <a href="#" class="">
                        <span>AutoGMO</span>
                    </a>
                </li>
            </ul>
        </nav>
    </svelte:fragment>
	<svelte:fragment slot="default">
        <nav class="h-full font-semibold text-lg">
            <ul class="h-full flex">
                <li class="p-4 hover:bg-primary-700 hover:text-on-primary-token transition">
                    <a href="#" class="h-full flex">
                        <span class="self-center p-4">
                            Guides
                        </span>
                    </a>
                </li>
                <li class="p-4 hover:bg-primary-700 hover:text-on-primary-token transition">
                    <a href="#" class="h-full flex">
                        <span class="self-center p-4">
                            Github
                        </span>
                    </a>
                </li>
                <li class="p-4 hover:bg-primary-700 hover:text-on-primary-token transition">
                    <a href="#" class="h-full flex">
                        <span class="self-center p-4">
                            About
                        </span>
                    </a>
                </li>
                <li class="p-4 hover:bg-primary-700 hover:text-on-primary-token transition">
                    <a href="#" class="h-full flex">
                        <span class="self-center p-4">
                            Donate
                        </span>
                    </a>
                </li>
            </ul>
        </nav>
    </svelte:fragment>
	<svelte:fragment slot="trail">
        <nav class="font-semibold text-lg">
            <ul class="flex items-center">
                <li class="m-2">
                    <a href="#" class="btn">Log in</a>
                </li>
                <li class="m-2">
                    <a href="#" class="btn variant-filled-primary">Get started</a>
                </li>
            </ul>
        </nav>
    </svelte:fragment>
</AppBar>