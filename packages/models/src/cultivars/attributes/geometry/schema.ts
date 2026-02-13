import { Schema as S } from '@triplit/client';

import { GeometryTypeEnumOptions } from '../../../workspaces/schema.js';

/** Schema. */
export const ExpectedGeometryProfile = S.Record({
	geometryType: S.Optional(S.String({ enum: GeometryTypeEnumOptions })),
	peakSize: S.Optional(S.Number()),
	seedlingScaleFactor: S.Optional(S.Number()),
	firstHarvestScaleFactor: S.Optional(S.Number()),
	lastHarvestScaleFactor: S.Optional(S.Number()),
	expiryScaleFactor: S.Optional(S.Number()),
	exitDormancyScaleFactor: S.Optional(S.Number()),
	enterDormancyScaleFactor: S.Optional(S.Number())
});
