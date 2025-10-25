<script lang="ts">
	import {
		type FieldErrors,
		type PlantingArea,
		type Workspace
	} from '@vdg-webapp/models';
	import {
		geometryUpdate,
		locationHistoryExtend,
		locationUpdate,
		plantingAreaUpdate
	} from '@vdg-webapp/models';

	import { EditableTree, createEditableTree, toTreeId } from '$components';
	import { plantingAreaTreeItem } from '$components';
	import { ScrollArea } from '$core';
	import { getControllerContext } from '$state';
	import createCommandHandler from '$state/commandHandler.svelte';

	import { getWorkspaceContext } from '../../../../state/context/workspacesContext.svelte';

	type Props = {
		plantingAreas: PlantingArea[];
		workspacesInGarden: Pick<Workspace, 'id' | 'name'>[];
	};
	let { plantingAreas = [], workspacesInGarden = [] }: Props = $props();

	/** The types of entities in the tree whose selections must be synchronized. */
	type TreeEntities = 'plantingArea';

	/** Workspace context. */
	const controller = getControllerContext();
	const workspaceContext = getWorkspaceContext();

	/** Stores errors of the tree fields. */
	const fieldErrors: FieldErrors = $state({});

	/** Queries. */

	/** Options for workspaces available to locations. */

	/** Handlers. */
	/** PlantingArea change. */
	const plantingAreaUpdateCommandHandler = createCommandHandler(plantingAreaUpdate);

	/** Geometry change. */
	const geometryUpdateCommandHandler = createCommandHandler(geometryUpdate);

	/** Location change. */
	const locationUpdateCommandHandler = createCommandHandler(locationUpdate);
	const locationHistoryExtendCommandHandler =
		createCommandHandler(locationHistoryExtend);

	/** Given the planting areas, construct the editable tree items. */
	let items = $derived(
		plantingAreas.map((plantingArea) => {
			return plantingAreaTreeItem(
				{ plantingArea, workspaces: workspacesInGarden },
				{
					fieldErrors,
					plantingAreaUpdateHandler: (id, data) => {
						plantingAreaUpdateCommandHandler.execute(id, data, controller);
					},
					geometryUpdateHandler: (id, data) => {
						geometryUpdateCommandHandler.execute(id, data, controller);
					},
					locationUpdateHandler: (id, data) => {
						locationUpdateCommandHandler.execute(id, data, controller);
					},
					locationHistoryExtendHandler: (id) => {
						locationHistoryExtendCommandHandler.execute(
							id,
							{ date: workspaceContext.timelineSelection.focusUtc },
							controller
						);
					}
				}
			);
		})
	);

	/** Create the editable tree. */
	const editableTree = createEditableTree<TreeEntities>(() => items, {
		/** Synchronize changes in the tree selection with the workspace context. */
		plantingArea: {
			add: (id: string) => {
				workspaceContext.selections.select('plantingArea', id);
			},
			remove: (id: string) => {
				workspaceContext.selections.deselect('plantingArea', id);
			}
		}
	});

	/** Synchronize changes in the workspace context selection with the tree selection. */
	workspaceContext.selections.addSelectionChangeHandler(
		'plantingArea',
		(addedIds, removedIds) => {
			addedIds.forEach((id) => {
				editableTree.tree.select(toTreeId('plantingArea', id));
			});

			removedIds.forEach((id) => {
				editableTree.tree.deselect(toTreeId('plantingArea', id));
			});
		}
	);
</script>

{#if plantingAreas.length === 0}
	<span class="p-2 italic"> No planting areas. </span>
{:else}
	<EditableTree {editableTree} {fieldErrors} editing={workspaceContext.editing} />
{/if}
