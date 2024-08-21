/* Store expiry of access token. 
Effect on expiry: when it changes, calculate
the time for the new one. set the timeout.
cancel the previous requests
*/
import { goto } from '$app/navigation'
import { userRefreshCommandOp } from '$codegen'

/**
 * The number of seconds before the access token expires
 * to request a new access token.
 */
const refreshExpiryWindowSeconds = 20

type AuthFlowState = {
	/**
	 * Stores whether the browser currently has
	 * a valid access token.
	 */
	isAuthenticated: boolean
	/**
	 * Set to true if any authentication related
	 * mutations are underway.
	 * Used to disable queries so they don't use
	 * old credentials.
	 */
	authPriorityTaskFlag: boolean

	/**
	 * On a received 401 return code, a
	 * token refresh is attempted.
	 * If it fails, this flag is set to true
	 * and a login should be required.
	 */
	retriedRefreshFlag: boolean

	/**
	 * Contains the task IDs returned from the
	 * setTimeout() function, so that they may
	 * be cancelled.
	 */
	scheduledRefreshTasks: ReturnType<typeof setTimeout>[]
}

let _rune = $state<AuthFlowState>({
	isAuthenticated: true,
	authPriorityTaskFlag: false,
	retriedRefreshFlag: false,
	scheduledRefreshTasks: []
})

function setAccess(accessExpirySeconds: number) {
	_rune.isAuthenticated = true
	_rune.retriedRefreshFlag = false
}

function removeAccess() {
	_rune.isAuthenticated = false
}

function requestAccessRefresh() {
	_rune.authPriorityTaskFlag = true

	userRefreshCommandOp()
		.then((data) => {
			setAccess(data.expiry_time_seconds)
			scheduleRefreshTask(data.expiry_time_seconds)
		})
		.catch(() => {
			removeAccess()
		})

	_rune.authPriorityTaskFlag = false
}

function scheduleRefreshTask(accessExpirySeconds: number) {
	const taskTimeout = accessExpirySeconds - refreshExpiryWindowSeconds

	_rune.scheduledRefreshTasks.forEach((value) => {
		clearTimeout(value)
	})

	const taskId: ReturnType<typeof setTimeout> = setTimeout(() => {
		requestAccessRefresh()
	}, taskTimeout * 1000)

	_rune.scheduledRefreshTasks = [taskId]
}

/* Exported state methods. */
export const authentication = {
	/* Getter. */
	get value(): AuthFlowState {
		return _rune
	},

	login(accessExpirySeconds: number) {
		setAccess(accessExpirySeconds)
		scheduleRefreshTask(accessExpirySeconds)
	},
	removeAccess,
	requestAccessRefresh
}
export default authentication
