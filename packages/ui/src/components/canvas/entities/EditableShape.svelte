<script lang="ts">
	import Konva from 'konva';
	import type { Vector2d } from 'konva/lib/types';
	import { getContext, onDestroy } from 'svelte';

	import {
		type Geometry,
		type GeometryUpdateCommand,
		getGeometryHeight
	} from '@vdg-webapp/models';

	import { getColor } from '$utils';

	import type { CanvasContext } from '../state';
	import { type SupportedShape, getClosedShape, updateShape } from '../utils';
	import EditableGeometryResizePoints from './EditableGeometryResizePoints.svelte';

	type Props = {
		/** The ID of the canvas. */
		canvasId: string;
		/** The ID of the layer which holds the shape. */
		layerId: string;
		/** Name of the planting area. Can be disabled */
		name: string;
		showName: boolean;
		/** The current position of the shape in the workspace, in model quantity (meters). */
		position: Vector2d | null;
		/** The geometry of the shape. */
		geometry: Omit<Geometry, 'id' | 'gardenId' | 'linesCoordinateIds' | 'date'>;
		/** If true, the shape may be moved and resized. */
		editable: boolean;
		/** If true, the shape is selected. */
		selected: boolean;
		/** Styles. */
		strokeColor: string;
		fillColor: string;
		nameTextFillColor: string;
		strokeWidth: number;
		/** Constant to add to the label's position. */
		labelTranslate?: Vector2d;
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
		/** Called when the shape is clicked. */
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
		strokeColor,
		fillColor,
		nameTextFillColor,
		strokeWidth,
		labelTranslate = { x: 0, y: 0 },
		onTranslate,
		onTransform: onTransformContainer,
		onClick
	}: Props = $props();

	/** The number of pixels the label is offset from the top of the shape. */
	const LABEL_OFFSET_PX = 10;

	/** Retrieve canvas and initialize Konva constructs. */
	const canvas = getContext<CanvasContext>(canvasId);
	const layer = canvas.container.getLayer(layerId);
	const group: Konva.Group = new Konva.Group({ draggable: editable });
	layer.add(group);

	/** Shapes. */
	let shape: SupportedShape | null = null;
	let nameText = new Konva.Text({
		fontFamily: 'sans',
		fontSize: 15,
		opacity: 0.7,
		text: name,
		visible: showName
	});
	group.add(nameText);

	/**
	 * Store the geometry type.
	 * If the geometry type is changed, a new shape may be rendered.
	 * Otherwise, the current shape can simply be updated.
	 */
	let previousGeometryType = geometry.type;

	/** Update shapes upon geometry change. */
	$effect(() => {
		/** If the geometry type has changed or the shape hasn't been initialized, initialize. */
		if (geometry.type !== previousGeometryType || !shape) {
			shape?.destroy();
			shape = getClosedShape(canvas, geometry, {
				stroke: strokeColor,
				fill: fillColor,
				strokeWidth: strokeWidth
			});
			if (shape) {
				group.add(shape);
				group.rotation(geometry.rotation);
				nameText.y(
					canvas.transform.canvasYPos(getGeometryHeight(geometry) + labelTranslate.y)
				);
				nameText.x(canvas.transform.canvasXPos(labelTranslate.x));
			}

			/** Otherwise, update the existing shape.*/
		} else {
			updateShape(canvas, geometry, shape);
			nameText.y(
				canvas.transform.canvasYPos(getGeometryHeight(geometry) + labelTranslate.y)
			);
			nameText.x(canvas.transform.canvasXPos(labelTranslate.x));
		}

		previousGeometryType = geometry.type;
	});

	/** Update position upon position change. */
	$effect(() => {
		if (position) {
			group.position({
				x: canvas.transform.canvasXPos(position.x),
				y: canvas.transform.canvasYPos(position.y)
			});
			group.visible(true);
		} else {
			group.visible(false);
		}
	});

	/** Update color on selection change. */
	$effect(() => {
		shape?.fill(fillColor);
		shape?.stroke(strokeColor);
		shape?.strokeWidth(strokeWidth);
		nameText.fill(nameTextFillColor);
	});

	/** Update name text on name change. */
	$effect(() => {
		nameText.text(name);
		nameText.offsetX(nameText.width() / 2);
		nameText.offsetY(nameText.height() + LABEL_OFFSET_PX);
	});

	/** Add events. */
	$effect(() => {
		if (editable) {
			group.draggable(true);
			shape?.on('mouseover', () => {
				document.body.style.cursor = 'move';
			});
			shape?.on('mouseout', () => {
				canvas.selectionGroup.setDocumentCursor();
			});
			group.on('dragmove', () => {
				if (onTranslate) {
					onTranslate({ x: group.x(), y: group.y() }, false);
				}
			});
			group.on('dragend', () => {
				group.position(canvas.gridManager.snapToGrid(group.position()));
				if (onTranslate) {
					onTranslate({ x: group.x(), y: group.y() }, true);
				}
			});
			group.on('pointerclick', () => {
				if (onClick) {
					onClick();
				}
			});
		} else {
			group.draggable(false);
			group.off('mouseover mouseout dragmove dragend pointerclick');
		}
	});

	/**
	 * Wrap the container's onTransform to optimistically update
	 * the shape before the geometry is updated in Triplit.
	 */
	function onTransform(newGeometry: GeometryUpdateCommand, transformOver: boolean) {
		if (shape) {
			updateShape(canvas, newGeometry, shape);
		}
		if (onTransformContainer) {
			onTransformContainer(newGeometry, transformOver);
		}
	}

	onDestroy(() => {
		group.destroy();
	});
</script>

{#if editable}
	<EditableGeometryResizePoints
		{canvasId}
		{geometry}
		{strokeColor}
		{fillColor}
		geometryGroup={group}
		{onTransform}
	/>
{/if}
