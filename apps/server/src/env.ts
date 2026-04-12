import { z } from 'zod';

const EnvSchema = z.object({
	/** Email verification. */
	EMAIL_VERIFICATION_REQUIRED: z
		.boolean({
			description:
				'If true, users will not be able to log in before confirming their email. If false, the email begins verified.'
		})
		.default(true),

	/** Postgres. */
	DATABASE_URL: z
		.string({ description: 'The connection string for the Postgres database.' })
		.default('postgres://postgres:postgres@localhost:5432/verdagraph'),

	/** Triplit. */
	TRIPLIT_URL: z
		.string({ description: 'The URL of the Triplit database server.' })
		.url()
		.default('http://localhost:6543'),
	TRIPLIT_SERVER_TOKEN: z
		.string({
			description:
				'The service JWT token provided by triplit for access to the database by the server.'
		})
		.default(
			'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ4LXRyaXBsaXQtdG9rZW4tdHlwZSI6InNlY3JldCIsIngtdHJpcGxpdC1wcm9qZWN0LWlkIjoibG9jYWwtcHJvamVjdC1pZCJ9.UvSPskzroY-eB0o46-uZWA_I932KgKn6aMsLyEpGs64'
		),

	/** Networking. */
	CLIENT_BASE_URL: z
		.string({ description: 'The base URL which points to the frontend.' })
		.default('http://localhost:5173'),
	USING_HTTPS: z
		.boolean({
			description: 'True if HTTPS connections are being used with the client.'
		})
		.default(false),
	CLIENT_SAMESITE: z
		.boolean({
			description: 'True if the client is served from the same domain as the server.'
		})
		.default(false),
	APP_HOST: z
		.string({ description: 'The host the server process is running on.' })
		.default('localhost'),
	APP_PORT: z
		.number({ description: 'The port the server process is running on' })
		.default(8000),

	/** JWTs. */
	ACCESS_TOKEN_SECRET: z
		.string({
			description: 'The secret used to encode JWT access tokens.'
		})
		.default('secret'),
	REFRESH_TOKEN_SECRET: z
		.string({
			description: 'The secret used to encode JWT refresh tokens.'
		})
		.default('secret'),
	EMAIL_CONFIRMATION_TOKEN_SECRET: z
		.string({
			description: 'The secret used to encode JWT email confirmation tokens.'
		})
		.default('secret'),
	PASSWORD_RESET_TOKEN_SECRET: z
		.string({
			description: 'The secret used to encode JWT password reset tokens.'
		})
		.default('secret'),
	REFRESH_TOKEN_EXPIRY_S: z
		.number({
			description: 'The expiry duration for JWT refresh tokens, in seconds.'
		})
		.default(3 * 24 * 60 * 60),
	EMAIL_CONFIRMATION_TOKEN_EXPIRY_S: z
		.number({
			description: 'The expiry duration for JWT email confirmation tokens, in seconds.'
		})
		.default(3 * 24 * 60 * 60),
	PASSWORD_RESET_TOKEN_EXPIRY_S: z
		.number({
			description: 'The expiry duration for JWT password reset tokens, in seconds.'
		})
		.default(3 * 24 * 60 * 60),
	COOKIE_SECRET: z
		.string({
			description: 'The secret used to encode cookie signatures.'
		})
		.default('secret'),

	/** Emails. */
	SMTP_HOST: z
		.string({ description: 'The host of the SMTP server used for sending emails.' })
		.default('localhost'),
	SMTP_PORT: z
		.number({ description: 'The port of the SMTP server used for sending emails.' })
		.default(1025),
	SMTP_USERNAME: z
		.string({ description: "The username of the server's user on the SMTP server" })
		.default('severSmtpUser'),
	SMTP_PASSWORD: z
		.string({ description: "The password of the server's user on the SMTP server." })
		.default('serverSmtpPassword'),
	SMTP_SENDER: z
		.string({
			description: "The email address of the server's user on the SMTP server."
		})
		.email()
		.default('Verdagraph@email.com')
});

const env = EnvSchema.parse(process.env);
export default env;
