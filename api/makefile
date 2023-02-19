PY = python3
VENV = venv
BIN=$(VENV)/bin

.PHONY: init-venv
init-venv:
	sudo apt install python3 && sudo apt install python3-pip && sudo apt install python3-venv
	$(PY) -m venv $(VENV)
	$(BIN)/$(PY) -m pip install --upgrade pip pip-tools wheel

.PHONY: sync-dependencies
sync-dependencies:
	$(BIN)/$(PY) -m pip install --upgrade pip pip-tools wheel
	$(BIN)/$(PY) -m piptools sync requirements/main.txt requirements/dev.txt
	$(BIN)/$(PY) -m pip check

.PHONY: upgrade-dependencies
upgrade-dependencies:
	$(BIN)/$(PY) -m pip install --upgrade pip pip-tools wheel
	$(BIN)/$(PY) -m piptools compile --upgrade --resolver backtracking -o requirements/main.txt pyproject.toml
	$(BIN)/$(PY) -m piptools compile --extra test --upgrade --resolver backtracking -o requirements/test.txt pyproject.toml
	$(BIN)/$(PY) -m piptools compile --extra test --extra dev --upgrade --resolver backtracking -o requirements/dev.txt pyproject.toml

.PHONY: update-dependencies
update-dependencies:
	$(BIN)/$(PY) -m piptools compile --resolver backtracking -o requirements/main.txt pyproject.toml
	$(BIN)/$(PY) -m piptools compile --extra test --resolver backtracking -o requirements/test.txt pyproject.toml
	$(BIN)/$(PY) -m piptools compile --extra test --extra dev --resolver backtracking -o requirements/dev.txt pyproject.toml

.PHONY: clean
clean:
	rm -rf autogmo_api.egg-info/
	rm -rf reports/
	rm .coverage

.PHONY: upgrade
upgrade: upgrade-dependencies sync-dependencies clean

.PHONY: update
update: update-dependencies sync-dependencies clean

.PHONY: build
build: init-venv sync-dependencies

.PHONY: run
run:
	$(BIN)/$(PY) autogmo_api/manage.py runserver --settings=autogmo_api.settings.development

.PHONY: lint
lint:
	$(BIN)/flakeheaven lint ./autogmo_api

.PHONY: format
format:
	$(BIN)/isort .
	$(BIN)/black autogmo_api

.PHONY: test
test:
	$(BIN)/$(PY) -m coverage run --source autogmo_api -m pytest --html=reports/pytest/index.html
	$(BIN)/$(PY) -m coverage html -d reports/coverage

.PHONY: migrate
migrate:
	$(BIN)/$(PY) autogmo_api/manage.py migrate

.PHONY: schema
schema:
	$(BIN)/$(PY) autogmo_api/manage.py spectacular --color --validate --file schema.yml
