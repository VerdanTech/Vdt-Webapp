<script lang="ts">
	import Icon from '@iconify/svelte';
	import { createTagsInput, melt } from '@melt-ui/svelte';
	import { useQuery } from '@triplit/svelte';

	import { Popover, iconIds } from '@vdg-webapp/ui';

	import triplit from '$data/triplit';
	import { userProfilesUsernameQuery } from '$data/users/queries';

	/** TODO: Redo this component once Melt-UI has updated the Tags-Input component to runes. */

	type Props = {
		tagsInput: string[];
		maxTags: number | undefined;
	};

	let { tagsInput = $bindable(), maxTags, ...restProps }: Props = $props();

	const {
		elements: { root, tag, input, deleteTrigger, edit },
		states: { tags }
	} = createTagsInput({
		unique: true,
		editable: true,
		addOnPaste: true,
		trim: true,
		maxTags,
		placeholder: 'Enter a username',
		/** Sync the bindable input prop and Melt's writable store. */
		add(tag: string) {
			tagsInput.push(tag);
			return { id: tag, value: tag };
		},
		/** The ID of the tag is the previous ID, the value is the newly set value. */
		update(tag) {
			tagsInput = tagsInput.filter((username) => {
				return username !== tag.id;
			});
			tagsInput.push(tag.value);
			return { id: tag.value, value: tag.value };
		},
		remove(tag) {
			tagsInput = tagsInput.filter((username) => {
				return username !== tag.id;
			});
			return true;
		}
	});

	/** Indicate in the input whether the username exists. */
	let profiles = $derived(
		useQuery(
			triplit,
			userProfilesUsernameQuery.Select(['username']).Vars({ usernames: [...tagsInput] })
		)
	);
</script>

<div
	class="border-neutral-7 bg-neutral-1 flex flex-col items-start justify-center gap-2 rounded-md border text-sm"
>
	<div
		use:melt={$root}
		class="bg-neutral-1 text-neutral-11 focus-within:ring-primary-6 flex w-full min-w-[280px] flex-row flex-wrap gap-2.5 rounded-md px-3 py-2 focus-within:ring"
	>
		{#each $tags as t}
			<div
				use:melt={$tag(t)}
				class="bg-neutral-2 text-neutral-11 flex items-center overflow-hidden rounded-md [word-break:break-word] data-[disabled]:hover:cursor-default data-[disabled]:focus:!ring-0 data-[disabled]:focus:!outline-none"
			>
				<span class="flex items-center px-1.5">{t.value}</span>
				<Popover.Root>
					<Popover.Trigger class="pr-1.5">
						{#if profiles.results && profiles.results.find((profile) => profile.username === t.value)}
							<Icon icon={iconIds.checkmarkIcon} class="text-primary-8" width="1rem" />
						{:else if profiles.fetching}
							<Icon
								icon={iconIds.defaultSpinnerIcon}
								class="text-neutral-6 animate-spin"
								width="1rem"
							/>
						{:else}
							<Icon icon={iconIds.errorIcon} class="text-destructive-8" width="1rem" />
						{/if}
					</Popover.Trigger>
					<Popover.Content>
						{#if profiles.results && profiles.results.includes({ username: t.value })}
							This user exists.
						{:else if profiles.fetching}
							Verifying username...
						{:else}
							This user does not exist.
						{/if}
					</Popover.Content>
				</Popover.Root>
				<button
					use:melt={$deleteTrigger(t)}
					type="button"
					class="enabled:hover:bg-neutral-3 border-neutral-5 flex h-full items-center border-l px-1"
				>
					<Icon icon={iconIds.defaultClose} width="1rem" />
				</button>
			</div>
			<div
				use:melt={$edit(t)}
				class="data-[invalid-edit]:focus:!ring-destructive-6 flex items-center overflow-hidden rounded-md px-1.5 [word-break:break-word]"
			></div>
		{/each}
		<input
			use:melt={$input}
			{...restProps}
			disabled={false}
			type="text"
			class="bg-neutral-1 text-neutral-11 data-[invalid]:text-destructive-6 w-full min-w-[4.5rem] shrink grow basis-0 border-0 outline-none focus:!ring-0"
		/>
	</div>
</div>
