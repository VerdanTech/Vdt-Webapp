import { type BulkInsert } from '@triplit/client';

import { type Garden, schema } from '@vdg-webapp/models';

import { user } from './user';

export const garden: Garden = {
	id: 'gardenId',
	name: 'Garden',
	visibility: 'PUBLIC',
	isActive: true,
	adminIds: new Set([user.profile.id]),
	editorIds: new Set(),
	viewerIds: new Set(),
	createdAt: new Date()
};

export default function gardenSeed(): BulkInsert<typeof schema> {
	return {
		gardens: [garden]
	};
}
