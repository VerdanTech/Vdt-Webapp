import { z as zod } from 'zod';
import { useMutation } from '@sveltestack/svelte-query';
import type {
	WorkspaceCreateCommand,
	WorkspaceUpdateCommand,
	WorkspaceDeleteCommand,
	PlantingAreaCreateCommand,
	PlantingAreaUpdateCommand,
	PlantingAreaDeleteCommand
} from '$codegen/types';
import {
	workspaceCreateCommandOp,
	workspaceDeleteCommandOp,
	workspaceUpdateCommandOp,
	plantingAreaCreateCommandOp,
	plantingAreaUpdateCommandOp,
	plantingAreaDeleteCommandOp
} from '$codegen';
import { workspaceFieldSchemas } from './schemas';
import { gardenFieldSchemas } from '$lib/data/garden/schemas';

/** Creates a new workspace in a garden. */
export const workspaceCreate = {
	schema: zod.object({
		garden_key: gardenFieldSchemas.key,
		name: workspaceFieldSchemas.workspace_name,
		description: workspaceFieldSchemas.workspace_description.optional()
	}),
	mutation: () => {
		return useMutation(function (data: WorkspaceCreateCommand) {
			return workspaceCreateCommandOp(data);
		});
	}
};

/** Updates a workspace. */
export const workspaceUpdate = {
	schema: zod.object({
		workspace_ref: zod.string().uuid(),
		name: workspaceFieldSchemas.workspace_name.optional(),
		description: workspaceFieldSchemas.workspace_description.optional()
	}),
	mutation: () => {
		return useMutation(function (data: WorkspaceUpdateCommand) {
			return workspaceUpdateCommandOp(data);
		});
	}
};

/** Deletes a workspace. */
export const workspaceDelete = {
	schema: zod.object({
		workspace_ref: zod.string().uuid()
	}),
	mutation: () => {
		return useMutation(function (data: WorkspaceDeleteCommand) {
			return workspaceDeleteCommandOp(data);
		});
	}
};

/** Creates a new planting area in a workspace. */
export const plantingAreaCreate = {
	schema: zod.object({
		workspace_ref: zod.string().uuid(),
		name: workspaceFieldSchemas.planting_area_name,
		description: workspaceFieldSchemas.planting_area_description.optional()
	}),
	mutation: () => {
		return useMutation(function (data: PlantingAreaCreateCommand) {
			return plantingAreaCreateCommandOp(data);
		});
	}
};

/** Updates a planting area. */
export const plantingAreaUpdate = {
	schema: zod.object({
		workspace_ref: zod.string().uuid(),
		planting_area_id: zod.string().uuid(),
		name: workspaceFieldSchemas.planting_area_name.optional(),
		description: workspaceFieldSchemas.planting_area_description.optional()
	}),
	mutation: () => {
		return useMutation(function (data: PlantingAreaUpdateCommand) {
			return plantingAreaUpdateCommandOp(data);
		});
	}
};

/** Deletes a planting area. */
export const plantingAreaDelete = {
	schema: zod.object({
		workspace_ref: zod.string().uuid(),
		planting_area_id: zod.string().uuid()
	}),
	mutation: () => {
		return useMutation(function (data: PlantingAreaDeleteCommand) {
			return plantingAreaDeleteCommandOp(data);
		});
	}
};
