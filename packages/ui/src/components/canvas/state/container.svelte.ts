/**
 * Context which stores the SVG root element reference and
 * container div sizing.
 * @param canvasId The ID of the canvas context.
 * @returns The container context.
 */
export function createCanvasContainer(canvasId: string) {
	/** Consts. */
	const containerId = canvasId; /** ID of the container HTML element. */
	let pixelsPerMeter = $state(100); /** The initial scale of rendering, pre-scaling. */

	/** The root SVG element that all shapes are rendered within. */
	let stageElement: SVGSVGElement | null = $state(null);

	/** Runes. */
	let initialized = $state(false);
	let height = $state(0);
	let width = $state(0);

	/**
	 * Used when the container is resized. The width/height runes are
	 * bound directly from the container div, so no further action is
	 * needed beyond notifying that initialization is complete.
	 */
	function onResize() {}

	/**
	 * Initializes the canvas.
	 */
	function initialize() {
		initialized = true;
	}

	return {
		get containerId() {
			return containerId;
		},
		get stageElement() {
			return stageElement;
		},
		set stageElement(newVal: SVGSVGElement | null) {
			stageElement = newVal;
		},
		get pixelsPerMeter() {
			return pixelsPerMeter;
		},
		get initialized() {
			return initialized;
		},
		get width() {
			return width;
		},
		get height() {
			return height;
		},
		set width(newVal: number) {
			width = newVal;
		},
		set height(newVal: number) {
			height = newVal;
		},
		set pixelsPerMeter(newVal) {
			pixelsPerMeter = newVal;
		},

		initialize,
		onResize
	};
}
export default createCanvasContainer;

export type CanvasContainer = ReturnType<typeof createCanvasContainer>;
