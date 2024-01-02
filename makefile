#
# Compile all dependencies specified in pyproject.toml into requirements.
#
.PHONY: compile-dependencies
compile-dependencies:
	pip-compile --resolver backtracking -o requirements/main.txt pyproject.toml
	pip-compile --extra test --resolver backtracking -o requirements/test.txt pyproject.toml
	pip-compile --extra test --extra dev --resolver backtracking -o requirements/dev.txt pyproject.toml

#
# Install all dependencies frozen in requirements/dev.txt.
#
.PHONY: sync-dependencies
sync-dependencies:
	pip-sync requirements/dev.txt

#
# Run all tests.
#
.PHONY: test
test:
	pytest

#
# Run all unit tests.
#
.PHONY: test-unit
test-unit:
	pytest -m unit

#
# Run all integration tests.
#
.PHONY: test-integration
test-intg:
	pytest -m integration

#
# Run all database tests.
#
.PHONY: test-db
test-db:
	pytest -m databases

#
# Run all tests and generate a coverage report.
#
.PHONY: test-cov
test-cov:
	coverage run --source tests -m pytest --html=reports/pytest/index.html
	coverage html -d reports/coverage

#
# Sort imports and format all source and test code.
#
.PHONY: format
format:
	isort ./src
	isort ./tests
	isort ./mocks
	black src
	black tests
	black mocks

#
# Lint check all source and test code.
#
.PHONY: lint
lint:
	ruff check ./src
	ruff check ./tests
	ruff check ./mocks
	pyright ./src

#
# Spin up documentation server.
#
.PHONY: docs
docs:
	mkdocs serve

#
# Output current backend routes into openapi schema.
#
.PHONY: schema
schema:
	litestar --app src.asgi.litestar.app:create_app schema openapi --output schema.yaml

#
# Run the backend server with uvicorn.
#
.PHONY: run
run:
	litestar --app src.asgi.litestar.app:create_app run -d

#
# Run Alembic's "revision" command to create database migrations from the current sqlalchemy metadata.
#
.PHONY: migrations
migrations:
	export PYTHONPATH=$(shell pwd); \
	python src/infra/persistence/sqlalchemy/migrations/create.py -m "$(filter-out $@,$(MAKECMDGOALS))"

#
# Run Alembic's "upgrade" command to apply migrations to the database.
#
.PHONY: migrate
migrate:
	export PYTHONPATH=$(shell pwd); \
	python src/infra/persistence/sqlalchemy/migrations/apply.py

#
# Run Alembic's "downgrade" command to un-apply all migrations.
#
.PHONY: reset-migrations
reset-migrations:
	export PYTHONPATH=$(shell pwd); \
	python src/infra/persistence/sqlalchemy/migrations/reset.py --reset