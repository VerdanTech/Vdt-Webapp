/** Schema. */
export declare const AnnualTemperatureProfile: import('@triplit/client').RecordType<
	{
		minimum: import('@triplit/client').TypeInterface<
			'number',
			{
				optional: true;
			}
		> &
			Omit<
				import('@triplit/client').NumberType<{}>,
				keyof import('@triplit/client').TypeInterface<string, {}>
			>;
		maximum: import('@triplit/client').TypeInterface<
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
