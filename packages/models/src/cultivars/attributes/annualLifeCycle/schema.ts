/** Stored as JSON in cultivar attributes. */
export interface AnnualLifeCycleProfile {
	sowToGerm?: number;
	germToTransplant?: number;
	germToFirstHarvest?: number;
	firstToLastHarvest?: number;
}
