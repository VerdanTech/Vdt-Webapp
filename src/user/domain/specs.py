from src.common.adapters.utils.specs import spec_manager

specs = {
    "user": {
    "username": {
        "min_length": {
            "spec": 3,
            "description": "Must be at least {min_length} characters",
        },
        "max_length": {
            "spec": 50,
            "description": "Must be at most {max_length} characters",
        },
        "pattern": {
            "spec": r"^[a-zA-Z0-9_]*$",
            "description": "Must contain only alphanumeric characters and underscores",
        },
        "description" : "Must be between {min_length} and {max_length} characters long and contain only alphanumeric characters and underscores. Must be unique.",
    },
    "password": {
        "min_length": {
            "spec": 6,
            "description": "Must be at least {min_length} characters",
        },
        "max_length": {
            "spec": 255,
            "description": "Must be at most {max_length} characters",
        },
        "pattern": {
            "spec": r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*\W).*$",
            "description": "Must contain at least one lowercase letter, one uppercase letter, one digit, and one special character",
        },
        "description" : "Must be between {min_length} and {max_length} characters long and contain at least one lowercase letter, one uppercase letter, one digit, and one special character",
    }, }
}