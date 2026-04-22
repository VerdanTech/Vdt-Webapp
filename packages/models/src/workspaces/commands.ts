import { z } from 'jazz-tools';
import { AppError, zodErrorToAppErrors } from '../errors.js';
import fields from './fields.js';
import * as schema from './schema.js'
import { commonFields } from '../commands.js';
import { historySelectDay } from './utils.js';

export const GeometryCreateCommandSchema = z.object({
	date: fields.geometryDateField,
	scaleFactor: fields.geometryScaleFactorField,
	rotation: fields.geometryRotationField,
	attributes: z.discriminatedUnion('type', [
		z.object({ type: z.literal('RECTANGLE'), rectangleLength: fields.geometryRectangleLengthField, rectangleWidth: fields.geometryRectangleWidthField }),
		z.object({ type: z.literal('ELLIPSE'), ellipseLength: fields.geometryEllipseLengthField, ellipseWidth: fields.geometryEllipseWidthField }),
		z.object({ type: z.literal('POLYGON'), polygonNumSides: fields.geometryPolygonNumSidesField, polygonRadius: fields.geometryPolygonRadiusField }),
		z.object({ type: z.literal('LINES'), linesCoordinates: fields.geometryLinesCoordinatesField, linesClosed: fields.geometryLinesClosedField })
	])
});
export type GeometryCreateCommand = z.infer<typeof GeometryCreateCommandSchema>;

export const GeometryUpdateCommandSchema = GeometryCreateCommandSchema.partial();
export type GeometryUpdateCommand = z.infer<typeof GeometryUpdateCommandSchema>;

/**
 * Location
 */

export const LocationCreateCommandSchema = z.object({
	date: fields.locationDateField,
	coordinate: fields.coordinateField,
	workspace: commonFields.schemaIdField
});
export type LocationCreateCommand = z.infer<typeof LocationCreateCommandSchema>;

/**
 * Creates a location in the object history.
 * Allows overwriting or throwing an exception if a location already exists at that day.
 * @param history The object history to update.
 * @param command The new location to create.
 * @param throwOnOverwrite If false and a location exists at the given day, it will be overwritten,
 * otherwise an exception will be raised.
 */
export function locationCreate(
	history: schema.ObjectHistory,
	command: LocationCreateCommand,
	throwOnOverwrite: boolean
) {
	const validated = LocationCreateCommandSchema.safeParse(command);
	if (!validated.success) {
		throw new AppError('Invalid coordinate.', zodErrorToAppErrors(validated.error));
	}

	const existing = historySelectDay([...history.locations], command.date);

	if (existing) {
		if (throwOnOverwrite) {
			throw new AppError('Location creation command would overwrite an existing item.')
		} else {
			existing.$jazz.applyDiff(validated)
		}

	} else {
		history.locations.$jazz.push(
			schema.LocationSchema.create(
				validated,
				{ owner: history.$jazz.owner }
			)
		);
	}
}

export const LocationUpdateCommandSchema = z.object({
	date: fields.locationDateField,
	coordinate: fields.coordinateField.optional(),
	workspace: commonFields.schemaIdField.optional()
});
export type LocationUpdateCommand = z.infer<typeof LocationUpdateCommandSchema>;

export function locationUpdate(
	history: schema.ObjectHistory,
	command: LocationUpdateCommand,
	throwOnNotFound: boolean
) {
	const validated = LocationUpdateCommandSchema.safeParse(command);
	if(!validated.success) {
		throw new AppError('Invalid coordinate.', zodErrorToAppErrors(validated.error));
	}

	const existing = historySelectDay([...history.locations], command.date)

	if(existing) {
		existing.$jazz.applyDiff({
			coordinate: validated.data.coordinate,
			// Can you assign IDs like this?
			workspace: validated.data.workspace
		})
	} else if(throwOnNotFound) {
		throw new AppError('Location update command found no location at this date.')
	}
}



/**
 * Create a new workspace.
 */
export const WorkspaceCreateCommandSchema = z.object({
	name: fields.workspaceNameField,
	description: z.string().optional()
});
export type WorkspaceCreateInput = z.infer<typeof WorkspaceCreateCommandSchema>;

/**
 * Update a workspace.
 */
export const WorkspaceUpdateCommandSchema = z.object({
	name: fields.workspaceNameField.optional(),
	description: z.string().optional()
});
export type WorkspaceUpdateInput = z.infer<typeof WorkspaceUpdateCommandSchema>;



/** Partial update applied to an existing loaded Geometry CoValue. */
export type GeometryDiff = {
	date?: Date;
	scaleFactor?: number;
	rotation?: number;
	attributes?: schema.GeometryAttributes;
};

/** Partial update applied to an existing loaded Location CoValue. */
export type LocationDiff = {
	date?: Date;
	coordinate?: schema.Coordinate.partial();
};

/**
 * Create a new planting area.
 */
export const PlantingAreaCreateComandSchema = z.object({
	name: fields.plantingAreaNameField,
	description: z.string().optional(),
	depth: fields.plantingAreaDepthField,
	initialGeometry: GeometryCreateCommandSchema,
	initialLocation: z.object({
		coordinate: fields.coordinateField,
		date: z.date()
	})
});
export type PlantingAreaCreateInput = z.infer<typeof PlantingAreaCreateComandSchema>;

/**
 * Update a planting area.
 */
export const plantingAreaUpdateInputSchema = z.object({
	name: fields.plantingAreaNameField.optional(),
	description: z.string().optional(),
	depth: fields.plantingAreaDepthField.optional()
});
export type PlantingAreaUpdateInput = z.infer<typeof plantingAreaUpdateInputSchema>;









/** Commands. */