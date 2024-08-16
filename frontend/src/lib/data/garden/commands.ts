import { z as zod } from 'zod'
import { useMutation } from '@sveltestack/svelte-query'
import type { GardenCreateCommand } from '$codegen/types'
import { gardenCreateCommandOp } from '$codegen'
import { gardenFieldSchemas } from './schemas'

/**
 * Sends an garden creation request to the backend.
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
			return gardenCreateCommandOp(data)
		})
	}
}
