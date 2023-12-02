#
# Compile all dependencies specified in pyproject.toml into requirements.
#
.PHONY: push-depedencies
push-depedencies:
	pip-compile --resolver backtracking -o requirements/main.txt pyproject.toml
	pip-compile --extra test --resolver backtracking -o requirements/test.txt pyproject.toml
	pip-compile --extra test --extra dev --resolver backtracking -o requirements/dev.txt pyproject.toml

.PHONY: test
test:
	coverage run --source tests -m pytest -m unit --html=reports/pytest/index.html
	coverage html -d reports/coverage