<script>
    import { AppBar } from '@skeletonlabs/skeleton';
</script>

<AppBar gridColumns="grid-cols-3" padding="p-0" slotLead="justify-self-start" slotDefault="justify-self-center" slotTrail="justify-self-end">

	<svelte:fragment slot="lead">
        <a href="#">
            <img class="w-12 mr-2 self-center" src="/autogmo_logo.png" alt="Logo" />
        </a>
        <div>
            <a href="#" class="text-3xl no-underline hover:text-blue-dark font-sans font-bold">AutoGMO</a><br>
            <span class="text-s text-grey-dark">Automated Garden Management & Optimization</span>
        </div>
    </svelte:fragment>
        <ul class="">
            <li class="">
                <a href="#" class="btn rounded-none hover:bg-primary-500">Home</a>
            </li>
            <li>
                <a href="#" class="btn rounded-none hover:bg-primary-500">Guides</a>
            </li>
            <li>
                <a href="#" class="btn rounded-none hover:bg-primary-500">Github</a>
            </li>
            <li>
                <a href="#" class="btn rounded-none hover:bg-primary-500">Donat</a>
            </li>
        </ul>
    <svelte:fragment slot="trail">
        <ul class="">
            <li>
                <a href="#" class="btn">Log in</a>
            </li>
            <li>
                <a href="#" class="btn variant-filled-primary">Register</a>
            </li>
        </ul>
    </svelte:fragment>


</AppBar>
