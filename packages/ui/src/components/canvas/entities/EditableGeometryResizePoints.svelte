<script lang="ts">
	import Konva from 'konva';
	import { getContext, onDestroy } from 'svelte';

	import type { Geometry, GeometryUpdateCommand } from '@vdg-webapp/models';
	import { AppError } from '@vdg-webapp/models';

	import { roundToDecimalPlaces } from '$utils';

	import type { CanvasContext } from '../state';
	import { getGeometryResizePoints } from './utils';

	type Props = {
		/** The ID of the canvas. */
		canvasId: string;
		/* The geometry to add points for. */
		geometry: Omit<Geometry, 'id' | 'gardenId' | 'linesCoordinateIds' | 'date'>;
		/** A konva group already made that stores the geometry's shapes. */
		geometryGroup: Konva.Group;
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
	let {
		canvasId,
		geometry,
		geometryGroup,
		strokeColor,
		fillColor,
		onTransform
	}: Props = $props();

	const ATTRIBUTE_DECIMALS = 2;

	/** Retrieve canvas and initialize Konva constructs. */
	const canvas = getContext<CanvasContext>(canvasId);
	let group = new Konva.Group();
	geometryGroup.add(group);
	group.moveToTop();
	let resizePoints: Array<Konva.Circle> = [];

	/**
	 * Store the geometry type and number of resize points.
	 * If either changes, the shapes must be re-initialized.
	 */
	let previousGeometryType = geometry.type;
	let previousNumResizePoints: number = 0;

	/**
	 * Given an index of a point in the resize points array,
	 * return a geometry update object which contains the changes
	 * to that geometry given the position of the resize point.
	 * @param index The index of the resize point.
	 */
	function handleResizePointDrag(index: number): GeometryUpdateCommand {
		const newGeometry: GeometryUpdateCommand = {};

		switch (geometry.type) {
			case 'RECTANGLE': {
				/**
				 * If the index is even, this is a corner point.
				 * Calculate the new width and height.
				 */
				if (index % 2 === 0) {
					const newLength = Math.abs(resizePoints[index].x()) * 2;
					const newWidth = Math.abs(resizePoints[index].y()) * 2;
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
						resizePoints[index].x(0);
						const newWidth = Math.abs(resizePoints[index].y()) * 2;
						newGeometry.rectangleWidth = roundToDecimalPlaces(
							canvas.transform.modelDistance(newWidth),
							ATTRIBUTE_DECIMALS
						);

						/** Side points. */
					} else {
						resizePoints[index].y(0);
						const newLength = Math.abs(resizePoints[index].x()) * 2;
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
				 * and constrain the movement to
				 * a vertical line.
				 */
				resizePoints[index].x(0);
				const newRadius = Math.abs(resizePoints[index].y());
				newGeometry.polygonRadius = roundToDecimalPlaces(
					canvas.transform.modelDistance(newRadius),
					ATTRIBUTE_DECIMALS
				);
				break;
			}

			case 'ELLIPSE': {
				/**
				 * If the index is even, this is a top or bottom point.
				 * Calculate the new width and
				 * constrain movement to the Y axis.
				 */
				if (index % 2 === 0) {
					resizePoints[index].x(0);
					const newWidthDiameter = Math.abs(resizePoints[index].y()) * 2;
					newGeometry.ellipseWidth = roundToDecimalPlaces(
						canvas.transform.modelDistance(newWidthDiameter),
						ATTRIBUTE_DECIMALS
					);

					/**
					 * If the index is odd, this is a side point.
					 * Calculate the new length and
					 * constrain movement to the X axis.
					 */
				} else {
					resizePoints[index].y(0);
					const newLengthDiameter = Math.abs(resizePoints[index].x()) * 2;
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
				newGeometry.linesCoordinates = resizePoints.map((point) => {
					return {
						x: roundToDecimalPlaces(
							canvas.transform.modelXPos(point.x()),
							ATTRIBUTE_DECIMALS
						),
						y: roundToDecimalPlaces(
							canvas.transform.modelYPos(point.y()),
							ATTRIBUTE_DECIMALS
						)
					};
				});
				break;
			}
		}
		return newGeometry;
	}

	$effect(() => {
		const coordinates = getGeometryResizePoints(geometry);
		/**
		 * If the points haven't been created yet,
		 * or the geometry type has switched,
		 * or another point has been added,
		 * re-initialize the points.
		 * Otherwise, update their positions.
		 */
		if (
			previousNumResizePoints === 0 ||
			previousGeometryType != geometry.type ||
			previousNumResizePoints != coordinates.length
		) {
			resizePoints = [];
			group.destroyChildren();
			coordinates.forEach((coordinate, index) => {
				const point = new Konva.Circle({
					radius: 6,
					strokeWidth: 3,
					x: canvas.transform.canvasXPos(coordinate.x),
					y: canvas.transform.canvasYPos(coordinate.y),
					draggable: true,
					stroke: strokeColor,
					fill: fillColor
				});

				/**
				 * Note that events aren't bubbled,
				 * this prevents triggering the events
				 * on the parent group.
				 */
				point.on('mouseover', (event) => {
					document.body.style.cursor = 'grab';
					event.cancelBubble = true;
				});
				point.on('mouseout', (event) => {
					document.body.style.cursor = 'default';
					event.cancelBubble = true;
				});
				point.on('dragmove', (event) => {
					if (onTransform) {
						onTransform(handleResizePointDrag(index), false);
					}
					event.cancelBubble = true;
				});
				point.on('dragend', (event) => {
					if (onTransform) {
						onTransform(handleResizePointDrag(index), true);
					}
					event.cancelBubble = true;
				});

				resizePoints.push(point);
				group.add(point);
			});
		} else {
			coordinates.forEach((coordinate, index) => {
				if (resizePoints[index]) {
					resizePoints[index].x(canvas.transform.canvasXPos(coordinate.x));
					resizePoints[index].y(canvas.transform.canvasYPos(coordinate.y));
				} else {
					throw new AppError('Geometry resize points caught in an invalid state.');
				}
			});
		}

		group.moveToTop();
		previousGeometryType = geometry.type;
		previousNumResizePoints = coordinates.length;
	});

	/** Update color on change. */
	$effect(() => {
		resizePoints.forEach((point) => {
			point.stroke(strokeColor);
			point.fill(fillColor);
		});
	});

	onDestroy(() => {
		group.destroy();
	});
</script>
