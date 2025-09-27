import { type ControllerContext } from '../controller.js';
import { AppError } from '../errors.js';
import {
	type Geometry,
	type GeometryCreateCommand,
	GeometryHistoryCreateCommand,
	type GeometryUpdateCommand,
	type LocationCreateCommand,
	type LocationHistory,
	type LocationHistoryUpdateCommand,
	type LocationUpdateCommand,
	type PlantingAreaCreateCommand,
	type PlantingAreaUpdateCommand,
	type TriplitTransaction,
	type Workspace,
	type WorkspaceCreateCommand,
	type WorkspaceUpdateCommand,
	historySelectDay
} from '../index.js';
import { slugify } from '../utils/index.js';

/** Helpers. */

/**
 * Insert a geometry into the database.
 * @param gardenId The ID of the garden.
 * @param data The geometry create command.
 * @param transaction The database transaction.
 * @returns The geometry after insertion.
 */
export async function geometryCreate(
	gardenId: string,
	data: GeometryCreateCommand,
	transaction: TriplitTransaction
): Promise<Omit<Geometry, 'linesCoordinates'>> {
	const coordinateIds: string[] = [];
	if (data.linesCoordinates && data.type === 'LINES') {
		for (const point of data.linesCoordinates) {
			const coordinate = await transaction.insert('coordinates', {
				gardenId: gardenId,
				x: point.x,
				y: point.y
			});
			coordinateIds.push(coordinate.id);
		}
	}

	const geometry: Omit<Geometry, 'id' | 'linesCoordinates'> = {
		gardenId: gardenId,
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
		linesCoordinateIds: new Set(coordinateIds),
		linesClosed: data.linesClosed
	};

	return await transaction.insert('geometries', geometry);
}

/**
 * Given a geometry partial object, which is a geometry object
 * where all values (including those of the nested attribute objects)
 * are optional, add these updated to Triplit.
 * @param id The ID of the geometry to update.
 * @param newGeometry The attributes to update.
 */
export async function geometryUpdate(
	id: string,
	data: GeometryUpdateCommand,
	ctx: ControllerContext
) {
	const geometry = await ctx.triplit.fetchOne(ctx.triplit.query('geometries').Id(id));
	if (!geometry) {
		throw new AppError('Geometry does not exist.', {
			nonFormErrors: ['Failed to update object geometry.']
		});
	}

	if (data.delete) {
		await ctx.triplit.delete('geometries', id);
		return;
	}

	await ctx.triplit.transact(async (transaction) => {
		/**
		 * The lines geometry update is a little trickier to handle
		 * because the points are connected via a relation.
		 * The new geometry may have the same number of points,
		 * or it may have more or less.
		 * The approach taken is to calculate the difference in the number
		 * of coordinates between the new list and the old, delete any
		 * coordinates that are unused, modify the rest, then add any
		 * new coordinates that need to be added.
		 */
		let existingCoordinateIds = [...geometry.linesCoordinateIds];
		if (data.linesCoordinates) {
			const newCoordinatesCount = data.linesCoordinates.length;

			/** Update existing coordinates. */
			const minLength = Math.min(existingCoordinateIds.length, newCoordinatesCount);
			for (let i = 0; i < minLength; i++) {
				const coordinateId = existingCoordinateIds[i];
				await transaction.update('coordinates', coordinateId, (coordinate) => {
					if (data.linesCoordinates) {
						coordinate.x = data.linesCoordinates[i].x;
						coordinate.y = data.linesCoordinates[i].y;
					}
				});
			}

			/** Delete excess coordinates if new list is shorter. */
			if (existingCoordinateIds.length > newCoordinatesCount) {
				const coordinatesToDelete = existingCoordinateIds.slice(newCoordinatesCount);
				for (const coordinateId of coordinatesToDelete) {
					await transaction.delete('coordinates', coordinateId);
				}
				existingCoordinateIds = existingCoordinateIds.slice(0, newCoordinatesCount);
			}

			/** Add new coordinates if new list is longer. */
			if (newCoordinatesCount > existingCoordinateIds.length) {
				const newPoints = data.linesCoordinates.slice(existingCoordinateIds.length);
				for (const point of newPoints) {
					const coordinate = await transaction.insert('coordinates', {
						gardenId: geometry.gardenId,
						x: point.x,
						y: point.y
					});
					existingCoordinateIds.push(coordinate.id);
				}
			}
		}

		await transaction.update('geometries', geometry.id, (geometry) => {
			if (data.type) {
				geometry.type = data.type;
			}
			if (data.date) {
				geometry.date = data.date;
			}
			if (data.scaleFactor) {
				geometry.scaleFactor = data.scaleFactor;
			}
			if (data.rotation) {
				geometry.rotation = data.rotation;
			}
			if (data.rectangleLength) {
				geometry.rectangleLength = data.rectangleLength;
			}
			if (data.rectangleWidth) {
				geometry.rectangleWidth = data.rectangleWidth;
			}
			if (data.polygonNumSides) {
				geometry.polygonNumSides = data.polygonNumSides;
			}
			if (data.polygonRadius) {
				geometry.polygonRadius = data.polygonRadius;
			}
			if (data.ellipseLength) {
				geometry.ellipseLength = data.ellipseLength;
			}
			if (data.ellipseWidth) {
				geometry.ellipseWidth = data.ellipseWidth;
			}
			if (data.linesCoordinates) {
				geometry.linesCoordinateIds = new Set(existingCoordinateIds);
			}
			if (data.linesClosed) {
				geometry.linesClosed = data.linesClosed;
			}
		});
	});
}

export async function geometryHistoryExtend(
	id: string,
	date: Date,
	ctx: ControllerContext
) {
	const geometryHistory = await ctx.triplit.fetchOne(
		ctx.triplit
			.query('geometryHistories')
			.Id(id)
			.Include('geometries', (rel) => rel('geometries').Include('linesCoordinates'))
	);
	if (!geometryHistory) {
		throw new AppError('Geometry history does not exist.', {
			nonFormErrors: ['Failed to update object geometry.']
		});
	}

	const latestGeometry =
		geometryHistory.geometries[geometryHistory.geometries.length - 1];
	latestGeometry.date = date;
	await ctx.triplit.transact(async (transaction) => {
		await geometryCreate(geometryHistory.gardenId, latestGeometry, transaction);
	});
}

export async function geometryHistoryCreate(
	data: GeometryHistoryCreateCommand,
	ctx: ControllerContext
) {
	//const geometries =
}

/**
 * Insert a new location history into the database.
 * @param data The location create command.
 * @param transaction The database transaction.
 * @returns The location history after insertion.
 */
export async function locationHistoryCreate(
	data: LocationCreateCommand,
	transaction: TriplitTransaction
): Promise<Omit<LocationHistory, 'locations'>> {
	const location = await transaction.insert('locations', {
		gardenId: data.gardenId,
		workspaceId: data.workspaceId,
		x: data.coordinate.x,
		y: data.coordinate.y,
		date: data.date
	});
	return await transaction.insert('locationHistories', {
		gardenId: data.gardenId,
		locationIds: new Set([location.id]),
		workspaceIds: new Set([data.workspaceId])
	});
}

/**
 * Updates or deletes a single location.
 * @param id The ID of the location.
 * @param data The location update command.
 */
export async function locationUpdate(
	id: string,
	data: LocationUpdateCommand,
	ctx: ControllerContext
) {
	const location = await ctx.triplit.fetchOne(ctx.triplit.query('locations').Id(id));
	if (!location) {
		throw new AppError('Location does not exist.', {
			nonFormErrors: ['Failed to update object location.']
		});
	}

	if (data.delete) {
		await ctx.triplit.delete('locations', id);
		return;
	}
	await ctx.triplit.update('locations', id, (location) => {
		if (data.coordinate) {
			location.x = data.coordinate.x;
			location.y = data.coordinate.y;
		}
		if (data.date) {
			location.date = data.date;
		}
		if (data.workspaceId) {
			location.workspaceId = data.workspaceId;
		}
	});
}

/**
 * Updates a location history with a new position.
 * If a position already exists in this location history
 * at the same day at the given date, that location is updated.
 * If not, a new location is created.
 * @param data The history update command.
 */
export async function locationHistoryUpdate(
	data: LocationHistoryUpdateCommand,
	ctx: ControllerContext
) {
	const locationHistory = await ctx.triplit.fetchOne(
		ctx.triplit.query('locationHistories').Id(data.id).Include('locations')
	);
	if (!locationHistory) {
		throw new AppError('Location history does not exist.', {
			nonFormErrors: ['Failed to update object location.']
		});
	}

	/** If a location already exists at the given day, update it. */
	const existingLocation = historySelectDay(locationHistory.locations, data.date);
	if (existingLocation) {
		await ctx.triplit.update('locations', existingLocation.id, (location) => {
			location.x = data.coordinate.x;
			location.y = data.coordinate.y;
		});

		/** If no location exists, create a new one. */
	} else {
		await ctx.triplit.transact(async (transaction) => {
			const location = await transaction.insert('locations', {
				gardenId: locationHistory.gardenId,
				workspaceId: data.workspaceId,
				x: data.coordinate.x,
				y: data.coordinate.y,
				date: data.date
			});
			await transaction.update(
				'locationHistories',
				locationHistory.id,
				(locationHistory) => {
					locationHistory.locationIds.add(location.id);
					if (!locationHistory.workspaceIds.has(data.workspaceId)) {
						locationHistory.workspaceIds.add(data.workspaceId);
					}
				}
			);
		});
	}
}

export async function locationHistoryExtend(
	id: string,
	data: {
		date: Date;
	},
	ctx: ControllerContext
) {
	const locationHistory = await ctx.triplit.fetchOne(
		ctx.triplit.query('locationHistories').Id(id).Include('locations')
	);
	if (!locationHistory) {
		throw new AppError('Location history does not exist.', {
			nonFormErrors: ['Failed to update object location.']
		});
	}

	const nearestLocation = historySelectDay(locationHistory.locations, data.date) ||
		locationHistory.locations[locationHistory.locations.length - 1] || { x: 0, y: 0 };
	await ctx.triplit.transact(async (transaction) => {
		const location = await transaction.insert('locations', {
			gardenId: locationHistory.gardenId,
			workspaceId: nearestLocation.workspaceId,
			x: nearestLocation.x,
			y: nearestLocation.y,
			date: data.date
		});
		await transaction.update('locationHistories', id, (locationHistory) => {
			locationHistory.locationIds.add(location.id);
		});
	});
}

/** Creates a new workspace in a garden. */
export async function workspaceCreate(
	data: WorkspaceCreateCommand,
	ctx: ControllerContext
): Promise<Workspace> {
	/** Retrieve client and authorize. */
	await ctx.requireRole(data.gardenId, 'WorkspaceCreate');

	/** Generate workspace slug from name. */
	const workspaceSlug = slugify(data.name);

	/** Validate garden-scoped unique workspace slug requirement. */
	const existingWorkspace = await ctx.triplit.fetchOne(
		ctx.triplit.query('workspaces').Where([
			['gardenId', '=', data.gardenId],
			['slug', '=', workspaceSlug]
		])
	);
	if (existingWorkspace) {
		throw new AppError('Workspace slug already exists.', {
			fieldErrors: { name: ['This workspace name already exists in this garden.'] }
		});
	}

	/** Add the workspace */
	return await ctx.triplit.insert('workspaces', {
		gardenId: data.gardenId,
		name: data.name,
		slug: workspaceSlug,
		description: data.description
	});
}

/** Updates a new workspace in a garden. */
export async function workspaceUpdate(
	gardenId: string,
	id: string,
	data: WorkspaceUpdateCommand,
	ctx: ControllerContext
) {
	/** Retrieve client and authorize. */
	await ctx.requireRole(gardenId, 'WorkspaceUpdate');

	/** Generate workspace slug from name. */
	let newSlug: string | undefined;
	if (data.name) {
		/** Validate garden-scoped unique workspace slug requirement. */
		newSlug = slugify(data.name);
		const existingWorkspace = await ctx.triplit.fetchOne(
			ctx.triplit.query('workspaces').Where([
				['gardenId', '=', id],
				['slug', '=', newSlug]
			])
		);
		if (existingWorkspace) {
			throw new AppError('Workspace slug already exists.', {
				fieldErrors: { name: ['This workspace name already exists in this garden.'] }
			});
		}
	}

	/** Update the workspace */
	await ctx.triplit.update('workspaces', id, (workspace) => {
		if (data.name && newSlug) {
			workspace.name = data.name;
			workspace.slug = newSlug;
		}
		if (data.description) {
			workspace.description = data.description;
		}
	});
}

/** Creates a new planting area in a workspace. */
export async function plantingAreaCreate(
	data: PlantingAreaCreateCommand,
	ctx: ControllerContext
) {
	const { garden } = await ctx.requireRole(data.gardenId, 'PlantingAreaCreate');

	/** Retrieve workspace. */
	const workspace = await ctx.triplit.fetchOne(
		ctx.triplit.query('workspaces').Id(data.workspaceId)
	);
	if (workspace == null) {
		throw new AppError(`Failed to retrieve workspace ${data.workspaceId}`, {
			nonFormErrors: ['Failed to retrieve workspace.']
		});
	}

	await ctx.triplit.transact(async (transaction) => {
		/** Persist geometry. */
		const geometry = await geometryCreate(data.gardenId, data.geometry, transaction);

		/** Persist locations. */
		const locationHistory = await locationHistoryCreate(data.location, transaction);

		/** Persist planting area. */
		await transaction.insert('plantingAreas', {
			gardenId: garden.id,
			name: data.name,
			description: data.description || '',
			geometryId: geometry.id,
			locationHistoryId: locationHistory.id,
			depth: data.depth
		});
	});
}

export async function plantingAreaUpdate(
	id: string,
	data: PlantingAreaUpdateCommand,
	ctx: ControllerContext
) {
	/** Retrieve planting area. */
	const plantingArea = await ctx.triplit.fetchOne(
		ctx.triplit.query('plantingAreas').Id(id)
	);
	if (plantingArea == null) {
		throw new AppError(`Failed to retrieve planting area ${id}`, {
			nonFormErrors: ['Failed to retrieve planting area.']
		});
	}

	await ctx.triplit.update('plantingAreas', id, (plantingArea) => {
		if (data.name) {
			plantingArea.name = data.name;
		}
		if (data.description) {
			plantingArea.description = data.description;
		}
		if (data.depth) {
			plantingArea.depth = data.depth;
		}
	});
}
