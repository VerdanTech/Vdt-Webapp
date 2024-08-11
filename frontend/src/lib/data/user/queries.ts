import { useQuery } from '@sveltestack/svelte-query'
import { userClientProfileQueryOp, userPublicProfilesQueryOp } from '$codegen'
import type { UserPublicProfilesQueryOpParams } from '$codegen/types'

/**
 * Retrieves the client's User object from the backend. Returns an error if not authenticated.
 */
export const userClientQuery = () => {
	return useQuery('clientProfile', userClientProfileQueryOp)
}

/**
 * Retrieves the requested user profiles.
 */
export const userProfilesQuery = (data: UserPublicProfilesQueryOpParams) => {
	return useQuery(data.user_ids, () => {
		return userPublicProfilesQueryOp(data)
	})
}
