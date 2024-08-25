export const cultivarFields = {
    last_frost_window_open: {
        min: {
            value: -200,
            message: 'Must be greater than -200',
        },
        max: {
            value: 200,
            message: 'Must be less than 200',
        },
        description: 'The amount of days between the last frost and the beginning of the planting window. Positive values indicate the window begins after the last frost date. For example, a value of -15 indicates the cultivar may be planted 15 days before the last frost date. Must be between -200 and -200 days.',
        label: 'Last Frost Window - Open',
        unit: 'days',
    },
    frost_date_planting_window_profile: {
        description: 'A planting window defines a period of time within an environment that a cultivar should be planted. These attributes define an allowed planting window of time relative to the first and last frost dates.',
        label: 'Frost Date Planting Window Profile',
    },
}
export default cultivarFields