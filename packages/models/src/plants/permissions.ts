import { anyOf, schema as s } from 'jazz-tools';

import type { JazzApp } from '../schema.js';

export function constructPermissions(app: JazzApp) {
	s.definePermissions(app, ({ policy, session, allowedTo }) => {
		/* Lifespans - readable if garden is readable, writable by admins and editors. */
		policy.lifespans.allowRead.where(allowedTo.read('gardenId'));
		policy.lifespans.allowInsert.where((row) =>
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
		policy.lifespans.allowUpdate.where((row) =>
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
		policy.lifespans.allowDelete.where((row) =>
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

		/* Plants - readable if garden is readable, writable by admins and editors. */
		policy.plants.allowRead.where(allowedTo.read('gardenId'));
		policy.plants.allowInsert.where((row) =>
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
		policy.plants.allowUpdate.where((row) =>
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
		policy.plants.allowDelete.where((row) =>
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

		/* PlantGroups - readable if garden is readable, writable by admins and editors. */
		policy.plantGroups.allowRead.where(allowedTo.read('gardenId'));
		policy.plantGroups.allowInsert.where((row) =>
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
		policy.plantGroups.allowUpdate.where((row) =>
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
		policy.plantGroups.allowDelete.where((row) =>
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
