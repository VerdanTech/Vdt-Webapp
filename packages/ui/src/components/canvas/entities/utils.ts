import { type Geometry } from '@vdg-webapp/models';

/**
 * Given a geometry, returns an array of coordinates
 * where each coordinate is a point on the shape which
 * can be dragged to resize the shape. Two geometries
 * of the same type will have exactly the same number
 * of resize points, unless the geometry is a lines geometry,
 * in which case it will have a point for each coordinate.
 *
 * The points are different for each geometry type:
 *
 * For a rectangle, there is a point at each corner,
 * and a point in the middle of each side. The points
 * start at the top left corner, meaning that even
 * points are corners and odd points are sides.
 * 0----1----2
 * |		 |
 * 7		 3
 * |		 |
 * 6----5----4
 *
 * For an ellise, there is a point at each side,
 * starting from the top.
 *     0
 *   /   \
 *  3     1
 *   \   /
 *     2
 *
 * For a polygon, there is a one point, at the top.
 *    0
 *  /   \
 *  \   /
 *   ---
 *
 * For a lines geometry described by a set of points,
 * the resize points are simply the set of points.
 * 0----1
 *  \    |
 *   \   2--3
 *    \     |
 *     \    |
 *      \   |
 *       \  |
 *        \ |
 *         \|
 * 	        4
 *
 * @param geometry The geometry to extract from.
 * @returns The list of points which can be used as resize points.
 */
export function getGeometryResizePoints(
	geometry: Omit<Geometry, 'id' | 'gardenId' | 'linesCoordinateIds' | 'date'>
): Array<{ x: number; y: number }> {
	switch (geometry.type) {
		case 'RECTANGLE': {
			const halfLength = geometry.rectangleLength / 2;
			const halfWidth = geometry.rectangleWidth / 2;

			return [
				{ x: -halfLength, y: halfWidth },
				{ x: 0, y: halfWidth },
				{ x: halfLength, y: halfWidth },
				{ x: halfLength, y: 0 },
				{ x: halfLength, y: -halfWidth },
				{ x: 0, y: -halfWidth },
				{ x: -halfLength, y: -halfWidth },
				{ x: -halfLength, y: 0 }
			];
		}

		case 'POLYGON': {
			return [{ x: 0, y: geometry.polygonRadius }];
		}

		case 'ELLIPSE': {
			const radiusLength = geometry.ellipseLength / 2;
			const radiusWidth = geometry.ellipseWidth / 2;

			return [
				{ x: 0, y: radiusWidth },
				{ x: radiusLength, y: 0 },
				{ x: 0, y: -radiusWidth },
				{ x: -radiusLength, y: 0 }
			];
		}

		case 'LINES': {
			return geometry.linesCoordinates.map((coordinate) => {
				return { x: coordinate.x, y: coordinate.y };
			});
		}
	}
}

/**
 * Canonical resize-arrow angle for each RECTANGLE resize point, in degrees,
 * measured from horizontal (0deg = horizontal/ew, 90deg = vertical/ns,
 * 45deg/135deg = the two diagonals) - indexed per the diagram above.
 */
const rectangleResizeAngles = [45, 90, 135, 0, 45, 90, 135, 0];

/** Canonical resize-arrow angle for each ELLIPSE resize point, indexed per the diagram above. */
const ellipseResizeAngles = [90, 0, 90, 0];

/**
 * Folds an angle in degrees into [0, 180) - a straight double-headed
 * resize arrow looks identical every 180 degrees, so this is the natural
 * equivalence class to compare/round within.
 * @param angleDegrees The angle to fold.
 * @returns The equivalent angle in [0, 180).
 */
function foldAngleToHalfTurn(angleDegrees: number): number {
	const folded = angleDegrees % 180;
	return folded < 0 ? folded + 180 : folded;
}

/** The four standard resize cursor keywords, used as a fallback for browsers that can't render a custom cursor image. */
const resizeCursorKeywordsByAngle: Record<number, string> = {
	0: 'ew-resize',
	45: 'nwse-resize',
	90: 'ns-resize',
	135: 'nesw-resize'
};

/**
 * A double-headed straight-arrow path, drawn horizontally (0deg), for a
 * resize cursor. Rotated to the exact target angle via an SVG `<g>`
 * transform, so - unlike the fixed set of CSS cursor keywords - it
 * follows the shape's rotation continuously rather than snapping to the
 * nearest 45deg increment.
 */
const resizeArrowPath = 'M4 12 H20 M4 12 L8 8 M4 12 L8 16 M20 12 L16 8 M20 12 L16 16';

/**
 * A four-way arrow (up/down/left/right), for the cursor over a freely
 * (unconstrained) draggable point - e.g. a LINES geometry's vertices,
 * which don't have a single resize direction the way the other geometry
 * types' handles do. Symmetric under 90deg rotation, so it isn't rotated.
 */
const moveArrowPath =
	'M12 3 V21 M3 12 H21 M12 3 L9 7 M12 3 L15 7 M12 21 L9 17 M12 21 L15 17 M21 12 L17 9 M21 12 L17 15 M3 12 L7 9 M3 12 L7 15';

/**
 * Builds a `cursor` CSS value from an SVG icon: a white outline behind a
 * black stroke (the standard cursor-legibility trick, so the icon reads
 * against both light and dark canvas backgrounds), plus a fallback
 * keyword for the rare case a custom cursor image can't be rendered.
 * @param path The SVG path data for the icon, drawn within a 24x24 viewBox centered on (12, 12).
 * @param rotationDegrees Rotation to apply to the icon, about its center.
 * @param fallbackKeyword The standard CSS cursor keyword to fall back to.
 * @returns A full CSS `cursor` property value.
 */
function buildArrowCursor(
	path: string,
	rotationDegrees: number,
	fallbackKeyword: string
): string {
	const svg =
		`<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">` +
		`<g transform="rotate(${rotationDegrees} 12 12)">` +
		`<path d="${path}" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>` +
		`<path d="${path}" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>` +
		`</g></svg>`;
	return `url("data:image/svg+xml,${encodeURIComponent(svg)}") 12 12, ${fallbackKeyword}`;
}

/**
 * Given a geometry and the index of one of its resize points (from
 * `getGeometryResizePoints`), returns the CSS cursor that communicates
 * which direction dragging that point resizes the shape - the standard
 * convention visual editors use for resize handles (directional arrows),
 * as opposed to the `grab`/`grabbing` hand used for freely repositioning
 * a whole shape or panning the canvas.
 *
 * For RECTANGLE/ELLIPSE/POLYGON, the arrow is a custom SVG cursor rotated
 * to the shape's exact `rotation`, rather than one of the eight fixed CSS
 * cursor keywords - those keywords can't represent an arbitrary rotation
 * angle, only 45deg increments, so a rotated shape's handles would
 * otherwise point in the wrong direction on screen.
 * @param geometry The geometry the resize point belongs to.
 * @param index The index of the resize point.
 * @returns The CSS `cursor` value for that resize point.
 */
export function getGeometryResizePointCursor(
	geometry: Omit<Geometry, 'id' | 'gardenId' | 'linesCoordinateIds' | 'date'>,
	index: number
): string {
	switch (geometry.type) {
		case 'RECTANGLE':
		case 'ELLIPSE': {
			const canonicalAngle =
				geometry.type === 'RECTANGLE'
					? rectangleResizeAngles[index]
					: ellipseResizeAngles[index];
			const effectiveAngle = foldAngleToHalfTurn(canonicalAngle + geometry.rotation);
			const nearestKeywordAngle = foldAngleToHalfTurn(Math.round(effectiveAngle / 45) * 45);
			return buildArrowCursor(
				resizeArrowPath,
				effectiveAngle,
				resizeCursorKeywordsByAngle[nearestKeywordAngle] ?? 'ew-resize'
			);
		}
		case 'POLYGON': {
			/** The only point is constrained to vertical movement (see handlePointerMove's axis constraints). */
			const effectiveAngle = foldAngleToHalfTurn(90 + geometry.rotation);
			const nearestKeywordAngle = foldAngleToHalfTurn(Math.round(effectiveAngle / 45) * 45);
			return buildArrowCursor(
				resizeArrowPath,
				effectiveAngle,
				resizeCursorKeywordsByAngle[nearestKeywordAngle] ?? 'ns-resize'
			);
		}
		case 'LINES':
			/** Each point moves freely in both axes, unlike the constrained points above - there's no single direction to indicate. */
			return buildArrowCursor(moveArrowPath, 0, 'move');
	}
}
