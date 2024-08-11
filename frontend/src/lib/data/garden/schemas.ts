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
	gardenCreateCommandOpBodyNameMax as nameMaxLen,
	gardenCreateCommandOpBodyNameMin as nameMinLen,
	gardenCreateCommandOpBodyNameRegExp as namePattern,
	gardenMembershipAcceptCommandOpBodyGardenKeyMax as keyMaxLen,
	gardenMembershipAcceptCommandOpBodyGardenKeyMin as keyMinLen,
	gardenMembershipAcceptCommandOpBodyGardenKeyRegExp as keyPattern,
	gardenCreateCommandOpBodyDescriptionMax as descriptionMaxLen
} from '$codegen/zod/gardens'
import { GardenCreateCommandVisibility } from '$codegen/types'

/* Regex descriptions are formatted as "Must ...conditions. <RegexDescreption>." */
const gardenDescriptions = {
	namePattern: `Must contain only alphanumeric characters and spaces.`,
	name: (minLen: number, maxLen: number, patternDescription: string) =>
		`Must be between ${minLen} and ${maxLen} characters long. ${patternDescription}.`,
	keyPattern: `Must contain only alphanumeric characters and hyphens.`,
	key: (minLen: number, maxLen: number, patternDescription: string) =>
		`Must be between ${minLen} and ${maxLen} characters long. ${patternDescription}.`,
	description: (maxLen: number) => `Must be less than ${maxLen} characters long.`
}
export const gardenFieldSchemas = {
	name: zod
		.string()
		.min(nameMinLen)
		.max(nameMaxLen)
		.regex(namePattern, gardenDescriptions.namePattern)
		.describe(
			gardenDescriptions.name(nameMinLen, nameMaxLen, gardenDescriptions.namePattern)
		),
	key: zod
		.string()
		.min(keyMinLen)
		.max(keyMaxLen)
		.regex(keyPattern, gardenDescriptions.keyPattern)
		.describe(
			gardenDescriptions.key(keyMinLen, keyMaxLen, gardenDescriptions.keyPattern)
		),
	description: zod
		.string()
		.max(descriptionMaxLen)
		.describe(gardenDescriptions.description(descriptionMaxLen)),
	visibility: zod.nativeEnum(GardenCreateCommandVisibility).optional()
}
