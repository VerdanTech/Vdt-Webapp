import { writable } from 'svelte/store';

export const csrftoken = writable<string>('');
export const is_authenticated = writable<boolean>(false);
//export const active_garden = writable();
