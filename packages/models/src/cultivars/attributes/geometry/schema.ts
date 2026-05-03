import type { GeometryType } from '../../../workspaces/schema.js';

/** Stored as JSON in cultivar attributes. */
export interface ExpectedGeometryProfile {
	geometryType?: GeometryType;
	peakSize?: number;
	seedlingScaleFactor?: number;
	firstHarvestScaleFactor?: number;
	lastHarvestScaleFactor?: number;
	expiryScaleFactor?: number;
	exitDormancyScaleFactor?: number;
	enterDormancyScaleFactor?: number;
}
