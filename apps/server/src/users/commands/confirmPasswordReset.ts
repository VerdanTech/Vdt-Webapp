import { diContainer } from '@fastify/awilix';
import { ValidationError } from 'common/errors.js';
import { hashPassword } from 'users/auth/passwords.js';
import { decodePasswordResetToken } from 'users/auth/tokens.js';

import { type UserConfirmPasswordResetCommand } from '@vdg-webapp/models';

import { getAccountById, updatePassword } from '../../controllers/users.js';

/**
 * Closes a password reset request.
 * @param command The request command.
 * @param container The service locator.
 */
const confirmPasswordReset = async (
	command: UserConfirmPasswordResetCommand,
	container: typeof diContainer
) => {
	const db = container.resolve('db');

	/** Decode the token. */
	const token = await decodePasswordResetToken(command.token);
	if (token == null) {
		throw new ValidationError(
			'Failure while decoding password reset token - expired or malformed.',
			{ nonFormErrors: ['Invalid password reset token.'] }
		);
	}

	/** Retrieve the user from the token. */
	const user = await getAccountById(db, token.accountId);
	if (user == null) {
		throw new ValidationError(
			'Failure while decoding password reset token - user does not exist.',
			{ nonFormErrors: ['Invalid password reset token.'] }
		);
	}

	/** Ensure the user has a password reset request with the provided token. */
	if (user.passwordResetToken != command.token || user.id != command.userId) {
		throw new ValidationError(
			'Failure while decoding password reset token - token does not exist',
			{ nonFormErrors: ['Invalid password reset token.'] }
		);
	}

	/** Update the password. */
	const passwordHash = await hashPassword(command.password1);
	await updatePassword(db, user.id, passwordHash);
};
export default confirmPasswordReset;
