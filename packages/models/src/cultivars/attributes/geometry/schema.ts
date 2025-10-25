import { Schema as S } from '@triplit/client';

import { GeometryTypeEnumOptions } from '../../../workspaces/schema.js';

/** Schema. */
export const PlantExpectedGeometryProfile = S.Record({
	geometryType: S.String({ enum: GeometryTypeEnumOptions }),
	peakSize: S.Number(),
	seedScaleFactor: S.Number(),
	seedlingScaleFactor: S.Number(),
	firstHarvestScaleFactor: S.Number(),
	lastHarvestScaleFactor: S.Number(),
	expiryScaleFactor: S.Number(),
	exitDormancyScaleFactor: S.Number(),
	enterDormancyScaleFactor: S.Number()
});
