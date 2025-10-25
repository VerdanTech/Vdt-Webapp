import { ControllerContext } from '../index.js';
import { geometryHistoryCreate } from '../workspaces/index.js';
import { PlantsCreateCommand } from './index.js';

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
