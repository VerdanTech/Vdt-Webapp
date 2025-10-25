import { mode } from 'mode-watcher';
import { getContext, setContext } from 'svelte';
import { defaults, superForm } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';

import {
	CONTROLLER_CONTEXT_ID,
	type ControllerContext,
	PlantsCreateCommandSchema,
	plantsCreate
} from '@vdg-webapp/models';

import {
	type CanvasContext,
	createCanvasContext,
	createSelectionManager
} from '$components';
import { createTimelineSelection } from '$components';
import { createPaneSettings, isMobile } from '$state';
import createCommandHandler from '$state/commandHandler.svelte';

import { verdagraphToolbox } from './tools';

const verdagraphContextId = 'verdagraphEditorContext';
const verdagraphLayoutCanvasContextId = 'verdagraphLayoutCanvas';

/**
 * TODO: Disable the tree by default on small devices.
 * Once the Layout has achieved feature parity with the Tree,
 * including editing the geometry of plantings, this may be done.
 */
const defaultTreeEnabled = isMobile() ? true : true;

/** Organize content panes vertically on narrow screens. */
const defaultContentPaneDirection = isMobile() ? 'vertical' : 'horizontal';

export type VerdagraphContextParams = {
	defaultSelectedWorkspaceId: string;
};

/**
 * Holds context for the verdagraph.
 */
export function createVerdagraphContext(params: VerdagraphContextParams) {
	/** Controller reference. */
	const controller = getContext<ControllerContext>(CONTROLLER_CONTEXT_ID);

	const paneSettings = createPaneSettings<['tree', 'calendar', 'layout']>(
		'verdagraphPaneSettings',
		defaultTreeEnabled ? ['tree', 'calendar', 'layout'] : ['calendar', 'layout'],
		defaultContentPaneDirection
	);
	const toolbox = verdagraphToolbox();
	/** Timeline. */
	const timeline = createTimelineSelection();
	/** Selected entities. */
	const selections = createSelectionManager(['workspace', 'plantingArea']);
	selections.select('workspace', params.defaultSelectedWorkspaceId);

	/** Canvas context. */
	setContext(
		verdagraphLayoutCanvasContextId,
		createCanvasContext(verdagraphLayoutCanvasContextId, 'id', mode)
	);

	/** Forms. */
	const plantsCreateHandler = createCommandHandler(plantsCreate, {
		onSuccess: () => {
			toolbox.deactivate('plantsCreate');
		}
	});
	const plantsCreateSuperform = superForm(defaults(zod(PlantsCreateCommandSchema)), {
		SPA: true,
		dataType: 'json',
		validators: zod(PlantsCreateCommandSchema),
		onUpdate({ form }) {
			if (form.valid) {
				plantsCreateHandler.execute(form.data, controller);
			}
		},
		onChange() {
			plantsCreateHandler.reset();
		}
	});

	return {
		/* Getters. */
		get layoutCanvasContext() {
			return getContext<CanvasContext>(verdagraphLayoutCanvasContextId);
		},

		/** Setters. */
		paneSettings,
		timeline,
		selections,
		toolbox,
		plantsCreateForm: {
			handler: plantsCreateHandler,
			form: plantsCreateSuperform
		}
	};
}
export type VerdagraphContext = ReturnType<typeof createVerdagraphContext>;

export function setVerdagraphContext(params: VerdagraphContextParams) {
	return setContext(verdagraphContextId, createVerdagraphContext(params));
}

export function getVerdagraphContext() {
	return getContext<VerdagraphContext>(verdagraphContextId);
}
