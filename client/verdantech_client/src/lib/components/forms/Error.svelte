<script>
    import ErrorCircleRoundedOutline from 'virtual:icons/material-symbols/error-circle-rounded-outline';
    export let text = ""
</script>

<div class="p-2 bg-error-500 rounded-token border-token">
    <span>
        <ErrorCircleRoundedOutline style="font-size: 2em" />
    </span>
    <span class="text-on-error-token">
        {text}
    </span>
</div>