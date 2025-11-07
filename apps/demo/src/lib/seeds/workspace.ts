import { type BulkInsert } from '@triplit/client';

import { type Workspace, schema } from '@vdg-webapp/models';

import { garden } from './garden';

export const workspace: Workspace = {
	id: 'workspaceId',
	gardenId: garden.id,
	name: 'Workspace',
	slug: 'workspace',
	description: ''
};

export default function workspacesSeed(): BulkInsert<typeof schema> {
	return {
		workspaces: [workspace]
	};
}
