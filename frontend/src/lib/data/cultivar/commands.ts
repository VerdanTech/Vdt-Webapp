import { z as zod } from 'zod';
import { useMutation } from '@sveltestack/svelte-query';
import type {
	CultivarCreateCommand,
	CultivarUpdateCommand,
	CultivarDeleteCommand,
	CultivarCollectionCreateCommand,
	CultivarCollectionUpdateCommand,
	CultivarCollectionDeleteCommand,
	CultivarCollectionDuplicateCommand,
	CultivarCollectionMergeCommand
} from '$codegen/types';
import {
	CultivarCollectionCreateCommandVisibility,
	CultivarCollectionUpdateCommandVisibility
} from '$codegen/types';
import {
	cultivarCreateCommandOp,
	cultivarUpdateCommandOp,
	cultivarDeleteCommandOp,
	cultivarCollectionCreateCommandOp,
	cultivarCollectionUpdateCommandOp,
	cultivarCollectionDeleteCommandOp,
	cultivarCollectionDuplicateCommandOp,
	cultivarCollectionMergeCommandOp
} from '$codegen';
import { cultivarFieldSchemas } from './schemas';

/** Creates a new cultivar in a collection. */
export const cultivarCreate = {
	schema: zod.object({
		collection_ref: zod.string().uuid(),
		names: cultivarFieldSchemas.cultivar_names,
		key: cultivarFieldSchemas.cultivar_key.optional(),
		scientific_name: cultivarFieldSchemas.cultivar_scientific_name.optional(),
		description: cultivarFieldSchemas.cultivar_description.optional(),
		parent_id: zod.string().uuid().optional()
	}),
	mutation: () => {
		return useMutation(function (data: CultivarCreateCommand) {
			return cultivarCreateCommandOp(data);
		});
	}
};

/** Updates a cultivar. */
export const cultivarUpdate = {
	schema: zod.object({
		collection_ref: zod.string().uuid(),
		cultivar_id: zod.string().uuid(),
		names: cultivarFieldSchemas.cultivar_names.optional(),
		key: cultivarFieldSchemas.cultivar_key.optional(),
		scientific_name: cultivarFieldSchemas.cultivar_scientific_name.optional(),
		description: cultivarFieldSchemas.cultivar_description.optional(),
		parent_id: zod.string().uuid().optional(),
		remove_parent: zod.boolean().optional()
	}),
	mutation: () => {
		return useMutation(function (data: CultivarUpdateCommand) {
			return cultivarUpdateCommandOp(data);
		});
	}
};

/** Deletes a cultivar. */
export const cultivarDelete = {
	schema: zod.object({
		collection_ref: zod.string().uuid(),
		cultivar_id: zod.string().uuid()
	}),
	mutation: () => {
		return useMutation(function (data: CultivarDeleteCommand) {
			return cultivarDeleteCommandOp(data);
		});
	}
};

/** Creates a new cultivar collection. */
export const culviarCollectionCreate = {
	schema: zod.object({
		name: cultivarFieldSchemas.cultivar_collection_name,
		visibility: zod.nativeEnum(CultivarCollectionCreateCommandVisibility).optional(),
		description: cultivarFieldSchemas.cultivar_collection_description.optional(),
		tags: cultivarFieldSchemas.cultivar_collection_tags.optional(),
		parent_ref: zod.string().uuid().optional(),
		garden_ref: zod.string().uuid().optional()
	}),
	mutation: () => {
		return useMutation(function (data: CultivarCollectionCreateCommand) {
			return cultivarCollectionCreateCommandOp(data);
		});
	}
};

/** Updates a cultivar collection. */
export const cultivarCollectionUpdate = {
	schema: zod.object({
		collection_ref: zod.string().uuid(),
		name: cultivarFieldSchemas.cultivar_collection_name.optional(),
		visibility: zod.nativeEnum(CultivarCollectionUpdateCommandVisibility).optional(),
		description: cultivarFieldSchemas.cultivar_collection_description.optional(),
		tags: cultivarFieldSchemas.cultivar_collection_tags.optional(),
		parent_ref: zod.string().uuid().optional(),
		remove_parent: zod.boolean().optional()
	}),
	mutation: () => {
		return useMutation(function (data: CultivarCollectionUpdateCommand) {
			return cultivarCollectionUpdateCommandOp(data);
		});
	}
};

/** Deletes a cultivar collection.. */
export const cultivarCollectionDelete = {
	schema: zod.object({
		collection_ref: zod.string().uuid()
	}),
	mutation: () => {
		return useMutation(function (data: CultivarCollectionDeleteCommand) {
			return cultivarCollectionDeleteCommandOp(data);
		});
	}
};

/** Creates a new cultivar collection by copying another. */
export const cultivarCollectionDuplicate = {
	schema: zod.object({
		source_collection_ref: zod.string().uuid(),
		garden_ref: zod.string().uuid().optional()
	}),
	mutation: () => {
		return useMutation(function (data: CultivarCollectionDuplicateCommand) {
			return cultivarCollectionDuplicateCommandOp(data);
		});
	}
};

/** Merges an existing cultivar collection into another. */
export const cultivarCollectionMerge = {
	schema: zod.object({
		target_collection_ref: zod.string().uuid(),
		source_collection_ref: zod.string().uuid()
	}),
	mutation: () => {
		return useMutation(function (data: CultivarCollectionMergeCommand) {
			return cultivarCollectionMergeCommandOp(data);
		});
	}
};