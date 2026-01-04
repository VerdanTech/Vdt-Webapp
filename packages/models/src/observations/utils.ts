import { AppError } from '../errors.js';
import type { GenericObservation } from './schema.js';

export function narrowObservation<TObservation>(
	type: string,
	observation: GenericObservation
): TObservation {
	if (observation.type != type) {
		throw new AppError(
			'Observation within narrowObservation failed to narrow to the expected type.',
			{ nonFormErrors: ['Failed to retrieve observation.'] }
		);
	}

	return observation as TObservation;
}
