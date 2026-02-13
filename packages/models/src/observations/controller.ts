import { type ControllerContext } from '../controller.js';
import { type ObservationUpdateCommand } from '../index.js';

export async function observationUpdate(
	data: ObservationUpdateCommand,
	ctx: ControllerContext
) {
	console.log('here!!!!');
	console.log(data, ctx);
	/** Retrieve client and authorize. */
	//await ctx.requireRole(gardenId, 'ObservationUpdate');

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
