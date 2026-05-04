import type { Db } from 'jazz-tools/backend';

import {
	type ActionType,
	AppError,
	type Garden,
	type User,
	isUserAuthorized,
	requiredRole
} from './index.js';
import { type JazzApp, jazz } from './schema.js';

/** Descriptive alias for the Jazz runtime database type. */
export type JazzDb = Db;

export const CONTROLLER_CONTEXT_ID = 'JazzController';

export type ControllerContextParams = {
	db: JazzDb;
	jazz: JazzApp;
	/** Returns the currently authenticated user, or null if unauthenticated. */
	getClient: (db: JazzDb) => Promise<User | null>;
};

/**
 * Controller class: singleton interface to the data layer.
 * Passed to controller functions to provide configurable behaviour.
 * @param params.db The Jazz Db instance.
 * @param params.jazz The app schema proxy with table query builders.
 * @param params.getClient A function for returning an authenticated user.
 * @returns ControllerContext.
 */
export function createController(params: ControllerContextParams) {
	/**
	 * Fetches the client's user object.
	 * If the client fails to authenticate, an AppError is raised.
	 * @returns The authenticated user.
	 */
	async function getClientOrError(): Promise<User> {
		const client = await params.getClient(params.db);
		if (client) return client;
		throw new AppError('Authentication failed.', {
			nonFormErrors: ['Authentication failed. A login is required.']
		});
	}

	/**
	 * Given a garden and an action, retrieve the client
	 * and throw an error if the client does not have at least that role.
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
		const client = await getClientOrError();

		const garden = await params.db.one(params.jazz.gardens.where({ id: gardenId }));
		if (garden == null) {
			throw new AppError('Garden key does not exist.', {
				nonFormErrors: ['Garden key does not exist.']
			});
		}

		const role = requiredRole(action);
		if (!isUserAuthorized(garden, client.profile.id, role)) {
			throw new AppError(`Requires ${role} access.`, {
				nonFormErrors: [`This action requires the ${role} role.`]
			});
		}

		return { client, garden };
	}

	return {
		db: params.db,
		jazz: params.jazz,
		getClient: params.getClient,
		getClientOrError,
		requireRole
	};
}
export type ControllerContext = ReturnType<typeof createController>;
