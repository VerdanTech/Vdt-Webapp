<script lang="ts">
    import { melt, createTreeView, type TreeView } from '@melt-ui/svelte';
	import Icon from '@iconify/svelte';
	import iconIds from '$lib/assets/icons';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import * as Popover from '$lib/components/ui/popover';
	import * as Collapsible from '$lib/components/ui/collapsible';
	import * as Select from '$lib/components/ui/select';
	import { Field, Control, Label, FieldErrors, Description } from 'formsnap';
	import cultivarFields from '$lib/backendSchema/specs/cultivar';
	import { cultivarCollectionQuery } from '$data/cultivar/queries';
	import InPlaceEdit from '$components/InPlaceEdit.svelte';
	import { superForm, defaults } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';
	import {
		CultivarCollectionCreateCommandVisibility,
		CultivarCollectionFullSchemaVisibility, CultivarCollectionUpdateCommandVisibility 
	} from '$codegen/types';
	import type { CultivarSchema, CultivarCollectionFullSchema } from '$codegen/types';
	import { cultivarCollectionUpdate } from '$data/cultivar/commands';
	import { createServerErrors } from '$state/formServerErrors.svelte';
    
    type Props = {
        collectionRef: string;
        cultivar: CultivarSchema;
    }

    let {collectionRef, cultivar}: Props = $props()
</script>

    <button
        use:melt={$item({ id: cultivarTreeId, hasChildren: hasProfiles })}
        class="flex w-full w-full select-none items-center justify-between rounded-lg py-1 transition-colors hover:bg-neutral-3"
    >
        <div class="flex items-center overflow-hidden">
            <span class="mx-2 truncate text-lg font-bold text-neutral-12">
                {cultivar.name}
            </span>
            {#if cultivar.key}
                <span class="h-l w-1 text-neutral-12">&#183;</span>
                <span class="text-md mx-2 italic">{cultivar.key}</span>
            {/if}
        </div>
        <div class="h-[1px] flex-grow rounded-lg bg-neutral-3"></div>
        <Icon
            icon={iconIds.chevronRight}
            width="1.5rem"
            class="ml-2 {$isExpanded(cultivarTreeId) ? 'rotate-90' : ''}"
        />
    </button>

    <!-- Cultivar tree item children. -->
    <ul use:melt={$group({ id: cultivar.id })} class="w-full">
        <!-- Details tree item -->
        <li class="my-2 w-full">
            <button
                use:melt={$item({ id: cultivar.id + 'details', hasChildren: true })}
                class="flex w-full items-center justify-between rounded-lg py-1 transition-colors hover:bg-neutral-3"
            >
                <span class="text-md ml-6 truncate font-medium text-neutral-12">
                    Details
                </span>
                <div class="ml-4 h-[1px] flex-grow rounded-lg bg-neutral-3"></div>
                <Icon
                    icon={iconIds.chevronRight}
                    width="1.5rem"
                    class="ml-2 {$isExpanded(cultivar.id + 'details') ? 'rotate-90' : ''}"
                />
            </button>

            <ul use:melt={$group({ id: cultivar.id + 'details' })} class="w-full">
                <!-- Cultivar name tree item. -->
                <li class="my-2 w-full">
                    <div
                        use:melt={$item({ id: cultivar.id + 'name' })}
                        class="flex items-center justify-between"
                    >
                        <span class="ml-10 text-sm font-light text-neutral-11">Name</span>
                        <span
                            class="text-md rounded-lg border border-neutral-4 bg-neutral-2 p-2"
                            >{cultivar.names}</span
                        >
                    </div>
                </li>
                <!-- Cultivar key tree item. -->
                <li class="my-2 w-full">
                    <div
                        use:melt={$item({ id: cultivar.id + 'key' })}
                        class="flex items-center justify-between"
                    >
                        <span class="ml-10 text-sm font-light text-neutral-11">Key</span>
                        <span
                            class="text-md rounded-lg border border-neutral-4 bg-neutral-2 p-2"
                            >{cultivar.key}</span
                        >
                    </div>
                </li>
                <!-- Cultivar description tree item. -->
                <li class="my-2 w-full">
                    <div
                        use:melt={$item({ id: cultivar.id + 'description' })}
                        class="flex items-center justify-between"
                    >
                        <span class="ml-10 text-sm font-light text-neutral-11"
                            >Description</span
                        >
                        <span
                            class="text-md ml-8 text-wrap rounded-lg border border-neutral-4 bg-neutral-2 p-2 md:ml-16 lg:ml-64"
                            >{cultivar.description}</span
                        >
                    </div>
                </li>
            </ul>
        </li>

        <!-- Cultivar attribute profiles tree items. -->
        {#if cultivar.attributes}
            {#each Object.entries(cultivar.attributes) as [profileKey, profileValue]}
                {@const profileTreeId = cultivar.id + profileKey}
                {@const profileLabel =
                    cultivarFields[profileKey as keyof typeof cultivarFields]?.label}
                {@const profileDescription =
                    cultivarFields[profileKey as keyof typeof cultivarFields]
                        ?.description}
                {@const hasAttributes = true}

                <li class="my-1">
                    <button
                        use:melt={$item({ id: profileTreeId, hasChildren: hasAttributes })}
                        class="flex w-full items-center justify-between rounded-lg py-1 transition-colors hover:bg-neutral-3"
                    >
                        <span class="text-md ml-6 truncate font-medium text-neutral-12">
                            {profileLabel}
                        </span>
                        {@render infoPopover(profileDescription)}
                        <div class="ml-4 h-[1px] flex-grow rounded-lg bg-neutral-3"></div>
                        <Icon
                            icon={iconIds.chevronRight}
                            width="1.5rem"
                            class="ml-2 {$isExpanded(profileTreeId) ? 'rotate-90' : ''}"
                        />
                    </button>

                    <!-- Cultivar attributes tree items. -->
                    {#if profileValue}
                        <ul use:melt={$group({ id: profileTreeId })}>
                            {#each Object.entries(profileValue) as [attributeKey, attributeValue]}
                                {@const attributeTreeId =
                                    cultivar.id + profileKey + attributeKey}
                                {@const attributeLabel =
                                    cultivarFields[attributeKey as keyof typeof cultivarFields]
                                        ?.label}
                                {@const attributeDescription =
                                    cultivarFields[attributeKey as keyof typeof cultivarFields]
                                        ?.description}
                                {@const attributeUnit =
                                    cultivarFields[attributeKey as keyof typeof cultivarFields]
                                        ?.unit}
                                <li class="my-2 flex w-full items-center justify-between">
                                    <button
                                        use:melt={$item({ id: attributeTreeId })}
                                        class="flex w-auto items-center"
                                    >
                                        <span class="ml-10 text-sm text-neutral-11">
                                            {attributeLabel}
                                        </span>
                                        {@render infoPopover(attributeDescription)}
                                    </button>
                                    <div class="flex items-center">
                                        <span
                                            class="mx-2 rounded-lg border border-neutral-4 bg-neutral-2 px-4 py-2"
                                        >
                                            20
                                        </span>
                                        <span>
                                            {attributeUnit}
                                        </span>
                                    </div>
                                </li>
                            {/each}
                        </ul>
                    {/if}
                </li>
            {/each}
        {/if}
    </ul>