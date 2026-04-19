import { co, z } from 'jazz-tools';

import { CultivarCollectionSchema } from '../cultivars/schema.js';
import { GardenSchema } from '../gardens/schema.js';

const UserRootSchema = co.map({
	email: z.optional(z.email()),
	gardens: co.list(GardenSchema),
	cultivarCollections: co.list(CultivarCollectionSchema)
});

export const UserProfileSchema = co.profile({
	name: z.string()
});

export const UserSchema = co.account({
	root: UserRootSchema,
	profile: UserProfileSchema
});

export type User = co.loaded<typeof UserSchema>;
export type UserProfile = co.loaded<typeof UserProfileSchema>;
