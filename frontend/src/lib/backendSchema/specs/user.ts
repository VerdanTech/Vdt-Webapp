export const userFields = {
	username: {
		min_length: {
			value: 3,
			message: 'Must be at least 3 characters'
		},
		max_length: {
			value: 50,
			message: 'Must be at most 50 characters'
		},
		pattern: {
			value: /^[a-zA-Z0-9_]*$/,
			message: 'Must contain only alphanumeric characters and underscores'
		},
		description:
			'Must be between 3 and 50 characters long and contain only alphanumeric characters and underscores. Must be unique'
	},
	password: {
		min_length: {
			value: 6,
			message: 'Must be at least 6 characters'
		},
		max_length: {
			value: 255,
			message: 'Must be at most 255 characters'
		},
		pattern: {
			value: /^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*\W).*$/,
			message:
				'Must contain at least one lowercase letter, one uppercase letter, one digit, and one special character'
		},
		description:
			'Must be between 6 and 255 characters long and contain at least one lowercase letter, one uppercase letter, one digit, and one special character'
	}
};
export default userFields;
