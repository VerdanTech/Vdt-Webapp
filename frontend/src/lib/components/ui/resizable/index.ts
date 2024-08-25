import { Pane } from 'paneforge';
import Handle from './resizable-handle.svelte';
import PaneGroup from './resizable-pane-group.svelte';

export type Direction = 'horizontal' | 'vertical';

export {
	PaneGroup,
	Pane,
	Handle,
	//
	PaneGroup as ResizablePaneGroup,
	Pane as ResizablePane,
	Handle as ResizableHandle
};
