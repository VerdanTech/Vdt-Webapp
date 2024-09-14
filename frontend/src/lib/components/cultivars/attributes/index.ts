import { SvelteComponent } from 'svelte';
import LastFrostWindowOpen from './LastFrostWindowOpen.svelte';

/** Maps each cultivar attribute to a component. */
const attributeComponents = {
	/** Frost date planting windows profile. */
	last_frost_window_open: LastFrostWindowOpen,
	last_frost_window_close: LastFrostWindowOpen,
	first_frost_window_open: LastFrostWindowOpen,
	first_frost_window_close: LastFrostWindowOpen,

	/** Origin profile. */
	transplantable: LastFrostWindowOpen,

	/** Annual lifecycle profile. */
	seed_to_germ: LastFrostWindowOpen,
	germ_to_transplant: LastFrostWindowOpen,
	germ_to_first_harvest: LastFrostWindowOpen,
	first_to_last_harvest: LastFrostWindowOpen
};
/**
 * Given a cultivar attribute key, returns the component represented by it.
 * If none is found, throws an exception
 */
export const attributeKeyToComponent = (key: string) => {
	const component = attributeComponents[key as keyof typeof attributeComponents];
	if (!component) {
		throw new Error(`No component found for attribute key: ${key}`);
	}
	return component;
};
