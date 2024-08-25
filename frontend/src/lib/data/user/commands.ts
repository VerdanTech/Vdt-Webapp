import { z as zod } from 'zod';
import { useMutation } from '@sveltestack/svelte-query';
import type {
	UserCreateCommand,
	UserConfirmEmailConfirmationCommand,
	UserRequestEmailConfirmationCommand,
	UserRequestPasswordResetCommand,
	UserConfirmPasswordResetCommand
} from '$codegen/types';
import {
	userCreateCommandOp,
	userConfirmEmailConfirmationCommandOp,
	userRequestEmailConfirmationCommandOp,
	userConfirmPasswordResetCommandOp,
	userRequestPasswordResetCommandOp
} from '$codegen';
import { userFieldSchemas } from './schemas';

/**
 * Sends an user creation request to the backend.
 */
export const userCreate = {
	schema: zod.object({
		email_address: userFieldSchemas.email,
		password1: userFieldSchemas.password,
		password2: userFieldSchemas.password,
		username: userFieldSchemas.username
	}),
	mutation: () => {
		return useMutation(function (data: UserCreateCommand) {
			return userCreateCommandOp(data);
		});
	}
};

/**
 * Sends an email verification request to the backend.
 */
export const userRequestEmailConfirmation = {
	schema: zod.object({
		email_address: userFieldSchemas.email
	}),
	mutation: () => {
		return useMutation(function (data: UserRequestEmailConfirmationCommand) {
			return userRequestEmailConfirmationCommandOp(data);
		});
	}
};

/**
 * Sends an email verification confirmation to the backend.
 */
export const userConfirmEmailConfirmation = {
	schema: zod.object({ key: zod.string().uuid() }),
	mutation: () => {
		return useMutation(function (data: UserConfirmEmailConfirmationCommand) {
			return userConfirmEmailConfirmationCommandOp(data);
		});
	}
};

/**
 * Sends a password reset request to the backend.
 */
export const userRequestPasswordReset = {
	schema: zod.object({
		email_address: userFieldSchemas.email
	}),
	mutation: () => {
		return useMutation(function (data: UserRequestPasswordResetCommand) {
			return userRequestPasswordResetCommandOp(data);
		});
	}
};

/**
 * Sends a password reset confirmation to the backend.
 */
export const userConfirmPasswordReset = {
	schema: zod.object({
		key: zod.string().uuid(),
		new_password1: userFieldSchemas.password,
		new_password2: userFieldSchemas.password,
		user_id: zod.string().uuid()
	}),
	mutation: () => {
		return useMutation(function (data: UserConfirmPasswordResetCommand) {
			return userConfirmPasswordResetCommandOp(data);
		});
	}
};
