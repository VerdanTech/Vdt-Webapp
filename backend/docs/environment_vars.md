# Environment Variables

The environment configuration for the default development environment is contained in `.env-default`. During the build process of the default development environment, this file is copied to create a `.env` file that is accessed by python and other scripts.

The Python package [decouple](https://pypi.org/project/python-decouple/) is used to access environment variables within the application. This typically happens in the settings files.


| Name | Type | Description | Default |
| -------- | ------- | ------- | ------- |
| ENVIRONMENT | str (enum) | Controls whether the application is run with its development, test, or production settings. Must be one of `"DEV"`, `"TEST"`, or `"PROD"`. | `"DEV"` |
| USING_HTTPS | bool | Tracks whether HTTPS is in use | `False` |
| CLIENT_SAMESITE | bool | If true, all clients connecting to the API must be on the same domain. | `False` |
| CLIENT_DOMAIN | str | Domain name of the frontend. Used to construct links for emails.  | `verdantech.io` |
| ALLOWED_HOSTS | str or list[str] | Allowed hosts of the Litestar application.  | `.localhost` |
| ALLOWED_ORIGINS | str or list[str] | Allowed origins (CORS) of the Litestar application.  | `""` |
| JWT_SECRET | str | Secret key for generating the short lived access JWT authentication token.  | `developmentsecret123` |
| JWT_SECRET | str | Secret key for generating the long lived refresh JWT authentication token.  | `developmentsecret456` |
| POSTGRES_DB_URI | str | URI of the postgres database | `postgresql+asyncpg://verdantech_db:xkrytusefhrerifuthrh@postgres:5432/dev_db` |
