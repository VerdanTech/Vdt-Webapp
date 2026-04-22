import {z} from 'jazz-tools'

/** Field specifications for user domain commands. */
const userFields = {
	usernameField: z
		.string()
		.trim()
		.min(3, 'Must be at least 3 characters.')
		.max(50, 'May be at most 50 characters.')
		.regex(
			/^[a-zA-Z0-9-_]*$/,
			'Must contain only letters, numbers, hyphens, and underscores.'
		)
		.describe(
			'Unique username to identify yourself in the application. May be changed later.'
		),
	emailField: z
		.string()
		.email('Must be a valid email address.')
		.describe('Must be a valid email address.'),
	passwordField: z
		.string()
		.min(6, 'Must be at least 6 characters.')
		.max(255, 'Must be at most 255 characters.')
		.describe('Must be between 6 and 255 characters long.')
};
export default userFields;
