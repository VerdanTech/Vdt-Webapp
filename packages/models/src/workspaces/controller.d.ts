import { type ControllerContext } from '../controller.js';
import {
	type Geometry,
	type GeometryCreateCommand,
	GeometryHistoryCreateCommand,
	type GeometryHistoryUpdateCommand,
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
	type WorkspaceUpdateCommand
} from '../index.js';

/** Helpers. */
/**
 * Insert a geometry into the database.
 * @param gardenId The ID of the garden.
 * @param data The geometry create command.
 * @param transaction The database transaction.
 * @returns The geometry after insertion.
 */
export declare function geometryCreate(
	gardenId: string,
	data: GeometryCreateCommand,
	transaction: TriplitTransaction
): Promise<Omit<Geometry, 'linesCoordinates'>>;
/**
 * Given a geometry partial object, which is a geometry object
 * where all values (including those of the nested attribute objects)
 * are optional, add these updated to Triplit.
 * @param id The ID of the geometry to update.
 * @param newGeometry The attributes to update.
 */
export declare function geometryUpdate(
	id: string,
	data: GeometryUpdateCommand,
	ctx: ControllerContext
): Promise<void>;
export declare function geometryHistoryExtend(
	id: string,
	date: Date,
	ctx: ControllerContext
): Promise<void>;
export declare function geometryHistoryCreate(
	data: GeometryHistoryCreateCommand,
	ctx: ControllerContext
): Promise<void>;
/**
 * Updates a geometry history with a new geometry.
 * If a geometry already exists in this location history
 * at the same day at the given date, that geometry is updated.
 * If not, a new geometry is created.
 * @param data The history update command.
 */
export declare function geometryHistoryUpdate(
	data: GeometryHistoryUpdateCommand,
	ctx: ControllerContext
): Promise<void>;
/**
 * Insert a new location history into the database.
 * @param data The location create command.
 * @param transaction The database transaction.
 * @returns The location history after insertion.
 */
export declare function locationHistoryCreate(
	data: LocationCreateCommand,
	transaction: TriplitTransaction
): Promise<Omit<LocationHistory, 'locations'>>;
/**
 * Updates or deletes a single location.
 * @param id The ID of the location.
 * @param data The location update command.
 */
export declare function locationUpdate(
	id: string,
	data: LocationUpdateCommand,
	ctx: ControllerContext
): Promise<void>;
/**
 * Updates a location history with a new position.
 * If a position already exists in this location history
 * at the same day at the given date, that location is updated.
 * If not, a new location is created.
 * @param data The history update command.
 */
export declare function locationHistoryUpdate(
	data: LocationHistoryUpdateCommand,
	ctx: ControllerContext
): Promise<void>;
export declare function locationHistoryExtend(
	id: string,
	data: {
		date: Date;
	},
	ctx: ControllerContext
): Promise<void>;
/** Creates a new workspace in a garden. */
export declare function workspaceCreate(
	data: WorkspaceCreateCommand,
	ctx: ControllerContext
): Promise<Workspace>;
/** Updates a new workspace in a garden. */
export declare function workspaceUpdate(
	gardenId: string,
	id: string,
	data: WorkspaceUpdateCommand,
	ctx: ControllerContext
): Promise<void>;
/** Creates a new planting area in a workspace. */
export declare function plantingAreaCreate(
	data: PlantingAreaCreateCommand,
	ctx: ControllerContext
): Promise<void>;
export declare function plantingAreaUpdate(
	id: string,
	data: PlantingAreaUpdateCommand,
	ctx: ControllerContext
): Promise<void>;
//# sourceMappingURL=controller.d.ts.map
