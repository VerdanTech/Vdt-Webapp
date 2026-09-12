<script lang="ts">
	import { getContext } from 'svelte';

	import { type Geometry, type GeometryUpdateCommand, type Position } from '@vdg-webapp/models';

	import { getColor } from '$utils';

	import type { CanvasContext } from '../state';
	import EditableShape from './EditableShape.svelte';

	type Props = {
		/** The ID of the canvas. */
		canvasId: string;
		/** Name of the plant. Can be disabled */
		name: string;
		showName: boolean;
		/** The current position of the plant in the workspace, in model quantity (meters). */
		position: Position | null;
		/** The geometry of the plant. */
		geometry: Omit<Geometry, 'id' | 'gardenId' | 'linesCoordinateIds' | 'date'>;
		/** If true, the plant may be moved and resized. */
		editable: boolean;
		/** If true, the plant is selected. */
		selected: boolean;
		labelTranslate?: Position;
		/** The grid attributes of the plant. */
		grid?: { numRows: number; numCols: number };
		/** Called when the position is moved in the canvas. */
		onTranslate?: (
			/** The new position, in canvas quantity (pixels). */
			newPos: Position,
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
		/** Called when the plant is clicked. */
		onClick?: () => void;
	};
	let {
		canvasId,
		name,
		showName = true,
		position,
		geometry,
		editable,
		selected,
		labelTranslate = { x: 0, y: 0 },
		onTranslate,
		onTransform,
		onClick
	}: Props = $props();

	/** Retrieve canvas. */
	const canvas = getContext<CanvasContext>(canvasId);

	/**
	 * Shape style settings.
	 */
	let strokeColor = $derived(
		selected
			? getColor('lime', 8, canvas.mode.current)
			: getColor('green', 10, canvas.mode.current)
	);
	let fillColor = $derived(
		selected
			? getColor('lime', 5, canvas.mode.current)
			: getColor('green', 3, canvas.mode.current)
	);
	let strokeWidth = $derived(selected ? 3 : 2);
	let nameTextFillColor = $derived(
		selected
			? getColor('lime', 11, canvas.mode.current)
			: getColor('green', 11, canvas.mode.current)
	);
</script>

<EditableShape
	{canvasId}
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
