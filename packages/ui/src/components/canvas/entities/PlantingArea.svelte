<script lang="ts">
	import type { Vector2d } from 'konva/lib/types';
	import { getContext } from 'svelte';

	import { type Geometry, type GeometryUpdateCommand } from '@vdg-webapp/models';

	import { getColor } from '$utils';

	import type { CanvasContext } from '../state';
	import EditableShape from './EditableShape.svelte';

	type Props = {
		/** The ID of the canvas. */
		canvasId: string;
		/** The ID of the layer which holds the planting areas. */
		layerId: string;
		/** Name of the planting area. Can be disabled */
		name: string;
		showName: boolean;
		/** The current position of the planting area in the workspace, in model quantity (meters). */
		position: Vector2d | null;
		/** The geometry of the planting area. */
		geometry: Omit<Geometry, 'id' | 'gardenId' | 'linesCoordinateIds' | 'date'>;
		/** If true, the planting area may be moved and resized. */
		editable: boolean;
		/** If true, the planting area is selected. */
		selected: boolean;
		labelTranslate?: Vector2d;
		/** The grid attributes of the planting area. */
		grid?: { numRows: number; numCols: number };
		/** Called when the position is moved in the canvas. */
		onTranslate?: (
			/** The new position, in canvas quantity (pixels). */
			newPos: Vector2d,
			/** If true, the movement has ended (dragend).*/
			movementOver: boolean
		) => void;
		/** Called when the geometry is transformed in the canvas. */
		onTransform?: (
			/** The updated geometry attributes after transformation. */
			newGeometry: GeometryUpdateCommand,
			/** If true, the transform has ended.*/
			transformOver: boolean
		) => void;
		/** Called when the planting area is clicked. */
		onClick?: () => void;
	};
	let {
		canvasId,
		layerId,
		name,
		showName = true,
		position,
		geometry,
		editable,
		selected,
		labelTranslate = { x: 0, y: 0 },
		// grid,
		onTranslate,
		onTransform,
		onClick
	}: Props = $props();

	/** Retrieve canvas and initialize Konva constructs. */
	const canvas = getContext<CanvasContext>(canvasId);

	/**
	 * Shape style settings.
	 */
	let strokeColor = $derived(
		selected
			? getColor('accent', 8, canvas.mode.current)
			: getColor('brown', 10, canvas.mode.current)
	);
	let fillColor = $derived(
		selected
			? getColor('accent', 5, canvas.mode.current)
			: getColor('brown', 3, canvas.mode.current)
	);
	let strokeWidth = $derived(selected ? 3 : 2);
	let nameTextFillColor = $derived(
		selected
			? getColor('accent', 11, canvas.mode.current)
			: getColor('brown', 11, canvas.mode.current)
	);
</script>

<EditableShape
	{canvasId}
	{layerId}
	{name}
	{showName}
	{position}
	{geometry}
	{editable}
	{selected}
	{strokeColor}
	{fillColor}
	{nameTextFillColor}
	{strokeWidth}
	{labelTranslate}
	{onTranslate}
	{onTransform}
	{onClick}
/>
