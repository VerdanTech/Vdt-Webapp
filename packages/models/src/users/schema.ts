import { boolean, pgTable, text, timestamp, uuid } from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';

export const profiles = pgTable('profiles', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** Username. Unique and used within the app to search for users. */
	username: text('username').notNull().unique(),

	/** Date of user creation. */
	createdAt: timestamp('created_at').defaultNow().notNull()
});

export const accounts = pgTable('accounts', {
	id: uuid('id').primaryKey().defaultRandom(),

	/** The ID of the associated profile. */
	profileId: uuid('profile_id')
		.notNull()
		.references(() => profiles.id),

	/** Hashed password. */
	passwordHash: text('password_hash').notNull(),

	/** Primary email address. Only verified emails use this field. */
	verifiedEmail: text('verified_email'),

	/**
	 * Secondary email address. Used to avoid replacing primary email when switching.
	 * Upon verification, should be nulled and used to set verifiedEmail.
	 */
	unverifiedEmailAddress: text('unverified_email_address'),

	/** JWT confirmation token sent to the user for email verification. */
	unverifiedEmailToken: text('unverified_email_token'),

	/** JWT confirmation token used to confirm a password reset. */
	passwordResetToken: text('password_reset_token'),

	/** Set to false for inactive users. */
	isActive: boolean('is_active').default(true).notNull()
});

export const accountsRelations = relations(accounts, ({ one }) => ({
	profile: one(profiles, {
		fields: [accounts.profileId],
		references: [profiles.id]
	})
}));

export type UserProfile = typeof profiles.$inferSelect;
export type UserAccount = typeof accounts.$inferSelect;
export type User = { account: UserAccount; profile: UserProfile };
