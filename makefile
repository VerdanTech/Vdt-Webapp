#
# Compile all dependencies specified in pyproject.toml into requirements.
#
.PHONY: compile-dependencies
compile-deps:
	uv pip compile pyproject.toml -o requirements/main.txt
	uv pip compile --extra test pyproject.toml -o requirements/test.txt
	uv pip compile --extra test --extra dev pyproject.toml -o requirements/dev.txt 

#
# Install all dependencies frozen in requirements/dev.txt.
#
.PHONY: sync-deps
sync-deps:
	uv pip sync --system requirements/dev.txt

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
# Run all database tests.
#
.PHONY: test-db
test-db:
	pytest -m databases

#
# Run all application integration tests.
#
.PHONY: test-asgi
test-asgi:
	pytest -m asgi


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
	black src
	black tests

#
# Lint check all source and test code.
#
.PHONY: lint
lint:
	ruff check ./src
	ruff check ./tests
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
	python3 -m litestar --app src.common.entrypoints.litestar.app:create_app schema openapi --output schema.yaml

# python3.12 ./src/asgi/litestar/patch_openapi.py

#
# Run the backend server with uvicorn.
#
.PHONY: run
run:
	litestar --app src.common.entrypoints.litestar.app:create_app run -d

#
# Run Alembic's "revision" command to create database migrations from the current sqlalchemy metadata.
#
.PHONY: migrations
migrations:
	export PYTHONPATH=$(shell pwd); \
	python src/common/adapters/persistence/sqlalchemy/migrations/create.py -m "$(filter-out $@,$(MAKECMDGOALS))"

#
# Run Alembic's "upgrade" command to apply migrations to the database.
#
.PHONY: migrate
migrate:
	export PYTHONPATH=$(shell pwd); \
	python src/common/adapters/persistence/sqlalchemy/migrations/apply.py

#
# Run Alembic's "downgrade" command to un-apply all migrations.
#
.PHONY: reset-migrations
reset-migrations:
	export PYTHONPATH=$(shell pwd); \
	python src/common/adapters/persistence/sqlalchemy/migrations/reset.py --reset