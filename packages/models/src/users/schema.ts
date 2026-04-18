import {co, z} from "jazz-tools"

const UserRootSchema = co.map({
	email: z.email()
})

export const UserProfileSchema = co.profile({
	name: z.string()
})

export const UserSchema = co.account({
	root: UserRootSchema,
	profile: UserProfileSchema
})

export type User = co.loaded<typeof UserSchema>
export type UserProfile = co.loaded<typeof UserProfileSchema>
