const verdagraphContext = getVerdagraphContext();
const calendarContext = createCalendarContext(verdagraphContext.timeline, [
	{ entityType: 'plants', items: () => [] },
	{
		entityType: 'plantingWindows',
		items: () => {
			return [
				{
					id: '1',
					label: 'Tomato',
					labelOnly: false,
					description: 'Garden - Planting Window',
					startDate: new CalendarDate(2025, 5, 10),
					endDate: new CalendarDate(2025, 12, 30),
					bottomMargin: 4,
					fillColor: getColor('tomato', 4, mode.current),
					borderColor: getColor('tomato', 7, mode.current),
					itemColor: getColor('tomato', 5, mode.current),
					infoPoints: [
						{
							label: 'this is really a mf label yes haha',
							date: new CalendarDate(2025, 8, 25),
							icon: iconIds.cultivarsIcon,
							popup: TestComponent
						},
						{ label: 'also a label', date: new CalendarDate(2025, 8, 18) }
					]
				},
				{
					id: '2',
					label: 'Lettuce',
					labelOnly: true,
					description: 'Planting Windows',
					startDate: new CalendarDate(2025, 5, 20),
					endDate: new CalendarDate(2025, 12, 30),
					bottomMargin: 4,
					bottomMarginChild: 0,
					fillColor: getColor('grass', 4, mode.current),
					borderColor: getColor('grass', 7, mode.current),
					itemColor: getColor('grass', 5, mode.current),
					children: [
						{
							id: '2a',
							label: 'Lettuce',
							labelOnly: false,
							description: 'Garden - Planting Window',
							startDate: new CalendarDate(2025, 5, 20),
							endDate: new CalendarDate(2025, 12, 28),
							bottomMargin: 0,
							fillColor: getColor('green', 4, mode.current),
							borderColor: getColor('green', 7, mode.current),
							itemColor: getColor('green', 5, mode.current)
						},
						{
							id: '2b',
							label: 'Lettuce',
							labelOnly: false,
							description: 'Environment 2 - Planting Window',
							startDate: new CalendarDate(2025, 2, 22),
							endDate: new CalendarDate(2025, 8, 30),
							bottomMargin: 2,
							fillColor: getColor('lime', 4, mode.current),
							borderColor: getColor('lime', 7, mode.current),
							itemColor: getColor('lime', 5, mode.current)
						}
					]
				},
				{
					id: '3',
					label: 'Beet',
					labelOnly: true,
					description: 'Garden - Planting Window',
					startDate: new CalendarDate(2025, 12, 5),
					endDate: new CalendarDate(2025, 12, 29),
					bottomMargin: 4,
					fillColor: getColor('purple', 4, mode.current),
					borderColor: getColor('purple', 7, mode.current),
					itemColor: getColor('purple', 5, mode.current)
				}
			];
		}
	},
	{ entityType: 'actions', items: () => [] }
]);
