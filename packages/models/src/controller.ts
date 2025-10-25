import { TriplitClient as TriplitClientBase } from '@triplit/client';

import {
	type ActionType,
	AppError,
	type Garden,
	type User,
	isUserAuthorized,
	requiredRole,
	schema
} from './index.js';

type TriplitClient = TriplitClientBase<typeof schema>;

export const CONTROLLER_CONTEXT_ID = 'TriplitController';

export type ControllerContextParams = {
	triplit: TriplitClient;
	getClient: (triplit: TriplitClient) => Promise<User | null>;
};

/**
 * Controller class: singleton interface to the data layer.
 * Passed to controller functions to provide configurable behaviour.
 * @param triplit The Triplit client to perform operations on.
 * @param getClient A function for returning an authenticated user.
 * @returns ControllerContext.
 */
export function createController(params: ControllerContextParams) {
	const gardenQuery = params.triplit.query('gardens').Id('$query.id');
	/**
	 * Fetches the client's Account and Profile objects.
	 * If the client fails to authenticate, an access refresh is attempted.
	 * If this fails, an AppError is raised.
	 * @returns The client.
	 */
	async function getClientOrError(): Promise<User> {
		/** Return the client if authenticated. */
		const client = await params.getClient(params.triplit);
		if (client) {
			return client;
		}

		throw new AppError('Authentication failed.', {
			nonFormErrors: ['Authentication failed. A login is required.']
		});
	}

	/**
	 * Given a garden and an action, retrieve the client
	 * and throw an error if the client does not have at least
	 * that role.
	 * @param gardenId The garden to retrieve.
	 * @param action The action to authorize for.
	 * @returns The client and garden objects.
	 */
	async function requireRole(
		gardenId: string,
		action: ActionType
	): Promise<{
		client: User;
		garden: Garden;
	}> {
		/** Retrieve client. */
		const client = await getClientOrError();

		/** Retrieve garden. */
		const garden = await params.triplit.fetchOne(gardenQuery.Vars({ id: gardenId }));
		if (garden == null) {
			throw new AppError('Garden key does not exist.', {
				nonFormErrors: ['Garden key does not exist.']
			});
		}

		/** Ensure client is of the specified role. */
		const role = requiredRole(action);
		if (!isUserAuthorized(garden, client.profile.id, role)) {
			throw new AppError(`Requires ${role} access.`, {
				nonFormErrors: [`This action requires the ${role} role.`]
			});
		}

		return { client, garden };
	}

	return {
		triplit: params.triplit,
		getClient: params.getClient,
		getClientOrError,
		requireRole
	};
}
export type ControllerContext = ReturnType<typeof createController>;
