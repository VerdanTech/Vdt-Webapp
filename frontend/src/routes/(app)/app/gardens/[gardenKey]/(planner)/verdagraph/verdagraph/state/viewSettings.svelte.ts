import * as Resizable from '$components/ui/resizable';
import { localStore } from '$lib/state/localStore.svelte';

type contentPaneType = 'tree' | 'calendar' | 'layout';

export type VerdagraphViewSettings = {
	/** Controls which of the content panes are open at once. */
	treeEnabled: boolean;
	calendarEnabled: boolean;
	layoutEnabled: boolean;

	/** Controls the orientation between the content panes and the form pane. */
	formPaneDirection: Resizable.Direction;
	/** Controls the orientation between the content panes. */
	contentPaneDirection: Resizable.Direction;

	/** Minimum size a single content pane can take up in the content panes pane, in percent. */
	minContentPaneSize: number;
};

export default function createViewSettings() {
	let _store = localStore<VerdagraphViewSettings>('verdagraphViewSettings', {
		treeEnabled: true,
		calendarEnabled: true,
		layoutEnabled: true,
		formPaneDirection: 'horizontal',
		contentPaneDirection: 'horizontal',
		minContentPaneSize: 10
	});

	return {
		get value(): VerdagraphViewSettings {
			return _store.value;
		},
		set value(newVal: VerdagraphViewSettings) {
			_store.value = newVal;
		}
	};
}
