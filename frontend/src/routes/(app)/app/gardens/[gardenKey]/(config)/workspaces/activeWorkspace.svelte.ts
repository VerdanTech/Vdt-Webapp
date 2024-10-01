/**
 * Stores the active workspace's state
 */
type ActiveWorkspaceState = {
	activeWorkspaceId: string | null /** The ID of the active workspace. */;
	editing: boolean /** The editing state. */;
};
let _rune: ActiveWorkspaceState = $state({ activeWorkspaceId: null, editing: false });

/* Exported state methods. */
export const activeWorkspace = {
	/* Getter. */
	get value(): ActiveWorkspaceState {
		return _rune;
	},

	/* Setter. */
	set value(newVal: ActiveWorkspaceState) {
		_rune = newVal;
	}
};
export default activeWorkspace;
