/** TypeScript type for the annual life cycle attribute, stored as jsonb. */
export type AnnualLifeCycleProfile = {
	sowToGerm?: number;
	germToTransplant?: number;
	germToFirstHarvest?: number;
	firstToLastHarvest?: number;
};
