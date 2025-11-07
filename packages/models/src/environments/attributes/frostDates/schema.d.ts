/** Schema. */
export declare const FrostDateProfile: import('@triplit/client').RecordType<
	{
		lastFrostDate: import('@triplit/client').TypeInterface<
			'date',
			{
				optional: true;
			}
		> &
			Omit<
				import('@triplit/client').DateType<{}>,
				keyof import('@triplit/client').TypeInterface<string, {}>
			>;
		firstFrostDate: import('@triplit/client').TypeInterface<
			'date',
			{
				optional: true;
			}
		> &
			Omit<
				import('@triplit/client').DateType<{}>,
				keyof import('@triplit/client').TypeInterface<string, {}>
			>;
	},
	{}
>;
//# sourceMappingURL=schema.d.ts.map
