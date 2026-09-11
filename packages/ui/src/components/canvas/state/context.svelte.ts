import { mode } from 'mode-watcher';
import { getContext, setContext } from 'svelte';

import createCanvasContainer from './container.svelte';
import createCanvasGridManager from './grid.svelte';
import createSelectionGroup from './selectionGroup.svelte';
import createCanvasTransform from './transform.svelte';

type ModeStore = typeof mode;

export * from './transform.svelte';

type CanvasOptions = {
	/** The draggable property for the stage. */
	draggable?: boolean;
	/** The default value for strokeScaleEnabled for shapes. */
	strokeScale?: boolean;
};

/**
 * The Canvas Context provides access to all canvas state
 * that must be shared amongst components.
 * Note that one canvas represents one workspace.
 * @param canvasId Unique identifier for this canvas.
 * @param canvasWorkspaceId The ID of the workspace represented in the canvas.
 * @param mode Access to the ModeWatcher current store value.
 * @param strokeScale: The default value for strokeScaleEnabled for shapes.
 * @returns The canvas contexts.
 */
export function createCanvasContext(
	canvasContextId: string,
	canvasWorkspaceId: string,
	mode: ModeStore,
	options: CanvasOptions = {}
) {
	const canvasId = canvasContextId;
	const workspaceId = canvasWorkspaceId;

	/** Sub-contexts. */
	const container = createCanvasContainer(canvasId);
	const transform = createCanvasTransform(
		container,
		options.draggable || true,
		options.strokeScale || true
	);
	const selectionGroup = createSelectionGroup();
	const gridManager = createCanvasGridManager(container, transform);

	/**
	 * Initialize sub-contexts.
	 * Where applicable, sub-contexts are initialized by their
	 * associated component. Otherwise, they are initialized here.
	 */
	function initialize() {
		container.initialize();
		transform.initialize();
	}

	/**
	 * Destroy the canvas. No-op now that there is no imperative Stage
	 * instance to tear down, kept so `resetCanvasContext` has a stable
	 * function to call.
	 */
	function destroy() {}

	return {
		get canvasId() {
			return canvasId;
		},
		get workspaceId() {
			return workspaceId;
		},
		transform,
		container,
		selectionGroup,
		gridManager,
		initialize,
		destroy,
		mode
	};
}
export default createCanvasContext;
export type CanvasContext = ReturnType<typeof createCanvasContext>;

/**
 * Creates a canvas context and sets it in svelte context.
 * @param canvasContextId ID of the context in svelte context.
 * @param canvasWorkspaceId The ID of the workspace the canvas is representing.
 * @param mode A mode store from mode-watcher.
 * @param options Options for the canvas
 * @returns The canvas context after creation.
 */
export function setCanvasContext(
	canvasContextId: string,
	canvasWorkspaceId: string,
	mode: ModeStore,
	options: CanvasOptions = {}
) {
	return setContext<CanvasContext>(
		canvasContextId,
		createCanvasContext(canvasContextId, canvasWorkspaceId, mode, options)
	);
}

/**
 * Retrieves the current canvas context from svelte context.
 * @param canvasContextId ID of the context in svelte context.
 * @returns The canvas context.
 */
export function getCanvasContext(canvasContextId: string) {
	return getContext<CanvasContext>(canvasContextId);
}

/**
 * Destroys the current canvas context in svelte context,
 * creates a new context and sets it back in svelte context.
 * @param canvasContextId ID of the context in svelte context.
 * @param canvasWorkspaceId The ID of the workspace the canvas is representing.
 * @param mode A mode store from mode-watcher.
 * @param options Options for the canvas
 * @returns The new canvas context after creation.
 */
export function resetCanvasContext(
	canvasContextId: string,
	canvasWorkspaceId: string,
	mode: ModeStore,
	options: CanvasOptions = {}
) {
	const canvas = getContext<CanvasContext>(canvasContextId);
	if (canvas) {
		canvas.destroy();
	}
	return setContext<CanvasContext>(
		canvasContextId,
		createCanvasContext(canvasContextId, canvasWorkspaceId, mode, options)
	);
}
