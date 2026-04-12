import { eq, sql } from 'drizzle-orm';

import {
	AppError,
	type LifespanUpdateCommand,
	type PlantUpdateCommand,
	lifespans,
	plants
} from '@vdg-webapp/models';

import { type ServerContext, requireGardenRole } from './context.js';

export async function plantUpdate(
	id: string,
	data: PlantUpdateCommand,
	ctx: ServerContext
): Promise<{ txid: number }> {
	const plant = await ctx.db.query.plants.findFirst({
		where: eq(plants.id, id),
		columns: { id: true, gardenId: true }
	});
	if (!plant) {
		throw new AppError('Plant does not exist.', {
			nonFormErrors: ['Failed to update plant.']
		});
	}

	await requireGardenRole(ctx, plant.gardenId, 'PlantUpdate');

	return ctx.db.transaction(async (tx) => {
		await tx
			.update(plants)
			.set({
				...(data.cultivarName !== undefined && { cultivarName: data.cultivarName }),
				...(data.quantity !== undefined && { quantity: data.quantity })
			})
			.where(eq(plants.id, id));

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}

export async function lifespanUpdate(
	id: string,
	data: LifespanUpdateCommand,
	ctx: ServerContext
): Promise<{ txid: number }> {
	const lifespan = await ctx.db.query.lifespans.findFirst({
		where: eq(lifespans.id, id),
		columns: { id: true, gardenId: true }
	});
	if (!lifespan) {
		throw new AppError('Lifespan does not exist.', {
			nonFormErrors: ['Failed to update lifespan.']
		});
	}

	await requireGardenRole(ctx, lifespan.gardenId, 'LifespanUpdate');

	return ctx.db.transaction(async (tx) => {
		await tx
			.update(lifespans)
			.set({
				...(data.origin !== undefined && { origin: data.origin })
			})
			.where(eq(lifespans.id, id));

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}
