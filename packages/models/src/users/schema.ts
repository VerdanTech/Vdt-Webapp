/** Minimal user profile shape used by controllers. */
export type UserProfile = {
	id: string;
	username: string;
};

/** Minimal user account shape used by controllers. */
export type UserAccount = {
	id: string;
	profileId: string;
};

/** Authenticated user: account paired with profile. */
export type User = {
	account: UserAccount;
	profile: UserProfile;
};
