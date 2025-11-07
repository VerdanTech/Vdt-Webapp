import { type Entity } from '@triplit/client';

/**
 * Controls the visibility of the garden.
 * HIDDEN: the garden is visible only to those who are members.
 * UNLISTED: the garden is visibile to anyone but is not listed
 *     on any public page - a link is required.
 * PUBLIC: the garden is visible to anyone and may be searchable.
 */
export declare const GardenVisibilityEnumOptions: readonly [
	'HIDDEN',
	'UNLISTED',
	'PUBLIC'
];
/**
 * Controls the level of access of a garden membership.
 * ADMIN: all actions are supported.
 * EDITOR: routine changes in model state are supported, such as adding plant models,
 *     while configuration changes such as garden attributes are not.
 * VIEWER: Read-only access.
 */
export declare const GardenMembershipRoleEnumOptions: readonly [
	'ADMIN',
	'EDITOR',
	'VIEWER'
];
/**
 * Indicates the acceptance status of a garden membership.
 * CREATED: the invite has been created but no notification has been sent.
 * PENDING: a notification has been sent and is pending acceptance.
 * ACCEPTED: the membership has been accepted.
 */
export declare const GardenMembershipStatusEnumOptions: readonly [
	'CREATED',
	'PENDING',
	'ACCEPTED'
];
export declare const gardenSchema: {
	/** Garden schema. */
	gardens: {
		schema: import('@triplit/client').RecordType<
			{
				/** URL-friendly shorthand - unique. */
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				/** Non-unique name of the garden. */
				name: import('@triplit/client').StringType<{}>;
				/** Controls which non-users may view the garden. */
				visibility: import('@triplit/client').StringType<{
					enum: ('HIDDEN' | 'UNLISTED' | 'PUBLIC')[];
				}>;
				/** Optional description. */
				description: import('@triplit/client').StringType<{
					nullable: true;
					default: null;
				}>;
				/** Set to false for inactive gardens. */
				isActive: import('@triplit/client').BooleanType<{
					default: boolean;
				}>;
				/**
				 * User who created the garden.
				 * Note that the creator has access through an admin membership.
				 * If undefined, the original creator has left the garden.
				 */
				creatorId: import('@triplit/client').StringType<{
					nullable: true;
				}>;
				/** Set of users which have admin access. */
				adminIds: import('@triplit/client').SetType<
					import('@triplit/client').StringType<{}>,
					{}
				>;
				/** Set of users which have editing access. */
				editorIds: import('@triplit/client').SetType<
					import('@triplit/client').StringType<{}>,
					{
						default: {
							func: string;
							args: null;
						};
					}
				>;
				/** Set of users which have viewing access. */
				viewerIds: import('@triplit/client').SetType<
					import('@triplit/client').StringType<{}>,
					{
						default: {
							func: string;
							args: null;
						};
					}
				>;
				/** Date of garden creation. */
				createdAt: import('@triplit/client').DateType<{
					default: {
						func: string;
						args: null;
					};
				}>;
			},
			{}
		>;
		relationships: {
			creator: {
				query: {
					collectionName: 'profiles';
					where: any;
				};
				cardinality: 'one';
			};
			adminMemberships: {
				query: {
					collectionName: 'gardenMemberships';
				} & {
					where: ['userId', string, string][];
				};
				cardinality: 'many';
			};
			editorMemberships: {
				query: {
					collectionName: 'gardenMemberships';
				} & {
					where: ['userId', string, string][];
				};
				cardinality: 'many';
			};
			viewerMemberships: {
				query: {
					collectionName: 'gardenMemberships';
				} & {
					where: ['userId', string, string][];
				};
				cardinality: 'many';
			};
		};
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: ['visibility', string, string][];
				};
			};
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: {
						mod: 'or';
						filters: (
							| ['visibility', string, string]
							| ['adminIds', string, string]
							| ['editorIds', string, string]
							| ['viewerIds', string, string]
						)[];
					}[];
				};
				insert: {
					/** Allow new gardens to be created by creators. */
					filter: ['creatorId', string, string][];
				};
				update: {
					/** Restrict edit access to admins. */
					filter: ['adminIds', string, string][];
				};
			};
		};
	};
	/** Garden membership schema. */
	gardenMemberships: {
		schema: import('@triplit/client').RecordType<
			{
				id: import('@triplit/client').StringType<{
					nullable: false;
					default: {
						func: string;
						args: string[] | null;
					};
				}>;
				/** Garden the membership is in. */
				gardenId: import('@triplit/client').StringType<{}>;
				/** User who is the subject of the membership. */
				userId: import('@triplit/client').StringType<{}>;
				/** Role of the membership. */
				role: import('@triplit/client').StringType<{
					enum: ('ADMIN' | 'EDITOR' | 'VIEWER')[];
				}>;
				/** User who created the membership. */
				inviterId: import('@triplit/client').StringType<{
					nullable: true;
				}>;
				/** The acceptance status and acceptance date of the membership. */
				status: import('@triplit/client').StringType<{
					enum: ('CREATED' | 'PENDING' | 'ACCEPTED')[];
				}>;
				acceptedAt: import('@triplit/client').DateType<{
					nullable: true;
					default: null;
				}>;
				/** Allows marking gardens as favorites in the menu. */
				favorite: import('@triplit/client').BooleanType<{
					default: boolean;
				}>;
			},
			{}
		>;
		relationships: {
			garden: {
				query: {
					collectionName: 'gardens';
					where: any;
				};
				cardinality: 'one';
			};
			user: {
				query: {
					collectionName: 'profiles';
					where: any;
				};
				cardinality: 'one';
			};
			inviter: {
				query: {
					collectionName: 'profiles';
					where: any;
				};
				cardinality: 'one';
			};
		};
		permissions: {
			anon: {
				read: {
					/** Allow anonymous reads if the garden is not hidden. */
					filter: ['garden.visibility', string, string][];
				};
			};
			user: {
				read: {
					/** Allow reads if the garden is not hidden or the user is a member. */
					filter: {
						mod: 'or';
						filters: (
							| ['garden.visibility', string, string]
							| ['garden.adminIds', string, string]
							| ['garden.editorIds', string, string]
							| ['garden.viewerIds', string, string]
						)[];
					}[];
				};
				insert: {
					/** Allow new memberships to be created by admins. */
					filter: ['garden.adminIds', string, string][];
				};
				update: {
					/** Restrict membership updates to admins and subjects. */
					filter: {
						mod: 'or';
						filters: (
							| ['userId', string, string]
							| ['garden.adminIds', string, string]
						)[];
					}[];
				};
				delete: {
					/** Allow the membership to be revoked by an admin or deleted by the subject. */
					filter: {
						mod: 'or';
						filters: (
							| ['userId', string, string]
							| ['garden.adminIds', string, string]
						)[];
					}[];
				};
			};
		};
	};
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
				username: import('@triplit/client').StringType<{}>;
				createdAt: import('@triplit/client').DateType<{
					default: {
						func: string;
						args: null;
					};
				}>;
			},
			{}
		>;
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
				profileId: import('@triplit/client').StringType<{}>;
				passwordHash: import('@triplit/client').StringType<{}>;
				verifiedEmail: import('@triplit/client').StringType<{
					nullable: true;
				}>;
				unverifiedEmail: import('@triplit/client').RecordType<
					{
						address: import('@triplit/client').StringType<{
							nullable: true;
							default: null;
						}>;
						token: import('@triplit/client').StringType<{
							nullable: true;
							default: null;
						}>;
					},
					{}
				>;
				passwordResetToken: import('@triplit/client').StringType<{
					nullable: true;
					default: null;
				}>;
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
		permissions: {
			user: {
				read: {
					filter: ['id', string, string][];
				};
			};
		};
	};
};
export type Garden = Entity<typeof gardenSchema, 'gardens'>;
export type GardenMembership = Entity<typeof gardenSchema, 'gardenMemberships'>;
export type GardenVisibility = (typeof GardenVisibilityEnumOptions)[number];
export type GardenRole = (typeof GardenMembershipRoleEnumOptions)[number];
export type GardenMembershipStatus = (typeof GardenMembershipStatusEnumOptions)[number];
//# sourceMappingURL=schema.d.ts.map
