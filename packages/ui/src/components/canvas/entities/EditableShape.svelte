<script lang="ts">
	import { getContext } from 'svelte';

	import {
		type Geometry,
		type GeometryUpdateCommand,
		type Position,
		getGeometryHeight
	} from '@vdg-webapp/models';

	import type { CanvasContext } from '../state';
	import { getShapeAttributes } from '../utils';
	import EditableGeometryResizePoints from './EditableGeometryResizePoints.svelte';

	type Props = {
		/** The ID of the canvas. */
		canvasId: string;
		/** The ID of the layer which holds the shape. Kept for caller compatibility; z-order is now plain DOM order. */
		layerId: string;
		/** Name of the planting area. Can be disabled */
		name: string;
		showName: boolean;
		/** The current position of the shape in the workspace, in model quantity (meters). */
		position: Position | null;
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
		labelTranslate?: Position;
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

	/** Retrieve canvas. */
	const canvas = getContext<CanvasContext>(canvasId);

	/**
	 * A resize's geometry updates are optimistically overlaid onto the
	 * committed `geometry` prop so the shape and its label reposition
	 * instantly, without waiting on the Triplit round trip that
	 * `onTransform` triggers. Cleared once the committed prop catches up.
	 */
	let geometryOverride: GeometryUpdateCommand | null = $state(null);
	const effectiveGeometry = $derived({ ...geometry, ...(geometryOverride ?? {}) });

	$effect(() => {
		void geometry;
		geometryOverride = null;
	});

	const shapeAttributes = $derived(getShapeAttributes(canvas, effectiveGeometry));

	/**
	 * A drag's translation is optimistically overlaid onto the committed
	 * `position` prop for the same reason as `geometryOverride` above.
	 */
	let positionOverride: Position | null = $state(null);

	$effect(() => {
		void position;
		positionOverride = null;
	});

	/** The shape's current position in local (pre-pan-zoom) canvas pixels, or null if not placed. */
	const canvasPosition = $derived(
		positionOverride ??
			(position
				? {
						x: canvas.transform.canvasXPos(position.x),
						y: canvas.transform.canvasYPos(position.y)
					}
				: null)
	);

	const groupTransform = $derived(
		canvasPosition
			? `translate(${canvasPosition.x} ${canvasPosition.y}) rotate(${effectiveGeometry.rotation})`
			: ''
	);

	/** Text label measurement. */
	let textElement: SVGTextElement | undefined = $state();
	/**
	 * A reasonable pre-measurement estimate matching the font size below,
	 * to avoid a visible jump before the first `getBBox()` measurement lands.
	 */
	let measuredTextHeight = $state(15);

	$effect(() => {
		/** Re-measure whenever the rendered text content changes. */
		void name;
		void showName;
		if (!textElement) return;
		/**
		 * getBBox() requires the element to already be rendered, unlike
		 * Konva.Text's synchronous width()/height(), which is why this is
		 * measured reactively after the fact rather than computed alongside
		 * the text content itself.
		 */
		try {
			measuredTextHeight = textElement.getBBox().height;
		} catch {
			/** Not yet measurable (e.g. not connected to a rendered document) - keep the previous estimate. */
		}
	});

	const labelPosition = $derived({
		x: canvas.transform.canvasXPos(labelTranslate.x),
		y:
			canvas.transform.canvasYPos(getGeometryHeight(effectiveGeometry) + labelTranslate.y) -
			measuredTextHeight -
			LABEL_OFFSET_PX
	});

	/** Dragging the shape. */
	let dragPointerOffset: Position = { x: 0, y: 0 };
	/**
	 * Tracks whether the current press actually moved the shape, so a real
	 * drag doesn't also fire `onClick` afterwards - the browser's native
	 * `click` event fires after any pointerdown/pointerup pair on the same
	 * captured element regardless of movement in between, unlike Konva's
	 * own drag machinery, which suppressed its click event once a real
	 * drag threshold was crossed.
	 */
	let dragOccurred = false;

	function handlePointerDown(event: PointerEvent) {
		if (!editable || !canvas.container.stageElement || !canvasPosition) return;
		event.stopPropagation();
		dragOccurred = false;
		(event.currentTarget as Element).setPointerCapture(event.pointerId);
		const pointerLocal = canvas.transform.localPixelPositionFromPointerEvent(
			event,
			canvas.container.stageElement
		);
		dragPointerOffset = {
			x: pointerLocal.x - canvasPosition.x,
			y: pointerLocal.y - canvasPosition.y
		};
		document.body.style.cursor = 'move';
	}

	function handlePointerMove(event: PointerEvent) {
		if (!editable || !canvas.container.stageElement) return;
		if (!(event.currentTarget as Element).hasPointerCapture(event.pointerId)) return;
		dragOccurred = true;
		const pointerLocal = canvas.transform.localPixelPositionFromPointerEvent(
			event,
			canvas.container.stageElement
		);
		positionOverride = {
			x: pointerLocal.x - dragPointerOffset.x,
			y: pointerLocal.y - dragPointerOffset.y
		};
		onTranslate?.(positionOverride, false);
	}

	function handlePointerUp(event: PointerEvent) {
		if (!editable) return;
		if (!(event.currentTarget as Element).hasPointerCapture(event.pointerId)) return;
		(event.currentTarget as Element).releasePointerCapture(event.pointerId);
		canvas.selectionGroup.setDocumentCursor();
		if (positionOverride) {
			positionOverride = canvas.gridManager.snapToGrid(positionOverride);
			onTranslate?.(positionOverride, true);
		}
	}

	function handlePointerEnter() {
		if (!editable) return;
		document.body.style.cursor = 'move';
	}

	function handlePointerLeave() {
		if (!editable) return;
		canvas.selectionGroup.setDocumentCursor();
	}

	function handleClick() {
		if (dragOccurred) {
			dragOccurred = false;
			return;
		}
		/** Matches the original Konva behavior: clicks were only wired up while editable. */
		if (!editable) return;
		onClick?.();
	}

	function handleKeyDown(event: KeyboardEvent) {
		if (!editable) return;
		if (event.key === 'Enter' || event.key === ' ') {
			event.preventDefault();
			onClick?.();
		}
	}

	/**
	 * Wrap the container's onTransform to optimistically update
	 * the shape before the geometry is updated in Triplit.
	 */
	function onTransform(newGeometry: GeometryUpdateCommand, transformOver: boolean) {
		geometryOverride = { ...geometryOverride, ...newGeometry };
		onTransformContainer?.(newGeometry, transformOver);
	}
</script>

{#if canvasPosition}
	<!-- role is 'button' whenever tabindex is set; the linter can't statically resolve the conditional. -->
	<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
	<g
		data-layer-id={layerId}
		transform={groupTransform}
		style:cursor={editable ? 'move' : undefined}
		onpointerdown={handlePointerDown}
		onpointermove={handlePointerMove}
		onpointerup={handlePointerUp}
		onpointerenter={handlePointerEnter}
		onpointerleave={handlePointerLeave}
		onclick={handleClick}
		onkeydown={handleKeyDown}
		role={editable ? 'button' : undefined}
		tabindex={editable ? 0 : undefined}
	>
		{#if shapeAttributes.type === 'RECTANGLE'}
			<rect
				x={shapeAttributes.x}
				y={shapeAttributes.y}
				width={shapeAttributes.width}
				height={shapeAttributes.height}
				fill={fillColor}
				stroke={strokeColor}
				stroke-width={strokeWidth}
			/>
		{:else if shapeAttributes.type === 'ELLIPSE'}
			<ellipse
				rx={shapeAttributes.rx}
				ry={shapeAttributes.ry}
				fill={fillColor}
				stroke={strokeColor}
				stroke-width={strokeWidth}
			/>
		{:else if shapeAttributes.type === 'POLYGON'}
			<polygon
				points={shapeAttributes.points}
				fill={fillColor}
				stroke={strokeColor}
				stroke-width={strokeWidth}
			/>
		{:else if shapeAttributes.type === 'LINES'}
			{#if shapeAttributes.closed}
				<polygon
					points={shapeAttributes.points}
					fill={fillColor}
					stroke={strokeColor}
					stroke-width={strokeWidth}
				/>
			{:else}
				<polyline
					points={shapeAttributes.points}
					fill="none"
					stroke={strokeColor}
					stroke-width={strokeWidth}
				/>
			{/if}
		{/if}

		{#if showName}
			<text
				bind:this={textElement}
				x={labelPosition.x}
				y={labelPosition.y}
				text-anchor="middle"
				dominant-baseline="hanging"
				font-family="sans-serif"
				font-size={15}
				opacity={0.7}
				fill={nameTextFillColor}
			>
				{name}
			</text>
		{/if}

		{#if editable}
			<EditableGeometryResizePoints
				{canvasId}
				geometry={effectiveGeometry}
				{strokeColor}
				{fillColor}
				shapePosition={canvasPosition}
				rotation={effectiveGeometry.rotation}
				{onTransform}
			/>
		{/if}
	</g>
{/if}
