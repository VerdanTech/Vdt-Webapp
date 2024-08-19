<script lang="ts">
	import Icon from '@iconify/svelte'
	import iconIds from '$lib/assets/icons'
	import { Button } from '$lib/components/ui/button'
	import { Separator } from '$lib/components/ui/separator'
	import { ScrollArea } from '$lib/components/ui/scroll-area/index.js'
    import type { GardenMembershipFullSchemaRole, GardenPendingInviteSchema } from '$codegen/types'
	import {gardenMembershipAccept, gardenMembershipDelete} from '$data/garden/commands'

	type Props = {
		invites: GardenPendingInviteSchema[]
	}

	let { invites }: Props = $props()

	/** Mutations. */
	const inviteAcceptMutation = gardenMembershipAccept.mutation()
	const inviteDeleteMutation = gardenMembershipDelete.mutation()
</script>

<!-- Pending invites list. -->
{#snippet pendingInvite(
	gardenName: string,
	gardenKey: string,
	inviterUsername: string | undefined,
	role: GardenMembershipFullSchemaRole,
	expiryCountdownHours: number
)}

	<li class="flex flex-row">
		<div class="flex flex-col mr-8">
			<div class="flex flex-col max-w-64 overflow-hidden text-wrap mb-4">
				<span class="break-words font-semibold mb-1">
					{gardenName}
				</span>
				<span class="italic rounded-md bg-primary-3 p-1 text-sm text-primary-11 break-all w-fit">
					{gardenKey}
				</span>
			</div>
			<div class="my-0.5">
				<span class="text-sm text-neutral-11">Invited by:</span>
				<span class="text-sm text-neutral-11 italic bg-neutral-4 p-1 rounded-lg">
					{#if inviterUsername}
					inviterUsername
					{:else}
					unknown
					{/if}
				</span>
			</div>
			<div class="my-0.5">
				<span class="text-sm text-neutral-11">Role:</span>
				<span class="text-sm text-neutral-11 italic">{role}</span>
			</div>
			<div class="my-0.5">
				<span class="text-sm text-neutral-11">Expires in:</span>
				<span class="text-sm text-neutral-11 italic">{expiryCountdownHours} hours</span>
			</div>
		</div>
		<div class="flex flex-col justify-evenly">
				<Button variant="default" on:click={() => {$inviteAcceptMutation.mutate({garden_key: gardenKey})}} >
					<Icon icon={iconIds.gardenInviteAcceptIcon} width="1.5rem"/>
				</Button>
				<Button variant="destructive" on:click={() => {$inviteDeleteMutation.mutate({garden_key: gardenKey})}><Icon width="1.5rem" icon={iconIds.gardenInviteRejectIcon}/></Button>
		</div>
	</li>
	<li class="mt-2 mb-4 last:hidden">
		<Separator class="w-full bg-neutral-5" />
	</li>
{/snippet}
<ScrollArea type="auto" orientation="vertical" class="w-auto {(invites.length > 1) ? 'h-96' : 'h-48'}">
	<ul class="p-4">
		{#each invites as invite}
				{@render pendingInvite(
					invite.garden.name,
					invite.garden.key,
					undefined,
					invite.invite.role,
					invite.expiry_countdown_hours
				)}

		{/each}
	</ul>
</ScrollArea>
