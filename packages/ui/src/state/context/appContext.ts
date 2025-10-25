import { getContext, setContext } from 'svelte';

import { createController } from '@vdg-webapp/models';

import { type ControllerContextParams } from '../../../../models/src/controller';
import { createCultivarContext } from './cultivarContext';
import { createGardenContext } from './gardenContext.svelte';
import { createWorkspacesContext } from './workspacesContext.svelte';

const appContextKey = 'appContext';

/**
 * Holds all relevant sub-context objects.
 */

/**
 * Controller class: singleton interface to the data layer.
 * Passed to controller functions to provide configurable behaviour.
 * @param controllerParams Parameters for the controller context.
 * @returns ControllerContext.
 */
export function createAppContext(controllerParams: ControllerContextParams) {
	const controller = setContext(
		'controllerContext',
		createController(controllerParams)
	);
	const garden = setContext('gardenContext', createGardenContext(controller));
	const cultivars = setContext(
		'cultivarsContext',
		createCultivarContext(controller, garden)
	);
	const workspaces = setContext('workspacesContext', createWorkspacesContext());

	return {
		controller,
		garden,
		cultivars,
		workspaces
	};
}
export type AppContext = ReturnType<typeof createAppContext>;

export function setAppContext(controllerParams: ControllerContextParams) {
	return setContext(appContextKey, createAppContext(controllerParams));
}

export function getAppContext() {
	return getContext<AppContext>(appContextKey);
}
