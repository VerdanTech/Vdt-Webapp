import { SvelteComponent } from 'svelte';
import NumberAttribute from './NumberAttribute.svelte';
import BooleanAttribute from './BooleanAttribute.svelte';

/** Maps each cultivar attribute to a component. */
const attributeComponents = {
	/** Frost date planting windows profile. */
	last_frost_window_open: NumberAttribute,
	last_frost_window_close: NumberAttribute,
	first_frost_window_open: NumberAttribute,
	first_frost_window_close: NumberAttribute,

	/** Origin profile. */
	transplantable: BooleanAttribute,

	/** Annual lifecycle profile. */
	seed_to_germ: NumberAttribute,
	germ_to_transplant: NumberAttribute,
	germ_to_first_harvest: NumberAttribute,
	first_to_last_harvest: NumberAttribute
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
