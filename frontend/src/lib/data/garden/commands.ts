import { z as zod } from 'zod';
import { useMutation } from '@sveltestack/svelte-query';
import type {
	GardenCreateCommand,
	GardenMembershipAcceptCommand,
	GardenMembershipDeleteCommand
} from '$codegen/types';
import {
	gardenCreateCommandOp,
	gardenMembershipAcceptCommandOp,
	gardenMembershipDeleteCommandOp
} from '$codegen';
import { gardenFieldSchemas } from './schemas';

/**
 * Sends a garden creation request to the backend.
 */
export const gardenCreate = {
	schema: zod.object({
		name: gardenFieldSchemas.name,
		key: gardenFieldSchemas.key,
		visibility: gardenFieldSchemas.visibility.optional(),
		description: gardenFieldSchemas.description.optional(),
		admin_usernames: gardenFieldSchemas.user_invites_list.optional(),
		editor_usernames: gardenFieldSchemas.user_invites_list.optional(),
		viewer_usernames: gardenFieldSchemas.user_invites_list.optional()
	}),
	mutation: () => {
		return useMutation(function (data: GardenCreateCommand) {
			return gardenCreateCommandOp(data);
		});
	}
};

/**
 * Sends a garden membership acceptance request to the backend.
 */
export const gardenMembershipAccept = {
	schema: zod.object({
		key: gardenFieldSchemas.key
	}),
	mutation: () => {
		return useMutation(function (data: GardenMembershipAcceptCommand) {
			return gardenMembershipAcceptCommandOp(data);
		});
	}
};

/**
 * Sends a garden membership deletion request to the backend.
 */
export const gardenMembershipDelete = {
	schema: zod.object({
		key: gardenFieldSchemas.key
	}),
	mutation: () => {
		return useMutation(function (data: GardenMembershipDeleteCommand) {
			return gardenMembershipDeleteCommandOp(data);
		});
	}
};
