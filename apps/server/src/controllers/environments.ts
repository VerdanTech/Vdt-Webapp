import { eq, sql } from 'drizzle-orm';

import {
	AppError,
	type EnvironmentAttributesUpdateCommand,
	type EnvironmentCreateCommand,
	environments
} from '@vdg-webapp/models';

import { type ServerContext, requireGardenRole } from './context.js';

export async function environmentCreate(
	data: EnvironmentCreateCommand,
	ctx: ServerContext
): Promise<{ id: string; txid: number }> {
	await requireGardenRole(ctx, data.gardenId, 'WorkspaceEdit');

	return ctx.db.transaction(async (tx) => {
		const [env] = await tx
			.insert(environments)
			.values({
				gardenId: data.gardenId,
				name: data.name,
				description: data.description ?? '',
				parentType: data.parentType,
				attributes: {}
			})
			.returning();

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { id: env.id, txid: parseInt(txid) };
	});
}

export async function environmentAttributesUpdate(
	id: string,
	attributes: EnvironmentAttributesUpdateCommand,
	ctx: ServerContext
): Promise<{ txid: number }> {
	const env = await ctx.db.query.environments.findFirst({
		where: eq(environments.id, id),
		columns: { id: true, gardenId: true }
	});
	if (!env) {
		throw new AppError('Environment does not exist.', {
			nonFormErrors: ['Failed to update environment.']
		});
	}

	await requireGardenRole(ctx, env.gardenId, 'WorkspaceEdit');

	return ctx.db.transaction(async (tx) => {
		await tx.update(environments).set({ attributes }).where(eq(environments.id, id));

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}
