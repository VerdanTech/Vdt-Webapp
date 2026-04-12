import { diContainer } from '@fastify/awilix';
import { ValidationError } from 'common/errors.js';
import env from 'env.js';

import { type UserCreateCommand } from '@vdg-webapp/models';

import {
	addEmailVerificationToken,
	emailExists,
	userCreate,
	usernameExists
} from '../../controllers/users.js';
import { hashPassword } from '../auth/passwords.js';
import { encodeEmailConfirmationToken } from '../auth/tokens.js';

/**
 * Creates a new user in the database.
 * @param command The create command.
 * @param container The service locator.
 */
const create = async (command: UserCreateCommand, container: typeof diContainer) => {
	const db = container.resolve('db');
	const emailSender = container.resolve('emailSender');

	/** Validate command against existing database state. */
	if (await emailExists(db, command.email)) {
		throw new ValidationError('Email exists', {
			fieldErrors: { email: ['This email is already registered.'] }
		});
	}
	if (await usernameExists(db, command.username)) {
		throw new ValidationError('Username exists', {
			fieldErrors: { username: ['This username is taken.'] }
		});
	}

	/** Hash password. */
	const passwordHash = await hashPassword(command.password1);

	/** Create the objects. */
	const result = await userCreate(
		db,
		command.username,
		passwordHash,
		command.email,
		env.EMAIL_VERIFICATION_REQUIRED
	);

	/** Return if no verification is required. */
	if (!env.EMAIL_VERIFICATION_REQUIRED) {
		return;
	}

	/** Create the verification token. */
	const token = await encodeEmailConfirmationToken(result.account.id);

	/** Add the verification token to the database. */
	await addEmailVerificationToken(db, result.account.id, token);

	/** Emit the event which sends the email verification. */
	await emailSender.sendEmailConfirmationEmail(
		command.email,
		command.username,
		env.CLIENT_BASE_URL,
		env.CLIENT_BASE_URL + `/register/verify/${token}`
	);
};
export default create;
