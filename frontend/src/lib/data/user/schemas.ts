/**
 * Central file to store descriptions of valid mutation schemas.
 * Ideally, these would be generated from the OpenAPI schema.
 * However no tool currently has the ability to pull the description
 * from the generated schema and into the zod schema, especially when
 * dealing with regular expressions. Thus they are manually defined here,
 * and must be maintained by hand.
 *
 * The ideal approach in the future would be to continue adding schema descriptions
 * on the backend so they get into the schema, then add a feature to Orval which
 * takes the schema description and makes it into another variable, so they
 * don't have to be defined here. They would still have to be contstructed manually however,
 * as ideally we want to run the descriptions through a translator.
 */
import { z as zod } from 'zod'
import {
	userLoginCommandOpBodyPasswordMin as passwordMinLen,
	userLoginCommandOpBodyPasswordMax as passwordMaxLen,
	userLoginCommandOpBodyPasswordRegExp as passwordPattern,
	userCreateCommandOpBodyUsernameMax as usernameMax,
	userCreateCommandOpBodyUsernameMin as usernameMin,
	userCreateCommandOpBodyUsernameRegExp as usernamePattern
} from '$codegen/zod/users'

/* Regex descriptions are formatted as "Must ...conditions. <RegexDescreption>." */
const userDescriptions = {
	usernamePattern: `Must contain only alphanumeric characters and underscores`,
	username: (minLen: number, maxLen: number, batternDescription: string) =>
		`Must be between ${minLen} and ${maxLen} characters long. ${batternDescription}.`,
	email: 'Must be a valid email address.',
	passwordPattern: `Must contain at least one lowercase letter, one uppercase letter, and one digit`,
	password: (minLen: number, maxLen: number, batternDescription: string) =>
		`Must be between ${minLen} and ${maxLen} characters long. ${batternDescription}.`
}
export const userFieldSchemas = {
	username: zod
		.string()
		.min(usernameMin)
		.max(usernameMax)
		.regex(usernamePattern, userDescriptions.usernamePattern)
		.describe(
			userDescriptions.username(
				usernameMin,
				usernameMax,
				userDescriptions.usernamePattern
			)
		),
	email: zod.string().email(userDescriptions.email).describe(userDescriptions.email),
	password: zod
		.string()
		.min(passwordMinLen)
		.max(passwordMaxLen)
		.regex(passwordPattern, userDescriptions.passwordPattern)
		.describe(
			userDescriptions.password(
				passwordMinLen,
				passwordMaxLen,
				userDescriptions.passwordPattern
			)
		)
}
