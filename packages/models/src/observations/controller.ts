import { type ControllerContext } from '../controller.js';
import { AppError } from '../errors.js';
import { type ObservationUpdateCommand } from '../index.js';

export async function observationUpdate(
	data: ObservationUpdateCommand,
	ctx: ControllerContext
) {
	const observation = await ctx.db.one(ctx.jazz.observations.where({ id: data.id }));
	if (!observation) {
		throw new AppError('Observation does not exist.', {
			nonFormErrors: ['Failed to update observation.']
		});
	}

	const partial: Partial<typeof observation> = {};
	if (data.entityIds) partial.entityIds = [...data.entityIds];
	if (data.date) partial.date = data.date;
	if (data.data !== undefined) partial.data = data.data;

	ctx.db.update(ctx.jazz.observations, data.id, partial);
}

/** Deletes an observation. */
export async function observationDelete(id: string, ctx: ControllerContext) {
	const observation = await ctx.db.one(ctx.jazz.observations.where({ id }));
	if (!observation) {
		throw new AppError('Observation does not exist.', {
			nonFormErrors: ['Failed to delete observation.']
		});
	}

	ctx.db.delete(ctx.jazz.observations, id);
}
