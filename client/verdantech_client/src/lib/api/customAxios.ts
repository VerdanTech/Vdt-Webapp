import type { Axios, AxiosRequestConfig } from 'axios';
import axios from 'axios';
import { get } from 'svelte/store';
import { csrftoken } from '$lib/stores/csrftoken';

export const AXIOS_INSTANCE = axios.create({
	headers: { 'X-CSRFToken': get(csrftoken) },
	withCredentials: true
});

function createAxiosResponseInterceptor(axiosInstance: any) {
	const interceptor = axiosInstance.interceptors.request.use(
		(config: AxiosRequestConfig): AxiosRequestConfig => {
			//config.headers['X-CSRFToken'] = get(csrftoken)
			return config;
		}
	);
}

createAxiosResponseInterceptor(AXIOS_INSTANCE);

export const customInstance = <T>(
	config: AxiosRequestConfig,

	options?: AxiosRequestConfig
): Promise<T> => {
	const source = axios.CancelToken.source();

	const promise = AXIOS_INSTANCE({
		...config,

		...options,

		cancelToken: source.token
	}).then(({ data }) => data);

	// @ts-ignore

	promise.cancel = () => {
		source.cancel('Query was cancelled');
	};

	return promise;
};

//export default AXIOS_INSTANCE
