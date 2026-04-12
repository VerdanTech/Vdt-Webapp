import { diContainer } from '@fastify/awilix';
import { ValidationError } from 'common/errors.js';
import { AuthenticationError } from 'common/errors.js';
import env from 'env.js';

import { type UserAccount, type UserUpdateCommand } from '@vdg-webapp/models';

import {
	emailExists,
	updateEmail,
	updatePassword,
	updateUsername,
	usernameExists
} from '../../controllers/users.js';
import { hashPassword, verifyPassword } from '../auth/passwords.js';

/**
 * Updates an existing user in the database.
 * @param command The update command.
 * @param container The service locator.
 */
const update = async (
	command: UserUpdateCommand,
	container: typeof diContainer,
	client: UserAccount
) => {
	const db = container.resolve('db');

	/** Validate command against existing database state. */
	if (command.newEmail) {
		if (await emailExists(db, command.newEmail)) {
			throw new ValidationError('Email exists', {
				fieldErrors: { email: ['This email is already registered.'] }
			});
		}
	}
	if (command.newUsername) {
		if (await usernameExists(db, command.newUsername)) {
			throw new ValidationError('Username exists', {
				fieldErrors: { username: ['This username is taken.'] }
			});
		}
	}

	/** Verify the provided password. */
	if ((await verifyPassword(command.password, client.passwordHash)) == false) {
		throw new AuthenticationError('Incorrect password', {
			fieldErrors: { password: ['This password is incorrect.'] }
		});
	}

	/** Update the email. */
	if (command.newEmail) {
		await updateEmail(db, client.id, command.newEmail, env.EMAIL_VERIFICATION_REQUIRED);

		/** Emit the event which sends the email verification. */
		if (env.EMAIL_VERIFICATION_REQUIRED) {
			/**
			 * TODO.
			 */
		}
	}

	/** Update the username. */
	if (command.newUsername) {
		await updateUsername(db, client.profileId, command.newUsername);
	}

	/** Update the password. */
	if (command.newPassword1) {
		const passwordHash = await hashPassword(command.newPassword1);
		await updatePassword(db, client.id, passwordHash);
	}
};
export default update;
