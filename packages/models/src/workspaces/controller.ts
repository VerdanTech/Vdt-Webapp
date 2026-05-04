import type { Db } from 'jazz-tools/backend';

import { type ControllerContext } from '../controller.js';
import { AppError } from '../errors.js';
import {
	type Geometry,
	type GeometryCreateCommand,
	type GeometryHistoryCreateCommand,
	type GeometryHistoryUpdateCommand,
	type GeometryUpdateCommand,
	type LocationCreateCommand,
	type LocationHistory,
	type LocationHistoryUpdateCommand,
	type LocationUpdateCommand,
	type PlantingAreaCreateCommand,
	type PlantingAreaUpdateCommand,
	type Workspace,
	type WorkspaceCreateCommand,
	type WorkspaceUpdateCommand,
	historySelectDay
} from '../index.js';
import { slugify } from '../utils/index.js';

type DbTransaction = ReturnType<Db['beginTransaction']>;

/** Helpers. */

/**
 * Insert a geometry into the database within a transaction.
 * @param gardenId The ID of the garden.
 * @param data The geometry create command.
 * @param ctx Controller context.
 * @param tx The database transaction.
 * @returns The geometry after insertion.
 */
export function geometryCreate(
	gardenId: string,
	data: GeometryCreateCommand,
	ctx: ControllerContext,
	tx: DbTransaction
): Omit<Geometry, 'linesCoordinates'> {
	const coordinateIds: string[] = [];
	if (data.linesCoordinates && data.type === 'LINES') {
		for (const point of data.linesCoordinates) {
			const coordinate = tx.insert(ctx.jazz.coordinates, {
				gardenId,
				x: point.x,
				y: point.y
			});
			coordinateIds.push(coordinate.id);
		}
	}

	return tx.insert(ctx.jazz.geometries, {
		gardenId,
		type: data.type,
		date: data.date,
		scaleFactor: data.scaleFactor,
		rotation: data.rotation,
		rectangleLength: data.rectangleLength,
		rectangleWidth: data.rectangleWidth,
		polygonNumSides: data.polygonNumSides,
		polygonRadius: data.polygonRadius,
		ellipseLength: data.ellipseLength,
		ellipseWidth: data.ellipseWidth,
		linesCoordinateIds: coordinateIds,
		linesClosed: data.linesClosed
	});
}

/**
 * Given a geometry partial object, update the geometry in the database.
 * @param id The ID of the geometry to update.
 * @param data The attributes to update.
 * @param ctx Controller context.
 */
export async function geometryUpdate(
	id: string,
	data: GeometryUpdateCommand,
	ctx: ControllerContext
) {
	const geometry = await ctx.db.one(ctx.jazz.geometries.where({ id }));
	if (!geometry) {
		throw new AppError('Geometry does not exist.', {
			nonFormErrors: ['Failed to update object geometry.']
		});
	}

	if (data.delete) {
		ctx.db.delete(ctx.jazz.geometries, id);
		return;
	}

	const tx = ctx.db.beginTransaction(ctx.jazz.geometries);

	/**
	 * For LINES geometry, reconcile the coordinate array:
	 * update existing, delete excess, insert new additions.
	 */
	let coordinateIds = [...geometry.linesCoordinateIds];
	if (data.linesCoordinates) {
		const newCount = data.linesCoordinates.length;
		const minLength = Math.min(coordinateIds.length, newCount);

		for (let i = 0; i < minLength; i++) {
			tx.update(ctx.jazz.coordinates, coordinateIds[i], {
				x: data.linesCoordinates[i].x,
				y: data.linesCoordinates[i].y
			});
		}

		if (coordinateIds.length > newCount) {
			for (const coordinateId of coordinateIds.slice(newCount)) {
				tx.delete(ctx.jazz.coordinates, coordinateId);
			}
			coordinateIds = coordinateIds.slice(0, newCount);
		}

		if (newCount > coordinateIds.length) {
			for (const point of data.linesCoordinates.slice(coordinateIds.length)) {
				const coordinate = tx.insert(ctx.jazz.coordinates, {
					gardenId: geometry.gardenId,
					x: point.x,
					y: point.y
				});
				coordinateIds.push(coordinate.id);
			}
		}
	}

	tx.update(ctx.jazz.geometries, geometry.id, {
		...(data.type && { type: data.type }),
		...(data.date && { date: data.date }),
		...(data.scaleFactor && { scaleFactor: data.scaleFactor }),
		...(data.rotation && { rotation: data.rotation }),
		...(data.rectangleLength && { rectangleLength: data.rectangleLength }),
		...(data.rectangleWidth && { rectangleWidth: data.rectangleWidth }),
		...(data.polygonNumSides && { polygonNumSides: data.polygonNumSides }),
		...(data.polygonRadius && { polygonRadius: data.polygonRadius }),
		...(data.ellipseLength && { ellipseLength: data.ellipseLength }),
		...(data.ellipseWidth && { ellipseWidth: data.ellipseWidth }),
		...(data.linesCoordinates && { linesCoordinateIds: coordinateIds }),
		...(data.linesClosed !== undefined && { linesClosed: data.linesClosed })
	});

	tx.commit();
}

export async function geometryHistoryExtend(
	id: string,
	date: Date,
	ctx: ControllerContext
) {
	const geometryHistory = await ctx.db.one(ctx.jazz.geometryHistories.where({ id }));
	if (!geometryHistory) {
		throw new AppError('Geometry history does not exist.', {
			nonFormErrors: ['Failed to update object geometry.']
		});
	}

	/** TODO: Implement include-based geometry retrieval for extend. */
}

export async function geometryHistoryCreate(
	data: GeometryHistoryCreateCommand,
	ctx: ControllerContext
) {
	/** TODO: Implement geometry history creation. */
}

/**
 * Updates a geometry history with a new geometry.
 * If a geometry already exists at the same day as the given date, that geometry is updated.
 * If not, a new geometry is created.
 * @param data The history update command.
 * @param ctx Controller context.
 */
export async function geometryHistoryUpdate(
	data: GeometryHistoryUpdateCommand,
	ctx: ControllerContext
) {
	const geometryHistory = await ctx.db.one(
		ctx.jazz.geometryHistories.where({ id: data.id })
	);
	if (!geometryHistory) {
		throw new AppError('Geometry history does not exist.', {
			nonFormErrors: ['Failed to update object geometry.']
		});
	}

	/** Fetch all geometries referenced by this history. */
	const geometries =
		geometryHistory.geometryIds.length > 0
			? await ctx.db.all(
					ctx.jazz.geometries.where({ id: { in: geometryHistory.geometryIds } })
				)
			: [];

	const existingGeometry = historySelectDay(geometries, data.date);
	if (existingGeometry) {
		await geometryUpdate(existingGeometry.id, data.geometry, ctx);
	} else {
		const tx = ctx.db.beginTransaction(ctx.jazz.geometryHistories);
		const geometry = geometryCreate(geometryHistory.gardenId, data.geometry, ctx, tx);
		tx.update(ctx.jazz.geometryHistories, geometryHistory.id, {
			geometryIds: [...geometryHistory.geometryIds, geometry.id]
		});
		tx.commit();
	}
}

/**
 * Insert a new location history into the database within a transaction.
 * @param data The location create command.
 * @param ctx Controller context.
 * @param tx The database transaction.
 * @returns The location history after insertion.
 */
export function locationHistoryCreate(
	data: LocationCreateCommand,
	ctx: ControllerContext,
	tx: DbTransaction
): Omit<LocationHistory, 'locations'> {
	const location = tx.insert(ctx.jazz.locations, {
		gardenId: data.gardenId,
		workspaceId: data.workspaceId,
		x: data.coordinate.x,
		y: data.coordinate.y,
		date: data.date
	});
	return tx.insert(ctx.jazz.locationHistories, {
		gardenId: data.gardenId,
		locationIds: [location.id],
		workspaceIds: [data.workspaceId]
	});
}

/**
 * Updates or deletes a single location.
 * @param id The ID of the location.
 * @param data The location update command.
 * @param ctx Controller context.
 */
export async function locationUpdate(
	id: string,
	data: LocationUpdateCommand,
	ctx: ControllerContext
) {
	const location = await ctx.db.one(ctx.jazz.locations.where({ id }));
	if (!location) {
		throw new AppError('Location does not exist.', {
			nonFormErrors: ['Failed to update object location.']
		});
	}

	if (data.delete) {
		ctx.db.delete(ctx.jazz.locations, id);
		return;
	}

	ctx.db.update(ctx.jazz.locations, id, {
		...(data.coordinate && { x: data.coordinate.x, y: data.coordinate.y }),
		...(data.date && { date: data.date }),
		...(data.workspaceId && { workspaceId: data.workspaceId })
	});
}

/**
 * Updates a location history with a new position.
 * If a position already exists at the same day as the given date, that location is updated.
 * If not, a new location is created.
 * @param data The history update command.
 * @param ctx Controller context.
 */
export async function locationHistoryUpdate(
	data: LocationHistoryUpdateCommand,
	ctx: ControllerContext
) {
	const locationHistory = await ctx.db.one(
		ctx.jazz.locationHistories.where({ id: data.id })
	);
	if (!locationHistory) {
		throw new AppError('Location history does not exist.', {
			nonFormErrors: ['Failed to update object location.']
		});
	}

	const locations =
		locationHistory.locationIds.length > 0
			? await ctx.db.all(
					ctx.jazz.locations.where({ id: { in: locationHistory.locationIds } })
				)
			: [];

	const existingLocation = historySelectDay(locations, data.date);
	if (existingLocation) {
		ctx.db.update(ctx.jazz.locations, existingLocation.id, {
			x: data.coordinate.x,
			y: data.coordinate.y
		});
	} else {
		const tx = ctx.db.beginTransaction(ctx.jazz.locationHistories);
		const location = tx.insert(ctx.jazz.locations, {
			gardenId: locationHistory.gardenId,
			workspaceId: data.workspaceId,
			x: data.coordinate.x,
			y: data.coordinate.y,
			date: data.date
		});
		const updatedWorkspaceIds = locationHistory.workspaceIds.includes(data.workspaceId)
			? locationHistory.workspaceIds
			: [...locationHistory.workspaceIds, data.workspaceId];
		tx.update(ctx.jazz.locationHistories, locationHistory.id, {
			locationIds: [...locationHistory.locationIds, location.id],
			workspaceIds: updatedWorkspaceIds
		});
		tx.commit();
	}
}

export async function locationHistoryExtend(
	id: string,
	data: { date: Date },
	ctx: ControllerContext
) {
	const locationHistory = await ctx.db.one(ctx.jazz.locationHistories.where({ id }));
	if (!locationHistory) {
		throw new AppError('Location history does not exist.', {
			nonFormErrors: ['Failed to update object location.']
		});
	}

	const locations =
		locationHistory.locationIds.length > 0
			? await ctx.db.all(
					ctx.jazz.locations.where({ id: { in: locationHistory.locationIds } })
				)
			: [];

	const nearestLocation = historySelectDay(locations, data.date) ||
		locations[locations.length - 1] || { workspaceId: '', x: 0, y: 0 };

	const tx = ctx.db.beginTransaction(ctx.jazz.locationHistories);
	const location = tx.insert(ctx.jazz.locations, {
		gardenId: locationHistory.gardenId,
		workspaceId: nearestLocation.workspaceId,
		x: nearestLocation.x,
		y: nearestLocation.y,
		date: data.date
	});
	tx.update(ctx.jazz.locationHistories, id, {
		locationIds: [...locationHistory.locationIds, location.id]
	});
	tx.commit();
}

/** Creates a new workspace in a garden. */
export async function workspaceCreate(
	data: WorkspaceCreateCommand,
	ctx: ControllerContext
): Promise<Workspace> {
	await ctx.requireRole(data.gardenId, 'WorkspaceCreate');

	const workspaceSlug = slugify(data.name);

	const existingWorkspace = await ctx.db.one(
		ctx.jazz.workspaces.where({ gardenId: data.gardenId, slug: workspaceSlug })
	);
	if (existingWorkspace) {
		throw new AppError('Workspace slug already exists.', {
			fieldErrors: { name: ['This workspace name already exists in this garden.'] }
		});
	}

	return ctx.db.insert(ctx.jazz.workspaces, {
		gardenId: data.gardenId,
		name: data.name,
		slug: workspaceSlug,
		description: data.description
	}).value;
}

/** Updates a workspace in a garden. */
export async function workspaceUpdate(
	gardenId: string,
	id: string,
	data: WorkspaceUpdateCommand,
	ctx: ControllerContext
) {
	await ctx.requireRole(gardenId, 'WorkspaceUpdate');

	let newSlug: string | undefined;
	if (data.name) {
		newSlug = slugify(data.name);
		const existingWorkspace = await ctx.db.one(
			ctx.jazz.workspaces.where({ gardenId, slug: newSlug })
		);
		if (existingWorkspace) {
			throw new AppError('Workspace slug already exists.', {
				fieldErrors: { name: ['This workspace name already exists in this garden.'] }
			});
		}
	}

	ctx.db.update(ctx.jazz.workspaces, id, {
		...(data.name && newSlug && { name: data.name, slug: newSlug }),
		...(data.description && { description: data.description })
	});
}

/** Creates a new planting area in a workspace. */
export async function plantingAreaCreate(
	data: PlantingAreaCreateCommand,
	ctx: ControllerContext
) {
	const { garden } = await ctx.requireRole(data.gardenId, 'PlantingAreaCreate');

	const workspace = await ctx.db.one(
		ctx.jazz.workspaces.where({ id: data.workspaceId })
	);
	if (workspace == null) {
		throw new AppError(`Failed to retrieve workspace ${data.workspaceId}`, {
			nonFormErrors: ['Failed to retrieve workspace.']
		});
	}

	const tx = ctx.db.beginTransaction(ctx.jazz.plantingAreas);

	const geometry = geometryCreate(data.gardenId, data.geometry, ctx, tx);
	const locationHistory = locationHistoryCreate(data.location, ctx, tx);

	tx.insert(ctx.jazz.plantingAreas, {
		gardenId: garden.id,
		name: data.name,
		description: data.description || '',
		geometryId: geometry.id,
		locationHistoryId: locationHistory.id,
		depth: data.depth
	});

	tx.commit();
}

export async function plantingAreaUpdate(
	id: string,
	data: PlantingAreaUpdateCommand,
	ctx: ControllerContext
) {
	const plantingArea = await ctx.db.one(ctx.jazz.plantingAreas.where({ id }));
	if (plantingArea == null) {
		throw new AppError(`Failed to retrieve planting area ${id}`, {
			nonFormErrors: ['Failed to retrieve planting area.']
		});
	}

	ctx.db.update(ctx.jazz.plantingAreas, id, {
		...(data.name && { name: data.name }),
		...(data.description && { description: data.description }),
		...(data.depth !== undefined && { depth: data.depth })
	});
}
