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
		visibility: gardenFieldSchemas.visibility,
		description: gardenFieldSchemas.description.optional(),
		admin_ids: zod.array(zod.string().uuid()).optional(),
		editor_ids: zod.array(zod.string().uuid()).optional(),
		viewer_ids: zod.array(zod.string().uuid()).optional()
	}),
	mutation: () => {
		return useMutation(function (data: GardenCreateCommand) {
			return gardenCreateCommandOp(data)
		})
	}
}
