/* Store expiry of access token. 
Effect on expiry: when it changes, calculate
the time for the new one. set the timeout.
cancel the previous requests
*/
import { userRefreshCommandOp } from '$codegen';

/**
 * The number of seconds before the access token expires
 * to request a new access token.
 */
const refreshExpiryWindowSeconds = 20;

type AuthFlowState = {
	/**
	 * Stores whether the browser currently has
	 * a valid access token.
	 */
	isAuthenticated: boolean;
	/**
	 * Set to true if any authentication related
	 * mutations are underway.
	 * Used to disable queries so they don't use
	 * old credentials.
	 */
	authPriorityTaskFlag: boolean;

	/**
	 * On a received 401 return code, a
	 * token refresh is attempted.
	 * If it fails, this flag is set to true
	 * and a login should be required.
	 */
	retriedRefreshFlag: boolean;

	/**
	 * Contains the task IDs returned from the
	 * setTimeout() function, so that they may
	 * be cancelled.
	 */
	scheduledRefreshTasks: ReturnType<typeof setTimeout>[];
};

let _rune = $state<AuthFlowState>({
	isAuthenticated: true,
	authPriorityTaskFlag: false,
	retriedRefreshFlag: false,
	scheduledRefreshTasks: []
});

/**
 * Sets the authentication status of the rune to true.
 */
function setAccess() {
	_rune.isAuthenticated = true;
	_rune.retriedRefreshFlag = false;
}

/** Sets the authentication status of the rune to false. */
function removeAccess() {
	_rune.isAuthenticated = false;
}

/**
 * Calls the access token refresh endpoint.
 * The priority task flags are set to true during
 * the function so that queries may be paused.
 * If the refresh is successful, access is set
 * and a refresh task is scheduled.
 */
function requestAccessRefresh() {
	_rune.authPriorityTaskFlag = true;

	/** Call the endpoint. */
	userRefreshCommandOp()
		.then((data) => {
			setAccess();
			scheduleRefreshTask(data.expiry_time_seconds);
		})
		.catch(() => {
			removeAccess();
		});

	_rune.authPriorityTaskFlag = false;
}

/**
 * Given an access expiry time, schedule a refresh
 * task for before the token expires.
 * @param accessExpirySeconds the number of seconds until
 * the access expries.
 */
function scheduleRefreshTask(accessExpirySeconds: number) {
	/** Add a small window between refresh and expiry. */
	if (accessExpirySeconds - refreshExpiryWindowSeconds <= 0) {
		throw Error('Invalid access expiry time or refresh configuration.');
	}
	const taskTimeout = accessExpirySeconds - refreshExpiryWindowSeconds;

	/** Clear all previously scheduled refresh tasks. */
	_rune.scheduledRefreshTasks.forEach((value) => {
		clearTimeout(value);
	});

	/** Set the task with the timeout in miliseconds. */
	const taskId = setTimeout(() => {
		requestAccessRefresh();
	}, taskTimeout * 1000);
	_rune.scheduledRefreshTasks = [taskId];
}

/* Exported state methods. */
export const authentication = {
	/* Getter. */
	get value(): AuthFlowState {
		return _rune;
	},

	/**
	 * Sets access and schedules the next refresh.
	 * To be called after the login mutation is successful.
	 * @param accessExpirySeconds the number of seconds until
	 * the access expries.
	 */
	login(accessExpirySeconds: number) {
		setAccess();
		scheduleRefreshTask(accessExpirySeconds);
	},
	removeAccess,
	requestAccessRefresh
};
export default authentication;
