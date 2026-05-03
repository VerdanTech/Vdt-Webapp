import { getSession } from 'jazz-tools/svelte';

import { type ControllerContext } from '@vdg-webapp/models';

export type ClientContextParams = {
	accountIdOverride?: string;
};

/**
 * Holds context for the user client.
 * Uses the Jazz session from the current auth provider.
 */
export function createClientContext(
	controller: ControllerContext,
	params?: ClientContextParams
) {
	const session = $derived(getSession());

	/** TODO: Replace with Better Auth user lookup once adapter is configured. */
	const account = $derived(session ? { id: session.userId } : null);

	return {
		get account() {
			return account;
		},
		/** Stub: returns the user ID as a minimal profile until Better Auth lands. */
		get profile() {
			return account ? { id: account.id } : null;
		}
	};
}
export type ClientContext = ReturnType<typeof createClientContext>;
