import { getContext, setContext } from 'svelte';

import { type ControllerContextParams, createController } from '@vdg-webapp/models';

import { type ClientContextParams, createClientContext } from './client.svelte';
import { createCultivarContext } from './cultivarContext.svelte';
import { createGardenContext } from './gardenContext.svelte';
import { createPlantsContext } from './plantsContext.svelte';
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
export function createAppContext(
	controllerParams: ControllerContextParams,
	clientParams?: ClientContextParams
) {
	const controller = setContext('controller', createController(controllerParams));
	const client = setContext('client', createClientContext(controller, clientParams));
	const settings = setContext('settings', createSettingsContext());
	const garden = setContext('garden', createGardenContext(controller, client));
	const cultivars = setContext('cultivars', createCultivarContext(controller, garden));
	const workspaces = setContext(
		'workspaces',
		createWorkspacesContext(controller, garden)
	);
	const plants = setContext('plants', createPlantsContext(controller, garden));

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

export function setAppContext(
	controllerParams: ControllerContextParams,
	clientParams?: ClientContextParams
) {
	return setContext(appContextKey, createAppContext(controllerParams, clientParams));
}

export function getAppContext() {
	return getContext<AppContext>(appContextKey);
}
