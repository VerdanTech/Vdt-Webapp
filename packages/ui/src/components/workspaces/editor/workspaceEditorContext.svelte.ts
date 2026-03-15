import { mode } from 'mode-watcher';
import { getContext, setContext } from 'svelte';
import { defaults, superForm } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';

import {
	PlantingAreaCreateCommandSchema,
	plantingAreaCreate
} from '@vdg-webapp/models';

import {
	createSelectionManager,
	createTimelineSelection,
	getCanvasContext,
	resetCanvasContext,
	setCanvasContext
} from '$components';
import { getAppContext, isMobile } from '$state';
import { createPaneSettings } from '$state';
import createCommandHandler from '$state/commandHandler.svelte';

import { workspaceToolbox } from './tools';

const workspaceContextKey = 'workspaceContext';

/**
 * TODO: Disable the tree by default on small devices.
 * Once the Layout has achieved feature parity with the Tree,
 * including editing the geometry of planting areas, this may be done.
 */
const defaultTreeEnabled = isMobile() ? true : true;

/** Organize content panes vertically on narrow screens. */
const defaultContentPaneDirection = isMobile() ? 'vertical' : 'horizontal';

/**
 * Holds context for a workspace editor.
 */
export function createWorkspaceEditorContext(id: string) {
	const ctx = getAppContext();

	/** If true, the workspace is being edited by the user. */
	let editing: boolean = $state(false);
	/** Layout canvas. */
	let canvas = setCanvasContext('workspaceLayoutCanvas', id, mode);
	/** Activated popout tools. */
	const toolbox = workspaceToolbox();
	/** Activated pane settings. */
	const paneSettings = createPaneSettings<['tree', 'layout']>(
		'workspacePaneSettings',
		defaultTreeEnabled ? ['tree', 'layout'] : ['layout'],
		defaultContentPaneDirection
	);
	/** Selected entities. */
	const selections = createSelectionManager(['plantingArea', 'environment']);
	/** Timeline. */
	const timelineSelection = createTimelineSelection(ctx.timeline);

	/** Forms. */
	const plantingAreaCreateHandler = createCommandHandler(plantingAreaCreate, {
		onSuccess: () => {
			toolbox.deactivate('plantingAreaCreate');
		}
	});
	const plantingAreaCreateSuperform = superForm(
		defaults(zod(PlantingAreaCreateCommandSchema)),
		{
			SPA: true,
			dataType: 'json',
			validators: zod(PlantingAreaCreateCommandSchema),
			onUpdate({ form }) {
				if (form.valid) {
					plantingAreaCreateHandler.execute(form.data, ctx.controller);
				}
			},
			onChange() {
				plantingAreaCreateHandler.reset();
			}
		}
	);

	/**
	 * Resets the context to a null state.
	 */
	function reset() {
		editing = false;
		selections.resetAll();
		plantingAreaCreateSuperform.reset();
		canvas = resetCanvasContext('workspaceLayoutCanvas', id, mode);
	}

	return {
		get id() {
			return id;
		},
		/* Getters. */
		get editing(): boolean {
			return editing;
		},
		get layoutCanvasContext() {
			return getCanvasContext('workspaceLayoutCanvas');
		},

		/* Setters. */
		canvas,
		toolbox,
		paneSettings,
		set editing(newVal: boolean) {
			editing = newVal;
		},
		timelineSelection,
		selections,
		plantingAreaCreateForm: {
			handler: plantingAreaCreateHandler,
			form: plantingAreaCreateSuperform
		},
		reset
	};
}
export type WorkspaceContext = ReturnType<typeof createWorkspaceEditorContext>;

export function setWorkspaceEditorContext(id: string) {
	return setContext(workspaceContextKey, createWorkspaceEditorContext(id));
}

export function getWorkspaceEditorContext() {
	return getContext<WorkspaceContext>(workspaceContextKey);
}
