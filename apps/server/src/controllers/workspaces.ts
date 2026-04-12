import { eq, inArray, sql } from 'drizzle-orm';

import {
	AppError,
	type GeometryCreateCommand,
	type GeometryHistoryUpdateCommand,
	type GeometryUpdateCommand,
	type LocationCreateCommand,
	type LocationHistoryUpdateCommand,
	type LocationUpdateCommand,
	type PlantingAreaCreateCommand,
	type PlantingAreaUpdateCommand,
	type WorkspaceCreateCommand,
	type WorkspaceUpdateCommand,
	geometries,
	geometryHistories,
	historySelectDay,
	locationHistories,
	locations,
	plantingAreas,
	slugify,
	workspaces
} from '@vdg-webapp/models';

import { type Db } from '../db/index.js';
import { type ServerContext, requireGardenRole } from './context.js';

/** ── Geometry helpers ── */

export async function geometryCreate(
	db: Db,
	gardenId: string,
	data: GeometryCreateCommand
): Promise<{ id: string; txid: number }> {
	return db.transaction(async (tx) => {
		const [geometry] = await tx
			.insert(geometries)
			.values({
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
				linesCoordinates: data.type === 'LINES' ? data.linesCoordinates : [],
				linesClosed: data.linesClosed
			})
			.returning();

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { id: geometry.id, txid: parseInt(txid) };
	});
}

export async function geometryUpdate(
	db: Db,
	id: string,
	data: GeometryUpdateCommand
): Promise<{ txid: number }> {
	const existing = await db.query.geometries.findFirst({
		where: eq(geometries.id, id),
		columns: { id: true }
	});
	if (!existing) {
		throw new AppError('Geometry does not exist.', {
			nonFormErrors: ['Failed to update object geometry.']
		});
	}

	return db.transaction(async (tx) => {
		if (data.delete) {
			await tx.delete(geometries).where(eq(geometries.id, id));
		} else {
			await tx
				.update(geometries)
				.set({
					...(data.type !== undefined && { type: data.type }),
					...(data.date !== undefined && { date: data.date }),
					...(data.scaleFactor !== undefined && { scaleFactor: data.scaleFactor }),
					...(data.rotation !== undefined && { rotation: data.rotation }),
					...(data.rectangleLength !== undefined && {
						rectangleLength: data.rectangleLength
					}),
					...(data.rectangleWidth !== undefined && {
						rectangleWidth: data.rectangleWidth
					}),
					...(data.polygonNumSides !== undefined && {
						polygonNumSides: data.polygonNumSides
					}),
					...(data.polygonRadius !== undefined && {
						polygonRadius: data.polygonRadius
					}),
					...(data.ellipseLength !== undefined && {
						ellipseLength: data.ellipseLength
					}),
					...(data.ellipseWidth !== undefined && { ellipseWidth: data.ellipseWidth }),
					/** linesCoordinates is stored inline — a single update replaces the whole array. */
					...(data.linesCoordinates !== undefined && {
						linesCoordinates: data.linesCoordinates
					}),
					...(data.linesClosed !== undefined && { linesClosed: data.linesClosed })
				})
				.where(eq(geometries.id, id));
		}

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}

export async function geometryHistoryUpdate(
	db: Db,
	data: GeometryHistoryUpdateCommand
): Promise<{ txid: number }> {
	const history = await db.query.geometryHistories.findFirst({
		where: eq(geometryHistories.id, data.id),
		columns: { id: true, gardenId: true, geometryIds: true }
	});
	if (!history) {
		throw new AppError('Geometry history does not exist.', {
			nonFormErrors: ['Failed to update object geometry.']
		});
	}

	/** Fetch existing geometries to find one on the same day. */
	const existingGeoms =
		history.geometryIds.length > 0
			? await db.query.geometries.findMany({
					where: inArray(geometries.id, history.geometryIds),
					columns: { id: true, date: true }
				})
			: [];

	const sameDay = historySelectDay(existingGeoms, data.date);

	return db.transaction(async (tx) => {
		if (sameDay) {
			/** Update the existing geometry on this day. */
			await geometryUpdate(db, sameDay.id, data.geometry);
		} else {
			/** Create a new geometry and add it to the history. */
			const [newGeom] = await tx
				.insert(geometries)
				.values({
					gardenId: history.gardenId,
					type: data.geometry.type,
					date: data.date,
					scaleFactor: data.geometry.scaleFactor,
					rotation: data.geometry.rotation,
					rectangleLength: data.geometry.rectangleLength,
					rectangleWidth: data.geometry.rectangleWidth,
					polygonNumSides: data.geometry.polygonNumSides,
					polygonRadius: data.geometry.polygonRadius,
					ellipseLength: data.geometry.ellipseLength,
					ellipseWidth: data.geometry.ellipseWidth,
					linesCoordinates:
						data.geometry.type === 'LINES' ? data.geometry.linesCoordinates : [],
					linesClosed: data.geometry.linesClosed
				})
				.returning();

			await tx
				.update(geometryHistories)
				.set({
					geometryIds: sql`array_append(${geometryHistories.geometryIds}, ${newGeom.id})`
				})
				.where(eq(geometryHistories.id, history.id));
		}

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}

/** ── Location helpers ── */

export async function locationHistoryCreate(
	db: Db,
	data: LocationCreateCommand
): Promise<{ id: string; txid: number }> {
	return db.transaction(async (tx) => {
		const [location] = await tx
			.insert(locations)
			.values({
				gardenId: data.gardenId,
				workspaceId: data.workspaceId,
				x: data.coordinate.x,
				y: data.coordinate.y,
				date: data.date
			})
			.returning();

		const [history] = await tx
			.insert(locationHistories)
			.values({
				gardenId: data.gardenId,
				locationIds: [location.id]
			})
			.returning();

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { id: history.id, txid: parseInt(txid) };
	});
}

export async function locationUpdate(
	db: Db,
	id: string,
	data: LocationUpdateCommand
): Promise<{ txid: number }> {
	const existing = await db.query.locations.findFirst({
		where: eq(locations.id, id),
		columns: { id: true }
	});
	if (!existing) {
		throw new AppError('Location does not exist.', {
			nonFormErrors: ['Failed to update object location.']
		});
	}

	return db.transaction(async (tx) => {
		if (data.delete) {
			await tx.delete(locations).where(eq(locations.id, id));
		} else {
			await tx
				.update(locations)
				.set({
					...(data.coordinate && { x: data.coordinate.x, y: data.coordinate.y }),
					...(data.date && { date: data.date }),
					...(data.workspaceId && { workspaceId: data.workspaceId })
				})
				.where(eq(locations.id, id));
		}

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}

export async function locationHistoryUpdate(
	db: Db,
	data: LocationHistoryUpdateCommand
): Promise<{ txid: number }> {
	const history = await db.query.locationHistories.findFirst({
		where: eq(locationHistories.id, data.id),
		columns: { id: true, gardenId: true, locationIds: true }
	});
	if (!history) {
		throw new AppError('Location history does not exist.', {
			nonFormErrors: ['Failed to update object location.']
		});
	}

	const existingLocs =
		history.locationIds.length > 0
			? await db.query.locations.findMany({
					where: inArray(locations.id, history.locationIds),
					columns: { id: true, date: true }
				})
			: [];

	const sameDay = historySelectDay(existingLocs, data.date);

	return db.transaction(async (tx) => {
		if (sameDay) {
			await tx
				.update(locations)
				.set({ x: data.coordinate.x, y: data.coordinate.y })
				.where(eq(locations.id, sameDay.id));
		} else {
			const [newLoc] = await tx
				.insert(locations)
				.values({
					gardenId: history.gardenId,
					workspaceId: data.workspaceId,
					x: data.coordinate.x,
					y: data.coordinate.y,
					date: data.date
				})
				.returning();

			await tx
				.update(locationHistories)
				.set({
					locationIds: sql`array_append(${locationHistories.locationIds}, ${newLoc.id})`
				})
				.where(eq(locationHistories.id, history.id));
		}

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}

/** Returns the distinct workspace IDs referenced by a location history. */
export async function getWorkspaceIdsForLocationHistory(
	db: Db,
	historyId: string
): Promise<string[]> {
	const history = await db.query.locationHistories.findFirst({
		where: eq(locationHistories.id, historyId),
		columns: { locationIds: true }
	});
	if (!history || history.locationIds.length === 0) return [];

	const rows = await db
		.selectDistinct({ workspaceId: locations.workspaceId })
		.from(locations)
		.where(inArray(locations.id, history.locationIds));

	return rows.map((r) => r.workspaceId);
}

/** ── Workspace commands ── */

export async function workspaceCreate(
	data: WorkspaceCreateCommand,
	ctx: ServerContext
): Promise<{ id: string; txid: number }> {
	await requireGardenRole(ctx, data.gardenId, 'WorkspaceCreate');

	const slug = slugify(data.name);

	const existing = await ctx.db.query.workspaces.findFirst({
		where: (w, { and, eq }) =>
			and(eq(w.gardenId, data.gardenId), eq(w.slug, slug)),
		columns: { id: true }
	});
	if (existing) {
		throw new AppError('Workspace slug already exists.', {
			fieldErrors: { name: ['This workspace name already exists in this garden.'] }
		});
	}

	return ctx.db.transaction(async (tx) => {
		const [workspace] = await tx
			.insert(workspaces)
			.values({
				gardenId: data.gardenId,
				name: data.name,
				slug,
				description: data.description ?? ''
			})
			.returning();

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { id: workspace.id, txid: parseInt(txid) };
	});
}

export async function workspaceUpdate(
	gardenId: string,
	id: string,
	data: WorkspaceUpdateCommand,
	ctx: ServerContext
): Promise<{ txid: number }> {
	await requireGardenRole(ctx, gardenId, 'WorkspaceUpdate');

	let newSlug: string | undefined;
	if (data.name) {
		newSlug = slugify(data.name);
		const existing = await ctx.db.query.workspaces.findFirst({
			where: (w, { and, eq }) =>
				and(eq(w.gardenId, gardenId), eq(w.slug, newSlug!)),
			columns: { id: true }
		});
		if (existing) {
			throw new AppError('Workspace slug already exists.', {
				fieldErrors: { name: ['This workspace name already exists in this garden.'] }
			});
		}
	}

	return ctx.db.transaction(async (tx) => {
		await tx
			.update(workspaces)
			.set({
				...(data.name && newSlug && { name: data.name, slug: newSlug }),
				...(data.description !== undefined && { description: data.description })
			})
			.where(eq(workspaces.id, id));

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}

/** ── Planting area commands ── */

export async function plantingAreaCreate(
	data: PlantingAreaCreateCommand,
	ctx: ServerContext
): Promise<{ id: string; txid: number }> {
	await requireGardenRole(ctx, data.gardenId, 'PlantingAreaCreate');

	const workspace = await ctx.db.query.workspaces.findFirst({
		where: eq(workspaces.id, data.workspaceId),
		columns: { id: true }
	});
	if (!workspace) {
		throw new AppError(`Workspace ${data.workspaceId} not found.`, {
			nonFormErrors: ['Failed to retrieve workspace.']
		});
	}

	return ctx.db.transaction(async (tx) => {
		const [geometry] = await tx
			.insert(geometries)
			.values({
				gardenId: data.gardenId,
				type: data.geometry.type,
				date: data.geometry.date,
				scaleFactor: data.geometry.scaleFactor,
				rotation: data.geometry.rotation,
				rectangleLength: data.geometry.rectangleLength,
				rectangleWidth: data.geometry.rectangleWidth,
				polygonNumSides: data.geometry.polygonNumSides,
				polygonRadius: data.geometry.polygonRadius,
				ellipseLength: data.geometry.ellipseLength,
				ellipseWidth: data.geometry.ellipseWidth,
				linesCoordinates:
					data.geometry.type === 'LINES' ? data.geometry.linesCoordinates : [],
				linesClosed: data.geometry.linesClosed
			})
			.returning();

		const [location] = await tx
			.insert(locations)
			.values({
				gardenId: data.gardenId,
				workspaceId: data.workspaceId,
				x: data.location.coordinate.x,
				y: data.location.coordinate.y,
				date: data.location.date
			})
			.returning();

		const [locationHistory] = await tx
			.insert(locationHistories)
			.values({ gardenId: data.gardenId, locationIds: [location.id] })
			.returning();

		const [area] = await tx
			.insert(plantingAreas)
			.values({
				gardenId: data.gardenId,
				name: data.name,
				description: data.description ?? '',
				geometryId: geometry.id,
				locationHistoryId: locationHistory.id,
				depth: data.depth
			})
			.returning();

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { id: area.id, txid: parseInt(txid) };
	});
}

export async function plantingAreaUpdate(
	id: string,
	data: PlantingAreaUpdateCommand,
	ctx: ServerContext
): Promise<{ txid: number }> {
	const area = await ctx.db.query.plantingAreas.findFirst({
		where: eq(plantingAreas.id, id),
		columns: { id: true, gardenId: true }
	});
	if (!area) {
		throw new AppError(`Planting area ${id} not found.`, {
			nonFormErrors: ['Failed to retrieve planting area.']
		});
	}

	return ctx.db.transaction(async (tx) => {
		await tx
			.update(plantingAreas)
			.set({
				...(data.name !== undefined && { name: data.name }),
				...(data.description !== undefined && { description: data.description }),
				...(data.depth !== undefined && { depth: data.depth })
			})
			.where(eq(plantingAreas.id, id));

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			sql`SELECT pg_current_xact_id()::xid::text AS txid`
		);
		return { txid: parseInt(txid) };
	});
}
