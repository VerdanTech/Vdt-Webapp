import { anyOf, schema as s } from 'jazz-tools';

import type { JazzApp } from '../schema.js';

export function constructPermissions(app: JazzApp) {
	s.definePermissions(app, ({ policy, session, allowedTo }) => {
		/* CultivarCollections - readable if not hidden or if user/garden member owns it. */
		policy.cultivarCollections.allowRead.where((row) =>
			anyOf([
				{ visibility: { ne: 'HIDDEN' } },
				{ userId: { eq: session.userId } },
				policy.gardens.exists.where({
					id: row.gardenId,
					adminIds: { contains: session.userId }
				}),
				policy.gardens.exists.where({
					id: row.gardenId,
					editorIds: { contains: session.userId }
				}),
				policy.gardens.exists.where({
					id: row.gardenId,
					viewerIds: { contains: session.userId }
				})
			])
		);

		/* Collections are owned by the user or by a garden admin. */
		policy.cultivarCollections.allowInsert.where((row) =>
			anyOf([
				{ userId: { eq: session.userId } },
				policy.gardens.exists.where({
					id: row.gardenId,
					adminIds: { contains: session.userId }
				})
			])
		);
		policy.cultivarCollections.allowUpdate.where((row) =>
			anyOf([
				{ userId: { eq: session.userId } },
				policy.gardens.exists.where({
					id: row.gardenId,
					adminIds: { contains: session.userId }
				})
			])
		);
		policy.cultivarCollections.allowDelete.where((row) =>
			anyOf([
				{ userId: { eq: session.userId } },
				policy.gardens.exists.where({
					id: row.gardenId,
					adminIds: { contains: session.userId }
				})
			])
		);

		/* Cultivars - access follows the parent collection's rules. */
		policy.cultivars.allowRead.where(allowedTo.read('collectionId'));
		policy.cultivars.allowInsert.where(allowedTo.update('collectionId'));
		policy.cultivars.allowUpdate.where(allowedTo.update('collectionId'));
		policy.cultivars.allowDelete.where(allowedTo.update('collectionId'));
	});
}
