import { type ControllerContext } from '../controller.js';
import { type ObservationUpdateCommand } from '../index.js';

export async function observationUpdate(
	data: ObservationUpdateCommand,
	ctx: ControllerContext
) {
	/** Retrieve client and authorize. */
	//await ctx.requireRole(gardenId, 'ObservationUpdate');

	const obs = await ctx.triplit.fetchOne(ctx.triplit.query('observations').Id(data.id))

	/** Update the observation. */
	await ctx.triplit.update('observations', data.id, (observation) => {
		if (data.entityIds) {
			observation.entityIds = data.entityIds;
		}
		if (data.date) {
			observation.date = data.date;
		}
		if (data.data) {
			observation.data = data.data;
		}
	});
}
