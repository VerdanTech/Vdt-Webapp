import { AppError, type Geometry } from '@vdg-webapp/models';

import type { CanvasContext } from '../state';

/** A rectangle's SVG attributes, centered on its parent group's origin. */
export type RectangleShapeAttributes = {
	type: 'RECTANGLE';
	x: number;
	y: number;
	width: number;
	height: number;
};

/** An ellipse's SVG attributes, centered on its parent group's origin. */
export type EllipseShapeAttributes = {
	type: 'ELLIPSE';
	rx: number;
	ry: number;
};

/** A regular polygon's SVG attributes, centered on its parent group's origin. */
export type PolygonShapeAttributes = {
	type: 'POLYGON';
	points: string;
};

/**
 * A lines geometry's SVG attributes. Rendered as a `<polygon>` when closed
 * (so it fills) and a `<polyline>` when open, since a `<polygon>` always
 * visually closes its stroke even when not explicitly told to.
 */
export type LinesShapeAttributes = {
	type: 'LINES';
	closed: boolean;
	points: string;
};

export type ShapeAttributes =
	| RectangleShapeAttributes
	| EllipseShapeAttributes
	| PolygonShapeAttributes
	| LinesShapeAttributes;

/**
 * Computes the vertices of a regular polygon centered on the origin,
 * starting from the top, matching the orientation of the single POLYGON
 * resize point in `entities/utils.ts`'s `getGeometryResizePoints`.
 * SVG has no native regular-polygon primitive, so a `<polygon>`'s
 * `points` attribute must be computed directly.
 * @param numSides The number of sides of the polygon.
 * @param radius The radius of the polygon, in canvas pixels.
 * @returns A space-separated `points` attribute value.
 */
function getRegularPolygonPoints(numSides: number, radius: number): string {
	const points: string[] = [];
	for (let side = 0; side < numSides; side++) {
		const angle = (side / numSides) * 2 * Math.PI - Math.PI / 2;
		points.push(`${radius * Math.cos(angle)},${radius * Math.sin(angle)}`);
	}
	return points.join(' ');
}

/**
 * Given a geometry, computes the SVG attributes needed to render it,
 * in canvas pixels relative to the shape's own (already positioned
 * and rotated) parent group.
 * @param canvas The canvas context.
 * @param geometry The geometry of the shape. Must have linesCoordinates included.
 * @param forceLinesClosed If true, a LINES geometry renders closed regardless of its attributes.
 * @returns The shape's SVG attributes.
 */
export function getShapeAttributes(
	canvas: CanvasContext,
	geometry: Omit<Geometry, 'id' | 'gardenId' | 'date' | 'linesCoordinateIds'>,
	forceLinesClosed: boolean = false
): ShapeAttributes {
	switch (geometry.type) {
		case 'RECTANGLE': {
			const width = canvas.transform.canvasDistance(geometry.rectangleLength);
			const height = canvas.transform.canvasDistance(geometry.rectangleWidth);
			return { type: 'RECTANGLE', x: -width / 2, y: -height / 2, width, height };
		}

		case 'POLYGON': {
			const radius = canvas.transform.canvasDistance(geometry.polygonRadius);
			return {
				type: 'POLYGON',
				points: getRegularPolygonPoints(geometry.polygonNumSides, radius)
			};
		}

		case 'ELLIPSE':
			return {
				type: 'ELLIPSE',
				rx: canvas.transform.canvasDistance(geometry.ellipseLength / 2),
				ry: canvas.transform.canvasDistance(geometry.ellipseWidth / 2)
			};

		case 'LINES': {
			const closed = geometry.linesClosed || forceLinesClosed;
			const points = geometry.linesCoordinates
				.map(
					(coordinate) =>
						`${canvas.transform.canvasXPos(coordinate.x)},${canvas.transform.canvasYPos(coordinate.y)}`
				)
				.join(' ');
			return { type: 'LINES', closed, points };
		}
	}

	/** Should not reach here. */
	throw new AppError('Geometry type undefined.');
}
