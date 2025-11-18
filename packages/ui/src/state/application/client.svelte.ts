import { useQuery } from '@triplit/svelte';

import { type ControllerContext } from '@vdg-webapp/models';

export type ClientContextParams = {
	accountIdOverride?: string;
};

/**
 * Holds context for the user client.
 * By default, uses the session ID set by Triplit's auth process.
 * Allows a static ID override for testing and demo app.
 */
export function createClientContext(
	controller: ControllerContext,
	params?: ClientContextParams
) {
	const clientQuery = $derived(
		useQuery(
			controller.triplit,
			controller.triplit.query('accounts').Id('$session.accountId').Include('profile')
		)
	);
	const clientOverrideQuery = $derived(
		params?.accountIdOverride
			? useQuery(
					controller.triplit,
					controller.triplit
						.query('accounts')
						.Id(params.accountIdOverride)
						.Include('profile')
				)
			: null
	);
	const account = $derived.by(() => {
		if (clientOverrideQuery && clientOverrideQuery.results) {
			return clientOverrideQuery.results[0];
		}

		if (clientQuery.results) {
			return clientQuery.results[0];
		}

		return null;
	});

	return {
		get account() {
			return account;
		},
		get profile() {
			return account?.profile;
		}
	};
}
export type ClientContext = ReturnType<typeof createClientContext>;
