<script lang="ts">
	import {
		type FieldErrors,
		type Plant,
		type Workspace,
		plantUpdate,
		lifespanUpdate,
		geometryUpdate,
		locationUpdate,
		locationHistoryExtend,
		geometryHistoryExtend,
		observationUpdate,
		observationDelete
	} from '@vdg-webapp/models';

	import { EditableTree, createEditableTree, toTreeId } from '$components';
	import { plantTreeItem } from '$components';
	import { ScrollArea } from '$core';
	import { getAppContext } from '$state';
	import createCommandHandler from '$state/commandHandler.svelte';

	import { getVerdagraphContext } from './verdagraphContext.svelte';

	type Props = {
		plants: Plant[];
		workspaces: Pick<Workspace, 'id' | 'name'>[];
	};
	let { plants = [], workspaces = [] }: Props = $props();

	/** The types of entities in the tree whose selections must be synchronized. */
	type TreeEntities = 'plant';

	/** Contexts. */
	const ctx = getAppContext();
	const verdagraphContext = getVerdagraphContext();

	/** Stores errors of the tree fields. */
	const fieldErrors: FieldErrors = $state({});

	/** Handlers. */
	/** Plant change. */
	const plantUpdateCommandHandler = createCommandHandler(plantUpdate);

	/** Lifespan change. */
	const lifespanUpdateCommandHandler = createCommandHandler(lifespanUpdate);

	/** Geometry change. */
	const geometryUpdateCommandHandler = createCommandHandler(geometryUpdate);

	/** Location change. */
	const locationUpdateCommandHandler = createCommandHandler(locationUpdate);
	const locationHistoryExtendCommandHandler =
		createCommandHandler(locationHistoryExtend);

	/** Geometry history change. */
	const geometryHistoryExtendCommandHandler =
		createCommandHandler(geometryHistoryExtend);

	/** Observation change. */
	const observationUpdateCommandHandler = createCommandHandler(observationUpdate);

	/** Observation delete. */
	const observationDeleteCommandHandler = createCommandHandler(observationDelete);

	/** Given the plants, construct the editable tree items. */
	let items = $derived(
		plants.map((plant) => {
			return plantTreeItem(
				{ plant, workspaces },
				{
					fieldErrors,
					plantUpdateHandler: (id, data) => {
						plantUpdateCommandHandler.execute(id, data, ctx.controller);
					},
					lifespanUpdateHandler: (id, data) => {
						lifespanUpdateCommandHandler.execute(id, data, ctx.controller);
					},
					geometryUpdateHandler: (id, data) => {
						geometryUpdateCommandHandler.execute(id, data, ctx.controller);
					},
					locationUpdateHandler: (id, data) => {
						locationUpdateCommandHandler.execute(id, data, ctx.controller);
					},
					locationHistoryExtendHandler: (id) => {
						locationHistoryExtendCommandHandler.execute(
							id,
							{ date: verdagraphContext.timeline.focusUtc },
							ctx.controller
						);
					},
					geometryHistoryExtendHandler: (id) => {
						geometryHistoryExtendCommandHandler.execute(
							id,
							verdagraphContext.timeline.focusUtc,
							ctx.controller
						);
					},
					observationUpdateHandler: (data) => {
						observationUpdateCommandHandler.execute(data, ctx.controller);
					},
					observationDeleteHandler: (id) => {
						observationDeleteCommandHandler.execute(id, ctx.controller);
					}
				}
			);
		})
	);

	/** Create the editable tree. */
	const editableTree = createEditableTree<TreeEntities>(() => items, {
		/** Synchronize changes in the tree selection with the verdagraph context. */
		plant: {
			add: (id: string) => {
				verdagraphContext.selections.select('plants', id);
			},
			remove: (id: string) => {
				verdagraphContext.selections.deselect('plants', id);
			}
		}
	});

	/** Synchronize changes in the verdagraph context selection with the tree selection. */
	verdagraphContext.selections.addSelectionChangeHandler(
		'plants',
		(addedIds, removedIds) => {
			addedIds.forEach((id) => {
				editableTree.tree.select(toTreeId('plant', id));
			});

			removedIds.forEach((id) => {
				editableTree.tree.deselect(toTreeId('plant', id));
			});
		}
	);
</script>

{#if plants.length === 0}
	<span class="p-2 italic"> No plants. </span>
{:else}
	<EditableTree {editableTree} {fieldErrors} editing={verdagraphContext.editing} />
{/if}
