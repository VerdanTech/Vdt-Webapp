import * as Resizable from '$components/ui/resizable';

/**
 * Stores the active workspace's state
 */
type ActiveWorkspaceState = {
	activeWorkspaceId: string | null /** The ID of the active workspace. */;
	editing: boolean /** The editing state. */;
	treeEnabled: boolean /** Whether the tree pane is open. */;
	layoutEnabled: boolean /** Wether the layout pane is open. */;
	contentPaneDirection: Resizable.Direction /** Controls the orientation between the content panes. */;
};
let _rune: ActiveWorkspaceState = $state({
	activeWorkspaceId: null,
	editing: false,
	treeEnabled: true,
	layoutEnabled: true,
	contentPaneDirection: 'horizontal'
});

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
