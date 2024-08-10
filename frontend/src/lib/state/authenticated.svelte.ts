/**
 * Stores whether the user is authenticated.
 */

let _rune: boolean = $state(false)

/* Exported state methods. */
export const isAuthenticated = {
	/* Getter. */
	get value(): boolean {
		return _rune
	},

	/* Setter. */
	set value(newVal: boolean) {
		_rune = newVal
	}
}
export default isAuthenticated
