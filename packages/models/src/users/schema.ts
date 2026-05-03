/** Minimal user profile shape used by controllers. */
export interface UserProfile {
	id: string;
	username: string;
}

/** Minimal user account shape used by controllers. */
export interface UserAccount {
	id: string;
	profileId: string;
}

/** Authenticated user: account paired with profile. */
export interface User {
	account: UserAccount;
	profile: UserProfile;
}
