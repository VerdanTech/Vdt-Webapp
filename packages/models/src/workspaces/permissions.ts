import { anyOf, schema as s } from 'jazz-tools';

import type { JazzApp } from '../schema.js';

export function constructPermissions(app: JazzApp) {
	s.definePermissions(app, ({ policy, session, allowedTo }) => {
		/* Coordinates - readable if garden is readable, writable by admins and editors. */
		policy.coordinates.allowRead.where(allowedTo.read('gardenId'));
		policy.coordinates.allowInsert.where((row) =>
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
		policy.coordinates.allowUpdate.where((row) =>
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
		policy.coordinates.allowDelete.where((row) =>
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

		/* Geometries - readable if garden is readable, writable by admins and editors. */
		policy.geometries.allowRead.where(allowedTo.read('gardenId'));
		policy.geometries.allowInsert.where((row) =>
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
		policy.geometries.allowUpdate.where((row) =>
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
		policy.geometries.allowDelete.where((row) =>
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

		/* GeometryHistories - readable if garden is readable, writable by admins and editors. */
		policy.geometryHistories.allowRead.where(allowedTo.read('gardenId'));
		policy.geometryHistories.allowInsert.where((row) =>
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
		policy.geometryHistories.allowUpdate.where((row) =>
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
		policy.geometryHistories.allowDelete.where((row) =>
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

		/* Locations - readable if garden is readable, writable by admins and editors. */
		policy.locations.allowRead.where(allowedTo.read('gardenId'));
		policy.locations.allowInsert.where((row) =>
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
		policy.locations.allowUpdate.where((row) =>
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
		policy.locations.allowDelete.where((row) =>
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

		/* LocationHistories - readable if garden is readable, writable by admins and editors. */
		policy.locationHistories.allowRead.where(allowedTo.read('gardenId'));
		policy.locationHistories.allowInsert.where((row) =>
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
		policy.locationHistories.allowUpdate.where((row) =>
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
		policy.locationHistories.allowDelete.where((row) =>
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

		/* PlantingAreas - readable if garden is readable, writable by admins only. */
		policy.plantingAreas.allowRead.where(allowedTo.read('gardenId'));
		policy.plantingAreas.allowInsert.where((row) =>
			policy.gardens.exists.where({
				id: row.gardenId,
				adminIds: { contains: session.userId }
			})
		);
		policy.plantingAreas.allowUpdate.where((row) =>
			policy.gardens.exists.where({
				id: row.gardenId,
				adminIds: { contains: session.userId }
			})
		);
		policy.plantingAreas.allowDelete.where((row) =>
			policy.gardens.exists.where({
				id: row.gardenId,
				adminIds: { contains: session.userId }
			})
		);

		/* Workspaces - readable if garden is readable, writable by admins only. */
		policy.workspaces.allowRead.where(allowedTo.read('gardenId'));
		policy.workspaces.allowInsert.where((row) =>
			policy.gardens.exists.where({
				id: row.gardenId,
				adminIds: { contains: session.userId }
			})
		);
		policy.workspaces.allowUpdate.where((row) =>
			policy.gardens.exists.where({
				id: row.gardenId,
				adminIds: { contains: session.userId }
			})
		);
		policy.workspaces.allowDelete.where((row) =>
			policy.gardens.exists.where({
				id: row.gardenId,
				adminIds: { contains: session.userId }
			})
		);
	});
}
