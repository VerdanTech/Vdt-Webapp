
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
├─ makefile
├─ pyproject.toml
├─ requirements
│  ├─ dev.txt
│  ├─ main.txt
│  └─ test.txt
├─ src
│  └─ verdantech_api
│     ├─ domain
│     │  └─ users
│     │     ├─ __init__.py
│     │     ├─ controllers
│     │     │  ├─ __init__.py
│     │     │  ├─ auth.py
│     │     │  ├─ email_verification.py
│     │     │  ├─ password_reset.py
│     │     │  └─ users.py
│     │     ├─ dependencies.py
│     │     ├─ models.py
│     │     ├─ repos
│     │     │  ├─ email.py
│     │     │  ├─ email_confirmation.py
│     │     │  ├─ password_confirmation.py
│     │     │  └─ user.py
│     │     ├─ schemas.py
│     │     ├─ services
│     │     │  ├─ __init__.py
│     │     │  ├─ auth.py
│     │     │  ├─ email_verification.py
│     │     │  ├─ password_reset.py
│     │     │  └─ users.py
│     │     └─ urls.py
│     ├─ lib
│     │  ├─ crypt
│     │  │  ├─ __init__.py
│     │  │  ├─ generic.py
│     │  │  └─ passlib_crypt.py
│     │  ├─ email
│     │  │  ├─ __init__.py
│     │  │  ├─ aiosmtplib.py
│     │  │  ├─ generic.py
│     │  │  └─ litestar.py
│     │  ├─ utils.py
│     │  └─ validators
│     │     ├─ __init__.py
│     │     ├─ concrete
│     │     │  ├─ __init__.py
│     │     │  ├─ email.py
│     │     │  ├─ password.py
│     │     │  └─ username.py
│     │     └─ generic
│     │        ├─ __init__.py
│     │        ├─ errors.py
│     │        ├─ validations.py
│     │        └─ validators.py
│     ├─ main.py
│     ├─ settings
│     │  ├─ __init__.py
│     │  ├─ base.py
│     │  ├─ dev.py
│     │  └─ prod.py
│     └─ static
│        └─ email
│           ├─ email_verification.html
│           └─ password_reset.html
└─ tests
   ├─ __init__.py
   ├─ conftest.py
   └─ unit
      ├─ conftest.py
      ├─ domain
      │  └─ users
      │     └─ services_test.py
      └─ lib
         ├─ crypt
         │  ├─ __init__.py
         │  ├─ conftest.py
         │  └─ passlib_crypt_test.py
         └─ email
            ├─ __init__.py
            ├─ conftest.py
            └─ test_generic_async_client.py

```