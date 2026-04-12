import { diContainer } from '@fastify/awilix';
import { AuthenticationError, NotFoundError } from 'common/errors.js';

import { type UserLoginCommand } from '@vdg-webapp/models';

import { getAccountByVerifiedEmail, getProfileById } from '../../controllers/users.js';
import { verifyPassword } from '../auth/passwords.js';
import { encodeAccessToken, encodeRefreshToken } from '../auth/tokens.js';

export type UserLoginResult = {
	/** The encoded access token. */
	accessToken: string;
	/** The encoded refresh token. */
	refreshToken: string;
};

/**
 * Authenticates the user and provides encoded JWT tokens.
 * @param command The login command.
 * @param container The service locator.
 * @returns The encoded access and refresh tokens and the access expiry time.
 */
const login = async (
	command: UserLoginCommand,
	container: typeof diContainer
): Promise<UserLoginResult> => {
	const db = container.resolve('db');

	/** Fetch the user from the database. */
	const userAccount = await getAccountByVerifiedEmail(db, command.email);
	if (userAccount == null) {
		throw new NotFoundError('User does not exist', {
			fieldErrors: { email: ['This email does not exist.'] }
		});
	}
	const userProfile = await getProfileById(db, userAccount.profileId);
	if (userProfile == null) {
		throw new NotFoundError('User does not exist', {
			fieldErrors: { email: ['This email does not exist.'] }
		});
	}

	/** Verify the provided password. */
	if ((await verifyPassword(command.password, userAccount.passwordHash)) == false) {
		throw new AuthenticationError('Incorrect password', {
			fieldErrors: { password: ['This password is incorrect.'] }
		});
	}

	/** Encode both access and refresh tokens. */
	const accessToken = await encodeAccessToken(
		userAccount.id,
		userProfile.id,
		userProfile.username
	);
	const refreshToken = await encodeRefreshToken(userAccount.id);

	return { accessToken, refreshToken };
};
export default login;
