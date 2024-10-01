export const gardenFields = {
	garden_name: {
		min_length: {
			value: 2,
			message: 'Must be at least 2 characters'
		},
		max_length: {
			value: 50,
			message: 'Must be at most 50 characters'
		},
		pattern: {
			value: /[0-9A-Za-z ]+/,
			message: 'Must contain only alphanumeric characters and spaces'
		},
		description:
			'Must be between 2 and 50 characters long and contain only alphanumeric characters and spaces'
	},
	garden_key: {
		min_length: {
			value: 4,
			message: 'Must be at least 4 characters'
		},
		max_length: {
			value: 16,
			message: 'Must be at most 16 characters'
		},
		pattern: {
			value: /[0-9A-Za-z-]+/,
			message: 'Must contain only alphanumeric characters and hyphens'
		},
		description:
			'Must be between 4 and 16 characters long and contain only alphanumeric characters and hyphens'
	},
	garden_description: {
		max_length: {
			value: 1400,
			message: 'Must be at most 1400 characters'
		},
		description: 'Must be at most 1400 characters'
	},
	user_invites_list: {
		max_length: {
			value: 10,
			message: 'A maximum of 10 users can be invited at once'
		},
		description: 'A maximum of 10 users can be invited at once'
	}
};
export default gardenFields;
