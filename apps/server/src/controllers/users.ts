import { eq, or } from 'drizzle-orm';

import { accounts, profiles, type User, type UserAccount, type UserProfile } from '@vdg-webapp/models';

import { type Db } from '../db/index.js';

/** Reads. */

export async function getAccountById(db: Db, id: string): Promise<UserAccount | null> {
	const result = await db.query.accounts.findFirst({
		where: eq(accounts.id, id)
	});
	return result ?? null;
}

export async function getProfileById(db: Db, id: string): Promise<UserProfile | null> {
	const result = await db.query.profiles.findFirst({
		where: eq(profiles.id, id)
	});
	return result ?? null;
}

export async function getAccountByVerifiedEmail(
	db: Db,
	email: string
): Promise<UserAccount | null> {
	const result = await db.query.accounts.findFirst({
		where: eq(accounts.verifiedEmail, email)
	});
	return result ?? null;
}

export async function getAccountByUnverifiedEmail(
	db: Db,
	email: string
): Promise<UserAccount | null> {
	const result = await db.query.accounts.findFirst({
		where: eq(accounts.unverifiedEmailAddress, email)
	});
	return result ?? null;
}

export async function emailExists(db: Db, email: string): Promise<boolean> {
	const result = await db.query.accounts.findFirst({
		where: or(
			eq(accounts.verifiedEmail, email),
			eq(accounts.unverifiedEmailAddress, email)
		),
		columns: { id: true }
	});
	return result != null;
}

export async function usernameExists(db: Db, username: string): Promise<boolean> {
	const result = await db.query.profiles.findFirst({
		where: eq(profiles.username, username),
		columns: { id: true }
	});
	return result != null;
}

/** Writes — all return txid for Electric optimistic reconciliation. */

export async function userCreate(
	db: Db,
	username: string,
	passwordHash: string,
	email: string,
	verificationRequired: boolean
): Promise<User & { txid: number }> {
	return db.transaction(async (tx) => {
		const [profile] = await tx.insert(profiles).values({ username }).returning();

		const [account] = await tx
			.insert(accounts)
			.values({
				profileId: profile.id,
				passwordHash,
				...(verificationRequired
					? { unverifiedEmailAddress: email }
					: { verifiedEmail: email })
			})
			.returning();

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			'SELECT pg_current_xact_id()::xid::text AS txid'
		);

		return { account, profile, txid: parseInt(txid) };
	});
}

export async function updateUsername(
	db: Db,
	profileId: string,
	username: string
): Promise<{ txid: number }> {
	return db.transaction(async (tx) => {
		await tx.update(profiles).set({ username }).where(eq(profiles.id, profileId));
		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			'SELECT pg_current_xact_id()::xid::text AS txid'
		);
		return { txid: parseInt(txid) };
	});
}

export async function updatePassword(
	db: Db,
	accountId: string,
	passwordHash: string
): Promise<{ txid: number }> {
	return db.transaction(async (tx) => {
		await tx.update(accounts).set({ passwordHash }).where(eq(accounts.id, accountId));
		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			'SELECT pg_current_xact_id()::xid::text AS txid'
		);
		return { txid: parseInt(txid) };
	});
}

export async function updateEmail(
	db: Db,
	accountId: string,
	email: string,
	verificationRequired: boolean
): Promise<{ txid: number }> {
	return db.transaction(async (tx) => {
		await tx
			.update(accounts)
			.set(
				verificationRequired
					? { unverifiedEmailAddress: email }
					: { verifiedEmail: email }
			)
			.where(eq(accounts.id, accountId));

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			'SELECT pg_current_xact_id()::xid::text AS txid'
		);
		return { txid: parseInt(txid) };
	});
}

export async function addEmailVerificationToken(
	db: Db,
	accountId: string,
	token: string
): Promise<{ txid: number }> {
	return db.transaction(async (tx) => {
		await tx
			.update(accounts)
			.set({ unverifiedEmailToken: token })
			.where(eq(accounts.id, accountId));
		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			'SELECT pg_current_xact_id()::xid::text AS txid'
		);
		return { txid: parseInt(txid) };
	});
}

export async function verifyEmail(db: Db, accountId: string): Promise<{ txid: number }> {
	return db.transaction(async (tx) => {
		const account = await tx.query.accounts.findFirst({
			where: eq(accounts.id, accountId),
			columns: { unverifiedEmailAddress: true }
		});
		if (!account?.unverifiedEmailAddress) {
			throw new Error('No unverified email on user when one was expected.');
		}

		await tx
			.update(accounts)
			.set({
				verifiedEmail: account.unverifiedEmailAddress,
				unverifiedEmailAddress: null,
				unverifiedEmailToken: null
			})
			.where(eq(accounts.id, accountId));

		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			'SELECT pg_current_xact_id()::xid::text AS txid'
		);
		return { txid: parseInt(txid) };
	});
}

export async function addPasswordResetToken(
	db: Db,
	accountId: string,
	token: string
): Promise<{ txid: number }> {
	return db.transaction(async (tx) => {
		await tx
			.update(accounts)
			.set({ passwordResetToken: token })
			.where(eq(accounts.id, accountId));
		const { rows: [{ txid }] } = await tx.execute<{ txid: string }>(
			'SELECT pg_current_xact_id()::xid::text AS txid'
		);
		return { txid: parseInt(txid) };
	});
}
