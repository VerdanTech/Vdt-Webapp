<script lang="ts">
    type Props = {

    }

    let {form, value = $bindable(), editing} = $props()
</script>

{#if editing}
<input type="number" bind:value placeholder="None"/>
{:else}
<span
class="mx-2 rounded-lg border border-neutral-4 bg-neutral-2 px-4 py-2"
>
{value}
</span>
{/if}