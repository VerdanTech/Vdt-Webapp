/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import type {
	CultivarCollectionCreateCommand,
	CultivarCollectionDeleteCommand,
	CultivarCollectionDuplicateCommand,
	CultivarCollectionFullSchema,
	CultivarCollectionGetByClientResult,
	CultivarCollectionGetByGardenQueryOpParams,
	CultivarCollectionGetByGardenResult,
	CultivarCollectionGetByIdsQueryOpParams,
	CultivarCollectionMergeCommand,
	CultivarCollectionUpdateCommand,
	CultivarCreateCommand,
	CultivarDeleteCommand,
	CultivarUpdateCommand
} from '../../types';
import { axiosClient } from '../../../data/customAxios';

/**
 * Creates a new cultivar collection.
 * @summary Cultivar collection create.
 */
export const cultivarCollectionCreateCommandOp = (
	cultivarCollectionCreateCommand: CultivarCollectionCreateCommand
) => {
	return axiosClient<string>({
		url: `/cultivars/command/create_collection`,
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		data: cultivarCollectionCreateCommand
	});
};
/**
 * Creates a new cultivar on the collection.
 * @summary Cultivar create.
 */
export const cultivarCreateCommandOp = (
	cultivarCreateCommand: CultivarCreateCommand
) => {
	return axiosClient<string>({
		url: `/cultivars/command/create_cultivar`,
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		data: cultivarCreateCommand
	});
};
/**
 * Deletes a cultivar collection.
 * @summary Cultivar collection delete.
 */
export const cultivarCollectionDeleteCommandOp = (
	cultivarCollectionDeleteCommand: CultivarCollectionDeleteCommand
) => {
	return axiosClient<string>({
		url: `/cultivars/command/delete_collection`,
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		data: cultivarCollectionDeleteCommand
	});
};
/**
 * Deletes a given cultivar from a collection.
 * @summary Cultivar delete.
 */
export const cultivarDeleteCommandOp = (
	cultivarDeleteCommand: CultivarDeleteCommand
) => {
	return axiosClient<string>({
		url: `/cultivars/command/delete_cultivar`,
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		data: cultivarDeleteCommand
	});
};
/**
 * Creates a new cultivar collection by copying the attributes of another.
 * @summary Cultivar collection duplication.
 */
export const cultivarCollectionDuplicateCommandOp = (
	cultivarCollectionDuplicateCommand: CultivarCollectionDuplicateCommand
) => {
	return axiosClient<string>({
		url: `/cultivars/command/duplicate_collection`,
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		data: cultivarCollectionDuplicateCommand
	});
};
/**
 * Copies the data of an exising cultivar collection into a another existing collection.
 * @summary Cultivar collection merge.
 */
export const cultivarCollectionMergeCommandOp = (
	cultivarCollectionMergeCommand: CultivarCollectionMergeCommand
) => {
	return axiosClient<string>({
		url: `/cultivars/command/merge_collection`,
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		data: cultivarCollectionMergeCommand
	});
};
/**
 * Sets the given attributes onto the cultivar collection.
 * @summary Cultivar collection update.
 */
export const cultivarCollectionUpdateCommandOp = (
	cultivarCollectionUpdateCommand: CultivarCollectionUpdateCommand
) => {
	return axiosClient<string>({
		url: `/cultivars/command/update_collection`,
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		data: cultivarCollectionUpdateCommand
	});
};
/**
 * Sets the given attributes onto the cultivar.
 * @summary Cultivar update.
 */
export const cultivarUpdateCommandOp = (
	cultivarUpdateCommand: CultivarUpdateCommand
) => {
	return axiosClient<string>({
		url: `/cultivars/command/update_cultivar`,
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		data: cultivarUpdateCommand
	});
};
/**
 * Retrieves the cultivar collections associated with this garden.
 * @summary Get cultivar collections from a garden.
 */
export const cultivarGetByClientQueryOp = () => {
	return axiosClient<CultivarCollectionGetByClientResult>({
		url: `/cultivars/query/get_by_client`,
		method: 'GET'
	});
};
/**
 * Retrieves the cultivar collections associated with this garden.
 * @summary Get cultivar collections from a garden.
 */
export const cultivarCollectionGetByGardenQueryOp = (
	params: CultivarCollectionGetByGardenQueryOpParams
) => {
	return axiosClient<CultivarCollectionGetByGardenResult>({
		url: `/cultivars/query/get_by_garden`,
		method: 'GET',
		params
	});
};
/**
 * Retrieves the cultivar collections associated with the IDs.
 * @summary Get cultivar collections from their IDs.
 */
export const cultivarCollectionGetByIdsQueryOp = (
	params: CultivarCollectionGetByIdsQueryOpParams
) => {
	return axiosClient<CultivarCollectionFullSchema[]>({
		url: `/cultivars/query/get_by_ids`,
		method: 'GET',
		params
	});
};
export type CultivarCollectionCreateCommandOpResult = NonNullable<
	Awaited<ReturnType<typeof cultivarCollectionCreateCommandOp>>
>;
export type CultivarCreateCommandOpResult = NonNullable<
	Awaited<ReturnType<typeof cultivarCreateCommandOp>>
>;
export type CultivarCollectionDeleteCommandOpResult = NonNullable<
	Awaited<ReturnType<typeof cultivarCollectionDeleteCommandOp>>
>;
export type CultivarDeleteCommandOpResult = NonNullable<
	Awaited<ReturnType<typeof cultivarDeleteCommandOp>>
>;
export type CultivarCollectionDuplicateCommandOpResult = NonNullable<
	Awaited<ReturnType<typeof cultivarCollectionDuplicateCommandOp>>
>;
export type CultivarCollectionMergeCommandOpResult = NonNullable<
	Awaited<ReturnType<typeof cultivarCollectionMergeCommandOp>>
>;
export type CultivarCollectionUpdateCommandOpResult = NonNullable<
	Awaited<ReturnType<typeof cultivarCollectionUpdateCommandOp>>
>;
export type CultivarUpdateCommandOpResult = NonNullable<
	Awaited<ReturnType<typeof cultivarUpdateCommandOp>>
>;
export type CultivarGetByClientQueryOpResult = NonNullable<
	Awaited<ReturnType<typeof cultivarGetByClientQueryOp>>
>;
export type CultivarCollectionGetByGardenQueryOpResult = NonNullable<
	Awaited<ReturnType<typeof cultivarCollectionGetByGardenQueryOp>>
>;
export type CultivarCollectionGetByIdsQueryOpResult = NonNullable<
	Awaited<ReturnType<typeof cultivarCollectionGetByIdsQueryOp>>
>;