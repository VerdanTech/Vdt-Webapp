/**
 * Contains Mock Service Worker setup and configuration
 */

import { setupWorker } from 'msw/browser'
import { getUsersMock } from '$codegen/client/users/users.msw'
import { getGardensMock } from '$codegen/client/gardens/gardens.msw'

const mock_handlers = [...getUsersMock(), ...getGardensMock()]

export const worker = setupWorker(...mock_handlers)

export async function enableMocking() {
	return
	const { worker } = await import('./mocks')

	// `worker.start()` returns a Promise that resolves
	// once the Service Worker is up and ready to intercept requests.
	console.log('Mocking enabled')
	return worker.start({
		onUnhandledRequest(request, print) {
			// Do not warn on unhandled internal requests.
			// All relevant mocked handlers are automatically generated.
			return
		}
	})
}
