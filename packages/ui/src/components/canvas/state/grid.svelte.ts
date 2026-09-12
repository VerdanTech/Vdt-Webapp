import { mode } from 'mode-watcher';

import type { Position } from '@vdg-webapp/models';

import { localStore } from '$state/localStore.svelte';
import { getColor } from '$utils';

import { type CanvasContainer } from './container.svelte';
import { type CanvasTransform } from './transform.svelte';

export type GridManagerConfig = {
	metersPerBackgroundGridline: number;
};

type GridManagerPersistedState = {
	snapToGrid: boolean;
	rightAngleConstraint: boolean;
	metersPerBackgroundGridline: number;
};

/** A single gridline to render, in local (pre-pan-zoom) canvas pixels. */
export type Gridline = {
	/** Unique and stable across pan/zoom, so `{#each}` doesn't thrash DOM nodes. */
	key: string;
	x1: number;
	y1: number;
	x2: number;
	y2: number;
	color: string;
	strokeWidth: number;
};

/**
 * Rounds the number up to the nearest multiple of step.
 * @param number The number to round.
 * @param step The step to round to a multiple of.
 * @returns The rounded number.
 */
function roundUpToStep(number: number, step: number): number {
	return Math.round(number / step) * step;
}

/**
 * Rounds the number down to the nearest multiple of step.
 * @param number The number to round.
 * @param step The step to round to a multiple of.
 * @returns The rounded number.
 */
function roundDownToStep(number: number, step: number): number {
	return Math.floor(number / step) * step;
}

export function createCanvasGridManager(
	container: CanvasContainer,
	transform: CanvasTransform
) {
	/** Runes. */
	const config = localStore<GridManagerPersistedState>('layoutGridState', {
		snapToGrid: true,
		rightAngleConstraint: false,
		metersPerBackgroundGridline: 0.3048
	});
	const pixelsPerBackgroundGridline = $derived(
		container.pixelsPerMeter * config.value.metersPerBackgroundGridline
	);

	/**
	 * The gridlines currently within the viewable area, recomputed
	 * reactively whenever the pan/zoom transform, container size, or
	 * gridline spacing changes.
	 */
	const visibleGridlines: Gridline[] = $derived.by(() => {
		if (!container.initialized) {
			return [];
		}

		/**
		 * Calculate the coordinate range viewable in the canvas currently,
		 * considering the canvas dimensions, position, and scaling.
		 */
		const viewableStartPosition: Position = {
			x: -transform.position.x / transform.scaleFactor.x,
			y: -transform.position.y / transform.scaleFactor.y
		};
		const viewableEndPosition: Position = {
			x: viewableStartPosition.x + container.width / transform.scaleFactor.x,
			y: viewableStartPosition.y + container.height / transform.scaleFactor.y
		};

		/**
		 * Calculate the starting and ending positions of the gridlines, such that it is outside of the viewable area
		 * and is a multiple of the spaces between gridlines, such that the gridlines stay at the same position
		 * across renders.
		 */
		const startPosition: Position = {
			x: roundDownToStep(viewableStartPosition.x, pixelsPerBackgroundGridline),
			y: roundDownToStep(viewableStartPosition.y, pixelsPerBackgroundGridline)
		};
		const endPosition: Position = {
			x: roundUpToStep(
				viewableEndPosition.x + pixelsPerBackgroundGridline,
				pixelsPerBackgroundGridline
			),
			y: roundUpToStep(
				viewableEndPosition.y + pixelsPerBackgroundGridline,
				pixelsPerBackgroundGridline
			)
		};

		/**
		 * Calculate the minimum number of grid segments to fully cover the viewable area.
		 */
		const numSegments = {
			x: Math.round((endPosition.y - startPosition.y) / pixelsPerBackgroundGridline),
			y: Math.round((endPosition.x - startPosition.x) / pixelsPerBackgroundGridline)
		};

		const gap = { x: pixelsPerBackgroundGridline, y: pixelsPerBackgroundGridline };

		const gridlines: Gridline[] = [];

		/** Horizontal gridlines. */
		for (let i = 0; i <= numSegments.x; i++) {
			const yPosition = startPosition.y + gap.x * i;
			let color = getColor('neutral', 3, mode.current);
			let strokeWidth = 1;
			if (yPosition == 0) {
				color = getColor('neutral', 4, mode.current);
				strokeWidth = 2;
			}
			gridlines.push({
				key: `h-${yPosition}`,
				x1: startPosition.x,
				y1: yPosition,
				x2: endPosition.x,
				y2: yPosition,
				color,
				strokeWidth
			});
		}

		/** Vertical gridlines. */
		for (let i = 0; i <= numSegments.y; i++) {
			const xPosition = startPosition.x + gap.y * i;
			let color = getColor('neutral', 2, mode.current);
			let strokeWidth = 1;
			if (xPosition == 0) {
				color = getColor('neutral', 3, mode.current);
				strokeWidth = 2;
			}
			gridlines.push({
				key: `v-${xPosition}`,
				x1: xPosition,
				y1: startPosition.y,
				x2: xPosition,
				y2: endPosition.y,
				color,
				strokeWidth
			});
		}

		return gridlines;
	});

	/** Functions. */

	/**
	 * Given a position, returns the closest position that matches a grid,
	 * meaning that it lies on a gridline or equally between two gridlines,
	 * with all other grids having a higher priority over the background grid.
	 *
	 * Returns the original position if snapping to grid is disabled.
	 * @param pos The position to snap.
	 * @returns The snapped position
	 */
	function snapToGrid(pos: Position): Position {
		if (!config.value.snapToGrid) {
			return pos;
		}

		/** TODO: support other grids than the background grid. */

		return {
			x: roundUpToStep(pos.x, pixelsPerBackgroundGridline / 2),
			y: roundUpToStep(pos.y, pixelsPerBackgroundGridline / 2)
		};
	}

	return {
		get config() {
			return config.value;
		},
		set config(newVal) {
			config.value = newVal;
		},
		get visibleGridlines() {
			return visibleGridlines;
		},
		snapToGrid
	};
}
export default createCanvasGridManager;

export type CanvasGridManager = ReturnType<typeof createCanvasGridManager>;
