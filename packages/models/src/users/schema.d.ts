import { type Entity, type Roles } from '@triplit/client';

export declare const roles: Roles;
export declare const userSchema: {
	/** User profiles. */
	profiles: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				/** Username. Unique and used within the app to search for users. */
				username: import('@triplit/client').StringType<{}>;
				/** Date of user creation. */
				createdAt: import('@triplit/client').DateType<{
					default: {
						func: string;
						args: null;
					};
				}>;
			},
			{}
		>;
		/** Profile objects can only be modified by the server but viewed by anyone. */
		permissions: {
			anon: {
				read: {
					filter: true[];
				};
			};
			user: {
				read: {
					filter: true[];
				};
			};
		};
	};
	/** User accounts. */
	accounts: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				/** The ID of the associated profile. */
				profileId: import('@triplit/client').StringType<{}>;
				/** Hashed password */
				passwordHash: import('@triplit/client').StringType<{}>;
				/** Primary email address. Only verified emails use this attribute. */
				verifiedEmail: import('@triplit/client').StringType<{
					nullable: true;
				}>;
				/**
				 * Secondary email. Used to avoid replacing primary email when switching emails.
				 * Upon verification, should be nulled and used to set primaryEmail.
				 */
				unverifiedEmail: import('@triplit/client').RecordType<
					{
						/** Address of the email. */
						address: import('@triplit/client').StringType<{
							nullable: true;
							default: null;
						}>;
						/** JWT confirmation token which is sent to the user for verification. */
						token: import('@triplit/client').StringType<{
							nullable: true;
							default: null;
						}>;
					},
					{}
				>;
				/** JWT confirmation key used to confirm a password reset. */
				passwordResetToken: import('@triplit/client').StringType<{
					nullable: true;
					default: null;
				}>;
				/** Set to false for inactive users. */
				isActive: import('@triplit/client').BooleanType<{
					default: boolean;
				}>;
			},
			{}
		>;
		relationships: {
			profile: {
				query: {
					collectionName: 'profiles';
					where: any;
				};
				cardinality: 'one';
			};
		};
		/** Accounts objects can only be modified by the server and viewed by the user. */
		permissions: {
			user: {
				read: {
					filter: ['id', string, string][];
				};
			};
		};
	};
};
export type UserProfile = Entity<typeof userSchema, 'profiles'>;
export type UserAccount = Entity<typeof userSchema, 'accounts'>;
export type User = {
	account: UserAccount;
	profile: UserProfile;
};
//# sourceMappingURL=schema.d.ts.map
