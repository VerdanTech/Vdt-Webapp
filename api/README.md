`make build`
Install python, initialize the virtual environment, and install all development dependencies

`make update`
Based on the dependendies listed in pyproject.toml, update the requirements files

`make upgrade`
Based on the dependencies listed in pyproject.toml, update the requirements files, and upgrade packagese to their newest versions

`make run`
Runs the server with the development settings

`make lint`
Lints files using flakeheaven

`make format`
Formats files using isort and black

`make test`
Runs pytest, outputting a report to reports/pytest, and coverage, outputting a report to report/coverage

`make up`
Runs format, lint, and test
