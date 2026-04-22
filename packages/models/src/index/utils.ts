import { AppError } from '../errors.js';
import { type GardenMembership, type GardenWithMemberships } from '../gardens/schema.js';
import { GLOBAL_COVAL_ID_PUBLIC_INDEX, GlobalIndex, GlobalIndexSchema } from './schema.js';

/**
 * Loads and returns the global index, throwing if inaccessible.
 */
export async function getGlobalIndex(): Promise<GlobalIndex> {
	const result = await GlobalIndexSchema.load(GLOBAL_COVAL_ID_PUBLIC_INDEX, {
		resolve: { gardens: true }
	});
	if (!result.$isLoaded) {
		throw new AppError('Failed to load the global index.');
	}
	return result;
}

/**
 * Loads a garden by its unique key from the global index, with memberships and
 * their associated user accounts resolved.
 * @param gardenKey The unique key (slug) of the garden.
 * @returns The loaded garden.
 */
export async function getGardenByKey(gardenKey: string): Promise<GardenWithMemberships> {
	const index = await getGlobalIndex();
	const maybeGarden = index.gardens[gardenKey];

	if (!maybeGarden || !maybeGarden.$isLoaded) {
		throw new AppError('Garden not found.', {
			nonFormErrors: ['Garden key does not exist.']
		});
	}

	const garden = await maybeGarden.$jazz.ensureLoaded({
		resolve: { memberships: { $each: { user: true } } }
	});

	return garden;
}

/**
 * Searches a garden's membership list for an accepted membership belonging to
 * the given account ID.
 * @param garden The garden to search.
 * @param accountId The Jazz account ID to match against.
 * @returns The matching membership, or undefined if none found.
 */
export function findAcceptedMembershipForAccount(
	garden: GardenWithMemberships,
	accountId: string
): GardenMembership | undefined {
	if (!garden.memberships) {
		return undefined;
	}

	for (const membership of garden.memberships) {
		if (!membership || !membership.$isLoaded) {
			continue;
		}

		if (!membership.user || !membership.user.$isLoaded) {
			continue;
		}

		if (membership.status !== 'ACCEPTED') {
			continue;
		}

		if (membership.user.$jazz.id !== accountId) {
			continue;
		}

		return membership;
	}

	return undefined;
}
