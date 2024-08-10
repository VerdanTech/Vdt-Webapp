/**
 * Contains Mock Service Worker setup and configuration
 */

import { setupWorker } from 'msw/browser'
import { getUsersMock } from '$codegen/client/users/users.msw'
import { getGardensMock } from '$codegen/client/gardens/gardens.msw'

const mock_handlers = [...getUsersMock(), ...getGardensMock()]

export const worker = setupWorker(...mock_handlers)

export async function enableMocking() {
	if (process.env.NODE_ENV !== 'development') {
		return
	}

	const { worker } = await import('./mocks')

	// `worker.start()` returns a Promise that resolves
	// once the Service Worker is up and ready to intercept requests.
	return worker.start({
		onUnhandledRequest(request, print) {
			// Do not warn on unhandled internal Svelte requests.
			// Those are not meant to be mocked.
			if (request.url.includes('svelte')) {
				return
			}

			print.warning()
		}
	})
}
