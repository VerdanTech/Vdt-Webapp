import { getContext, setContext } from 'svelte';
import { defaults, superForm } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';

import {
	type CanvasContext,
	Resizable,
	createCanvasContext,
	createSelectionManager,
	createTimelineSelection,
	isMobile,
	localStore
} from '@vdg-webapp/ui';

import { plantingAreaCreate } from '$data/workspaces/commands';
import createCommandHandler from '$state/commandHandler.svelte';

import toolbox from './tools';

/**
 * Holds context for the actively opened workspace editor.
 */
function createWorkspaceEditorContext() {
	/** The ID of the active workspace. */
	let activeWorkspaceId: string | null = $state(null);
	let activeWorkspace = createWorkspaceEditorContext();

	/**
	 * Resets the context to a null state.
	 */
	function reset() {
		activeWorkspaceId = null;
		activeWorkspace.reset();
	}

	/** Set a new workspace as the active one. */
	function setWorkspace(id: string) {
		reset();
		activeWorkspaceId = id;
		setContext(
			workspaceLayoutCanvasContextId,
			createCanvasContext(workspaceLayoutCanvasContextId, id)
		);
	}

	return {
		/* Getters. */
		get id(): string | null {
			return activeWorkspaceId;
		},
		plantingAreaCreateForm: {
			handler: plantingAreaCreateHandler,
			form: plantingAreaCreateSuperform
		},
		reset,
		setWorkspace
	};
}
export type WorkspaceContext = ReturnType<typeof createWorkspaceEditorContext>;

export function setWorkspaceContext() {
	return setContext(workspaceContextId, createWorkspaceEditorContext());
}

export function getWorkspaceContext() {
	return getContext<WorkspaceContext>(workspaceContextId);
}
