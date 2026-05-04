import { anyOf, schema as s } from 'jazz-tools';

import type { JazzApp } from '../schema.js';

export function constructPermissions(app: JazzApp) {
	s.definePermissions(app, ({ policy, session, allowedTo }) => {
		/* Observations - readable if garden is readable. */
		policy.observations.allowRead.where(allowedTo.read('gardenId'));

		/* Admins and editors may insert, update, and delete observations. */
		policy.observations.allowInsert.where((row) =>
			anyOf([
				policy.gardens.exists.where({
					id: row.gardenId,
					adminIds: { contains: session.userId }
				}),
				policy.gardens.exists.where({
					id: row.gardenId,
					editorIds: { contains: session.userId }
				})
			])
		);
		policy.observations.allowUpdate.where((row) =>
			anyOf([
				policy.gardens.exists.where({
					id: row.gardenId,
					adminIds: { contains: session.userId }
				}),
				policy.gardens.exists.where({
					id: row.gardenId,
					editorIds: { contains: session.userId }
				})
			])
		);
		policy.observations.allowDelete.where((row) =>
			anyOf([
				policy.gardens.exists.where({
					id: row.gardenId,
					adminIds: { contains: session.userId }
				}),
				policy.gardens.exists.where({
					id: row.gardenId,
					editorIds: { contains: session.userId }
				})
			])
		);
	});
}
