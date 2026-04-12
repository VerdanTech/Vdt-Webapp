import { diContainer, fastifyAwilixPlugin } from '@fastify/awilix';
import { Lifetime, asClass, asValue } from 'awilix';
import EmailSender from 'common/emails/sender.js';
import { FastifyInstance } from 'fastify';

import { type UserAccount } from '@vdg-webapp/models';

import { db } from '../db/index.js';

/** Declares the types of dependencies available in the DI container. */
declare module '@fastify/awilix' {
	interface Cradle {
		db: typeof db;
		emailSender: EmailSender;
	}
	interface RequestCradle {
		client: UserAccount | null;
	}
}

export const registerDiContainer = (app: FastifyInstance) => {
	app.register(fastifyAwilixPlugin);

	/** Postgres / Drizzle database. */
	diContainer.register({
		db: asValue(db)
	});

	/** Email. */
	diContainer.register({
		emailSender: asClass(EmailSender, {
			lifetime: Lifetime.SINGLETON
		})
	});
};
