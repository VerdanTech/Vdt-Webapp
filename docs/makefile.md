# Makefile

A makefile is used for standardizing development commands and providing an easy development CLI. To run a command, type `make <command>` with the command of choice into the terminal.  

| Name | Description |
| -------- | ------- |
| `compile-deps` | Compiles all dependencies specified in pyproject.toml into the requirements folder. Dependencies are grouped into production (main), test (main + whatever is needed for testing, such as pytest), and dev (test + whatever is needed for development, such as linting) |
| `sync-deps` | Installs all development depencies specified in requirements/dev.txt into the development environment. |
| `test` | Runs all tests. |
| `test-unit` | Runs all unit tests (marked with `pytest.mark.unit`). |
| `test-db` | Runs all tests of database functionality (marked with `pytest.mark.databases`) |
| `test-intg` | Runs all API integration tests (marked with `pytest.mark.integration`) |
| `test-cod` | Runs all tests, and outputs a code coverage report to reports/coverage. |
| `format` | Runs the isort tool (sorts and categorizes imports) and the black formatter (general formatting). |
| `lint` | Runs the ruff and pyright tools. |
| `docs` | Spins up the documentation server. |
| `schema` | Converts the currently configured Litestar application into its equivalent OpenAPI schema, written to schema.yaml |
| `run` | Runs the Litestar server. |
| `migrations` | Uses Alembic to generate sql migrations. |
| `migrate` | Applies the generated migrations/database schema to the database. |




