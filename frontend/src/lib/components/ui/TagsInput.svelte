<script lang="ts">
	import type Tag from '@melt-ui/svelte';
	import Icon from '@iconify/svelte';
	import iconIds from '$lib/assets/icons';
	import { createTagsInput, melt } from '@melt-ui/svelte';

	type Props = {
		tagsInput: string[] | undefined;
		maxTags: number;
		placeholder: string;
		onChange: Function | undefined;
		formAttrs: any;
	};

	let {
		tagsInput = $bindable([]),
		maxTags,
		placeholder,
		onChange,
		formAttrs
	}: Props = $props();

	const {
		elements: { root, tag, input, deleteTrigger, edit },
		states: { tags }
	} = createTagsInput({
		defaultTags: tagsInput,
		unique: true,
		editable: true,
		addOnPaste: true,
		trim: true,
		maxTags: maxTags,
		placeholder: placeholder,
		/** Sync the bindable input prop and Melt's writable store. */
		add(tag: string) {
			tagsInput.push(tag);
			console.log(tag);
			if (onChange) {
				onChange();
			}
			return { id: tag, value: tag };
		},
		/** The ID of the tag is the previous ID, the value is the newly set value. */
		update(tag: Tag.Tag) {
			tagsInput = tagsInput.filter((tagId) => {
				return tagId !== tag.id;
			});
			if (onChange) {
				onChange();
			}
			return { id: tag.value, value: tag.value };
		},
		remove(tag: Tag.Tag) {
			tagsInput = tagsInput.filter((tagId) => {
				return tagId !== tag.id;
			});
			if (onChange) {
				onChange();
			}
			return true;
		}
	});
</script>

<div
	class="flex flex-col items-start justify-center gap-2 rounded-md border border-neutral-12 bg-neutral-1 text-sm"
>
	<div
		use:melt={$root}
		class="flex w-full min-w-[280px] flex-row flex-wrap gap-2.5 rounded-md bg-neutral-1 px-3 py-2 text-neutral-11 focus-within:ring focus-within:ring-primary-6"
	>
		{#each $tags as t}
			<div
				use:melt={$tag(t)}
				class="flex items-center overflow-hidden rounded-md bg-neutral-2 text-neutral-11 [word-break:break-word] data-[disabled]:hover:cursor-default data-[disabled]:focus:!outline-none data-[disabled]:focus:!ring-0"
			>
				<span class="flex items-center border-r border-neutral-5 px-1.5">{t.value}</span
				>
				<button
					use:melt={$deleteTrigger(t)}
					class="flex h-full items-center px-1 enabled:hover:bg-neutral-3"
				>
					<Icon icon={iconIds.defaultClose} width="1rem" />
				</button>
			</div>
			<div
				use:melt={$edit(t)}
				class="flex items-center overflow-hidden rounded-md px-1.5 [word-break:break-word] data-[invalid-edit]:focus:!ring-destructive-6"
			></div>
		{/each}
		<input
			use:melt={$input}
			{...formAttrs}
			disabled={false}
			type="text"
			class="w-full min-w-[4.5rem] shrink grow basis-0 border-0 bg-neutral-1 text-neutral-11 outline-none focus:!ring-0 data-[invalid]:text-destructive-6"
		/>
	</div>
</div>
