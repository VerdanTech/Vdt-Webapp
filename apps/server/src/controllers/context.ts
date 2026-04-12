import { eq } from 'drizzle-orm';

import {
	AppError,
	type ActionType,
	type Garden,
	gardens,
	isUserAuthorized,
	requiredRole
} from '@vdg-webapp/models';

import { type Db } from '../db/index.js';

/**
 * Context passed into every controller function.
 * The db instance is the Drizzle client; userId is the authenticated
 * profile ID decoded from the request's JWT by the auth plugin.
 */
export type ServerContext = {
	db: Db;
	userId: string;
};

/**
 * Fetches the garden and asserts the calling user has at least the role
 * required by the given action. Throws AppError on missing garden or
 * insufficient permissions.
 */
export async function requireGardenRole(
	ctx: ServerContext,
	gardenId: string,
	action: ActionType
): Promise<Garden> {
	const garden = await ctx.db.query.gardens.findFirst({
		where: eq(gardens.id, gardenId)
	});
	if (!garden) {
		throw new AppError('Garden does not exist.', {
			nonFormErrors: ['Garden does not exist.']
		});
	}

	const role = requiredRole(action);
	if (!isUserAuthorized(garden, ctx.userId, role)) {
		throw new AppError(`Requires ${role} access.`, {
			nonFormErrors: [`This action requires the ${role} role.`]
		});
	}

	return garden;
}
