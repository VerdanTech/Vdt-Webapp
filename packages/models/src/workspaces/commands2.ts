import { co, type Account } from 'jazz-tools';

import { AppError, zodErrorToAppErrors } from '../errors.js';
import { GardenSchema } from '../gardens/schema.js';
import { GardenMembershipRoleEnumOptions } from '../gardens/fields.js';
import { requiredRole, type ActionType } from '../permissions.js';
import { slugify } from '../utils/index.js';
import {
	GeometrySchema,
	GeometryHistorySchema,
	LocationSchema,
	LocationHistorySchema,
	ObjectHistorySchema,
	PlantingAreaSchema,
	WorkspaceSchema,
	type Coordinate,
	type Geometry,
	type GeometryAttributes,
	type Location,
	type ObjectHistory,
	type PlantingArea,
	type Workspace
} from './schema.js';
import {
	coordinateValidation,
	geometryValidation,
	geometryDiffValidation,
	locationDiffValidation,
	plantingAreaCreateInputSchema,
	plantingAreaUpdateInputSchema,
	workspaceCreateInputSchema,
	workspaceUpdateInputSchema,
	type GeometryDiff,
	type LocationDiff,
	type PlantingAreaCreateInput,
	type PlantingAreaUpdateInput,
	type WorkspaceCreateInput,
	type WorkspaceUpdateInput
} from './commands.js';
import { historySelectDay } from './utils.js';

/**
 * A Garden loaded with the minimum depth required by mutation functions.
 * Memberships need user loaded for role checks.
 * Context needs workspaces loaded (shallowly) for slug uniqueness checks.
 */
type GardenForMutations = co.loaded<
	typeof GardenSchema,
	{
		memberships: { $each: { user: true } };
		context: { workspaces: { $each: true } };
	}
>;

type GardenRole = (typeof GardenMembershipRoleEnumOptions)[number];

const ROLE_ORDER: GardenRole[] = ['VIEWER', 'EDITOR', 'ADMIN'];

/**
 * Checks that the given account has sufficient role in the garden for the given action.
 * Throws AppError if the account is not a member or has insufficient role.
 * @param garden The garden to check membership in.
 * @param account The account to check.
 * @param action The action being performed, mapped to a required role via permissions.ts.
 */
function checkGardenRole(
	garden: GardenForMutations,
	account: Account,
	action: ActionType
): void {
	const required = requiredRole(action);
	const membership = [...garden.memberships].find(
		(member) => member.user.$jazz.id === account.$jazz.id
	);
	if (!membership) {
		throw new AppError('Not a member of this garden.', {
			nonFormErrors: ['Access denied.']
		});
	}
	if (ROLE_ORDER.indexOf(membership.role as GardenRole) < ROLE_ORDER.indexOf(required)) {
		throw new AppError('Insufficient permissions.', {
			nonFormErrors: ['Access denied.']
		});
	}
}

/**
 * Checks that no workspace in the garden already uses the given slug.
 * Throws AppError if the slug is taken.
 * @param garden The garden whose workspaces to check.
 * @param slug The slug to verify is unique.
 * @param excludeId Optional CoValue ID of a workspace to exclude (used when renaming).
 */
function checkWorkspaceSlugUniqueness(
	garden: GardenForMutations,
	slug: string,
	excludeId?: string
): void {
	const duplicate = [...garden.context.workspaces].find(
		(workspace) => workspace.slug === slug && workspace.$jazz.id !== excludeId
	);
	if (duplicate) {
		throw new AppError('Workspace name already exists.', {
			fieldErrors: { name: ['A workspace with this name already exists in this garden.'] }
		});
	}
}


/**
 * Validates and applies a partial update to an existing location.
 * @param location The location CoValue to update.
 * @param diff The partial location values to apply.
 */
export function updateLocation(location: Location, diff: LocationDiff) {
	const result = locationDiffValidation.safeParse(diff);
	if (!result.success) {
		throw new AppError('Invalid location update.', zodErrorToAppErrors(result.error));
	}

	location.$jazz.applyDiff(diff);
}

/**
 * Copies the most recent location entry to a new date.
 * Used when extending an object's active date range forward.
 * @param history The object history whose location list to extend.
 * @param workspace The workspace the new location entry belongs to.
 * @param date The new date to extend the history to.
 */
export function extendLocationHistory(
	history: ObjectHistory,
	workspace: Workspace,
	date: Date
) {
	const source = [...history.locations].at(-1);

	if (!source) {
		return;
	}

	history.locations.$jazz.push(
		LocationSchema.create(
			{ date, coordinate: source.coordinate, workspace },
			{ owner: history.$jazz.owner }
		)
	);
}

/**
 * Updates the geometry at the given date, or inserts a new one if none exists that day.
 * @param history The object history whose geometry list to update.
 * @param geometry The new geometry values to apply.
 */
export function upsertGeometry(
	history: ObjectHistory,
	geometry: Geometry
) {
	const geometryResult = geometryValidation.safeParse(geometry);
	if (!geometryResult.success) {
		throw new AppError('Invalid geometry.', zodErrorToAppErrors(geometryResult.error));
	}

	const existing = historySelectDay([...history.geometries], geometry.date);

	if (existing) {
		existing.$jazz.applyDiff({
			scaleFactor: geometry.scaleFactor,
			rotation: geometry.rotation
		});
		applyGeometryAttributesUpdate(existing, geometry.attributes);
	} else {
		history.geometries.$jazz.push(
			GeometrySchema.create(
				{
					date: geometry.date,
					scaleFactor: geometry.scaleFactor,
					rotation: geometry.rotation,
					attributes: geometry.attributes
				},
				{ owner: history.$jazz.owner }
			)
		);
	}
}

/**
 * Validates and applies a partial update to an existing geometry.
 * @param geometry The geometry CoValue to update.
 * @param diff The partial geometry values to apply.
 */
export function updateGeometry(geometry: Geometry, diff: GeometryDiff) {
	const result = geometryDiffValidation.safeParse(diff);
	if (!result.success) {
		throw new AppError('Invalid geometry update.', zodErrorToAppErrors(result.error));
	}

	const { attributes, ...scalarDiff } = diff;
	geometry.$jazz.applyDiff(scalarDiff);

	if (attributes) {
		applyGeometryAttributesUpdate(geometry, attributes);
	}
}

/**
 * Copies the most recent geometry entry to a new date.
 * Used when extending an object's active date range forward.
 * @param history The object history whose geometry list to extend.
 * @param date The new date to extend the history to.
 */
export function extendGeometryHistory(history: ObjectHistory, date: Date) {
	const source = [...history.geometries].at(-1);

	if (!source) {
		return;
	}

	history.geometries.$jazz.push(
		GeometrySchema.create(
			{
				date,
				scaleFactor: source.scaleFactor,
				rotation: source.rotation,
				attributes: source.attributes
			},
			{ owner: history.$jazz.owner }
		)
	);
}

/**
 * Creates a new workspace in a garden and pushes it to the garden's workspace list.
 * Requires ADMIN role. Validates name and enforces slug uniqueness within the garden.
 * @param garden The garden to create the workspace in.
 * @param input The workspace creation data.
 * @param currentAccount The account performing the action.
 * @returns The newly created Workspace CoValue.
 */
export function workspaceCreate(
	garden: GardenForMutations,
	input: WorkspaceCreateInput,
	currentAccount: Account
): Workspace {
	const validationResult = workspaceCreateInputSchema.safeParse(input);
	if (!validationResult.success) {
		throw new AppError('Invalid workspace.', zodErrorToAppErrors(validationResult.error));
	}
	const data = validationResult.data;

	checkGardenRole(garden, currentAccount, 'WorkspaceCreate');

	const slug = slugify(data.name);
	checkWorkspaceSlugUniqueness(garden, slug);

	const workspace = WorkspaceSchema.create(
		{ name: data.name, slug, description: data.description ?? '', plantingAreas: [] },
		{ owner: garden.$jazz.owner }
	);
	garden.context.workspaces.$jazz.push(workspace);
	return workspace;
}

/**
 * Updates the name and/or description of an existing workspace.
 * Requires ADMIN role. Re-validates slug uniqueness if the name changes.
 * @param garden The garden the workspace belongs to.
 * @param workspace The workspace to update.
 * @param input The fields to update.
 * @param currentAccount The account performing the action.
 */
export function workspaceUpdate(
	garden: GardenForMutations,
	workspace: Workspace,
	input: WorkspaceUpdateInput,
	currentAccount: Account
): void {
	const validationResult = workspaceUpdateInputSchema.safeParse(input);
	if (!validationResult.success) {
		throw new AppError('Invalid workspace update.', zodErrorToAppErrors(validationResult.error));
	}

	checkGardenRole(garden, currentAccount, 'WorkspaceUpdate');

	if (input.name !== undefined) {
		const slug = slugify(input.name);
		checkWorkspaceSlugUniqueness(garden, slug, workspace.$jazz.id);
		workspace.$jazz.applyDiff({ name: input.name, slug });
	}

	if (input.description !== undefined) {
		workspace.$jazz.set('description', input.description);
	}
}

/**
 * Creates a new planting area with initial geometry and location, and adds it to the workspace.
 * Requires EDITOR role.
 * @param garden The garden the workspace belongs to.
 * @param workspace The workspace to add the planting area to.
 * @param input The planting area creation data.
 * @param currentAccount The account performing the action.
 * @returns The newly created PlantingArea CoValue.
 */
export function plantingAreaCreate(
	garden: GardenForMutations,
	workspace: Workspace,
	input: PlantingAreaCreateInput,
	currentAccount: Account
): PlantingArea {
	const validationResult = plantingAreaCreateInputSchema.safeParse(input);
	if (!validationResult.success) {
		throw new AppError('Invalid planting area.', zodErrorToAppErrors(validationResult.error));
	}

	checkGardenRole(garden, currentAccount, 'PlantingAreaCreate');

	const owner = { owner: garden.$jazz.owner };

	const initialGeometry = GeometrySchema.create(
		{
			date: input.initialGeometry.date,
			scaleFactor: input.initialGeometry.scaleFactor,
			rotation: input.initialGeometry.rotation,
			attributes: input.initialGeometry.attributes
		},
		owner
	);

	const initialLocation = LocationSchema.create(
		{ date: input.initialLocation.date, coordinate: input.initialLocation.coordinate, workspace },
		owner
	);

	const history = ObjectHistorySchema.create(
		{
			geometries: GeometryHistorySchema.create([initialGeometry], owner),
			locations: LocationHistorySchema.create([initialLocation], owner)
		},
		owner
	);

	const plantingArea = PlantingAreaSchema.create(
		{ name: input.name, description: input.description ?? '', depth: input.depth, history },
		owner
	);

	workspace.plantingAreas.$jazz.push(plantingArea);
	return plantingArea;
}

/**
 * Updates the name, description, and/or depth of an existing planting area.
 * Requires EDITOR role.
 * @param garden The garden the planting area belongs to.
 * @param plantingArea The planting area to update.
 * @param input The fields to update.
 * @param currentAccount The account performing the action.
 */
export function plantingAreaUpdate(
	garden: GardenForMutations,
	plantingArea: PlantingArea,
	input: PlantingAreaUpdateInput,
	currentAccount: Account
): void {
	const validationResult = plantingAreaUpdateInputSchema.safeParse(input);
	if (!validationResult.success) {
		throw new AppError('Invalid planting area update.', zodErrorToAppErrors(validationResult.error));
	}

	checkGardenRole(garden, currentAccount, 'PlantingAreaCreate');

	const { description, ...scalarDiff } = input;
	if (Object.keys(scalarDiff).length > 0) {
		plantingArea.$jazz.applyDiff(scalarDiff);
	}
	if (description !== undefined) {
		plantingArea.$jazz.set('description', description);
	}
}

/**
 * Applies a geometry attributes update to an existing geometry.
 * If the type is the same, diffs the attributes in place.
 * If the type has changed, replaces the attributes CoValue entirely.
 * @param existing The geometry to update.
 * @param incomingAttributes The new attribute values to apply.
 */
function applyGeometryAttributesUpdate(existing: Geometry, incomingAttributes: GeometryAttributes) {
	if (!existing.attributes) {
		return;
	}

	if (existing.attributes.type === incomingAttributes.type) {
		/**
		 * Type equality is verified above; TypeScript cannot narrow discriminated union members
		 * through $jazz.applyDiff's parameter type, so the cast is safe here.
		 */
		// eslint-disable-next-line @typescript-eslint/no-explicit-any
		existing.attributes.$jazz.applyDiff(incomingAttributes as any);
	} else {
		existing.$jazz.set('attributes', incomingAttributes);
	}
}
