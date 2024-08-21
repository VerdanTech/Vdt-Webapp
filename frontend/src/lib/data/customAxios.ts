import type { AxiosRequestConfig, AxiosResponse } from 'axios'
import axios from 'axios'
import { goto } from '$app/navigation'
import { toast } from 'svelte-sonner'
import authentication from '$state/authentication.svelte'
//import { csrftoken } from '$lib/stores';

//Static configuration in the AXIOS_INSTANCE
export const AXIOS_INSTANCE = axios.create({
	baseURL: 'http://localhost:8000',
	withCredentials: true
})

//Dynamic configuration in request/response interceptors
AXIOS_INSTANCE.interceptors.request.use((config) => {
	//config.headers['X-CSRFToken'] = get(csrftoken);
	return config
})

AXIOS_INSTANCE.interceptors.response.use(
	(response) => {
		return response.data
	},
	(error) => {
		if (!error.response) {
			return
		}

		if (error.response.status === 401) {
			authentication.removeAccess()

			if (authentication.value.retriedRefreshFlag) {
				goto('login')
			} else {
				authentication.value.retriedRefreshFlag = true
				authentication.requestAccessRefresh()
			}
		} else {
			if (error.response.data.non_form_errors) {
				for (error in error.response.data.non_form_errors) {
					/** Toast */
					toast(error)
				}
			}
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
