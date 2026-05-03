import { AppError } from '../errors.js';
import type { ControllerContext } from '../index.js';
import { geometryHistoryCreate } from '../workspaces/index.js';
import {
	type LifespanUpdateCommand,
	type PlantUpdateCommand,
	type PlantsCreateCommand
} from './index.js';

async function plantsCreateSingle(data: PlantsCreateCommand, ctx: ControllerContext) {
	await ctx.requireRole(data.gardenId, 'PlantsCreate');

	/** TODO: Implement plant creation with lifespan and geometry setup. */
}

export async function plantsCreate(data: PlantsCreateCommand, ctx: ControllerContext) {
	switch (data.mode) {
		case 'SINGLE':
			return plantsCreateSingle(data, ctx);
		case 'GROUP':
			break;
		case 'PATTERN':
			break;
		case 'COMBINED':
			break;
		default:
			break;
	}
}

/** Updates a plant. */
export async function plantUpdate(
	id: string,
	data: PlantUpdateCommand,
	ctx: ControllerContext
) {
	const plant = await ctx.db.one(ctx.jazz.plants.where({ id }));
	if (!plant) {
		throw new AppError('Plant does not exist.', {
			nonFormErrors: ['Failed to update plant.']
		});
	}

	await ctx.requireRole(plant.gardenId, 'PlantUpdate');

	const partial: { cultivarName?: string; quantity?: number } = {};
	if (data.cultivarName) partial.cultivarName = data.cultivarName;
	if (data.quantity) partial.quantity = data.quantity;

	ctx.db.update(ctx.jazz.plants, id, partial);
}

/** Updates a lifespan. */
export async function lifespanUpdate(
	id: string,
	data: LifespanUpdateCommand,
	ctx: ControllerContext
) {
	const lifespan = await ctx.db.one(ctx.jazz.lifespans.where({ id }));
	if (!lifespan) {
		throw new AppError('Lifespan does not exist.', {
			nonFormErrors: ['Failed to update lifespan.']
		});
	}

	await ctx.requireRole(lifespan.gardenId, 'PlantUpdate');

	if (data.origin) {
		ctx.db.update(ctx.jazz.lifespans, id, { origin: data.origin });
	}
}
