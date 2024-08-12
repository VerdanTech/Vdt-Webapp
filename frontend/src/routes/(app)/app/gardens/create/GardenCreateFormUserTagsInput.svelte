<script lang="ts">
    import { writable } from 'svelte/store'
	import { Combobox } from 'bits-ui'
    import type Tag from '@melt-ui/svelte'
	import { flyAndScale } from '$lib/utils'
	import Icon from '@iconify/svelte'
	import iconIds from '$lib/assets/icons'
	import { createTagsInput, melt } from '@melt-ui/svelte'

	type Props = {
		tagsInput: string[]
		formAttrs: any
	}

	let { tagsInput = $bindable(), formAttrs }: Props = $props()

	const usernames = ['username1', 'username2']

	let comboboxInput = $state('')
	let touchedInput = $state(false)
	let filteredUsernames: string[] = $derived.by(() => {
		return comboboxInput && touchedInput
			? usernames.filter((username) => username.includes(comboboxInput.toLowerCase()))
			: usernames
	})

    function onComboboxSelectedChange(value: string) {
        console.log(value)
        $usernameTags.push({id: value, value: value})
    }

    let usernameTags = writable([{id: "Username1", value: "Username1"}])

	const {
		elements: { root, tag, input, deleteTrigger, edit },
		states: { tags }
	} = createTagsInput({
		defaultTags: ['Username1'],
		unique: true,
        editable: false,
		add(tag) {
			return { id: tag, value: tag }
		},
		addOnPaste: true,
        tags: usernameTags
	})
</script>

<Combobox.Root bind:inputValue={comboboxInput} bind:touchedInput onSelectedChange={onComboboxSelectedChange}>
	<div class="relative">
		<Icon
			icon={iconIds.gardenMembersIcon}
			class="absolute end-3 top-1/2 size-6 -translate-y-1/2 text-neutral-11"
		/>
		<Combobox.Input
			class="h-input rounded-9px border-border-input placeholder:text-neutral-11/50 focus:ring-offset-background inline-flex w-[296px] truncate border bg-neutral-1 px-11 text-sm transition-colors focus:outline-none focus:ring-2 focus:ring-primary-6 focus:ring-offset-2"
			placeholder="Enter a username"
			aria-label="Enter a username"
		/>
	</div>

	<Combobox.Content
		class="w-full rounded-xl border border-neutral-10 bg-neutral-2 px-1 py-3 outline-none"
		transition={flyAndScale}
		sideOffset={8}
	>
		{#each filteredUsernames as username}
			<Combobox.Item
				class="rounded-button data-[highlighted]:bg-muted flex h-10 w-full select-none items-center py-3 pl-5 pr-1.5 text-sm capitalize outline-none transition-all duration-75"
				value={username}
				label={username}
			>
				{username}
			</Combobox.Item>
		{:else}
			<span class="block px-5 py-2 text-sm text-muted-foreground">
				No results found
			</span>
		{/each}
	</Combobox.Content>
	<Combobox.HiddenInput name="newUsername" />
</Combobox.Root>

<div class="flex flex-col items-start justify-center gap-2">
	<div
		use:melt={$root}
		class="text-magnum-700 focus-within:ring-magnum-400 flex min-w-[280px] flex-row flex-wrap gap-2.5 rounded-md bg-white px-3
    py-2 focus-within:ring"
	>
		{#each $tags as t}
			<div
				use:melt={$tag(t)}
				class="bg-magnum-200 text-magnum-900 data-[disabled]:bg-magnum-300 data-[selected]:bg-magnum-400 flex items-center overflow-hidden
    rounded-md [word-break:break-word] data-[disabled]:hover:cursor-default
        data-[disabled]:focus:!outline-none data-[disabled]:focus:!ring-0"
			>
				<span class="flex items-center border-r border-white/10 px-1.5">{t.value}</span>
				<button
					use:melt={$deleteTrigger(t)}
					class="enabled:hover:bg-magnum-300 flex h-full items-center px-1"
				>
					<Icon icon={iconIds.defaultClose} width="1rem" />
				</button>
			</div>
			<div
				use:melt={$edit(t)}
				class="flex items-center overflow-hidden rounded-md px-1.5 [word-break:break-word] data-[invalid-edit]:focus:!ring-red-500"
			></div>
		{/each}
        <input
        use:melt={$input}
        disabled={true}
        type="text"
        class="min-w-[4.5rem] shrink grow basis-0 border-0 text-black outline-none focus:!ring-0 data-[invalid]:text-red-500"
      />
	</div>
</div>
