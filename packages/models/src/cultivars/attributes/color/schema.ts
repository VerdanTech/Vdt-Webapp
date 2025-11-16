import { Schema as S } from '@triplit/client';

/** Schema. */
export const ColorProfile = S.Record({
	baseColor: S.Optional(S.String()),
	outlineColor: S.Optional(S.String()),
 	textColor: S.Optional(S.String()),
});
