export const workspaceFields = {
	workspace_name: {
		min_length: {
			value: 3,
			message: 'Must be at least 3 characters'
		},
		max_length: {
			value: 30,
			message: 'Must be at most 30 characters'
		},
		pattern: {
			value: /[0-9A-Za-z _-]+/,
			message:
				'Must contain only alphanumeric characters, spaces, hyphens, and underscores'
		},
		description:
			'A descriptive name for this workspace. Must be between 3 and 30 characters long and contain only alphanumeric characters, spaces, hyphens, and underscores.'
	},
	workspace_description: {
		max_length: {
			value: 700,
			message: 'Must be at most 700 characters'
		},
		description: 'A description of this workspace. Must be at most 700 characters'
	},
	workspace_planting_areas: {
		max: {
			value: 100,
			message: 'Must contain at most 100 planting areas.'
		},
		description:
			'The planting areas contained within this workspace. Planting areas describe an area in a workspace where plants may be placed. May not contain more than 100 planting areas in a workplace.'
	},
	planting_area_name: {
		min_length: {
			value: 3,
			message: 'Must be at least 3 characters'
		},
		max_length: {
			value: 30,
			message: 'Must be at most 30 characters'
		},
		pattern: {
			value: /[0-9A-Za-z _-]+/,
			message:
				'Must contain only alphanumeric characters, spaces, hyphens, and underscores'
		},
		description:
			'A descriptive name for this planting area. Must be between 3 and 30 characters long and contain only alphanumeric characters, spaces, hyphens, and underscores.'
	},
	planting_area_description: {
		max_length: {
			value: 700,
			message: 'Must be at most 700 characters'
		},
		description: 'A description of this planting area. Must be at most 700 characters'
	}
};
export default workspaceFields;
