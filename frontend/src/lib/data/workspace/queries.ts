import { useQuery } from '@sveltestack/svelte-query';
import type { UseQueryOptions } from '@sveltestack/svelte-query';
import { workspaceGetPartialsQueryOp } from '$codegen';
import type {
	WorkspaceGetPartialsQueryOpParams,
	WorkspacePartialSchema
} from '$codegen/types';

/**
 * Retrieves the workspace partial schemas associated with a garden.
 */
export const workspacePartialsQuery = (
	data: WorkspaceGetPartialsQueryOpParams,
	options?: UseQueryOptions<WorkspacePartialSchema[]>
) => {
	return useQuery<WorkspacePartialSchema[]>(
		['workspacePartials', data.garden_key],
		() => {
			return workspaceGetPartialsQueryOp(data);
		},
		options
	);
};
