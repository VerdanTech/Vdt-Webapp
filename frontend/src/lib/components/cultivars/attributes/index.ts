import { SvelteComponent } from "svelte";
import LastFrostWindowOpen from "./LastFrostWindowOpen.svelte";

/** Maps each cultivar attribute to a component. */
const attributeComponents = 
{
        /** Frost date planting windows profile. */
        'last_frost_window_open': LastFrostWindowOpen
    }
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
}