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
    last_frost_window_close: {
        min: {
            value: -200,
            message: 'Must be greater than -200',
        },
        max: {
            value: 200,
            message: 'Must be less than 200',
        },
        description: 'The amount of days between the last frost and the end of the planting window. Positive values indicate the window begins after the last frost date. For example, a value of 15 indicates the cultivar must be planted before 15 days after the last frost date. Must be between -200 and -200 days.',
        label: 'Last Frost Window - Close',
        unit: 'days',
    },
    first_frost_window_open: {
        min: {
            value: -200,
            message: 'Must be greater than -200',
        },
        max: {
            value: 200,
            message: 'Must be less than 200',
        },
        description: 'The amount of days between the first frost and the beginning of the planting window. Positive values indicate the window begins after the first frost date. For example, a value of -15 indicates the cultivar may be planted 15 days before the first frost date. Must be between -200 and -200 days.',
        label: 'First Frost Window - Open',
        unit: 'days',
    },
    first_frost_window_close: {
        min: {
            value: -200,
            message: 'Must be greater than -200',
        },
        max: {
            value: 200,
            message: 'Must be less than 200',
        },
        description: 'The amount of days between the first frost and the end of the planting window. Positive values indicate the window begins after the first frost date. For example, a value of 15 indicates the cultivar must be planted before 15 days after the first frost date. Must be between -200 and -200 days.',
        label: 'First Frost Window - Close',
        unit: 'days',
    },
    frost_date_planting_window_profile: {
        description: 'A planting window defines a period of time within an environment that a cultivar should be planted. These attributes define an allowed planting window of time relative to the first and last frost dates. These planting windows are used for incdicating within the Verdagraph when plants are suggested to be planted.',
        label: 'Frost Date Planting Windows',
    },
    origin_profile: {
        description: 'The origin refers to the method used to create plants. ',
        label: 'Origin Profile',
    },
    allowed_origins: {
        description: 'A cultivar may be allowed to start in any combination of origins. In general, plants may be started from seed and transplanted to where they reach maturity, started from seed in the location they reach maturity, or brought in as seedlings. Some plants, such as carrots, don\'t tolerate transplants, and so must be started directly.',
        label: 'Allowed Origins',
    },
}
export default cultivarFields