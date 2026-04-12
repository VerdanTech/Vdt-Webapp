import { eq, inArray, sql } from 'drizzle-orm';

import {
	type Cultivar,
	type CultivarCollection,
	cultivarCollections,
	cultivars,
	mergeAttributes
} from '@vdg-webapp/models';

import { type Db } from '../db/index.js';

const MAX_INHERITANCE_DEPTH = 16;

/**
 * Resolves all cultivar collections in a garden, including their full ancestor
 * chains, using a single recursive CTE. Replaces the iterative Triplit approach
 * and eliminates the need for the denormalized ancestorIds field.
 */
export async function resolveCultivarCollections(
	db: Db,
	gardenId: string
): Promise<CultivarCollection[]> {
	const result = await db.execute<CultivarCollection>(sql`
		WITH RECURSIVE chain AS (
			SELECT *, 0 AS depth
			FROM cultivar_collections
			WHERE garden_id = ${gardenId}

			UNION ALL

			SELECT c.*, chain.depth + 1
			FROM cultivar_collections c
			INNER JOIN chain ON c.id = chain.parent_id
			WHERE chain.depth < ${MAX_INHERITANCE_DEPTH}
		)
		SELECT DISTINCT ON (id)
			id, name, slug, visibility, user_id, garden_id,
			priority, description, parent_id, created_at
		FROM chain
		ORDER BY id, depth
	`);
	return result.rows;
}

/**
 * Given a cultivar name, finds the matching cultivar ID in the garden.
 * Collections are sorted by priority. The first match walking child → ancestor
 * is returned. When multiple cultivars share a name in one collection, the
 * newest is chosen.
 */
export async function resolveCultivarName(
	db: Db,
	gardenId: string,
	cultivarName: string
): Promise<string | null> {
	/** One query: all cultivars named `cultivarName` in any relevant collection,
	 *  joined with their collection priority and ancestry depth. */
	const result = await db.execute<{
		id: string;
		created_at: Date;
		priority: number;
		depth: number;
	}>(sql`
		WITH RECURSIVE chain AS (
			SELECT id, priority, parent_id, 0 AS depth
			FROM cultivar_collections
			WHERE garden_id = ${gardenId}

			UNION ALL

			SELECT c.id, c.priority, c.parent_id, chain.depth + 1
			FROM cultivar_collections c
			INNER JOIN chain ON c.id = chain.parent_id
			WHERE chain.depth < ${MAX_INHERITANCE_DEPTH}
		)
		SELECT cv.id, cv.created_at, ch.priority, ch.depth
		FROM cultivars cv
		INNER JOIN chain ch ON cv.collection_id = ch.id
		WHERE cv.name = ${cultivarName}
		ORDER BY ch.priority ASC, ch.depth ASC, cv.created_at DESC
		LIMIT 1
	`);
	const rows = result.rows;

	return rows[0]?.id ?? null;
}

/**
 * Resolves a cultivar by ID, merging inherited attributes from its parent chain.
 * Uses a recursive CTE — no iterative fetchById loop needed.
 */
export async function resolveCultivarId(
	db: Db,
	cultivarId: string
): Promise<Cultivar | null> {
	const { rows } = await db.execute<Cultivar>(sql`
		WITH RECURSIVE chain AS (
			SELECT *, 0 AS depth
			FROM cultivars
			WHERE id = ${cultivarId}

			UNION ALL

			SELECT c.*, chain.depth + 1
			FROM cultivars c
			INNER JOIN chain ON c.id = chain.parent_id
			WHERE chain.depth < ${MAX_INHERITANCE_DEPTH}
		)
		SELECT id, collection_id, name, abbreviation, scientific_name,
		       description, parent_id, attributes, created_at
		FROM chain
		ORDER BY depth ASC
	`);

	if (rows.length === 0) return null;
	if (rows.length === 1) return rows[0];

	/** Merge: root (last row) is the base, each child overrides. */
	let result = rows[rows.length - 1];
	for (let i = rows.length - 2; i >= 0; i--) {
		result = mergeAttributes(result, rows[i]) as Cultivar;
	}
	return result;
}

/** Resolves a cultivar by name within a garden. */
export async function resolveCultivar(
	db: Db,
	gardenId: string,
	cultivarName: string
): Promise<Cultivar | null> {
	const cultivarId = await resolveCultivarName(db, gardenId, cultivarName);
	if (!cultivarId) return null;
	return resolveCultivarId(db, cultivarId);
}

/**
 * Returns all unique cultivar names available in a garden,
 * across all collections and their ancestor chains.
 */
export async function getAllCultivarNames(db: Db, gardenId: string): Promise<string[]> {
	const { rows } = await db.execute<{ name: string }>(sql`
		WITH RECURSIVE chain AS (
			SELECT id, parent_id, 0 AS depth
			FROM cultivar_collections
			WHERE garden_id = ${gardenId}

			UNION ALL

			SELECT c.id, c.parent_id, chain.depth + 1
			FROM cultivar_collections c
			INNER JOIN chain ON c.id = chain.parent_id
			WHERE chain.depth < ${MAX_INHERITANCE_DEPTH}
		)
		SELECT DISTINCT cv.name
		FROM cultivars cv
		INNER JOIN chain ON cv.collection_id = chain.id
	`);

	return rows.map((r) => r.name);
}
