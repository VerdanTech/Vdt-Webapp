import type { AxiosRequestConfig, AxiosResponse } from 'axios'
import axios from 'axios'
//import { csrftoken } from '$lib/stores';

//Static configuration in the AXIOS_INSTANCE
export const AXIOS_INSTANCE = axios.create({
	baseURL: '',
	withCredentials: true
})

//Dynamic configuration in request/response interceptors
AXIOS_INSTANCE.interceptors.request.use((config) => {
	//config.headers['X-CSRFToken'] = get(csrftoken);
	return config
})

AXIOS_INSTANCE.interceptors.response.use(
	(response) => {
		return response
	},
	(error) => {
		if (error.response.status == 500) {
			//Server side error toast
			/*
			const toast: ToastSettings = {
				message: 'Error: Server failed (HTTP 500)',
				type: ToastType.Error,
				dismissable: true,
				autohide: true,
				timeout: 5000
			};
			toastStore.trigger(toast);
		}
		*/
		} else if (error.response.status == 401) {
			// Unauthenticated toast. Redirect to login page.
		}

		throw error
	}
)

export const axiosClient = <Response>(
	config: AxiosRequestConfig
): Promise<Response> => {
	return AXIOS_INSTANCE({
		...config
	})
}
export default axiosClient
