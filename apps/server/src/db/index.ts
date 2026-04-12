import { drizzle } from 'drizzle-orm/node-postgres';
import pg from 'pg';

import * as schema from '@vdg-webapp/models/tables';
import env from '../env.js';

const pool = new pg.Pool({ connectionString: env.DATABASE_URL });

export const db = drizzle(pool, { schema });
export type Db = typeof db;
