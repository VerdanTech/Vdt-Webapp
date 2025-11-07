/** Schema. */
export declare const FrostDatePlantingWindowsProfile: import('@triplit/client').RecordType<
	{
		lastFrostWindowOpen: import('@triplit/client').TypeInterface<
			'number',
			{
				optional: true;
			}
		> &
			Omit<
				import('@triplit/client').NumberType<{}>,
				keyof import('@triplit/client').TypeInterface<string, {}>
			>;
		lastFrostWindowClose: import('@triplit/client').TypeInterface<
			'number',
			{
				optional: true;
			}
		> &
			Omit<
				import('@triplit/client').NumberType<{}>,
				keyof import('@triplit/client').TypeInterface<string, {}>
			>;
		firstFrostWindowOpen: import('@triplit/client').TypeInterface<
			'number',
			{
				optional: true;
			}
		> &
			Omit<
				import('@triplit/client').NumberType<{}>,
				keyof import('@triplit/client').TypeInterface<string, {}>
			>;
		firstFrostWindowClose: import('@triplit/client').TypeInterface<
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
