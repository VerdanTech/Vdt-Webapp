import { ControllerContext } from '../index.js';
import { AppError } from '../errors.js';
import { geometryHistoryCreate } from '../workspaces/index.js';
import {
	type LifespanUpdateCommand,
	type PlantUpdateCommand,
	type PlantsCreateCommand
} from './index.js';

async function plantsCreateSingle(data: PlantsCreateCommand, ctx: ControllerContext) {
	/** Retrieve client and authorize. */
	await ctx.requireRole(data.gardenId, 'PlantsCreate');

	/** Match cultivar. */

	/*
	const expectedGeometryHistoryId = await geometryHistoryCreate([data.singleSchema.])
	const expectedLifespan = await ctx.triplit.insert('lifespans', {
		gardenId: data.gardenId,
		origin: data.singleSchema.origin,
		geometryHistoryId: expectedGeometryHistoryId,
		locationHistoryId: expectedLocationHisotryId,
	})
	await ctx.triplit.insert('plants', {
		gardenId: data.gardenId,
		cultivarName: data.singleSchema.cultivarName,
		cultivarAttributes: data.singleSchema.cultivarOverride,
		expectedLifespanId,
		recordedLifespanId,
		aggregate: data.singleSchema.aggregate
	})
	*/
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

function generateDefaultGeometryHistory() {}

/** Updates a plant. */
export async function plantUpdate(
	id: string,
	data: PlantUpdateCommand,
	ctx: ControllerContext
) {
	const plant = await ctx.triplit.fetchOne(ctx.triplit.query('plants').Id(id));
	if (!plant) {
		throw new AppError('Plant does not exist.', {
			nonFormErrors: ['Failed to update plant.']
		});
	}

	await ctx.requireRole(plant.gardenId, 'PlantUpdate');

	await ctx.triplit.update('plants', id, (plant) => {
		if (data.cultivarName) {
			plant.cultivarName = data.cultivarName;
		}
		if (data.quantity) {
			plant.quantity = data.quantity;
		}
	});
}

/** Updates a lifespan. */
export async function lifespanUpdate(
	id: string,
	data: LifespanUpdateCommand,
	ctx: ControllerContext
) {
	const lifespan = await ctx.triplit.fetchOne(
		ctx.triplit.query('lifespans').Id(id)
	);
	if (!lifespan) {
		throw new AppError('Lifespan does not exist.', {
			nonFormErrors: ['Failed to update lifespan.']
		});
	}

	await ctx.requireRole(lifespan.gardenId, 'PlantUpdate');

	await ctx.triplit.update('lifespans', id, (lifespan) => {
		if (data.origin) {
			lifespan.origin = data.origin;
		}
	});
}
