import z from 'zod';

export declare const userFields: {
	usernameSchema: z.ZodString;
	emailSchema: z.ZodString;
	passwordSchema: z.ZodString;
};
/**
 * Command to authenticate a user.
 */
export declare const UserLoginCommandSchema: z.ZodObject<
	{
		email: z.ZodString;
		password: z.ZodString;
	},
	'strip',
	z.ZodTypeAny,
	{
		email: string;
		password: string;
	},
	{
		email: string;
		password: string;
	}
>;
export type UserLoginCommand = z.infer<typeof UserLoginCommandSchema>;
/**
 * Command to register a new user.
 */
export declare const UserCreateCommandSchema: z.ZodEffects<
	z.ZodObject<
		{
			email: z.ZodString;
			password1: z.ZodString;
			password2: z.ZodString;
			username: z.ZodString;
		},
		'strip',
		z.ZodTypeAny,
		{
			email: string;
			username: string;
			password1: string;
			password2: string;
		},
		{
			email: string;
			username: string;
			password1: string;
			password2: string;
		}
	>,
	{
		email: string;
		username: string;
		password1: string;
		password2: string;
	},
	{
		email: string;
		username: string;
		password1: string;
		password2: string;
	}
>;
export type UserCreateCommand = z.infer<typeof UserCreateCommandSchema>;
/**
 * Command to update a user.
 */
export declare const UserUpdateCommandSchema: z.ZodEffects<
	z.ZodObject<
		{
			newEmail: z.ZodOptional<z.ZodString>;
			newPassword1: z.ZodOptional<z.ZodString>;
			newPassword2: z.ZodOptional<z.ZodString>;
			newUsername: z.ZodOptional<z.ZodString>;
			password: z.ZodString;
		},
		'strip',
		z.ZodTypeAny,
		{
			password: string;
			newEmail?: string | undefined;
			newPassword1?: string | undefined;
			newPassword2?: string | undefined;
			newUsername?: string | undefined;
		},
		{
			password: string;
			newEmail?: string | undefined;
			newPassword1?: string | undefined;
			newPassword2?: string | undefined;
			newUsername?: string | undefined;
		}
	>,
	{
		password: string;
		newEmail?: string | undefined;
		newPassword1?: string | undefined;
		newPassword2?: string | undefined;
		newUsername?: string | undefined;
	},
	{
		password: string;
		newEmail?: string | undefined;
		newPassword1?: string | undefined;
		newPassword2?: string | undefined;
		newUsername?: string | undefined;
	}
>;
export type UserUpdateCommand = z.infer<typeof UserUpdateCommandSchema>;
/**
 * Command to request a verification email be sent.
 */
export declare const UserRequestEmailConfirmationCommandSchema: z.ZodObject<
	{
		email: z.ZodString;
	},
	'strip',
	z.ZodTypeAny,
	{
		email: string;
	},
	{
		email: string;
	}
>;
export type UserRequestEmailConfirmationCommand = z.infer<
	typeof UserRequestEmailConfirmationCommandSchema
>;
/**
 * Command to respond to a verification email.
 */
export declare const UserConfirmEmailConfirmationCommandSchema: z.ZodObject<
	{
		token: z.ZodString;
	},
	'strip',
	z.ZodTypeAny,
	{
		token: string;
	},
	{
		token: string;
	}
>;
export type UserConfirmEmailConfirmationCommand = z.infer<
	typeof UserConfirmEmailConfirmationCommandSchema
>;
/**
 * Command to request a password reset email be sent.
 */
export declare const UserRequestPasswordResetCommandSchema: z.ZodObject<
	{
		email: z.ZodString;
	},
	'strip',
	z.ZodTypeAny,
	{
		email: string;
	},
	{
		email: string;
	}
>;
export type UserRequestPasswordResetCommand = z.infer<
	typeof UserRequestPasswordResetCommandSchema
>;
/**
 * Command to respont to a password reset email.
 */
export declare const UserConfirmPasswordResetCommandSchema: z.ZodEffects<
	z.ZodObject<
		{
			userId: z.ZodString;
			token: z.ZodString;
			password1: z.ZodString;
			password2: z.ZodString;
		},
		'strip',
		z.ZodTypeAny,
		{
			token: string;
			userId: string;
			password1: string;
			password2: string;
		},
		{
			token: string;
			userId: string;
			password1: string;
			password2: string;
		}
	>,
	{
		token: string;
		userId: string;
		password1: string;
		password2: string;
	},
	{
		token: string;
		userId: string;
		password1: string;
		password2: string;
	}
>;
export type UserConfirmPasswordResetCommand = z.infer<
	typeof UserConfirmPasswordResetCommandSchema
>;
//# sourceMappingURL=commands.d.ts.map
