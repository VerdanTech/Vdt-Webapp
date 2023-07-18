
## Makefile commands

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

## Environment variables

SECRET_KEY: `str`, `default="django-insecure-n=r5mq#q09@3v_#x$ijj=l)(5aix3tav%!%_e9qrynsz=7+9ob"`

DEBUG: `bool`, `default="True"`

ALLOWED_HOSTS: `[str]`, `default=["127.0.0.1"]`

DATABASE_URL: `django_db_url`

API_URL_BASE: `str`, `default="api/"`

USING_HTTPS: `bool`, `default=True`

DOMAIN_NAME: `str`, `"default="verdantech.io"`

CLIENT_EMAIL_VERIFY_URL_POSTFIX: `str`, `default="register/verify/"`

CLIENT_PASSWORD_RESET_URL_POSTFIX: `str`, `default="password/reset/"`

## To implement

Periodic tasks:
delete user models with unverified emails that don't have a confirmation

```
api
├─ .gitignore
├─ README.md
├─ docs
│  ├─ architecture
│  │  └─ architecture.md
│  ├─ contributing.md
│  ├─ goals.md
│  └─ index.md
├─ makefile
├─ mkdocs.yml
├─ pyproject.toml
├─ requirements
│  ├─ dev.txt
│  ├─ main.txt
│  └─ test.txt
├─ src
│  ├─ verdantech_api
│  │  ├─ api
│  │  │  ├─ app.py
│  │  │  ├─ garden
│  │  │  ├─ plants
│  │  │  ├─ urls.py
│  │  │  ├─ user
│  │  │  │  ├─ __init__.py
│  │  │  │  ├─ controllers
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ auth.py
│  │  │  │  │  ├─ read.py
│  │  │  │  │  ├─ verification.py
│  │  │  │  │  └─ write.py
│  │  │  │  ├─ schema.py
│  │  │  │  └─ urls.py
│  │  │  └─ workspace
│  │  ├─ application
│  │  ├─ domain
│  │  │  ├─ __init__.py
│  │  │  ├─ common
│  │  │  │  ├─ __init__.py
│  │  │  │  ├─ entities.py
│  │  │  │  └─ values.py
│  │  │  ├─ garden
│  │  │  │  ├─ __init__.py
│  │  │  │  ├─ entities.py
│  │  │  │  └─ values.py
│  │  │  ├─ planner
│  │  │  │  ├─ __init__.py
│  │  │  │  ├─ entities.py
│  │  │  │  └─ values.py
│  │  │  ├─ plants
│  │  │  │  ├─ __init__.py
│  │  │  │  ├─ entities.py
│  │  │  │  └─ values.py
│  │  │  ├─ user
│  │  │  │  ├─ __init__.py
│  │  │  │  ├─ entities.py
│  │  │  │  ├─ services.py
│  │  │  │  └─ values.py
│  │  │  └─ workspace
│  │  │     ├─ __init__.py
│  │  │     ├─ entities.py
│  │  │     └─ values.py
│  │  └─ interfaces
│  │     └─ crypt
│  │        ├─ __init__.py
│  │        ├─ abstract.py
│  │        └─ passlib.py
│  └─
```