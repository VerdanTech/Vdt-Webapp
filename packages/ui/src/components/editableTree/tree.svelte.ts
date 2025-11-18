import { Tree } from 'melt/builders';

import type { Item } from './types';
import { fromTreeId } from './utils';

/**
 * Creates a container for a Melt-UI tree,
 * allowing editing of items and synchronization
 * of selection state with app selections.
 * @param items A getter for the tree items.
 * @param entitySelectionHandlers Handlers for adding
 * and removing selected tree items to/from app selections.
 * @param onSelectedChange Called when the tree selection changes,
 * after the synchronization has happened.
 * @returns Editable tree.
 */
export function createEditableTree<EntityTypeT extends string>(
	items: () => Item[],
	entitySelectionHandlers: Record<
		EntityTypeT,
		{ add: (id: string) => void; remove: (id: string) => void }
	>,
	onSelectedChange?: (value: Set<string>) => void
) {
	/** Stores a previous selection for diffing. */
	let previousSelection: Set<string> = new Set();

	/**
	 * Diffs the previous and new selections to find the IDs which
	 * have been added and removed, then calls the appropriate handlers.
	 * @param newSelection The new selection returned by Melt.
	 */
	function onSelectedChangeHandler(newSelection: Set<string>) {
		/** Get items that have been added and remoeved. */
		const addedIds = newSelection.difference(previousSelection);
		const removedIds = previousSelection.difference(newSelection);

		/** Add all selected items to the workspace context. */
		for (const id of addedIds) {
			const { entityType, entityId } = fromTreeId<EntityTypeT>(id);
			entitySelectionHandlers[entityType].add(entityId);
		}

		/** Remove unselected items from the workspace context. */
		for (const id of removedIds) {
			const { entityType, entityId } = fromTreeId<EntityTypeT>(id);
			entitySelectionHandlers[entityType].remove(entityId);
		}

		previousSelection = new Set([...newSelection]);

		if (onSelectedChange) {
			onSelectedChange(newSelection);
		}
	}

	/** The Melt-UI builder. */
	const tree = new Tree({
		items: items,
		expandOnClick: true,
		multiple: true,
		onSelectedChange: onSelectedChangeHandler
	});

	return {
		tree
	};
}
export type EditableTreeContext = ReturnType<typeof createEditableTree>;
