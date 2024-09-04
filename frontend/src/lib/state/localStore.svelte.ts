import { browser } from '$app/environment';

/**
 * Creates a rune that perists to local storage.
 *
 * https://www.youtube.com/watch?v=HnNgkwHZIII
 */
export class LocalStore<T> {
	_rune = $state<T>() as T;
	_key = '';

	constructor(key: string, value: T) {
		this._key = key;
		this._rune = value;

		if (browser) {
			const item = localStorage.getItem(key);
			if (item) this._rune = this.deserialize(item);
		}

		$effect(() => {
			this.persist();
		});
	}

	get value(): T {
		return this._rune;
	}

	set value(newVal: T) {
		this._rune = newVal;
	}

	persist() {
		localStorage.setItem(this._key, this.serialize(this._rune));
	}

	serialize(value: T): string {
		return JSON.stringify(value);
	}

	deserialize(item: string): T {
		return JSON.parse(item);
	}
}

export function localStore<T>(key: string, value: T) {
	return new LocalStore(key, value);
}
