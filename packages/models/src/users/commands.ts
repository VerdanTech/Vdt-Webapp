import {z} from 'jazz-tools';

import fields from './fields.js';

/**
 * Command to authenticate a user.
 */
export const UserLoginCommandSchema = z.object({
	email: fields.emailField,
	password: z.string()
});
export type UserLoginCommand = z.infer<typeof UserLoginCommandSchema>;

/**
 * Command to register a new user.
 */
export const UserCreateCommandSchema = z
	.object({
		email: fields.emailField,
		password1: fields.passwordField,
		password2: fields.passwordField,
		username: fields.usernameField
	})
	.refine((data) => data.password1 == data.password2, {
		message: 'Passwords must match',
		path: ['password2']
	});
export type UserCreateCommand = z.infer<typeof UserCreateCommandSchema>;

/**
 * Command to update a user.
 */
export const UserUpdateCommandSchema = z
	.object({
		newEmail: fields.emailField.optional(),
		newPassword1: fields.passwordField.optional(),
		newPassword2: fields.passwordField.optional(),
		newUsername: fields.usernameField.optional(),
		password: fields.passwordField
	})
	.refine((data) => data.newPassword1 == data.newPassword2, {
		message: 'Passwords must match',
		path: ['newPassword2']
	});
export type UserUpdateCommand = z.infer<typeof UserUpdateCommandSchema>;

/**
 * Command to request a verification email be sent.
 */
export const UserRequestEmailConfirmationCommandSchema = z.object({
	email: fields.emailField
});
export type UserRequestEmailConfirmationCommand = z.infer<
	typeof UserRequestEmailConfirmationCommandSchema
>;

/**
 * Command to respond to a verification email.
 */
export const UserConfirmEmailConfirmationCommandSchema = z.object({
	token: z.string()
});
export type UserConfirmEmailConfirmationCommand = z.infer<
	typeof UserConfirmEmailConfirmationCommandSchema
>;

/**
 * Command to request a password reset email be sent.
 */
export const UserRequestPasswordResetCommandSchema = z.object({
	email: fields.emailField
});
export type UserRequestPasswordResetCommand = z.infer<
	typeof UserRequestPasswordResetCommandSchema
>;

/**
 * Command to respond to a password reset email.
 */
export const UserConfirmPasswordResetCommandSchema = z
	.object({
		userId: z.string().nanoid(),
		token: z.string(),
		password1: fields.passwordField,
		password2: fields.passwordField
	})
	.refine((data) => data.password1 == data.password2, {
		message: 'Passwords must match',
		path: ['password2']
	});
export type UserConfirmPasswordResetCommand = z.infer<
	typeof UserConfirmPasswordResetCommandSchema
>;
