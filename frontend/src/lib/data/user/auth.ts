import { z as zod } from 'zod';
import { QueryClient, useMutation } from '@sveltestack/svelte-query';
import type { UserPasswordVerificationQuery } from '$codegen/types';
import { userLoginCommandOp } from '$codegen';
import { userFieldSchemas } from './schemas';

/**
 * Sends an authentication request to the backend.
 */
export const userLogin = {
	schema: zod.object({
		email_address: userFieldSchemas.email,
		password: userFieldSchemas.password
	}),
	mutation: (queryClient: QueryClient) => {
		return useMutation(
			function (data: UserPasswordVerificationQuery) {
				return userLoginCommandOp(data);
			},
			{
				/* Re-request the client user on mutation. */
				onSettled: () => {
					queryClient.invalidateQueries('clientProfile');
				}
			}
		);
	}
};
