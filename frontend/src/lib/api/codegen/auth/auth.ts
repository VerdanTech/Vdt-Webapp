/**
 * Generated by orval v6.12.0 🍺
 * Do not edit manually.
 * VerdanTech-API
 * API of the VerdanTech Project Web Application
 * OpenAPI spec version: 0.1.0
 */
import { createQuery, createMutation } from '@tanstack/svelte-query';
import type {
	CreateQueryOptions,
	CreateMutationOptions,
	QueryFunction,
	MutationFunction,
	CreateQueryResult,
	QueryKey
} from '@tanstack/svelte-query';
import type { CSRFToken, Login, LoginRequest } from '../verdanTechAPI.schemas';
import { customInstance } from '../../customAxios';

/**
 * Returns valid CSRF token
 */
export const authCsrfRetrieve = (signal?: AbortSignal) => {
	return customInstance<CSRFToken>({ url: `/auth/csrf`, method: 'get', signal });
};

export const getAuthCsrfRetrieveQueryKey = () => [`/auth/csrf`];

export type AuthCsrfRetrieveQueryResult = NonNullable<Awaited<ReturnType<typeof authCsrfRetrieve>>>;
export type AuthCsrfRetrieveQueryError = unknown;

export const createAuthCsrfRetrieve = <
	TData = Awaited<ReturnType<typeof authCsrfRetrieve>>,
	TError = unknown
>(options?: {
	query?: CreateQueryOptions<Awaited<ReturnType<typeof authCsrfRetrieve>>, TError, TData>;
}): CreateQueryResult<TData, TError> & { queryKey: QueryKey } => {
	const { query: queryOptions } = options ?? {};

	const queryKey = queryOptions?.queryKey ?? getAuthCsrfRetrieveQueryKey();

	const queryFn: QueryFunction<Awaited<ReturnType<typeof authCsrfRetrieve>>> = ({ signal }) =>
		authCsrfRetrieve(signal);

	const query = createQuery<Awaited<ReturnType<typeof authCsrfRetrieve>>, TError, TData>({
		queryKey,
		queryFn,
		...queryOptions
	}) as CreateQueryResult<TData, TError> & { queryKey: QueryKey };

	query.queryKey = queryKey;

	return query;
};

/**
 * Login using Session authentication.
Requires CSRF token to prevent login-csrf,
see: https://docs.djangoproject.com/en/4.1/ref/csrf/
 */
export const authLoginCreate = (loginRequest: LoginRequest) => {
	return customInstance<Login>({
		url: `/auth/login`,
		method: 'post',
		headers: { 'Content-Type': 'application/json' },
		data: loginRequest
	});
};

export type AuthLoginCreateMutationResult = NonNullable<
	Awaited<ReturnType<typeof authLoginCreate>>
>;
export type AuthLoginCreateMutationBody = LoginRequest;
export type AuthLoginCreateMutationError = unknown;

export const createAuthLoginCreate = <TError = unknown, TContext = unknown>(options?: {
	mutation?: CreateMutationOptions<
		Awaited<ReturnType<typeof authLoginCreate>>,
		TError,
		{ data: LoginRequest },
		TContext
	>;
}) => {
	const { mutation: mutationOptions } = options ?? {};

	const mutationFn: MutationFunction<
		Awaited<ReturnType<typeof authLoginCreate>>,
		{ data: LoginRequest }
	> = (props) => {
		const { data } = props ?? {};

		return authLoginCreate(data);
	};

	return createMutation<
		Awaited<ReturnType<typeof authLoginCreate>>,
		TError,
		{ data: LoginRequest },
		TContext
	>(mutationFn, mutationOptions);
};
/**
 * Calls Django logout methods and deletes the sessionid assigned to the user object
 */
export const authLogoutCreate = () => {
	return customInstance<void>({ url: `/auth/logout`, method: 'post' });
};

export type AuthLogoutCreateMutationResult = NonNullable<
	Awaited<ReturnType<typeof authLogoutCreate>>
>;

export type AuthLogoutCreateMutationError = unknown;

export const createAuthLogoutCreate = <
	TError = unknown,
	TVariables = void,
	TContext = unknown
>(options?: {
	mutation?: CreateMutationOptions<
		Awaited<ReturnType<typeof authLogoutCreate>>,
		TError,
		TVariables,
		TContext
	>;
}) => {
	const { mutation: mutationOptions } = options ?? {};

	const mutationFn: MutationFunction<
		Awaited<ReturnType<typeof authLogoutCreate>>,
		TVariables
	> = () => {
		return authLogoutCreate();
	};

	return createMutation<Awaited<ReturnType<typeof authLogoutCreate>>, TError, TVariables, TContext>(
		mutationFn,
		mutationOptions
	);
};
