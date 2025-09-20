import { mode } from 'mode-watcher';
import { getContext, setContext } from 'svelte';

import {
	type CanvasContext,
	createCanvasContext,
	createSelectionManager
} from '$components';
import { createTimelineSelection } from '$components';
import { createPaneSettings, isMobile } from '$state';

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

/**
 * Holds context for the verdagraph.
 */
function createVerdagraphContext() {
	const paneSettings = createPaneSettings<['tree', 'calendar', 'layout']>(
		'verdagraphPaneSettings',
		defaultTreeEnabled ? ['tree', 'calendar', 'layout'] : ['calendar', 'layout'],
		defaultContentPaneDirection
	);
	/** Timeline. */
	const timeline = createTimelineSelection();
	/** Selected entities. */
	const selections = createSelectionManager(['plantingArea']);

	/** Canvas context. */
	setContext(
		verdagraphLayoutCanvasContextId,
		createCanvasContext(verdagraphLayoutCanvasContextId, 'id', mode)
	);

	return {
		/* Getters. */
		get layoutCanvasContext() {
			return getContext<CanvasContext>(verdagraphLayoutCanvasContextId);
		},

		/** Setters. */
		paneSettings,
		timeline,
		selections
	};
}
export type VerdagraphContext = ReturnType<typeof createVerdagraphContext>;

export function setVerdagraphContext() {
	return setContext(verdagraphContextId, createVerdagraphContext());
}

export function getVerdagraphContext() {
	return getContext<VerdagraphContext>(verdagraphContextId);
}
