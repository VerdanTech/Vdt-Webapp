# Python version
PY-VER=python3.12
# Virtual environment directory
VENV=.venv
# Python bin directory
BIN=$(VENV)/bin
# Python interpreter directory
PY=$(BIN)/$(PY-VER)
# Provided environment variable defaults directory
ENV-VARS-DEFAULT=.env-default
# Environment variables directory
ENV-VARS=.env
# Dependency lockfile directory
LOCKFILE=requirements/.pdm-lockfile

#
# If an environment variable file does not already exist,
# create one by copying over the development defaults
#
.PHONY: setup-env-vars
setup-env-vars:
	@if [ ! -f $(ENV-VARS) ]; then \
		cp $(ENV-VARS-DEFAULT) $(ENV-VARS); \
		echo "Copied $(ENV-VARS-DEFAULT) to $(ENV-VARS)"; \
	fi

#
# Install required python version and all python application depedencies
#
.PHONY: init-app
init-app: setup-env-vars
	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt-get update && sudo apt-get upgrade
	sudo apt-get install $(PY-VER) && sudo apt-get install python3.12-dev && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12
	$(PY) -m pip install pdm
	$(PY) -m pdm sync --clean --lockfile $(LOCKFILE)

#
# Install, start and configure postgreql server with database
# configuration values set in environment variable
#
.PHONY: init-db
init-db: setup-env-vars
	$(eval POSTGRES_DB_NAME=$(shell grep 'POSTGRES_DB_NAME=' $(ENV-VARS) | sed 's/POSTGRES_DB_NAME=//'))
	$(eval POSTGRES_DB_USER=$(shell grep 'POSTGRES_DB_USER=' $(ENV-VARS) | sed 's/POSTGRES_DB_USER=//'))
	$(eval POSTGRES_DB_PASSWORD=$(shell grep 'POSTGRES_DB_PASSWORD=' $(ENV-VARS) | sed 's/POSTGRES_DB_PASSWORD=//'))
	chmod +x ./scripts/postgres/install.sh
	sudo ./scripts/postgres/install.sh
	chmod +x ./scripts/postgres/start.sh
	sudo ./scripts/postgres/start.sh
	chmod +x ./scripts/postgres/create_db.sh
	sudo ./scripts/postgres/create_db.sh $(POSTGRES_DB_NAME) $(POSTGRES_DB_USER) $(POSTGRES_DB_PASSWORD)

.PHONY: build
init-app: init-app init-db

.PHONY: update
update: 
	$(PY-VER) -m pdm update --lockfile requirements/.pdm-lock

.PHONY: clean
clean:
	rm -rf reports/
	rm .coverage
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

.PHONY: run
run:
	$(BIN)/litestar --app src.verdantech_api.api.litestar.app:create_app run --reload

.PHONY: migrations
migrations:
	export PYTHONPATH=$(shell pwd); \
	$(PY) src/verdantech_api/infrastructure/persistence/migrations/create.py -m "$(filter-out $@,$(MAKECMDGOALS))"

.PHONY: migrate
migrate:
	export PYTHONPATH=$(shell pwd); \
	$(PY) src/verdantech_api/infrastructure/persistence/migrations/apply.py

.PHONY: reset-migrations
reset-migrations:
	export PYTHONPATH=$(shell pwd); \
	$(PY) src/verdantech_api/infrastructure/persistence/migrations/reset.py --reset

.PHONY: schema
schema:
	$(BIN)/litestar openapi schema --output schema.yaml

.PHONY: lint
lint:
	$(BIN)/ruff check ./src/verdantech_api
	$(BIN)/ruff check ./tests

.PHONY: format
format:
	$(BIN)/isort ./src
	$(BIN)/isort ./tests
	$(BIN)/black src
	$(BIN)/black tests

.PHONY: test
test:
	$(PY) -m coverage run --source tests -m pytest --html=reports/pytest/index.html
	$(PY) -m coverage html -d reports/coverage

.PHONY: test-unit
test-unit:
	$(PY) -m coverage run --source tests/unit -m pytest

.PHONY: test-int
test-int:
	$(PY) -m coverage run --source tests/integration -m pytest

.PHONY: docs
docs:
	$(BIN)/mkdocs serve