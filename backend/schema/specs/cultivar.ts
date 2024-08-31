export const cultivarFields = {
    cultivar_name: {
        min_length: {
            value: 3,
            message: 'Must be at least 3 characters',
        },
        max_length: {
            value: 30,
            message: 'Must be at most 30 characters',
        },
        pattern: {
            value: /[0-9A-Za-z _-]+/,
            message: 'Must contain only alphanumeric characters, spaces, hyphens, and underscores',
        },
        description: 'A common name of this plant species. Must be between 3 and 30 characters long and contain only alphanumeric characters, spaces, hyphens, and underscores.',
    },
    cultivar_names: {
        max_length: {
            value: 10,
            message: 'Must contain at most 10 names',
        },
        description: 'A set of common names associated with this plant species. Each name must be between 3 and 30 characters long and contain only alphanumeric characters and spaces.There may be a maximumm of 10 names',
    },
    cultivar_key: {
        min_length: {
            value: 1,
            message: 'Must be at least 1 characters',
        },
        max_length: {
            value: 6,
            message: 'Must be at most 6 characters',
        },
        pattern: {
            value: /[0-9A-Za-z]+/,
            message: 'Must contain only alphanumeric characters',
        },
        description: 'A very short abbreviation for this plant species.Must be between 1 and 6 characters long and contain only alphanumeric characters.',
    },
    cultivar_scientific_name: {
        max_length: {
            value: 60,
            message: 'Must be at most 60 characters',
        },
        description: 'The scientific name of this plant species.Must be at most 60 characters',
    },
    cultivar_description: {
        max_length: {
            value: 1400,
            message: 'Must be at most 1400 characters',
        },
        description: 'A description of this plant species.Must be at most 1400 characters',
    },
    cultivar_collection_name: {
        min_length: {
            value: 3,
            message: 'Must be at least 3 characters',
        },
        max_length: {
            value: 50,
            message: 'Must be at most 50 characters',
        },
        pattern: {
            value: /[0-9A-Za-z _-]+/,
            message: 'Must contain only alphanumeric characters, spaces, hyphens, and underscores',
        },
        description: 'The name of the collection.Must be between 3 and 50 characters long and contain only alphanumeric characters, spaces, hyphens, and underscores.',
    },
    cultivar_collection_description: {
        max_length: {
            value: 1400,
            message: 'Must be at most 1400 characters',
        },
        description: 'The description of the collection.Must be at most 1400 characters',
    },
    cultivar_collection_tag: {
        max_length: {
            value: 150,
            message: 'Must be at most 150 characters',
        },
        pattern: {
            value: /[0-9A-Za-z ]+/,
            message: 'Must contain only alphanumeric characters and spaces',
        },
        description: 'A metadata tag.Must be at most 150 characters and contain only alphanumeric characters and spaces',
    },
    cultivar_collection_tags: {
        max_length: {
            value: 150,
            message: 'Must contain at most 150 tags',
        },
        description: 'A set of metadata tags.Each tag must be at most 150 characters and contain only alphanumeric characters and spaces. There may be at most 150 tags',
    },
    last_frost_window_open: {
        min: {
            value: -200,
            message: 'Must be greater than -200',
        },
        max: {
            value: 200,
            message: 'Must be less than 200',
        },
        description: 'The amount of days between the last frost and the beginning of the planting window. Positive values indicate the window begins after the last frost date. For example, a value of -15 indicates the cultivar may be planted 15 days before the last frost date. Must be between -200 and 200 days.',
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
        description: 'The amount of days between the last frost and the end of the planting window. Positive values indicate the window begins after the last frost date. For example, a value of 15 indicates the cultivar must be planted before 15 days after the last frost date. Must be between -200 and 200 days.',
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
        description: 'The amount of days between the first frost and the beginning of the planting window. Positive values indicate the window begins after the first frost date. For example, a value of -15 indicates the cultivar may be planted 15 days before the first frost date. Must be between -200 and 200 days.',
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
        description: 'The amount of days between the first frost and the end of the planting window. Positive values indicate the window begins after the first frost date. For example, a value of 15 indicates the cultivar must be planted before 15 days after the first frost date. Must be between -200 and 200 days.',
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