import { useQueries, useQuery } from '@sveltestack/svelte-query';
import {
	userClientProfileQueryOp,
	userPublicProfilesQueryOp,
	usernameExistsQueryOp
} from '$codegen';
import type {
	UserPublicProfilesQueryOpParams,
	UsernameExistsQueryOpParams
} from '$codegen/types';

/**
 * Retrieves the client's User object from the backend. Returns an error if not authenticated.
 */
export const userClientQuery = () => {
	return useQuery('clientProfile', userClientProfileQueryOp);
};

/**
 * Retrieves the requested user profiles.
 */
export const userProfilesQuery = (data: UserPublicProfilesQueryOpParams) => {
	return useQuery(['publicProfiles', data.user_ids], () => {
		return userPublicProfilesQueryOp(data);
	});
};

/**
 * Constructs a list of queries which return whether a username exists.
 */
export const usernamesExistQueries = (data: Array<string>) => {
	return useQueries(
		data.map((username) => {
			return {
				queryKey: ['usernameExists', username],
				queryFn: () => usernameExistsQueryOp({ username: username })
			};
		})
	);
};
