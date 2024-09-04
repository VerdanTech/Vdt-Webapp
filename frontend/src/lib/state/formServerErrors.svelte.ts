import { ValidationException } from '$lib/data/validationException';
import type { AxiosError } from 'axios';

/**
 * Stores the errors rerturned by the server.
 * @returns Rune factory
 */
export function createServerErrors() {
	let serverErrors = $state<Record<string, string[]>>({});

	/**
	 * Sets the errors returned by the server onto the rune.
	 * @param error The axios error returned by the server.
	 */
	function setErrors(error: AxiosError<ValidationException>) {
		const data = error?.response?.data;
		if (data && 'extra' in data) {
			for (const error of data.extra) {
				if (!serverErrors[error.key]) {
					serverErrors[error.key] = [];
				}
				serverErrors[error.key].push(error.message);
			}
		}
	}

	/**
	 * Reset the server errors.
	 */
	function reset() {
		serverErrors = {};
	}

	return {
		get errors() {
			return serverErrors;
		},
		setErrors,
		reset
	};
}
