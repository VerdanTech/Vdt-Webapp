type SelectTool = 'pointer' | 'group' | 'union' | 'intersect';

export function createSelectionGroup() {
	/** Runes. */
	const selectTool: SelectTool = $state('pointer');

	function setDocumentCursor() {
		switch (selectTool) {
			case 'pointer':
				document.body.style.cursor = 'default';
				break;
			case 'group':
				document.body.style.cursor = 'crosshair';
				break;
			case 'union':
				document.body.style.cursor = 'crosshair';
				break;
			case 'intersect':
				document.body.style.cursor = 'crosshair';
				break;
		}
	}

	return {
		setDocumentCursor
	};
}
export default createSelectionGroup;

export type SelectGroup = ReturnType<typeof createSelectionGroup>;
