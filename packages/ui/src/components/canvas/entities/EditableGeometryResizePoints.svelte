<script lang="ts">
	import { getContext } from 'svelte';

	import type { Geometry, GeometryUpdateCommand, Position } from '@vdg-webapp/models';

	import { roundToDecimalPlaces } from '$utils';

	import type { CanvasContext } from '../state';
	import { getGeometryResizePoints } from './utils';

	type Props = {
		/** The ID of the canvas. */
		canvasId: string;
		/* The geometry to add points for. */
		geometry: Omit<Geometry, 'id' | 'gardenId' | 'linesCoordinateIds' | 'date'>;
		/** The parent shape's current position, in local (pre-pan-zoom) canvas pixels. */
		shapePosition: Position;
		/** The parent shape's current rotation, in degrees. */
		rotation: number;
		/** Colors to make the points. */
		strokeColor: string;
		fillColor: string;
		/** Called when the geometry is transformed in the canvas. */
		onTransform?: (
			/** The updated geometry attributes after transformation. */
			newGeometry: GeometryUpdateCommand,
			/** If true, the transform has ended. */
			transformOver: boolean
		) => void;
	};
	let { canvasId, geometry, shapePosition, rotation, strokeColor, fillColor, onTransform }: Props =
		$props();

	const ATTRIBUTE_DECIMALS = 2;

	/** Retrieve canvas. */
	const canvas = getContext<CanvasContext>(canvasId);

	/** The canonical handle positions, in local canvas pixels relative to the shape's own (unrotated) origin. */
	const canonicalPositions = $derived(
		getGeometryResizePoints(geometry).map((point) => ({
			x: canvas.transform.canvasXPos(point.x),
			y: canvas.transform.canvasYPos(point.y)
		}))
	);

	/**
	 * While a handle is being dragged, its live position optimistically
	 * overrides the canonical one computed from the (not-yet-updated)
	 * geometry prop - the same pattern `EditableShape` uses for the shape
	 * itself, needed here for the same reason: no waiting on the Triplit
	 * round trip to see the handle move.
	 */
	let activeDragIndex: number | null = $state(null);
	let activeDragPosition: Position | null = $state(null);

	const displayedPositions = $derived(
		canonicalPositions.map((point, index) =>
			index === activeDragIndex && activeDragPosition ? activeDragPosition : point
		)
	);

	/**
	 * Given an index of a point in the displayed positions array,
	 * return a geometry update object which contains the changes
	 * to that geometry given the position of the resize point.
	 * @param index The index of the resize point.
	 */
	function handleResizePointDrag(index: number): GeometryUpdateCommand {
		const newGeometry: GeometryUpdateCommand = {};
		const point = displayedPositions[index];

		switch (geometry.type) {
			case 'RECTANGLE': {
				/**
				 * If the index is even, this is a corner point.
				 * Calculate the new width and height.
				 */
				if (index % 2 === 0) {
					const newLength = Math.abs(point.x) * 2;
					const newWidth = Math.abs(point.y) * 2;
					newGeometry.rectangleLength = roundToDecimalPlaces(
						canvas.transform.modelDistance(newLength),
						ATTRIBUTE_DECIMALS
					);

					newGeometry.rectangleWidth = roundToDecimalPlaces(
						canvas.transform.modelDistance(newWidth),
						ATTRIBUTE_DECIMALS
					);

					/**
					 * If the index is odd, this is a side point.
					 * Calculate the new width or height depending on the side,
					 * and constrain movement to an axis.
					 */
				} else {
					/** Top or bottom point. */
					if (index === 1 || index === 5) {
						const newWidth = Math.abs(point.y) * 2;
						newGeometry.rectangleWidth = roundToDecimalPlaces(
							canvas.transform.modelDistance(newWidth),
							ATTRIBUTE_DECIMALS
						);

						/** Side points. */
					} else {
						const newLength = Math.abs(point.x) * 2;
						newGeometry.rectangleLength = roundToDecimalPlaces(
							canvas.transform.modelDistance(newLength),
							ATTRIBUTE_DECIMALS
						);
					}
				}
				break;
			}

			case 'POLYGON': {
				/**
				 * Calculate the new radius,
				 * constrained to the point's vertical distance
				 * from the shape's origin.
				 */
				const newRadius = Math.abs(point.y);
				newGeometry.polygonRadius = roundToDecimalPlaces(
					canvas.transform.modelDistance(newRadius),
					ATTRIBUTE_DECIMALS
				);
				break;
			}

			case 'ELLIPSE': {
				/**
				 * If the index is even, this is a top or bottom point.
				 * Calculate the new width from the point's vertical distance.
				 *
				 * If the index is odd, this is a side point.
				 * Calculate the new length from the point's horizontal distance.
				 */
				if (index % 2 === 0) {
					const newWidthDiameter = Math.abs(point.y) * 2;
					newGeometry.ellipseWidth = roundToDecimalPlaces(
						canvas.transform.modelDistance(newWidthDiameter),
						ATTRIBUTE_DECIMALS
					);
				} else {
					const newLengthDiameter = Math.abs(point.x) * 2;
					newGeometry.ellipseLength = roundToDecimalPlaces(
						canvas.transform.modelDistance(newLengthDiameter),
						ATTRIBUTE_DECIMALS
					);
				}

				break;
			}

			case 'LINES': {
				/**
				 * Each point updates the whole coordinate array to the current state.
				 */
				newGeometry.linesCoordinates = displayedPositions.map((displayedPoint) => {
					return {
						x: roundToDecimalPlaces(
							canvas.transform.modelXPos(displayedPoint.x),
							ATTRIBUTE_DECIMALS
						),
						y: roundToDecimalPlaces(
							canvas.transform.modelYPos(displayedPoint.y),
							ATTRIBUTE_DECIMALS
						)
					};
				});
				break;
			}
		}
		return newGeometry;
	}

	/**
	 * Converts a pointer event into the shape's own local, unrotated
	 * coordinate frame (the same frame `getGeometryResizePoints` produces).
	 * Konva's per-node dragging did this automatically via the scene
	 * graph's transform inheritance, since the handles were nested inside
	 * the shape's own (rotated) group; SVG pointer events don't carry that
	 * inheritance, so the rotation has to be inverted manually here.
	 * @param event The pointer event to convert.
	 */
	function pointerEventToShapeLocalPosition(event: PointerEvent): Position | null {
		if (!canvas.container.stageElement) return null;
		const pointerLocal = canvas.transform.localPixelPositionFromPointerEvent(
			event,
			canvas.container.stageElement
		);
		const deltaX = pointerLocal.x - shapePosition.x;
		const deltaY = pointerLocal.y - shapePosition.y;
		const radians = (-rotation * Math.PI) / 180;
		const cos = Math.cos(radians);
		const sin = Math.sin(radians);
		return {
			x: deltaX * cos - deltaY * sin,
			y: deltaX * sin + deltaY * cos
		};
	}

	function handlePointerDown(event: PointerEvent, index: number) {
		(event.currentTarget as Element).setPointerCapture(event.pointerId);
		event.stopPropagation();
		activeDragIndex = index;
		activeDragPosition = canonicalPositions[index];
		document.body.style.cursor = 'grab';
	}

	function handlePointerMove(event: PointerEvent, index: number) {
		if (!(event.currentTarget as Element).hasPointerCapture(event.pointerId)) return;
		event.stopPropagation();
		if (activeDragIndex !== index) return;

		const localPosition = pointerEventToShapeLocalPosition(event);
		if (!localPosition) return;

		/** Constrain movement to the axis/behavior the current geometry type expects. */
		switch (geometry.type) {
			case 'RECTANGLE':
				if (index % 2 !== 0) {
					if (index === 1 || index === 5) {
						localPosition.x = 0;
					} else {
						localPosition.y = 0;
					}
				}
				break;
			case 'POLYGON':
				localPosition.x = 0;
				break;
			case 'ELLIPSE':
				if (index % 2 === 0) {
					localPosition.x = 0;
				} else {
					localPosition.y = 0;
				}
				break;
		}

		activeDragPosition = localPosition;
		onTransform?.(handleResizePointDrag(index), false);
	}

	function handlePointerUp(event: PointerEvent, index: number) {
		if (!(event.currentTarget as Element).hasPointerCapture(event.pointerId)) return;
		(event.currentTarget as Element).releasePointerCapture(event.pointerId);
		event.stopPropagation();
		if (activeDragIndex === index) {
			onTransform?.(handleResizePointDrag(index), true);
		}
		activeDragIndex = null;
		activeDragPosition = null;
		document.body.style.cursor = 'default';
	}

	function handlePointerEnter(event: PointerEvent) {
		event.stopPropagation();
		document.body.style.cursor = 'grab';
	}

	function handlePointerLeave(event: PointerEvent) {
		event.stopPropagation();
		if (activeDragIndex === null) {
			canvas.selectionGroup.setDocumentCursor();
		}
	}

</script>

{#each displayedPositions as point, index (index)}
	<circle
		cx={point.x}
		cy={point.y}
		r={6}
		stroke-width={3}
		stroke={strokeColor}
		fill={fillColor}
		style:cursor="grab"
		onpointerdown={(event) => handlePointerDown(event, index)}
		onpointermove={(event) => handlePointerMove(event, index)}
		onpointerup={(event) => handlePointerUp(event, index)}
		onpointerenter={handlePointerEnter}
		onpointerleave={handlePointerLeave}
	/>
{/each}
