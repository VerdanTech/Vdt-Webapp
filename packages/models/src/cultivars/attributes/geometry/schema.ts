import type { GeometryType } from '../../../workspaces/schema.js';

export type ExpectedGeometryProfile = {
	geometryType?: GeometryType;
	peakSize?: number;
	seedlingScaleFactor?: number;
	firstHarvestScaleFactor?: number;
	lastHarvestScaleFactor?: number;
	expiryScaleFactor?: number;
	exitDormancyScaleFactor?: number;
	enterDormancyScaleFactor?: number;
};
