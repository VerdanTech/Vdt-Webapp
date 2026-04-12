/**
 * Re-exports all Drizzle table definitions and relation objects.
 * Import this as a namespace to pass into drizzle({ schema }) for
 * relational query support.
 *
 * @example
 * import * as schema from '@vdg-webapp/models/tables'
 * const db = drizzle(pool, { schema })
 */
export * from './users/schema.js';
export * from './gardens/schema.js';
export * from './workspaces/schema.js';
export * from './environments/schema.js';
export * from './cultivars/schema.js';
export * from './observations/schema.js';
export * from './plants/schema.js';
