<script lang="ts">
	import { Field, Control, Label, FieldErrors, Description } from 'formsnap';
	import FormInfoPopover from '$components/misc/FormInfoPopover.svelte';
	import FormErrorPopover from '$components/misc/FormErrorPopover.svelte';
	import cultivarFields from '$lib/backendSchema/specs/cultivar';
	import { attributeKeyToComponent } from './attributes';
	type Props = {};

	let { attributeKey, attributeValue, form, serverErrors, editing } = $props();
</script>

{#snippet inlineErrors(formFieldName: string)}
	<FieldErrors let:errors let:errorAttrs class="flex items-center">
		{#each errors as err}
			<FormErrorPopover description={err} {errorAttrs} />
		{/each}
		{#each serverErrors.errors[formFieldName] as err}
			<FormErrorPopover description={err} {errorAttrs} />
		{/each}
	</FieldErrors>
{/snippet}

{#if editing}
	<Field {form} name={attributeKey}>
		<Control let:attrs>
			<div class="flex items-center justify-between w-full">
				<div class="flex items-center">
					<Label class="ml-10 text-sm font-light text-neutral-11">Scientific Name</Label
					>
					<Description class="flex items-center">
						<FormInfoPopover
							description={cultivarFields[attributeKey as keyof typeof cultivarFields]
								?.description}
						/>
					</Description>
					{@render inlineErrors(attributeKey)}
				</div>
                <svelte:component
                this={attributeKeyToComponent(attributeKey)}
                formAttrs={attrs}
                bind:value={attributeValue}
                editing={editing}
            />
			</div>
		</Control></Field
	>
{:else}
	<div class="flex items-center justify-between w-full">
		<div class="flex items-center">
			<span class="ml-10 text-sm font-light text-neutral-11">Scientific Name</span>
			<FormInfoPopover
				description={cultivarFields[attributeKey as keyof typeof cultivarFields]
					?.description}
			/>
		</div>
		<svelte:component
			this={attributeKeyToComponent(attributeKey)}
            bind:value={attributeValue}
			editing={editing}
		/>
	</div>
{/if}
