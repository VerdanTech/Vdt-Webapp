import z from 'zod';

export declare const gardenFields: {
	gardenIdSchema: z.ZodString;
	gardenNameSchema: z.ZodString;
	gardenDescriptionSchema: z.ZodString;
	gardenVisibilitySchema: z.ZodEnum<['HIDDEN', 'UNLISTED', 'PUBLIC']>;
	gardenMembershipRoleSchema: z.ZodEnum<['ADMIN', 'EDITOR', 'VIEWER']>;
	usernameInvitesListSchema: z.ZodArray<z.ZodString, 'many'>;
};
/**
 * Command to create a new garden.
 */
export declare const GardenCreateCommandSchema: z.ZodObject<
	{
		id: z.ZodString;
		name: z.ZodString;
		description: z.ZodDefault<z.ZodString>;
		visibility: z.ZodDefault<z.ZodEnum<['HIDDEN', 'UNLISTED', 'PUBLIC']>>;
		adminInvites: z.ZodDefault<z.ZodArray<z.ZodString, 'many'>>;
		editorInvites: z.ZodDefault<z.ZodArray<z.ZodString, 'many'>>;
		viewerInvites: z.ZodDefault<z.ZodArray<z.ZodString, 'many'>>;
	},
	'strip',
	z.ZodTypeAny,
	{
		name: string;
		id: string;
		description: string;
		visibility: 'HIDDEN' | 'UNLISTED' | 'PUBLIC';
		adminInvites: string[];
		editorInvites: string[];
		viewerInvites: string[];
	},
	{
		name: string;
		id: string;
		description?: string | undefined;
		visibility?: 'HIDDEN' | 'UNLISTED' | 'PUBLIC' | undefined;
		adminInvites?: string[] | undefined;
		editorInvites?: string[] | undefined;
		viewerInvites?: string[] | undefined;
	}
>;
export type GardenCreateCommand = z.infer<typeof GardenCreateCommandSchema>;
/**
 * Command to invite a user to a garden.
 */
export declare const GardenMembershipCreateCommandSchema: z.ZodObject<
	{
		gardenId: z.ZodString;
		adminInvites: z.ZodDefault<z.ZodArray<z.ZodString, 'many'>>;
		editorInvites: z.ZodDefault<z.ZodArray<z.ZodString, 'many'>>;
		viewerInvites: z.ZodDefault<z.ZodArray<z.ZodString, 'many'>>;
	},
	'strip',
	z.ZodTypeAny,
	{
		gardenId: string;
		adminInvites: string[];
		editorInvites: string[];
		viewerInvites: string[];
	},
	{
		gardenId: string;
		adminInvites?: string[] | undefined;
		editorInvites?: string[] | undefined;
		viewerInvites?: string[] | undefined;
	}
>;
export type GardenMembershipCreateCommand = z.infer<
	typeof GardenMembershipCreateCommandSchema
>;
/**
 * Command to accept a garden membership invite.
 */
export declare const GardenMembershipAcceptCommandSchema: z.ZodObject<
	{
		gardenId: z.ZodString;
	},
	'strip',
	z.ZodTypeAny,
	{
		gardenId: string;
	},
	{
		gardenId: string;
	}
>;
export type GardenMembershipAcceptCommand = z.infer<
	typeof GardenMembershipAcceptCommandSchema
>;
/**
 * Command to leave a garden.
 */
export declare const GardenMembershipDeleteCommandSchema: z.ZodObject<
	{
		gardenId: z.ZodString;
	},
	'strip',
	z.ZodTypeAny,
	{
		gardenId: string;
	},
	{
		gardenId: string;
	}
>;
export type GardenMembershipDeleteCommand = z.infer<
	typeof GardenMembershipDeleteCommandSchema
>;
/**
 * Command to revoke a user's membership.
 */
export declare const GardenMembershipRevokeCommandSchema: z.ZodObject<
	{
		gardenId: z.ZodString;
		profileId: z.ZodString;
	},
	'strip',
	z.ZodTypeAny,
	{
		gardenId: string;
		profileId: string;
	},
	{
		gardenId: string;
		profileId: string;
	}
>;
export type GardenMembershipRevokeCommand = z.infer<
	typeof GardenMembershipRevokeCommandSchema
>;
/**
 * Command to change the role on a user's membership.
 */
export declare const GardenMembershipRoleChangeCommandSchema: z.ZodObject<
	{
		gardenId: z.ZodString;
		profileId: z.ZodString;
		newRole: z.ZodEnum<['ADMIN', 'EDITOR', 'VIEWER']>;
	},
	'strip',
	z.ZodTypeAny,
	{
		gardenId: string;
		profileId: string;
		newRole: 'ADMIN' | 'EDITOR' | 'VIEWER';
	},
	{
		gardenId: string;
		profileId: string;
		newRole: 'ADMIN' | 'EDITOR' | 'VIEWER';
	}
>;
export type GardenMembershipRoleChangeCommand = z.infer<
	typeof GardenMembershipRoleChangeCommandSchema
>;
//# sourceMappingURL=commands.d.ts.map
