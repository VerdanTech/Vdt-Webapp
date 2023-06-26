import type { AxiosRequestConfig, AxiosResponse } from 'axios';
import axios from 'axios';
import { get } from 'svelte/store';
import { csrftoken } from '$lib/stores';
import { toastStore } from '@skeletonlabs/skeleton';
import type { ToastSettings } from '@skeletonlabs/skeleton';

//Static configuration in the AXIOS_INSTANCE
export const AXIOS_INSTANCE = axios.create({
	baseURL: '/api',
	withCredentials: true,
});

//Dynamic configuration in request/response interceptors
AXIOS_INSTANCE.interceptors.request.use((config) => {
	config.headers['X-CSRFToken'] = get(csrftoken);
	return config;
});

AXIOS_INSTANCE.interceptors.response.use(
	(response) => {
		return response;
	},
	(error) => {
		if (error.response.status == 500) {
			//Server connection fail toast
			const toast: ToastSettings = {
				message: 'Error: Server connection failed (HTTP 500)',
				background: 'bg-error-500',
				autohide: true,
				timeout: 5000
			};
			toastStore.trigger(toast);
		}
		throw error;
	}
);

export const customInstance = <T>(config: AxiosRequestConfig): Promise<AxiosResponse<T>> => {
	return AXIOS_INSTANCE({ ...config });
};

export default customInstance;
