import { type BulkInsert } from '@triplit/client';

import { type User, schema } from '@vdg-webapp/models';

export const user: User = {
	account: {
		id: 'defaultUserAccount',
		profileId: 'defaultUser',
		passwordHash: 'password',
		unverifiedEmail: {},
		isActive: true
	},
	profile: { id: 'defaultUser', username: 'Demo User', createdAt: new Date() }
};

export default function userSeed(): BulkInsert<typeof schema> {
	return {
		profiles: [user.profile],
		accounts: [user.account]
	};
}
