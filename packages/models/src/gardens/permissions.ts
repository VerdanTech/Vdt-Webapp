import { anyOf, schema as s } from 'jazz-tools';

import type { JazzApp } from '../schema.js';

export function constructPermissions(app: JazzApp) {
	s.definePermissions(app, ({ policy, session }) => {
		/* Gardens. */
		policy.gardens.allowRead.where(
			anyOf([
				{ visibility: { ne: 'HIDDEN' } },
				{ adminIds: { contains: session.userId } },
				{ editorIds: { contains: session.userId } },
				{ viewerIds: { contains: session.userId } }
			])
		);
		policy.gardens.allowInsert.always();
		policy.gardens.allowUpdate.where({ adminIds: { contains: session.userId } });
		policy.gardens.allowDelete.never();

		/* GardenMemberships - readable by garden members, writable by admins only. */
		policy.gardenMemberships.allowRead.where((membership) =>
			anyOf([
				policy.gardens.exists.where({
					id: membership.gardenId,
					adminIds: { contains: session.userId }
				}),
				policy.gardens.exists.where({
					id: membership.gardenId,
					editorIds: { contains: session.userId }
				}),
				policy.gardens.exists.where({
					id: membership.gardenId,
					viewerIds: { contains: session.userId }
				})
			])
		);
		policy.gardenMemberships.allowInsert.where((membership) =>
			policy.gardens.exists.where({
				id: membership.gardenId,
				adminIds: { contains: session.userId }
			})
		);
		policy.gardenMemberships.allowUpdate.where((membership) =>
			policy.gardens.exists.where({
				id: membership.gardenId,
				adminIds: { contains: session.userId }
			})
		);
		policy.gardenMemberships.allowDelete.where((membership) =>
			policy.gardens.exists.where({
				id: membership.gardenId,
				adminIds: { contains: session.userId }
			})
		);
	});
}
