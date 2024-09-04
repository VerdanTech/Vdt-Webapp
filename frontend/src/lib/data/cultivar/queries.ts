import { useQuery } from '@sveltestack/svelte-query';
import type { UseQueryOptions } from '@sveltestack/svelte-query';
import { cultivarCollectionGetByIdsQueryOp } from '$codegen';
import type {
	CultivarCollectionFullSchema,
	CultivarCollectionGetByIdsQueryOpParams
} from '$codegen/types';

/**
 * Retrieves a cultivar collection
 */
export const cultivarCollectionQuery = (
	data: CultivarCollectionGetByIdsQueryOpParams,
	options?: UseQueryOptions<CultivarCollectionFullSchema[]>
) => {
	return useQuery<CultivarCollectionFullSchema[]>(
		['cultivarCollections', data.ids],
		() => {
			return cultivarCollectionGetByIdsQueryOp(data);
		},
		options
	);
};
