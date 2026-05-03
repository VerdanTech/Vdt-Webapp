import { type TableRow, schema as s } from 'jazz-tools';

/**
 * Defines the parent entity that the environment describes characteristics for.
 * - GARDEN: the environment applies to a garden.
 * - WORKSPACE: the environment applies to a workspace.
 * - PLANTING_AREA: the environment applies to a planting area.
 * - INDEPENDENT: the environment applies to an independent geometry.
 */
export const EnvironmentParentTypeEnumOptions = [
	'GARDEN',
	'WORKSPACE',
	'PLANTING_AREA',
	'INDEPENDENT'
] as const;

export const environmentSchema = {
	/** Environment schema. */
	environments: s.table({
		/** Non-unique name of the environment. */
		name: s.string(),

		/** Optional description. */
		description: s.string().default(''),

		/** Type of the parent entity of the environment. */
		parentType: s.enum(...EnvironmentParentTypeEnumOptions),

		/** Garden the environment exists in. Defined regardless of parentType. */
		gardenId: s.ref('gardens'),

		/** The workspaces the environment applies to. Defined only if parentType = 'WORKSPACE'. */
		workspaceIds: s.array(s.string()).optional(),

		/** The planting areas the environment applies to. Defined only if parentType = 'PLANTING_AREA'. */
		plantingAreaIds: s.array(s.string()).optional(),

		/** The geometry the environment applies to. Defined only if parentType = 'INDEPENDENT'. */
		geometryHistoryId: s.ref('geometryHistories').optional(),

		/** The locations the environment geometry exists at. Defined only if parentType = 'INDEPENDENT'. */
		locationHistoryId: s.ref('locationHistories').optional(),

		/**
		 * If true, the environment will inherit the attributes of the environments
		 * defined at higher levels.
		 */
		inherit: s.boolean().default(true),

		/** Environment attributes. Stored as JSON. */
		attributes: s.json().optional()
	})
};

export type Environment = TableRow<typeof environmentSchema, 'environments'>;
export type EnvironmentParent = (typeof EnvironmentParentTypeEnumOptions)[number];
