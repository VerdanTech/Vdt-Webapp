/** Schema. */
export declare const AnnualLifeCycleProfile: import('@triplit/client').RecordType<
	{
		sowToGerm: import('@triplit/client').TypeInterface<
			'number',
			{
				optional: true;
			}
		> &
			Omit<
				import('@triplit/client').NumberType<{}>,
				keyof import('@triplit/client').TypeInterface<string, {}>
			>;
		germToTransplant: import('@triplit/client').TypeInterface<
			'number',
			{
				optional: true;
			}
		> &
			Omit<
				import('@triplit/client').NumberType<{}>,
				keyof import('@triplit/client').TypeInterface<string, {}>
			>;
		germToFirstHarvest: import('@triplit/client').TypeInterface<
			'number',
			{
				optional: true;
			}
		> &
			Omit<
				import('@triplit/client').NumberType<{}>,
				keyof import('@triplit/client').TypeInterface<string, {}>
			>;
		firstToLastHarvest: import('@triplit/client').TypeInterface<
			'number',
			{
				optional: true;
			}
		> &
			Omit<
				import('@triplit/client').NumberType<{}>,
				keyof import('@triplit/client').TypeInterface<string, {}>
			>;
	},
	{}
>;
//# sourceMappingURL=schema.d.ts.map
