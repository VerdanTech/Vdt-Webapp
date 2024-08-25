import iconIds from '$lib/assets/icons';
import { externalLinks } from '$lib/assets/links';
import { GardenPartialSchema } from '$codegen';

/**
 * Utility to get the base URL for the active garden.
 */
const getGardenBaseUrl = (gardenKey: string): string => {
	return '/app/gardens/' + gardenKey;
};

/**
 * @brief   Specifies the primary navigation tabs between feature domains.
 */
export type PrimaryTabSpec = {
	id: string;
	url: string;
	label: string;
	iconId: string;
	submenuItems: PrimaryTabItemSpec[] | null;
};

/**
 * @brief   Specifies the entries to the submenu of primary navigation tabs.
 */
export type PrimaryTabItemSpec = {
	url: string;
	label: string;
	iconId: string | null;
};

/**
 * Constructs the tab which lists gardens the user has access to.
 * @param gardenPartials list of partial garden schemas associated with the user.
 * @returns Tab specification for the gardens tab.
 */
export const getGardensTab = (
	gardenPartials: GardenPartialSchema[] = []
): PrimaryTabSpec => {
	return {
		id: 'gardens',
		label: 'Gardens',
		iconId: iconIds.gardensIcon,
		url: getGardenBaseUrl(''),
		submenuItems: gardenPartials.map((garden) => ({
			label: garden.name,
			url: getGardenBaseUrl(garden.key),
			iconId: null
		}))
	};
};

/**
 * Constructs the tabs of pages specific to one garden.
 * @param gardenKey Key of the active garden.
 * @returns Tab specifications for the garden tabs.
 */
export const getGardenSpecifcTabs = (gardenKey: string): PrimaryTabSpec[] => {
	return [
		{
			id: 'garden',
			label: 'Garden',
			iconId: iconIds.gardenIcon,
			url: getGardenBaseUrl(gardenKey),
			submenuItems: [
				{
					label: 'Homepage',
					url: getGardenBaseUrl(gardenKey),
					iconId: iconIds.gardenIcon
				},
				{
					label: 'Dashboard',
					url: getGardenBaseUrl(gardenKey) + '/dash',
					iconId: iconIds.gardenDashboardIcon
				},
				{
					label: 'Members',
					url: getGardenBaseUrl(gardenKey) + '/members',
					iconId: iconIds.gardenMembersIcon
				},
				{
					label: 'Metrics',
					url: getGardenBaseUrl(gardenKey) + '/metrics',
					iconId: iconIds.gardenMetricsIcon
				}
			]
		},
		{
			id: 'planner',
			label: 'Planner',
			iconId: iconIds.gardenPlannerIcon,
			url: getGardenBaseUrl(gardenKey) + '/verdagraph',
			submenuItems: [
				{
					label: 'Verdagraph',
					url: getGardenBaseUrl(gardenKey) + '/verdagraph',
					iconId: iconIds.gardenPlannerVerdagraphIcon
				},
				{
					label: 'Workbook',
					url: getGardenBaseUrl(gardenKey) + '/workbook',
					iconId: iconIds.gardenPlannerWorkbookIcon
				}
			]
		},
		{
			id: 'config',
			label: 'Configuration',
			iconId: iconIds.gardenConfigIcon,
			url: getGardenBaseUrl(gardenKey) + '/cultivars',
			submenuItems: [
				{
					label: 'Cultivars',
					iconId: iconIds.cultivarIcon,
					url: getGardenBaseUrl(gardenKey) + '/cultivars'
				},
				{
					label: 'Workspaces',
					iconId: iconIds.workspaceIcon,
					url: getGardenBaseUrl(gardenKey) + '/workspaces'
				},
				{
					label: 'Environments',
					iconId: iconIds.environmentIcon,
					url: getGardenBaseUrl(gardenKey) + '/environments'
				}
			]
		}
		//{
		//id: 'connections',
		//label: 'Connections',
		//iconId: gardenConnectionsIconId,
		//url: getGardenBaseUrl(gardenKey) + '/connections',
		//submenuItems: null
		//}
	];
};

/**
 * Constructs the non-garden specific tabs of static pages.
 * @returns Tab specifications for non-garden specific tabs.
 */
export const getNonGardenSpecificTabs = (): PrimaryTabSpec[] => {
	return [
		{
			id: 'traits',
			label: 'Traits',
			iconId: iconIds.traitsIcon,
			url: '/app/traits',
			submenuItems: [
				{
					label: 'Cultivars',
					iconId: iconIds.cultivarIcon,
					url: '/app/traits/cultivars'
				},
				{
					label: 'Workspaces',
					iconId: iconIds.workspaceIcon,
					url: '/app/traits/workspaces'
				},
				{
					label: 'Environments',
					iconId: iconIds.environmentIcon,
					url: '/app/traits/environments'
				}
			]
		},
		{
			id: 'resources',
			label: 'Resources',
			iconId: iconIds.resourcesIcon,
			url: '/guides',
			submenuItems: [
				{
					label: 'Guides',
					url: '/guides',
					iconId: iconIds.resourcesGuidesIcon
				},
				{
					label: 'Project',
					url: externalLinks.project,
					iconId: iconIds.resourcesProjectIcon
				},
				{
					label: 'Donate',
					url: externalLinks.donation,
					iconId: iconIds.resourcesDonateIcon
				}
			]
		},
		{
			id: 'profileIcon',
			label: 'ProfileName',
			iconId: iconIds.profileIcon,
			url: '/app/account',
			submenuItems: [
				{
					label: 'Notifications',
					url: '/app/notifications',
					iconId: iconIds.profileNotificationsIcon
				},
				{
					label: 'Account',
					url: '/app/account',
					iconId: iconIds.profileAccountIcon
				},
				{
					label: 'Settings',
					url: '/app/settings',
					iconId: iconIds.profileSettingsIcon
				}
			]
		}
	];
};
