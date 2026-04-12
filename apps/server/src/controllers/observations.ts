import { eq, sql } from 'drizzle-orm';

import { AppError, type ObservationUpdateCommand, observations } from '@vdg-webapp/models';

import { type ServerContext, requireGardenRole } from './context.js';

export async function observationUpdate(
	id: string,
	data: ObservationUpdateCommand,
	ctx: ServerContext
): Promise<{ txid: number }> {
	const obs = await ctx.db.query.observations.findFirst({
		where: eq(observations.id, id),
		columns: { id: true, gardenId: true }
	});
	if (!obs) {
		throw new AppError('Observation does not exist.', {
			nonFormErrors: ['Failed to update observation.']
		});
	}

	await requireGardenRole(ctx, obs.gardenId, 'ObservationUpdate');

	return ctx.db.transaction(async (tx) => {
		await tx
			.update(observations)
			.set({
				...(data.entityIds !== undefined && { entityIds: [...data.entityIds] }),
				...(data.date !== undefined && { date: data.date }),
				...(data.data !== undefined && { data: data.data })
			})
			.where(eq(observations.id, id));

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}

export async function observationDelete(
	id: string,
	ctx: ServerContext
): Promise<{ txid: number }> {
	const obs = await ctx.db.query.observations.findFirst({
		where: eq(observations.id, id),
		columns: { id: true, gardenId: true }
	});
	if (!obs) {
		throw new AppError('Observation does not exist.', {
			nonFormErrors: ['Failed to delete observation.']
		});
	}

	await requireGardenRole(ctx, obs.gardenId, 'ObservationUpdate');

	return ctx.db.transaction(async (tx) => {
		await tx.delete(observations).where(eq(observations.id, id));

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}
