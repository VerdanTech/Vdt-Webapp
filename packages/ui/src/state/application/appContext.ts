import { getContext, setContext } from 'svelte';

import { type ControllerContextParams, createController } from '@vdg-webapp/models';

import { createCultivarContext } from './cultivarContext';
import { createGardenContext } from './gardenContext.svelte';
import { createPlantsContext } from './plantsContext';
import { createSettingsContext } from './userSettings.svelte';
import { createWorkspacesContext } from './workspacesContext.svelte';

const appContextKey = 'appContext';

/**
 * Holds all relevant sub-context objects.
 */
/* 
export type AppContext = {
	controller: ControllerContext;
	settings: SettingsContext
	garden: GardenContext;
	cultivars: CultivarContext;
	workspaces: WorkspacesContext;
	plants: PlantsContext;
};
*/

/**
 * Controller class: singleton interface to the data layer.
 * Passed to controller functions to provide configurable behaviour.
 * @param controllerParams Parameters for the controller context.
 * @returns ControllerContext.
 */
export function createAppContext(controllerParams: ControllerContextParams) {
	const controller = createController(controllerParams);
	const settings = createSettingsContext();
	const garden = createGardenContext(controller);
	const cultivars = createCultivarContext(controller, garden);
	const workspaces = createWorkspacesContext(controller, garden);
	const plants = createPlantsContext(controller, garden);

	return {
		controller,
		settings,
		garden,
		cultivars,
		workspaces,
		plants
	};
}
export type AppContext = ReturnType<typeof createAppContext>;

export function setAppContext(controllerParams: ControllerContextParams) {
	return setContext(appContextKey, createAppContext(controllerParams));
}

export function getAppContext() {
	return getContext<AppContext>(appContextKey);
}
