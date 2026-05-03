<script lang="ts">
	import Icon from '@iconify/svelte';
	import { useQuery } from '@triplit/svelte';

	import { Button, Separator, iconIds } from '@vdg-webapp/ui';

	import {
		gardenMembershipAccept,
		gardenMembershipDelete
	} from '$data/gardens/commands';
	import type { AcceptancePendingMembershipsQueryResult } from '$data/gardens/queries';
	import triplit from '$data/triplit';
	import { userProfilesQuery } from '$data/users/queries';
	import createCommandHandler from '$state/commandHandler.svelte';

	type Props = {
		invite: AcceptancePendingMembershipsQueryResult;
	};
	let { invite }: Props = $props();

	let inviterProfile = useQuery(
		triplit,
		userProfilesQuery.Vars({ profileIds: [invite.inviterId] })
	);

	/** Mutations. */
	const gardenMembershipAcceptHandler = createCommandHandler(
		gardenMembershipAccept.mutation
	);
	const gardenMembershipDeleteHandler = createCommandHandler(
		gardenMembershipDelete.mutation
	);
</script>

<li class="flex flex-row">
	<div class="mr-8 flex flex-col">
		<div class="mb-4 flex max-w-64 flex-col overflow-hidden text-wrap">
			<span class="mb-1 font-semibold break-words">
				{invite.garden?.name ?? 'Error - garden not found.'}
			</span>
			<span
				class="bg-primary-3 text-primary-11 w-fit rounded-md p-1 text-sm break-all italic"
			>
				{invite.gardenId}
			</span>
		</div>
		<div class="my-0.5">
			<span class="text-neutral-11 text-sm">Invited by: </span>
			<span class="bg-neutral-4 text-neutral-11 rounded-lg p-1 text-sm italic">
				{#if inviterProfile.fetching}
					?
				{:else if inviterProfile.error}
					<i>unknown</i>
				{:else if inviterProfile.results}
					{inviterProfile.results[0].username}
				{/if}
			</span>
		</div>
		<div class="my-0.5">
			<span class="text-neutral-11 text-sm">Role:</span>
			<span class="text-neutral-11 text-sm italic">{invite.role}</span>
		</div>
	</div>
	<div class="flex flex-col justify-evenly">
		<Button.Root
			variant="default"
			onclick={() => {
				gardenMembershipAcceptHandler.execute({ gardenId: invite.gardenId });
			}}
		>
			<Icon icon={iconIds.gardenInviteAcceptIcon} width="1.5rem" />
		</Button.Root>
		<Button.Root
			variant="destructive"
			onclick={() => {
				gardenMembershipDeleteHandler.execute({ gardenId: invite.gardenId });
			}}><Icon width="1.5rem" icon={iconIds.gardenInviteRejectIcon} /></Button.Root
		>
	</div>
</li>
<li class="mt-2 mb-4 last:hidden">
	<Separator.Root class="bg-neutral-5 w-full" />
</li>
