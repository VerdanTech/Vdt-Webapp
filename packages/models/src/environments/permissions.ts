import { anyOf, schema as s } from 'jazz-tools';

import type { JazzApp } from '../schema.js';

export function constructPermissions(app: JazzApp) {
	s.definePermissions(app, ({ policy, session, allowedTo }) => {
		/* Environments - readable if garden is readable, writable by admins and editors. */
		policy.environments.allowRead.where(allowedTo.read('gardenId'));
		policy.environments.allowInsert.where((row) =>
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
		policy.environments.allowUpdate.where((row) =>
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
		policy.environments.allowDelete.where((row) =>
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
