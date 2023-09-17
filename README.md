# VerdanTech

This is the home repository for the VerdanTech web application - an application striving towards creating software tools to automate gardening in a collaborative way - including planning, tracking, optimizing, and automating growing plants. This project is still in its early stages and lacks documentation. You can see the previous version of this project (here)[https://github.com/nathanielarking/Autonomous-Agriculture].

In terms of infrastructure, the project aims to create a REST api using Django Rest Framework, and a frontend Svelte SPA.

Eventually, the application will be integrated with embedded automation projects. Those have a seperate repository, which you can find (here)[https://github.com/nathanielarking/VerdanTech-Devices/tree/main/VerdanTech%20Drip%20-%20Irrigation%20Controller]
```
VerdanTech
├─ .vscode
│  └─ extensions.json
├─ LICENSE
├─ README.md
├─ api
│  ├─ .coverage
│  ├─ .pytest_cache
│  │  ├─ CACHEDIR.TAG
│  │  ├─ README.md
│  │  └─ v
│  │     └─ cache
│  │        ├─ lastfailed
│  │        ├─ nodeids
│  │        └─ stepwise
│  ├─ README.md
│  ├─ makefile
│  ├─ pyproject.toml
│  ├─ reports
│  │  └─ pytest
│  │     ├─ assets
│  │     │  └─ style.css
│  │     └─ index.html
│  ├─ requirements
│  │  ├─ dev.txt
│  │  ├─ main.txt
│  │  └─ test.txt
│  ├─ src
│  │  └─ verdantech_api
│  │     ├─ domain
│  │     │  └─ users
│  │     │     ├─ __init__.py
│  │     │     ├─ controllers
│  │     │     │  ├─ __init__.py
│  │     │     │  ├─ auth.py
│  │     │     │  ├─ email_verification.py
│  │     │     │  ├─ password_reset.py
│  │     │     │  └─ users.py
│  │     │     ├─ dependencies.py
│  │     │     ├─ models.py
│  │     │     ├─ repos
│  │     │     │  ├─ email.py
│  │     │     │  ├─ email_confirmation.py
│  │     │     │  ├─ password_confirmation.py
│  │     │     │  └─ user.py
│  │     │     ├─ schemas.py
│  │     │     ├─ services
│  │     │     │  ├─ __init__.py
│  │     │     │  ├─ auth.py
│  │     │     │  ├─ email_verification.py
│  │     │     │  ├─ password_reset.py
│  │     │     │  └─ users.py
│  │     │     └─ urls.py
│  │     ├─ lib
│  │     │  ├─ crypt
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __pycache__
│  │     │  │  │  └─ __init__.cpython-310.pyc
│  │     │  │  ├─ generic.py
│  │     │  │  └─ passlib_crypt.py
│  │     │  ├─ email
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ aiosmtplib.py
│  │     │  │  ├─ generic.py
│  │     │  │  └─ litestar.py
│  │     │  ├─ utils.py
│  │     │  └─ validators
│  │     │     ├─ __init__.py
│  │     │     ├─ concrete
│  │     │     │  ├─ __init__.py
│  │     │     │  ├─ email.py
│  │     │     │  ├─ password.py
│  │     │     │  └─ username.py
│  │     │     └─ generic
│  │     │        ├─ __init__.py
│  │     │        ├─ errors.py
│  │     │        ├─ validations.py
│  │     │        └─ validators.py
│  │     ├─ main.py
│  │     ├─ settings
│  │     │  ├─ __init__.py
│  │     │  ├─ base.py
│  │     │  ├─ dev.py
│  │     │  └─ prod.py
│  │     └─ static
│  │        └─ email
│  │           ├─ email_verification.html
│  │           └─ password_reset.html
│  ├─ tests
│  │  ├─ __init__.py
│  │  ├─ __pycache__
│  │  │  └─ __init__.cpython-310-pytest-7.4.0.pyc
│  │  └─ unit
│  │     ├─ domain
│  │     │  └─ users
│  │     │     ├─ __pycache__
│  │     │     │  └─ services_test.cpython-310-pytest-7.4.0.pyc
│  │     │     └─ services_test.py
│  │     └─ lib
│  │        └─ crypt
│  │           ├─ __init__.py
│  │           ├─ __pycache__
│  │           │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│  │           │  └─ conftest.cpython-310-pytest-7.4.0.pyc
│  │           ├─ conftest.py
│  │           └─ test_passlib_crypt.py
│  └─ venv
│     ├─ bin
│     │  ├─ Activate.ps1
│     │  ├─ activate
│     │  ├─ activate.csh
│     │  ├─ activate.fish
│     │  ├─ alembic
│     │  ├─ black
│     │  ├─ blackd
│     │  ├─ coverage
│     │  ├─ coverage-3.10
│     │  ├─ coverage3
│     │  ├─ dotenv
│     │  ├─ editorconfig
│     │  ├─ email_validator
│     │  ├─ faker
│     │  ├─ html2text
│     │  ├─ httpx
│     │  ├─ isort
│     │  ├─ isort-identify-imports
│     │  ├─ js-beautify
│     │  ├─ litestar
│     │  ├─ mako-render
│     │  ├─ markdown-it
│     │  ├─ pip
│     │  ├─ pip-compile
│     │  ├─ pip-sync
│     │  ├─ pip3
│     │  ├─ pip3.10
│     │  ├─ py.test
│     │  ├─ pygmentize
│     │  ├─ pyproject-build
│     │  ├─ pytest
│     │  ├─ python
│     │  ├─ python3
│     │  ├─ python3.10
│     │  ├─ rich-click
│     │  ├─ ruff
│     │  ├─ uvicorn
│     │  ├─ validate-pyproject
│     │  ├─ watchfiles
│     │  └─ wheel
│     ├─ include
│     │  └─ site
│     │     └─ python3.10
│     │        └─ greenlet
│     │           └─ greenlet.h
│     ├─ lib
│     │  └─ python3.10
│     │     └─ site-packages
│     │        ├─ 2ec0e72aa72355e6eccf__mypyc.cpython-310-x86_64-linux-gnu.so
│     │        ├─ EditorConfig-0.12.3.dist-info
│     │        │  ├─ COPYING
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.BSD
│     │        │  ├─ LICENSE.PSF
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ Faker-18.11.2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.txt
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  ├─ top_level.txt
│     │        │  └─ zip-safe
│     │        ├─ Mako-1.2.4.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ MarkupSafe-2.1.3.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.rst
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ PyYAML-6.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ Pygments-2.15.1.dist-info
│     │        │  ├─ AUTHORS
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ SQLAlchemy-2.0.17.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ __pycache__
│     │        │  ├─ _black_version.cpython-310.pyc
│     │        │  ├─ decouple.cpython-310.pyc
│     │        │  ├─ mypy_extensions.cpython-310.pyc
│     │        │  ├─ py.cpython-310.pyc
│     │        │  ├─ six.cpython-310.pyc
│     │        │  └─ typing_extensions.cpython-310.pyc
│     │        ├─ _argon2_cffi_bindings
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  └─ _ffi_build.cpython-310.pyc
│     │        │  ├─ _ffi.abi3.so
│     │        │  └─ _ffi_build.py
│     │        ├─ _black_version.py
│     │        ├─ _cffi_backend.cpython-310-x86_64-linux-gnu.so
│     │        ├─ _distutils_hack
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  └─ override.cpython-310.pyc
│     │        │  └─ override.py
│     │        ├─ _pytest
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _argcomplete.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  ├─ cacheprovider.cpython-310.pyc
│     │        │  │  ├─ capture.cpython-310.pyc
│     │        │  │  ├─ compat.cpython-310.pyc
│     │        │  │  ├─ debugging.cpython-310.pyc
│     │        │  │  ├─ deprecated.cpython-310.pyc
│     │        │  │  ├─ doctest.cpython-310.pyc
│     │        │  │  ├─ faulthandler.cpython-310.pyc
│     │        │  │  ├─ fixtures.cpython-310.pyc
│     │        │  │  ├─ freeze_support.cpython-310.pyc
│     │        │  │  ├─ helpconfig.cpython-310.pyc
│     │        │  │  ├─ junitxml.cpython-310.pyc
│     │        │  │  ├─ legacypath.cpython-310.pyc
│     │        │  │  ├─ logging.cpython-310.pyc
│     │        │  │  ├─ main.cpython-310.pyc
│     │        │  │  ├─ monkeypatch.cpython-310.pyc
│     │        │  │  ├─ nodes.cpython-310.pyc
│     │        │  │  ├─ nose.cpython-310.pyc
│     │        │  │  ├─ outcomes.cpython-310.pyc
│     │        │  │  ├─ pastebin.cpython-310.pyc
│     │        │  │  ├─ pathlib.cpython-310.pyc
│     │        │  │  ├─ pytester.cpython-310.pyc
│     │        │  │  ├─ pytester_assertions.cpython-310.pyc
│     │        │  │  ├─ python.cpython-310.pyc
│     │        │  │  ├─ python_api.cpython-310.pyc
│     │        │  │  ├─ python_path.cpython-310.pyc
│     │        │  │  ├─ recwarn.cpython-310.pyc
│     │        │  │  ├─ reports.cpython-310.pyc
│     │        │  │  ├─ runner.cpython-310.pyc
│     │        │  │  ├─ scope.cpython-310.pyc
│     │        │  │  ├─ setuponly.cpython-310.pyc
│     │        │  │  ├─ setupplan.cpython-310.pyc
│     │        │  │  ├─ skipping.cpython-310.pyc
│     │        │  │  ├─ stash.cpython-310.pyc
│     │        │  │  ├─ stepwise.cpython-310.pyc
│     │        │  │  ├─ terminal.cpython-310.pyc
│     │        │  │  ├─ threadexception.cpython-310.pyc
│     │        │  │  ├─ timing.cpython-310.pyc
│     │        │  │  ├─ tmpdir.cpython-310.pyc
│     │        │  │  ├─ unittest.cpython-310.pyc
│     │        │  │  ├─ unraisableexception.cpython-310.pyc
│     │        │  │  ├─ warning_types.cpython-310.pyc
│     │        │  │  └─ warnings.cpython-310.pyc
│     │        │  ├─ _argcomplete.py
│     │        │  ├─ _code
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ code.cpython-310.pyc
│     │        │  │  │  └─ source.cpython-310.pyc
│     │        │  │  ├─ code.py
│     │        │  │  └─ source.py
│     │        │  ├─ _io
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ saferepr.cpython-310.pyc
│     │        │  │  │  ├─ terminalwriter.cpython-310.pyc
│     │        │  │  │  └─ wcwidth.cpython-310.pyc
│     │        │  │  ├─ saferepr.py
│     │        │  │  ├─ terminalwriter.py
│     │        │  │  └─ wcwidth.py
│     │        │  ├─ _py
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ error.cpython-310.pyc
│     │        │  │  │  └─ path.cpython-310.pyc
│     │        │  │  ├─ error.py
│     │        │  │  └─ path.py
│     │        │  ├─ _version.py
│     │        │  ├─ assertion
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ rewrite.cpython-310.pyc
│     │        │  │  │  ├─ truncate.cpython-310.pyc
│     │        │  │  │  └─ util.cpython-310.pyc
│     │        │  │  ├─ rewrite.py
│     │        │  │  ├─ truncate.py
│     │        │  │  └─ util.py
│     │        │  ├─ cacheprovider.py
│     │        │  ├─ capture.py
│     │        │  ├─ compat.py
│     │        │  ├─ config
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ argparsing.cpython-310.pyc
│     │        │  │  │  ├─ compat.cpython-310.pyc
│     │        │  │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  │  └─ findpaths.cpython-310.pyc
│     │        │  │  ├─ argparsing.py
│     │        │  │  ├─ compat.py
│     │        │  │  ├─ exceptions.py
│     │        │  │  └─ findpaths.py
│     │        │  ├─ debugging.py
│     │        │  ├─ deprecated.py
│     │        │  ├─ doctest.py
│     │        │  ├─ faulthandler.py
│     │        │  ├─ fixtures.py
│     │        │  ├─ freeze_support.py
│     │        │  ├─ helpconfig.py
│     │        │  ├─ junitxml.py
│     │        │  ├─ legacypath.py
│     │        │  ├─ logging.py
│     │        │  ├─ main.py
│     │        │  ├─ mark
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ expression.cpython-310.pyc
│     │        │  │  │  └─ structures.cpython-310.pyc
│     │        │  │  ├─ expression.py
│     │        │  │  └─ structures.py
│     │        │  ├─ monkeypatch.py
│     │        │  ├─ nodes.py
│     │        │  ├─ nose.py
│     │        │  ├─ outcomes.py
│     │        │  ├─ pastebin.py
│     │        │  ├─ pathlib.py
│     │        │  ├─ py.typed
│     │        │  ├─ pytester.py
│     │        │  ├─ pytester_assertions.py
│     │        │  ├─ python.py
│     │        │  ├─ python_api.py
│     │        │  ├─ python_path.py
│     │        │  ├─ recwarn.py
│     │        │  ├─ reports.py
│     │        │  ├─ runner.py
│     │        │  ├─ scope.py
│     │        │  ├─ setuponly.py
│     │        │  ├─ setupplan.py
│     │        │  ├─ skipping.py
│     │        │  ├─ stash.py
│     │        │  ├─ stepwise.py
│     │        │  ├─ terminal.py
│     │        │  ├─ threadexception.py
│     │        │  ├─ timing.py
│     │        │  ├─ tmpdir.py
│     │        │  ├─ unittest.py
│     │        │  ├─ unraisableexception.py
│     │        │  ├─ warning_types.py
│     │        │  └─ warnings.py
│     │        ├─ _yaml
│     │        │  ├─ __init__.py
│     │        │  └─ __pycache__
│     │        │     └─ __init__.cpython-310.pyc
│     │        ├─ aiofiles
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ base.cpython-310.pyc
│     │        │  │  ├─ os.cpython-310.pyc
│     │        │  │  └─ ospath.cpython-310.pyc
│     │        │  ├─ base.py
│     │        │  ├─ os.py
│     │        │  ├─ ospath.py
│     │        │  ├─ tempfile
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ temptypes.cpython-310.pyc
│     │        │  │  └─ temptypes.py
│     │        │  └─ threadpool
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ binary.cpython-310.pyc
│     │        │     │  ├─ text.cpython-310.pyc
│     │        │     │  └─ utils.cpython-310.pyc
│     │        │     ├─ binary.py
│     │        │     ├─ text.py
│     │        │     └─ utils.py
│     │        ├─ aiofiles-23.1.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ aiosmtplib
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ api.cpython-310.pyc
│     │        │  │  ├─ auth.cpython-310.pyc
│     │        │  │  ├─ email.cpython-310.pyc
│     │        │  │  ├─ errors.cpython-310.pyc
│     │        │  │  ├─ esmtp.cpython-310.pyc
│     │        │  │  ├─ protocol.cpython-310.pyc
│     │        │  │  ├─ response.cpython-310.pyc
│     │        │  │  ├─ smtp.cpython-310.pyc
│     │        │  │  ├─ status.cpython-310.pyc
│     │        │  │  └─ typing.cpython-310.pyc
│     │        │  ├─ api.py
│     │        │  ├─ auth.py
│     │        │  ├─ email.py
│     │        │  ├─ errors.py
│     │        │  ├─ esmtp.py
│     │        │  ├─ protocol.py
│     │        │  ├─ py.typed
│     │        │  ├─ response.py
│     │        │  ├─ smtp.py
│     │        │  ├─ status.py
│     │        │  └─ typing.py
│     │        ├─ aiosmtplib-2.0.2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.txt
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ alembic
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ command.cpython-310.pyc
│     │        │  │  ├─ config.cpython-310.pyc
│     │        │  │  ├─ context.cpython-310.pyc
│     │        │  │  ├─ environment.cpython-310.pyc
│     │        │  │  ├─ migration.cpython-310.pyc
│     │        │  │  └─ op.cpython-310.pyc
│     │        │  ├─ autogenerate
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ api.cpython-310.pyc
│     │        │  │  │  ├─ compare.cpython-310.pyc
│     │        │  │  │  ├─ render.cpython-310.pyc
│     │        │  │  │  └─ rewriter.cpython-310.pyc
│     │        │  │  ├─ api.py
│     │        │  │  ├─ compare.py
│     │        │  │  ├─ render.py
│     │        │  │  └─ rewriter.py
│     │        │  ├─ command.py
│     │        │  ├─ config.py
│     │        │  ├─ context.py
│     │        │  ├─ context.pyi
│     │        │  ├─ ddl
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ impl.cpython-310.pyc
│     │        │  │  │  ├─ mssql.cpython-310.pyc
│     │        │  │  │  ├─ mysql.cpython-310.pyc
│     │        │  │  │  ├─ oracle.cpython-310.pyc
│     │        │  │  │  ├─ postgresql.cpython-310.pyc
│     │        │  │  │  └─ sqlite.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ impl.py
│     │        │  │  ├─ mssql.py
│     │        │  │  ├─ mysql.py
│     │        │  │  ├─ oracle.py
│     │        │  │  ├─ postgresql.py
│     │        │  │  └─ sqlite.py
│     │        │  ├─ environment.py
│     │        │  ├─ migration.py
│     │        │  ├─ op.py
│     │        │  ├─ op.pyi
│     │        │  ├─ operations
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ batch.cpython-310.pyc
│     │        │  │  │  ├─ ops.cpython-310.pyc
│     │        │  │  │  ├─ schemaobj.cpython-310.pyc
│     │        │  │  │  └─ toimpl.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ batch.py
│     │        │  │  ├─ ops.py
│     │        │  │  ├─ schemaobj.py
│     │        │  │  └─ toimpl.py
│     │        │  ├─ py.typed
│     │        │  ├─ runtime
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ environment.cpython-310.pyc
│     │        │  │  │  └─ migration.cpython-310.pyc
│     │        │  │  ├─ environment.py
│     │        │  │  └─ migration.py
│     │        │  ├─ script
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  └─ revision.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  └─ revision.py
│     │        │  ├─ templates
│     │        │  │  ├─ async
│     │        │  │  │  ├─ README
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  └─ env.cpython-310.pyc
│     │        │  │  │  ├─ alembic.ini.mako
│     │        │  │  │  ├─ env.py
│     │        │  │  │  └─ script.py.mako
│     │        │  │  ├─ generic
│     │        │  │  │  ├─ README
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  └─ env.cpython-310.pyc
│     │        │  │  │  ├─ alembic.ini.mako
│     │        │  │  │  ├─ env.py
│     │        │  │  │  └─ script.py.mako
│     │        │  │  └─ multidb
│     │        │  │     ├─ README
│     │        │  │     ├─ __pycache__
│     │        │  │     │  └─ env.cpython-310.pyc
│     │        │  │     ├─ alembic.ini.mako
│     │        │  │     ├─ env.py
│     │        │  │     └─ script.py.mako
│     │        │  ├─ testing
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ assertions.cpython-310.pyc
│     │        │  │  │  ├─ env.cpython-310.pyc
│     │        │  │  │  ├─ fixtures.cpython-310.pyc
│     │        │  │  │  ├─ requirements.cpython-310.pyc
│     │        │  │  │  ├─ schemacompare.cpython-310.pyc
│     │        │  │  │  ├─ util.cpython-310.pyc
│     │        │  │  │  └─ warnings.cpython-310.pyc
│     │        │  │  ├─ assertions.py
│     │        │  │  ├─ env.py
│     │        │  │  ├─ fixtures.py
│     │        │  │  ├─ plugin
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  └─ bootstrap.cpython-310.pyc
│     │        │  │  │  └─ bootstrap.py
│     │        │  │  ├─ requirements.py
│     │        │  │  ├─ schemacompare.py
│     │        │  │  ├─ suite
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _autogen_fixtures.cpython-310.pyc
│     │        │  │  │  │  ├─ test_autogen_comments.cpython-310.pyc
│     │        │  │  │  │  ├─ test_autogen_computed.cpython-310.pyc
│     │        │  │  │  │  ├─ test_autogen_diffs.cpython-310.pyc
│     │        │  │  │  │  ├─ test_autogen_fks.cpython-310.pyc
│     │        │  │  │  │  ├─ test_autogen_identity.cpython-310.pyc
│     │        │  │  │  │  ├─ test_environment.cpython-310.pyc
│     │        │  │  │  │  └─ test_op.cpython-310.pyc
│     │        │  │  │  ├─ _autogen_fixtures.py
│     │        │  │  │  ├─ test_autogen_comments.py
│     │        │  │  │  ├─ test_autogen_computed.py
│     │        │  │  │  ├─ test_autogen_diffs.py
│     │        │  │  │  ├─ test_autogen_fks.py
│     │        │  │  │  ├─ test_autogen_identity.py
│     │        │  │  │  ├─ test_environment.py
│     │        │  │  │  └─ test_op.py
│     │        │  │  ├─ util.py
│     │        │  │  └─ warnings.py
│     │        │  └─ util
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ compat.cpython-310.pyc
│     │        │     │  ├─ editor.cpython-310.pyc
│     │        │     │  ├─ exc.cpython-310.pyc
│     │        │     │  ├─ langhelpers.cpython-310.pyc
│     │        │     │  ├─ messaging.cpython-310.pyc
│     │        │     │  ├─ pyfiles.cpython-310.pyc
│     │        │     │  └─ sqla_compat.cpython-310.pyc
│     │        │     ├─ compat.py
│     │        │     ├─ editor.py
│     │        │     ├─ exc.py
│     │        │     ├─ langhelpers.py
│     │        │     ├─ messaging.py
│     │        │     ├─ pyfiles.py
│     │        │     └─ sqla_compat.py
│     │        ├─ alembic-1.11.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ anyio
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ from_thread.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ from_thread.cpython-310.pyc
│     │        │  │  ├─ lowlevel.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ lowlevel.cpython-310.pyc
│     │        │  │  ├─ pytest_plugin.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ pytest_plugin.cpython-310.pyc
│     │        │  │  ├─ to_process.cpython-310.pyc
│     │        │  │  ├─ to_thread.cpython-310-pytest-7.4.0.pyc
│     │        │  │  └─ to_thread.cpython-310.pyc
│     │        │  ├─ _backends
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _asyncio.cpython-310.pyc
│     │        │  │  │  └─ _trio.cpython-310.pyc
│     │        │  │  ├─ _asyncio.py
│     │        │  │  └─ _trio.py
│     │        │  ├─ _core
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _compat.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _compat.cpython-310.pyc
│     │        │  │  │  ├─ _eventloop.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _eventloop.cpython-310.pyc
│     │        │  │  │  ├─ _exceptions.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _exceptions.cpython-310.pyc
│     │        │  │  │  ├─ _fileio.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _fileio.cpython-310.pyc
│     │        │  │  │  ├─ _resources.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _resources.cpython-310.pyc
│     │        │  │  │  ├─ _signals.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _signals.cpython-310.pyc
│     │        │  │  │  ├─ _sockets.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _sockets.cpython-310.pyc
│     │        │  │  │  ├─ _streams.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _streams.cpython-310.pyc
│     │        │  │  │  ├─ _subprocesses.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _subprocesses.cpython-310.pyc
│     │        │  │  │  ├─ _synchronization.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _synchronization.cpython-310.pyc
│     │        │  │  │  ├─ _tasks.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _tasks.cpython-310.pyc
│     │        │  │  │  ├─ _testing.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _testing.cpython-310.pyc
│     │        │  │  │  ├─ _typedattr.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  └─ _typedattr.cpython-310.pyc
│     │        │  │  ├─ _compat.py
│     │        │  │  ├─ _eventloop.py
│     │        │  │  ├─ _exceptions.py
│     │        │  │  ├─ _fileio.py
│     │        │  │  ├─ _resources.py
│     │        │  │  ├─ _signals.py
│     │        │  │  ├─ _sockets.py
│     │        │  │  ├─ _streams.py
│     │        │  │  ├─ _subprocesses.py
│     │        │  │  ├─ _synchronization.py
│     │        │  │  ├─ _tasks.py
│     │        │  │  ├─ _testing.py
│     │        │  │  └─ _typedattr.py
│     │        │  ├─ abc
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _resources.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _resources.cpython-310.pyc
│     │        │  │  │  ├─ _sockets.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _sockets.cpython-310.pyc
│     │        │  │  │  ├─ _streams.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _streams.cpython-310.pyc
│     │        │  │  │  ├─ _subprocesses.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _subprocesses.cpython-310.pyc
│     │        │  │  │  ├─ _tasks.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _tasks.cpython-310.pyc
│     │        │  │  │  ├─ _testing.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  └─ _testing.cpython-310.pyc
│     │        │  │  ├─ _resources.py
│     │        │  │  ├─ _sockets.py
│     │        │  │  ├─ _streams.py
│     │        │  │  ├─ _subprocesses.py
│     │        │  │  ├─ _tasks.py
│     │        │  │  └─ _testing.py
│     │        │  ├─ from_thread.py
│     │        │  ├─ lowlevel.py
│     │        │  ├─ py.typed
│     │        │  ├─ pytest_plugin.py
│     │        │  ├─ streams
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ buffered.cpython-310.pyc
│     │        │  │  │  ├─ file.cpython-310.pyc
│     │        │  │  │  ├─ memory.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ memory.cpython-310.pyc
│     │        │  │  │  ├─ stapled.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ stapled.cpython-310.pyc
│     │        │  │  │  ├─ text.cpython-310.pyc
│     │        │  │  │  ├─ tls.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  └─ tls.cpython-310.pyc
│     │        │  │  ├─ buffered.py
│     │        │  │  ├─ file.py
│     │        │  │  ├─ memory.py
│     │        │  │  ├─ stapled.py
│     │        │  │  ├─ text.py
│     │        │  │  └─ tls.py
│     │        │  ├─ to_process.py
│     │        │  └─ to_thread.py
│     │        ├─ anyio-3.7.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ argon2
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ _legacy.cpython-310.pyc
│     │        │  │  ├─ _password_hasher.cpython-310.pyc
│     │        │  │  ├─ _typing.cpython-310.pyc
│     │        │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ low_level.cpython-310.pyc
│     │        │  │  └─ profiles.cpython-310.pyc
│     │        │  ├─ _legacy.py
│     │        │  ├─ _password_hasher.py
│     │        │  ├─ _typing.py
│     │        │  ├─ _utils.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ low_level.py
│     │        │  ├─ profiles.py
│     │        │  └─ py.typed
│     │        ├─ argon2_cffi-21.3.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ argon2_cffi_bindings-21.2.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ black
│     │        │  ├─ __init__.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ _width_table.cpython-310.pyc
│     │        │  │  ├─ brackets.cpython-310.pyc
│     │        │  │  ├─ cache.cpython-310.pyc
│     │        │  │  ├─ comments.cpython-310.pyc
│     │        │  │  ├─ concurrency.cpython-310.pyc
│     │        │  │  ├─ const.cpython-310.pyc
│     │        │  │  ├─ debug.cpython-310.pyc
│     │        │  │  ├─ files.cpython-310.pyc
│     │        │  │  ├─ handle_ipynb_magics.cpython-310.pyc
│     │        │  │  ├─ linegen.cpython-310.pyc
│     │        │  │  ├─ lines.cpython-310.pyc
│     │        │  │  ├─ mode.cpython-310.pyc
│     │        │  │  ├─ nodes.cpython-310.pyc
│     │        │  │  ├─ numerics.cpython-310.pyc
│     │        │  │  ├─ output.cpython-310.pyc
│     │        │  │  ├─ parsing.cpython-310.pyc
│     │        │  │  ├─ report.cpython-310.pyc
│     │        │  │  ├─ rusty.cpython-310.pyc
│     │        │  │  ├─ strings.cpython-310.pyc
│     │        │  │  └─ trans.cpython-310.pyc
│     │        │  ├─ _width_table.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ _width_table.py
│     │        │  ├─ brackets.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ brackets.py
│     │        │  ├─ cache.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ cache.py
│     │        │  ├─ comments.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ comments.py
│     │        │  ├─ concurrency.py
│     │        │  ├─ const.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ const.py
│     │        │  ├─ debug.py
│     │        │  ├─ files.py
│     │        │  ├─ handle_ipynb_magics.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ handle_ipynb_magics.py
│     │        │  ├─ linegen.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ linegen.py
│     │        │  ├─ lines.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ lines.py
│     │        │  ├─ mode.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ mode.py
│     │        │  ├─ nodes.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ nodes.py
│     │        │  ├─ numerics.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ numerics.py
│     │        │  ├─ output.py
│     │        │  ├─ parsing.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ parsing.py
│     │        │  ├─ py.typed
│     │        │  ├─ report.py
│     │        │  ├─ rusty.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ rusty.py
│     │        │  ├─ strings.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ strings.py
│     │        │  ├─ trans.cpython-310-x86_64-linux-gnu.so
│     │        │  └─ trans.py
│     │        ├─ black-23.3.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ licenses
│     │        │     ├─ AUTHORS.md
│     │        │     └─ LICENSE
│     │        ├─ blackd
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  └─ middlewares.cpython-310.pyc
│     │        │  └─ middlewares.py
│     │        ├─ blib2to3
│     │        │  ├─ Grammar.txt
│     │        │  ├─ LICENSE
│     │        │  ├─ PatternGrammar.txt
│     │        │  ├─ README
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ pygram.cpython-310.pyc
│     │        │  │  └─ pytree.cpython-310.pyc
│     │        │  ├─ pgen2
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ conv.cpython-310.pyc
│     │        │  │  │  ├─ driver.cpython-310.pyc
│     │        │  │  │  ├─ grammar.cpython-310.pyc
│     │        │  │  │  ├─ literals.cpython-310.pyc
│     │        │  │  │  ├─ parse.cpython-310.pyc
│     │        │  │  │  ├─ pgen.cpython-310.pyc
│     │        │  │  │  ├─ token.cpython-310.pyc
│     │        │  │  │  └─ tokenize.cpython-310.pyc
│     │        │  │  ├─ conv.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ conv.py
│     │        │  │  ├─ driver.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ driver.py
│     │        │  │  ├─ grammar.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ grammar.py
│     │        │  │  ├─ literals.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ literals.py
│     │        │  │  ├─ parse.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ parse.py
│     │        │  │  ├─ pgen.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ pgen.py
│     │        │  │  ├─ token.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ token.py
│     │        │  │  ├─ tokenize.cpython-310-x86_64-linux-gnu.so
│     │        │  │  └─ tokenize.py
│     │        │  ├─ pygram.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ pygram.py
│     │        │  ├─ pytree.cpython-310-x86_64-linux-gnu.so
│     │        │  └─ pytree.py
│     │        ├─ build
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ env.cpython-310.pyc
│     │        │  │  └─ util.cpython-310.pyc
│     │        │  ├─ env.py
│     │        │  ├─ py.typed
│     │        │  └─ util.py
│     │        ├─ build-0.10.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ WHEEL
│     │        │  └─ entry_points.txt
│     │        ├─ certifi
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  └─ core.cpython-310.pyc
│     │        │  ├─ cacert.pem
│     │        │  ├─ core.py
│     │        │  └─ py.typed
│     │        ├─ certifi-2023.5.7.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ cffi
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ api.cpython-310.pyc
│     │        │  │  ├─ backend_ctypes.cpython-310.pyc
│     │        │  │  ├─ cffi_opcode.cpython-310.pyc
│     │        │  │  ├─ commontypes.cpython-310.pyc
│     │        │  │  ├─ cparser.cpython-310.pyc
│     │        │  │  ├─ error.cpython-310.pyc
│     │        │  │  ├─ ffiplatform.cpython-310.pyc
│     │        │  │  ├─ lock.cpython-310.pyc
│     │        │  │  ├─ model.cpython-310.pyc
│     │        │  │  ├─ pkgconfig.cpython-310.pyc
│     │        │  │  ├─ recompiler.cpython-310.pyc
│     │        │  │  ├─ setuptools_ext.cpython-310.pyc
│     │        │  │  ├─ vengine_cpy.cpython-310.pyc
│     │        │  │  ├─ vengine_gen.cpython-310.pyc
│     │        │  │  └─ verifier.cpython-310.pyc
│     │        │  ├─ _cffi_errors.h
│     │        │  ├─ _cffi_include.h
│     │        │  ├─ _embedding.h
│     │        │  ├─ api.py
│     │        │  ├─ backend_ctypes.py
│     │        │  ├─ cffi_opcode.py
│     │        │  ├─ commontypes.py
│     │        │  ├─ cparser.py
│     │        │  ├─ error.py
│     │        │  ├─ ffiplatform.py
│     │        │  ├─ lock.py
│     │        │  ├─ model.py
│     │        │  ├─ parse_c_type.h
│     │        │  ├─ pkgconfig.py
│     │        │  ├─ recompiler.py
│     │        │  ├─ setuptools_ext.py
│     │        │  ├─ vengine_cpy.py
│     │        │  ├─ vengine_gen.py
│     │        │  └─ verifier.py
│     │        ├─ cffi-1.15.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ click
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _compat.cpython-310.pyc
│     │        │  │  ├─ _termui_impl.cpython-310.pyc
│     │        │  │  ├─ _textwrap.cpython-310.pyc
│     │        │  │  ├─ _winconsole.cpython-310.pyc
│     │        │  │  ├─ core.cpython-310.pyc
│     │        │  │  ├─ decorators.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ formatting.cpython-310.pyc
│     │        │  │  ├─ globals.cpython-310.pyc
│     │        │  │  ├─ parser.cpython-310.pyc
│     │        │  │  ├─ shell_completion.cpython-310.pyc
│     │        │  │  ├─ termui.cpython-310.pyc
│     │        │  │  ├─ testing.cpython-310.pyc
│     │        │  │  ├─ types.cpython-310.pyc
│     │        │  │  └─ utils.cpython-310.pyc
│     │        │  ├─ _compat.py
│     │        │  ├─ _termui_impl.py
│     │        │  ├─ _textwrap.py
│     │        │  ├─ _winconsole.py
│     │        │  ├─ core.py
│     │        │  ├─ decorators.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ formatting.py
│     │        │  ├─ globals.py
│     │        │  ├─ parser.py
│     │        │  ├─ py.typed
│     │        │  ├─ shell_completion.py
│     │        │  ├─ termui.py
│     │        │  ├─ testing.py
│     │        │  ├─ types.py
│     │        │  └─ utils.py
│     │        ├─ click-8.1.3.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.rst
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ coverage
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ annotate.cpython-310.pyc
│     │        │  │  ├─ bytecode.cpython-310.pyc
│     │        │  │  ├─ cmdline.cpython-310.pyc
│     │        │  │  ├─ collector.cpython-310.pyc
│     │        │  │  ├─ config.cpython-310.pyc
│     │        │  │  ├─ context.cpython-310.pyc
│     │        │  │  ├─ control.cpython-310.pyc
│     │        │  │  ├─ data.cpython-310.pyc
│     │        │  │  ├─ debug.cpython-310.pyc
│     │        │  │  ├─ disposition.cpython-310.pyc
│     │        │  │  ├─ env.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ execfile.cpython-310.pyc
│     │        │  │  ├─ files.cpython-310.pyc
│     │        │  │  ├─ html.cpython-310.pyc
│     │        │  │  ├─ inorout.cpython-310.pyc
│     │        │  │  ├─ jsonreport.cpython-310.pyc
│     │        │  │  ├─ lcovreport.cpython-310.pyc
│     │        │  │  ├─ misc.cpython-310.pyc
│     │        │  │  ├─ multiproc.cpython-310.pyc
│     │        │  │  ├─ numbits.cpython-310.pyc
│     │        │  │  ├─ parser.cpython-310.pyc
│     │        │  │  ├─ phystokens.cpython-310.pyc
│     │        │  │  ├─ plugin.cpython-310.pyc
│     │        │  │  ├─ plugin_support.cpython-310.pyc
│     │        │  │  ├─ python.cpython-310.pyc
│     │        │  │  ├─ pytracer.cpython-310.pyc
│     │        │  │  ├─ report.cpython-310.pyc
│     │        │  │  ├─ report_core.cpython-310.pyc
│     │        │  │  ├─ results.cpython-310.pyc
│     │        │  │  ├─ sqldata.cpython-310.pyc
│     │        │  │  ├─ templite.cpython-310.pyc
│     │        │  │  ├─ tomlconfig.cpython-310.pyc
│     │        │  │  ├─ types.cpython-310.pyc
│     │        │  │  ├─ version.cpython-310.pyc
│     │        │  │  └─ xmlreport.cpython-310.pyc
│     │        │  ├─ annotate.py
│     │        │  ├─ bytecode.py
│     │        │  ├─ cmdline.py
│     │        │  ├─ collector.py
│     │        │  ├─ config.py
│     │        │  ├─ context.py
│     │        │  ├─ control.py
│     │        │  ├─ data.py
│     │        │  ├─ debug.py
│     │        │  ├─ disposition.py
│     │        │  ├─ env.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ execfile.py
│     │        │  ├─ files.py
│     │        │  ├─ fullcoverage
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ encodings.cpython-310.pyc
│     │        │  │  └─ encodings.py
│     │        │  ├─ html.py
│     │        │  ├─ htmlfiles
│     │        │  │  ├─ coverage_html.js
│     │        │  │  ├─ favicon_32.png
│     │        │  │  ├─ index.html
│     │        │  │  ├─ keybd_closed.png
│     │        │  │  ├─ keybd_open.png
│     │        │  │  ├─ pyfile.html
│     │        │  │  ├─ style.css
│     │        │  │  └─ style.scss
│     │        │  ├─ inorout.py
│     │        │  ├─ jsonreport.py
│     │        │  ├─ lcovreport.py
│     │        │  ├─ misc.py
│     │        │  ├─ multiproc.py
│     │        │  ├─ numbits.py
│     │        │  ├─ parser.py
│     │        │  ├─ phystokens.py
│     │        │  ├─ plugin.py
│     │        │  ├─ plugin_support.py
│     │        │  ├─ py.typed
│     │        │  ├─ python.py
│     │        │  ├─ pytracer.py
│     │        │  ├─ report.py
│     │        │  ├─ report_core.py
│     │        │  ├─ results.py
│     │        │  ├─ sqldata.py
│     │        │  ├─ templite.py
│     │        │  ├─ tomlconfig.py
│     │        │  ├─ tracer.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ types.py
│     │        │  ├─ version.py
│     │        │  └─ xmlreport.py
│     │        ├─ coverage-7.2.7.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.txt
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ dateutil
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _common.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  ├─ easter.cpython-310.pyc
│     │        │  │  ├─ relativedelta.cpython-310.pyc
│     │        │  │  ├─ rrule.cpython-310.pyc
│     │        │  │  ├─ tzwin.cpython-310.pyc
│     │        │  │  └─ utils.cpython-310.pyc
│     │        │  ├─ _common.py
│     │        │  ├─ _version.py
│     │        │  ├─ easter.py
│     │        │  ├─ parser
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _parser.cpython-310.pyc
│     │        │  │  │  └─ isoparser.cpython-310.pyc
│     │        │  │  ├─ _parser.py
│     │        │  │  └─ isoparser.py
│     │        │  ├─ relativedelta.py
│     │        │  ├─ rrule.py
│     │        │  ├─ tz
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _common.cpython-310.pyc
│     │        │  │  │  ├─ _factories.cpython-310.pyc
│     │        │  │  │  ├─ tz.cpython-310.pyc
│     │        │  │  │  └─ win.cpython-310.pyc
│     │        │  │  ├─ _common.py
│     │        │  │  ├─ _factories.py
│     │        │  │  ├─ tz.py
│     │        │  │  └─ win.py
│     │        │  ├─ tzwin.py
│     │        │  ├─ utils.py
│     │        │  └─ zoneinfo
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  └─ rebuild.cpython-310.pyc
│     │        │     ├─ dateutil-zoneinfo.tar.gz
│     │        │     └─ rebuild.py
│     │        ├─ decouple.py
│     │        ├─ distutils-precedence.pth
│     │        ├─ dns
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _asyncbackend.cpython-310.pyc
│     │        │  │  ├─ _asyncio_backend.cpython-310.pyc
│     │        │  │  ├─ _curio_backend.cpython-310.pyc
│     │        │  │  ├─ _immutable_ctx.cpython-310.pyc
│     │        │  │  ├─ _trio_backend.cpython-310.pyc
│     │        │  │  ├─ asyncbackend.cpython-310.pyc
│     │        │  │  ├─ asyncquery.cpython-310.pyc
│     │        │  │  ├─ asyncresolver.cpython-310.pyc
│     │        │  │  ├─ dnssec.cpython-310.pyc
│     │        │  │  ├─ dnssectypes.cpython-310.pyc
│     │        │  │  ├─ e164.cpython-310.pyc
│     │        │  │  ├─ edns.cpython-310.pyc
│     │        │  │  ├─ entropy.cpython-310.pyc
│     │        │  │  ├─ enum.cpython-310.pyc
│     │        │  │  ├─ exception.cpython-310.pyc
│     │        │  │  ├─ flags.cpython-310.pyc
│     │        │  │  ├─ grange.cpython-310.pyc
│     │        │  │  ├─ immutable.cpython-310.pyc
│     │        │  │  ├─ inet.cpython-310.pyc
│     │        │  │  ├─ ipv4.cpython-310.pyc
│     │        │  │  ├─ ipv6.cpython-310.pyc
│     │        │  │  ├─ message.cpython-310.pyc
│     │        │  │  ├─ name.cpython-310.pyc
│     │        │  │  ├─ namedict.cpython-310.pyc
│     │        │  │  ├─ node.cpython-310.pyc
│     │        │  │  ├─ opcode.cpython-310.pyc
│     │        │  │  ├─ query.cpython-310.pyc
│     │        │  │  ├─ rcode.cpython-310.pyc
│     │        │  │  ├─ rdata.cpython-310.pyc
│     │        │  │  ├─ rdataclass.cpython-310.pyc
│     │        │  │  ├─ rdataset.cpython-310.pyc
│     │        │  │  ├─ rdatatype.cpython-310.pyc
│     │        │  │  ├─ renderer.cpython-310.pyc
│     │        │  │  ├─ resolver.cpython-310.pyc
│     │        │  │  ├─ reversename.cpython-310.pyc
│     │        │  │  ├─ rrset.cpython-310.pyc
│     │        │  │  ├─ serial.cpython-310.pyc
│     │        │  │  ├─ set.cpython-310.pyc
│     │        │  │  ├─ tokenizer.cpython-310.pyc
│     │        │  │  ├─ transaction.cpython-310.pyc
│     │        │  │  ├─ tsig.cpython-310.pyc
│     │        │  │  ├─ tsigkeyring.cpython-310.pyc
│     │        │  │  ├─ ttl.cpython-310.pyc
│     │        │  │  ├─ update.cpython-310.pyc
│     │        │  │  ├─ version.cpython-310.pyc
│     │        │  │  ├─ versioned.cpython-310.pyc
│     │        │  │  ├─ win32util.cpython-310.pyc
│     │        │  │  ├─ wire.cpython-310.pyc
│     │        │  │  ├─ xfr.cpython-310.pyc
│     │        │  │  ├─ zone.cpython-310.pyc
│     │        │  │  ├─ zonefile.cpython-310.pyc
│     │        │  │  └─ zonetypes.cpython-310.pyc
│     │        │  ├─ _asyncbackend.py
│     │        │  ├─ _asyncio_backend.py
│     │        │  ├─ _curio_backend.py
│     │        │  ├─ _immutable_ctx.py
│     │        │  ├─ _trio_backend.py
│     │        │  ├─ asyncbackend.py
│     │        │  ├─ asyncquery.py
│     │        │  ├─ asyncresolver.py
│     │        │  ├─ dnssec.py
│     │        │  ├─ dnssectypes.py
│     │        │  ├─ e164.py
│     │        │  ├─ edns.py
│     │        │  ├─ entropy.py
│     │        │  ├─ enum.py
│     │        │  ├─ exception.py
│     │        │  ├─ flags.py
│     │        │  ├─ grange.py
│     │        │  ├─ immutable.py
│     │        │  ├─ inet.py
│     │        │  ├─ ipv4.py
│     │        │  ├─ ipv6.py
│     │        │  ├─ message.py
│     │        │  ├─ name.py
│     │        │  ├─ namedict.py
│     │        │  ├─ node.py
│     │        │  ├─ opcode.py
│     │        │  ├─ py.typed
│     │        │  ├─ query.py
│     │        │  ├─ quic
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _asyncio.cpython-310.pyc
│     │        │  │  │  ├─ _common.cpython-310.pyc
│     │        │  │  │  ├─ _sync.cpython-310.pyc
│     │        │  │  │  └─ _trio.cpython-310.pyc
│     │        │  │  ├─ _asyncio.py
│     │        │  │  ├─ _common.py
│     │        │  │  ├─ _sync.py
│     │        │  │  └─ _trio.py
│     │        │  ├─ rcode.py
│     │        │  ├─ rdata.py
│     │        │  ├─ rdataclass.py
│     │        │  ├─ rdataset.py
│     │        │  ├─ rdatatype.py
│     │        │  ├─ rdtypes
│     │        │  │  ├─ ANY
│     │        │  │  │  ├─ AFSDB.py
│     │        │  │  │  ├─ AMTRELAY.py
│     │        │  │  │  ├─ AVC.py
│     │        │  │  │  ├─ CAA.py
│     │        │  │  │  ├─ CDNSKEY.py
│     │        │  │  │  ├─ CDS.py
│     │        │  │  │  ├─ CERT.py
│     │        │  │  │  ├─ CNAME.py
│     │        │  │  │  ├─ CSYNC.py
│     │        │  │  │  ├─ DLV.py
│     │        │  │  │  ├─ DNAME.py
│     │        │  │  │  ├─ DNSKEY.py
│     │        │  │  │  ├─ DS.py
│     │        │  │  │  ├─ EUI48.py
│     │        │  │  │  ├─ EUI64.py
│     │        │  │  │  ├─ GPOS.py
│     │        │  │  │  ├─ HINFO.py
│     │        │  │  │  ├─ HIP.py
│     │        │  │  │  ├─ ISDN.py
│     │        │  │  │  ├─ L32.py
│     │        │  │  │  ├─ L64.py
│     │        │  │  │  ├─ LOC.py
│     │        │  │  │  ├─ LP.py
│     │        │  │  │  ├─ MX.py
│     │        │  │  │  ├─ NID.py
│     │        │  │  │  ├─ NINFO.py
│     │        │  │  │  ├─ NS.py
│     │        │  │  │  ├─ NSEC.py
│     │        │  │  │  ├─ NSEC3.py
│     │        │  │  │  ├─ NSEC3PARAM.py
│     │        │  │  │  ├─ OPENPGPKEY.py
│     │        │  │  │  ├─ OPT.py
│     │        │  │  │  ├─ PTR.py
│     │        │  │  │  ├─ RP.py
│     │        │  │  │  ├─ RRSIG.py
│     │        │  │  │  ├─ RT.py
│     │        │  │  │  ├─ SMIMEA.py
│     │        │  │  │  ├─ SOA.py
│     │        │  │  │  ├─ SPF.py
│     │        │  │  │  ├─ SSHFP.py
│     │        │  │  │  ├─ TKEY.py
│     │        │  │  │  ├─ TLSA.py
│     │        │  │  │  ├─ TSIG.py
│     │        │  │  │  ├─ TXT.py
│     │        │  │  │  ├─ URI.py
│     │        │  │  │  ├─ X25.py
│     │        │  │  │  ├─ ZONEMD.py
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  └─ __pycache__
│     │        │  │  │     ├─ AFSDB.cpython-310.pyc
│     │        │  │  │     ├─ AMTRELAY.cpython-310.pyc
│     │        │  │  │     ├─ AVC.cpython-310.pyc
│     │        │  │  │     ├─ CAA.cpython-310.pyc
│     │        │  │  │     ├─ CDNSKEY.cpython-310.pyc
│     │        │  │  │     ├─ CDS.cpython-310.pyc
│     │        │  │  │     ├─ CERT.cpython-310.pyc
│     │        │  │  │     ├─ CNAME.cpython-310.pyc
│     │        │  │  │     ├─ CSYNC.cpython-310.pyc
│     │        │  │  │     ├─ DLV.cpython-310.pyc
│     │        │  │  │     ├─ DNAME.cpython-310.pyc
│     │        │  │  │     ├─ DNSKEY.cpython-310.pyc
│     │        │  │  │     ├─ DS.cpython-310.pyc
│     │        │  │  │     ├─ EUI48.cpython-310.pyc
│     │        │  │  │     ├─ EUI64.cpython-310.pyc
│     │        │  │  │     ├─ GPOS.cpython-310.pyc
│     │        │  │  │     ├─ HINFO.cpython-310.pyc
│     │        │  │  │     ├─ HIP.cpython-310.pyc
│     │        │  │  │     ├─ ISDN.cpython-310.pyc
│     │        │  │  │     ├─ L32.cpython-310.pyc
│     │        │  │  │     ├─ L64.cpython-310.pyc
│     │        │  │  │     ├─ LOC.cpython-310.pyc
│     │        │  │  │     ├─ LP.cpython-310.pyc
│     │        │  │  │     ├─ MX.cpython-310.pyc
│     │        │  │  │     ├─ NID.cpython-310.pyc
│     │        │  │  │     ├─ NINFO.cpython-310.pyc
│     │        │  │  │     ├─ NS.cpython-310.pyc
│     │        │  │  │     ├─ NSEC.cpython-310.pyc
│     │        │  │  │     ├─ NSEC3.cpython-310.pyc
│     │        │  │  │     ├─ NSEC3PARAM.cpython-310.pyc
│     │        │  │  │     ├─ OPENPGPKEY.cpython-310.pyc
│     │        │  │  │     ├─ OPT.cpython-310.pyc
│     │        │  │  │     ├─ PTR.cpython-310.pyc
│     │        │  │  │     ├─ RP.cpython-310.pyc
│     │        │  │  │     ├─ RRSIG.cpython-310.pyc
│     │        │  │  │     ├─ RT.cpython-310.pyc
│     │        │  │  │     ├─ SMIMEA.cpython-310.pyc
│     │        │  │  │     ├─ SOA.cpython-310.pyc
│     │        │  │  │     ├─ SPF.cpython-310.pyc
│     │        │  │  │     ├─ SSHFP.cpython-310.pyc
│     │        │  │  │     ├─ TKEY.cpython-310.pyc
│     │        │  │  │     ├─ TLSA.cpython-310.pyc
│     │        │  │  │     ├─ TSIG.cpython-310.pyc
│     │        │  │  │     ├─ TXT.cpython-310.pyc
│     │        │  │  │     ├─ URI.cpython-310.pyc
│     │        │  │  │     ├─ X25.cpython-310.pyc
│     │        │  │  │     ├─ ZONEMD.cpython-310.pyc
│     │        │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  ├─ CH
│     │        │  │  │  ├─ A.py
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  └─ __pycache__
│     │        │  │  │     ├─ A.cpython-310.pyc
│     │        │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  ├─ IN
│     │        │  │  │  ├─ A.py
│     │        │  │  │  ├─ AAAA.py
│     │        │  │  │  ├─ APL.py
│     │        │  │  │  ├─ DHCID.py
│     │        │  │  │  ├─ HTTPS.py
│     │        │  │  │  ├─ IPSECKEY.py
│     │        │  │  │  ├─ KX.py
│     │        │  │  │  ├─ NAPTR.py
│     │        │  │  │  ├─ NSAP.py
│     │        │  │  │  ├─ NSAP_PTR.py
│     │        │  │  │  ├─ PX.py
│     │        │  │  │  ├─ SRV.py
│     │        │  │  │  ├─ SVCB.py
│     │        │  │  │  ├─ WKS.py
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  └─ __pycache__
│     │        │  │  │     ├─ A.cpython-310.pyc
│     │        │  │  │     ├─ AAAA.cpython-310.pyc
│     │        │  │  │     ├─ APL.cpython-310.pyc
│     │        │  │  │     ├─ DHCID.cpython-310.pyc
│     │        │  │  │     ├─ HTTPS.cpython-310.pyc
│     │        │  │  │     ├─ IPSECKEY.cpython-310.pyc
│     │        │  │  │     ├─ KX.cpython-310.pyc
│     │        │  │  │     ├─ NAPTR.cpython-310.pyc
│     │        │  │  │     ├─ NSAP.cpython-310.pyc
│     │        │  │  │     ├─ NSAP_PTR.cpython-310.pyc
│     │        │  │  │     ├─ PX.cpython-310.pyc
│     │        │  │  │     ├─ SRV.cpython-310.pyc
│     │        │  │  │     ├─ SVCB.cpython-310.pyc
│     │        │  │  │     ├─ WKS.cpython-310.pyc
│     │        │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ dnskeybase.cpython-310.pyc
│     │        │  │  │  ├─ dsbase.cpython-310.pyc
│     │        │  │  │  ├─ euibase.cpython-310.pyc
│     │        │  │  │  ├─ mxbase.cpython-310.pyc
│     │        │  │  │  ├─ nsbase.cpython-310.pyc
│     │        │  │  │  ├─ svcbbase.cpython-310.pyc
│     │        │  │  │  ├─ tlsabase.cpython-310.pyc
│     │        │  │  │  ├─ txtbase.cpython-310.pyc
│     │        │  │  │  └─ util.cpython-310.pyc
│     │        │  │  ├─ dnskeybase.py
│     │        │  │  ├─ dsbase.py
│     │        │  │  ├─ euibase.py
│     │        │  │  ├─ mxbase.py
│     │        │  │  ├─ nsbase.py
│     │        │  │  ├─ svcbbase.py
│     │        │  │  ├─ tlsabase.py
│     │        │  │  ├─ txtbase.py
│     │        │  │  └─ util.py
│     │        │  ├─ renderer.py
│     │        │  ├─ resolver.py
│     │        │  ├─ reversename.py
│     │        │  ├─ rrset.py
│     │        │  ├─ serial.py
│     │        │  ├─ set.py
│     │        │  ├─ tokenizer.py
│     │        │  ├─ transaction.py
│     │        │  ├─ tsig.py
│     │        │  ├─ tsigkeyring.py
│     │        │  ├─ ttl.py
│     │        │  ├─ update.py
│     │        │  ├─ version.py
│     │        │  ├─ versioned.py
│     │        │  ├─ win32util.py
│     │        │  ├─ wire.py
│     │        │  ├─ xfr.py
│     │        │  ├─ zone.py
│     │        │  ├─ zonefile.py
│     │        │  └─ zonetypes.py
│     │        ├─ dnspython-2.3.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ dotenv
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ cli.cpython-310.pyc
│     │        │  │  ├─ ipython.cpython-310.pyc
│     │        │  │  ├─ main.cpython-310.pyc
│     │        │  │  ├─ parser.cpython-310.pyc
│     │        │  │  ├─ variables.cpython-310.pyc
│     │        │  │  └─ version.cpython-310.pyc
│     │        │  ├─ cli.py
│     │        │  ├─ ipython.py
│     │        │  ├─ main.py
│     │        │  ├─ parser.py
│     │        │  ├─ py.typed
│     │        │  ├─ variables.py
│     │        │  └─ version.py
│     │        ├─ editorconfig
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ compat.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ fnmatch.cpython-310.pyc
│     │        │  │  ├─ handler.cpython-310.pyc
│     │        │  │  ├─ ini.cpython-310.pyc
│     │        │  │  ├─ version.cpython-310.pyc
│     │        │  │  └─ versiontools.cpython-310.pyc
│     │        │  ├─ compat.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ fnmatch.py
│     │        │  ├─ handler.py
│     │        │  ├─ ini.py
│     │        │  ├─ version.py
│     │        │  └─ versiontools.py
│     │        ├─ email_validator
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ deliverability.cpython-310.pyc
│     │        │  │  ├─ exceptions_types.cpython-310.pyc
│     │        │  │  ├─ rfc_constants.cpython-310.pyc
│     │        │  │  ├─ syntax.cpython-310.pyc
│     │        │  │  └─ validate_email.cpython-310.pyc
│     │        │  ├─ deliverability.py
│     │        │  ├─ exceptions_types.py
│     │        │  ├─ py.typed
│     │        │  ├─ rfc_constants.py
│     │        │  ├─ syntax.py
│     │        │  └─ validate_email.py
│     │        ├─ email_validator-2.0.0.post2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ exceptiongroup
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _catch.cpython-310.pyc
│     │        │  │  ├─ _exceptions.cpython-310.pyc
│     │        │  │  ├─ _formatting.cpython-310.pyc
│     │        │  │  └─ _version.cpython-310.pyc
│     │        │  ├─ _catch.py
│     │        │  ├─ _exceptions.py
│     │        │  ├─ _formatting.py
│     │        │  ├─ _version.py
│     │        │  └─ py.typed
│     │        ├─ exceptiongroup-1.1.2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ factory
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ alchemy.cpython-310.pyc
│     │        │  │  ├─ base.cpython-310.pyc
│     │        │  │  ├─ builder.cpython-310.pyc
│     │        │  │  ├─ declarations.cpython-310.pyc
│     │        │  │  ├─ django.cpython-310.pyc
│     │        │  │  ├─ enums.cpython-310.pyc
│     │        │  │  ├─ errors.cpython-310.pyc
│     │        │  │  ├─ faker.cpython-310.pyc
│     │        │  │  ├─ fuzzy.cpython-310.pyc
│     │        │  │  ├─ helpers.cpython-310.pyc
│     │        │  │  ├─ mogo.cpython-310.pyc
│     │        │  │  ├─ mongoengine.cpython-310.pyc
│     │        │  │  ├─ random.cpython-310.pyc
│     │        │  │  └─ utils.cpython-310.pyc
│     │        │  ├─ alchemy.py
│     │        │  ├─ base.py
│     │        │  ├─ builder.py
│     │        │  ├─ declarations.py
│     │        │  ├─ django.py
│     │        │  ├─ enums.py
│     │        │  ├─ errors.py
│     │        │  ├─ faker.py
│     │        │  ├─ fuzzy.py
│     │        │  ├─ helpers.py
│     │        │  ├─ mogo.py
│     │        │  ├─ mongoengine.py
│     │        │  ├─ random.py
│     │        │  └─ utils.py
│     │        ├─ factory_boy-3.2.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ faker
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ cli.cpython-310.pyc
│     │        │  │  ├─ config.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ config.cpython-310.pyc
│     │        │  │  ├─ documentor.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ factory.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ factory.cpython-310.pyc
│     │        │  │  ├─ generator.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ generator.cpython-310.pyc
│     │        │  │  ├─ proxy.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ proxy.cpython-310.pyc
│     │        │  │  ├─ typing.cpython-310-pytest-7.4.0.pyc
│     │        │  │  └─ typing.cpython-310.pyc
│     │        │  ├─ cli.py
│     │        │  ├─ config.py
│     │        │  ├─ contrib
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  └─ pytest
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ plugin.cpython-310-pytest-7.4.0.pyc
│     │        │  │     │  └─ plugin.cpython-310.pyc
│     │        │  │     └─ plugin.py
│     │        │  ├─ decode
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ codes.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  └─ codes.cpython-310.pyc
│     │        │  │  └─ codes.py
│     │        │  ├─ documentor.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ factory.py
│     │        │  ├─ generator.py
│     │        │  ├─ providers
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ address
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_AU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_GB
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_NZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_MX
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ he_IL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hi_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ja_JP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ka_GE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ne_NP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sl_SI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ta_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ uk_UA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ automotive
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_BH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_JO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_PS
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_SA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_GB
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_NZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ et_EE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ he_IL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lt_LT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sq_AL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ vi_VN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ bank
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_GB
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_MX
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_CN
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ barcode
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ ja_JP
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ color
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ color.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ color.cpython-310.pyc
│     │        │  │  │  ├─ ar_PS
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bg_BG
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ color.py
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ he_IL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ uk_UA
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ company
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bg_BG
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_MX
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ja_JP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sl_SI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ credit_card
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ ru_RU
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ currency
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_AU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ tr_TR
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ date_time
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_AA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_EG
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hi_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sl_SI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ta_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ emoji
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ en_US
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ file
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ en_US
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ geo
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ tr_TR
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ internet
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_AA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bg_BG
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bs_BA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_AU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_GB
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_NZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ja_JP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sl_SI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ uk_UA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ isbn
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ isbn.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  ├─ isbn.cpython-310.pyc
│     │        │  │  │  │  ├─ rules.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ rules.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ isbn.py
│     │        │  │  │  └─ rules.py
│     │        │  │  ├─ job
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_AA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bs_BA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_MX
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ja_JP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ uk_UA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ lorem
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_AA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ he_IL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ja_JP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ la
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ misc
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ tl_PH
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ passport
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ en_US
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ person
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_AA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_PS
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_SA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bg_BG
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_GB
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_NZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_MX
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ et_EE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_QC
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ga_IE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ he_IL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hi_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ja_JP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ka_GE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lt_LT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lv_LV
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ne_NP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ or_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sl_SI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ta_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tw_GH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ uk_UA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ phone_number
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_AE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_JO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_PS
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bg_BG
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bs_BA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_AU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_GB
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_NZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_MX
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ he_IL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hi_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ja_JP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lt_LT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lv_LV
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ne_NP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sl_SI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ta_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tw_GH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ uk_UA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ profile
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ en_US
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ python
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ en_US
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ sbn
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ rules.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  ├─ rules.cpython-310.pyc
│     │        │  │  │  │  ├─ sbn.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ sbn.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ rules.py
│     │        │  │  │  └─ sbn.py
│     │        │  │  ├─ ssn
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bg_BG
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ dk_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_CY
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_GB
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_MX
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ et_EE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ he_IL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lb_LU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lt_LT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lv_LV
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ mt_MT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sl_SI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ uk_UA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  └─ user_agent
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │     │  └─ __init__.cpython-310.pyc
│     │        │  │     └─ en_US
│     │        │  │        ├─ __init__.py
│     │        │  │        └─ __pycache__
│     │        │  │           └─ __init__.cpython-310.pyc
│     │        │  ├─ proxy.py
│     │        │  ├─ py.typed
│     │        │  ├─ sphinx
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ autodoc.cpython-310.pyc
│     │        │  │  │  ├─ docstring.cpython-310.pyc
│     │        │  │  │  ├─ documentor.cpython-310.pyc
│     │        │  │  │  └─ validator.cpython-310.pyc
│     │        │  │  ├─ autodoc.py
│     │        │  │  ├─ docstring.py
│     │        │  │  ├─ documentor.py
│     │        │  │  └─ validator.py
│     │        │  ├─ typing.py
│     │        │  └─ utils
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ checksums.cpython-310.pyc
│     │        │     │  ├─ datasets.cpython-310-pytest-7.4.0.pyc
│     │        │     │  ├─ datasets.cpython-310.pyc
│     │        │     │  ├─ decorators.cpython-310-pytest-7.4.0.pyc
│     │        │     │  ├─ decorators.cpython-310.pyc
│     │        │     │  ├─ distribution.cpython-310-pytest-7.4.0.pyc
│     │        │     │  ├─ distribution.cpython-310.pyc
│     │        │     │  ├─ loading.cpython-310-pytest-7.4.0.pyc
│     │        │     │  ├─ loading.cpython-310.pyc
│     │        │     │  ├─ text.cpython-310-pytest-7.4.0.pyc
│     │        │     │  └─ text.cpython-310.pyc
│     │        │     ├─ checksums.py
│     │        │     ├─ datasets.py
│     │        │     ├─ decorators.py
│     │        │     ├─ distribution.py
│     │        │     ├─ loading.py
│     │        │     └─ text.py
│     │        ├─ fast_query_parsers
│     │        │  ├─ __init__.py
│     │        │  ├─ __init__.pyi
│     │        │  ├─ __pycache__
│     │        │  │  └─ __init__.cpython-310.pyc
│     │        │  ├─ fast_query_parsers.abi3.so
│     │        │  └─ py.typed
│     │        ├─ fast_query_parsers-0.4.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ license_files
│     │        │     └─ LICENSE
│     │        ├─ fastjsonschema
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ draft04.cpython-310.pyc
│     │        │  │  ├─ draft06.cpython-310.pyc
│     │        │  │  ├─ draft07.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ generator.cpython-310.pyc
│     │        │  │  ├─ indent.cpython-310.pyc
│     │        │  │  ├─ ref_resolver.cpython-310.pyc
│     │        │  │  └─ version.cpython-310.pyc
│     │        │  ├─ draft04.py
│     │        │  ├─ draft06.py
│     │        │  ├─ draft07.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ generator.py
│     │        │  ├─ indent.py
│     │        │  ├─ ref_resolver.py
│     │        │  └─ version.py
│     │        ├─ fastjsonschema-2.17.1.dist-info
│     │        │  ├─ AUTHORS
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ greenlet
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  └─ __init__.cpython-310.pyc
│     │        │  ├─ _greenlet.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ greenlet.cpp
│     │        │  ├─ greenlet.h
│     │        │  ├─ greenlet_allocator.hpp
│     │        │  ├─ greenlet_compiler_compat.hpp
│     │        │  ├─ greenlet_cpython_compat.hpp
│     │        │  ├─ greenlet_exceptions.hpp
│     │        │  ├─ greenlet_greenlet.hpp
│     │        │  ├─ greenlet_internal.hpp
│     │        │  ├─ greenlet_refs.hpp
│     │        │  ├─ greenlet_slp_switch.hpp
│     │        │  ├─ greenlet_thread_state.hpp
│     │        │  ├─ greenlet_thread_state_dict_cleanup.hpp
│     │        │  ├─ greenlet_thread_support.hpp
│     │        │  ├─ platform
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ setup_switch_x64_masm.cmd
│     │        │  │  ├─ switch_aarch64_gcc.h
│     │        │  │  ├─ switch_alpha_unix.h
│     │        │  │  ├─ switch_amd64_unix.h
│     │        │  │  ├─ switch_arm32_gcc.h
│     │        │  │  ├─ switch_arm32_ios.h
│     │        │  │  ├─ switch_arm64_masm.asm
│     │        │  │  ├─ switch_arm64_masm.obj
│     │        │  │  ├─ switch_arm64_msvc.h
│     │        │  │  ├─ switch_csky_gcc.h
│     │        │  │  ├─ switch_m68k_gcc.h
│     │        │  │  ├─ switch_mips_unix.h
│     │        │  │  ├─ switch_ppc64_aix.h
│     │        │  │  ├─ switch_ppc64_linux.h
│     │        │  │  ├─ switch_ppc_aix.h
│     │        │  │  ├─ switch_ppc_linux.h
│     │        │  │  ├─ switch_ppc_macosx.h
│     │        │  │  ├─ switch_ppc_unix.h
│     │        │  │  ├─ switch_riscv_unix.h
│     │        │  │  ├─ switch_s390_unix.h
│     │        │  │  ├─ switch_sparc_sun_gcc.h
│     │        │  │  ├─ switch_x32_unix.h
│     │        │  │  ├─ switch_x64_masm.asm
│     │        │  │  ├─ switch_x64_masm.obj
│     │        │  │  ├─ switch_x64_msvc.h
│     │        │  │  ├─ switch_x86_msvc.h
│     │        │  │  └─ switch_x86_unix.h
│     │        │  ├─ slp_platformselect.h
│     │        │  └─ tests
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ leakcheck.cpython-310.pyc
│     │        │     │  ├─ test_contextvars.cpython-310.pyc
│     │        │     │  ├─ test_cpp.cpython-310.pyc
│     │        │     │  ├─ test_extension_interface.cpython-310.pyc
│     │        │     │  ├─ test_gc.cpython-310.pyc
│     │        │     │  ├─ test_generator.cpython-310.pyc
│     │        │     │  ├─ test_generator_nested.cpython-310.pyc
│     │        │     │  ├─ test_greenlet.cpython-310.pyc
│     │        │     │  ├─ test_greenlet_trash.cpython-310.pyc
│     │        │     │  ├─ test_leaks.cpython-310.pyc
│     │        │     │  ├─ test_stack_saved.cpython-310.pyc
│     │        │     │  ├─ test_throw.cpython-310.pyc
│     │        │     │  ├─ test_tracing.cpython-310.pyc
│     │        │     │  ├─ test_version.cpython-310.pyc
│     │        │     │  └─ test_weakref.cpython-310.pyc
│     │        │     ├─ _test_extension.c
│     │        │     ├─ _test_extension.cpython-310-x86_64-linux-gnu.so
│     │        │     ├─ _test_extension_cpp.cpp
│     │        │     ├─ _test_extension_cpp.cpython-310-x86_64-linux-gnu.so
│     │        │     ├─ leakcheck.py
│     │        │     ├─ test_contextvars.py
│     │        │     ├─ test_cpp.py
│     │        │     ├─ test_extension_interface.py
│     │        │     ├─ test_gc.py
│     │        │     ├─ test_generator.py
│     │        │     ├─ test_generator_nested.py
│     │        │     ├─ test_greenlet.py
│     │        │     ├─ test_greenlet_trash.py
│     │        │     ├─ test_leaks.py
│     │        │     ├─ test_stack_saved.py
│     │        │     ├─ test_throw.py
│     │        │     ├─ test_tracing.py
│     │        │     ├─ test_version.py
│     │        │     └─ test_weakref.py
│     │        ├─ greenlet-2.0.2.dist-info
│     │        │  ├─ AUTHORS
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ LICENSE.PSF
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ h11
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _abnf.cpython-310.pyc
│     │        │  │  ├─ _connection.cpython-310.pyc
│     │        │  │  ├─ _events.cpython-310.pyc
│     │        │  │  ├─ _headers.cpython-310.pyc
│     │        │  │  ├─ _readers.cpython-310.pyc
│     │        │  │  ├─ _receivebuffer.cpython-310.pyc
│     │        │  │  ├─ _state.cpython-310.pyc
│     │        │  │  ├─ _util.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  └─ _writers.cpython-310.pyc
│     │        │  ├─ _abnf.py
│     │        │  ├─ _connection.py
│     │        │  ├─ _events.py
│     │        │  ├─ _headers.py
│     │        │  ├─ _readers.py
│     │        │  ├─ _receivebuffer.py
│     │        │  ├─ _state.py
│     │        │  ├─ _util.py
│     │        │  ├─ _version.py
│     │        │  ├─ _writers.py
│     │        │  ├─ py.typed
│     │        │  └─ tests
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ helpers.cpython-310.pyc
│     │        │     │  ├─ test_against_stdlib_http.cpython-310.pyc
│     │        │     │  ├─ test_connection.cpython-310.pyc
│     │        │     │  ├─ test_events.cpython-310.pyc
│     │        │     │  ├─ test_headers.cpython-310.pyc
│     │        │     │  ├─ test_helpers.cpython-310.pyc
│     │        │     │  ├─ test_io.cpython-310.pyc
│     │        │     │  ├─ test_receivebuffer.cpython-310.pyc
│     │        │     │  ├─ test_state.cpython-310.pyc
│     │        │     │  └─ test_util.cpython-310.pyc
│     │        │     ├─ data
│     │        │     │  └─ test-file
│     │        │     ├─ helpers.py
│     │        │     ├─ test_against_stdlib_http.py
│     │        │     ├─ test_connection.py
│     │        │     ├─ test_events.py
│     │        │     ├─ test_headers.py
│     │        │     ├─ test_helpers.py
│     │        │     ├─ test_io.py
│     │        │     ├─ test_receivebuffer.py
│     │        │     ├─ test_state.py
│     │        │     └─ test_util.py
│     │        ├─ h11-0.14.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.txt
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ html2text
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ cli.cpython-310.pyc
│     │        │  │  ├─ config.cpython-310.pyc
│     │        │  │  ├─ elements.cpython-310.pyc
│     │        │  │  ├─ typing.cpython-310.pyc
│     │        │  │  └─ utils.cpython-310.pyc
│     │        │  ├─ cli.py
│     │        │  ├─ config.py
│     │        │  ├─ elements.py
│     │        │  ├─ py.typed
│     │        │  ├─ typing.py
│     │        │  └─ utils.py
│     │        ├─ html2text-2020.1.16.dist-info
│     │        │  ├─ AUTHORS.rst
│     │        │  ├─ COPYING
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ httpcore
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _api.cpython-310.pyc
│     │        │  │  ├─ _exceptions.cpython-310.pyc
│     │        │  │  ├─ _models.cpython-310.pyc
│     │        │  │  ├─ _ssl.cpython-310.pyc
│     │        │  │  ├─ _synchronization.cpython-310.pyc
│     │        │  │  ├─ _trace.cpython-310.pyc
│     │        │  │  └─ _utils.cpython-310.pyc
│     │        │  ├─ _api.py
│     │        │  ├─ _async
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ connection.cpython-310.pyc
│     │        │  │  │  ├─ connection_pool.cpython-310.pyc
│     │        │  │  │  ├─ http11.cpython-310.pyc
│     │        │  │  │  ├─ http2.cpython-310.pyc
│     │        │  │  │  ├─ http_proxy.cpython-310.pyc
│     │        │  │  │  ├─ interfaces.cpython-310.pyc
│     │        │  │  │  └─ socks_proxy.cpython-310.pyc
│     │        │  │  ├─ connection.py
│     │        │  │  ├─ connection_pool.py
│     │        │  │  ├─ http11.py
│     │        │  │  ├─ http2.py
│     │        │  │  ├─ http_proxy.py
│     │        │  │  ├─ interfaces.py
│     │        │  │  └─ socks_proxy.py
│     │        │  ├─ _exceptions.py
│     │        │  ├─ _models.py
│     │        │  ├─ _ssl.py
│     │        │  ├─ _sync
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ connection.cpython-310.pyc
│     │        │  │  │  ├─ connection_pool.cpython-310.pyc
│     │        │  │  │  ├─ http11.cpython-310.pyc
│     │        │  │  │  ├─ http2.cpython-310.pyc
│     │        │  │  │  ├─ http_proxy.cpython-310.pyc
│     │        │  │  │  ├─ interfaces.cpython-310.pyc
│     │        │  │  │  └─ socks_proxy.cpython-310.pyc
│     │        │  │  ├─ connection.py
│     │        │  │  ├─ connection_pool.py
│     │        │  │  ├─ http11.py
│     │        │  │  ├─ http2.py
│     │        │  │  ├─ http_proxy.py
│     │        │  │  ├─ interfaces.py
│     │        │  │  └─ socks_proxy.py
│     │        │  ├─ _synchronization.py
│     │        │  ├─ _trace.py
│     │        │  ├─ _utils.py
│     │        │  ├─ backends
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asyncio.cpython-310.pyc
│     │        │  │  │  ├─ auto.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ mock.cpython-310.pyc
│     │        │  │  │  ├─ sync.cpython-310.pyc
│     │        │  │  │  └─ trio.cpython-310.pyc
│     │        │  │  ├─ asyncio.py
│     │        │  │  ├─ auto.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ mock.py
│     │        │  │  ├─ sync.py
│     │        │  │  └─ trio.py
│     │        │  └─ py.typed
│     │        ├─ httpcore-0.17.2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.md
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ httptools
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  └─ _version.cpython-310.pyc
│     │        │  ├─ _version.py
│     │        │  └─ parser
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  └─ errors.cpython-310.pyc
│     │        │     ├─ errors.py
│     │        │     ├─ parser.c
│     │        │     ├─ parser.cpython-310-x86_64-linux-gnu.so
│     │        │     ├─ url_parser.c
│     │        │     └─ url_parser.cpython-310-x86_64-linux-gnu.so
│     │        ├─ httptools-0.5.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ httpx
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __version__.cpython-310.pyc
│     │        │  │  ├─ _api.cpython-310.pyc
│     │        │  │  ├─ _auth.cpython-310.pyc
│     │        │  │  ├─ _client.cpython-310.pyc
│     │        │  │  ├─ _compat.cpython-310.pyc
│     │        │  │  ├─ _config.cpython-310.pyc
│     │        │  │  ├─ _content.cpython-310.pyc
│     │        │  │  ├─ _decoders.cpython-310.pyc
│     │        │  │  ├─ _exceptions.cpython-310.pyc
│     │        │  │  ├─ _main.cpython-310.pyc
│     │        │  │  ├─ _models.cpython-310.pyc
│     │        │  │  ├─ _multipart.cpython-310.pyc
│     │        │  │  ├─ _status_codes.cpython-310.pyc
│     │        │  │  ├─ _types.cpython-310.pyc
│     │        │  │  ├─ _urlparse.cpython-310.pyc
│     │        │  │  ├─ _urls.cpython-310.pyc
│     │        │  │  └─ _utils.cpython-310.pyc
│     │        │  ├─ __version__.py
│     │        │  ├─ _api.py
│     │        │  ├─ _auth.py
│     │        │  ├─ _client.py
│     │        │  ├─ _compat.py
│     │        │  ├─ _config.py
│     │        │  ├─ _content.py
│     │        │  ├─ _decoders.py
│     │        │  ├─ _exceptions.py
│     │        │  ├─ _main.py
│     │        │  ├─ _models.py
│     │        │  ├─ _multipart.py
│     │        │  ├─ _status_codes.py
│     │        │  ├─ _transports
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asgi.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ default.cpython-310.pyc
│     │        │  │  │  ├─ mock.cpython-310.pyc
│     │        │  │  │  └─ wsgi.cpython-310.pyc
│     │        │  │  ├─ asgi.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ default.py
│     │        │  │  ├─ mock.py
│     │        │  │  └─ wsgi.py
│     │        │  ├─ _types.py
│     │        │  ├─ _urlparse.py
│     │        │  ├─ _urls.py
│     │        │  ├─ _utils.py
│     │        │  └─ py.typed
│     │        ├─ httpx-0.24.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ licenses
│     │        │     └─ LICENSE.md
│     │        ├─ idna
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ codec.cpython-310.pyc
│     │        │  │  ├─ compat.cpython-310.pyc
│     │        │  │  ├─ core.cpython-310.pyc
│     │        │  │  ├─ idnadata.cpython-310.pyc
│     │        │  │  ├─ intranges.cpython-310.pyc
│     │        │  │  ├─ package_data.cpython-310.pyc
│     │        │  │  └─ uts46data.cpython-310.pyc
│     │        │  ├─ codec.py
│     │        │  ├─ compat.py
│     │        │  ├─ core.py
│     │        │  ├─ idnadata.py
│     │        │  ├─ intranges.py
│     │        │  ├─ package_data.py
│     │        │  ├─ py.typed
│     │        │  └─ uts46data.py
│     │        ├─ idna-3.4.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.md
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ iniconfig
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _parse.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  └─ exceptions.cpython-310.pyc
│     │        │  ├─ _parse.py
│     │        │  ├─ _version.py
│     │        │  ├─ exceptions.py
│     │        │  └─ py.typed
│     │        ├─ iniconfig-2.0.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ licenses
│     │        │     └─ LICENSE
│     │        ├─ isort
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  ├─ api.cpython-310.pyc
│     │        │  │  ├─ comments.cpython-310.pyc
│     │        │  │  ├─ core.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ files.cpython-310.pyc
│     │        │  │  ├─ format.cpython-310.pyc
│     │        │  │  ├─ identify.cpython-310.pyc
│     │        │  │  ├─ io.cpython-310.pyc
│     │        │  │  ├─ literal.cpython-310.pyc
│     │        │  │  ├─ logo.cpython-310.pyc
│     │        │  │  ├─ main.cpython-310.pyc
│     │        │  │  ├─ output.cpython-310.pyc
│     │        │  │  ├─ parse.cpython-310.pyc
│     │        │  │  ├─ place.cpython-310.pyc
│     │        │  │  ├─ profiles.cpython-310.pyc
│     │        │  │  ├─ pylama_isort.cpython-310.pyc
│     │        │  │  ├─ sections.cpython-310.pyc
│     │        │  │  ├─ settings.cpython-310.pyc
│     │        │  │  ├─ setuptools_commands.cpython-310.pyc
│     │        │  │  ├─ sorting.cpython-310.pyc
│     │        │  │  ├─ utils.cpython-310.pyc
│     │        │  │  ├─ wrap.cpython-310.pyc
│     │        │  │  └─ wrap_modes.cpython-310.pyc
│     │        │  ├─ _vendored
│     │        │  │  └─ tomli
│     │        │  │     ├─ LICENSE
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ _parser.cpython-310.pyc
│     │        │  │     │  └─ _re.cpython-310.pyc
│     │        │  │     ├─ _parser.py
│     │        │  │     ├─ _re.py
│     │        │  │     └─ py.typed
│     │        │  ├─ _version.py
│     │        │  ├─ api.py
│     │        │  ├─ comments.py
│     │        │  ├─ core.py
│     │        │  ├─ deprecated
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ finders.cpython-310.pyc
│     │        │  │  └─ finders.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ files.py
│     │        │  ├─ format.py
│     │        │  ├─ identify.py
│     │        │  ├─ io.py
│     │        │  ├─ literal.py
│     │        │  ├─ logo.py
│     │        │  ├─ main.py
│     │        │  ├─ output.py
│     │        │  ├─ parse.py
│     │        │  ├─ place.py
│     │        │  ├─ profiles.py
│     │        │  ├─ py.typed
│     │        │  ├─ pylama_isort.py
│     │        │  ├─ sections.py
│     │        │  ├─ settings.py
│     │        │  ├─ setuptools_commands.py
│     │        │  ├─ sorting.py
│     │        │  ├─ stdlibs
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ all.cpython-310.pyc
│     │        │  │  │  ├─ py2.cpython-310.pyc
│     │        │  │  │  ├─ py27.cpython-310.pyc
│     │        │  │  │  ├─ py3.cpython-310.pyc
│     │        │  │  │  ├─ py310.cpython-310.pyc
│     │        │  │  │  ├─ py311.cpython-310.pyc
│     │        │  │  │  ├─ py36.cpython-310.pyc
│     │        │  │  │  ├─ py37.cpython-310.pyc
│     │        │  │  │  ├─ py38.cpython-310.pyc
│     │        │  │  │  └─ py39.cpython-310.pyc
│     │        │  │  ├─ all.py
│     │        │  │  ├─ py2.py
│     │        │  │  ├─ py27.py
│     │        │  │  ├─ py3.py
│     │        │  │  ├─ py310.py
│     │        │  │  ├─ py311.py
│     │        │  │  ├─ py36.py
│     │        │  │  ├─ py37.py
│     │        │  │  ├─ py38.py
│     │        │  │  └─ py39.py
│     │        │  ├─ utils.py
│     │        │  ├─ wrap.py
│     │        │  └─ wrap_modes.py
│     │        ├─ isort-5.12.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ entry_points.txt
│     │        ├─ jsbeautifier
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  └─ __version__.cpython-310.pyc
│     │        │  ├─ __version__.py
│     │        │  ├─ cli
│     │        │  │  ├─ __init__.py
│     │        │  │  └─ __pycache__
│     │        │  │     └─ __init__.cpython-310.pyc
│     │        │  ├─ core
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ directives.cpython-310.pyc
│     │        │  │  │  ├─ inputscanner.cpython-310.pyc
│     │        │  │  │  ├─ options.cpython-310.pyc
│     │        │  │  │  ├─ output.cpython-310.pyc
│     │        │  │  │  ├─ pattern.cpython-310.pyc
│     │        │  │  │  ├─ templatablepattern.cpython-310.pyc
│     │        │  │  │  ├─ token.cpython-310.pyc
│     │        │  │  │  ├─ tokenizer.cpython-310.pyc
│     │        │  │  │  ├─ tokenstream.cpython-310.pyc
│     │        │  │  │  └─ whitespacepattern.cpython-310.pyc
│     │        │  │  ├─ directives.py
│     │        │  │  ├─ inputscanner.py
│     │        │  │  ├─ options.py
│     │        │  │  ├─ output.py
│     │        │  │  ├─ pattern.py
│     │        │  │  ├─ templatablepattern.py
│     │        │  │  ├─ token.py
│     │        │  │  ├─ tokenizer.py
│     │        │  │  ├─ tokenstream.py
│     │        │  │  └─ whitespacepattern.py
│     │        │  ├─ javascript
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ acorn.cpython-310.pyc
│     │        │  │  │  ├─ beautifier.cpython-310.pyc
│     │        │  │  │  ├─ options.cpython-310.pyc
│     │        │  │  │  └─ tokenizer.cpython-310.pyc
│     │        │  │  ├─ acorn.py
│     │        │  │  ├─ beautifier.py
│     │        │  │  ├─ options.py
│     │        │  │  └─ tokenizer.py
│     │        │  ├─ tests
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ testindentation.cpython-310.pyc
│     │        │  │  ├─ generated
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  └─ tests.cpython-310.pyc
│     │        │  │  │  └─ tests.py
│     │        │  │  └─ testindentation.py
│     │        │  └─ unpackers
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ evalbased.cpython-310.pyc
│     │        │     │  ├─ javascriptobfuscator.cpython-310.pyc
│     │        │     │  ├─ myobfuscate.cpython-310.pyc
│     │        │     │  ├─ packer.cpython-310.pyc
│     │        │     │  └─ urlencode.cpython-310.pyc
│     │        │     ├─ evalbased.py
│     │        │     ├─ javascriptobfuscator.py
│     │        │     ├─ myobfuscate.py
│     │        │     ├─ packer.py
│     │        │     ├─ tests
│     │        │     │  ├─ __init__.py
│     │        │     │  ├─ __pycache__
│     │        │     │  │  ├─ __init__.cpython-310.pyc
│     │        │     │  │  ├─ testjavascriptobfuscator.cpython-310.pyc
│     │        │     │  │  ├─ testmyobfuscate.cpython-310.pyc
│     │        │     │  │  ├─ testpacker.cpython-310.pyc
│     │        │     │  │  └─ testurlencode.cpython-310.pyc
│     │        │     │  ├─ testjavascriptobfuscator.py
│     │        │     │  ├─ testmyobfuscate.py
│     │        │     │  ├─ testpacker.py
│     │        │     │  └─ testurlencode.py
│     │        │     └─ urlencode.py
│     │        ├─ jsbeautifier-1.14.8.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ litestar
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ _multipart.cpython-310.pyc
│     │        │  │  ├─ _parsers.cpython-310.pyc
│     │        │  │  ├─ app.cpython-310.pyc
│     │        │  │  ├─ background_tasks.cpython-310.pyc
│     │        │  │  ├─ constants.cpython-310.pyc
│     │        │  │  ├─ controller.cpython-310.pyc
│     │        │  │  ├─ data_extractors.cpython-310.pyc
│     │        │  │  ├─ di.cpython-310.pyc
│     │        │  │  ├─ enums.cpython-310.pyc
│     │        │  │  ├─ file_system.cpython-310.pyc
│     │        │  │  ├─ pagination.cpython-310.pyc
│     │        │  │  ├─ params.cpython-310.pyc
│     │        │  │  ├─ partial.cpython-310.pyc
│     │        │  │  ├─ plugins.cpython-310.pyc
│     │        │  │  ├─ router.cpython-310.pyc
│     │        │  │  ├─ serialization.cpython-310.pyc
│     │        │  │  ├─ status_codes.cpython-310.pyc
│     │        │  │  └─ typing.cpython-310.pyc
│     │        │  ├─ _asgi
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asgi_router.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  ├─ asgi_router.py
│     │        │  │  ├─ routing_trie
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ mapping.cpython-310.pyc
│     │        │  │  │  │  ├─ traversal.cpython-310.pyc
│     │        │  │  │  │  ├─ types.cpython-310.pyc
│     │        │  │  │  │  └─ validate.cpython-310.pyc
│     │        │  │  │  ├─ mapping.py
│     │        │  │  │  ├─ traversal.py
│     │        │  │  │  ├─ types.py
│     │        │  │  │  └─ validate.py
│     │        │  │  └─ utils.py
│     │        │  ├─ _kwargs
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cleanup.cpython-310.pyc
│     │        │  │  │  ├─ dependencies.cpython-310.pyc
│     │        │  │  │  ├─ extractors.cpython-310.pyc
│     │        │  │  │  ├─ kwargs_model.cpython-310.pyc
│     │        │  │  │  └─ parameter_definition.cpython-310.pyc
│     │        │  │  ├─ cleanup.py
│     │        │  │  ├─ dependencies.py
│     │        │  │  ├─ extractors.py
│     │        │  │  ├─ kwargs_model.py
│     │        │  │  └─ parameter_definition.py
│     │        │  ├─ _layers
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  └─ utils.py
│     │        │  ├─ _multipart.py
│     │        │  ├─ _openapi
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ parameters.cpython-310.pyc
│     │        │  │  │  ├─ path_item.cpython-310.pyc
│     │        │  │  │  ├─ request_body.cpython-310.pyc
│     │        │  │  │  ├─ responses.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  ├─ parameters.py
│     │        │  │  ├─ path_item.py
│     │        │  │  ├─ request_body.py
│     │        │  │  ├─ responses.py
│     │        │  │  ├─ schema_generation
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ constrained_fields.cpython-310.pyc
│     │        │  │  │  │  ├─ examples.cpython-310.pyc
│     │        │  │  │  │  ├─ schema.cpython-310.pyc
│     │        │  │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  │  ├─ constrained_fields.py
│     │        │  │  │  ├─ examples.py
│     │        │  │  │  ├─ schema.py
│     │        │  │  │  └─ utils.py
│     │        │  │  ├─ typescript_converter
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ converter.cpython-310.pyc
│     │        │  │  │  │  ├─ schema_parsing.cpython-310.pyc
│     │        │  │  │  │  └─ types.cpython-310.pyc
│     │        │  │  │  ├─ converter.py
│     │        │  │  │  ├─ schema_parsing.py
│     │        │  │  │  └─ types.py
│     │        │  │  └─ utils.py
│     │        │  ├─ _parsers.py
│     │        │  ├─ _signature
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ field.cpython-310.pyc
│     │        │  │  │  ├─ metadata.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  ├─ field.py
│     │        │  │  ├─ metadata.py
│     │        │  │  ├─ models
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ attrs_signature_model.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  └─ pydantic_signature_model.cpython-310.pyc
│     │        │  │  │  ├─ attrs_signature_model.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  └─ pydantic_signature_model.py
│     │        │  │  └─ utils.py
│     │        │  ├─ app.py
│     │        │  ├─ background_tasks.py
│     │        │  ├─ channels
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ plugin.cpython-310.pyc
│     │        │  │  │  └─ subscriber.cpython-310.pyc
│     │        │  │  ├─ backends
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ memory.cpython-310.pyc
│     │        │  │  │  │  └─ redis.cpython-310.pyc
│     │        │  │  │  ├─ _redis_flushall_streams.lua
│     │        │  │  │  ├─ _redis_pubsub_publish.lua
│     │        │  │  │  ├─ _redis_xadd_expire.lua
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ memory.py
│     │        │  │  │  └─ redis.py
│     │        │  │  ├─ plugin.py
│     │        │  │  └─ subscriber.py
│     │        │  ├─ cli
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  │  └─ main.cpython-310.pyc
│     │        │  │  ├─ _utils.py
│     │        │  │  ├─ commands
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ core.cpython-310.pyc
│     │        │  │  │  │  ├─ schema.cpython-310.pyc
│     │        │  │  │  │  └─ sessions.cpython-310.pyc
│     │        │  │  │  ├─ core.py
│     │        │  │  │  ├─ schema.py
│     │        │  │  │  └─ sessions.py
│     │        │  │  └─ main.py
│     │        │  ├─ config
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ allowed_hosts.cpython-310.pyc
│     │        │  │  │  ├─ app.cpython-310.pyc
│     │        │  │  │  ├─ compression.cpython-310.pyc
│     │        │  │  │  ├─ cors.cpython-310.pyc
│     │        │  │  │  ├─ csrf.cpython-310.pyc
│     │        │  │  │  └─ response_cache.cpython-310.pyc
│     │        │  │  ├─ allowed_hosts.py
│     │        │  │  ├─ app.py
│     │        │  │  ├─ compression.py
│     │        │  │  ├─ cors.py
│     │        │  │  ├─ csrf.py
│     │        │  │  └─ response_cache.py
│     │        │  ├─ connection
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ request.cpython-310.pyc
│     │        │  │  │  └─ websocket.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ request.py
│     │        │  │  └─ websocket.py
│     │        │  ├─ constants.py
│     │        │  ├─ contrib
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ jinja.cpython-310.pyc
│     │        │  │  │  ├─ mako.cpython-310.pyc
│     │        │  │  │  ├─ msgspec.cpython-310.pyc
│     │        │  │  │  └─ pydantic.cpython-310.pyc
│     │        │  │  ├─ htmx
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  │  │  ├─ request.cpython-310.pyc
│     │        │  │  │  │  ├─ response.cpython-310.pyc
│     │        │  │  │  │  └─ types.cpython-310.pyc
│     │        │  │  │  ├─ _utils.py
│     │        │  │  │  ├─ request.py
│     │        │  │  │  ├─ response.py
│     │        │  │  │  └─ types.py
│     │        │  │  ├─ jinja.py
│     │        │  │  ├─ jwt
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ jwt_auth.cpython-310.pyc
│     │        │  │  │  │  ├─ jwt_token.cpython-310.pyc
│     │        │  │  │  │  └─ middleware.cpython-310.pyc
│     │        │  │  │  ├─ jwt_auth.py
│     │        │  │  │  ├─ jwt_token.py
│     │        │  │  │  └─ middleware.py
│     │        │  │  ├─ mako.py
│     │        │  │  ├─ msgspec.py
│     │        │  │  ├─ opentelemetry
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  │  └─ middleware.cpython-310.pyc
│     │        │  │  │  ├─ _utils.py
│     │        │  │  │  ├─ config.py
│     │        │  │  │  └─ middleware.py
│     │        │  │  ├─ prometheus
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  │  ├─ controller.cpython-310.pyc
│     │        │  │  │  │  └─ middleware.cpython-310.pyc
│     │        │  │  │  ├─ config.py
│     │        │  │  │  ├─ controller.py
│     │        │  │  │  └─ middleware.py
│     │        │  │  ├─ pydantic.py
│     │        │  │  ├─ repository
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  │  │  ├─ filters.cpython-310.pyc
│     │        │  │  │  │  └─ handlers.cpython-310.pyc
│     │        │  │  │  ├─ abc
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ _async.cpython-310.pyc
│     │        │  │  │  │  │  └─ _sync.cpython-310.pyc
│     │        │  │  │  │  ├─ _async.py
│     │        │  │  │  │  └─ _sync.py
│     │        │  │  │  ├─ exceptions.py
│     │        │  │  │  ├─ filters.py
│     │        │  │  │  ├─ handlers.py
│     │        │  │  │  └─ testing
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     ├─ __pycache__
│     │        │  │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │  │     │  └─ generic_mock_repository.cpython-310.pyc
│     │        │  │  │     └─ generic_mock_repository.py
│     │        │  │  └─ sqlalchemy
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ base.cpython-310.pyc
│     │        │  │     │  ├─ dto.cpython-310.pyc
│     │        │  │     │  └─ types.cpython-310.pyc
│     │        │  │     ├─ base.py
│     │        │  │     ├─ dto.py
│     │        │  │     ├─ plugins
│     │        │  │     │  ├─ __init__.py
│     │        │  │     │  ├─ __pycache__
│     │        │  │     │  │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  │  ├─ _slots_base.cpython-310.pyc
│     │        │  │     │  │  └─ serialization.cpython-310.pyc
│     │        │  │     │  ├─ _slots_base.py
│     │        │  │     │  ├─ init
│     │        │  │     │  │  ├─ __init__.py
│     │        │  │     │  │  ├─ __pycache__
│     │        │  │     │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  │  │  └─ plugin.cpython-310.pyc
│     │        │  │     │  │  ├─ config
│     │        │  │     │  │  │  ├─ __init__.py
│     │        │  │     │  │  │  ├─ __pycache__
│     │        │  │     │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  │  │  │  ├─ asyncio.cpython-310.pyc
│     │        │  │     │  │  │  │  ├─ common.cpython-310.pyc
│     │        │  │     │  │  │  │  ├─ engine.cpython-310.pyc
│     │        │  │     │  │  │  │  └─ sync.cpython-310.pyc
│     │        │  │     │  │  │  ├─ asyncio.py
│     │        │  │     │  │  │  ├─ common.py
│     │        │  │     │  │  │  ├─ engine.py
│     │        │  │     │  │  │  └─ sync.py
│     │        │  │     │  │  └─ plugin.py
│     │        │  │     │  └─ serialization.py
│     │        │  │     ├─ repository
│     │        │  │     │  ├─ __init__.py
│     │        │  │     │  ├─ __pycache__
│     │        │  │     │  │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  │  ├─ _async.cpython-310.pyc
│     │        │  │     │  │  ├─ _sync.cpython-310.pyc
│     │        │  │     │  │  ├─ _util.cpython-310.pyc
│     │        │  │     │  │  └─ types.cpython-310.pyc
│     │        │  │     │  ├─ _async.py
│     │        │  │     │  ├─ _sync.py
│     │        │  │     │  ├─ _util.py
│     │        │  │     │  └─ types.py
│     │        │  │     └─ types.py
│     │        │  ├─ controller.py
│     │        │  ├─ data_extractors.py
│     │        │  ├─ datastructures
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cookie.cpython-310.pyc
│     │        │  │  │  ├─ headers.cpython-310.pyc
│     │        │  │  │  ├─ multi_dicts.cpython-310.pyc
│     │        │  │  │  ├─ response_header.cpython-310.pyc
│     │        │  │  │  ├─ state.cpython-310.pyc
│     │        │  │  │  ├─ upload_file.cpython-310.pyc
│     │        │  │  │  └─ url.cpython-310.pyc
│     │        │  │  ├─ cookie.py
│     │        │  │  ├─ headers.py
│     │        │  │  ├─ multi_dicts.py
│     │        │  │  ├─ response_header.py
│     │        │  │  ├─ state.py
│     │        │  │  ├─ upload_file.py
│     │        │  │  └─ url.py
│     │        │  ├─ di.py
│     │        │  ├─ dto
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ interface.cpython-310.pyc
│     │        │  │  │  └─ types.cpython-310.pyc
│     │        │  │  ├─ factory
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ abc.cpython-310.pyc
│     │        │  │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  │  ├─ data_structures.cpython-310.pyc
│     │        │  │  │  │  ├─ exc.cpython-310.pyc
│     │        │  │  │  │  ├─ field.cpython-310.pyc
│     │        │  │  │  │  ├─ types.cpython-310.pyc
│     │        │  │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  │  ├─ _backends
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ abc.cpython-310.pyc
│     │        │  │  │  │  │  ├─ types.cpython-310.pyc
│     │        │  │  │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  │  │  ├─ abc.py
│     │        │  │  │  │  ├─ msgspec
│     │        │  │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  │  ├─ backend.cpython-310.pyc
│     │        │  │  │  │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  │  │  │  ├─ backend.py
│     │        │  │  │  │  │  └─ utils.py
│     │        │  │  │  │  ├─ pydantic
│     │        │  │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  │  ├─ backend.cpython-310.pyc
│     │        │  │  │  │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  │  │  │  ├─ backend.py
│     │        │  │  │  │  │  └─ utils.py
│     │        │  │  │  │  ├─ types.py
│     │        │  │  │  │  └─ utils.py
│     │        │  │  │  ├─ abc.py
│     │        │  │  │  ├─ config.py
│     │        │  │  │  ├─ data_structures.py
│     │        │  │  │  ├─ exc.py
│     │        │  │  │  ├─ field.py
│     │        │  │  │  ├─ stdlib
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  └─ dataclass.cpython-310.pyc
│     │        │  │  │  │  └─ dataclass.py
│     │        │  │  │  ├─ types.py
│     │        │  │  │  └─ utils.py
│     │        │  │  ├─ interface.py
│     │        │  │  └─ types.py
│     │        │  ├─ enums.py
│     │        │  ├─ events
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ emitter.cpython-310.pyc
│     │        │  │  │  └─ listener.cpython-310.pyc
│     │        │  │  ├─ emitter.py
│     │        │  │  └─ listener.py
│     │        │  ├─ exceptions
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base_exceptions.cpython-310.pyc
│     │        │  │  │  ├─ http_exceptions.cpython-310.pyc
│     │        │  │  │  └─ websocket_exceptions.cpython-310.pyc
│     │        │  │  ├─ base_exceptions.py
│     │        │  │  ├─ http_exceptions.py
│     │        │  │  └─ websocket_exceptions.py
│     │        │  ├─ file_system.py
│     │        │  ├─ handlers
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asgi_handlers.cpython-310.pyc
│     │        │  │  │  └─ base.cpython-310.pyc
│     │        │  │  ├─ asgi_handlers.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ http_handlers
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  └─ decorators.cpython-310.pyc
│     │        │  │  │  ├─ _utils.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  └─ decorators.py
│     │        │  │  └─ websocket_handlers
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ _utils.cpython-310.pyc
│     │        │  │     │  ├─ listener.cpython-310.pyc
│     │        │  │     │  └─ route_handler.cpython-310.pyc
│     │        │  │     ├─ _utils.py
│     │        │  │     ├─ listener.py
│     │        │  │     └─ route_handler.py
│     │        │  ├─ logging
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  ├─ picologging.cpython-310.pyc
│     │        │  │  │  └─ standard.cpython-310.pyc
│     │        │  │  ├─ _utils.py
│     │        │  │  ├─ config.py
│     │        │  │  ├─ picologging.py
│     │        │  │  └─ standard.py
│     │        │  ├─ middleware
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  │  ├─ allowed_hosts.cpython-310.pyc
│     │        │  │  │  ├─ authentication.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ compression.cpython-310.pyc
│     │        │  │  │  ├─ cors.cpython-310.pyc
│     │        │  │  │  ├─ csrf.cpython-310.pyc
│     │        │  │  │  ├─ logging.cpython-310.pyc
│     │        │  │  │  └─ rate_limit.cpython-310.pyc
│     │        │  │  ├─ _utils.py
│     │        │  │  ├─ allowed_hosts.py
│     │        │  │  ├─ authentication.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ compression.py
│     │        │  │  ├─ cors.py
│     │        │  │  ├─ csrf.py
│     │        │  │  ├─ exceptions
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _debug_response.cpython-310.pyc
│     │        │  │  │  │  └─ middleware.cpython-310.pyc
│     │        │  │  │  ├─ _debug_response.py
│     │        │  │  │  ├─ middleware.py
│     │        │  │  │  └─ templates
│     │        │  │  │     ├─ body.html
│     │        │  │  │     ├─ frame.html
│     │        │  │  │     ├─ scripts.js
│     │        │  │  │     └─ styles.css
│     │        │  │  ├─ logging.py
│     │        │  │  ├─ rate_limit.py
│     │        │  │  └─ session
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ base.cpython-310.pyc
│     │        │  │     │  ├─ client_side.cpython-310.pyc
│     │        │  │     │  └─ server_side.cpython-310.pyc
│     │        │  │     ├─ base.py
│     │        │  │     ├─ client_side.py
│     │        │  │     └─ server_side.py
│     │        │  ├─ openapi
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  ├─ controller.cpython-310.pyc
│     │        │  │  │  └─ datastructures.cpython-310.pyc
│     │        │  │  ├─ config.py
│     │        │  │  ├─ controller.py
│     │        │  │  ├─ datastructures.py
│     │        │  │  └─ spec
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ base.cpython-310.pyc
│     │        │  │     │  ├─ callback.cpython-310.pyc
│     │        │  │     │  ├─ components.cpython-310.pyc
│     │        │  │     │  ├─ contact.cpython-310.pyc
│     │        │  │     │  ├─ discriminator.cpython-310.pyc
│     │        │  │     │  ├─ encoding.cpython-310.pyc
│     │        │  │     │  ├─ enums.cpython-310.pyc
│     │        │  │     │  ├─ example.cpython-310.pyc
│     │        │  │     │  ├─ external_documentation.cpython-310.pyc
│     │        │  │     │  ├─ header.cpython-310.pyc
│     │        │  │     │  ├─ info.cpython-310.pyc
│     │        │  │     │  ├─ license.cpython-310.pyc
│     │        │  │     │  ├─ link.cpython-310.pyc
│     │        │  │     │  ├─ media_type.cpython-310.pyc
│     │        │  │     │  ├─ oauth_flow.cpython-310.pyc
│     │        │  │     │  ├─ oauth_flows.cpython-310.pyc
│     │        │  │     │  ├─ open_api.cpython-310.pyc
│     │        │  │     │  ├─ operation.cpython-310.pyc
│     │        │  │     │  ├─ parameter.cpython-310.pyc
│     │        │  │     │  ├─ path_item.cpython-310.pyc
│     │        │  │     │  ├─ paths.cpython-310.pyc
│     │        │  │     │  ├─ reference.cpython-310.pyc
│     │        │  │     │  ├─ request_body.cpython-310.pyc
│     │        │  │     │  ├─ response.cpython-310.pyc
│     │        │  │     │  ├─ responses.cpython-310.pyc
│     │        │  │     │  ├─ schema.cpython-310.pyc
│     │        │  │     │  ├─ security_requirement.cpython-310.pyc
│     │        │  │     │  ├─ security_scheme.cpython-310.pyc
│     │        │  │     │  ├─ server.cpython-310.pyc
│     │        │  │     │  ├─ server_variable.cpython-310.pyc
│     │        │  │     │  ├─ tag.cpython-310.pyc
│     │        │  │     │  └─ xml.cpython-310.pyc
│     │        │  │     ├─ base.py
│     │        │  │     ├─ callback.py
│     │        │  │     ├─ components.py
│     │        │  │     ├─ contact.py
│     │        │  │     ├─ discriminator.py
│     │        │  │     ├─ encoding.py
│     │        │  │     ├─ enums.py
│     │        │  │     ├─ example.py
│     │        │  │     ├─ external_documentation.py
│     │        │  │     ├─ header.py
│     │        │  │     ├─ info.py
│     │        │  │     ├─ license.py
│     │        │  │     ├─ link.py
│     │        │  │     ├─ media_type.py
│     │        │  │     ├─ oauth_flow.py
│     │        │  │     ├─ oauth_flows.py
│     │        │  │     ├─ open_api.py
│     │        │  │     ├─ operation.py
│     │        │  │     ├─ parameter.py
│     │        │  │     ├─ path_item.py
│     │        │  │     ├─ paths.py
│     │        │  │     ├─ reference.py
│     │        │  │     ├─ request_body.py
│     │        │  │     ├─ response.py
│     │        │  │     ├─ responses.py
│     │        │  │     ├─ schema.py
│     │        │  │     ├─ security_requirement.py
│     │        │  │     ├─ security_scheme.py
│     │        │  │     ├─ server.py
│     │        │  │     ├─ server_variable.py
│     │        │  │     ├─ tag.py
│     │        │  │     └─ xml.py
│     │        │  ├─ pagination.py
│     │        │  ├─ params.py
│     │        │  ├─ partial.py
│     │        │  ├─ plugins.py
│     │        │  ├─ py.typed
│     │        │  ├─ response
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ file.cpython-310.pyc
│     │        │  │  │  ├─ redirect.cpython-310.pyc
│     │        │  │  │  ├─ streaming.cpython-310.pyc
│     │        │  │  │  └─ template.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ file.py
│     │        │  │  ├─ redirect.py
│     │        │  │  ├─ streaming.py
│     │        │  │  └─ template.py
│     │        │  ├─ router.py
│     │        │  ├─ routes
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asgi.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ http.cpython-310.pyc
│     │        │  │  │  └─ websocket.cpython-310.pyc
│     │        │  │  ├─ asgi.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ http.py
│     │        │  │  └─ websocket.py
│     │        │  ├─ security
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ base.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  └─ session_auth
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ auth.cpython-310.pyc
│     │        │  │     │  └─ middleware.cpython-310.pyc
│     │        │  │     ├─ auth.py
│     │        │  │     └─ middleware.py
│     │        │  ├─ serialization.py
│     │        │  ├─ static_files
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  └─ config.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  └─ config.py
│     │        │  ├─ status_codes.py
│     │        │  ├─ stores
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ file.cpython-310.pyc
│     │        │  │  │  ├─ memory.cpython-310.pyc
│     │        │  │  │  ├─ redis.cpython-310.pyc
│     │        │  │  │  └─ registry.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ file.py
│     │        │  │  ├─ memory.py
│     │        │  │  ├─ redis.py
│     │        │  │  └─ registry.py
│     │        │  ├─ template
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  └─ config.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  └─ config.py
│     │        │  ├─ testing
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ helpers.cpython-310.pyc
│     │        │  │  │  ├─ life_span_handler.cpython-310.pyc
│     │        │  │  │  ├─ request_factory.cpython-310.pyc
│     │        │  │  │  ├─ transport.cpython-310.pyc
│     │        │  │  │  └─ websocket_test_session.cpython-310.pyc
│     │        │  │  ├─ client
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ async_client.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  └─ sync_client.cpython-310.pyc
│     │        │  │  │  ├─ async_client.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  └─ sync_client.py
│     │        │  │  ├─ helpers.py
│     │        │  │  ├─ life_span_handler.py
│     │        │  │  ├─ request_factory.py
│     │        │  │  ├─ transport.py
│     │        │  │  └─ websocket_test_session.py
│     │        │  ├─ types
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asgi_types.cpython-310.pyc
│     │        │  │  │  ├─ builtin_types.cpython-310.pyc
│     │        │  │  │  ├─ callable_types.cpython-310.pyc
│     │        │  │  │  ├─ composite_types.cpython-310.pyc
│     │        │  │  │  ├─ empty.cpython-310.pyc
│     │        │  │  │  ├─ file_types.cpython-310.pyc
│     │        │  │  │  ├─ helper_types.cpython-310.pyc
│     │        │  │  │  ├─ internal_types.cpython-310.pyc
│     │        │  │  │  ├─ protocols.cpython-310.pyc
│     │        │  │  │  └─ serialization.cpython-310.pyc
│     │        │  │  ├─ asgi_types.py
│     │        │  │  ├─ builtin_types.py
│     │        │  │  ├─ callable_types.py
│     │        │  │  ├─ composite_types.py
│     │        │  │  ├─ empty.py
│     │        │  │  ├─ file_types.py
│     │        │  │  ├─ helper_types.py
│     │        │  │  ├─ internal_types.py
│     │        │  │  ├─ protocols.py
│     │        │  │  └─ serialization.py
│     │        │  ├─ typing.py
│     │        │  └─ utils
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ compat.cpython-310.pyc
│     │        │     │  ├─ dataclass.cpython-310.pyc
│     │        │     │  ├─ deprecation.cpython-310.pyc
│     │        │     │  ├─ helpers.cpython-310.pyc
│     │        │     │  ├─ path.cpython-310.pyc
│     │        │     │  ├─ predicates.cpython-310.pyc
│     │        │     │  ├─ scope.cpython-310.pyc
│     │        │     │  ├─ sequence.cpython-310.pyc
│     │        │     │  ├─ signature.cpython-310.pyc
│     │        │     │  ├─ sync.cpython-310.pyc
│     │        │     │  ├─ typing.cpython-310.pyc
│     │        │     │  ├─ version.cpython-310.pyc
│     │        │     │  └─ warnings.cpython-310.pyc
│     │        │     ├─ compat.py
│     │        │     ├─ dataclass.py
│     │        │     ├─ deprecation.py
│     │        │     ├─ helpers.py
│     │        │     ├─ path.py
│     │        │     ├─ predicates.py
│     │        │     ├─ scope.py
│     │        │     ├─ sequence.py
│     │        │     ├─ signature.py
│     │        │     ├─ sync.py
│     │        │     ├─ typing.py
│     │        │     ├─ version.py
│     │        │     └─ warnings.py
│     │        ├─ litestar-2.0.0b2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ entry_points.txt
│     │        ├─ mako
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _ast_util.cpython-310.pyc
│     │        │  │  ├─ ast.cpython-310.pyc
│     │        │  │  ├─ cache.cpython-310.pyc
│     │        │  │  ├─ cmd.cpython-310.pyc
│     │        │  │  ├─ codegen.cpython-310.pyc
│     │        │  │  ├─ compat.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ filters.cpython-310.pyc
│     │        │  │  ├─ lexer.cpython-310.pyc
│     │        │  │  ├─ lookup.cpython-310.pyc
│     │        │  │  ├─ parsetree.cpython-310.pyc
│     │        │  │  ├─ pygen.cpython-310.pyc
│     │        │  │  ├─ pyparser.cpython-310.pyc
│     │        │  │  ├─ runtime.cpython-310.pyc
│     │        │  │  ├─ template.cpython-310.pyc
│     │        │  │  └─ util.cpython-310.pyc
│     │        │  ├─ _ast_util.py
│     │        │  ├─ ast.py
│     │        │  ├─ cache.py
│     │        │  ├─ cmd.py
│     │        │  ├─ codegen.py
│     │        │  ├─ compat.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ ext
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ autohandler.cpython-310.pyc
│     │        │  │  │  ├─ babelplugin.cpython-310.pyc
│     │        │  │  │  ├─ beaker_cache.cpython-310.pyc
│     │        │  │  │  ├─ extract.cpython-310.pyc
│     │        │  │  │  ├─ linguaplugin.cpython-310.pyc
│     │        │  │  │  ├─ preprocessors.cpython-310.pyc
│     │        │  │  │  ├─ pygmentplugin.cpython-310.pyc
│     │        │  │  │  └─ turbogears.cpython-310.pyc
│     │        │  │  ├─ autohandler.py
│     │        │  │  ├─ babelplugin.py
│     │        │  │  ├─ beaker_cache.py
│     │        │  │  ├─ extract.py
│     │        │  │  ├─ linguaplugin.py
│     │        │  │  ├─ preprocessors.py
│     │        │  │  ├─ pygmentplugin.py
│     │        │  │  └─ turbogears.py
│     │        │  ├─ filters.py
│     │        │  ├─ lexer.py
│     │        │  ├─ lookup.py
│     │        │  ├─ parsetree.py
│     │        │  ├─ pygen.py
│     │        │  ├─ pyparser.py
│     │        │  ├─ runtime.py
│     │        │  ├─ template.py
│     │        │  ├─ testing
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _config.cpython-310.pyc
│     │        │  │  │  ├─ assertions.cpython-310.pyc
│     │        │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  ├─ exclusions.cpython-310.pyc
│     │        │  │  │  ├─ fixtures.cpython-310.pyc
│     │        │  │  │  └─ helpers.cpython-310.pyc
│     │        │  │  ├─ _config.py
│     │        │  │  ├─ assertions.py
│     │        │  │  ├─ config.py
│     │        │  │  ├─ exclusions.py
│     │        │  │  ├─ fixtures.py
│     │        │  │  └─ helpers.py
│     │        │  └─ util.py
│     │        ├─ markdown_it
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _compat.cpython-310.pyc
│     │        │  │  ├─ _punycode.cpython-310.pyc
│     │        │  │  ├─ main.cpython-310.pyc
│     │        │  │  ├─ parser_block.cpython-310.pyc
│     │        │  │  ├─ parser_core.cpython-310.pyc
│     │        │  │  ├─ parser_inline.cpython-310.pyc
│     │        │  │  ├─ renderer.cpython-310.pyc
│     │        │  │  ├─ ruler.cpython-310.pyc
│     │        │  │  ├─ token.cpython-310.pyc
│     │        │  │  ├─ tree.cpython-310.pyc
│     │        │  │  └─ utils.cpython-310.pyc
│     │        │  ├─ _compat.py
│     │        │  ├─ _punycode.py
│     │        │  ├─ cli
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ parse.cpython-310.pyc
│     │        │  │  └─ parse.py
│     │        │  ├─ common
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ entities.cpython-310.pyc
│     │        │  │  │  ├─ html_blocks.cpython-310.pyc
│     │        │  │  │  ├─ html_re.cpython-310.pyc
│     │        │  │  │  ├─ normalize_url.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  ├─ entities.py
│     │        │  │  ├─ html_blocks.py
│     │        │  │  ├─ html_re.py
│     │        │  │  ├─ normalize_url.py
│     │        │  │  └─ utils.py
│     │        │  ├─ helpers
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ parse_link_destination.cpython-310.pyc
│     │        │  │  │  ├─ parse_link_label.cpython-310.pyc
│     │        │  │  │  └─ parse_link_title.cpython-310.pyc
│     │        │  │  ├─ parse_link_destination.py
│     │        │  │  ├─ parse_link_label.py
│     │        │  │  └─ parse_link_title.py
│     │        │  ├─ main.py
│     │        │  ├─ parser_block.py
│     │        │  ├─ parser_core.py
│     │        │  ├─ parser_inline.py
│     │        │  ├─ port.yaml
│     │        │  ├─ presets
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ commonmark.cpython-310.pyc
│     │        │  │  │  ├─ default.cpython-310.pyc
│     │        │  │  │  └─ zero.cpython-310.pyc
│     │        │  │  ├─ commonmark.py
│     │        │  │  ├─ default.py
│     │        │  │  └─ zero.py
│     │        │  ├─ py.typed
│     │        │  ├─ renderer.py
│     │        │  ├─ ruler.py
│     │        │  ├─ rules_block
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ blockquote.cpython-310.pyc
│     │        │  │  │  ├─ code.cpython-310.pyc
│     │        │  │  │  ├─ fence.cpython-310.pyc
│     │        │  │  │  ├─ heading.cpython-310.pyc
│     │        │  │  │  ├─ hr.cpython-310.pyc
│     │        │  │  │  ├─ html_block.cpython-310.pyc
│     │        │  │  │  ├─ lheading.cpython-310.pyc
│     │        │  │  │  ├─ list.cpython-310.pyc
│     │        │  │  │  ├─ paragraph.cpython-310.pyc
│     │        │  │  │  ├─ reference.cpython-310.pyc
│     │        │  │  │  ├─ state_block.cpython-310.pyc
│     │        │  │  │  └─ table.cpython-310.pyc
│     │        │  │  ├─ blockquote.py
│     │        │  │  ├─ code.py
│     │        │  │  ├─ fence.py
│     │        │  │  ├─ heading.py
│     │        │  │  ├─ hr.py
│     │        │  │  ├─ html_block.py
│     │        │  │  ├─ lheading.py
│     │        │  │  ├─ list.py
│     │        │  │  ├─ paragraph.py
│     │        │  │  ├─ reference.py
│     │        │  │  ├─ state_block.py
│     │        │  │  └─ table.py
│     │        │  ├─ rules_core
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ block.cpython-310.pyc
│     │        │  │  │  ├─ inline.cpython-310.pyc
│     │        │  │  │  ├─ linkify.cpython-310.pyc
│     │        │  │  │  ├─ normalize.cpython-310.pyc
│     │        │  │  │  ├─ replacements.cpython-310.pyc
│     │        │  │  │  ├─ smartquotes.cpython-310.pyc
│     │        │  │  │  ├─ state_core.cpython-310.pyc
│     │        │  │  │  └─ text_join.cpython-310.pyc
│     │        │  │  ├─ block.py
│     │        │  │  ├─ inline.py
│     │        │  │  ├─ linkify.py
│     │        │  │  ├─ normalize.py
│     │        │  │  ├─ replacements.py
│     │        │  │  ├─ smartquotes.py
│     │        │  │  ├─ state_core.py
│     │        │  │  └─ text_join.py
│     │        │  ├─ rules_inline
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ autolink.cpython-310.pyc
│     │        │  │  │  ├─ backticks.cpython-310.pyc
│     │        │  │  │  ├─ balance_pairs.cpython-310.pyc
│     │        │  │  │  ├─ emphasis.cpython-310.pyc
│     │        │  │  │  ├─ entity.cpython-310.pyc
│     │        │  │  │  ├─ escape.cpython-310.pyc
│     │        │  │  │  ├─ fragments_join.cpython-310.pyc
│     │        │  │  │  ├─ html_inline.cpython-310.pyc
│     │        │  │  │  ├─ image.cpython-310.pyc
│     │        │  │  │  ├─ link.cpython-310.pyc
│     │        │  │  │  ├─ linkify.cpython-310.pyc
│     │        │  │  │  ├─ newline.cpython-310.pyc
│     │        │  │  │  ├─ state_inline.cpython-310.pyc
│     │        │  │  │  ├─ strikethrough.cpython-310.pyc
│     │        │  │  │  └─ text.cpython-310.pyc
│     │        │  │  ├─ autolink.py
│     │        │  │  ├─ backticks.py
│     │        │  │  ├─ balance_pairs.py
│     │        │  │  ├─ emphasis.py
│     │        │  │  ├─ entity.py
│     │        │  │  ├─ escape.py
│     │        │  │  ├─ fragments_join.py
│     │        │  │  ├─ html_inline.py
│     │        │  │  ├─ image.py
│     │        │  │  ├─ link.py
│     │        │  │  ├─ linkify.py
│     │        │  │  ├─ newline.py
│     │        │  │  ├─ state_inline.py
│     │        │  │  ├─ strikethrough.py
│     │        │  │  └─ text.py
│     │        │  ├─ token.py
│     │        │  ├─ tree.py
│     │        │  └─ utils.py
│     │        ├─ markdown_it_py-3.0.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ LICENSE.markdown-it
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ entry_points.txt
│     │        ├─ markupsafe
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  └─ _native.cpython-310.pyc
│     │        │  ├─ _native.py
│     │        │  ├─ _speedups.c
│     │        │  ├─ _speedups.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ _speedups.pyi
│     │        │  └─ py.typed
│     │        ├─ mdurl
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _decode.cpython-310.pyc
│     │        │  │  ├─ _encode.cpython-310.pyc
│     │        │  │  ├─ _format.cpython-310.pyc
│     │        │  │  ├─ _parse.cpython-310.pyc
│     │        │  │  └─ _url.cpython-310.pyc
│     │        │  ├─ _decode.py
│     │        │  ├─ _encode.py
│     │        │  ├─ _format.py
│     │        │  ├─ _parse.py
│     │        │  ├─ _url.py
│     │        │  └─ py.typed
│     │        ├─ mdurl-0.1.2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ msgspec
│     │        │  ├─ __init__.py
│     │        │  ├─ __init__.pyi
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _json_schema.cpython-310.pyc
│     │        │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  ├─ inspect.cpython-310.pyc
│     │        │  │  ├─ json.cpython-310.pyc
│     │        │  │  ├─ msgpack.cpython-310.pyc
│     │        │  │  ├─ structs.cpython-310.pyc
│     │        │  │  ├─ toml.cpython-310.pyc
│     │        │  │  └─ yaml.cpython-310.pyc
│     │        │  ├─ _core.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ _json_schema.py
│     │        │  ├─ _utils.py
│     │        │  ├─ _version.py
│     │        │  ├─ inspect.py
│     │        │  ├─ json.py
│     │        │  ├─ json.pyi
│     │        │  ├─ msgpack.py
│     │        │  ├─ msgpack.pyi
│     │        │  ├─ py.typed
│     │        │  ├─ structs.py
│     │        │  ├─ structs.pyi
│     │        │  ├─ toml.py
│     │        │  └─ yaml.py
│     │        ├─ msgspec-0.16.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ multidict
│     │        │  ├─ __init__.py
│     │        │  ├─ __init__.pyi
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _abc.cpython-310.pyc
│     │        │  │  ├─ _compat.cpython-310.pyc
│     │        │  │  ├─ _multidict_base.cpython-310.pyc
│     │        │  │  └─ _multidict_py.cpython-310.pyc
│     │        │  ├─ _abc.py
│     │        │  ├─ _compat.py
│     │        │  ├─ _multidict.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ _multidict_base.py
│     │        │  ├─ _multidict_py.py
│     │        │  └─ py.typed
│     │        ├─ multidict-6.0.4.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ mypy_extensions-1.0.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ mypy_extensions.py
│     │        ├─ packaging
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _elffile.cpython-310.pyc
│     │        │  │  ├─ _manylinux.cpython-310.pyc
│     │        │  │  ├─ _musllinux.cpython-310.pyc
│     │        │  │  ├─ _parser.cpython-310.pyc
│     │        │  │  ├─ _structures.cpython-310.pyc
│     │        │  │  ├─ _tokenizer.cpython-310.pyc
│     │        │  │  ├─ markers.cpython-310.pyc
│     │        │  │  ├─ metadata.cpython-310.pyc
│     │        │  │  ├─ requirements.cpython-310.pyc
│     │        │  │  ├─ specifiers.cpython-310.pyc
│     │        │  │  ├─ tags.cpython-310.pyc
│     │        │  │  ├─ utils.cpython-310.pyc
│     │        │  │  └─ version.cpython-310.pyc
│     │        │  ├─ _elffile.py
│     │        │  ├─ _manylinux.py
│     │        │  ├─ _musllinux.py
│     │        │  ├─ _parser.py
│     │        │  ├─ _structures.py
│     │        │  ├─ _tokenizer.py
│     │        │  ├─ markers.py
│     │        │  ├─ metadata.py
│     │        │  ├─ py.typed
│     │        │  ├─ requirements.py
│     │        │  ├─ specifiers.py
│     │        │  ├─ tags.py
│     │        │  ├─ utils.py
│     │        │  └─ version.py
│     │        ├─ packaging-23.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ LICENSE.APACHE
│     │        │  ├─ LICENSE.BSD
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ passlib
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ apache.cpython-310.pyc
│     │        │  │  ├─ apps.cpython-310.pyc
│     │        │  │  ├─ context.cpython-310.pyc
│     │        │  │  ├─ exc.cpython-310.pyc
│     │        │  │  ├─ hash.cpython-310.pyc
│     │        │  │  ├─ hosts.cpython-310.pyc
│     │        │  │  ├─ ifc.cpython-310.pyc
│     │        │  │  ├─ pwd.cpython-310.pyc
│     │        │  │  ├─ registry.cpython-310.pyc
│     │        │  │  ├─ totp.cpython-310.pyc
│     │        │  │  └─ win32.cpython-310.pyc
│     │        │  ├─ _data
│     │        │  │  └─ wordsets
│     │        │  │     ├─ bip39.txt
│     │        │  │     ├─ eff_long.txt
│     │        │  │     ├─ eff_prefixed.txt
│     │        │  │     └─ eff_short.txt
│     │        │  ├─ apache.py
│     │        │  ├─ apps.py
│     │        │  ├─ context.py
│     │        │  ├─ crypto
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _md4.cpython-310.pyc
│     │        │  │  │  ├─ des.cpython-310.pyc
│     │        │  │  │  └─ digest.cpython-310.pyc
│     │        │  │  ├─ _blowfish
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _gen_files.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  └─ unrolled.cpython-310.pyc
│     │        │  │  │  ├─ _gen_files.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  └─ unrolled.py
│     │        │  │  ├─ _md4.py
│     │        │  │  ├─ des.py
│     │        │  │  ├─ digest.py
│     │        │  │  └─ scrypt
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ _builtin.cpython-310.pyc
│     │        │  │     │  ├─ _gen_files.cpython-310.pyc
│     │        │  │     │  └─ _salsa.cpython-310.pyc
│     │        │  │     ├─ _builtin.py
│     │        │  │     ├─ _gen_files.py
│     │        │  │     └─ _salsa.py
│     │        │  ├─ exc.py
│     │        │  ├─ ext
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  └─ django
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ models.cpython-310.pyc
│     │        │  │     │  └─ utils.cpython-310.pyc
│     │        │  │     ├─ models.py
│     │        │  │     └─ utils.py
│     │        │  ├─ handlers
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ argon2.cpython-310.pyc
│     │        │  │  │  ├─ bcrypt.cpython-310.pyc
│     │        │  │  │  ├─ cisco.cpython-310.pyc
│     │        │  │  │  ├─ des_crypt.cpython-310.pyc
│     │        │  │  │  ├─ digests.cpython-310.pyc
│     │        │  │  │  ├─ django.cpython-310.pyc
│     │        │  │  │  ├─ fshp.cpython-310.pyc
│     │        │  │  │  ├─ ldap_digests.cpython-310.pyc
│     │        │  │  │  ├─ md5_crypt.cpython-310.pyc
│     │        │  │  │  ├─ misc.cpython-310.pyc
│     │        │  │  │  ├─ mssql.cpython-310.pyc
│     │        │  │  │  ├─ mysql.cpython-310.pyc
│     │        │  │  │  ├─ oracle.cpython-310.pyc
│     │        │  │  │  ├─ pbkdf2.cpython-310.pyc
│     │        │  │  │  ├─ phpass.cpython-310.pyc
│     │        │  │  │  ├─ postgres.cpython-310.pyc
│     │        │  │  │  ├─ roundup.cpython-310.pyc
│     │        │  │  │  ├─ scram.cpython-310.pyc
│     │        │  │  │  ├─ scrypt.cpython-310.pyc
│     │        │  │  │  ├─ sha1_crypt.cpython-310.pyc
│     │        │  │  │  ├─ sha2_crypt.cpython-310.pyc
│     │        │  │  │  ├─ sun_md5_crypt.cpython-310.pyc
│     │        │  │  │  └─ windows.cpython-310.pyc
│     │        │  │  ├─ argon2.py
│     │        │  │  ├─ bcrypt.py
│     │        │  │  ├─ cisco.py
│     │        │  │  ├─ des_crypt.py
│     │        │  │  ├─ digests.py
│     │        │  │  ├─ django.py
│     │        │  │  ├─ fshp.py
│     │        │  │  ├─ ldap_digests.py
│     │        │  │  ├─ md5_crypt.py
│     │        │  │  ├─ misc.py
│     │        │  │  ├─ mssql.py
│     │        │  │  ├─ mysql.py
│     │        │  │  ├─ oracle.py
│     │        │  │  ├─ pbkdf2.py
│     │        │  │  ├─ phpass.py
│     │        │  │  ├─ postgres.py
│     │        │  │  ├─ roundup.py
│     │        │  │  ├─ scram.py
│     │        │  │  ├─ scrypt.py
│     │        │  │  ├─ sha1_crypt.py
│     │        │  │  ├─ sha2_crypt.py
│     │        │  │  ├─ sun_md5_crypt.py
│     │        │  │  └─ windows.py
│     │        │  ├─ hash.py
│     │        │  ├─ hosts.py
│     │        │  ├─ ifc.py
│     │        │  ├─ pwd.py
│     │        │  ├─ registry.py
│     │        │  ├─ tests
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __main__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  │  ├─ _test_bad_register.cpython-310.pyc
│     │        │  │  │  ├─ backports.cpython-310.pyc
│     │        │  │  │  ├─ test_apache.cpython-310.pyc
│     │        │  │  │  ├─ test_apps.cpython-310.pyc
│     │        │  │  │  ├─ test_context.cpython-310.pyc
│     │        │  │  │  ├─ test_context_deprecated.cpython-310.pyc
│     │        │  │  │  ├─ test_crypto_builtin_md4.cpython-310.pyc
│     │        │  │  │  ├─ test_crypto_des.cpython-310.pyc
│     │        │  │  │  ├─ test_crypto_digest.cpython-310.pyc
│     │        │  │  │  ├─ test_crypto_scrypt.cpython-310.pyc
│     │        │  │  │  ├─ test_ext_django.cpython-310.pyc
│     │        │  │  │  ├─ test_ext_django_source.cpython-310.pyc
│     │        │  │  │  ├─ test_handlers.cpython-310.pyc
│     │        │  │  │  ├─ test_handlers_argon2.cpython-310.pyc
│     │        │  │  │  ├─ test_handlers_bcrypt.cpython-310.pyc
│     │        │  │  │  ├─ test_handlers_cisco.cpython-310.pyc
│     │        │  │  │  ├─ test_handlers_django.cpython-310.pyc
│     │        │  │  │  ├─ test_handlers_pbkdf2.cpython-310.pyc
│     │        │  │  │  ├─ test_handlers_scrypt.cpython-310.pyc
│     │        │  │  │  ├─ test_hosts.cpython-310.pyc
│     │        │  │  │  ├─ test_pwd.cpython-310.pyc
│     │        │  │  │  ├─ test_registry.cpython-310.pyc
│     │        │  │  │  ├─ test_totp.cpython-310.pyc
│     │        │  │  │  ├─ test_utils.cpython-310.pyc
│     │        │  │  │  ├─ test_utils_handlers.cpython-310.pyc
│     │        │  │  │  ├─ test_utils_md4.cpython-310.pyc
│     │        │  │  │  ├─ test_utils_pbkdf2.cpython-310.pyc
│     │        │  │  │  ├─ test_win32.cpython-310.pyc
│     │        │  │  │  ├─ tox_support.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  ├─ _test_bad_register.py
│     │        │  │  ├─ backports.py
│     │        │  │  ├─ sample1.cfg
│     │        │  │  ├─ sample1b.cfg
│     │        │  │  ├─ sample1c.cfg
│     │        │  │  ├─ sample_config_1s.cfg
│     │        │  │  ├─ test_apache.py
│     │        │  │  ├─ test_apps.py
│     │        │  │  ├─ test_context.py
│     │        │  │  ├─ test_context_deprecated.py
│     │        │  │  ├─ test_crypto_builtin_md4.py
│     │        │  │  ├─ test_crypto_des.py
│     │        │  │  ├─ test_crypto_digest.py
│     │        │  │  ├─ test_crypto_scrypt.py
│     │        │  │  ├─ test_ext_django.py
│     │        │  │  ├─ test_ext_django_source.py
│     │        │  │  ├─ test_handlers.py
│     │        │  │  ├─ test_handlers_argon2.py
│     │        │  │  ├─ test_handlers_bcrypt.py
│     │        │  │  ├─ test_handlers_cisco.py
│     │        │  │  ├─ test_handlers_django.py
│     │        │  │  ├─ test_handlers_pbkdf2.py
│     │        │  │  ├─ test_handlers_scrypt.py
│     │        │  │  ├─ test_hosts.py
│     │        │  │  ├─ test_pwd.py
│     │        │  │  ├─ test_registry.py
│     │        │  │  ├─ test_totp.py
│     │        │  │  ├─ test_utils.py
│     │        │  │  ├─ test_utils_handlers.py
│     │        │  │  ├─ test_utils_md4.py
│     │        │  │  ├─ test_utils_pbkdf2.py
│     │        │  │  ├─ test_win32.py
│     │        │  │  ├─ tox_support.py
│     │        │  │  └─ utils.py
│     │        │  ├─ totp.py
│     │        │  ├─ utils
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ binary.cpython-310.pyc
│     │        │  │  │  ├─ decor.cpython-310.pyc
│     │        │  │  │  ├─ des.cpython-310.pyc
│     │        │  │  │  ├─ handlers.cpython-310.pyc
│     │        │  │  │  ├─ md4.cpython-310.pyc
│     │        │  │  │  └─ pbkdf2.cpython-310.pyc
│     │        │  │  ├─ binary.py
│     │        │  │  ├─ compat
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  └─ _ordered_dict.cpython-310.pyc
│     │        │  │  │  └─ _ordered_dict.py
│     │        │  │  ├─ decor.py
│     │        │  │  ├─ des.py
│     │        │  │  ├─ handlers.py
│     │        │  │  ├─ md4.py
│     │        │  │  └─ pbkdf2.py
│     │        │  └─ win32.py
│     │        ├─ passlib-1.7.4.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ top_level.txt
│     │        │  └─ zip-safe
│     │        ├─ pathspec
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _meta.cpython-310.pyc
│     │        │  │  ├─ gitignore.cpython-310.pyc
│     │        │  │  ├─ pathspec.cpython-310.pyc
│     │        │  │  ├─ pattern.cpython-310.pyc
│     │        │  │  └─ util.cpython-310.pyc
│     │        │  ├─ _meta.py
│     │        │  ├─ gitignore.py
│     │        │  ├─ pathspec.py
│     │        │  ├─ pattern.py
│     │        │  ├─ patterns
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ gitwildmatch.cpython-310.pyc
│     │        │  │  └─ gitwildmatch.py
│     │        │  ├─ py.typed
│     │        │  └─ util.py
│     │        ├─ pathspec-0.11.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ pip
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pip-runner__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  └─ __pip-runner__.cpython-310.pyc
│     │        │  ├─ _internal
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ build_env.cpython-310.pyc
│     │        │  │  │  ├─ cache.cpython-310.pyc
│     │        │  │  │  ├─ configuration.cpython-310.pyc
│     │        │  │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  │  ├─ main.cpython-310.pyc
│     │        │  │  │  ├─ pyproject.cpython-310.pyc
│     │        │  │  │  ├─ self_outdated_check.cpython-310.pyc
│     │        │  │  │  └─ wheel_builder.cpython-310.pyc
│     │        │  │  ├─ build_env.py
│     │        │  │  ├─ cache.py
│     │        │  │  ├─ cli
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ autocompletion.cpython-310.pyc
│     │        │  │  │  │  ├─ base_command.cpython-310.pyc
│     │        │  │  │  │  ├─ cmdoptions.cpython-310.pyc
│     │        │  │  │  │  ├─ command_context.cpython-310.pyc
│     │        │  │  │  │  ├─ main.cpython-310.pyc
│     │        │  │  │  │  ├─ main_parser.cpython-310.pyc
│     │        │  │  │  │  ├─ parser.cpython-310.pyc
│     │        │  │  │  │  ├─ progress_bars.cpython-310.pyc
│     │        │  │  │  │  ├─ req_command.cpython-310.pyc
│     │        │  │  │  │  ├─ spinners.cpython-310.pyc
│     │        │  │  │  │  └─ status_codes.cpython-310.pyc
│     │        │  │  │  ├─ autocompletion.py
│     │        │  │  │  ├─ base_command.py
│     │        │  │  │  ├─ cmdoptions.py
│     │        │  │  │  ├─ command_context.py
│     │        │  │  │  ├─ main.py
│     │        │  │  │  ├─ main_parser.py
│     │        │  │  │  ├─ parser.py
│     │        │  │  │  ├─ progress_bars.py
│     │        │  │  │  ├─ req_command.py
│     │        │  │  │  ├─ spinners.py
│     │        │  │  │  └─ status_codes.py
│     │        │  │  ├─ commands
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ cache.cpython-310.pyc
│     │        │  │  │  │  ├─ check.cpython-310.pyc
│     │        │  │  │  │  ├─ completion.cpython-310.pyc
│     │        │  │  │  │  ├─ configuration.cpython-310.pyc
│     │        │  │  │  │  ├─ debug.cpython-310.pyc
│     │        │  │  │  │  ├─ download.cpython-310.pyc
│     │        │  │  │  │  ├─ freeze.cpython-310.pyc
│     │        │  │  │  │  ├─ hash.cpython-310.pyc
│     │        │  │  │  │  ├─ help.cpython-310.pyc
│     │        │  │  │  │  ├─ index.cpython-310.pyc
│     │        │  │  │  │  ├─ inspect.cpython-310.pyc
│     │        │  │  │  │  ├─ install.cpython-310.pyc
│     │        │  │  │  │  ├─ list.cpython-310.pyc
│     │        │  │  │  │  ├─ search.cpython-310.pyc
│     │        │  │  │  │  ├─ show.cpython-310.pyc
│     │        │  │  │  │  ├─ uninstall.cpython-310.pyc
│     │        │  │  │  │  └─ wheel.cpython-310.pyc
│     │        │  │  │  ├─ cache.py
│     │        │  │  │  ├─ check.py
│     │        │  │  │  ├─ completion.py
│     │        │  │  │  ├─ configuration.py
│     │        │  │  │  ├─ debug.py
│     │        │  │  │  ├─ download.py
│     │        │  │  │  ├─ freeze.py
│     │        │  │  │  ├─ hash.py
│     │        │  │  │  ├─ help.py
│     │        │  │  │  ├─ index.py
│     │        │  │  │  ├─ inspect.py
│     │        │  │  │  ├─ install.py
│     │        │  │  │  ├─ list.py
│     │        │  │  │  ├─ search.py
│     │        │  │  │  ├─ show.py
│     │        │  │  │  ├─ uninstall.py
│     │        │  │  │  └─ wheel.py
│     │        │  │  ├─ configuration.py
│     │        │  │  ├─ distributions
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ installed.cpython-310.pyc
│     │        │  │  │  │  ├─ sdist.cpython-310.pyc
│     │        │  │  │  │  └─ wheel.cpython-310.pyc
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ installed.py
│     │        │  │  │  ├─ sdist.py
│     │        │  │  │  └─ wheel.py
│     │        │  │  ├─ exceptions.py
│     │        │  │  ├─ index
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ collector.cpython-310.pyc
│     │        │  │  │  │  ├─ package_finder.cpython-310.pyc
│     │        │  │  │  │  └─ sources.cpython-310.pyc
│     │        │  │  │  ├─ collector.py
│     │        │  │  │  ├─ package_finder.py
│     │        │  │  │  └─ sources.py
│     │        │  │  ├─ locations
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _distutils.cpython-310.pyc
│     │        │  │  │  │  ├─ _sysconfig.cpython-310.pyc
│     │        │  │  │  │  └─ base.cpython-310.pyc
│     │        │  │  │  ├─ _distutils.py
│     │        │  │  │  ├─ _sysconfig.py
│     │        │  │  │  └─ base.py
│     │        │  │  ├─ main.py
│     │        │  │  ├─ metadata
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _json.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  └─ pkg_resources.cpython-310.pyc
│     │        │  │  │  ├─ _json.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ importlib
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ _compat.cpython-310.pyc
│     │        │  │  │  │  │  ├─ _dists.cpython-310.pyc
│     │        │  │  │  │  │  └─ _envs.cpython-310.pyc
│     │        │  │  │  │  ├─ _compat.py
│     │        │  │  │  │  ├─ _dists.py
│     │        │  │  │  │  └─ _envs.py
│     │        │  │  │  └─ pkg_resources.py
│     │        │  │  ├─ models
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ candidate.cpython-310.pyc
│     │        │  │  │  │  ├─ direct_url.cpython-310.pyc
│     │        │  │  │  │  ├─ format_control.cpython-310.pyc
│     │        │  │  │  │  ├─ index.cpython-310.pyc
│     │        │  │  │  │  ├─ installation_report.cpython-310.pyc
│     │        │  │  │  │  ├─ link.cpython-310.pyc
│     │        │  │  │  │  ├─ scheme.cpython-310.pyc
│     │        │  │  │  │  ├─ search_scope.cpython-310.pyc
│     │        │  │  │  │  ├─ selection_prefs.cpython-310.pyc
│     │        │  │  │  │  ├─ target_python.cpython-310.pyc
│     │        │  │  │  │  └─ wheel.cpython-310.pyc
│     │        │  │  │  ├─ candidate.py
│     │        │  │  │  ├─ direct_url.py
│     │        │  │  │  ├─ format_control.py
│     │        │  │  │  ├─ index.py
│     │        │  │  │  ├─ installation_report.py
│     │        │  │  │  ├─ link.py
│     │        │  │  │  ├─ scheme.py
│     │        │  │  │  ├─ search_scope.py
│     │        │  │  │  ├─ selection_prefs.py
│     │        │  │  │  ├─ target_python.py
│     │        │  │  │  └─ wheel.py
│     │        │  │  ├─ network
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ auth.cpython-310.pyc
│     │        │  │  │  │  ├─ cache.cpython-310.pyc
│     │        │  │  │  │  ├─ download.cpython-310.pyc
│     │        │  │  │  │  ├─ lazy_wheel.cpython-310.pyc
│     │        │  │  │  │  ├─ session.cpython-310.pyc
│     │        │  │  │  │  ├─ utils.cpython-310.pyc
│     │        │  │  │  │  └─ xmlrpc.cpython-310.pyc
│     │        │  │  │  ├─ auth.py
│     │        │  │  │  ├─ cache.py
│     │        │  │  │  ├─ download.py
│     │        │  │  │  ├─ lazy_wheel.py
│     │        │  │  │  ├─ session.py
│     │        │  │  │  ├─ utils.py
│     │        │  │  │  └─ xmlrpc.py
│     │        │  │  ├─ operations
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ check.cpython-310.pyc
│     │        │  │  │  │  ├─ freeze.cpython-310.pyc
│     │        │  │  │  │  └─ prepare.cpython-310.pyc
│     │        │  │  │  ├─ build
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ build_tracker.cpython-310.pyc
│     │        │  │  │  │  │  ├─ metadata.cpython-310.pyc
│     │        │  │  │  │  │  ├─ metadata_editable.cpython-310.pyc
│     │        │  │  │  │  │  ├─ metadata_legacy.cpython-310.pyc
│     │        │  │  │  │  │  ├─ wheel.cpython-310.pyc
│     │        │  │  │  │  │  ├─ wheel_editable.cpython-310.pyc
│     │        │  │  │  │  │  └─ wheel_legacy.cpython-310.pyc
│     │        │  │  │  │  ├─ build_tracker.py
│     │        │  │  │  │  ├─ metadata.py
│     │        │  │  │  │  ├─ metadata_editable.py
│     │        │  │  │  │  ├─ metadata_legacy.py
│     │        │  │  │  │  ├─ wheel.py
│     │        │  │  │  │  ├─ wheel_editable.py
│     │        │  │  │  │  └─ wheel_legacy.py
│     │        │  │  │  ├─ check.py
│     │        │  │  │  ├─ freeze.py
│     │        │  │  │  ├─ install
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ editable_legacy.cpython-310.pyc
│     │        │  │  │  │  │  └─ wheel.cpython-310.pyc
│     │        │  │  │  │  ├─ editable_legacy.py
│     │        │  │  │  │  └─ wheel.py
│     │        │  │  │  └─ prepare.py
│     │        │  │  ├─ pyproject.py
│     │        │  │  ├─ req
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ constructors.cpython-310.pyc
│     │        │  │  │  │  ├─ req_file.cpython-310.pyc
│     │        │  │  │  │  ├─ req_install.cpython-310.pyc
│     │        │  │  │  │  ├─ req_set.cpython-310.pyc
│     │        │  │  │  │  └─ req_uninstall.cpython-310.pyc
│     │        │  │  │  ├─ constructors.py
│     │        │  │  │  ├─ req_file.py
│     │        │  │  │  ├─ req_install.py
│     │        │  │  │  ├─ req_set.py
│     │        │  │  │  └─ req_uninstall.py
│     │        │  │  ├─ resolution
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  └─ base.cpython-310.pyc
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ legacy
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  └─ resolver.cpython-310.pyc
│     │        │  │  │  │  └─ resolver.py
│     │        │  │  │  └─ resolvelib
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     ├─ __pycache__
│     │        │  │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │  │     │  ├─ base.cpython-310.pyc
│     │        │  │  │     │  ├─ candidates.cpython-310.pyc
│     │        │  │  │     │  ├─ factory.cpython-310.pyc
│     │        │  │  │     │  ├─ found_candidates.cpython-310.pyc
│     │        │  │  │     │  ├─ provider.cpython-310.pyc
│     │        │  │  │     │  ├─ reporter.cpython-310.pyc
│     │        │  │  │     │  ├─ requirements.cpython-310.pyc
│     │        │  │  │     │  └─ resolver.cpython-310.pyc
│     │        │  │  │     ├─ base.py
│     │        │  │  │     ├─ candidates.py
│     │        │  │  │     ├─ factory.py
│     │        │  │  │     ├─ found_candidates.py
│     │        │  │  │     ├─ provider.py
│     │        │  │  │     ├─ reporter.py
│     │        │  │  │     ├─ requirements.py
│     │        │  │  │     └─ resolver.py
│     │        │  │  ├─ self_outdated_check.py
│     │        │  │  ├─ utils
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _jaraco_text.cpython-310.pyc
│     │        │  │  │  │  ├─ _log.cpython-310.pyc
│     │        │  │  │  │  ├─ appdirs.cpython-310.pyc
│     │        │  │  │  │  ├─ compat.cpython-310.pyc
│     │        │  │  │  │  ├─ compatibility_tags.cpython-310.pyc
│     │        │  │  │  │  ├─ datetime.cpython-310.pyc
│     │        │  │  │  │  ├─ deprecation.cpython-310.pyc
│     │        │  │  │  │  ├─ direct_url_helpers.cpython-310.pyc
│     │        │  │  │  │  ├─ egg_link.cpython-310.pyc
│     │        │  │  │  │  ├─ encoding.cpython-310.pyc
│     │        │  │  │  │  ├─ entrypoints.cpython-310.pyc
│     │        │  │  │  │  ├─ filesystem.cpython-310.pyc
│     │        │  │  │  │  ├─ filetypes.cpython-310.pyc
│     │        │  │  │  │  ├─ glibc.cpython-310.pyc
│     │        │  │  │  │  ├─ hashes.cpython-310.pyc
│     │        │  │  │  │  ├─ inject_securetransport.cpython-310.pyc
│     │        │  │  │  │  ├─ logging.cpython-310.pyc
│     │        │  │  │  │  ├─ misc.cpython-310.pyc
│     │        │  │  │  │  ├─ models.cpython-310.pyc
│     │        │  │  │  │  ├─ packaging.cpython-310.pyc
│     │        │  │  │  │  ├─ setuptools_build.cpython-310.pyc
│     │        │  │  │  │  ├─ subprocess.cpython-310.pyc
│     │        │  │  │  │  ├─ temp_dir.cpython-310.pyc
│     │        │  │  │  │  ├─ unpacking.cpython-310.pyc
│     │        │  │  │  │  ├─ urls.cpython-310.pyc
│     │        │  │  │  │  ├─ virtualenv.cpython-310.pyc
│     │        │  │  │  │  └─ wheel.cpython-310.pyc
│     │        │  │  │  ├─ _jaraco_text.py
│     │        │  │  │  ├─ _log.py
│     │        │  │  │  ├─ appdirs.py
│     │        │  │  │  ├─ compat.py
│     │        │  │  │  ├─ compatibility_tags.py
│     │        │  │  │  ├─ datetime.py
│     │        │  │  │  ├─ deprecation.py
│     │        │  │  │  ├─ direct_url_helpers.py
│     │        │  │  │  ├─ egg_link.py
│     │        │  │  │  ├─ encoding.py
│     │        │  │  │  ├─ entrypoints.py
│     │        │  │  │  ├─ filesystem.py
│     │        │  │  │  ├─ filetypes.py
│     │        │  │  │  ├─ glibc.py
│     │        │  │  │  ├─ hashes.py
│     │        │  │  │  ├─ inject_securetransport.py
│     │        │  │  │  ├─ logging.py
│     │        │  │  │  ├─ misc.py
│     │        │  │  │  ├─ models.py
│     │        │  │  │  ├─ packaging.py
│     │        │  │  │  ├─ setuptools_build.py
│     │        │  │  │  ├─ subprocess.py
│     │        │  │  │  ├─ temp_dir.py
│     │        │  │  │  ├─ unpacking.py
│     │        │  │  │  ├─ urls.py
│     │        │  │  │  ├─ virtualenv.py
│     │        │  │  │  └─ wheel.py
│     │        │  │  ├─ vcs
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ bazaar.cpython-310.pyc
│     │        │  │  │  │  ├─ git.cpython-310.pyc
│     │        │  │  │  │  ├─ mercurial.cpython-310.pyc
│     │        │  │  │  │  ├─ subversion.cpython-310.pyc
│     │        │  │  │  │  └─ versioncontrol.cpython-310.pyc
│     │        │  │  │  ├─ bazaar.py
│     │        │  │  │  ├─ git.py
│     │        │  │  │  ├─ mercurial.py
│     │        │  │  │  ├─ subversion.py
│     │        │  │  │  └─ versioncontrol.py
│     │        │  │  └─ wheel_builder.py
│     │        │  ├─ _vendor
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ six.cpython-310.pyc
│     │        │  │  │  └─ typing_extensions.cpython-310.pyc
│     │        │  │  ├─ cachecontrol
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _cmd.cpython-310.pyc
│     │        │  │  │  │  ├─ adapter.cpython-310.pyc
│     │        │  │  │  │  ├─ cache.cpython-310.pyc
│     │        │  │  │  │  ├─ compat.cpython-310.pyc
│     │        │  │  │  │  ├─ controller.cpython-310.pyc
│     │        │  │  │  │  ├─ filewrapper.cpython-310.pyc
│     │        │  │  │  │  ├─ heuristics.cpython-310.pyc
│     │        │  │  │  │  ├─ serialize.cpython-310.pyc
│     │        │  │  │  │  └─ wrapper.cpython-310.pyc
│     │        │  │  │  ├─ _cmd.py
│     │        │  │  │  ├─ adapter.py
│     │        │  │  │  ├─ cache.py
│     │        │  │  │  ├─ caches
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ file_cache.cpython-310.pyc
│     │        │  │  │  │  │  └─ redis_cache.cpython-310.pyc
│     │        │  │  │  │  ├─ file_cache.py
│     │        │  │  │  │  └─ redis_cache.py
│     │        │  │  │  ├─ compat.py
│     │        │  │  │  ├─ controller.py
│     │        │  │  │  ├─ filewrapper.py
│     │        │  │  │  ├─ heuristics.py
│     │        │  │  │  ├─ serialize.py
│     │        │  │  │  └─ wrapper.py
│     │        │  │  ├─ certifi
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __main__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  │  │  └─ core.cpython-310.pyc
│     │        │  │  │  ├─ cacert.pem
│     │        │  │  │  └─ core.py
│     │        │  │  ├─ chardet
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ big5freq.cpython-310.pyc
│     │        │  │  │  │  ├─ big5prober.cpython-310.pyc
│     │        │  │  │  │  ├─ chardistribution.cpython-310.pyc
│     │        │  │  │  │  ├─ charsetgroupprober.cpython-310.pyc
│     │        │  │  │  │  ├─ charsetprober.cpython-310.pyc
│     │        │  │  │  │  ├─ codingstatemachine.cpython-310.pyc
│     │        │  │  │  │  ├─ codingstatemachinedict.cpython-310.pyc
│     │        │  │  │  │  ├─ cp949prober.cpython-310.pyc
│     │        │  │  │  │  ├─ enums.cpython-310.pyc
│     │        │  │  │  │  ├─ escprober.cpython-310.pyc
│     │        │  │  │  │  ├─ escsm.cpython-310.pyc
│     │        │  │  │  │  ├─ eucjpprober.cpython-310.pyc
│     │        │  │  │  │  ├─ euckrfreq.cpython-310.pyc
│     │        │  │  │  │  ├─ euckrprober.cpython-310.pyc
│     │        │  │  │  │  ├─ euctwfreq.cpython-310.pyc
│     │        │  │  │  │  ├─ euctwprober.cpython-310.pyc
│     │        │  │  │  │  ├─ gb2312freq.cpython-310.pyc
│     │        │  │  │  │  ├─ gb2312prober.cpython-310.pyc
│     │        │  │  │  │  ├─ hebrewprober.cpython-310.pyc
│     │        │  │  │  │  ├─ jisfreq.cpython-310.pyc
│     │        │  │  │  │  ├─ johabfreq.cpython-310.pyc
│     │        │  │  │  │  ├─ johabprober.cpython-310.pyc
│     │        │  │  │  │  ├─ jpcntx.cpython-310.pyc
│     │        │  │  │  │  ├─ langbulgarianmodel.cpython-310.pyc
│     │        │  │  │  │  ├─ langgreekmodel.cpython-310.pyc
│     │        │  │  │  │  ├─ langhebrewmodel.cpython-310.pyc
│     │        │  │  │  │  ├─ langhungarianmodel.cpython-310.pyc
│     │        │  │  │  │  ├─ langrussianmodel.cpython-310.pyc
│     │        │  │  │  │  ├─ langthaimodel.cpython-310.pyc
│     │        │  │  │  │  ├─ langturkishmodel.cpython-310.pyc
│     │        │  │  │  │  ├─ latin1prober.cpython-310.pyc
│     │        │  │  │  │  ├─ macromanprober.cpython-310.pyc
│     │        │  │  │  │  ├─ mbcharsetprober.cpython-310.pyc
│     │        │  │  │  │  ├─ mbcsgroupprober.cpython-310.pyc
│     │        │  │  │  │  ├─ mbcssm.cpython-310.pyc
│     │        │  │  │  │  ├─ resultdict.cpython-310.pyc
│     │        │  │  │  │  ├─ sbcharsetprober.cpython-310.pyc
│     │        │  │  │  │  ├─ sbcsgroupprober.cpython-310.pyc
│     │        │  │  │  │  ├─ sjisprober.cpython-310.pyc
│     │        │  │  │  │  ├─ universaldetector.cpython-310.pyc
│     │        │  │  │  │  ├─ utf1632prober.cpython-310.pyc
│     │        │  │  │  │  ├─ utf8prober.cpython-310.pyc
│     │        │  │  │  │  └─ version.cpython-310.pyc
│     │        │  │  │  ├─ big5freq.py
│     │        │  │  │  ├─ big5prober.py
│     │        │  │  │  ├─ chardistribution.py
│     │        │  │  │  ├─ charsetgroupprober.py
│     │        │  │  │  ├─ charsetprober.py
│     │        │  │  │  ├─ cli
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  └─ chardetect.cpython-310.pyc
│     │        │  │  │  │  └─ chardetect.py
│     │        │  │  │  ├─ codingstatemachine.py
│     │        │  │  │  ├─ codingstatemachinedict.py
│     │        │  │  │  ├─ cp949prober.py
│     │        │  │  │  ├─ enums.py
│     │        │  │  │  ├─ escprober.py
│     │        │  │  │  ├─ escsm.py
│     │        │  │  │  ├─ eucjpprober.py
│     │        │  │  │  ├─ euckrfreq.py
│     │        │  │  │  ├─ euckrprober.py
│     │        │  │  │  ├─ euctwfreq.py
│     │        │  │  │  ├─ euctwprober.py
│     │        │  │  │  ├─ gb2312freq.py
│     │        │  │  │  ├─ gb2312prober.py
│     │        │  │  │  ├─ hebrewprober.py
│     │        │  │  │  ├─ jisfreq.py
│     │        │  │  │  ├─ johabfreq.py
│     │        │  │  │  ├─ johabprober.py
│     │        │  │  │  ├─ jpcntx.py
│     │        │  │  │  ├─ langbulgarianmodel.py
│     │        │  │  │  ├─ langgreekmodel.py
│     │        │  │  │  ├─ langhebrewmodel.py
│     │        │  │  │  ├─ langhungarianmodel.py
│     │        │  │  │  ├─ langrussianmodel.py
│     │        │  │  │  ├─ langthaimodel.py
│     │        │  │  │  ├─ langturkishmodel.py
│     │        │  │  │  ├─ latin1prober.py
│     │        │  │  │  ├─ macromanprober.py
│     │        │  │  │  ├─ mbcharsetprober.py
│     │        │  │  │  ├─ mbcsgroupprober.py
│     │        │  │  │  ├─ mbcssm.py
│     │        │  │  │  ├─ metadata
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  └─ languages.cpython-310.pyc
│     │        │  │  │  │  └─ languages.py
│     │        │  │  │  ├─ resultdict.py
│     │        │  │  │  ├─ sbcharsetprober.py
│     │        │  │  │  ├─ sbcsgroupprober.py
│     │        │  │  │  ├─ sjisprober.py
│     │        │  │  │  ├─ universaldetector.py
│     │        │  │  │  ├─ utf1632prober.py
│     │        │  │  │  ├─ utf8prober.py
│     │        │  │  │  └─ version.py
│     │        │  │  ├─ colorama
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ ansi.cpython-310.pyc
│     │        │  │  │  │  ├─ ansitowin32.cpython-310.pyc
│     │        │  │  │  │  ├─ initialise.cpython-310.pyc
│     │        │  │  │  │  ├─ win32.cpython-310.pyc
│     │        │  │  │  │  └─ winterm.cpython-310.pyc
│     │        │  │  │  ├─ ansi.py
│     │        │  │  │  ├─ ansitowin32.py
│     │        │  │  │  ├─ initialise.py
│     │        │  │  │  ├─ tests
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ ansi_test.cpython-310.pyc
│     │        │  │  │  │  │  ├─ ansitowin32_test.cpython-310.pyc
│     │        │  │  │  │  │  ├─ initialise_test.cpython-310.pyc
│     │        │  │  │  │  │  ├─ isatty_test.cpython-310.pyc
│     │        │  │  │  │  │  ├─ utils.cpython-310.pyc
│     │        │  │  │  │  │  └─ winterm_test.cpython-310.pyc
│     │        │  │  │  │  ├─ ansi_test.py
│     │        │  │  │  │  ├─ ansitowin32_test.py
│     │        │  │  │  │  ├─ initialise_test.py
│     │        │  │  │  │  ├─ isatty_test.py
│     │        │  │  │  │  ├─ utils.py
│     │        │  │  │  │  └─ winterm_test.py
│     │        │  │  │  ├─ win32.py
│     │        │  │  │  └─ winterm.py
│     │        │  │  ├─ distlib
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ compat.cpython-310.pyc
│     │        │  │  │  │  ├─ database.cpython-310.pyc
│     │        │  │  │  │  ├─ index.cpython-310.pyc
│     │        │  │  │  │  ├─ locators.cpython-310.pyc
│     │        │  │  │  │  ├─ manifest.cpython-310.pyc
│     │        │  │  │  │  ├─ markers.cpython-310.pyc
│     │        │  │  │  │  ├─ metadata.cpython-310.pyc
│     │        │  │  │  │  ├─ resources.cpython-310.pyc
│     │        │  │  │  │  ├─ scripts.cpython-310.pyc
│     │        │  │  │  │  ├─ util.cpython-310.pyc
│     │        │  │  │  │  ├─ version.cpython-310.pyc
│     │        │  │  │  │  └─ wheel.cpython-310.pyc
│     │        │  │  │  ├─ compat.py
│     │        │  │  │  ├─ database.py
│     │        │  │  │  ├─ index.py
│     │        │  │  │  ├─ locators.py
│     │        │  │  │  ├─ manifest.py
│     │        │  │  │  ├─ markers.py
│     │        │  │  │  ├─ metadata.py
│     │        │  │  │  ├─ resources.py
│     │        │  │  │  ├─ scripts.py
│     │        │  │  │  ├─ t32.exe
│     │        │  │  │  ├─ t64-arm.exe
│     │        │  │  │  ├─ t64.exe
│     │        │  │  │  ├─ util.py
│     │        │  │  │  ├─ version.py
│     │        │  │  │  ├─ w32.exe
│     │        │  │  │  ├─ w64-arm.exe
│     │        │  │  │  ├─ w64.exe
│     │        │  │  │  └─ wheel.py
│     │        │  │  ├─ distro
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __main__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  │  │  └─ distro.cpython-310.pyc
│     │        │  │  │  └─ distro.py
│     │        │  │  ├─ idna
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ codec.cpython-310.pyc
│     │        │  │  │  │  ├─ compat.cpython-310.pyc
│     │        │  │  │  │  ├─ core.cpython-310.pyc
│     │        │  │  │  │  ├─ idnadata.cpython-310.pyc
│     │        │  │  │  │  ├─ intranges.cpython-310.pyc
│     │        │  │  │  │  ├─ package_data.cpython-310.pyc
│     │        │  │  │  │  └─ uts46data.cpython-310.pyc
│     │        │  │  │  ├─ codec.py
│     │        │  │  │  ├─ compat.py
│     │        │  │  │  ├─ core.py
│     │        │  │  │  ├─ idnadata.py
│     │        │  │  │  ├─ intranges.py
│     │        │  │  │  ├─ package_data.py
│     │        │  │  │  └─ uts46data.py
│     │        │  │  ├─ msgpack
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  │  │  ├─ ext.cpython-310.pyc
│     │        │  │  │  │  └─ fallback.cpython-310.pyc
│     │        │  │  │  ├─ exceptions.py
│     │        │  │  │  ├─ ext.py
│     │        │  │  │  └─ fallback.py
│     │        │  │  ├─ packaging
│     │        │  │  │  ├─ __about__.py
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __about__.cpython-310.pyc
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _manylinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _musllinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _structures.cpython-310.pyc
│     │        │  │  │  │  ├─ markers.cpython-310.pyc
│     │        │  │  │  │  ├─ requirements.cpython-310.pyc
│     │        │  │  │  │  ├─ specifiers.cpython-310.pyc
│     │        │  │  │  │  ├─ tags.cpython-310.pyc
│     │        │  │  │  │  ├─ utils.cpython-310.pyc
│     │        │  │  │  │  └─ version.cpython-310.pyc
│     │        │  │  │  ├─ _manylinux.py
│     │        │  │  │  ├─ _musllinux.py
│     │        │  │  │  ├─ _structures.py
│     │        │  │  │  ├─ markers.py
│     │        │  │  │  ├─ requirements.py
│     │        │  │  │  ├─ specifiers.py
│     │        │  │  │  ├─ tags.py
│     │        │  │  │  ├─ utils.py
│     │        │  │  │  └─ version.py
│     │        │  │  ├─ pkg_resources
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  └─ __pycache__
│     │        │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  ├─ platformdirs
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __main__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  │  │  ├─ android.cpython-310.pyc
│     │        │  │  │  │  ├─ api.cpython-310.pyc
│     │        │  │  │  │  ├─ macos.cpython-310.pyc
│     │        │  │  │  │  ├─ unix.cpython-310.pyc
│     │        │  │  │  │  ├─ version.cpython-310.pyc
│     │        │  │  │  │  └─ windows.cpython-310.pyc
│     │        │  │  │  ├─ android.py
│     │        │  │  │  ├─ api.py
│     │        │  │  │  ├─ macos.py
│     │        │  │  │  ├─ unix.py
│     │        │  │  │  ├─ version.py
│     │        │  │  │  └─ windows.py
│     │        │  │  ├─ pygments
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __main__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  │  │  ├─ cmdline.cpython-310.pyc
│     │        │  │  │  │  ├─ console.cpython-310.pyc
│     │        │  │  │  │  ├─ filter.cpython-310.pyc
│     │        │  │  │  │  ├─ formatter.cpython-310.pyc
│     │        │  │  │  │  ├─ lexer.cpython-310.pyc
│     │        │  │  │  │  ├─ modeline.cpython-310.pyc
│     │        │  │  │  │  ├─ plugin.cpython-310.pyc
│     │        │  │  │  │  ├─ regexopt.cpython-310.pyc
│     │        │  │  │  │  ├─ scanner.cpython-310.pyc
│     │        │  │  │  │  ├─ sphinxext.cpython-310.pyc
│     │        │  │  │  │  ├─ style.cpython-310.pyc
│     │        │  │  │  │  ├─ token.cpython-310.pyc
│     │        │  │  │  │  ├─ unistring.cpython-310.pyc
│     │        │  │  │  │  └─ util.cpython-310.pyc
│     │        │  │  │  ├─ cmdline.py
│     │        │  │  │  ├─ console.py
│     │        │  │  │  ├─ filter.py
│     │        │  │  │  ├─ filters
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ formatter.py
│     │        │  │  │  ├─ formatters
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ _mapping.cpython-310.pyc
│     │        │  │  │  │  │  ├─ bbcode.cpython-310.pyc
│     │        │  │  │  │  │  ├─ groff.cpython-310.pyc
│     │        │  │  │  │  │  ├─ html.cpython-310.pyc
│     │        │  │  │  │  │  ├─ img.cpython-310.pyc
│     │        │  │  │  │  │  ├─ irc.cpython-310.pyc
│     │        │  │  │  │  │  ├─ latex.cpython-310.pyc
│     │        │  │  │  │  │  ├─ other.cpython-310.pyc
│     │        │  │  │  │  │  ├─ pangomarkup.cpython-310.pyc
│     │        │  │  │  │  │  ├─ rtf.cpython-310.pyc
│     │        │  │  │  │  │  ├─ svg.cpython-310.pyc
│     │        │  │  │  │  │  ├─ terminal.cpython-310.pyc
│     │        │  │  │  │  │  └─ terminal256.cpython-310.pyc
│     │        │  │  │  │  ├─ _mapping.py
│     │        │  │  │  │  ├─ bbcode.py
│     │        │  │  │  │  ├─ groff.py
│     │        │  │  │  │  ├─ html.py
│     │        │  │  │  │  ├─ img.py
│     │        │  │  │  │  ├─ irc.py
│     │        │  │  │  │  ├─ latex.py
│     │        │  │  │  │  ├─ other.py
│     │        │  │  │  │  ├─ pangomarkup.py
│     │        │  │  │  │  ├─ rtf.py
│     │        │  │  │  │  ├─ svg.py
│     │        │  │  │  │  ├─ terminal.py
│     │        │  │  │  │  └─ terminal256.py
│     │        │  │  │  ├─ lexer.py
│     │        │  │  │  ├─ lexers
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ _mapping.cpython-310.pyc
│     │        │  │  │  │  │  └─ python.cpython-310.pyc
│     │        │  │  │  │  ├─ _mapping.py
│     │        │  │  │  │  └─ python.py
│     │        │  │  │  ├─ modeline.py
│     │        │  │  │  ├─ plugin.py
│     │        │  │  │  ├─ regexopt.py
│     │        │  │  │  ├─ scanner.py
│     │        │  │  │  ├─ sphinxext.py
│     │        │  │  │  ├─ style.py
│     │        │  │  │  ├─ styles
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ token.py
│     │        │  │  │  ├─ unistring.py
│     │        │  │  │  └─ util.py
│     │        │  │  ├─ pyparsing
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ actions.cpython-310.pyc
│     │        │  │  │  │  ├─ common.cpython-310.pyc
│     │        │  │  │  │  ├─ core.cpython-310.pyc
│     │        │  │  │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  │  │  ├─ helpers.cpython-310.pyc
│     │        │  │  │  │  ├─ results.cpython-310.pyc
│     │        │  │  │  │  ├─ testing.cpython-310.pyc
│     │        │  │  │  │  ├─ unicode.cpython-310.pyc
│     │        │  │  │  │  └─ util.cpython-310.pyc
│     │        │  │  │  ├─ actions.py
│     │        │  │  │  ├─ common.py
│     │        │  │  │  ├─ core.py
│     │        │  │  │  ├─ diagram
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ exceptions.py
│     │        │  │  │  ├─ helpers.py
│     │        │  │  │  ├─ results.py
│     │        │  │  │  ├─ testing.py
│     │        │  │  │  ├─ unicode.py
│     │        │  │  │  └─ util.py
│     │        │  │  ├─ requests
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ __version__.cpython-310.pyc
│     │        │  │  │  │  ├─ _internal_utils.cpython-310.pyc
│     │        │  │  │  │  ├─ adapters.cpython-310.pyc
│     │        │  │  │  │  ├─ api.cpython-310.pyc
│     │        │  │  │  │  ├─ auth.cpython-310.pyc
│     │        │  │  │  │  ├─ certs.cpython-310.pyc
│     │        │  │  │  │  ├─ compat.cpython-310.pyc
│     │        │  │  │  │  ├─ cookies.cpython-310.pyc
│     │        │  │  │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  │  │  ├─ help.cpython-310.pyc
│     │        │  │  │  │  ├─ models.cpython-310.pyc
│     │        │  │  │  │  ├─ packages.cpython-310.pyc
│     │        │  │  │  │  ├─ sessions.cpython-310.pyc
│     │        │  │  │  │  ├─ status_codes.cpython-310.pyc
│     │        │  │  │  │  ├─ structures.cpython-310.pyc
│     │        │  │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  │  ├─ __version__.py
│     │        │  │  │  ├─ _internal_utils.py
│     │        │  │  │  ├─ adapters.py
│     │        │  │  │  ├─ api.py
│     │        │  │  │  ├─ auth.py
│     │        │  │  │  ├─ certs.py
│     │        │  │  │  ├─ compat.py
│     │        │  │  │  ├─ cookies.py
│     │        │  │  │  ├─ exceptions.py
│     │        │  │  │  ├─ help.py
│     │        │  │  │  ├─ models.py
│     │        │  │  │  ├─ packages.py
│     │        │  │  │  ├─ sessions.py
│     │        │  │  │  ├─ status_codes.py
│     │        │  │  │  ├─ structures.py
│     │        │  │  │  └─ utils.py
│     │        │  │  ├─ resolvelib
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ providers.cpython-310.pyc
│     │        │  │  │  │  ├─ reporters.cpython-310.pyc
│     │        │  │  │  │  ├─ resolvers.cpython-310.pyc
│     │        │  │  │  │  └─ structs.cpython-310.pyc
│     │        │  │  │  ├─ compat
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  └─ collections_abc.cpython-310.pyc
│     │        │  │  │  │  └─ collections_abc.py
│     │        │  │  │  ├─ providers.py
│     │        │  │  │  ├─ reporters.py
│     │        │  │  │  ├─ resolvers.py
│     │        │  │  │  └─ structs.py
│     │        │  │  ├─ rich
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __main__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  │  │  ├─ _cell_widths.cpython-310.pyc
│     │        │  │  │  │  ├─ _emoji_codes.cpython-310.pyc
│     │        │  │  │  │  ├─ _emoji_replace.cpython-310.pyc
│     │        │  │  │  │  ├─ _export_format.cpython-310.pyc
│     │        │  │  │  │  ├─ _extension.cpython-310.pyc
│     │        │  │  │  │  ├─ _fileno.cpython-310.pyc
│     │        │  │  │  │  ├─ _inspect.cpython-310.pyc
│     │        │  │  │  │  ├─ _log_render.cpython-310.pyc
│     │        │  │  │  │  ├─ _loop.cpython-310.pyc
│     │        │  │  │  │  ├─ _null_file.cpython-310.pyc
│     │        │  │  │  │  ├─ _palettes.cpython-310.pyc
│     │        │  │  │  │  ├─ _pick.cpython-310.pyc
│     │        │  │  │  │  ├─ _ratio.cpython-310.pyc
│     │        │  │  │  │  ├─ _spinners.cpython-310.pyc
│     │        │  │  │  │  ├─ _stack.cpython-310.pyc
│     │        │  │  │  │  ├─ _timer.cpython-310.pyc
│     │        │  │  │  │  ├─ _win32_console.cpython-310.pyc
│     │        │  │  │  │  ├─ _windows.cpython-310.pyc
│     │        │  │  │  │  ├─ _windows_renderer.cpython-310.pyc
│     │        │  │  │  │  ├─ _wrap.cpython-310.pyc
│     │        │  │  │  │  ├─ abc.cpython-310.pyc
│     │        │  │  │  │  ├─ align.cpython-310.pyc
│     │        │  │  │  │  ├─ ansi.cpython-310.pyc
│     │        │  │  │  │  ├─ bar.cpython-310.pyc
│     │        │  │  │  │  ├─ box.cpython-310.pyc
│     │        │  │  │  │  ├─ cells.cpython-310.pyc
│     │        │  │  │  │  ├─ color.cpython-310.pyc
│     │        │  │  │  │  ├─ color_triplet.cpython-310.pyc
│     │        │  │  │  │  ├─ columns.cpython-310.pyc
│     │        │  │  │  │  ├─ console.cpython-310.pyc
│     │        │  │  │  │  ├─ constrain.cpython-310.pyc
│     │        │  │  │  │  ├─ containers.cpython-310.pyc
│     │        │  │  │  │  ├─ control.cpython-310.pyc
│     │        │  │  │  │  ├─ default_styles.cpython-310.pyc
│     │        │  │  │  │  ├─ diagnose.cpython-310.pyc
│     │        │  │  │  │  ├─ emoji.cpython-310.pyc
│     │        │  │  │  │  ├─ errors.cpython-310.pyc
│     │        │  │  │  │  ├─ file_proxy.cpython-310.pyc
│     │        │  │  │  │  ├─ filesize.cpython-310.pyc
│     │        │  │  │  │  ├─ highlighter.cpython-310.pyc
│     │        │  │  │  │  ├─ json.cpython-310.pyc
│     │        │  │  │  │  ├─ jupyter.cpython-310.pyc
│     │        │  │  │  │  ├─ layout.cpython-310.pyc
│     │        │  │  │  │  ├─ live.cpython-310.pyc
│     │        │  │  │  │  ├─ live_render.cpython-310.pyc
│     │        │  │  │  │  ├─ logging.cpython-310.pyc
│     │        │  │  │  │  ├─ markup.cpython-310.pyc
│     │        │  │  │  │  ├─ measure.cpython-310.pyc
│     │        │  │  │  │  ├─ padding.cpython-310.pyc
│     │        │  │  │  │  ├─ pager.cpython-310.pyc
│     │        │  │  │  │  ├─ palette.cpython-310.pyc
│     │        │  │  │  │  ├─ panel.cpython-310.pyc
│     │        │  │  │  │  ├─ pretty.cpython-310.pyc
│     │        │  │  │  │  ├─ progress.cpython-310.pyc
│     │        │  │  │  │  ├─ progress_bar.cpython-310.pyc
│     │        │  │  │  │  ├─ prompt.cpython-310.pyc
│     │        │  │  │  │  ├─ protocol.cpython-310.pyc
│     │        │  │  │  │  ├─ region.cpython-310.pyc
│     │        │  │  │  │  ├─ repr.cpython-310.pyc
│     │        │  │  │  │  ├─ rule.cpython-310.pyc
│     │        │  │  │  │  ├─ scope.cpython-310.pyc
│     │        │  │  │  │  ├─ screen.cpython-310.pyc
│     │        │  │  │  │  ├─ segment.cpython-310.pyc
│     │        │  │  │  │  ├─ spinner.cpython-310.pyc
│     │        │  │  │  │  ├─ status.cpython-310.pyc
│     │        │  │  │  │  ├─ style.cpython-310.pyc
│     │        │  │  │  │  ├─ styled.cpython-310.pyc
│     │        │  │  │  │  ├─ syntax.cpython-310.pyc
│     │        │  │  │  │  ├─ table.cpython-310.pyc
│     │        │  │  │  │  ├─ terminal_theme.cpython-310.pyc
│     │        │  │  │  │  ├─ text.cpython-310.pyc
│     │        │  │  │  │  ├─ theme.cpython-310.pyc
│     │        │  │  │  │  ├─ themes.cpython-310.pyc
│     │        │  │  │  │  ├─ traceback.cpython-310.pyc
│     │        │  │  │  │  └─ tree.cpython-310.pyc
│     │        │  │  │  ├─ _cell_widths.py
│     │        │  │  │  ├─ _emoji_codes.py
│     │        │  │  │  ├─ _emoji_replace.py
│     │        │  │  │  ├─ _export_format.py
│     │        │  │  │  ├─ _extension.py
│     │        │  │  │  ├─ _fileno.py
│     │        │  │  │  ├─ _inspect.py
│     │        │  │  │  ├─ _log_render.py
│     │        │  │  │  ├─ _loop.py
│     │        │  │  │  ├─ _null_file.py
│     │        │  │  │  ├─ _palettes.py
│     │        │  │  │  ├─ _pick.py
│     │        │  │  │  ├─ _ratio.py
│     │        │  │  │  ├─ _spinners.py
│     │        │  │  │  ├─ _stack.py
│     │        │  │  │  ├─ _timer.py
│     │        │  │  │  ├─ _win32_console.py
│     │        │  │  │  ├─ _windows.py
│     │        │  │  │  ├─ _windows_renderer.py
│     │        │  │  │  ├─ _wrap.py
│     │        │  │  │  ├─ abc.py
│     │        │  │  │  ├─ align.py
│     │        │  │  │  ├─ ansi.py
│     │        │  │  │  ├─ bar.py
│     │        │  │  │  ├─ box.py
│     │        │  │  │  ├─ cells.py
│     │        │  │  │  ├─ color.py
│     │        │  │  │  ├─ color_triplet.py
│     │        │  │  │  ├─ columns.py
│     │        │  │  │  ├─ console.py
│     │        │  │  │  ├─ constrain.py
│     │        │  │  │  ├─ containers.py
│     │        │  │  │  ├─ control.py
│     │        │  │  │  ├─ default_styles.py
│     │        │  │  │  ├─ diagnose.py
│     │        │  │  │  ├─ emoji.py
│     │        │  │  │  ├─ errors.py
│     │        │  │  │  ├─ file_proxy.py
│     │        │  │  │  ├─ filesize.py
│     │        │  │  │  ├─ highlighter.py
│     │        │  │  │  ├─ json.py
│     │        │  │  │  ├─ jupyter.py
│     │        │  │  │  ├─ layout.py
│     │        │  │  │  ├─ live.py
│     │        │  │  │  ├─ live_render.py
│     │        │  │  │  ├─ logging.py
│     │        │  │  │  ├─ markup.py
│     │        │  │  │  ├─ measure.py
│     │        │  │  │  ├─ padding.py
│     │        │  │  │  ├─ pager.py
│     │        │  │  │  ├─ palette.py
│     │        │  │  │  ├─ panel.py
│     │        │  │  │  ├─ pretty.py
│     │        │  │  │  ├─ progress.py
│     │        │  │  │  ├─ progress_bar.py
│     │        │  │  │  ├─ prompt.py
│     │        │  │  │  ├─ protocol.py
│     │        │  │  │  ├─ region.py
│     │        │  │  │  ├─ repr.py
│     │        │  │  │  ├─ rule.py
│     │        │  │  │  ├─ scope.py
│     │        │  │  │  ├─ screen.py
│     │        │  │  │  ├─ segment.py
│     │        │  │  │  ├─ spinner.py
│     │        │  │  │  ├─ status.py
│     │        │  │  │  ├─ style.py
│     │        │  │  │  ├─ styled.py
│     │        │  │  │  ├─ syntax.py
│     │        │  │  │  ├─ table.py
│     │        │  │  │  ├─ terminal_theme.py
│     │        │  │  │  ├─ text.py
│     │        │  │  │  ├─ theme.py
│     │        │  │  │  ├─ themes.py
│     │        │  │  │  ├─ traceback.py
│     │        │  │  │  └─ tree.py
│     │        │  │  ├─ six.py
│     │        │  │  ├─ tenacity
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _asyncio.cpython-310.pyc
│     │        │  │  │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  │  │  ├─ after.cpython-310.pyc
│     │        │  │  │  │  ├─ before.cpython-310.pyc
│     │        │  │  │  │  ├─ before_sleep.cpython-310.pyc
│     │        │  │  │  │  ├─ nap.cpython-310.pyc
│     │        │  │  │  │  ├─ retry.cpython-310.pyc
│     │        │  │  │  │  ├─ stop.cpython-310.pyc
│     │        │  │  │  │  ├─ tornadoweb.cpython-310.pyc
│     │        │  │  │  │  └─ wait.cpython-310.pyc
│     │        │  │  │  ├─ _asyncio.py
│     │        │  │  │  ├─ _utils.py
│     │        │  │  │  ├─ after.py
│     │        │  │  │  ├─ before.py
│     │        │  │  │  ├─ before_sleep.py
│     │        │  │  │  ├─ nap.py
│     │        │  │  │  ├─ retry.py
│     │        │  │  │  ├─ stop.py
│     │        │  │  │  ├─ tornadoweb.py
│     │        │  │  │  └─ wait.py
│     │        │  │  ├─ tomli
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _parser.cpython-310.pyc
│     │        │  │  │  │  ├─ _re.cpython-310.pyc
│     │        │  │  │  │  └─ _types.cpython-310.pyc
│     │        │  │  │  ├─ _parser.py
│     │        │  │  │  ├─ _re.py
│     │        │  │  │  └─ _types.py
│     │        │  │  ├─ typing_extensions.py
│     │        │  │  ├─ urllib3
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _collections.cpython-310.pyc
│     │        │  │  │  │  ├─ _version.cpython-310.pyc
│     │        │  │  │  │  ├─ connection.cpython-310.pyc
│     │        │  │  │  │  ├─ connectionpool.cpython-310.pyc
│     │        │  │  │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  │  │  ├─ fields.cpython-310.pyc
│     │        │  │  │  │  ├─ filepost.cpython-310.pyc
│     │        │  │  │  │  ├─ poolmanager.cpython-310.pyc
│     │        │  │  │  │  ├─ request.cpython-310.pyc
│     │        │  │  │  │  └─ response.cpython-310.pyc
│     │        │  │  │  ├─ _collections.py
│     │        │  │  │  ├─ _version.py
│     │        │  │  │  ├─ connection.py
│     │        │  │  │  ├─ connectionpool.py
│     │        │  │  │  ├─ contrib
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ _appengine_environ.cpython-310.pyc
│     │        │  │  │  │  │  ├─ appengine.cpython-310.pyc
│     │        │  │  │  │  │  ├─ ntlmpool.cpython-310.pyc
│     │        │  │  │  │  │  ├─ pyopenssl.cpython-310.pyc
│     │        │  │  │  │  │  ├─ securetransport.cpython-310.pyc
│     │        │  │  │  │  │  └─ socks.cpython-310.pyc
│     │        │  │  │  │  ├─ _appengine_environ.py
│     │        │  │  │  │  ├─ _securetransport
│     │        │  │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  │  ├─ bindings.cpython-310.pyc
│     │        │  │  │  │  │  │  └─ low_level.cpython-310.pyc
│     │        │  │  │  │  │  ├─ bindings.py
│     │        │  │  │  │  │  └─ low_level.py
│     │        │  │  │  │  ├─ appengine.py
│     │        │  │  │  │  ├─ ntlmpool.py
│     │        │  │  │  │  ├─ pyopenssl.py
│     │        │  │  │  │  ├─ securetransport.py
│     │        │  │  │  │  └─ socks.py
│     │        │  │  │  ├─ exceptions.py
│     │        │  │  │  ├─ fields.py
│     │        │  │  │  ├─ filepost.py
│     │        │  │  │  ├─ packages
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  └─ six.cpython-310.pyc
│     │        │  │  │  │  ├─ backports
│     │        │  │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  │  └─ makefile.cpython-310.pyc
│     │        │  │  │  │  │  └─ makefile.py
│     │        │  │  │  │  └─ six.py
│     │        │  │  │  ├─ poolmanager.py
│     │        │  │  │  ├─ request.py
│     │        │  │  │  ├─ response.py
│     │        │  │  │  └─ util
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     ├─ __pycache__
│     │        │  │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │  │     │  ├─ connection.cpython-310.pyc
│     │        │  │  │     │  ├─ proxy.cpython-310.pyc
│     │        │  │  │     │  ├─ queue.cpython-310.pyc
│     │        │  │  │     │  ├─ request.cpython-310.pyc
│     │        │  │  │     │  ├─ response.cpython-310.pyc
│     │        │  │  │     │  ├─ retry.cpython-310.pyc
│     │        │  │  │     │  ├─ ssl_.cpython-310.pyc
│     │        │  │  │     │  ├─ ssl_match_hostname.cpython-310.pyc
│     │        │  │  │     │  ├─ ssltransport.cpython-310.pyc
│     │        │  │  │     │  ├─ timeout.cpython-310.pyc
│     │        │  │  │     │  ├─ url.cpython-310.pyc
│     │        │  │  │     │  └─ wait.cpython-310.pyc
│     │        │  │  │     ├─ connection.py
│     │        │  │  │     ├─ proxy.py
│     │        │  │  │     ├─ queue.py
│     │        │  │  │     ├─ request.py
│     │        │  │  │     ├─ response.py
│     │        │  │  │     ├─ retry.py
│     │        │  │  │     ├─ ssl_.py
│     │        │  │  │     ├─ ssl_match_hostname.py
│     │        │  │  │     ├─ ssltransport.py
│     │        │  │  │     ├─ timeout.py
│     │        │  │  │     ├─ url.py
│     │        │  │  │     └─ wait.py
│     │        │  │  ├─ vendor.txt
│     │        │  │  └─ webencodings
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ labels.cpython-310.pyc
│     │        │  │     │  ├─ mklabels.cpython-310.pyc
│     │        │  │     │  ├─ tests.cpython-310.pyc
│     │        │  │     │  └─ x_user_defined.cpython-310.pyc
│     │        │  │     ├─ labels.py
│     │        │  │     ├─ mklabels.py
│     │        │  │     ├─ tests.py
│     │        │  │     └─ x_user_defined.py
│     │        │  └─ py.typed
│     │        ├─ pip-23.1.2.dist-info
│     │        │  ├─ AUTHORS.txt
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.txt
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ pip_tools-6.14.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ piptools
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ cache.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ locations.cpython-310.pyc
│     │        │  │  ├─ logging.cpython-310.pyc
│     │        │  │  ├─ resolver.cpython-310.pyc
│     │        │  │  ├─ subprocess_utils.cpython-310.pyc
│     │        │  │  ├─ sync.cpython-310.pyc
│     │        │  │  ├─ utils.cpython-310.pyc
│     │        │  │  └─ writer.cpython-310.pyc
│     │        │  ├─ _compat
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ pip_compat.cpython-310.pyc
│     │        │  │  └─ pip_compat.py
│     │        │  ├─ cache.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ locations.py
│     │        │  ├─ logging.py
│     │        │  ├─ py.typed
│     │        │  ├─ repositories
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ local.cpython-310.pyc
│     │        │  │  │  └─ pypi.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ local.py
│     │        │  │  └─ pypi.py
│     │        │  ├─ resolver.py
│     │        │  ├─ scripts
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ compile.cpython-310.pyc
│     │        │  │  │  └─ sync.cpython-310.pyc
│     │        │  │  ├─ compile.py
│     │        │  │  └─ sync.py
│     │        │  ├─ subprocess_utils.py
│     │        │  ├─ sync.py
│     │        │  ├─ utils.py
│     │        │  └─ writer.py
│     │        ├─ pkg_resources
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  └─ __init__.cpython-310.pyc
│     │        │  ├─ _vendor
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ appdirs.cpython-310.pyc
│     │        │  │  │  └─ pyparsing.cpython-310.pyc
│     │        │  │  ├─ appdirs.py
│     │        │  │  ├─ packaging
│     │        │  │  │  ├─ __about__.py
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __about__.cpython-310.pyc
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _manylinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _musllinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _structures.cpython-310.pyc
│     │        │  │  │  │  ├─ markers.cpython-310.pyc
│     │        │  │  │  │  ├─ requirements.cpython-310.pyc
│     │        │  │  │  │  ├─ specifiers.cpython-310.pyc
│     │        │  │  │  │  ├─ tags.cpython-310.pyc
│     │        │  │  │  │  ├─ utils.cpython-310.pyc
│     │        │  │  │  │  └─ version.cpython-310.pyc
│     │        │  │  │  ├─ _manylinux.py
│     │        │  │  │  ├─ _musllinux.py
│     │        │  │  │  ├─ _structures.py
│     │        │  │  │  ├─ markers.py
│     │        │  │  │  ├─ requirements.py
│     │        │  │  │  ├─ specifiers.py
│     │        │  │  │  ├─ tags.py
│     │        │  │  │  ├─ utils.py
│     │        │  │  │  └─ version.py
│     │        │  │  └─ pyparsing.py
│     │        │  ├─ extern
│     │        │  │  ├─ __init__.py
│     │        │  │  └─ __pycache__
│     │        │  │     └─ __init__.cpython-310.pyc
│     │        │  └─ tests
│     │        │     └─ data
│     │        │        └─ my-test-package-source
│     │        │           ├─ __pycache__
│     │        │           │  └─ setup.cpython-310.pyc
│     │        │           └─ setup.py
│     │        ├─ platformdirs
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ android.cpython-310.pyc
│     │        │  │  ├─ api.cpython-310.pyc
│     │        │  │  ├─ macos.cpython-310.pyc
│     │        │  │  ├─ unix.cpython-310.pyc
│     │        │  │  ├─ version.cpython-310.pyc
│     │        │  │  └─ windows.cpython-310.pyc
│     │        │  ├─ android.py
│     │        │  ├─ api.py
│     │        │  ├─ macos.py
│     │        │  ├─ py.typed
│     │        │  ├─ unix.py
│     │        │  ├─ version.py
│     │        │  └─ windows.py
│     │        ├─ platformdirs-3.8.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ licenses
│     │        │     └─ LICENSE
│     │        ├─ pluggy
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _callers.cpython-310.pyc
│     │        │  │  ├─ _manager.cpython-310.pyc
│     │        │  │  ├─ _result.cpython-310.pyc
│     │        │  │  ├─ _tracing.cpython-310.pyc
│     │        │  │  └─ _version.cpython-310.pyc
│     │        │  ├─ _callers.py
│     │        │  ├─ _manager.py
│     │        │  ├─ _result.py
│     │        │  ├─ _tracing.py
│     │        │  └─ _version.py
│     │        ├─ pluggy-1.2.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ polyfactory
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ constants.cpython-310.pyc
│     │        │  │  ├─ decorators.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ field_meta.cpython-310.pyc
│     │        │  │  ├─ fields.cpython-310.pyc
│     │        │  │  ├─ persistence.cpython-310.pyc
│     │        │  │  └─ pytest_plugin.cpython-310.pyc
│     │        │  ├─ constants.py
│     │        │  ├─ decorators.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ factories
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ beanie_odm_factory.cpython-310.pyc
│     │        │  │  │  ├─ dataclass_factory.cpython-310.pyc
│     │        │  │  │  ├─ msgspec_factory.cpython-310.pyc
│     │        │  │  │  ├─ odmantic_odm_factory.cpython-310.pyc
│     │        │  │  │  ├─ pydantic_factory.cpython-310.pyc
│     │        │  │  │  └─ typed_dict_factory.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ beanie_odm_factory.py
│     │        │  │  ├─ dataclass_factory.py
│     │        │  │  ├─ msgspec_factory.py
│     │        │  │  ├─ odmantic_odm_factory.py
│     │        │  │  ├─ pydantic_factory.py
│     │        │  │  └─ typed_dict_factory.py
│     │        │  ├─ field_meta.py
│     │        │  ├─ fields.py
│     │        │  ├─ persistence.py
│     │        │  ├─ py.typed
│     │        │  ├─ pytest_plugin.py
│     │        │  ├─ utils
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ helpers.cpython-310.pyc
│     │        │  │  │  └─ predicates.cpython-310.pyc
│     │        │  │  ├─ helpers.py
│     │        │  │  └─ predicates.py
│     │        │  └─ value_generators
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ complex_types.cpython-310.pyc
│     │        │     │  ├─ constrained_collections.cpython-310.pyc
│     │        │     │  ├─ constrained_dates.cpython-310.pyc
│     │        │     │  ├─ constrained_numbers.cpython-310.pyc
│     │        │     │  ├─ constrained_path.cpython-310.pyc
│     │        │     │  ├─ constrained_strings.cpython-310.pyc
│     │        │     │  ├─ constrained_url.cpython-310.pyc
│     │        │     │  ├─ constrained_uuid.cpython-310.pyc
│     │        │     │  ├─ primitives.cpython-310.pyc
│     │        │     │  └─ regex.cpython-310.pyc
│     │        │     ├─ complex_types.py
│     │        │     ├─ constrained_collections.py
│     │        │     ├─ constrained_dates.py
│     │        │     ├─ constrained_numbers.py
│     │        │     ├─ constrained_path.py
│     │        │     ├─ constrained_strings.py
│     │        │     ├─ constrained_url.py
│     │        │     ├─ constrained_uuid.py
│     │        │     ├─ primitives.py
│     │        │     └─ regex.py
│     │        ├─ polyfactory-2.5.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ py
│     │        │  ├─ __init__.py
│     │        │  ├─ __init__.pyi
│     │        │  ├─ __metainfo.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __metainfo.cpython-310.pyc
│     │        │  │  ├─ _builtin.cpython-310.pyc
│     │        │  │  ├─ _error.cpython-310.pyc
│     │        │  │  ├─ _std.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  ├─ _xmlgen.cpython-310.pyc
│     │        │  │  └─ test.cpython-310.pyc
│     │        │  ├─ _builtin.py
│     │        │  ├─ _code
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _assertionnew.cpython-310.pyc
│     │        │  │  │  ├─ _assertionold.cpython-310.pyc
│     │        │  │  │  ├─ _py2traceback.cpython-310.pyc
│     │        │  │  │  ├─ assertion.cpython-310.pyc
│     │        │  │  │  ├─ code.cpython-310.pyc
│     │        │  │  │  └─ source.cpython-310.pyc
│     │        │  │  ├─ _assertionnew.py
│     │        │  │  ├─ _assertionold.py
│     │        │  │  ├─ _py2traceback.py
│     │        │  │  ├─ assertion.py
│     │        │  │  ├─ code.py
│     │        │  │  └─ source.py
│     │        │  ├─ _error.py
│     │        │  ├─ _io
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ capture.cpython-310.pyc
│     │        │  │  │  ├─ saferepr.cpython-310.pyc
│     │        │  │  │  └─ terminalwriter.cpython-310.pyc
│     │        │  │  ├─ capture.py
│     │        │  │  ├─ saferepr.py
│     │        │  │  └─ terminalwriter.py
│     │        │  ├─ _log
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ log.cpython-310.pyc
│     │        │  │  │  └─ warning.cpython-310.pyc
│     │        │  │  ├─ log.py
│     │        │  │  └─ warning.py
│     │        │  ├─ _path
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cacheutil.cpython-310.pyc
│     │        │  │  │  ├─ common.cpython-310.pyc
│     │        │  │  │  ├─ local.cpython-310.pyc
│     │        │  │  │  ├─ svnurl.cpython-310.pyc
│     │        │  │  │  └─ svnwc.cpython-310.pyc
│     │        │  │  ├─ cacheutil.py
│     │        │  │  ├─ common.py
│     │        │  │  ├─ local.py
│     │        │  │  ├─ svnurl.py
│     │        │  │  └─ svnwc.py
│     │        │  ├─ _process
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cmdexec.cpython-310.pyc
│     │        │  │  │  ├─ forkedfunc.cpython-310.pyc
│     │        │  │  │  └─ killproc.cpython-310.pyc
│     │        │  │  ├─ cmdexec.py
│     │        │  │  ├─ forkedfunc.py
│     │        │  │  └─ killproc.py
│     │        │  ├─ _std.py
│     │        │  ├─ _vendored_packages
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ apipkg
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  └─ version.cpython-310.pyc
│     │        │  │  │  └─ version.py
│     │        │  │  ├─ apipkg-2.0.0.dist-info
│     │        │  │  │  ├─ INSTALLER
│     │        │  │  │  ├─ LICENSE
│     │        │  │  │  ├─ METADATA
│     │        │  │  │  ├─ RECORD
│     │        │  │  │  ├─ REQUESTED
│     │        │  │  │  ├─ WHEEL
│     │        │  │  │  └─ top_level.txt
│     │        │  │  ├─ iniconfig
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __init__.pyi
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ py.typed
│     │        │  │  └─ iniconfig-1.1.1.dist-info
│     │        │  │     ├─ INSTALLER
│     │        │  │     ├─ LICENSE
│     │        │  │     ├─ METADATA
│     │        │  │     ├─ RECORD
│     │        │  │     ├─ REQUESTED
│     │        │  │     ├─ WHEEL
│     │        │  │     └─ top_level.txt
│     │        │  ├─ _version.py
│     │        │  ├─ _xmlgen.py
│     │        │  ├─ error.pyi
│     │        │  ├─ iniconfig.pyi
│     │        │  ├─ io.pyi
│     │        │  ├─ path.pyi
│     │        │  ├─ py.typed
│     │        │  ├─ test.py
│     │        │  └─ xml.pyi
│     │        ├─ py-1.11.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ py.py
│     │        ├─ pycparser
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _ast_gen.cpython-310.pyc
│     │        │  │  ├─ _build_tables.cpython-310.pyc
│     │        │  │  ├─ ast_transforms.cpython-310.pyc
│     │        │  │  ├─ c_ast.cpython-310.pyc
│     │        │  │  ├─ c_generator.cpython-310.pyc
│     │        │  │  ├─ c_lexer.cpython-310.pyc
│     │        │  │  ├─ c_parser.cpython-310.pyc
│     │        │  │  ├─ lextab.cpython-310.pyc
│     │        │  │  ├─ plyparser.cpython-310.pyc
│     │        │  │  └─ yacctab.cpython-310.pyc
│     │        │  ├─ _ast_gen.py
│     │        │  ├─ _build_tables.py
│     │        │  ├─ _c_ast.cfg
│     │        │  ├─ ast_transforms.py
│     │        │  ├─ c_ast.py
│     │        │  ├─ c_generator.py
│     │        │  ├─ c_lexer.py
│     │        │  ├─ c_parser.py
│     │        │  ├─ lextab.py
│     │        │  ├─ ply
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cpp.cpython-310.pyc
│     │        │  │  │  ├─ ctokens.cpython-310.pyc
│     │        │  │  │  ├─ lex.cpython-310.pyc
│     │        │  │  │  ├─ yacc.cpython-310.pyc
│     │        │  │  │  └─ ygen.cpython-310.pyc
│     │        │  │  ├─ cpp.py
│     │        │  │  ├─ ctokens.py
│     │        │  │  ├─ lex.py
│     │        │  │  ├─ yacc.py
│     │        │  │  └─ ygen.py
│     │        │  ├─ plyparser.py
│     │        │  └─ yacctab.py
│     │        ├─ pycparser-2.21.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ pydantic
│     │        │  ├─ __init__.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _hypothesis_plugin.cpython-310.pyc
│     │        │  │  ├─ annotated_types.cpython-310.pyc
│     │        │  │  ├─ class_validators.cpython-310.pyc
│     │        │  │  ├─ color.cpython-310.pyc
│     │        │  │  ├─ config.cpython-310.pyc
│     │        │  │  ├─ dataclasses.cpython-310.pyc
│     │        │  │  ├─ datetime_parse.cpython-310.pyc
│     │        │  │  ├─ decorator.cpython-310.pyc
│     │        │  │  ├─ env_settings.cpython-310.pyc
│     │        │  │  ├─ error_wrappers.cpython-310.pyc
│     │        │  │  ├─ errors.cpython-310.pyc
│     │        │  │  ├─ fields.cpython-310.pyc
│     │        │  │  ├─ generics.cpython-310.pyc
│     │        │  │  ├─ json.cpython-310.pyc
│     │        │  │  ├─ main.cpython-310.pyc
│     │        │  │  ├─ mypy.cpython-310.pyc
│     │        │  │  ├─ networks.cpython-310.pyc
│     │        │  │  ├─ parse.cpython-310.pyc
│     │        │  │  ├─ schema.cpython-310.pyc
│     │        │  │  ├─ tools.cpython-310.pyc
│     │        │  │  ├─ types.cpython-310.pyc
│     │        │  │  ├─ typing.cpython-310.pyc
│     │        │  │  ├─ utils.cpython-310.pyc
│     │        │  │  ├─ validators.cpython-310.pyc
│     │        │  │  └─ version.cpython-310.pyc
│     │        │  ├─ _hypothesis_plugin.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ _hypothesis_plugin.py
│     │        │  ├─ annotated_types.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ annotated_types.py
│     │        │  ├─ class_validators.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ class_validators.py
│     │        │  ├─ color.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ color.py
│     │        │  ├─ config.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ config.py
│     │        │  ├─ dataclasses.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ dataclasses.py
│     │        │  ├─ datetime_parse.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ datetime_parse.py
│     │        │  ├─ decorator.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ decorator.py
│     │        │  ├─ env_settings.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ env_settings.py
│     │        │  ├─ error_wrappers.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ error_wrappers.py
│     │        │  ├─ errors.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ errors.py
│     │        │  ├─ fields.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ fields.py
│     │        │  ├─ generics.py
│     │        │  ├─ json.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ json.py
│     │        │  ├─ main.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ main.py
│     │        │  ├─ mypy.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ mypy.py
│     │        │  ├─ networks.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ networks.py
│     │        │  ├─ parse.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ parse.py
│     │        │  ├─ py.typed
│     │        │  ├─ schema.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ schema.py
│     │        │  ├─ tools.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ tools.py
│     │        │  ├─ types.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ types.py
│     │        │  ├─ typing.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ typing.py
│     │        │  ├─ utils.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ utils.py
│     │        │  ├─ validators.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ validators.py
│     │        │  ├─ version.cpython-310-x86_64-linux-gnu.so
│     │        │  └─ version.py
│     │        ├─ pydantic-1.10.11.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ pygments
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ cmdline.cpython-310.pyc
│     │        │  │  ├─ console.cpython-310.pyc
│     │        │  │  ├─ filter.cpython-310.pyc
│     │        │  │  ├─ formatter.cpython-310.pyc
│     │        │  │  ├─ lexer.cpython-310.pyc
│     │        │  │  ├─ modeline.cpython-310.pyc
│     │        │  │  ├─ plugin.cpython-310.pyc
│     │        │  │  ├─ regexopt.cpython-310.pyc
│     │        │  │  ├─ scanner.cpython-310.pyc
│     │        │  │  ├─ sphinxext.cpython-310.pyc
│     │        │  │  ├─ style.cpython-310.pyc
│     │        │  │  ├─ token.cpython-310.pyc
│     │        │  │  ├─ unistring.cpython-310.pyc
│     │        │  │  └─ util.cpython-310.pyc
│     │        │  ├─ cmdline.py
│     │        │  ├─ console.py
│     │        │  ├─ filter.py
│     │        │  ├─ filters
│     │        │  │  ├─ __init__.py
│     │        │  │  └─ __pycache__
│     │        │  │     └─ __init__.cpython-310.pyc
│     │        │  ├─ formatter.py
│     │        │  ├─ formatters
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _mapping.cpython-310.pyc
│     │        │  │  │  ├─ bbcode.cpython-310.pyc
│     │        │  │  │  ├─ groff.cpython-310.pyc
│     │        │  │  │  ├─ html.cpython-310.pyc
│     │        │  │  │  ├─ img.cpython-310.pyc
│     │        │  │  │  ├─ irc.cpython-310.pyc
│     │        │  │  │  ├─ latex.cpython-310.pyc
│     │        │  │  │  ├─ other.cpython-310.pyc
│     │        │  │  │  ├─ pangomarkup.cpython-310.pyc
│     │        │  │  │  ├─ rtf.cpython-310.pyc
│     │        │  │  │  ├─ svg.cpython-310.pyc
│     │        │  │  │  ├─ terminal.cpython-310.pyc
│     │        │  │  │  └─ terminal256.cpython-310.pyc
│     │        │  │  ├─ _mapping.py
│     │        │  │  ├─ bbcode.py
│     │        │  │  ├─ groff.py
│     │        │  │  ├─ html.py
│     │        │  │  ├─ img.py
│     │        │  │  ├─ irc.py
│     │        │  │  ├─ latex.py
│     │        │  │  ├─ other.py
│     │        │  │  ├─ pangomarkup.py
│     │        │  │  ├─ rtf.py
│     │        │  │  ├─ svg.py
│     │        │  │  ├─ terminal.py
│     │        │  │  └─ terminal256.py
│     │        │  ├─ lexer.py
│     │        │  ├─ lexers
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _ada_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _asy_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _cl_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _cocoa_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _csound_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _css_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _julia_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _lasso_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _lilypond_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _lua_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _mapping.cpython-310.pyc
│     │        │  │  │  ├─ _mql_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _mysql_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _openedge_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _php_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _postgres_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _qlik_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _scheme_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _scilab_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _sourcemod_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _stan_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _stata_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _tsql_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _usd_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _vbscript_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _vim_builtins.cpython-310.pyc
│     │        │  │  │  ├─ actionscript.cpython-310.pyc
│     │        │  │  │  ├─ ada.cpython-310.pyc
│     │        │  │  │  ├─ agile.cpython-310.pyc
│     │        │  │  │  ├─ algebra.cpython-310.pyc
│     │        │  │  │  ├─ ambient.cpython-310.pyc
│     │        │  │  │  ├─ amdgpu.cpython-310.pyc
│     │        │  │  │  ├─ ampl.cpython-310.pyc
│     │        │  │  │  ├─ apdlexer.cpython-310.pyc
│     │        │  │  │  ├─ apl.cpython-310.pyc
│     │        │  │  │  ├─ archetype.cpython-310.pyc
│     │        │  │  │  ├─ arrow.cpython-310.pyc
│     │        │  │  │  ├─ arturo.cpython-310.pyc
│     │        │  │  │  ├─ asc.cpython-310.pyc
│     │        │  │  │  ├─ asm.cpython-310.pyc
│     │        │  │  │  ├─ automation.cpython-310.pyc
│     │        │  │  │  ├─ bare.cpython-310.pyc
│     │        │  │  │  ├─ basic.cpython-310.pyc
│     │        │  │  │  ├─ bdd.cpython-310.pyc
│     │        │  │  │  ├─ berry.cpython-310.pyc
│     │        │  │  │  ├─ bibtex.cpython-310.pyc
│     │        │  │  │  ├─ boa.cpython-310.pyc
│     │        │  │  │  ├─ business.cpython-310.pyc
│     │        │  │  │  ├─ c_cpp.cpython-310.pyc
│     │        │  │  │  ├─ c_like.cpython-310.pyc
│     │        │  │  │  ├─ capnproto.cpython-310.pyc
│     │        │  │  │  ├─ carbon.cpython-310.pyc
│     │        │  │  │  ├─ cddl.cpython-310.pyc
│     │        │  │  │  ├─ chapel.cpython-310.pyc
│     │        │  │  │  ├─ clean.cpython-310.pyc
│     │        │  │  │  ├─ comal.cpython-310.pyc
│     │        │  │  │  ├─ compiled.cpython-310.pyc
│     │        │  │  │  ├─ configs.cpython-310.pyc
│     │        │  │  │  ├─ console.cpython-310.pyc
│     │        │  │  │  ├─ cplint.cpython-310.pyc
│     │        │  │  │  ├─ crystal.cpython-310.pyc
│     │        │  │  │  ├─ csound.cpython-310.pyc
│     │        │  │  │  ├─ css.cpython-310.pyc
│     │        │  │  │  ├─ d.cpython-310.pyc
│     │        │  │  │  ├─ dalvik.cpython-310.pyc
│     │        │  │  │  ├─ data.cpython-310.pyc
│     │        │  │  │  ├─ dax.cpython-310.pyc
│     │        │  │  │  ├─ devicetree.cpython-310.pyc
│     │        │  │  │  ├─ diff.cpython-310.pyc
│     │        │  │  │  ├─ dotnet.cpython-310.pyc
│     │        │  │  │  ├─ dsls.cpython-310.pyc
│     │        │  │  │  ├─ dylan.cpython-310.pyc
│     │        │  │  │  ├─ ecl.cpython-310.pyc
│     │        │  │  │  ├─ eiffel.cpython-310.pyc
│     │        │  │  │  ├─ elm.cpython-310.pyc
│     │        │  │  │  ├─ elpi.cpython-310.pyc
│     │        │  │  │  ├─ email.cpython-310.pyc
│     │        │  │  │  ├─ erlang.cpython-310.pyc
│     │        │  │  │  ├─ esoteric.cpython-310.pyc
│     │        │  │  │  ├─ ezhil.cpython-310.pyc
│     │        │  │  │  ├─ factor.cpython-310.pyc
│     │        │  │  │  ├─ fantom.cpython-310.pyc
│     │        │  │  │  ├─ felix.cpython-310.pyc
│     │        │  │  │  ├─ fift.cpython-310.pyc
│     │        │  │  │  ├─ floscript.cpython-310.pyc
│     │        │  │  │  ├─ forth.cpython-310.pyc
│     │        │  │  │  ├─ fortran.cpython-310.pyc
│     │        │  │  │  ├─ foxpro.cpython-310.pyc
│     │        │  │  │  ├─ freefem.cpython-310.pyc
│     │        │  │  │  ├─ func.cpython-310.pyc
│     │        │  │  │  ├─ functional.cpython-310.pyc
│     │        │  │  │  ├─ futhark.cpython-310.pyc
│     │        │  │  │  ├─ gcodelexer.cpython-310.pyc
│     │        │  │  │  ├─ gdscript.cpython-310.pyc
│     │        │  │  │  ├─ go.cpython-310.pyc
│     │        │  │  │  ├─ grammar_notation.cpython-310.pyc
│     │        │  │  │  ├─ graph.cpython-310.pyc
│     │        │  │  │  ├─ graphics.cpython-310.pyc
│     │        │  │  │  ├─ graphviz.cpython-310.pyc
│     │        │  │  │  ├─ gsql.cpython-310.pyc
│     │        │  │  │  ├─ haskell.cpython-310.pyc
│     │        │  │  │  ├─ haxe.cpython-310.pyc
│     │        │  │  │  ├─ hdl.cpython-310.pyc
│     │        │  │  │  ├─ hexdump.cpython-310.pyc
│     │        │  │  │  ├─ html.cpython-310.pyc
│     │        │  │  │  ├─ idl.cpython-310.pyc
│     │        │  │  │  ├─ igor.cpython-310.pyc
│     │        │  │  │  ├─ inferno.cpython-310.pyc
│     │        │  │  │  ├─ installers.cpython-310.pyc
│     │        │  │  │  ├─ int_fiction.cpython-310.pyc
│     │        │  │  │  ├─ iolang.cpython-310.pyc
│     │        │  │  │  ├─ j.cpython-310.pyc
│     │        │  │  │  ├─ javascript.cpython-310.pyc
│     │        │  │  │  ├─ jmespath.cpython-310.pyc
│     │        │  │  │  ├─ jslt.cpython-310.pyc
│     │        │  │  │  ├─ jsonnet.cpython-310.pyc
│     │        │  │  │  ├─ julia.cpython-310.pyc
│     │        │  │  │  ├─ jvm.cpython-310.pyc
│     │        │  │  │  ├─ kuin.cpython-310.pyc
│     │        │  │  │  ├─ lilypond.cpython-310.pyc
│     │        │  │  │  ├─ lisp.cpython-310.pyc
│     │        │  │  │  ├─ macaulay2.cpython-310.pyc
│     │        │  │  │  ├─ make.cpython-310.pyc
│     │        │  │  │  ├─ markup.cpython-310.pyc
│     │        │  │  │  ├─ math.cpython-310.pyc
│     │        │  │  │  ├─ matlab.cpython-310.pyc
│     │        │  │  │  ├─ maxima.cpython-310.pyc
│     │        │  │  │  ├─ meson.cpython-310.pyc
│     │        │  │  │  ├─ mime.cpython-310.pyc
│     │        │  │  │  ├─ minecraft.cpython-310.pyc
│     │        │  │  │  ├─ mips.cpython-310.pyc
│     │        │  │  │  ├─ ml.cpython-310.pyc
│     │        │  │  │  ├─ modeling.cpython-310.pyc
│     │        │  │  │  ├─ modula2.cpython-310.pyc
│     │        │  │  │  ├─ monte.cpython-310.pyc
│     │        │  │  │  ├─ mosel.cpython-310.pyc
│     │        │  │  │  ├─ ncl.cpython-310.pyc
│     │        │  │  │  ├─ nimrod.cpython-310.pyc
│     │        │  │  │  ├─ nit.cpython-310.pyc
│     │        │  │  │  ├─ nix.cpython-310.pyc
│     │        │  │  │  ├─ oberon.cpython-310.pyc
│     │        │  │  │  ├─ objective.cpython-310.pyc
│     │        │  │  │  ├─ ooc.cpython-310.pyc
│     │        │  │  │  ├─ other.cpython-310.pyc
│     │        │  │  │  ├─ parasail.cpython-310.pyc
│     │        │  │  │  ├─ parsers.cpython-310.pyc
│     │        │  │  │  ├─ pascal.cpython-310.pyc
│     │        │  │  │  ├─ pawn.cpython-310.pyc
│     │        │  │  │  ├─ perl.cpython-310.pyc
│     │        │  │  │  ├─ phix.cpython-310.pyc
│     │        │  │  │  ├─ php.cpython-310.pyc
│     │        │  │  │  ├─ pointless.cpython-310.pyc
│     │        │  │  │  ├─ pony.cpython-310.pyc
│     │        │  │  │  ├─ praat.cpython-310.pyc
│     │        │  │  │  ├─ procfile.cpython-310.pyc
│     │        │  │  │  ├─ prolog.cpython-310.pyc
│     │        │  │  │  ├─ promql.cpython-310.pyc
│     │        │  │  │  ├─ python.cpython-310.pyc
│     │        │  │  │  ├─ q.cpython-310.pyc
│     │        │  │  │  ├─ qlik.cpython-310.pyc
│     │        │  │  │  ├─ qvt.cpython-310.pyc
│     │        │  │  │  ├─ r.cpython-310.pyc
│     │        │  │  │  ├─ rdf.cpython-310.pyc
│     │        │  │  │  ├─ rebol.cpython-310.pyc
│     │        │  │  │  ├─ resource.cpython-310.pyc
│     │        │  │  │  ├─ ride.cpython-310.pyc
│     │        │  │  │  ├─ rita.cpython-310.pyc
│     │        │  │  │  ├─ rnc.cpython-310.pyc
│     │        │  │  │  ├─ roboconf.cpython-310.pyc
│     │        │  │  │  ├─ robotframework.cpython-310.pyc
│     │        │  │  │  ├─ ruby.cpython-310.pyc
│     │        │  │  │  ├─ rust.cpython-310.pyc
│     │        │  │  │  ├─ sas.cpython-310.pyc
│     │        │  │  │  ├─ savi.cpython-310.pyc
│     │        │  │  │  ├─ scdoc.cpython-310.pyc
│     │        │  │  │  ├─ scripting.cpython-310.pyc
│     │        │  │  │  ├─ sgf.cpython-310.pyc
│     │        │  │  │  ├─ shell.cpython-310.pyc
│     │        │  │  │  ├─ sieve.cpython-310.pyc
│     │        │  │  │  ├─ slash.cpython-310.pyc
│     │        │  │  │  ├─ smalltalk.cpython-310.pyc
│     │        │  │  │  ├─ smithy.cpython-310.pyc
│     │        │  │  │  ├─ smv.cpython-310.pyc
│     │        │  │  │  ├─ snobol.cpython-310.pyc
│     │        │  │  │  ├─ solidity.cpython-310.pyc
│     │        │  │  │  ├─ sophia.cpython-310.pyc
│     │        │  │  │  ├─ special.cpython-310.pyc
│     │        │  │  │  ├─ spice.cpython-310.pyc
│     │        │  │  │  ├─ sql.cpython-310.pyc
│     │        │  │  │  ├─ srcinfo.cpython-310.pyc
│     │        │  │  │  ├─ stata.cpython-310.pyc
│     │        │  │  │  ├─ supercollider.cpython-310.pyc
│     │        │  │  │  ├─ tal.cpython-310.pyc
│     │        │  │  │  ├─ tcl.cpython-310.pyc
│     │        │  │  │  ├─ teal.cpython-310.pyc
│     │        │  │  │  ├─ templates.cpython-310.pyc
│     │        │  │  │  ├─ teraterm.cpython-310.pyc
│     │        │  │  │  ├─ testing.cpython-310.pyc
│     │        │  │  │  ├─ text.cpython-310.pyc
│     │        │  │  │  ├─ textedit.cpython-310.pyc
│     │        │  │  │  ├─ textfmts.cpython-310.pyc
│     │        │  │  │  ├─ theorem.cpython-310.pyc
│     │        │  │  │  ├─ thingsdb.cpython-310.pyc
│     │        │  │  │  ├─ tlb.cpython-310.pyc
│     │        │  │  │  ├─ tnt.cpython-310.pyc
│     │        │  │  │  ├─ trafficscript.cpython-310.pyc
│     │        │  │  │  ├─ typoscript.cpython-310.pyc
│     │        │  │  │  ├─ ul4.cpython-310.pyc
│     │        │  │  │  ├─ unicon.cpython-310.pyc
│     │        │  │  │  ├─ urbi.cpython-310.pyc
│     │        │  │  │  ├─ usd.cpython-310.pyc
│     │        │  │  │  ├─ varnish.cpython-310.pyc
│     │        │  │  │  ├─ verification.cpython-310.pyc
│     │        │  │  │  ├─ web.cpython-310.pyc
│     │        │  │  │  ├─ webassembly.cpython-310.pyc
│     │        │  │  │  ├─ webidl.cpython-310.pyc
│     │        │  │  │  ├─ webmisc.cpython-310.pyc
│     │        │  │  │  ├─ wgsl.cpython-310.pyc
│     │        │  │  │  ├─ whiley.cpython-310.pyc
│     │        │  │  │  ├─ wowtoc.cpython-310.pyc
│     │        │  │  │  ├─ wren.cpython-310.pyc
│     │        │  │  │  ├─ x10.cpython-310.pyc
│     │        │  │  │  ├─ xorg.cpython-310.pyc
│     │        │  │  │  ├─ yang.cpython-310.pyc
│     │        │  │  │  └─ zig.cpython-310.pyc
│     │        │  │  ├─ _ada_builtins.py
│     │        │  │  ├─ _asy_builtins.py
│     │        │  │  ├─ _cl_builtins.py
│     │        │  │  ├─ _cocoa_builtins.py
│     │        │  │  ├─ _csound_builtins.py
│     │        │  │  ├─ _css_builtins.py
│     │        │  │  ├─ _julia_builtins.py
│     │        │  │  ├─ _lasso_builtins.py
│     │        │  │  ├─ _lilypond_builtins.py
│     │        │  │  ├─ _lua_builtins.py
│     │        │  │  ├─ _mapping.py
│     │        │  │  ├─ _mql_builtins.py
│     │        │  │  ├─ _mysql_builtins.py
│     │        │  │  ├─ _openedge_builtins.py
│     │        │  │  ├─ _php_builtins.py
│     │        │  │  ├─ _postgres_builtins.py
│     │        │  │  ├─ _qlik_builtins.py
│     │        │  │  ├─ _scheme_builtins.py
│     │        │  │  ├─ _scilab_builtins.py
│     │        │  │  ├─ _sourcemod_builtins.py
│     │        │  │  ├─ _stan_builtins.py
│     │        │  │  ├─ _stata_builtins.py
│     │        │  │  ├─ _tsql_builtins.py
│     │        │  │  ├─ _usd_builtins.py
│     │        │  │  ├─ _vbscript_builtins.py
│     │        │  │  ├─ _vim_builtins.py
│     │        │  │  ├─ actionscript.py
│     │        │  │  ├─ ada.py
│     │        │  │  ├─ agile.py
│     │        │  │  ├─ algebra.py
│     │        │  │  ├─ ambient.py
│     │        │  │  ├─ amdgpu.py
│     │        │  │  ├─ ampl.py
│     │        │  │  ├─ apdlexer.py
│     │        │  │  ├─ apl.py
│     │        │  │  ├─ archetype.py
│     │        │  │  ├─ arrow.py
│     │        │  │  ├─ arturo.py
│     │        │  │  ├─ asc.py
│     │        │  │  ├─ asm.py
│     │        │  │  ├─ automation.py
│     │        │  │  ├─ bare.py
│     │        │  │  ├─ basic.py
│     │        │  │  ├─ bdd.py
│     │        │  │  ├─ berry.py
│     │        │  │  ├─ bibtex.py
│     │        │  │  ├─ boa.py
│     │        │  │  ├─ business.py
│     │        │  │  ├─ c_cpp.py
│     │        │  │  ├─ c_like.py
│     │        │  │  ├─ capnproto.py
│     │        │  │  ├─ carbon.py
│     │        │  │  ├─ cddl.py
│     │        │  │  ├─ chapel.py
│     │        │  │  ├─ clean.py
│     │        │  │  ├─ comal.py
│     │        │  │  ├─ compiled.py
│     │        │  │  ├─ configs.py
│     │        │  │  ├─ console.py
│     │        │  │  ├─ cplint.py
│     │        │  │  ├─ crystal.py
│     │        │  │  ├─ csound.py
│     │        │  │  ├─ css.py
│     │        │  │  ├─ d.py
│     │        │  │  ├─ dalvik.py
│     │        │  │  ├─ data.py
│     │        │  │  ├─ dax.py
│     │        │  │  ├─ devicetree.py
│     │        │  │  ├─ diff.py
│     │        │  │  ├─ dotnet.py
│     │        │  │  ├─ dsls.py
│     │        │  │  ├─ dylan.py
│     │        │  │  ├─ ecl.py
│     │        │  │  ├─ eiffel.py
│     │        │  │  ├─ elm.py
│     │        │  │  ├─ elpi.py
│     │        │  │  ├─ email.py
│     │        │  │  ├─ erlang.py
│     │        │  │  ├─ esoteric.py
│     │        │  │  ├─ ezhil.py
│     │        │  │  ├─ factor.py
│     │        │  │  ├─ fantom.py
│     │        │  │  ├─ felix.py
│     │        │  │  ├─ fift.py
│     │        │  │  ├─ floscript.py
│     │        │  │  ├─ forth.py
│     │        │  │  ├─ fortran.py
│     │        │  │  ├─ foxpro.py
│     │        │  │  ├─ freefem.py
│     │        │  │  ├─ func.py
│     │        │  │  ├─ functional.py
│     │        │  │  ├─ futhark.py
│     │        │  │  ├─ gcodelexer.py
│     │        │  │  ├─ gdscript.py
│     │        │  │  ├─ go.py
│     │        │  │  ├─ grammar_notation.py
│     │        │  │  ├─ graph.py
│     │        │  │  ├─ graphics.py
│     │        │  │  ├─ graphviz.py
│     │        │  │  ├─ gsql.py
│     │        │  │  ├─ haskell.py
│     │        │  │  ├─ haxe.py
│     │        │  │  ├─ hdl.py
│     │        │  │  ├─ hexdump.py
│     │        │  │  ├─ html.py
│     │        │  │  ├─ idl.py
│     │        │  │  ├─ igor.py
│     │        │  │  ├─ inferno.py
│     │        │  │  ├─ installers.py
│     │        │  │  ├─ int_fiction.py
│     │        │  │  ├─ iolang.py
│     │        │  │  ├─ j.py
│     │        │  │  ├─ javascript.py
│     │        │  │  ├─ jmespath.py
│     │        │  │  ├─ jslt.py
│     │        │  │  ├─ jsonnet.py
│     │        │  │  ├─ julia.py
│     │        │  │  ├─ jvm.py
│     │        │  │  ├─ kuin.py
│     │        │  │  ├─ lilypond.py
│     │        │  │  ├─ lisp.py
│     │        │  │  ├─ macaulay2.py
│     │        │  │  ├─ make.py
│     │        │  │  ├─ markup.py
│     │        │  │  ├─ math.py
│     │        │  │  ├─ matlab.py
│     │        │  │  ├─ maxima.py
│     │        │  │  ├─ meson.py
│     │        │  │  ├─ mime.py
│     │        │  │  ├─ minecraft.py
│     │        │  │  ├─ mips.py
│     │        │  │  ├─ ml.py
│     │        │  │  ├─ modeling.py
│     │        │  │  ├─ modula2.py
│     │        │  │  ├─ monte.py
│     │        │  │  ├─ mosel.py
│     │        │  │  ├─ ncl.py
│     │        │  │  ├─ nimrod.py
│     │        │  │  ├─ nit.py
│     │        │  │  ├─ nix.py
│     │        │  │  ├─ oberon.py
│     │        │  │  ├─ objective.py
│     │        │  │  ├─ ooc.py
│     │        │  │  ├─ other.py
│     │        │  │  ├─ parasail.py
│     │        │  │  ├─ parsers.py
│     │        │  │  ├─ pascal.py
│     │        │  │  ├─ pawn.py
│     │        │  │  ├─ perl.py
│     │        │  │  ├─ phix.py
│     │        │  │  ├─ php.py
│     │        │  │  ├─ pointless.py
│     │        │  │  ├─ pony.py
│     │        │  │  ├─ praat.py
│     │        │  │  ├─ procfile.py
│     │        │  │  ├─ prolog.py
│     │        │  │  ├─ promql.py
│     │        │  │  ├─ python.py
│     │        │  │  ├─ q.py
│     │        │  │  ├─ qlik.py
│     │        │  │  ├─ qvt.py
│     │        │  │  ├─ r.py
│     │        │  │  ├─ rdf.py
│     │        │  │  ├─ rebol.py
│     │        │  │  ├─ resource.py
│     │        │  │  ├─ ride.py
│     │        │  │  ├─ rita.py
│     │        │  │  ├─ rnc.py
│     │        │  │  ├─ roboconf.py
│     │        │  │  ├─ robotframework.py
│     │        │  │  ├─ ruby.py
│     │        │  │  ├─ rust.py
│     │        │  │  ├─ sas.py
│     │        │  │  ├─ savi.py
│     │        │  │  ├─ scdoc.py
│     │        │  │  ├─ scripting.py
│     │        │  │  ├─ sgf.py
│     │        │  │  ├─ shell.py
│     │        │  │  ├─ sieve.py
│     │        │  │  ├─ slash.py
│     │        │  │  ├─ smalltalk.py
│     │        │  │  ├─ smithy.py
│     │        │  │  ├─ smv.py
│     │        │  │  ├─ snobol.py
│     │        │  │  ├─ solidity.py
│     │        │  │  ├─ sophia.py
│     │        │  │  ├─ special.py
│     │        │  │  ├─ spice.py
│     │        │  │  ├─ sql.py
│     │        │  │  ├─ srcinfo.py
│     │        │  │  ├─ stata.py
│     │        │  │  ├─ supercollider.py
│     │        │  │  ├─ tal.py
│     │        │  │  ├─ tcl.py
│     │        │  │  ├─ teal.py
│     │        │  │  ├─ templates.py
│     │        │  │  ├─ teraterm.py
│     │        │  │  ├─ testing.py
│     │        │  │  ├─ text.py
│     │        │  │  ├─ textedit.py
│     │        │  │  ├─ textfmts.py
│     │        │  │  ├─ theorem.py
│     │        │  │  ├─ thingsdb.py
│     │        │  │  ├─ tlb.py
│     │        │  │  ├─ tnt.py
│     │        │  │  ├─ trafficscript.py
│     │        │  │  ├─ typoscript.py
│     │        │  │  ├─ ul4.py
│     │        │  │  ├─ unicon.py
│     │        │  │  ├─ urbi.py
│     │        │  │  ├─ usd.py
│     │        │  │  ├─ varnish.py
│     │        │  │  ├─ verification.py
│     │        │  │  ├─ web.py
│     │        │  │  ├─ webassembly.py
│     │        │  │  ├─ webidl.py
│     │        │  │  ├─ webmisc.py
│     │        │  │  ├─ wgsl.py
│     │        │  │  ├─ whiley.py
│     │        │  │  ├─ wowtoc.py
│     │        │  │  ├─ wren.py
│     │        │  │  ├─ x10.py
│     │        │  │  ├─ xorg.py
│     │        │  │  ├─ yang.py
│     │        │  │  └─ zig.py
│     │        │  ├─ modeline.py
│     │        │  ├─ plugin.py
│     │        │  ├─ regexopt.py
│     │        │  ├─ scanner.py
│     │        │  ├─ sphinxext.py
│     │        │  ├─ style.py
│     │        │  ├─ styles
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ abap.cpython-310.pyc
│     │        │  │  │  ├─ algol.cpython-310.pyc
│     │        │  │  │  ├─ algol_nu.cpython-310.pyc
│     │        │  │  │  ├─ arduino.cpython-310.pyc
│     │        │  │  │  ├─ autumn.cpython-310.pyc
│     │        │  │  │  ├─ borland.cpython-310.pyc
│     │        │  │  │  ├─ bw.cpython-310.pyc
│     │        │  │  │  ├─ colorful.cpython-310.pyc
│     │        │  │  │  ├─ default.cpython-310.pyc
│     │        │  │  │  ├─ dracula.cpython-310.pyc
│     │        │  │  │  ├─ emacs.cpython-310.pyc
│     │        │  │  │  ├─ friendly.cpython-310.pyc
│     │        │  │  │  ├─ friendly_grayscale.cpython-310.pyc
│     │        │  │  │  ├─ fruity.cpython-310.pyc
│     │        │  │  │  ├─ gh_dark.cpython-310.pyc
│     │        │  │  │  ├─ gruvbox.cpython-310.pyc
│     │        │  │  │  ├─ igor.cpython-310.pyc
│     │        │  │  │  ├─ inkpot.cpython-310.pyc
│     │        │  │  │  ├─ lilypond.cpython-310.pyc
│     │        │  │  │  ├─ lovelace.cpython-310.pyc
│     │        │  │  │  ├─ manni.cpython-310.pyc
│     │        │  │  │  ├─ material.cpython-310.pyc
│     │        │  │  │  ├─ monokai.cpython-310.pyc
│     │        │  │  │  ├─ murphy.cpython-310.pyc
│     │        │  │  │  ├─ native.cpython-310.pyc
│     │        │  │  │  ├─ nord.cpython-310.pyc
│     │        │  │  │  ├─ onedark.cpython-310.pyc
│     │        │  │  │  ├─ paraiso_dark.cpython-310.pyc
│     │        │  │  │  ├─ paraiso_light.cpython-310.pyc
│     │        │  │  │  ├─ pastie.cpython-310.pyc
│     │        │  │  │  ├─ perldoc.cpython-310.pyc
│     │        │  │  │  ├─ rainbow_dash.cpython-310.pyc
│     │        │  │  │  ├─ rrt.cpython-310.pyc
│     │        │  │  │  ├─ sas.cpython-310.pyc
│     │        │  │  │  ├─ solarized.cpython-310.pyc
│     │        │  │  │  ├─ staroffice.cpython-310.pyc
│     │        │  │  │  ├─ stata_dark.cpython-310.pyc
│     │        │  │  │  ├─ stata_light.cpython-310.pyc
│     │        │  │  │  ├─ tango.cpython-310.pyc
│     │        │  │  │  ├─ trac.cpython-310.pyc
│     │        │  │  │  ├─ vim.cpython-310.pyc
│     │        │  │  │  ├─ vs.cpython-310.pyc
│     │        │  │  │  ├─ xcode.cpython-310.pyc
│     │        │  │  │  └─ zenburn.cpython-310.pyc
│     │        │  │  ├─ abap.py
│     │        │  │  ├─ algol.py
│     │        │  │  ├─ algol_nu.py
│     │        │  │  ├─ arduino.py
│     │        │  │  ├─ autumn.py
│     │        │  │  ├─ borland.py
│     │        │  │  ├─ bw.py
│     │        │  │  ├─ colorful.py
│     │        │  │  ├─ default.py
│     │        │  │  ├─ dracula.py
│     │        │  │  ├─ emacs.py
│     │        │  │  ├─ friendly.py
│     │        │  │  ├─ friendly_grayscale.py
│     │        │  │  ├─ fruity.py
│     │        │  │  ├─ gh_dark.py
│     │        │  │  ├─ gruvbox.py
│     │        │  │  ├─ igor.py
│     │        │  │  ├─ inkpot.py
│     │        │  │  ├─ lilypond.py
│     │        │  │  ├─ lovelace.py
│     │        │  │  ├─ manni.py
│     │        │  │  ├─ material.py
│     │        │  │  ├─ monokai.py
│     │        │  │  ├─ murphy.py
│     │        │  │  ├─ native.py
│     │        │  │  ├─ nord.py
│     │        │  │  ├─ onedark.py
│     │        │  │  ├─ paraiso_dark.py
│     │        │  │  ├─ paraiso_light.py
│     │        │  │  ├─ pastie.py
│     │        │  │  ├─ perldoc.py
│     │        │  │  ├─ rainbow_dash.py
│     │        │  │  ├─ rrt.py
│     │        │  │  ├─ sas.py
│     │        │  │  ├─ solarized.py
│     │        │  │  ├─ staroffice.py
│     │        │  │  ├─ stata_dark.py
│     │        │  │  ├─ stata_light.py
│     │        │  │  ├─ tango.py
│     │        │  │  ├─ trac.py
│     │        │  │  ├─ vim.py
│     │        │  │  ├─ vs.py
│     │        │  │  ├─ xcode.py
│     │        │  │  └─ zenburn.py
│     │        │  ├─ token.py
│     │        │  ├─ unistring.py
│     │        │  └─ util.py
│     │        ├─ pytest
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  └─ __main__.cpython-310.pyc
│     │        │  └─ py.typed
│     │        ├─ pytest-7.4.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ pytest_asyncio
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  ├─ plugin.cpython-310-pytest-7.4.0.pyc
│     │        │  │  └─ plugin.cpython-310.pyc
│     │        │  ├─ _version.py
│     │        │  ├─ plugin.py
│     │        │  └─ py.typed
│     │        ├─ pytest_asyncio-0.21.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ pytest_html
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __version.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ __version.cpython-310.pyc
│     │        │  │  ├─ extras.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ extras.cpython-310.pyc
│     │        │  │  ├─ html_report.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ html_report.cpython-310.pyc
│     │        │  │  ├─ outcome.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ outcome.cpython-310.pyc
│     │        │  │  ├─ plugin.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ plugin.cpython-310.pyc
│     │        │  │  ├─ result.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ result.cpython-310.pyc
│     │        │  │  ├─ util.cpython-310-pytest-7.4.0.pyc
│     │        │  │  └─ util.cpython-310.pyc
│     │        │  ├─ __version.py
│     │        │  ├─ extras.py
│     │        │  ├─ html_report.py
│     │        │  ├─ outcome.py
│     │        │  ├─ plugin.py
│     │        │  ├─ resources
│     │        │  │  ├─ main.js
│     │        │  │  └─ style.css
│     │        │  ├─ result.py
│     │        │  └─ util.py
│     │        ├─ pytest_html-3.2.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ pytest_metadata
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __version.cpython-310.pyc
│     │        │  │  ├─ plugin.cpython-310-pytest-7.4.0.pyc
│     │        │  │  └─ plugin.cpython-310.pyc
│     │        │  ├─ __version.py
│     │        │  ├─ ci
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ appveyor.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ appveyor.cpython-310.pyc
│     │        │  │  │  ├─ bitbucket.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ bitbucket.cpython-310.pyc
│     │        │  │  │  ├─ circleci.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ circleci.cpython-310.pyc
│     │        │  │  │  ├─ gitlab_ci.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ gitlab_ci.cpython-310.pyc
│     │        │  │  │  ├─ jenkins.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ jenkins.cpython-310.pyc
│     │        │  │  │  ├─ taskcluster.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ taskcluster.cpython-310.pyc
│     │        │  │  │  ├─ travis_ci.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  └─ travis_ci.cpython-310.pyc
│     │        │  │  ├─ appveyor.py
│     │        │  │  ├─ bitbucket.py
│     │        │  │  ├─ circleci.py
│     │        │  │  ├─ gitlab_ci.py
│     │        │  │  ├─ jenkins.py
│     │        │  │  ├─ taskcluster.py
│     │        │  │  └─ travis_ci.py
│     │        │  └─ plugin.py
│     │        ├─ pytest_metadata-3.0.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ licenses
│     │        │     ├─ AUTHORS
│     │        │     └─ LICENSE
│     │        ├─ pytest_mock
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _util.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ _util.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  ├─ plugin.cpython-310-pytest-7.4.0.pyc
│     │        │  │  └─ plugin.cpython-310.pyc
│     │        │  ├─ _util.py
│     │        │  ├─ _version.py
│     │        │  ├─ plugin.py
│     │        │  └─ py.typed
│     │        ├─ pytest_mock-3.11.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ python_dateutil-2.8.2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ top_level.txt
│     │        │  └─ zip-safe
│     │        ├─ python_decouple-3.8.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ python_dotenv-1.0.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ rich
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ _cell_widths.cpython-310.pyc
│     │        │  │  ├─ _emoji_codes.cpython-310.pyc
│     │        │  │  ├─ _emoji_replace.cpython-310.pyc
│     │        │  │  ├─ _export_format.cpython-310.pyc
│     │        │  │  ├─ _extension.cpython-310.pyc
│     │        │  │  ├─ _fileno.cpython-310.pyc
│     │        │  │  ├─ _inspect.cpython-310.pyc
│     │        │  │  ├─ _log_render.cpython-310.pyc
│     │        │  │  ├─ _loop.cpython-310.pyc
│     │        │  │  ├─ _null_file.cpython-310.pyc
│     │        │  │  ├─ _palettes.cpython-310.pyc
│     │        │  │  ├─ _pick.cpython-310.pyc
│     │        │  │  ├─ _ratio.cpython-310.pyc
│     │        │  │  ├─ _spinners.cpython-310.pyc
│     │        │  │  ├─ _stack.cpython-310.pyc
│     │        │  │  ├─ _timer.cpython-310.pyc
│     │        │  │  ├─ _win32_console.cpython-310.pyc
│     │        │  │  ├─ _windows.cpython-310.pyc
│     │        │  │  ├─ _windows_renderer.cpython-310.pyc
│     │        │  │  ├─ _wrap.cpython-310.pyc
│     │        │  │  ├─ abc.cpython-310.pyc
│     │        │  │  ├─ align.cpython-310.pyc
│     │        │  │  ├─ ansi.cpython-310.pyc
│     │        │  │  ├─ bar.cpython-310.pyc
│     │        │  │  ├─ box.cpython-310.pyc
│     │        │  │  ├─ cells.cpython-310.pyc
│     │        │  │  ├─ color.cpython-310.pyc
│     │        │  │  ├─ color_triplet.cpython-310.pyc
│     │        │  │  ├─ columns.cpython-310.pyc
│     │        │  │  ├─ console.cpython-310.pyc
│     │        │  │  ├─ constrain.cpython-310.pyc
│     │        │  │  ├─ containers.cpython-310.pyc
│     │        │  │  ├─ control.cpython-310.pyc
│     │        │  │  ├─ default_styles.cpython-310.pyc
│     │        │  │  ├─ diagnose.cpython-310.pyc
│     │        │  │  ├─ emoji.cpython-310.pyc
│     │        │  │  ├─ errors.cpython-310.pyc
│     │        │  │  ├─ file_proxy.cpython-310.pyc
│     │        │  │  ├─ filesize.cpython-310.pyc
│     │        │  │  ├─ highlighter.cpython-310.pyc
│     │        │  │  ├─ json.cpython-310.pyc
│     │        │  │  ├─ jupyter.cpython-310.pyc
│     │        │  │  ├─ layout.cpython-310.pyc
│     │        │  │  ├─ live.cpython-310.pyc
│     │        │  │  ├─ live_render.cpython-310.pyc
│     │        │  │  ├─ logging.cpython-310.pyc
│     │        │  │  ├─ markdown.cpython-310.pyc
│     │        │  │  ├─ markup.cpython-310.pyc
│     │        │  │  ├─ measure.cpython-310.pyc
│     │        │  │  ├─ padding.cpython-310.pyc
│     │        │  │  ├─ pager.cpython-310.pyc
│     │        │  │  ├─ palette.cpython-310.pyc
│     │        │  │  ├─ panel.cpython-310.pyc
│     │        │  │  ├─ pretty.cpython-310.pyc
│     │        │  │  ├─ progress.cpython-310.pyc
│     │        │  │  ├─ progress_bar.cpython-310.pyc
│     │        │  │  ├─ prompt.cpython-310.pyc
│     │        │  │  ├─ protocol.cpython-310.pyc
│     │        │  │  ├─ region.cpython-310.pyc
│     │        │  │  ├─ repr.cpython-310.pyc
│     │        │  │  ├─ rule.cpython-310.pyc
│     │        │  │  ├─ scope.cpython-310.pyc
│     │        │  │  ├─ screen.cpython-310.pyc
│     │        │  │  ├─ segment.cpython-310.pyc
│     │        │  │  ├─ spinner.cpython-310.pyc
│     │        │  │  ├─ status.cpython-310.pyc
│     │        │  │  ├─ style.cpython-310.pyc
│     │        │  │  ├─ styled.cpython-310.pyc
│     │        │  │  ├─ syntax.cpython-310.pyc
│     │        │  │  ├─ table.cpython-310.pyc
│     │        │  │  ├─ terminal_theme.cpython-310.pyc
│     │        │  │  ├─ text.cpython-310.pyc
│     │        │  │  ├─ theme.cpython-310.pyc
│     │        │  │  ├─ themes.cpython-310.pyc
│     │        │  │  ├─ traceback.cpython-310.pyc
│     │        │  │  └─ tree.cpython-310.pyc
│     │        │  ├─ _cell_widths.py
│     │        │  ├─ _emoji_codes.py
│     │        │  ├─ _emoji_replace.py
│     │        │  ├─ _export_format.py
│     │        │  ├─ _extension.py
│     │        │  ├─ _fileno.py
│     │        │  ├─ _inspect.py
│     │        │  ├─ _log_render.py
│     │        │  ├─ _loop.py
│     │        │  ├─ _null_file.py
│     │        │  ├─ _palettes.py
│     │        │  ├─ _pick.py
│     │        │  ├─ _ratio.py
│     │        │  ├─ _spinners.py
│     │        │  ├─ _stack.py
│     │        │  ├─ _timer.py
│     │        │  ├─ _win32_console.py
│     │        │  ├─ _windows.py
│     │        │  ├─ _windows_renderer.py
│     │        │  ├─ _wrap.py
│     │        │  ├─ abc.py
│     │        │  ├─ align.py
│     │        │  ├─ ansi.py
│     │        │  ├─ bar.py
│     │        │  ├─ box.py
│     │        │  ├─ cells.py
│     │        │  ├─ color.py
│     │        │  ├─ color_triplet.py
│     │        │  ├─ columns.py
│     │        │  ├─ console.py
│     │        │  ├─ constrain.py
│     │        │  ├─ containers.py
│     │        │  ├─ control.py
│     │        │  ├─ default_styles.py
│     │        │  ├─ diagnose.py
│     │        │  ├─ emoji.py
│     │        │  ├─ errors.py
│     │        │  ├─ file_proxy.py
│     │        │  ├─ filesize.py
│     │        │  ├─ highlighter.py
│     │        │  ├─ json.py
│     │        │  ├─ jupyter.py
│     │        │  ├─ layout.py
│     │        │  ├─ live.py
│     │        │  ├─ live_render.py
│     │        │  ├─ logging.py
│     │        │  ├─ markdown.py
│     │        │  ├─ markup.py
│     │        │  ├─ measure.py
│     │        │  ├─ padding.py
│     │        │  ├─ pager.py
│     │        │  ├─ palette.py
│     │        │  ├─ panel.py
│     │        │  ├─ pretty.py
│     │        │  ├─ progress.py
│     │        │  ├─ progress_bar.py
│     │        │  ├─ prompt.py
│     │        │  ├─ protocol.py
│     │        │  ├─ py.typed
│     │        │  ├─ region.py
│     │        │  ├─ repr.py
│     │        │  ├─ rule.py
│     │        │  ├─ scope.py
│     │        │  ├─ screen.py
│     │        │  ├─ segment.py
│     │        │  ├─ spinner.py
│     │        │  ├─ status.py
│     │        │  ├─ style.py
│     │        │  ├─ styled.py
│     │        │  ├─ syntax.py
│     │        │  ├─ table.py
│     │        │  ├─ terminal_theme.py
│     │        │  ├─ text.py
│     │        │  ├─ theme.py
│     │        │  ├─ themes.py
│     │        │  ├─ traceback.py
│     │        │  └─ tree.py
│     │        ├─ rich-13.4.2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ rich_click
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ cli.cpython-310.pyc
│     │        │  │  ├─ rich_click.cpython-310.pyc
│     │        │  │  ├─ rich_command.cpython-310.pyc
│     │        │  │  └─ rich_group.cpython-310.pyc
│     │        │  ├─ cli.py
│     │        │  ├─ py.typed
│     │        │  ├─ rich_click.py
│     │        │  ├─ rich_command.py
│     │        │  └─ rich_group.py
│     │        ├─ rich_click-1.6.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ ruff
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  └─ __pycache__
│     │        │     ├─ __init__.cpython-310.pyc
│     │        │     └─ __main__.cpython-310.pyc
│     │        ├─ ruff-0.0.277.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ license_files
│     │        │     └─ LICENSE
│     │        ├─ setuptools
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _deprecation_warning.cpython-310.pyc
│     │        │  │  ├─ _imp.cpython-310.pyc
│     │        │  │  ├─ archive_util.cpython-310.pyc
│     │        │  │  ├─ build_meta.cpython-310.pyc
│     │        │  │  ├─ config.cpython-310.pyc
│     │        │  │  ├─ dep_util.cpython-310.pyc
│     │        │  │  ├─ depends.cpython-310.pyc
│     │        │  │  ├─ dist.cpython-310.pyc
│     │        │  │  ├─ errors.cpython-310.pyc
│     │        │  │  ├─ extension.cpython-310.pyc
│     │        │  │  ├─ glob.cpython-310.pyc
│     │        │  │  ├─ installer.cpython-310.pyc
│     │        │  │  ├─ launch.cpython-310.pyc
│     │        │  │  ├─ monkey.cpython-310.pyc
│     │        │  │  ├─ msvc.cpython-310.pyc
│     │        │  │  ├─ namespaces.cpython-310.pyc
│     │        │  │  ├─ package_index.cpython-310.pyc
│     │        │  │  ├─ py34compat.cpython-310.pyc
│     │        │  │  ├─ sandbox.cpython-310.pyc
│     │        │  │  ├─ unicode_utils.cpython-310.pyc
│     │        │  │  ├─ version.cpython-310.pyc
│     │        │  │  ├─ wheel.cpython-310.pyc
│     │        │  │  └─ windows_support.cpython-310.pyc
│     │        │  ├─ _deprecation_warning.py
│     │        │  ├─ _distutils
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _msvccompiler.cpython-310.pyc
│     │        │  │  │  ├─ archive_util.cpython-310.pyc
│     │        │  │  │  ├─ bcppcompiler.cpython-310.pyc
│     │        │  │  │  ├─ ccompiler.cpython-310.pyc
│     │        │  │  │  ├─ cmd.cpython-310.pyc
│     │        │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  ├─ core.cpython-310.pyc
│     │        │  │  │  ├─ cygwinccompiler.cpython-310.pyc
│     │        │  │  │  ├─ debug.cpython-310.pyc
│     │        │  │  │  ├─ dep_util.cpython-310.pyc
│     │        │  │  │  ├─ dir_util.cpython-310.pyc
│     │        │  │  │  ├─ dist.cpython-310.pyc
│     │        │  │  │  ├─ errors.cpython-310.pyc
│     │        │  │  │  ├─ extension.cpython-310.pyc
│     │        │  │  │  ├─ fancy_getopt.cpython-310.pyc
│     │        │  │  │  ├─ file_util.cpython-310.pyc
│     │        │  │  │  ├─ filelist.cpython-310.pyc
│     │        │  │  │  ├─ log.cpython-310.pyc
│     │        │  │  │  ├─ msvc9compiler.cpython-310.pyc
│     │        │  │  │  ├─ msvccompiler.cpython-310.pyc
│     │        │  │  │  ├─ py35compat.cpython-310.pyc
│     │        │  │  │  ├─ py38compat.cpython-310.pyc
│     │        │  │  │  ├─ spawn.cpython-310.pyc
│     │        │  │  │  ├─ sysconfig.cpython-310.pyc
│     │        │  │  │  ├─ text_file.cpython-310.pyc
│     │        │  │  │  ├─ unixccompiler.cpython-310.pyc
│     │        │  │  │  ├─ util.cpython-310.pyc
│     │        │  │  │  ├─ version.cpython-310.pyc
│     │        │  │  │  └─ versionpredicate.cpython-310.pyc
│     │        │  │  ├─ _msvccompiler.py
│     │        │  │  ├─ archive_util.py
│     │        │  │  ├─ bcppcompiler.py
│     │        │  │  ├─ ccompiler.py
│     │        │  │  ├─ cmd.py
│     │        │  │  ├─ command
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ bdist.cpython-310.pyc
│     │        │  │  │  │  ├─ bdist_dumb.cpython-310.pyc
│     │        │  │  │  │  ├─ bdist_msi.cpython-310.pyc
│     │        │  │  │  │  ├─ bdist_rpm.cpython-310.pyc
│     │        │  │  │  │  ├─ bdist_wininst.cpython-310.pyc
│     │        │  │  │  │  ├─ build.cpython-310.pyc
│     │        │  │  │  │  ├─ build_clib.cpython-310.pyc
│     │        │  │  │  │  ├─ build_ext.cpython-310.pyc
│     │        │  │  │  │  ├─ build_py.cpython-310.pyc
│     │        │  │  │  │  ├─ build_scripts.cpython-310.pyc
│     │        │  │  │  │  ├─ check.cpython-310.pyc
│     │        │  │  │  │  ├─ clean.cpython-310.pyc
│     │        │  │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  │  ├─ install.cpython-310.pyc
│     │        │  │  │  │  ├─ install_data.cpython-310.pyc
│     │        │  │  │  │  ├─ install_egg_info.cpython-310.pyc
│     │        │  │  │  │  ├─ install_headers.cpython-310.pyc
│     │        │  │  │  │  ├─ install_lib.cpython-310.pyc
│     │        │  │  │  │  ├─ install_scripts.cpython-310.pyc
│     │        │  │  │  │  ├─ py37compat.cpython-310.pyc
│     │        │  │  │  │  ├─ register.cpython-310.pyc
│     │        │  │  │  │  ├─ sdist.cpython-310.pyc
│     │        │  │  │  │  └─ upload.cpython-310.pyc
│     │        │  │  │  ├─ bdist.py
│     │        │  │  │  ├─ bdist_dumb.py
│     │        │  │  │  ├─ bdist_msi.py
│     │        │  │  │  ├─ bdist_rpm.py
│     │        │  │  │  ├─ bdist_wininst.py
│     │        │  │  │  ├─ build.py
│     │        │  │  │  ├─ build_clib.py
│     │        │  │  │  ├─ build_ext.py
│     │        │  │  │  ├─ build_py.py
│     │        │  │  │  ├─ build_scripts.py
│     │        │  │  │  ├─ check.py
│     │        │  │  │  ├─ clean.py
│     │        │  │  │  ├─ config.py
│     │        │  │  │  ├─ install.py
│     │        │  │  │  ├─ install_data.py
│     │        │  │  │  ├─ install_egg_info.py
│     │        │  │  │  ├─ install_headers.py
│     │        │  │  │  ├─ install_lib.py
│     │        │  │  │  ├─ install_scripts.py
│     │        │  │  │  ├─ py37compat.py
│     │        │  │  │  ├─ register.py
│     │        │  │  │  ├─ sdist.py
│     │        │  │  │  └─ upload.py
│     │        │  │  ├─ config.py
│     │        │  │  ├─ core.py
│     │        │  │  ├─ cygwinccompiler.py
│     │        │  │  ├─ debug.py
│     │        │  │  ├─ dep_util.py
│     │        │  │  ├─ dir_util.py
│     │        │  │  ├─ dist.py
│     │        │  │  ├─ errors.py
│     │        │  │  ├─ extension.py
│     │        │  │  ├─ fancy_getopt.py
│     │        │  │  ├─ file_util.py
│     │        │  │  ├─ filelist.py
│     │        │  │  ├─ log.py
│     │        │  │  ├─ msvc9compiler.py
│     │        │  │  ├─ msvccompiler.py
│     │        │  │  ├─ py35compat.py
│     │        │  │  ├─ py38compat.py
│     │        │  │  ├─ spawn.py
│     │        │  │  ├─ sysconfig.py
│     │        │  │  ├─ text_file.py
│     │        │  │  ├─ unixccompiler.py
│     │        │  │  ├─ util.py
│     │        │  │  ├─ version.py
│     │        │  │  └─ versionpredicate.py
│     │        │  ├─ _imp.py
│     │        │  ├─ _vendor
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ordered_set.cpython-310.pyc
│     │        │  │  │  └─ pyparsing.cpython-310.pyc
│     │        │  │  ├─ more_itertools
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ more.cpython-310.pyc
│     │        │  │  │  │  └─ recipes.cpython-310.pyc
│     │        │  │  │  ├─ more.py
│     │        │  │  │  └─ recipes.py
│     │        │  │  ├─ ordered_set.py
│     │        │  │  ├─ packaging
│     │        │  │  │  ├─ __about__.py
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __about__.cpython-310.pyc
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _manylinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _musllinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _structures.cpython-310.pyc
│     │        │  │  │  │  ├─ markers.cpython-310.pyc
│     │        │  │  │  │  ├─ requirements.cpython-310.pyc
│     │        │  │  │  │  ├─ specifiers.cpython-310.pyc
│     │        │  │  │  │  ├─ tags.cpython-310.pyc
│     │        │  │  │  │  ├─ utils.cpython-310.pyc
│     │        │  │  │  │  └─ version.cpython-310.pyc
│     │        │  │  │  ├─ _manylinux.py
│     │        │  │  │  ├─ _musllinux.py
│     │        │  │  │  ├─ _structures.py
│     │        │  │  │  ├─ markers.py
│     │        │  │  │  ├─ requirements.py
│     │        │  │  │  ├─ specifiers.py
│     │        │  │  │  ├─ tags.py
│     │        │  │  │  ├─ utils.py
│     │        │  │  │  └─ version.py
│     │        │  │  └─ pyparsing.py
│     │        │  ├─ archive_util.py
│     │        │  ├─ build_meta.py
│     │        │  ├─ cli-32.exe
│     │        │  ├─ cli-64.exe
│     │        │  ├─ cli-arm64.exe
│     │        │  ├─ cli.exe
│     │        │  ├─ command
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ alias.cpython-310.pyc
│     │        │  │  │  ├─ bdist_egg.cpython-310.pyc
│     │        │  │  │  ├─ bdist_rpm.cpython-310.pyc
│     │        │  │  │  ├─ build_clib.cpython-310.pyc
│     │        │  │  │  ├─ build_ext.cpython-310.pyc
│     │        │  │  │  ├─ build_py.cpython-310.pyc
│     │        │  │  │  ├─ develop.cpython-310.pyc
│     │        │  │  │  ├─ dist_info.cpython-310.pyc
│     │        │  │  │  ├─ easy_install.cpython-310.pyc
│     │        │  │  │  ├─ egg_info.cpython-310.pyc
│     │        │  │  │  ├─ install.cpython-310.pyc
│     │        │  │  │  ├─ install_egg_info.cpython-310.pyc
│     │        │  │  │  ├─ install_lib.cpython-310.pyc
│     │        │  │  │  ├─ install_scripts.cpython-310.pyc
│     │        │  │  │  ├─ py36compat.cpython-310.pyc
│     │        │  │  │  ├─ register.cpython-310.pyc
│     │        │  │  │  ├─ rotate.cpython-310.pyc
│     │        │  │  │  ├─ saveopts.cpython-310.pyc
│     │        │  │  │  ├─ sdist.cpython-310.pyc
│     │        │  │  │  ├─ setopt.cpython-310.pyc
│     │        │  │  │  ├─ test.cpython-310.pyc
│     │        │  │  │  ├─ upload.cpython-310.pyc
│     │        │  │  │  └─ upload_docs.cpython-310.pyc
│     │        │  │  ├─ alias.py
│     │        │  │  ├─ bdist_egg.py
│     │        │  │  ├─ bdist_rpm.py
│     │        │  │  ├─ build_clib.py
│     │        │  │  ├─ build_ext.py
│     │        │  │  ├─ build_py.py
│     │        │  │  ├─ develop.py
│     │        │  │  ├─ dist_info.py
│     │        │  │  ├─ easy_install.py
│     │        │  │  ├─ egg_info.py
│     │        │  │  ├─ install.py
│     │        │  │  ├─ install_egg_info.py
│     │        │  │  ├─ install_lib.py
│     │        │  │  ├─ install_scripts.py
│     │        │  │  ├─ launcher manifest.xml
│     │        │  │  ├─ py36compat.py
│     │        │  │  ├─ register.py
│     │        │  │  ├─ rotate.py
│     │        │  │  ├─ saveopts.py
│     │        │  │  ├─ sdist.py
│     │        │  │  ├─ setopt.py
│     │        │  │  ├─ test.py
│     │        │  │  ├─ upload.py
│     │        │  │  └─ upload_docs.py
│     │        │  ├─ config.py
│     │        │  ├─ dep_util.py
│     │        │  ├─ depends.py
│     │        │  ├─ dist.py
│     │        │  ├─ errors.py
│     │        │  ├─ extension.py
│     │        │  ├─ extern
│     │        │  │  ├─ __init__.py
│     │        │  │  └─ __pycache__
│     │        │  │     └─ __init__.cpython-310.pyc
│     │        │  ├─ glob.py
│     │        │  ├─ gui-32.exe
│     │        │  ├─ gui-64.exe
│     │        │  ├─ gui-arm64.exe
│     │        │  ├─ gui.exe
│     │        │  ├─ installer.py
│     │        │  ├─ launch.py
│     │        │  ├─ monkey.py
│     │        │  ├─ msvc.py
│     │        │  ├─ namespaces.py
│     │        │  ├─ package_index.py
│     │        │  ├─ py34compat.py
│     │        │  ├─ sandbox.py
│     │        │  ├─ script (dev).tmpl
│     │        │  ├─ script.tmpl
│     │        │  ├─ unicode_utils.py
│     │        │  ├─ version.py
│     │        │  ├─ wheel.py
│     │        │  └─ windows_support.py
│     │        ├─ setuptools-59.6.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ six-1.16.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ six.py
│     │        ├─ sniffio
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _impl.cpython-310.pyc
│     │        │  │  └─ _version.cpython-310.pyc
│     │        │  ├─ _impl.py
│     │        │  ├─ _tests
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ test_sniffio.cpython-310.pyc
│     │        │  │  └─ test_sniffio.py
│     │        │  ├─ _version.py
│     │        │  └─ py.typed
│     │        ├─ sniffio-1.3.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ LICENSE.APACHE2
│     │        │  ├─ LICENSE.MIT
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ sqlalchemy
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ events.cpython-310.pyc
│     │        │  │  ├─ exc.cpython-310.pyc
│     │        │  │  ├─ inspection.cpython-310.pyc
│     │        │  │  ├─ log.cpython-310.pyc
│     │        │  │  ├─ schema.cpython-310.pyc
│     │        │  │  └─ types.cpython-310.pyc
│     │        │  ├─ connectors
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ pyodbc.cpython-310.pyc
│     │        │  │  └─ pyodbc.py
│     │        │  ├─ cyextension
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ collections.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ collections.pyx
│     │        │  │  ├─ immutabledict.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ immutabledict.pxd
│     │        │  │  ├─ immutabledict.pyx
│     │        │  │  ├─ processors.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ processors.pyx
│     │        │  │  ├─ resultproxy.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ resultproxy.pyx
│     │        │  │  ├─ util.cpython-310-x86_64-linux-gnu.so
│     │        │  │  └─ util.pyx
│     │        │  ├─ dialects
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ mssql
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ information_schema.cpython-310.pyc
│     │        │  │  │  │  ├─ json.cpython-310.pyc
│     │        │  │  │  │  ├─ provision.cpython-310.pyc
│     │        │  │  │  │  ├─ pymssql.cpython-310.pyc
│     │        │  │  │  │  └─ pyodbc.cpython-310.pyc
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ information_schema.py
│     │        │  │  │  ├─ json.py
│     │        │  │  │  ├─ provision.py
│     │        │  │  │  ├─ pymssql.py
│     │        │  │  │  └─ pyodbc.py
│     │        │  │  ├─ mysql
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ aiomysql.cpython-310.pyc
│     │        │  │  │  │  ├─ asyncmy.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ cymysql.cpython-310.pyc
│     │        │  │  │  │  ├─ dml.cpython-310.pyc
│     │        │  │  │  │  ├─ enumerated.cpython-310.pyc
│     │        │  │  │  │  ├─ expression.cpython-310.pyc
│     │        │  │  │  │  ├─ json.cpython-310.pyc
│     │        │  │  │  │  ├─ mariadb.cpython-310.pyc
│     │        │  │  │  │  ├─ mariadbconnector.cpython-310.pyc
│     │        │  │  │  │  ├─ mysqlconnector.cpython-310.pyc
│     │        │  │  │  │  ├─ mysqldb.cpython-310.pyc
│     │        │  │  │  │  ├─ provision.cpython-310.pyc
│     │        │  │  │  │  ├─ pymysql.cpython-310.pyc
│     │        │  │  │  │  ├─ pyodbc.cpython-310.pyc
│     │        │  │  │  │  ├─ reflection.cpython-310.pyc
│     │        │  │  │  │  ├─ reserved_words.cpython-310.pyc
│     │        │  │  │  │  └─ types.cpython-310.pyc
│     │        │  │  │  ├─ aiomysql.py
│     │        │  │  │  ├─ asyncmy.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ cymysql.py
│     │        │  │  │  ├─ dml.py
│     │        │  │  │  ├─ enumerated.py
│     │        │  │  │  ├─ expression.py
│     │        │  │  │  ├─ json.py
│     │        │  │  │  ├─ mariadb.py
│     │        │  │  │  ├─ mariadbconnector.py
│     │        │  │  │  ├─ mysqlconnector.py
│     │        │  │  │  ├─ mysqldb.py
│     │        │  │  │  ├─ provision.py
│     │        │  │  │  ├─ pymysql.py
│     │        │  │  │  ├─ pyodbc.py
│     │        │  │  │  ├─ reflection.py
│     │        │  │  │  ├─ reserved_words.py
│     │        │  │  │  └─ types.py
│     │        │  │  ├─ oracle
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ cx_oracle.cpython-310.pyc
│     │        │  │  │  │  ├─ dictionary.cpython-310.pyc
│     │        │  │  │  │  ├─ oracledb.cpython-310.pyc
│     │        │  │  │  │  ├─ provision.cpython-310.pyc
│     │        │  │  │  │  └─ types.cpython-310.pyc
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ cx_oracle.py
│     │        │  │  │  ├─ dictionary.py
│     │        │  │  │  ├─ oracledb.py
│     │        │  │  │  ├─ provision.py
│     │        │  │  │  └─ types.py
│     │        │  │  ├─ postgresql
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _psycopg_common.cpython-310.pyc
│     │        │  │  │  │  ├─ array.cpython-310.pyc
│     │        │  │  │  │  ├─ asyncpg.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ dml.cpython-310.pyc
│     │        │  │  │  │  ├─ ext.cpython-310.pyc
│     │        │  │  │  │  ├─ hstore.cpython-310.pyc
│     │        │  │  │  │  ├─ json.cpython-310.pyc
│     │        │  │  │  │  ├─ named_types.cpython-310.pyc
│     │        │  │  │  │  ├─ operators.cpython-310.pyc
│     │        │  │  │  │  ├─ pg8000.cpython-310.pyc
│     │        │  │  │  │  ├─ pg_catalog.cpython-310.pyc
│     │        │  │  │  │  ├─ provision.cpython-310.pyc
│     │        │  │  │  │  ├─ psycopg.cpython-310.pyc
│     │        │  │  │  │  ├─ psycopg2.cpython-310.pyc
│     │        │  │  │  │  ├─ psycopg2cffi.cpython-310.pyc
│     │        │  │  │  │  ├─ ranges.cpython-310.pyc
│     │        │  │  │  │  └─ types.cpython-310.pyc
│     │        │  │  │  ├─ _psycopg_common.py
│     │        │  │  │  ├─ array.py
│     │        │  │  │  ├─ asyncpg.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ dml.py
│     │        │  │  │  ├─ ext.py
│     │        │  │  │  ├─ hstore.py
│     │        │  │  │  ├─ json.py
│     │        │  │  │  ├─ named_types.py
│     │        │  │  │  ├─ operators.py
│     │        │  │  │  ├─ pg8000.py
│     │        │  │  │  ├─ pg_catalog.py
│     │        │  │  │  ├─ provision.py
│     │        │  │  │  ├─ psycopg.py
│     │        │  │  │  ├─ psycopg2.py
│     │        │  │  │  ├─ psycopg2cffi.py
│     │        │  │  │  ├─ ranges.py
│     │        │  │  │  └─ types.py
│     │        │  │  ├─ sqlite
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ aiosqlite.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ dml.cpython-310.pyc
│     │        │  │  │  │  ├─ json.cpython-310.pyc
│     │        │  │  │  │  ├─ provision.cpython-310.pyc
│     │        │  │  │  │  ├─ pysqlcipher.cpython-310.pyc
│     │        │  │  │  │  └─ pysqlite.cpython-310.pyc
│     │        │  │  │  ├─ aiosqlite.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ dml.py
│     │        │  │  │  ├─ json.py
│     │        │  │  │  ├─ provision.py
│     │        │  │  │  ├─ pysqlcipher.py
│     │        │  │  │  └─ pysqlite.py
│     │        │  │  └─ type_migration_guidelines.txt
│     │        │  ├─ engine
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _py_processors.cpython-310.pyc
│     │        │  │  │  ├─ _py_row.cpython-310.pyc
│     │        │  │  │  ├─ _py_util.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ characteristics.cpython-310.pyc
│     │        │  │  │  ├─ create.cpython-310.pyc
│     │        │  │  │  ├─ cursor.cpython-310.pyc
│     │        │  │  │  ├─ default.cpython-310.pyc
│     │        │  │  │  ├─ events.cpython-310.pyc
│     │        │  │  │  ├─ interfaces.cpython-310.pyc
│     │        │  │  │  ├─ mock.cpython-310.pyc
│     │        │  │  │  ├─ processors.cpython-310.pyc
│     │        │  │  │  ├─ reflection.cpython-310.pyc
│     │        │  │  │  ├─ result.cpython-310.pyc
│     │        │  │  │  ├─ row.cpython-310.pyc
│     │        │  │  │  ├─ strategies.cpython-310.pyc
│     │        │  │  │  ├─ url.cpython-310.pyc
│     │        │  │  │  └─ util.cpython-310.pyc
│     │        │  │  ├─ _py_processors.py
│     │        │  │  ├─ _py_row.py
│     │        │  │  ├─ _py_util.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ characteristics.py
│     │        │  │  ├─ create.py
│     │        │  │  ├─ cursor.py
│     │        │  │  ├─ default.py
│     │        │  │  ├─ events.py
│     │        │  │  ├─ interfaces.py
│     │        │  │  ├─ mock.py
│     │        │  │  ├─ processors.py
│     │        │  │  ├─ reflection.py
│     │        │  │  ├─ result.py
│     │        │  │  ├─ row.py
│     │        │  │  ├─ strategies.py
│     │        │  │  ├─ url.py
│     │        │  │  └─ util.py
│     │        │  ├─ event
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ api.cpython-310.pyc
│     │        │  │  │  ├─ attr.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ legacy.cpython-310.pyc
│     │        │  │  │  └─ registry.cpython-310.pyc
│     │        │  │  ├─ api.py
│     │        │  │  ├─ attr.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ legacy.py
│     │        │  │  └─ registry.py
│     │        │  ├─ events.py
│     │        │  ├─ exc.py
│     │        │  ├─ ext
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ associationproxy.cpython-310.pyc
│     │        │  │  │  ├─ automap.cpython-310.pyc
│     │        │  │  │  ├─ baked.cpython-310.pyc
│     │        │  │  │  ├─ compiler.cpython-310.pyc
│     │        │  │  │  ├─ horizontal_shard.cpython-310.pyc
│     │        │  │  │  ├─ hybrid.cpython-310.pyc
│     │        │  │  │  ├─ indexable.cpython-310.pyc
│     │        │  │  │  ├─ instrumentation.cpython-310.pyc
│     │        │  │  │  ├─ mutable.cpython-310.pyc
│     │        │  │  │  ├─ orderinglist.cpython-310.pyc
│     │        │  │  │  └─ serializer.cpython-310.pyc
│     │        │  │  ├─ associationproxy.py
│     │        │  │  ├─ asyncio
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ engine.cpython-310.pyc
│     │        │  │  │  │  ├─ exc.cpython-310.pyc
│     │        │  │  │  │  ├─ result.cpython-310.pyc
│     │        │  │  │  │  ├─ scoping.cpython-310.pyc
│     │        │  │  │  │  └─ session.cpython-310.pyc
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ engine.py
│     │        │  │  │  ├─ exc.py
│     │        │  │  │  ├─ result.py
│     │        │  │  │  ├─ scoping.py
│     │        │  │  │  └─ session.py
│     │        │  │  ├─ automap.py
│     │        │  │  ├─ baked.py
│     │        │  │  ├─ compiler.py
│     │        │  │  ├─ declarative
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  └─ extensions.cpython-310.pyc
│     │        │  │  │  └─ extensions.py
│     │        │  │  ├─ horizontal_shard.py
│     │        │  │  ├─ hybrid.py
│     │        │  │  ├─ indexable.py
│     │        │  │  ├─ instrumentation.py
│     │        │  │  ├─ mutable.py
│     │        │  │  ├─ mypy
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ apply.cpython-310.pyc
│     │        │  │  │  │  ├─ decl_class.cpython-310.pyc
│     │        │  │  │  │  ├─ infer.cpython-310.pyc
│     │        │  │  │  │  ├─ names.cpython-310.pyc
│     │        │  │  │  │  ├─ plugin.cpython-310.pyc
│     │        │  │  │  │  └─ util.cpython-310.pyc
│     │        │  │  │  ├─ apply.py
│     │        │  │  │  ├─ decl_class.py
│     │        │  │  │  ├─ infer.py
│     │        │  │  │  ├─ names.py
│     │        │  │  │  ├─ plugin.py
│     │        │  │  │  └─ util.py
│     │        │  │  ├─ orderinglist.py
│     │        │  │  └─ serializer.py
│     │        │  ├─ future
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ engine.cpython-310.pyc
│     │        │  │  └─ engine.py
│     │        │  ├─ inspection.py
│     │        │  ├─ log.py
│     │        │  ├─ orm
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _orm_constructors.cpython-310.pyc
│     │        │  │  │  ├─ _typing.cpython-310.pyc
│     │        │  │  │  ├─ attributes.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ bulk_persistence.cpython-310.pyc
│     │        │  │  │  ├─ clsregistry.cpython-310.pyc
│     │        │  │  │  ├─ collections.cpython-310.pyc
│     │        │  │  │  ├─ context.cpython-310.pyc
│     │        │  │  │  ├─ decl_api.cpython-310.pyc
│     │        │  │  │  ├─ decl_base.cpython-310.pyc
│     │        │  │  │  ├─ dependency.cpython-310.pyc
│     │        │  │  │  ├─ descriptor_props.cpython-310.pyc
│     │        │  │  │  ├─ dynamic.cpython-310.pyc
│     │        │  │  │  ├─ evaluator.cpython-310.pyc
│     │        │  │  │  ├─ events.cpython-310.pyc
│     │        │  │  │  ├─ exc.cpython-310.pyc
│     │        │  │  │  ├─ identity.cpython-310.pyc
│     │        │  │  │  ├─ instrumentation.cpython-310.pyc
│     │        │  │  │  ├─ interfaces.cpython-310.pyc
│     │        │  │  │  ├─ loading.cpython-310.pyc
│     │        │  │  │  ├─ mapped_collection.cpython-310.pyc
│     │        │  │  │  ├─ mapper.cpython-310.pyc
│     │        │  │  │  ├─ path_registry.cpython-310.pyc
│     │        │  │  │  ├─ persistence.cpython-310.pyc
│     │        │  │  │  ├─ properties.cpython-310.pyc
│     │        │  │  │  ├─ query.cpython-310.pyc
│     │        │  │  │  ├─ relationships.cpython-310.pyc
│     │        │  │  │  ├─ scoping.cpython-310.pyc
│     │        │  │  │  ├─ session.cpython-310.pyc
│     │        │  │  │  ├─ state.cpython-310.pyc
│     │        │  │  │  ├─ state_changes.cpython-310.pyc
│     │        │  │  │  ├─ strategies.cpython-310.pyc
│     │        │  │  │  ├─ strategy_options.cpython-310.pyc
│     │        │  │  │  ├─ sync.cpython-310.pyc
│     │        │  │  │  ├─ unitofwork.cpython-310.pyc
│     │        │  │  │  ├─ util.cpython-310.pyc
│     │        │  │  │  └─ writeonly.cpython-310.pyc
│     │        │  │  ├─ _orm_constructors.py
│     │        │  │  ├─ _typing.py
│     │        │  │  ├─ attributes.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ bulk_persistence.py
│     │        │  │  ├─ clsregistry.py
│     │        │  │  ├─ collections.py
│     │        │  │  ├─ context.py
│     │        │  │  ├─ decl_api.py
│     │        │  │  ├─ decl_base.py
│     │        │  │  ├─ dependency.py
│     │        │  │  ├─ descriptor_props.py
│     │        │  │  ├─ dynamic.py
│     │        │  │  ├─ evaluator.py
│     │        │  │  ├─ events.py
│     │        │  │  ├─ exc.py
│     │        │  │  ├─ identity.py
│     │        │  │  ├─ instrumentation.py
│     │        │  │  ├─ interfaces.py
│     │        │  │  ├─ loading.py
│     │        │  │  ├─ mapped_collection.py
│     │        │  │  ├─ mapper.py
│     │        │  │  ├─ path_registry.py
│     │        │  │  ├─ persistence.py
│     │        │  │  ├─ properties.py
│     │        │  │  ├─ query.py
│     │        │  │  ├─ relationships.py
│     │        │  │  ├─ scoping.py
│     │        │  │  ├─ session.py
│     │        │  │  ├─ state.py
│     │        │  │  ├─ state_changes.py
│     │        │  │  ├─ strategies.py
│     │        │  │  ├─ strategy_options.py
│     │        │  │  ├─ sync.py
│     │        │  │  ├─ unitofwork.py
│     │        │  │  ├─ util.py
│     │        │  │  └─ writeonly.py
│     │        │  ├─ pool
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ events.cpython-310.pyc
│     │        │  │  │  └─ impl.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ events.py
│     │        │  │  └─ impl.py
│     │        │  ├─ py.typed
│     │        │  ├─ schema.py
│     │        │  ├─ sql
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _dml_constructors.cpython-310.pyc
│     │        │  │  │  ├─ _elements_constructors.cpython-310.pyc
│     │        │  │  │  ├─ _orm_types.cpython-310.pyc
│     │        │  │  │  ├─ _py_util.cpython-310.pyc
│     │        │  │  │  ├─ _selectable_constructors.cpython-310.pyc
│     │        │  │  │  ├─ _typing.cpython-310.pyc
│     │        │  │  │  ├─ annotation.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ cache_key.cpython-310.pyc
│     │        │  │  │  ├─ coercions.cpython-310.pyc
│     │        │  │  │  ├─ compiler.cpython-310.pyc
│     │        │  │  │  ├─ crud.cpython-310.pyc
│     │        │  │  │  ├─ ddl.cpython-310.pyc
│     │        │  │  │  ├─ default_comparator.cpython-310.pyc
│     │        │  │  │  ├─ dml.cpython-310.pyc
│     │        │  │  │  ├─ elements.cpython-310.pyc
│     │        │  │  │  ├─ events.cpython-310.pyc
│     │        │  │  │  ├─ expression.cpython-310.pyc
│     │        │  │  │  ├─ functions.cpython-310.pyc
│     │        │  │  │  ├─ lambdas.cpython-310.pyc
│     │        │  │  │  ├─ naming.cpython-310.pyc
│     │        │  │  │  ├─ operators.cpython-310.pyc
│     │        │  │  │  ├─ roles.cpython-310.pyc
│     │        │  │  │  ├─ schema.cpython-310.pyc
│     │        │  │  │  ├─ selectable.cpython-310.pyc
│     │        │  │  │  ├─ sqltypes.cpython-310.pyc
│     │        │  │  │  ├─ traversals.cpython-310.pyc
│     │        │  │  │  ├─ type_api.cpython-310.pyc
│     │        │  │  │  ├─ util.cpython-310.pyc
│     │        │  │  │  └─ visitors.cpython-310.pyc
│     │        │  │  ├─ _dml_constructors.py
│     │        │  │  ├─ _elements_constructors.py
│     │        │  │  ├─ _orm_types.py
│     │        │  │  ├─ _py_util.py
│     │        │  │  ├─ _selectable_constructors.py
│     │        │  │  ├─ _typing.py
│     │        │  │  ├─ annotation.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ cache_key.py
│     │        │  │  ├─ coercions.py
│     │        │  │  ├─ compiler.py
│     │        │  │  ├─ crud.py
│     │        │  │  ├─ ddl.py
│     │        │  │  ├─ default_comparator.py
│     │        │  │  ├─ dml.py
│     │        │  │  ├─ elements.py
│     │        │  │  ├─ events.py
│     │        │  │  ├─ expression.py
│     │        │  │  ├─ functions.py
│     │        │  │  ├─ lambdas.py
│     │        │  │  ├─ naming.py
│     │        │  │  ├─ operators.py
│     │        │  │  ├─ roles.py
│     │        │  │  ├─ schema.py
│     │        │  │  ├─ selectable.py
│     │        │  │  ├─ sqltypes.py
│     │        │  │  ├─ traversals.py
│     │        │  │  ├─ type_api.py
│     │        │  │  ├─ util.py
│     │        │  │  └─ visitors.py
│     │        │  ├─ testing
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ assertions.cpython-310.pyc
│     │        │  │  │  ├─ assertsql.cpython-310.pyc
│     │        │  │  │  ├─ asyncio.cpython-310.pyc
│     │        │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  ├─ engines.cpython-310.pyc
│     │        │  │  │  ├─ entities.cpython-310.pyc
│     │        │  │  │  ├─ exclusions.cpython-310.pyc
│     │        │  │  │  ├─ fixtures.cpython-310.pyc
│     │        │  │  │  ├─ pickleable.cpython-310.pyc
│     │        │  │  │  ├─ profiling.cpython-310.pyc
│     │        │  │  │  ├─ provision.cpython-310.pyc
│     │        │  │  │  ├─ requirements.cpython-310.pyc
│     │        │  │  │  ├─ schema.cpython-310.pyc
│     │        │  │  │  ├─ util.cpython-310.pyc
│     │        │  │  │  └─ warnings.cpython-310.pyc
│     │        │  │  ├─ assertions.py
│     │        │  │  ├─ assertsql.py
│     │        │  │  ├─ asyncio.py
│     │        │  │  ├─ config.py
│     │        │  │  ├─ engines.py
│     │        │  │  ├─ entities.py
│     │        │  │  ├─ exclusions.py
│     │        │  │  ├─ fixtures.py
│     │        │  │  ├─ pickleable.py
│     │        │  │  ├─ plugin
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ bootstrap.cpython-310.pyc
│     │        │  │  │  │  ├─ plugin_base.cpython-310.pyc
│     │        │  │  │  │  └─ pytestplugin.cpython-310.pyc
│     │        │  │  │  ├─ bootstrap.py
│     │        │  │  │  ├─ plugin_base.py
│     │        │  │  │  └─ pytestplugin.py
│     │        │  │  ├─ profiling.py
│     │        │  │  ├─ provision.py
│     │        │  │  ├─ requirements.py
│     │        │  │  ├─ schema.py
│     │        │  │  ├─ suite
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ test_cte.cpython-310.pyc
│     │        │  │  │  │  ├─ test_ddl.cpython-310.pyc
│     │        │  │  │  │  ├─ test_deprecations.cpython-310.pyc
│     │        │  │  │  │  ├─ test_dialect.cpython-310.pyc
│     │        │  │  │  │  ├─ test_insert.cpython-310.pyc
│     │        │  │  │  │  ├─ test_reflection.cpython-310.pyc
│     │        │  │  │  │  ├─ test_results.cpython-310.pyc
│     │        │  │  │  │  ├─ test_rowcount.cpython-310.pyc
│     │        │  │  │  │  ├─ test_select.cpython-310.pyc
│     │        │  │  │  │  ├─ test_sequence.cpython-310.pyc
│     │        │  │  │  │  ├─ test_types.cpython-310.pyc
│     │        │  │  │  │  ├─ test_unicode_ddl.cpython-310.pyc
│     │        │  │  │  │  └─ test_update_delete.cpython-310.pyc
│     │        │  │  │  ├─ test_cte.py
│     │        │  │  │  ├─ test_ddl.py
│     │        │  │  │  ├─ test_deprecations.py
│     │        │  │  │  ├─ test_dialect.py
│     │        │  │  │  ├─ test_insert.py
│     │        │  │  │  ├─ test_reflection.py
│     │        │  │  │  ├─ test_results.py
│     │        │  │  │  ├─ test_rowcount.py
│     │        │  │  │  ├─ test_select.py
│     │        │  │  │  ├─ test_sequence.py
│     │        │  │  │  ├─ test_types.py
│     │        │  │  │  ├─ test_unicode_ddl.py
│     │        │  │  │  └─ test_update_delete.py
│     │        │  │  ├─ util.py
│     │        │  │  └─ warnings.py
│     │        │  ├─ types.py
│     │        │  └─ util
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ _collections.cpython-310.pyc
│     │        │     │  ├─ _concurrency_py3k.cpython-310.pyc
│     │        │     │  ├─ _has_cy.cpython-310.pyc
│     │        │     │  ├─ _py_collections.cpython-310.pyc
│     │        │     │  ├─ compat.cpython-310.pyc
│     │        │     │  ├─ concurrency.cpython-310.pyc
│     │        │     │  ├─ deprecations.cpython-310.pyc
│     │        │     │  ├─ langhelpers.cpython-310.pyc
│     │        │     │  ├─ preloaded.cpython-310.pyc
│     │        │     │  ├─ queue.cpython-310.pyc
│     │        │     │  ├─ tool_support.cpython-310.pyc
│     │        │     │  ├─ topological.cpython-310.pyc
│     │        │     │  └─ typing.cpython-310.pyc
│     │        │     ├─ _collections.py
│     │        │     ├─ _concurrency_py3k.py
│     │        │     ├─ _has_cy.py
│     │        │     ├─ _py_collections.py
│     │        │     ├─ compat.py
│     │        │     ├─ concurrency.py
│     │        │     ├─ deprecations.py
│     │        │     ├─ langhelpers.py
│     │        │     ├─ preloaded.py
│     │        │     ├─ queue.py
│     │        │     ├─ tool_support.py
│     │        │     ├─ topological.py
│     │        │     └─ typing.py
│     │        ├─ tomli
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _parser.cpython-310.pyc
│     │        │  │  ├─ _re.cpython-310.pyc
│     │        │  │  └─ _types.cpython-310.pyc
│     │        │  ├─ _parser.py
│     │        │  ├─ _re.py
│     │        │  ├─ _types.py
│     │        │  └─ py.typed
│     │        ├─ tomli-2.0.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  └─ WHEEL
│     │        ├─ typing_extensions-4.7.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ typing_extensions.py
│     │        ├─ uvicorn
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ _subprocess.cpython-310.pyc
│     │        │  │  ├─ _types.cpython-310.pyc
│     │        │  │  ├─ config.cpython-310.pyc
│     │        │  │  ├─ importer.cpython-310.pyc
│     │        │  │  ├─ logging.cpython-310.pyc
│     │        │  │  ├─ main.cpython-310.pyc
│     │        │  │  ├─ server.cpython-310.pyc
│     │        │  │  └─ workers.cpython-310.pyc
│     │        │  ├─ _subprocess.py
│     │        │  ├─ _types.py
│     │        │  ├─ config.py
│     │        │  ├─ importer.py
│     │        │  ├─ lifespan
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ off.cpython-310.pyc
│     │        │  │  │  └─ on.cpython-310.pyc
│     │        │  │  ├─ off.py
│     │        │  │  └─ on.py
│     │        │  ├─ logging.py
│     │        │  ├─ loops
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asyncio.cpython-310.pyc
│     │        │  │  │  ├─ auto.cpython-310.pyc
│     │        │  │  │  └─ uvloop.cpython-310.pyc
│     │        │  │  ├─ asyncio.py
│     │        │  │  ├─ auto.py
│     │        │  │  └─ uvloop.py
│     │        │  ├─ main.py
│     │        │  ├─ middleware
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asgi2.cpython-310.pyc
│     │        │  │  │  ├─ message_logger.cpython-310.pyc
│     │        │  │  │  ├─ proxy_headers.cpython-310.pyc
│     │        │  │  │  └─ wsgi.cpython-310.pyc
│     │        │  │  ├─ asgi2.py
│     │        │  │  ├─ message_logger.py
│     │        │  │  ├─ proxy_headers.py
│     │        │  │  └─ wsgi.py
│     │        │  ├─ protocols
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  ├─ http
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ auto.cpython-310.pyc
│     │        │  │  │  │  ├─ flow_control.cpython-310.pyc
│     │        │  │  │  │  ├─ h11_impl.cpython-310.pyc
│     │        │  │  │  │  └─ httptools_impl.cpython-310.pyc
│     │        │  │  │  ├─ auto.py
│     │        │  │  │  ├─ flow_control.py
│     │        │  │  │  ├─ h11_impl.py
│     │        │  │  │  └─ httptools_impl.py
│     │        │  │  ├─ utils.py
│     │        │  │  └─ websockets
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ auto.cpython-310.pyc
│     │        │  │     │  ├─ websockets_impl.cpython-310.pyc
│     │        │  │     │  └─ wsproto_impl.cpython-310.pyc
│     │        │  │     ├─ auto.py
│     │        │  │     ├─ websockets_impl.py
│     │        │  │     └─ wsproto_impl.py
│     │        │  ├─ py.typed
│     │        │  ├─ server.py
│     │        │  ├─ supervisors
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ basereload.cpython-310.pyc
│     │        │  │  │  ├─ multiprocess.cpython-310.pyc
│     │        │  │  │  ├─ statreload.cpython-310.pyc
│     │        │  │  │  ├─ watchfilesreload.cpython-310.pyc
│     │        │  │  │  └─ watchgodreload.cpython-310.pyc
│     │        │  │  ├─ basereload.py
│     │        │  │  ├─ multiprocess.py
│     │        │  │  ├─ statreload.py
│     │        │  │  ├─ watchfilesreload.py
│     │        │  │  └─ watchgodreload.py
│     │        │  └─ workers.py
│     │        ├─ uvicorn-0.22.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ licenses
│     │        │     └─ LICENSE.md
│     │        ├─ uvloop
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _noop.cpython-310.pyc
│     │        │  │  ├─ _testbase.cpython-310.pyc
│     │        │  │  └─ _version.cpython-310.pyc
│     │        │  ├─ _noop.py
│     │        │  ├─ _testbase.py
│     │        │  ├─ _version.py
│     │        │  ├─ cbhandles.pxd
│     │        │  ├─ cbhandles.pyx
│     │        │  ├─ dns.pyx
│     │        │  ├─ errors.pyx
│     │        │  ├─ handles
│     │        │  │  ├─ async_.pxd
│     │        │  │  ├─ async_.pyx
│     │        │  │  ├─ basetransport.pxd
│     │        │  │  ├─ basetransport.pyx
│     │        │  │  ├─ check.pxd
│     │        │  │  ├─ check.pyx
│     │        │  │  ├─ fsevent.pxd
│     │        │  │  ├─ fsevent.pyx
│     │        │  │  ├─ handle.pxd
│     │        │  │  ├─ handle.pyx
│     │        │  │  ├─ idle.pxd
│     │        │  │  ├─ idle.pyx
│     │        │  │  ├─ pipe.pxd
│     │        │  │  ├─ pipe.pyx
│     │        │  │  ├─ poll.pxd
│     │        │  │  ├─ poll.pyx
│     │        │  │  ├─ process.pxd
│     │        │  │  ├─ process.pyx
│     │        │  │  ├─ stream.pxd
│     │        │  │  ├─ stream.pyx
│     │        │  │  ├─ streamserver.pxd
│     │        │  │  ├─ streamserver.pyx
│     │        │  │  ├─ tcp.pxd
│     │        │  │  ├─ tcp.pyx
│     │        │  │  ├─ timer.pxd
│     │        │  │  ├─ timer.pyx
│     │        │  │  ├─ udp.pxd
│     │        │  │  └─ udp.pyx
│     │        │  ├─ includes
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ compat.h
│     │        │  │  ├─ consts.pxi
│     │        │  │  ├─ debug.h
│     │        │  │  ├─ debug.pxd
│     │        │  │  ├─ flowcontrol.pxd
│     │        │  │  ├─ fork_handler.h
│     │        │  │  ├─ python.pxd
│     │        │  │  ├─ stdlib.pxi
│     │        │  │  ├─ system.pxd
│     │        │  │  └─ uv.pxd
│     │        │  ├─ loop.c
│     │        │  ├─ loop.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ loop.pxd
│     │        │  ├─ loop.pyi
│     │        │  ├─ loop.pyx
│     │        │  ├─ lru.pyx
│     │        │  ├─ pseudosock.pyx
│     │        │  ├─ py.typed
│     │        │  ├─ request.pxd
│     │        │  ├─ request.pyx
│     │        │  ├─ server.pxd
│     │        │  ├─ server.pyx
│     │        │  ├─ sslproto.pxd
│     │        │  └─ sslproto.pyx
│     │        ├─ uvloop-0.17.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE-APACHE
│     │        │  ├─ LICENSE-MIT
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ validate_pyproject
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ api.cpython-310.pyc
│     │        │  │  ├─ cli.cpython-310.pyc
│     │        │  │  ├─ error_reporting.cpython-310.pyc
│     │        │  │  ├─ errors.cpython-310.pyc
│     │        │  │  ├─ extra_validations.cpython-310.pyc
│     │        │  │  ├─ formats.cpython-310.pyc
│     │        │  │  └─ types.cpython-310.pyc
│     │        │  ├─ api.py
│     │        │  ├─ cli.py
│     │        │  ├─ error_reporting.py
│     │        │  ├─ errors.py
│     │        │  ├─ extra_validations.py
│     │        │  ├─ formats.py
│     │        │  ├─ plugins
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ distutils.schema.json
│     │        │  │  └─ setuptools.schema.json
│     │        │  ├─ pre_compile
│     │        │  │  ├─ NOTICE.template
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __main__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  │  └─ cli.cpython-310.pyc
│     │        │  │  ├─ api-notice.template
│     │        │  │  ├─ cli-notice.template
│     │        │  │  ├─ cli.py
│     │        │  │  └─ main_file.template
│     │        │  ├─ project_metadata.schema.json
│     │        │  ├─ py.typed
│     │        │  ├─ pyproject_toml.schema.json
│     │        │  ├─ types.py
│     │        │  └─ vendoring
│     │        │     ├─ __init__.py
│     │        │     ├─ __main__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ __main__.cpython-310.pyc
│     │        │     │  └─ cli.cpython-310.pyc
│     │        │     └─ cli.py
│     │        ├─ validate_pyproject-0.13.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.txt
│     │        │  ├─ METADATA
│     │        │  ├─ NOTICE.txt
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ watchfiles
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ cli.cpython-310.pyc
│     │        │  │  ├─ filters.cpython-310.pyc
│     │        │  │  ├─ main.cpython-310.pyc
│     │        │  │  ├─ run.cpython-310.pyc
│     │        │  │  └─ version.cpython-310.pyc
│     │        │  ├─ _rust_notify.abi3.so
│     │        │  ├─ _rust_notify.pyi
│     │        │  ├─ cli.py
│     │        │  ├─ filters.py
│     │        │  ├─ main.py
│     │        │  ├─ py.typed
│     │        │  ├─ run.py
│     │        │  └─ version.py
│     │        ├─ watchfiles-0.19.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ license_files
│     │        │     └─ LICENSE
│     │        ├─ websockets
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ auth.cpython-310.pyc
│     │        │  │  ├─ client.cpython-310.pyc
│     │        │  │  ├─ connection.cpython-310.pyc
│     │        │  │  ├─ datastructures.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ frames.cpython-310.pyc
│     │        │  │  ├─ headers.cpython-310.pyc
│     │        │  │  ├─ http.cpython-310.pyc
│     │        │  │  ├─ http11.cpython-310.pyc
│     │        │  │  ├─ imports.cpython-310.pyc
│     │        │  │  ├─ protocol.cpython-310.pyc
│     │        │  │  ├─ server.cpython-310.pyc
│     │        │  │  ├─ streams.cpython-310.pyc
│     │        │  │  ├─ typing.cpython-310.pyc
│     │        │  │  ├─ uri.cpython-310.pyc
│     │        │  │  ├─ utils.cpython-310.pyc
│     │        │  │  └─ version.cpython-310.pyc
│     │        │  ├─ auth.py
│     │        │  ├─ client.py
│     │        │  ├─ connection.py
│     │        │  ├─ datastructures.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ extensions
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  └─ permessage_deflate.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  └─ permessage_deflate.py
│     │        │  ├─ frames.py
│     │        │  ├─ headers.py
│     │        │  ├─ http.py
│     │        │  ├─ http11.py
│     │        │  ├─ imports.py
│     │        │  ├─ legacy
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ async_timeout.cpython-310.pyc
│     │        │  │  │  ├─ auth.cpython-310.pyc
│     │        │  │  │  ├─ client.cpython-310.pyc
│     │        │  │  │  ├─ compatibility.cpython-310.pyc
│     │        │  │  │  ├─ framing.cpython-310.pyc
│     │        │  │  │  ├─ handshake.cpython-310.pyc
│     │        │  │  │  ├─ http.cpython-310.pyc
│     │        │  │  │  ├─ protocol.cpython-310.pyc
│     │        │  │  │  └─ server.cpython-310.pyc
│     │        │  │  ├─ async_timeout.py
│     │        │  │  ├─ auth.py
│     │        │  │  ├─ client.py
│     │        │  │  ├─ compatibility.py
│     │        │  │  ├─ framing.py
│     │        │  │  ├─ handshake.py
│     │        │  │  ├─ http.py
│     │        │  │  ├─ protocol.py
│     │        │  │  └─ server.py
│     │        │  ├─ protocol.py
│     │        │  ├─ py.typed
│     │        │  ├─ server.py
│     │        │  ├─ speedups.c
│     │        │  ├─ speedups.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ streams.py
│     │        │  ├─ sync
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ client.cpython-310.pyc
│     │        │  │  │  ├─ compatibility.cpython-310.pyc
│     │        │  │  │  ├─ connection.cpython-310.pyc
│     │        │  │  │  ├─ messages.cpython-310.pyc
│     │        │  │  │  ├─ server.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  ├─ client.py
│     │        │  │  ├─ compatibility.py
│     │        │  │  ├─ connection.py
│     │        │  │  ├─ messages.py
│     │        │  │  ├─ server.py
│     │        │  │  └─ utils.py
│     │        │  ├─ typing.py
│     │        │  ├─ uri.py
│     │        │  ├─ utils.py
│     │        │  └─ version.py
│     │        ├─ websockets-11.0.3.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ wheel
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ _setuptools_logging.cpython-310.pyc
│     │        │  │  ├─ bdist_wheel.cpython-310.pyc
│     │        │  │  ├─ macosx_libfile.cpython-310.pyc
│     │        │  │  ├─ metadata.cpython-310.pyc
│     │        │  │  ├─ util.cpython-310.pyc
│     │        │  │  └─ wheelfile.cpython-310.pyc
│     │        │  ├─ _setuptools_logging.py
│     │        │  ├─ bdist_wheel.py
│     │        │  ├─ cli
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ convert.cpython-310.pyc
│     │        │  │  │  ├─ pack.cpython-310.pyc
│     │        │  │  │  ├─ tags.cpython-310.pyc
│     │        │  │  │  └─ unpack.cpython-310.pyc
│     │        │  │  ├─ convert.py
│     │        │  │  ├─ pack.py
│     │        │  │  ├─ tags.py
│     │        │  │  └─ unpack.py
│     │        │  ├─ macosx_libfile.py
│     │        │  ├─ metadata.py
│     │        │  ├─ util.py
│     │        │  ├─ vendored
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ packaging
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _elffile.cpython-310.pyc
│     │        │  │  │  │  ├─ _manylinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _musllinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _parser.cpython-310.pyc
│     │        │  │  │  │  ├─ _structures.cpython-310.pyc
│     │        │  │  │  │  ├─ _tokenizer.cpython-310.pyc
│     │        │  │  │  │  ├─ markers.cpython-310.pyc
│     │        │  │  │  │  ├─ requirements.cpython-310.pyc
│     │        │  │  │  │  ├─ specifiers.cpython-310.pyc
│     │        │  │  │  │  ├─ tags.cpython-310.pyc
│     │        │  │  │  │  ├─ utils.cpython-310.pyc
│     │        │  │  │  │  └─ version.cpython-310.pyc
│     │        │  │  │  ├─ _elffile.py
│     │        │  │  │  ├─ _manylinux.py
│     │        │  │  │  ├─ _musllinux.py
│     │        │  │  │  ├─ _parser.py
│     │        │  │  │  ├─ _structures.py
│     │        │  │  │  ├─ _tokenizer.py
│     │        │  │  │  ├─ markers.py
│     │        │  │  │  ├─ requirements.py
│     │        │  │  │  ├─ specifiers.py
│     │        │  │  │  ├─ tags.py
│     │        │  │  │  ├─ utils.py
│     │        │  │  │  └─ version.py
│     │        │  │  └─ vendor.txt
│     │        │  └─ wheelfile.py
│     │        ├─ wheel-0.40.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.txt
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ entry_points.txt
│     │        └─ yaml
│     │           ├─ __init__.py
│     │           ├─ __pycache__
│     │           │  ├─ __init__.cpython-310.pyc
│     │           │  ├─ composer.cpython-310.pyc
│     │           │  ├─ constructor.cpython-310.pyc
│     │           │  ├─ cyaml.cpython-310.pyc
│     │           │  ├─ dumper.cpython-310.pyc
│     │           │  ├─ emitter.cpython-310.pyc
│     │           │  ├─ error.cpython-310.pyc
│     │           │  ├─ events.cpython-310.pyc
│     │           │  ├─ loader.cpython-310.pyc
│     │           │  ├─ nodes.cpython-310.pyc
│     │           │  ├─ parser.cpython-310.pyc
│     │           │  ├─ reader.cpython-310.pyc
│     │           │  ├─ representer.cpython-310.pyc
│     │           │  ├─ resolver.cpython-310.pyc
│     │           │  ├─ scanner.cpython-310.pyc
│     │           │  ├─ serializer.cpython-310.pyc
│     │           │  └─ tokens.cpython-310.pyc
│     │           ├─ _yaml.cpython-310-x86_64-linux-gnu.so
│     │           ├─ composer.py
│     │           ├─ constructor.py
│     │           ├─ cyaml.py
│     │           ├─ dumper.py
│     │           ├─ emitter.py
│     │           ├─ error.py
│     │           ├─ events.py
│     │           ├─ loader.py
│     │           ├─ nodes.py
│     │           ├─ parser.py
│     │           ├─ reader.py
│     │           ├─ representer.py
│     │           ├─ resolver.py
│     │           ├─ scanner.py
│     │           ├─ serializer.py
│     │           └─ tokens.py
│     ├─ lib64
│     │  └─ python3.10
│     │     └─ site-packages
│     │        ├─ 2ec0e72aa72355e6eccf__mypyc.cpython-310-x86_64-linux-gnu.so
│     │        ├─ EditorConfig-0.12.3.dist-info
│     │        │  ├─ COPYING
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.BSD
│     │        │  ├─ LICENSE.PSF
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ Faker-18.11.2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.txt
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  ├─ top_level.txt
│     │        │  └─ zip-safe
│     │        ├─ Mako-1.2.4.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ MarkupSafe-2.1.3.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.rst
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ PyYAML-6.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ Pygments-2.15.1.dist-info
│     │        │  ├─ AUTHORS
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ SQLAlchemy-2.0.17.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ __pycache__
│     │        │  ├─ _black_version.cpython-310.pyc
│     │        │  ├─ decouple.cpython-310.pyc
│     │        │  ├─ mypy_extensions.cpython-310.pyc
│     │        │  ├─ py.cpython-310.pyc
│     │        │  ├─ six.cpython-310.pyc
│     │        │  └─ typing_extensions.cpython-310.pyc
│     │        ├─ _argon2_cffi_bindings
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  └─ _ffi_build.cpython-310.pyc
│     │        │  ├─ _ffi.abi3.so
│     │        │  └─ _ffi_build.py
│     │        ├─ _black_version.py
│     │        ├─ _cffi_backend.cpython-310-x86_64-linux-gnu.so
│     │        ├─ _distutils_hack
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  └─ override.cpython-310.pyc
│     │        │  └─ override.py
│     │        ├─ _pytest
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _argcomplete.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  ├─ cacheprovider.cpython-310.pyc
│     │        │  │  ├─ capture.cpython-310.pyc
│     │        │  │  ├─ compat.cpython-310.pyc
│     │        │  │  ├─ debugging.cpython-310.pyc
│     │        │  │  ├─ deprecated.cpython-310.pyc
│     │        │  │  ├─ doctest.cpython-310.pyc
│     │        │  │  ├─ faulthandler.cpython-310.pyc
│     │        │  │  ├─ fixtures.cpython-310.pyc
│     │        │  │  ├─ freeze_support.cpython-310.pyc
│     │        │  │  ├─ helpconfig.cpython-310.pyc
│     │        │  │  ├─ junitxml.cpython-310.pyc
│     │        │  │  ├─ legacypath.cpython-310.pyc
│     │        │  │  ├─ logging.cpython-310.pyc
│     │        │  │  ├─ main.cpython-310.pyc
│     │        │  │  ├─ monkeypatch.cpython-310.pyc
│     │        │  │  ├─ nodes.cpython-310.pyc
│     │        │  │  ├─ nose.cpython-310.pyc
│     │        │  │  ├─ outcomes.cpython-310.pyc
│     │        │  │  ├─ pastebin.cpython-310.pyc
│     │        │  │  ├─ pathlib.cpython-310.pyc
│     │        │  │  ├─ pytester.cpython-310.pyc
│     │        │  │  ├─ pytester_assertions.cpython-310.pyc
│     │        │  │  ├─ python.cpython-310.pyc
│     │        │  │  ├─ python_api.cpython-310.pyc
│     │        │  │  ├─ python_path.cpython-310.pyc
│     │        │  │  ├─ recwarn.cpython-310.pyc
│     │        │  │  ├─ reports.cpython-310.pyc
│     │        │  │  ├─ runner.cpython-310.pyc
│     │        │  │  ├─ scope.cpython-310.pyc
│     │        │  │  ├─ setuponly.cpython-310.pyc
│     │        │  │  ├─ setupplan.cpython-310.pyc
│     │        │  │  ├─ skipping.cpython-310.pyc
│     │        │  │  ├─ stash.cpython-310.pyc
│     │        │  │  ├─ stepwise.cpython-310.pyc
│     │        │  │  ├─ terminal.cpython-310.pyc
│     │        │  │  ├─ threadexception.cpython-310.pyc
│     │        │  │  ├─ timing.cpython-310.pyc
│     │        │  │  ├─ tmpdir.cpython-310.pyc
│     │        │  │  ├─ unittest.cpython-310.pyc
│     │        │  │  ├─ unraisableexception.cpython-310.pyc
│     │        │  │  ├─ warning_types.cpython-310.pyc
│     │        │  │  └─ warnings.cpython-310.pyc
│     │        │  ├─ _argcomplete.py
│     │        │  ├─ _code
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ code.cpython-310.pyc
│     │        │  │  │  └─ source.cpython-310.pyc
│     │        │  │  ├─ code.py
│     │        │  │  └─ source.py
│     │        │  ├─ _io
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ saferepr.cpython-310.pyc
│     │        │  │  │  ├─ terminalwriter.cpython-310.pyc
│     │        │  │  │  └─ wcwidth.cpython-310.pyc
│     │        │  │  ├─ saferepr.py
│     │        │  │  ├─ terminalwriter.py
│     │        │  │  └─ wcwidth.py
│     │        │  ├─ _py
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ error.cpython-310.pyc
│     │        │  │  │  └─ path.cpython-310.pyc
│     │        │  │  ├─ error.py
│     │        │  │  └─ path.py
│     │        │  ├─ _version.py
│     │        │  ├─ assertion
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ rewrite.cpython-310.pyc
│     │        │  │  │  ├─ truncate.cpython-310.pyc
│     │        │  │  │  └─ util.cpython-310.pyc
│     │        │  │  ├─ rewrite.py
│     │        │  │  ├─ truncate.py
│     │        │  │  └─ util.py
│     │        │  ├─ cacheprovider.py
│     │        │  ├─ capture.py
│     │        │  ├─ compat.py
│     │        │  ├─ config
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ argparsing.cpython-310.pyc
│     │        │  │  │  ├─ compat.cpython-310.pyc
│     │        │  │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  │  └─ findpaths.cpython-310.pyc
│     │        │  │  ├─ argparsing.py
│     │        │  │  ├─ compat.py
│     │        │  │  ├─ exceptions.py
│     │        │  │  └─ findpaths.py
│     │        │  ├─ debugging.py
│     │        │  ├─ deprecated.py
│     │        │  ├─ doctest.py
│     │        │  ├─ faulthandler.py
│     │        │  ├─ fixtures.py
│     │        │  ├─ freeze_support.py
│     │        │  ├─ helpconfig.py
│     │        │  ├─ junitxml.py
│     │        │  ├─ legacypath.py
│     │        │  ├─ logging.py
│     │        │  ├─ main.py
│     │        │  ├─ mark
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ expression.cpython-310.pyc
│     │        │  │  │  └─ structures.cpython-310.pyc
│     │        │  │  ├─ expression.py
│     │        │  │  └─ structures.py
│     │        │  ├─ monkeypatch.py
│     │        │  ├─ nodes.py
│     │        │  ├─ nose.py
│     │        │  ├─ outcomes.py
│     │        │  ├─ pastebin.py
│     │        │  ├─ pathlib.py
│     │        │  ├─ py.typed
│     │        │  ├─ pytester.py
│     │        │  ├─ pytester_assertions.py
│     │        │  ├─ python.py
│     │        │  ├─ python_api.py
│     │        │  ├─ python_path.py
│     │        │  ├─ recwarn.py
│     │        │  ├─ reports.py
│     │        │  ├─ runner.py
│     │        │  ├─ scope.py
│     │        │  ├─ setuponly.py
│     │        │  ├─ setupplan.py
│     │        │  ├─ skipping.py
│     │        │  ├─ stash.py
│     │        │  ├─ stepwise.py
│     │        │  ├─ terminal.py
│     │        │  ├─ threadexception.py
│     │        │  ├─ timing.py
│     │        │  ├─ tmpdir.py
│     │        │  ├─ unittest.py
│     │        │  ├─ unraisableexception.py
│     │        │  ├─ warning_types.py
│     │        │  └─ warnings.py
│     │        ├─ _yaml
│     │        │  ├─ __init__.py
│     │        │  └─ __pycache__
│     │        │     └─ __init__.cpython-310.pyc
│     │        ├─ aiofiles
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ base.cpython-310.pyc
│     │        │  │  ├─ os.cpython-310.pyc
│     │        │  │  └─ ospath.cpython-310.pyc
│     │        │  ├─ base.py
│     │        │  ├─ os.py
│     │        │  ├─ ospath.py
│     │        │  ├─ tempfile
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ temptypes.cpython-310.pyc
│     │        │  │  └─ temptypes.py
│     │        │  └─ threadpool
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ binary.cpython-310.pyc
│     │        │     │  ├─ text.cpython-310.pyc
│     │        │     │  └─ utils.cpython-310.pyc
│     │        │     ├─ binary.py
│     │        │     ├─ text.py
│     │        │     └─ utils.py
│     │        ├─ aiofiles-23.1.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ aiosmtplib
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ api.cpython-310.pyc
│     │        │  │  ├─ auth.cpython-310.pyc
│     │        │  │  ├─ email.cpython-310.pyc
│     │        │  │  ├─ errors.cpython-310.pyc
│     │        │  │  ├─ esmtp.cpython-310.pyc
│     │        │  │  ├─ protocol.cpython-310.pyc
│     │        │  │  ├─ response.cpython-310.pyc
│     │        │  │  ├─ smtp.cpython-310.pyc
│     │        │  │  ├─ status.cpython-310.pyc
│     │        │  │  └─ typing.cpython-310.pyc
│     │        │  ├─ api.py
│     │        │  ├─ auth.py
│     │        │  ├─ email.py
│     │        │  ├─ errors.py
│     │        │  ├─ esmtp.py
│     │        │  ├─ protocol.py
│     │        │  ├─ py.typed
│     │        │  ├─ response.py
│     │        │  ├─ smtp.py
│     │        │  ├─ status.py
│     │        │  └─ typing.py
│     │        ├─ aiosmtplib-2.0.2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.txt
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ alembic
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ command.cpython-310.pyc
│     │        │  │  ├─ config.cpython-310.pyc
│     │        │  │  ├─ context.cpython-310.pyc
│     │        │  │  ├─ environment.cpython-310.pyc
│     │        │  │  ├─ migration.cpython-310.pyc
│     │        │  │  └─ op.cpython-310.pyc
│     │        │  ├─ autogenerate
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ api.cpython-310.pyc
│     │        │  │  │  ├─ compare.cpython-310.pyc
│     │        │  │  │  ├─ render.cpython-310.pyc
│     │        │  │  │  └─ rewriter.cpython-310.pyc
│     │        │  │  ├─ api.py
│     │        │  │  ├─ compare.py
│     │        │  │  ├─ render.py
│     │        │  │  └─ rewriter.py
│     │        │  ├─ command.py
│     │        │  ├─ config.py
│     │        │  ├─ context.py
│     │        │  ├─ context.pyi
│     │        │  ├─ ddl
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ impl.cpython-310.pyc
│     │        │  │  │  ├─ mssql.cpython-310.pyc
│     │        │  │  │  ├─ mysql.cpython-310.pyc
│     │        │  │  │  ├─ oracle.cpython-310.pyc
│     │        │  │  │  ├─ postgresql.cpython-310.pyc
│     │        │  │  │  └─ sqlite.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ impl.py
│     │        │  │  ├─ mssql.py
│     │        │  │  ├─ mysql.py
│     │        │  │  ├─ oracle.py
│     │        │  │  ├─ postgresql.py
│     │        │  │  └─ sqlite.py
│     │        │  ├─ environment.py
│     │        │  ├─ migration.py
│     │        │  ├─ op.py
│     │        │  ├─ op.pyi
│     │        │  ├─ operations
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ batch.cpython-310.pyc
│     │        │  │  │  ├─ ops.cpython-310.pyc
│     │        │  │  │  ├─ schemaobj.cpython-310.pyc
│     │        │  │  │  └─ toimpl.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ batch.py
│     │        │  │  ├─ ops.py
│     │        │  │  ├─ schemaobj.py
│     │        │  │  └─ toimpl.py
│     │        │  ├─ py.typed
│     │        │  ├─ runtime
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ environment.cpython-310.pyc
│     │        │  │  │  └─ migration.cpython-310.pyc
│     │        │  │  ├─ environment.py
│     │        │  │  └─ migration.py
│     │        │  ├─ script
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  └─ revision.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  └─ revision.py
│     │        │  ├─ templates
│     │        │  │  ├─ async
│     │        │  │  │  ├─ README
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  └─ env.cpython-310.pyc
│     │        │  │  │  ├─ alembic.ini.mako
│     │        │  │  │  ├─ env.py
│     │        │  │  │  └─ script.py.mako
│     │        │  │  ├─ generic
│     │        │  │  │  ├─ README
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  └─ env.cpython-310.pyc
│     │        │  │  │  ├─ alembic.ini.mako
│     │        │  │  │  ├─ env.py
│     │        │  │  │  └─ script.py.mako
│     │        │  │  └─ multidb
│     │        │  │     ├─ README
│     │        │  │     ├─ __pycache__
│     │        │  │     │  └─ env.cpython-310.pyc
│     │        │  │     ├─ alembic.ini.mako
│     │        │  │     ├─ env.py
│     │        │  │     └─ script.py.mako
│     │        │  ├─ testing
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ assertions.cpython-310.pyc
│     │        │  │  │  ├─ env.cpython-310.pyc
│     │        │  │  │  ├─ fixtures.cpython-310.pyc
│     │        │  │  │  ├─ requirements.cpython-310.pyc
│     │        │  │  │  ├─ schemacompare.cpython-310.pyc
│     │        │  │  │  ├─ util.cpython-310.pyc
│     │        │  │  │  └─ warnings.cpython-310.pyc
│     │        │  │  ├─ assertions.py
│     │        │  │  ├─ env.py
│     │        │  │  ├─ fixtures.py
│     │        │  │  ├─ plugin
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  └─ bootstrap.cpython-310.pyc
│     │        │  │  │  └─ bootstrap.py
│     │        │  │  ├─ requirements.py
│     │        │  │  ├─ schemacompare.py
│     │        │  │  ├─ suite
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _autogen_fixtures.cpython-310.pyc
│     │        │  │  │  │  ├─ test_autogen_comments.cpython-310.pyc
│     │        │  │  │  │  ├─ test_autogen_computed.cpython-310.pyc
│     │        │  │  │  │  ├─ test_autogen_diffs.cpython-310.pyc
│     │        │  │  │  │  ├─ test_autogen_fks.cpython-310.pyc
│     │        │  │  │  │  ├─ test_autogen_identity.cpython-310.pyc
│     │        │  │  │  │  ├─ test_environment.cpython-310.pyc
│     │        │  │  │  │  └─ test_op.cpython-310.pyc
│     │        │  │  │  ├─ _autogen_fixtures.py
│     │        │  │  │  ├─ test_autogen_comments.py
│     │        │  │  │  ├─ test_autogen_computed.py
│     │        │  │  │  ├─ test_autogen_diffs.py
│     │        │  │  │  ├─ test_autogen_fks.py
│     │        │  │  │  ├─ test_autogen_identity.py
│     │        │  │  │  ├─ test_environment.py
│     │        │  │  │  └─ test_op.py
│     │        │  │  ├─ util.py
│     │        │  │  └─ warnings.py
│     │        │  └─ util
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ compat.cpython-310.pyc
│     │        │     │  ├─ editor.cpython-310.pyc
│     │        │     │  ├─ exc.cpython-310.pyc
│     │        │     │  ├─ langhelpers.cpython-310.pyc
│     │        │     │  ├─ messaging.cpython-310.pyc
│     │        │     │  ├─ pyfiles.cpython-310.pyc
│     │        │     │  └─ sqla_compat.cpython-310.pyc
│     │        │     ├─ compat.py
│     │        │     ├─ editor.py
│     │        │     ├─ exc.py
│     │        │     ├─ langhelpers.py
│     │        │     ├─ messaging.py
│     │        │     ├─ pyfiles.py
│     │        │     └─ sqla_compat.py
│     │        ├─ alembic-1.11.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ anyio
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ from_thread.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ from_thread.cpython-310.pyc
│     │        │  │  ├─ lowlevel.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ lowlevel.cpython-310.pyc
│     │        │  │  ├─ pytest_plugin.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ pytest_plugin.cpython-310.pyc
│     │        │  │  ├─ to_process.cpython-310.pyc
│     │        │  │  ├─ to_thread.cpython-310-pytest-7.4.0.pyc
│     │        │  │  └─ to_thread.cpython-310.pyc
│     │        │  ├─ _backends
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _asyncio.cpython-310.pyc
│     │        │  │  │  └─ _trio.cpython-310.pyc
│     │        │  │  ├─ _asyncio.py
│     │        │  │  └─ _trio.py
│     │        │  ├─ _core
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _compat.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _compat.cpython-310.pyc
│     │        │  │  │  ├─ _eventloop.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _eventloop.cpython-310.pyc
│     │        │  │  │  ├─ _exceptions.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _exceptions.cpython-310.pyc
│     │        │  │  │  ├─ _fileio.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _fileio.cpython-310.pyc
│     │        │  │  │  ├─ _resources.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _resources.cpython-310.pyc
│     │        │  │  │  ├─ _signals.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _signals.cpython-310.pyc
│     │        │  │  │  ├─ _sockets.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _sockets.cpython-310.pyc
│     │        │  │  │  ├─ _streams.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _streams.cpython-310.pyc
│     │        │  │  │  ├─ _subprocesses.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _subprocesses.cpython-310.pyc
│     │        │  │  │  ├─ _synchronization.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _synchronization.cpython-310.pyc
│     │        │  │  │  ├─ _tasks.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _tasks.cpython-310.pyc
│     │        │  │  │  ├─ _testing.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _testing.cpython-310.pyc
│     │        │  │  │  ├─ _typedattr.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  └─ _typedattr.cpython-310.pyc
│     │        │  │  ├─ _compat.py
│     │        │  │  ├─ _eventloop.py
│     │        │  │  ├─ _exceptions.py
│     │        │  │  ├─ _fileio.py
│     │        │  │  ├─ _resources.py
│     │        │  │  ├─ _signals.py
│     │        │  │  ├─ _sockets.py
│     │        │  │  ├─ _streams.py
│     │        │  │  ├─ _subprocesses.py
│     │        │  │  ├─ _synchronization.py
│     │        │  │  ├─ _tasks.py
│     │        │  │  ├─ _testing.py
│     │        │  │  └─ _typedattr.py
│     │        │  ├─ abc
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _resources.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _resources.cpython-310.pyc
│     │        │  │  │  ├─ _sockets.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _sockets.cpython-310.pyc
│     │        │  │  │  ├─ _streams.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _streams.cpython-310.pyc
│     │        │  │  │  ├─ _subprocesses.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _subprocesses.cpython-310.pyc
│     │        │  │  │  ├─ _tasks.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ _tasks.cpython-310.pyc
│     │        │  │  │  ├─ _testing.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  └─ _testing.cpython-310.pyc
│     │        │  │  ├─ _resources.py
│     │        │  │  ├─ _sockets.py
│     │        │  │  ├─ _streams.py
│     │        │  │  ├─ _subprocesses.py
│     │        │  │  ├─ _tasks.py
│     │        │  │  └─ _testing.py
│     │        │  ├─ from_thread.py
│     │        │  ├─ lowlevel.py
│     │        │  ├─ py.typed
│     │        │  ├─ pytest_plugin.py
│     │        │  ├─ streams
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ buffered.cpython-310.pyc
│     │        │  │  │  ├─ file.cpython-310.pyc
│     │        │  │  │  ├─ memory.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ memory.cpython-310.pyc
│     │        │  │  │  ├─ stapled.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ stapled.cpython-310.pyc
│     │        │  │  │  ├─ text.cpython-310.pyc
│     │        │  │  │  ├─ tls.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  └─ tls.cpython-310.pyc
│     │        │  │  ├─ buffered.py
│     │        │  │  ├─ file.py
│     │        │  │  ├─ memory.py
│     │        │  │  ├─ stapled.py
│     │        │  │  ├─ text.py
│     │        │  │  └─ tls.py
│     │        │  ├─ to_process.py
│     │        │  └─ to_thread.py
│     │        ├─ anyio-3.7.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ argon2
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ _legacy.cpython-310.pyc
│     │        │  │  ├─ _password_hasher.cpython-310.pyc
│     │        │  │  ├─ _typing.cpython-310.pyc
│     │        │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ low_level.cpython-310.pyc
│     │        │  │  └─ profiles.cpython-310.pyc
│     │        │  ├─ _legacy.py
│     │        │  ├─ _password_hasher.py
│     │        │  ├─ _typing.py
│     │        │  ├─ _utils.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ low_level.py
│     │        │  ├─ profiles.py
│     │        │  └─ py.typed
│     │        ├─ argon2_cffi-21.3.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ argon2_cffi_bindings-21.2.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ black
│     │        │  ├─ __init__.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ _width_table.cpython-310.pyc
│     │        │  │  ├─ brackets.cpython-310.pyc
│     │        │  │  ├─ cache.cpython-310.pyc
│     │        │  │  ├─ comments.cpython-310.pyc
│     │        │  │  ├─ concurrency.cpython-310.pyc
│     │        │  │  ├─ const.cpython-310.pyc
│     │        │  │  ├─ debug.cpython-310.pyc
│     │        │  │  ├─ files.cpython-310.pyc
│     │        │  │  ├─ handle_ipynb_magics.cpython-310.pyc
│     │        │  │  ├─ linegen.cpython-310.pyc
│     │        │  │  ├─ lines.cpython-310.pyc
│     │        │  │  ├─ mode.cpython-310.pyc
│     │        │  │  ├─ nodes.cpython-310.pyc
│     │        │  │  ├─ numerics.cpython-310.pyc
│     │        │  │  ├─ output.cpython-310.pyc
│     │        │  │  ├─ parsing.cpython-310.pyc
│     │        │  │  ├─ report.cpython-310.pyc
│     │        │  │  ├─ rusty.cpython-310.pyc
│     │        │  │  ├─ strings.cpython-310.pyc
│     │        │  │  └─ trans.cpython-310.pyc
│     │        │  ├─ _width_table.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ _width_table.py
│     │        │  ├─ brackets.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ brackets.py
│     │        │  ├─ cache.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ cache.py
│     │        │  ├─ comments.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ comments.py
│     │        │  ├─ concurrency.py
│     │        │  ├─ const.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ const.py
│     │        │  ├─ debug.py
│     │        │  ├─ files.py
│     │        │  ├─ handle_ipynb_magics.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ handle_ipynb_magics.py
│     │        │  ├─ linegen.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ linegen.py
│     │        │  ├─ lines.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ lines.py
│     │        │  ├─ mode.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ mode.py
│     │        │  ├─ nodes.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ nodes.py
│     │        │  ├─ numerics.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ numerics.py
│     │        │  ├─ output.py
│     │        │  ├─ parsing.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ parsing.py
│     │        │  ├─ py.typed
│     │        │  ├─ report.py
│     │        │  ├─ rusty.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ rusty.py
│     │        │  ├─ strings.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ strings.py
│     │        │  ├─ trans.cpython-310-x86_64-linux-gnu.so
│     │        │  └─ trans.py
│     │        ├─ black-23.3.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ licenses
│     │        │     ├─ AUTHORS.md
│     │        │     └─ LICENSE
│     │        ├─ blackd
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  └─ middlewares.cpython-310.pyc
│     │        │  └─ middlewares.py
│     │        ├─ blib2to3
│     │        │  ├─ Grammar.txt
│     │        │  ├─ LICENSE
│     │        │  ├─ PatternGrammar.txt
│     │        │  ├─ README
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ pygram.cpython-310.pyc
│     │        │  │  └─ pytree.cpython-310.pyc
│     │        │  ├─ pgen2
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ conv.cpython-310.pyc
│     │        │  │  │  ├─ driver.cpython-310.pyc
│     │        │  │  │  ├─ grammar.cpython-310.pyc
│     │        │  │  │  ├─ literals.cpython-310.pyc
│     │        │  │  │  ├─ parse.cpython-310.pyc
│     │        │  │  │  ├─ pgen.cpython-310.pyc
│     │        │  │  │  ├─ token.cpython-310.pyc
│     │        │  │  │  └─ tokenize.cpython-310.pyc
│     │        │  │  ├─ conv.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ conv.py
│     │        │  │  ├─ driver.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ driver.py
│     │        │  │  ├─ grammar.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ grammar.py
│     │        │  │  ├─ literals.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ literals.py
│     │        │  │  ├─ parse.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ parse.py
│     │        │  │  ├─ pgen.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ pgen.py
│     │        │  │  ├─ token.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ token.py
│     │        │  │  ├─ tokenize.cpython-310-x86_64-linux-gnu.so
│     │        │  │  └─ tokenize.py
│     │        │  ├─ pygram.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ pygram.py
│     │        │  ├─ pytree.cpython-310-x86_64-linux-gnu.so
│     │        │  └─ pytree.py
│     │        ├─ build
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ env.cpython-310.pyc
│     │        │  │  └─ util.cpython-310.pyc
│     │        │  ├─ env.py
│     │        │  ├─ py.typed
│     │        │  └─ util.py
│     │        ├─ build-0.10.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ WHEEL
│     │        │  └─ entry_points.txt
│     │        ├─ certifi
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  └─ core.cpython-310.pyc
│     │        │  ├─ cacert.pem
│     │        │  ├─ core.py
│     │        │  └─ py.typed
│     │        ├─ certifi-2023.5.7.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ cffi
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ api.cpython-310.pyc
│     │        │  │  ├─ backend_ctypes.cpython-310.pyc
│     │        │  │  ├─ cffi_opcode.cpython-310.pyc
│     │        │  │  ├─ commontypes.cpython-310.pyc
│     │        │  │  ├─ cparser.cpython-310.pyc
│     │        │  │  ├─ error.cpython-310.pyc
│     │        │  │  ├─ ffiplatform.cpython-310.pyc
│     │        │  │  ├─ lock.cpython-310.pyc
│     │        │  │  ├─ model.cpython-310.pyc
│     │        │  │  ├─ pkgconfig.cpython-310.pyc
│     │        │  │  ├─ recompiler.cpython-310.pyc
│     │        │  │  ├─ setuptools_ext.cpython-310.pyc
│     │        │  │  ├─ vengine_cpy.cpython-310.pyc
│     │        │  │  ├─ vengine_gen.cpython-310.pyc
│     │        │  │  └─ verifier.cpython-310.pyc
│     │        │  ├─ _cffi_errors.h
│     │        │  ├─ _cffi_include.h
│     │        │  ├─ _embedding.h
│     │        │  ├─ api.py
│     │        │  ├─ backend_ctypes.py
│     │        │  ├─ cffi_opcode.py
│     │        │  ├─ commontypes.py
│     │        │  ├─ cparser.py
│     │        │  ├─ error.py
│     │        │  ├─ ffiplatform.py
│     │        │  ├─ lock.py
│     │        │  ├─ model.py
│     │        │  ├─ parse_c_type.h
│     │        │  ├─ pkgconfig.py
│     │        │  ├─ recompiler.py
│     │        │  ├─ setuptools_ext.py
│     │        │  ├─ vengine_cpy.py
│     │        │  ├─ vengine_gen.py
│     │        │  └─ verifier.py
│     │        ├─ cffi-1.15.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ click
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _compat.cpython-310.pyc
│     │        │  │  ├─ _termui_impl.cpython-310.pyc
│     │        │  │  ├─ _textwrap.cpython-310.pyc
│     │        │  │  ├─ _winconsole.cpython-310.pyc
│     │        │  │  ├─ core.cpython-310.pyc
│     │        │  │  ├─ decorators.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ formatting.cpython-310.pyc
│     │        │  │  ├─ globals.cpython-310.pyc
│     │        │  │  ├─ parser.cpython-310.pyc
│     │        │  │  ├─ shell_completion.cpython-310.pyc
│     │        │  │  ├─ termui.cpython-310.pyc
│     │        │  │  ├─ testing.cpython-310.pyc
│     │        │  │  ├─ types.cpython-310.pyc
│     │        │  │  └─ utils.cpython-310.pyc
│     │        │  ├─ _compat.py
│     │        │  ├─ _termui_impl.py
│     │        │  ├─ _textwrap.py
│     │        │  ├─ _winconsole.py
│     │        │  ├─ core.py
│     │        │  ├─ decorators.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ formatting.py
│     │        │  ├─ globals.py
│     │        │  ├─ parser.py
│     │        │  ├─ py.typed
│     │        │  ├─ shell_completion.py
│     │        │  ├─ termui.py
│     │        │  ├─ testing.py
│     │        │  ├─ types.py
│     │        │  └─ utils.py
│     │        ├─ click-8.1.3.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.rst
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ coverage
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ annotate.cpython-310.pyc
│     │        │  │  ├─ bytecode.cpython-310.pyc
│     │        │  │  ├─ cmdline.cpython-310.pyc
│     │        │  │  ├─ collector.cpython-310.pyc
│     │        │  │  ├─ config.cpython-310.pyc
│     │        │  │  ├─ context.cpython-310.pyc
│     │        │  │  ├─ control.cpython-310.pyc
│     │        │  │  ├─ data.cpython-310.pyc
│     │        │  │  ├─ debug.cpython-310.pyc
│     │        │  │  ├─ disposition.cpython-310.pyc
│     │        │  │  ├─ env.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ execfile.cpython-310.pyc
│     │        │  │  ├─ files.cpython-310.pyc
│     │        │  │  ├─ html.cpython-310.pyc
│     │        │  │  ├─ inorout.cpython-310.pyc
│     │        │  │  ├─ jsonreport.cpython-310.pyc
│     │        │  │  ├─ lcovreport.cpython-310.pyc
│     │        │  │  ├─ misc.cpython-310.pyc
│     │        │  │  ├─ multiproc.cpython-310.pyc
│     │        │  │  ├─ numbits.cpython-310.pyc
│     │        │  │  ├─ parser.cpython-310.pyc
│     │        │  │  ├─ phystokens.cpython-310.pyc
│     │        │  │  ├─ plugin.cpython-310.pyc
│     │        │  │  ├─ plugin_support.cpython-310.pyc
│     │        │  │  ├─ python.cpython-310.pyc
│     │        │  │  ├─ pytracer.cpython-310.pyc
│     │        │  │  ├─ report.cpython-310.pyc
│     │        │  │  ├─ report_core.cpython-310.pyc
│     │        │  │  ├─ results.cpython-310.pyc
│     │        │  │  ├─ sqldata.cpython-310.pyc
│     │        │  │  ├─ templite.cpython-310.pyc
│     │        │  │  ├─ tomlconfig.cpython-310.pyc
│     │        │  │  ├─ types.cpython-310.pyc
│     │        │  │  ├─ version.cpython-310.pyc
│     │        │  │  └─ xmlreport.cpython-310.pyc
│     │        │  ├─ annotate.py
│     │        │  ├─ bytecode.py
│     │        │  ├─ cmdline.py
│     │        │  ├─ collector.py
│     │        │  ├─ config.py
│     │        │  ├─ context.py
│     │        │  ├─ control.py
│     │        │  ├─ data.py
│     │        │  ├─ debug.py
│     │        │  ├─ disposition.py
│     │        │  ├─ env.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ execfile.py
│     │        │  ├─ files.py
│     │        │  ├─ fullcoverage
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ encodings.cpython-310.pyc
│     │        │  │  └─ encodings.py
│     │        │  ├─ html.py
│     │        │  ├─ htmlfiles
│     │        │  │  ├─ coverage_html.js
│     │        │  │  ├─ favicon_32.png
│     │        │  │  ├─ index.html
│     │        │  │  ├─ keybd_closed.png
│     │        │  │  ├─ keybd_open.png
│     │        │  │  ├─ pyfile.html
│     │        │  │  ├─ style.css
│     │        │  │  └─ style.scss
│     │        │  ├─ inorout.py
│     │        │  ├─ jsonreport.py
│     │        │  ├─ lcovreport.py
│     │        │  ├─ misc.py
│     │        │  ├─ multiproc.py
│     │        │  ├─ numbits.py
│     │        │  ├─ parser.py
│     │        │  ├─ phystokens.py
│     │        │  ├─ plugin.py
│     │        │  ├─ plugin_support.py
│     │        │  ├─ py.typed
│     │        │  ├─ python.py
│     │        │  ├─ pytracer.py
│     │        │  ├─ report.py
│     │        │  ├─ report_core.py
│     │        │  ├─ results.py
│     │        │  ├─ sqldata.py
│     │        │  ├─ templite.py
│     │        │  ├─ tomlconfig.py
│     │        │  ├─ tracer.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ types.py
│     │        │  ├─ version.py
│     │        │  └─ xmlreport.py
│     │        ├─ coverage-7.2.7.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.txt
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ dateutil
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _common.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  ├─ easter.cpython-310.pyc
│     │        │  │  ├─ relativedelta.cpython-310.pyc
│     │        │  │  ├─ rrule.cpython-310.pyc
│     │        │  │  ├─ tzwin.cpython-310.pyc
│     │        │  │  └─ utils.cpython-310.pyc
│     │        │  ├─ _common.py
│     │        │  ├─ _version.py
│     │        │  ├─ easter.py
│     │        │  ├─ parser
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _parser.cpython-310.pyc
│     │        │  │  │  └─ isoparser.cpython-310.pyc
│     │        │  │  ├─ _parser.py
│     │        │  │  └─ isoparser.py
│     │        │  ├─ relativedelta.py
│     │        │  ├─ rrule.py
│     │        │  ├─ tz
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _common.cpython-310.pyc
│     │        │  │  │  ├─ _factories.cpython-310.pyc
│     │        │  │  │  ├─ tz.cpython-310.pyc
│     │        │  │  │  └─ win.cpython-310.pyc
│     │        │  │  ├─ _common.py
│     │        │  │  ├─ _factories.py
│     │        │  │  ├─ tz.py
│     │        │  │  └─ win.py
│     │        │  ├─ tzwin.py
│     │        │  ├─ utils.py
│     │        │  └─ zoneinfo
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  └─ rebuild.cpython-310.pyc
│     │        │     ├─ dateutil-zoneinfo.tar.gz
│     │        │     └─ rebuild.py
│     │        ├─ decouple.py
│     │        ├─ distutils-precedence.pth
│     │        ├─ dns
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _asyncbackend.cpython-310.pyc
│     │        │  │  ├─ _asyncio_backend.cpython-310.pyc
│     │        │  │  ├─ _curio_backend.cpython-310.pyc
│     │        │  │  ├─ _immutable_ctx.cpython-310.pyc
│     │        │  │  ├─ _trio_backend.cpython-310.pyc
│     │        │  │  ├─ asyncbackend.cpython-310.pyc
│     │        │  │  ├─ asyncquery.cpython-310.pyc
│     │        │  │  ├─ asyncresolver.cpython-310.pyc
│     │        │  │  ├─ dnssec.cpython-310.pyc
│     │        │  │  ├─ dnssectypes.cpython-310.pyc
│     │        │  │  ├─ e164.cpython-310.pyc
│     │        │  │  ├─ edns.cpython-310.pyc
│     │        │  │  ├─ entropy.cpython-310.pyc
│     │        │  │  ├─ enum.cpython-310.pyc
│     │        │  │  ├─ exception.cpython-310.pyc
│     │        │  │  ├─ flags.cpython-310.pyc
│     │        │  │  ├─ grange.cpython-310.pyc
│     │        │  │  ├─ immutable.cpython-310.pyc
│     │        │  │  ├─ inet.cpython-310.pyc
│     │        │  │  ├─ ipv4.cpython-310.pyc
│     │        │  │  ├─ ipv6.cpython-310.pyc
│     │        │  │  ├─ message.cpython-310.pyc
│     │        │  │  ├─ name.cpython-310.pyc
│     │        │  │  ├─ namedict.cpython-310.pyc
│     │        │  │  ├─ node.cpython-310.pyc
│     │        │  │  ├─ opcode.cpython-310.pyc
│     │        │  │  ├─ query.cpython-310.pyc
│     │        │  │  ├─ rcode.cpython-310.pyc
│     │        │  │  ├─ rdata.cpython-310.pyc
│     │        │  │  ├─ rdataclass.cpython-310.pyc
│     │        │  │  ├─ rdataset.cpython-310.pyc
│     │        │  │  ├─ rdatatype.cpython-310.pyc
│     │        │  │  ├─ renderer.cpython-310.pyc
│     │        │  │  ├─ resolver.cpython-310.pyc
│     │        │  │  ├─ reversename.cpython-310.pyc
│     │        │  │  ├─ rrset.cpython-310.pyc
│     │        │  │  ├─ serial.cpython-310.pyc
│     │        │  │  ├─ set.cpython-310.pyc
│     │        │  │  ├─ tokenizer.cpython-310.pyc
│     │        │  │  ├─ transaction.cpython-310.pyc
│     │        │  │  ├─ tsig.cpython-310.pyc
│     │        │  │  ├─ tsigkeyring.cpython-310.pyc
│     │        │  │  ├─ ttl.cpython-310.pyc
│     │        │  │  ├─ update.cpython-310.pyc
│     │        │  │  ├─ version.cpython-310.pyc
│     │        │  │  ├─ versioned.cpython-310.pyc
│     │        │  │  ├─ win32util.cpython-310.pyc
│     │        │  │  ├─ wire.cpython-310.pyc
│     │        │  │  ├─ xfr.cpython-310.pyc
│     │        │  │  ├─ zone.cpython-310.pyc
│     │        │  │  ├─ zonefile.cpython-310.pyc
│     │        │  │  └─ zonetypes.cpython-310.pyc
│     │        │  ├─ _asyncbackend.py
│     │        │  ├─ _asyncio_backend.py
│     │        │  ├─ _curio_backend.py
│     │        │  ├─ _immutable_ctx.py
│     │        │  ├─ _trio_backend.py
│     │        │  ├─ asyncbackend.py
│     │        │  ├─ asyncquery.py
│     │        │  ├─ asyncresolver.py
│     │        │  ├─ dnssec.py
│     │        │  ├─ dnssectypes.py
│     │        │  ├─ e164.py
│     │        │  ├─ edns.py
│     │        │  ├─ entropy.py
│     │        │  ├─ enum.py
│     │        │  ├─ exception.py
│     │        │  ├─ flags.py
│     │        │  ├─ grange.py
│     │        │  ├─ immutable.py
│     │        │  ├─ inet.py
│     │        │  ├─ ipv4.py
│     │        │  ├─ ipv6.py
│     │        │  ├─ message.py
│     │        │  ├─ name.py
│     │        │  ├─ namedict.py
│     │        │  ├─ node.py
│     │        │  ├─ opcode.py
│     │        │  ├─ py.typed
│     │        │  ├─ query.py
│     │        │  ├─ quic
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _asyncio.cpython-310.pyc
│     │        │  │  │  ├─ _common.cpython-310.pyc
│     │        │  │  │  ├─ _sync.cpython-310.pyc
│     │        │  │  │  └─ _trio.cpython-310.pyc
│     │        │  │  ├─ _asyncio.py
│     │        │  │  ├─ _common.py
│     │        │  │  ├─ _sync.py
│     │        │  │  └─ _trio.py
│     │        │  ├─ rcode.py
│     │        │  ├─ rdata.py
│     │        │  ├─ rdataclass.py
│     │        │  ├─ rdataset.py
│     │        │  ├─ rdatatype.py
│     │        │  ├─ rdtypes
│     │        │  │  ├─ ANY
│     │        │  │  │  ├─ AFSDB.py
│     │        │  │  │  ├─ AMTRELAY.py
│     │        │  │  │  ├─ AVC.py
│     │        │  │  │  ├─ CAA.py
│     │        │  │  │  ├─ CDNSKEY.py
│     │        │  │  │  ├─ CDS.py
│     │        │  │  │  ├─ CERT.py
│     │        │  │  │  ├─ CNAME.py
│     │        │  │  │  ├─ CSYNC.py
│     │        │  │  │  ├─ DLV.py
│     │        │  │  │  ├─ DNAME.py
│     │        │  │  │  ├─ DNSKEY.py
│     │        │  │  │  ├─ DS.py
│     │        │  │  │  ├─ EUI48.py
│     │        │  │  │  ├─ EUI64.py
│     │        │  │  │  ├─ GPOS.py
│     │        │  │  │  ├─ HINFO.py
│     │        │  │  │  ├─ HIP.py
│     │        │  │  │  ├─ ISDN.py
│     │        │  │  │  ├─ L32.py
│     │        │  │  │  ├─ L64.py
│     │        │  │  │  ├─ LOC.py
│     │        │  │  │  ├─ LP.py
│     │        │  │  │  ├─ MX.py
│     │        │  │  │  ├─ NID.py
│     │        │  │  │  ├─ NINFO.py
│     │        │  │  │  ├─ NS.py
│     │        │  │  │  ├─ NSEC.py
│     │        │  │  │  ├─ NSEC3.py
│     │        │  │  │  ├─ NSEC3PARAM.py
│     │        │  │  │  ├─ OPENPGPKEY.py
│     │        │  │  │  ├─ OPT.py
│     │        │  │  │  ├─ PTR.py
│     │        │  │  │  ├─ RP.py
│     │        │  │  │  ├─ RRSIG.py
│     │        │  │  │  ├─ RT.py
│     │        │  │  │  ├─ SMIMEA.py
│     │        │  │  │  ├─ SOA.py
│     │        │  │  │  ├─ SPF.py
│     │        │  │  │  ├─ SSHFP.py
│     │        │  │  │  ├─ TKEY.py
│     │        │  │  │  ├─ TLSA.py
│     │        │  │  │  ├─ TSIG.py
│     │        │  │  │  ├─ TXT.py
│     │        │  │  │  ├─ URI.py
│     │        │  │  │  ├─ X25.py
│     │        │  │  │  ├─ ZONEMD.py
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  └─ __pycache__
│     │        │  │  │     ├─ AFSDB.cpython-310.pyc
│     │        │  │  │     ├─ AMTRELAY.cpython-310.pyc
│     │        │  │  │     ├─ AVC.cpython-310.pyc
│     │        │  │  │     ├─ CAA.cpython-310.pyc
│     │        │  │  │     ├─ CDNSKEY.cpython-310.pyc
│     │        │  │  │     ├─ CDS.cpython-310.pyc
│     │        │  │  │     ├─ CERT.cpython-310.pyc
│     │        │  │  │     ├─ CNAME.cpython-310.pyc
│     │        │  │  │     ├─ CSYNC.cpython-310.pyc
│     │        │  │  │     ├─ DLV.cpython-310.pyc
│     │        │  │  │     ├─ DNAME.cpython-310.pyc
│     │        │  │  │     ├─ DNSKEY.cpython-310.pyc
│     │        │  │  │     ├─ DS.cpython-310.pyc
│     │        │  │  │     ├─ EUI48.cpython-310.pyc
│     │        │  │  │     ├─ EUI64.cpython-310.pyc
│     │        │  │  │     ├─ GPOS.cpython-310.pyc
│     │        │  │  │     ├─ HINFO.cpython-310.pyc
│     │        │  │  │     ├─ HIP.cpython-310.pyc
│     │        │  │  │     ├─ ISDN.cpython-310.pyc
│     │        │  │  │     ├─ L32.cpython-310.pyc
│     │        │  │  │     ├─ L64.cpython-310.pyc
│     │        │  │  │     ├─ LOC.cpython-310.pyc
│     │        │  │  │     ├─ LP.cpython-310.pyc
│     │        │  │  │     ├─ MX.cpython-310.pyc
│     │        │  │  │     ├─ NID.cpython-310.pyc
│     │        │  │  │     ├─ NINFO.cpython-310.pyc
│     │        │  │  │     ├─ NS.cpython-310.pyc
│     │        │  │  │     ├─ NSEC.cpython-310.pyc
│     │        │  │  │     ├─ NSEC3.cpython-310.pyc
│     │        │  │  │     ├─ NSEC3PARAM.cpython-310.pyc
│     │        │  │  │     ├─ OPENPGPKEY.cpython-310.pyc
│     │        │  │  │     ├─ OPT.cpython-310.pyc
│     │        │  │  │     ├─ PTR.cpython-310.pyc
│     │        │  │  │     ├─ RP.cpython-310.pyc
│     │        │  │  │     ├─ RRSIG.cpython-310.pyc
│     │        │  │  │     ├─ RT.cpython-310.pyc
│     │        │  │  │     ├─ SMIMEA.cpython-310.pyc
│     │        │  │  │     ├─ SOA.cpython-310.pyc
│     │        │  │  │     ├─ SPF.cpython-310.pyc
│     │        │  │  │     ├─ SSHFP.cpython-310.pyc
│     │        │  │  │     ├─ TKEY.cpython-310.pyc
│     │        │  │  │     ├─ TLSA.cpython-310.pyc
│     │        │  │  │     ├─ TSIG.cpython-310.pyc
│     │        │  │  │     ├─ TXT.cpython-310.pyc
│     │        │  │  │     ├─ URI.cpython-310.pyc
│     │        │  │  │     ├─ X25.cpython-310.pyc
│     │        │  │  │     ├─ ZONEMD.cpython-310.pyc
│     │        │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  ├─ CH
│     │        │  │  │  ├─ A.py
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  └─ __pycache__
│     │        │  │  │     ├─ A.cpython-310.pyc
│     │        │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  ├─ IN
│     │        │  │  │  ├─ A.py
│     │        │  │  │  ├─ AAAA.py
│     │        │  │  │  ├─ APL.py
│     │        │  │  │  ├─ DHCID.py
│     │        │  │  │  ├─ HTTPS.py
│     │        │  │  │  ├─ IPSECKEY.py
│     │        │  │  │  ├─ KX.py
│     │        │  │  │  ├─ NAPTR.py
│     │        │  │  │  ├─ NSAP.py
│     │        │  │  │  ├─ NSAP_PTR.py
│     │        │  │  │  ├─ PX.py
│     │        │  │  │  ├─ SRV.py
│     │        │  │  │  ├─ SVCB.py
│     │        │  │  │  ├─ WKS.py
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  └─ __pycache__
│     │        │  │  │     ├─ A.cpython-310.pyc
│     │        │  │  │     ├─ AAAA.cpython-310.pyc
│     │        │  │  │     ├─ APL.cpython-310.pyc
│     │        │  │  │     ├─ DHCID.cpython-310.pyc
│     │        │  │  │     ├─ HTTPS.cpython-310.pyc
│     │        │  │  │     ├─ IPSECKEY.cpython-310.pyc
│     │        │  │  │     ├─ KX.cpython-310.pyc
│     │        │  │  │     ├─ NAPTR.cpython-310.pyc
│     │        │  │  │     ├─ NSAP.cpython-310.pyc
│     │        │  │  │     ├─ NSAP_PTR.cpython-310.pyc
│     │        │  │  │     ├─ PX.cpython-310.pyc
│     │        │  │  │     ├─ SRV.cpython-310.pyc
│     │        │  │  │     ├─ SVCB.cpython-310.pyc
│     │        │  │  │     ├─ WKS.cpython-310.pyc
│     │        │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ dnskeybase.cpython-310.pyc
│     │        │  │  │  ├─ dsbase.cpython-310.pyc
│     │        │  │  │  ├─ euibase.cpython-310.pyc
│     │        │  │  │  ├─ mxbase.cpython-310.pyc
│     │        │  │  │  ├─ nsbase.cpython-310.pyc
│     │        │  │  │  ├─ svcbbase.cpython-310.pyc
│     │        │  │  │  ├─ tlsabase.cpython-310.pyc
│     │        │  │  │  ├─ txtbase.cpython-310.pyc
│     │        │  │  │  └─ util.cpython-310.pyc
│     │        │  │  ├─ dnskeybase.py
│     │        │  │  ├─ dsbase.py
│     │        │  │  ├─ euibase.py
│     │        │  │  ├─ mxbase.py
│     │        │  │  ├─ nsbase.py
│     │        │  │  ├─ svcbbase.py
│     │        │  │  ├─ tlsabase.py
│     │        │  │  ├─ txtbase.py
│     │        │  │  └─ util.py
│     │        │  ├─ renderer.py
│     │        │  ├─ resolver.py
│     │        │  ├─ reversename.py
│     │        │  ├─ rrset.py
│     │        │  ├─ serial.py
│     │        │  ├─ set.py
│     │        │  ├─ tokenizer.py
│     │        │  ├─ transaction.py
│     │        │  ├─ tsig.py
│     │        │  ├─ tsigkeyring.py
│     │        │  ├─ ttl.py
│     │        │  ├─ update.py
│     │        │  ├─ version.py
│     │        │  ├─ versioned.py
│     │        │  ├─ win32util.py
│     │        │  ├─ wire.py
│     │        │  ├─ xfr.py
│     │        │  ├─ zone.py
│     │        │  ├─ zonefile.py
│     │        │  └─ zonetypes.py
│     │        ├─ dnspython-2.3.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ dotenv
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ cli.cpython-310.pyc
│     │        │  │  ├─ ipython.cpython-310.pyc
│     │        │  │  ├─ main.cpython-310.pyc
│     │        │  │  ├─ parser.cpython-310.pyc
│     │        │  │  ├─ variables.cpython-310.pyc
│     │        │  │  └─ version.cpython-310.pyc
│     │        │  ├─ cli.py
│     │        │  ├─ ipython.py
│     │        │  ├─ main.py
│     │        │  ├─ parser.py
│     │        │  ├─ py.typed
│     │        │  ├─ variables.py
│     │        │  └─ version.py
│     │        ├─ editorconfig
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ compat.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ fnmatch.cpython-310.pyc
│     │        │  │  ├─ handler.cpython-310.pyc
│     │        │  │  ├─ ini.cpython-310.pyc
│     │        │  │  ├─ version.cpython-310.pyc
│     │        │  │  └─ versiontools.cpython-310.pyc
│     │        │  ├─ compat.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ fnmatch.py
│     │        │  ├─ handler.py
│     │        │  ├─ ini.py
│     │        │  ├─ version.py
│     │        │  └─ versiontools.py
│     │        ├─ email_validator
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ deliverability.cpython-310.pyc
│     │        │  │  ├─ exceptions_types.cpython-310.pyc
│     │        │  │  ├─ rfc_constants.cpython-310.pyc
│     │        │  │  ├─ syntax.cpython-310.pyc
│     │        │  │  └─ validate_email.cpython-310.pyc
│     │        │  ├─ deliverability.py
│     │        │  ├─ exceptions_types.py
│     │        │  ├─ py.typed
│     │        │  ├─ rfc_constants.py
│     │        │  ├─ syntax.py
│     │        │  └─ validate_email.py
│     │        ├─ email_validator-2.0.0.post2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ exceptiongroup
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _catch.cpython-310.pyc
│     │        │  │  ├─ _exceptions.cpython-310.pyc
│     │        │  │  ├─ _formatting.cpython-310.pyc
│     │        │  │  └─ _version.cpython-310.pyc
│     │        │  ├─ _catch.py
│     │        │  ├─ _exceptions.py
│     │        │  ├─ _formatting.py
│     │        │  ├─ _version.py
│     │        │  └─ py.typed
│     │        ├─ exceptiongroup-1.1.2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ factory
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ alchemy.cpython-310.pyc
│     │        │  │  ├─ base.cpython-310.pyc
│     │        │  │  ├─ builder.cpython-310.pyc
│     │        │  │  ├─ declarations.cpython-310.pyc
│     │        │  │  ├─ django.cpython-310.pyc
│     │        │  │  ├─ enums.cpython-310.pyc
│     │        │  │  ├─ errors.cpython-310.pyc
│     │        │  │  ├─ faker.cpython-310.pyc
│     │        │  │  ├─ fuzzy.cpython-310.pyc
│     │        │  │  ├─ helpers.cpython-310.pyc
│     │        │  │  ├─ mogo.cpython-310.pyc
│     │        │  │  ├─ mongoengine.cpython-310.pyc
│     │        │  │  ├─ random.cpython-310.pyc
│     │        │  │  └─ utils.cpython-310.pyc
│     │        │  ├─ alchemy.py
│     │        │  ├─ base.py
│     │        │  ├─ builder.py
│     │        │  ├─ declarations.py
│     │        │  ├─ django.py
│     │        │  ├─ enums.py
│     │        │  ├─ errors.py
│     │        │  ├─ faker.py
│     │        │  ├─ fuzzy.py
│     │        │  ├─ helpers.py
│     │        │  ├─ mogo.py
│     │        │  ├─ mongoengine.py
│     │        │  ├─ random.py
│     │        │  └─ utils.py
│     │        ├─ factory_boy-3.2.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ faker
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ cli.cpython-310.pyc
│     │        │  │  ├─ config.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ config.cpython-310.pyc
│     │        │  │  ├─ documentor.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ factory.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ factory.cpython-310.pyc
│     │        │  │  ├─ generator.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ generator.cpython-310.pyc
│     │        │  │  ├─ proxy.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ proxy.cpython-310.pyc
│     │        │  │  ├─ typing.cpython-310-pytest-7.4.0.pyc
│     │        │  │  └─ typing.cpython-310.pyc
│     │        │  ├─ cli.py
│     │        │  ├─ config.py
│     │        │  ├─ contrib
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  └─ pytest
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ plugin.cpython-310-pytest-7.4.0.pyc
│     │        │  │     │  └─ plugin.cpython-310.pyc
│     │        │  │     └─ plugin.py
│     │        │  ├─ decode
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ codes.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  └─ codes.cpython-310.pyc
│     │        │  │  └─ codes.py
│     │        │  ├─ documentor.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ factory.py
│     │        │  ├─ generator.py
│     │        │  ├─ providers
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ address
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_AU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_GB
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_NZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_MX
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ he_IL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hi_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ja_JP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ka_GE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ne_NP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sl_SI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ta_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ uk_UA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ automotive
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_BH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_JO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_PS
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_SA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_GB
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_NZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ et_EE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ he_IL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lt_LT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sq_AL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ vi_VN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ bank
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_GB
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_MX
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_CN
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ barcode
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ ja_JP
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ color
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ color.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ color.cpython-310.pyc
│     │        │  │  │  ├─ ar_PS
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bg_BG
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ color.py
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ he_IL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ uk_UA
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ company
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bg_BG
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_MX
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ja_JP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sl_SI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ credit_card
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ ru_RU
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ currency
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_AU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ tr_TR
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ date_time
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_AA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_EG
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hi_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sl_SI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ta_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ emoji
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ en_US
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ file
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ en_US
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ geo
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ tr_TR
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ internet
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_AA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bg_BG
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bs_BA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_AU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_GB
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_NZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ja_JP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sl_SI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ uk_UA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ isbn
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ isbn.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  ├─ isbn.cpython-310.pyc
│     │        │  │  │  │  ├─ rules.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ rules.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ isbn.py
│     │        │  │  │  └─ rules.py
│     │        │  │  ├─ job
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_AA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bs_BA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_MX
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ja_JP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ uk_UA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ lorem
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_AA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ he_IL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ja_JP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ la
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ misc
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ tl_PH
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ passport
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ en_US
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ person
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_AA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_PS
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_SA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bg_BG
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_GB
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_NZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_MX
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ et_EE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_QC
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ga_IE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ he_IL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hi_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ja_JP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ka_GE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lt_LT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lv_LV
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ne_NP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ or_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sl_SI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ta_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tw_GH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ uk_UA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ phone_number
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_AE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_JO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ar_PS
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bg_BG
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bs_BA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ da_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_AU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_GB
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_NZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_AR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_MX
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fa_IR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ he_IL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hi_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hy_AM
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ id_ID
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ja_JP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lt_LT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lv_LV
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ne_NP
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sl_SI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ta_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tw_GH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ uk_UA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ profile
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ en_US
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ python
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ en_US
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  ├─ sbn
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ rules.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  ├─ rules.cpython-310.pyc
│     │        │  │  │  │  ├─ sbn.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ sbn.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ rules.py
│     │        │  │  │  └─ sbn.py
│     │        │  │  ├─ ssn
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ az_AZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bg_BG
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ bn_BD
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cs_CZ
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_AT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ de_DE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ dk_DK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_CY
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ el_GR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_GB
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_IN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ en_US
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_CO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_ES
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ es_MX
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ et_EE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fi_FI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fil_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_CH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ fr_FR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ he_IL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hr_HR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ hu_HU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ it_IT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ko_KR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lb_LU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lt_LT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ lv_LV
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ mt_MT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_BE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ nl_NL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ no_NO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pl_PL
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_BR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ pt_PT
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ro_RO
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ru_RU
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sk_SK
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sl_SI
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ sv_SE
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ th_TH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tl_PH
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ tr_TR
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ uk_UA
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ zh_CN
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ zh_TW
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     └─ __pycache__
│     │        │  │  │        └─ __init__.cpython-310.pyc
│     │        │  │  └─ user_agent
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │     │  └─ __init__.cpython-310.pyc
│     │        │  │     └─ en_US
│     │        │  │        ├─ __init__.py
│     │        │  │        └─ __pycache__
│     │        │  │           └─ __init__.cpython-310.pyc
│     │        │  ├─ proxy.py
│     │        │  ├─ py.typed
│     │        │  ├─ sphinx
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ autodoc.cpython-310.pyc
│     │        │  │  │  ├─ docstring.cpython-310.pyc
│     │        │  │  │  ├─ documentor.cpython-310.pyc
│     │        │  │  │  └─ validator.cpython-310.pyc
│     │        │  │  ├─ autodoc.py
│     │        │  │  ├─ docstring.py
│     │        │  │  ├─ documentor.py
│     │        │  │  └─ validator.py
│     │        │  ├─ typing.py
│     │        │  └─ utils
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ checksums.cpython-310.pyc
│     │        │     │  ├─ datasets.cpython-310-pytest-7.4.0.pyc
│     │        │     │  ├─ datasets.cpython-310.pyc
│     │        │     │  ├─ decorators.cpython-310-pytest-7.4.0.pyc
│     │        │     │  ├─ decorators.cpython-310.pyc
│     │        │     │  ├─ distribution.cpython-310-pytest-7.4.0.pyc
│     │        │     │  ├─ distribution.cpython-310.pyc
│     │        │     │  ├─ loading.cpython-310-pytest-7.4.0.pyc
│     │        │     │  ├─ loading.cpython-310.pyc
│     │        │     │  ├─ text.cpython-310-pytest-7.4.0.pyc
│     │        │     │  └─ text.cpython-310.pyc
│     │        │     ├─ checksums.py
│     │        │     ├─ datasets.py
│     │        │     ├─ decorators.py
│     │        │     ├─ distribution.py
│     │        │     ├─ loading.py
│     │        │     └─ text.py
│     │        ├─ fast_query_parsers
│     │        │  ├─ __init__.py
│     │        │  ├─ __init__.pyi
│     │        │  ├─ __pycache__
│     │        │  │  └─ __init__.cpython-310.pyc
│     │        │  ├─ fast_query_parsers.abi3.so
│     │        │  └─ py.typed
│     │        ├─ fast_query_parsers-0.4.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ license_files
│     │        │     └─ LICENSE
│     │        ├─ fastjsonschema
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ draft04.cpython-310.pyc
│     │        │  │  ├─ draft06.cpython-310.pyc
│     │        │  │  ├─ draft07.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ generator.cpython-310.pyc
│     │        │  │  ├─ indent.cpython-310.pyc
│     │        │  │  ├─ ref_resolver.cpython-310.pyc
│     │        │  │  └─ version.cpython-310.pyc
│     │        │  ├─ draft04.py
│     │        │  ├─ draft06.py
│     │        │  ├─ draft07.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ generator.py
│     │        │  ├─ indent.py
│     │        │  ├─ ref_resolver.py
│     │        │  └─ version.py
│     │        ├─ fastjsonschema-2.17.1.dist-info
│     │        │  ├─ AUTHORS
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ greenlet
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  └─ __init__.cpython-310.pyc
│     │        │  ├─ _greenlet.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ greenlet.cpp
│     │        │  ├─ greenlet.h
│     │        │  ├─ greenlet_allocator.hpp
│     │        │  ├─ greenlet_compiler_compat.hpp
│     │        │  ├─ greenlet_cpython_compat.hpp
│     │        │  ├─ greenlet_exceptions.hpp
│     │        │  ├─ greenlet_greenlet.hpp
│     │        │  ├─ greenlet_internal.hpp
│     │        │  ├─ greenlet_refs.hpp
│     │        │  ├─ greenlet_slp_switch.hpp
│     │        │  ├─ greenlet_thread_state.hpp
│     │        │  ├─ greenlet_thread_state_dict_cleanup.hpp
│     │        │  ├─ greenlet_thread_support.hpp
│     │        │  ├─ platform
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ setup_switch_x64_masm.cmd
│     │        │  │  ├─ switch_aarch64_gcc.h
│     │        │  │  ├─ switch_alpha_unix.h
│     │        │  │  ├─ switch_amd64_unix.h
│     │        │  │  ├─ switch_arm32_gcc.h
│     │        │  │  ├─ switch_arm32_ios.h
│     │        │  │  ├─ switch_arm64_masm.asm
│     │        │  │  ├─ switch_arm64_masm.obj
│     │        │  │  ├─ switch_arm64_msvc.h
│     │        │  │  ├─ switch_csky_gcc.h
│     │        │  │  ├─ switch_m68k_gcc.h
│     │        │  │  ├─ switch_mips_unix.h
│     │        │  │  ├─ switch_ppc64_aix.h
│     │        │  │  ├─ switch_ppc64_linux.h
│     │        │  │  ├─ switch_ppc_aix.h
│     │        │  │  ├─ switch_ppc_linux.h
│     │        │  │  ├─ switch_ppc_macosx.h
│     │        │  │  ├─ switch_ppc_unix.h
│     │        │  │  ├─ switch_riscv_unix.h
│     │        │  │  ├─ switch_s390_unix.h
│     │        │  │  ├─ switch_sparc_sun_gcc.h
│     │        │  │  ├─ switch_x32_unix.h
│     │        │  │  ├─ switch_x64_masm.asm
│     │        │  │  ├─ switch_x64_masm.obj
│     │        │  │  ├─ switch_x64_msvc.h
│     │        │  │  ├─ switch_x86_msvc.h
│     │        │  │  └─ switch_x86_unix.h
│     │        │  ├─ slp_platformselect.h
│     │        │  └─ tests
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ leakcheck.cpython-310.pyc
│     │        │     │  ├─ test_contextvars.cpython-310.pyc
│     │        │     │  ├─ test_cpp.cpython-310.pyc
│     │        │     │  ├─ test_extension_interface.cpython-310.pyc
│     │        │     │  ├─ test_gc.cpython-310.pyc
│     │        │     │  ├─ test_generator.cpython-310.pyc
│     │        │     │  ├─ test_generator_nested.cpython-310.pyc
│     │        │     │  ├─ test_greenlet.cpython-310.pyc
│     │        │     │  ├─ test_greenlet_trash.cpython-310.pyc
│     │        │     │  ├─ test_leaks.cpython-310.pyc
│     │        │     │  ├─ test_stack_saved.cpython-310.pyc
│     │        │     │  ├─ test_throw.cpython-310.pyc
│     │        │     │  ├─ test_tracing.cpython-310.pyc
│     │        │     │  ├─ test_version.cpython-310.pyc
│     │        │     │  └─ test_weakref.cpython-310.pyc
│     │        │     ├─ _test_extension.c
│     │        │     ├─ _test_extension.cpython-310-x86_64-linux-gnu.so
│     │        │     ├─ _test_extension_cpp.cpp
│     │        │     ├─ _test_extension_cpp.cpython-310-x86_64-linux-gnu.so
│     │        │     ├─ leakcheck.py
│     │        │     ├─ test_contextvars.py
│     │        │     ├─ test_cpp.py
│     │        │     ├─ test_extension_interface.py
│     │        │     ├─ test_gc.py
│     │        │     ├─ test_generator.py
│     │        │     ├─ test_generator_nested.py
│     │        │     ├─ test_greenlet.py
│     │        │     ├─ test_greenlet_trash.py
│     │        │     ├─ test_leaks.py
│     │        │     ├─ test_stack_saved.py
│     │        │     ├─ test_throw.py
│     │        │     ├─ test_tracing.py
│     │        │     ├─ test_version.py
│     │        │     └─ test_weakref.py
│     │        ├─ greenlet-2.0.2.dist-info
│     │        │  ├─ AUTHORS
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ LICENSE.PSF
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ h11
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _abnf.cpython-310.pyc
│     │        │  │  ├─ _connection.cpython-310.pyc
│     │        │  │  ├─ _events.cpython-310.pyc
│     │        │  │  ├─ _headers.cpython-310.pyc
│     │        │  │  ├─ _readers.cpython-310.pyc
│     │        │  │  ├─ _receivebuffer.cpython-310.pyc
│     │        │  │  ├─ _state.cpython-310.pyc
│     │        │  │  ├─ _util.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  └─ _writers.cpython-310.pyc
│     │        │  ├─ _abnf.py
│     │        │  ├─ _connection.py
│     │        │  ├─ _events.py
│     │        │  ├─ _headers.py
│     │        │  ├─ _readers.py
│     │        │  ├─ _receivebuffer.py
│     │        │  ├─ _state.py
│     │        │  ├─ _util.py
│     │        │  ├─ _version.py
│     │        │  ├─ _writers.py
│     │        │  ├─ py.typed
│     │        │  └─ tests
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ helpers.cpython-310.pyc
│     │        │     │  ├─ test_against_stdlib_http.cpython-310.pyc
│     │        │     │  ├─ test_connection.cpython-310.pyc
│     │        │     │  ├─ test_events.cpython-310.pyc
│     │        │     │  ├─ test_headers.cpython-310.pyc
│     │        │     │  ├─ test_helpers.cpython-310.pyc
│     │        │     │  ├─ test_io.cpython-310.pyc
│     │        │     │  ├─ test_receivebuffer.cpython-310.pyc
│     │        │     │  ├─ test_state.cpython-310.pyc
│     │        │     │  └─ test_util.cpython-310.pyc
│     │        │     ├─ data
│     │        │     │  └─ test-file
│     │        │     ├─ helpers.py
│     │        │     ├─ test_against_stdlib_http.py
│     │        │     ├─ test_connection.py
│     │        │     ├─ test_events.py
│     │        │     ├─ test_headers.py
│     │        │     ├─ test_helpers.py
│     │        │     ├─ test_io.py
│     │        │     ├─ test_receivebuffer.py
│     │        │     ├─ test_state.py
│     │        │     └─ test_util.py
│     │        ├─ h11-0.14.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.txt
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ html2text
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ cli.cpython-310.pyc
│     │        │  │  ├─ config.cpython-310.pyc
│     │        │  │  ├─ elements.cpython-310.pyc
│     │        │  │  ├─ typing.cpython-310.pyc
│     │        │  │  └─ utils.cpython-310.pyc
│     │        │  ├─ cli.py
│     │        │  ├─ config.py
│     │        │  ├─ elements.py
│     │        │  ├─ py.typed
│     │        │  ├─ typing.py
│     │        │  └─ utils.py
│     │        ├─ html2text-2020.1.16.dist-info
│     │        │  ├─ AUTHORS.rst
│     │        │  ├─ COPYING
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ httpcore
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _api.cpython-310.pyc
│     │        │  │  ├─ _exceptions.cpython-310.pyc
│     │        │  │  ├─ _models.cpython-310.pyc
│     │        │  │  ├─ _ssl.cpython-310.pyc
│     │        │  │  ├─ _synchronization.cpython-310.pyc
│     │        │  │  ├─ _trace.cpython-310.pyc
│     │        │  │  └─ _utils.cpython-310.pyc
│     │        │  ├─ _api.py
│     │        │  ├─ _async
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ connection.cpython-310.pyc
│     │        │  │  │  ├─ connection_pool.cpython-310.pyc
│     │        │  │  │  ├─ http11.cpython-310.pyc
│     │        │  │  │  ├─ http2.cpython-310.pyc
│     │        │  │  │  ├─ http_proxy.cpython-310.pyc
│     │        │  │  │  ├─ interfaces.cpython-310.pyc
│     │        │  │  │  └─ socks_proxy.cpython-310.pyc
│     │        │  │  ├─ connection.py
│     │        │  │  ├─ connection_pool.py
│     │        │  │  ├─ http11.py
│     │        │  │  ├─ http2.py
│     │        │  │  ├─ http_proxy.py
│     │        │  │  ├─ interfaces.py
│     │        │  │  └─ socks_proxy.py
│     │        │  ├─ _exceptions.py
│     │        │  ├─ _models.py
│     │        │  ├─ _ssl.py
│     │        │  ├─ _sync
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ connection.cpython-310.pyc
│     │        │  │  │  ├─ connection_pool.cpython-310.pyc
│     │        │  │  │  ├─ http11.cpython-310.pyc
│     │        │  │  │  ├─ http2.cpython-310.pyc
│     │        │  │  │  ├─ http_proxy.cpython-310.pyc
│     │        │  │  │  ├─ interfaces.cpython-310.pyc
│     │        │  │  │  └─ socks_proxy.cpython-310.pyc
│     │        │  │  ├─ connection.py
│     │        │  │  ├─ connection_pool.py
│     │        │  │  ├─ http11.py
│     │        │  │  ├─ http2.py
│     │        │  │  ├─ http_proxy.py
│     │        │  │  ├─ interfaces.py
│     │        │  │  └─ socks_proxy.py
│     │        │  ├─ _synchronization.py
│     │        │  ├─ _trace.py
│     │        │  ├─ _utils.py
│     │        │  ├─ backends
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asyncio.cpython-310.pyc
│     │        │  │  │  ├─ auto.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ mock.cpython-310.pyc
│     │        │  │  │  ├─ sync.cpython-310.pyc
│     │        │  │  │  └─ trio.cpython-310.pyc
│     │        │  │  ├─ asyncio.py
│     │        │  │  ├─ auto.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ mock.py
│     │        │  │  ├─ sync.py
│     │        │  │  └─ trio.py
│     │        │  └─ py.typed
│     │        ├─ httpcore-0.17.2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.md
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ httptools
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  └─ _version.cpython-310.pyc
│     │        │  ├─ _version.py
│     │        │  └─ parser
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  └─ errors.cpython-310.pyc
│     │        │     ├─ errors.py
│     │        │     ├─ parser.c
│     │        │     ├─ parser.cpython-310-x86_64-linux-gnu.so
│     │        │     ├─ url_parser.c
│     │        │     └─ url_parser.cpython-310-x86_64-linux-gnu.so
│     │        ├─ httptools-0.5.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ httpx
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __version__.cpython-310.pyc
│     │        │  │  ├─ _api.cpython-310.pyc
│     │        │  │  ├─ _auth.cpython-310.pyc
│     │        │  │  ├─ _client.cpython-310.pyc
│     │        │  │  ├─ _compat.cpython-310.pyc
│     │        │  │  ├─ _config.cpython-310.pyc
│     │        │  │  ├─ _content.cpython-310.pyc
│     │        │  │  ├─ _decoders.cpython-310.pyc
│     │        │  │  ├─ _exceptions.cpython-310.pyc
│     │        │  │  ├─ _main.cpython-310.pyc
│     │        │  │  ├─ _models.cpython-310.pyc
│     │        │  │  ├─ _multipart.cpython-310.pyc
│     │        │  │  ├─ _status_codes.cpython-310.pyc
│     │        │  │  ├─ _types.cpython-310.pyc
│     │        │  │  ├─ _urlparse.cpython-310.pyc
│     │        │  │  ├─ _urls.cpython-310.pyc
│     │        │  │  └─ _utils.cpython-310.pyc
│     │        │  ├─ __version__.py
│     │        │  ├─ _api.py
│     │        │  ├─ _auth.py
│     │        │  ├─ _client.py
│     │        │  ├─ _compat.py
│     │        │  ├─ _config.py
│     │        │  ├─ _content.py
│     │        │  ├─ _decoders.py
│     │        │  ├─ _exceptions.py
│     │        │  ├─ _main.py
│     │        │  ├─ _models.py
│     │        │  ├─ _multipart.py
│     │        │  ├─ _status_codes.py
│     │        │  ├─ _transports
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asgi.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ default.cpython-310.pyc
│     │        │  │  │  ├─ mock.cpython-310.pyc
│     │        │  │  │  └─ wsgi.cpython-310.pyc
│     │        │  │  ├─ asgi.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ default.py
│     │        │  │  ├─ mock.py
│     │        │  │  └─ wsgi.py
│     │        │  ├─ _types.py
│     │        │  ├─ _urlparse.py
│     │        │  ├─ _urls.py
│     │        │  ├─ _utils.py
│     │        │  └─ py.typed
│     │        ├─ httpx-0.24.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ licenses
│     │        │     └─ LICENSE.md
│     │        ├─ idna
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ codec.cpython-310.pyc
│     │        │  │  ├─ compat.cpython-310.pyc
│     │        │  │  ├─ core.cpython-310.pyc
│     │        │  │  ├─ idnadata.cpython-310.pyc
│     │        │  │  ├─ intranges.cpython-310.pyc
│     │        │  │  ├─ package_data.cpython-310.pyc
│     │        │  │  └─ uts46data.cpython-310.pyc
│     │        │  ├─ codec.py
│     │        │  ├─ compat.py
│     │        │  ├─ core.py
│     │        │  ├─ idnadata.py
│     │        │  ├─ intranges.py
│     │        │  ├─ package_data.py
│     │        │  ├─ py.typed
│     │        │  └─ uts46data.py
│     │        ├─ idna-3.4.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.md
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ iniconfig
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _parse.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  └─ exceptions.cpython-310.pyc
│     │        │  ├─ _parse.py
│     │        │  ├─ _version.py
│     │        │  ├─ exceptions.py
│     │        │  └─ py.typed
│     │        ├─ iniconfig-2.0.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ licenses
│     │        │     └─ LICENSE
│     │        ├─ isort
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  ├─ api.cpython-310.pyc
│     │        │  │  ├─ comments.cpython-310.pyc
│     │        │  │  ├─ core.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ files.cpython-310.pyc
│     │        │  │  ├─ format.cpython-310.pyc
│     │        │  │  ├─ identify.cpython-310.pyc
│     │        │  │  ├─ io.cpython-310.pyc
│     │        │  │  ├─ literal.cpython-310.pyc
│     │        │  │  ├─ logo.cpython-310.pyc
│     │        │  │  ├─ main.cpython-310.pyc
│     │        │  │  ├─ output.cpython-310.pyc
│     │        │  │  ├─ parse.cpython-310.pyc
│     │        │  │  ├─ place.cpython-310.pyc
│     │        │  │  ├─ profiles.cpython-310.pyc
│     │        │  │  ├─ pylama_isort.cpython-310.pyc
│     │        │  │  ├─ sections.cpython-310.pyc
│     │        │  │  ├─ settings.cpython-310.pyc
│     │        │  │  ├─ setuptools_commands.cpython-310.pyc
│     │        │  │  ├─ sorting.cpython-310.pyc
│     │        │  │  ├─ utils.cpython-310.pyc
│     │        │  │  ├─ wrap.cpython-310.pyc
│     │        │  │  └─ wrap_modes.cpython-310.pyc
│     │        │  ├─ _vendored
│     │        │  │  └─ tomli
│     │        │  │     ├─ LICENSE
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ _parser.cpython-310.pyc
│     │        │  │     │  └─ _re.cpython-310.pyc
│     │        │  │     ├─ _parser.py
│     │        │  │     ├─ _re.py
│     │        │  │     └─ py.typed
│     │        │  ├─ _version.py
│     │        │  ├─ api.py
│     │        │  ├─ comments.py
│     │        │  ├─ core.py
│     │        │  ├─ deprecated
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ finders.cpython-310.pyc
│     │        │  │  └─ finders.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ files.py
│     │        │  ├─ format.py
│     │        │  ├─ identify.py
│     │        │  ├─ io.py
│     │        │  ├─ literal.py
│     │        │  ├─ logo.py
│     │        │  ├─ main.py
│     │        │  ├─ output.py
│     │        │  ├─ parse.py
│     │        │  ├─ place.py
│     │        │  ├─ profiles.py
│     │        │  ├─ py.typed
│     │        │  ├─ pylama_isort.py
│     │        │  ├─ sections.py
│     │        │  ├─ settings.py
│     │        │  ├─ setuptools_commands.py
│     │        │  ├─ sorting.py
│     │        │  ├─ stdlibs
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ all.cpython-310.pyc
│     │        │  │  │  ├─ py2.cpython-310.pyc
│     │        │  │  │  ├─ py27.cpython-310.pyc
│     │        │  │  │  ├─ py3.cpython-310.pyc
│     │        │  │  │  ├─ py310.cpython-310.pyc
│     │        │  │  │  ├─ py311.cpython-310.pyc
│     │        │  │  │  ├─ py36.cpython-310.pyc
│     │        │  │  │  ├─ py37.cpython-310.pyc
│     │        │  │  │  ├─ py38.cpython-310.pyc
│     │        │  │  │  └─ py39.cpython-310.pyc
│     │        │  │  ├─ all.py
│     │        │  │  ├─ py2.py
│     │        │  │  ├─ py27.py
│     │        │  │  ├─ py3.py
│     │        │  │  ├─ py310.py
│     │        │  │  ├─ py311.py
│     │        │  │  ├─ py36.py
│     │        │  │  ├─ py37.py
│     │        │  │  ├─ py38.py
│     │        │  │  └─ py39.py
│     │        │  ├─ utils.py
│     │        │  ├─ wrap.py
│     │        │  └─ wrap_modes.py
│     │        ├─ isort-5.12.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ entry_points.txt
│     │        ├─ jsbeautifier
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  └─ __version__.cpython-310.pyc
│     │        │  ├─ __version__.py
│     │        │  ├─ cli
│     │        │  │  ├─ __init__.py
│     │        │  │  └─ __pycache__
│     │        │  │     └─ __init__.cpython-310.pyc
│     │        │  ├─ core
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ directives.cpython-310.pyc
│     │        │  │  │  ├─ inputscanner.cpython-310.pyc
│     │        │  │  │  ├─ options.cpython-310.pyc
│     │        │  │  │  ├─ output.cpython-310.pyc
│     │        │  │  │  ├─ pattern.cpython-310.pyc
│     │        │  │  │  ├─ templatablepattern.cpython-310.pyc
│     │        │  │  │  ├─ token.cpython-310.pyc
│     │        │  │  │  ├─ tokenizer.cpython-310.pyc
│     │        │  │  │  ├─ tokenstream.cpython-310.pyc
│     │        │  │  │  └─ whitespacepattern.cpython-310.pyc
│     │        │  │  ├─ directives.py
│     │        │  │  ├─ inputscanner.py
│     │        │  │  ├─ options.py
│     │        │  │  ├─ output.py
│     │        │  │  ├─ pattern.py
│     │        │  │  ├─ templatablepattern.py
│     │        │  │  ├─ token.py
│     │        │  │  ├─ tokenizer.py
│     │        │  │  ├─ tokenstream.py
│     │        │  │  └─ whitespacepattern.py
│     │        │  ├─ javascript
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ acorn.cpython-310.pyc
│     │        │  │  │  ├─ beautifier.cpython-310.pyc
│     │        │  │  │  ├─ options.cpython-310.pyc
│     │        │  │  │  └─ tokenizer.cpython-310.pyc
│     │        │  │  ├─ acorn.py
│     │        │  │  ├─ beautifier.py
│     │        │  │  ├─ options.py
│     │        │  │  └─ tokenizer.py
│     │        │  ├─ tests
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ testindentation.cpython-310.pyc
│     │        │  │  ├─ generated
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  └─ tests.cpython-310.pyc
│     │        │  │  │  └─ tests.py
│     │        │  │  └─ testindentation.py
│     │        │  └─ unpackers
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ evalbased.cpython-310.pyc
│     │        │     │  ├─ javascriptobfuscator.cpython-310.pyc
│     │        │     │  ├─ myobfuscate.cpython-310.pyc
│     │        │     │  ├─ packer.cpython-310.pyc
│     │        │     │  └─ urlencode.cpython-310.pyc
│     │        │     ├─ evalbased.py
│     │        │     ├─ javascriptobfuscator.py
│     │        │     ├─ myobfuscate.py
│     │        │     ├─ packer.py
│     │        │     ├─ tests
│     │        │     │  ├─ __init__.py
│     │        │     │  ├─ __pycache__
│     │        │     │  │  ├─ __init__.cpython-310.pyc
│     │        │     │  │  ├─ testjavascriptobfuscator.cpython-310.pyc
│     │        │     │  │  ├─ testmyobfuscate.cpython-310.pyc
│     │        │     │  │  ├─ testpacker.cpython-310.pyc
│     │        │     │  │  └─ testurlencode.cpython-310.pyc
│     │        │     │  ├─ testjavascriptobfuscator.py
│     │        │     │  ├─ testmyobfuscate.py
│     │        │     │  ├─ testpacker.py
│     │        │     │  └─ testurlencode.py
│     │        │     └─ urlencode.py
│     │        ├─ jsbeautifier-1.14.8.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ litestar
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ _multipart.cpython-310.pyc
│     │        │  │  ├─ _parsers.cpython-310.pyc
│     │        │  │  ├─ app.cpython-310.pyc
│     │        │  │  ├─ background_tasks.cpython-310.pyc
│     │        │  │  ├─ constants.cpython-310.pyc
│     │        │  │  ├─ controller.cpython-310.pyc
│     │        │  │  ├─ data_extractors.cpython-310.pyc
│     │        │  │  ├─ di.cpython-310.pyc
│     │        │  │  ├─ enums.cpython-310.pyc
│     │        │  │  ├─ file_system.cpython-310.pyc
│     │        │  │  ├─ pagination.cpython-310.pyc
│     │        │  │  ├─ params.cpython-310.pyc
│     │        │  │  ├─ partial.cpython-310.pyc
│     │        │  │  ├─ plugins.cpython-310.pyc
│     │        │  │  ├─ router.cpython-310.pyc
│     │        │  │  ├─ serialization.cpython-310.pyc
│     │        │  │  ├─ status_codes.cpython-310.pyc
│     │        │  │  └─ typing.cpython-310.pyc
│     │        │  ├─ _asgi
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asgi_router.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  ├─ asgi_router.py
│     │        │  │  ├─ routing_trie
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ mapping.cpython-310.pyc
│     │        │  │  │  │  ├─ traversal.cpython-310.pyc
│     │        │  │  │  │  ├─ types.cpython-310.pyc
│     │        │  │  │  │  └─ validate.cpython-310.pyc
│     │        │  │  │  ├─ mapping.py
│     │        │  │  │  ├─ traversal.py
│     │        │  │  │  ├─ types.py
│     │        │  │  │  └─ validate.py
│     │        │  │  └─ utils.py
│     │        │  ├─ _kwargs
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cleanup.cpython-310.pyc
│     │        │  │  │  ├─ dependencies.cpython-310.pyc
│     │        │  │  │  ├─ extractors.cpython-310.pyc
│     │        │  │  │  ├─ kwargs_model.cpython-310.pyc
│     │        │  │  │  └─ parameter_definition.cpython-310.pyc
│     │        │  │  ├─ cleanup.py
│     │        │  │  ├─ dependencies.py
│     │        │  │  ├─ extractors.py
│     │        │  │  ├─ kwargs_model.py
│     │        │  │  └─ parameter_definition.py
│     │        │  ├─ _layers
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  └─ utils.py
│     │        │  ├─ _multipart.py
│     │        │  ├─ _openapi
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ parameters.cpython-310.pyc
│     │        │  │  │  ├─ path_item.cpython-310.pyc
│     │        │  │  │  ├─ request_body.cpython-310.pyc
│     │        │  │  │  ├─ responses.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  ├─ parameters.py
│     │        │  │  ├─ path_item.py
│     │        │  │  ├─ request_body.py
│     │        │  │  ├─ responses.py
│     │        │  │  ├─ schema_generation
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ constrained_fields.cpython-310.pyc
│     │        │  │  │  │  ├─ examples.cpython-310.pyc
│     │        │  │  │  │  ├─ schema.cpython-310.pyc
│     │        │  │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  │  ├─ constrained_fields.py
│     │        │  │  │  ├─ examples.py
│     │        │  │  │  ├─ schema.py
│     │        │  │  │  └─ utils.py
│     │        │  │  ├─ typescript_converter
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ converter.cpython-310.pyc
│     │        │  │  │  │  ├─ schema_parsing.cpython-310.pyc
│     │        │  │  │  │  └─ types.cpython-310.pyc
│     │        │  │  │  ├─ converter.py
│     │        │  │  │  ├─ schema_parsing.py
│     │        │  │  │  └─ types.py
│     │        │  │  └─ utils.py
│     │        │  ├─ _parsers.py
│     │        │  ├─ _signature
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ field.cpython-310.pyc
│     │        │  │  │  ├─ metadata.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  ├─ field.py
│     │        │  │  ├─ metadata.py
│     │        │  │  ├─ models
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ attrs_signature_model.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  └─ pydantic_signature_model.cpython-310.pyc
│     │        │  │  │  ├─ attrs_signature_model.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  └─ pydantic_signature_model.py
│     │        │  │  └─ utils.py
│     │        │  ├─ app.py
│     │        │  ├─ background_tasks.py
│     │        │  ├─ channels
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ plugin.cpython-310.pyc
│     │        │  │  │  └─ subscriber.cpython-310.pyc
│     │        │  │  ├─ backends
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ memory.cpython-310.pyc
│     │        │  │  │  │  └─ redis.cpython-310.pyc
│     │        │  │  │  ├─ _redis_flushall_streams.lua
│     │        │  │  │  ├─ _redis_pubsub_publish.lua
│     │        │  │  │  ├─ _redis_xadd_expire.lua
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ memory.py
│     │        │  │  │  └─ redis.py
│     │        │  │  ├─ plugin.py
│     │        │  │  └─ subscriber.py
│     │        │  ├─ cli
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  │  └─ main.cpython-310.pyc
│     │        │  │  ├─ _utils.py
│     │        │  │  ├─ commands
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ core.cpython-310.pyc
│     │        │  │  │  │  ├─ schema.cpython-310.pyc
│     │        │  │  │  │  └─ sessions.cpython-310.pyc
│     │        │  │  │  ├─ core.py
│     │        │  │  │  ├─ schema.py
│     │        │  │  │  └─ sessions.py
│     │        │  │  └─ main.py
│     │        │  ├─ config
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ allowed_hosts.cpython-310.pyc
│     │        │  │  │  ├─ app.cpython-310.pyc
│     │        │  │  │  ├─ compression.cpython-310.pyc
│     │        │  │  │  ├─ cors.cpython-310.pyc
│     │        │  │  │  ├─ csrf.cpython-310.pyc
│     │        │  │  │  └─ response_cache.cpython-310.pyc
│     │        │  │  ├─ allowed_hosts.py
│     │        │  │  ├─ app.py
│     │        │  │  ├─ compression.py
│     │        │  │  ├─ cors.py
│     │        │  │  ├─ csrf.py
│     │        │  │  └─ response_cache.py
│     │        │  ├─ connection
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ request.cpython-310.pyc
│     │        │  │  │  └─ websocket.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ request.py
│     │        │  │  └─ websocket.py
│     │        │  ├─ constants.py
│     │        │  ├─ contrib
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ jinja.cpython-310.pyc
│     │        │  │  │  ├─ mako.cpython-310.pyc
│     │        │  │  │  ├─ msgspec.cpython-310.pyc
│     │        │  │  │  └─ pydantic.cpython-310.pyc
│     │        │  │  ├─ htmx
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  │  │  ├─ request.cpython-310.pyc
│     │        │  │  │  │  ├─ response.cpython-310.pyc
│     │        │  │  │  │  └─ types.cpython-310.pyc
│     │        │  │  │  ├─ _utils.py
│     │        │  │  │  ├─ request.py
│     │        │  │  │  ├─ response.py
│     │        │  │  │  └─ types.py
│     │        │  │  ├─ jinja.py
│     │        │  │  ├─ jwt
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ jwt_auth.cpython-310.pyc
│     │        │  │  │  │  ├─ jwt_token.cpython-310.pyc
│     │        │  │  │  │  └─ middleware.cpython-310.pyc
│     │        │  │  │  ├─ jwt_auth.py
│     │        │  │  │  ├─ jwt_token.py
│     │        │  │  │  └─ middleware.py
│     │        │  │  ├─ mako.py
│     │        │  │  ├─ msgspec.py
│     │        │  │  ├─ opentelemetry
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  │  └─ middleware.cpython-310.pyc
│     │        │  │  │  ├─ _utils.py
│     │        │  │  │  ├─ config.py
│     │        │  │  │  └─ middleware.py
│     │        │  │  ├─ prometheus
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  │  ├─ controller.cpython-310.pyc
│     │        │  │  │  │  └─ middleware.cpython-310.pyc
│     │        │  │  │  ├─ config.py
│     │        │  │  │  ├─ controller.py
│     │        │  │  │  └─ middleware.py
│     │        │  │  ├─ pydantic.py
│     │        │  │  ├─ repository
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  │  │  ├─ filters.cpython-310.pyc
│     │        │  │  │  │  └─ handlers.cpython-310.pyc
│     │        │  │  │  ├─ abc
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ _async.cpython-310.pyc
│     │        │  │  │  │  │  └─ _sync.cpython-310.pyc
│     │        │  │  │  │  ├─ _async.py
│     │        │  │  │  │  └─ _sync.py
│     │        │  │  │  ├─ exceptions.py
│     │        │  │  │  ├─ filters.py
│     │        │  │  │  ├─ handlers.py
│     │        │  │  │  └─ testing
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     ├─ __pycache__
│     │        │  │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │  │     │  └─ generic_mock_repository.cpython-310.pyc
│     │        │  │  │     └─ generic_mock_repository.py
│     │        │  │  └─ sqlalchemy
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ base.cpython-310.pyc
│     │        │  │     │  ├─ dto.cpython-310.pyc
│     │        │  │     │  └─ types.cpython-310.pyc
│     │        │  │     ├─ base.py
│     │        │  │     ├─ dto.py
│     │        │  │     ├─ plugins
│     │        │  │     │  ├─ __init__.py
│     │        │  │     │  ├─ __pycache__
│     │        │  │     │  │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  │  ├─ _slots_base.cpython-310.pyc
│     │        │  │     │  │  └─ serialization.cpython-310.pyc
│     │        │  │     │  ├─ _slots_base.py
│     │        │  │     │  ├─ init
│     │        │  │     │  │  ├─ __init__.py
│     │        │  │     │  │  ├─ __pycache__
│     │        │  │     │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  │  │  └─ plugin.cpython-310.pyc
│     │        │  │     │  │  ├─ config
│     │        │  │     │  │  │  ├─ __init__.py
│     │        │  │     │  │  │  ├─ __pycache__
│     │        │  │     │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  │  │  │  ├─ asyncio.cpython-310.pyc
│     │        │  │     │  │  │  │  ├─ common.cpython-310.pyc
│     │        │  │     │  │  │  │  ├─ engine.cpython-310.pyc
│     │        │  │     │  │  │  │  └─ sync.cpython-310.pyc
│     │        │  │     │  │  │  ├─ asyncio.py
│     │        │  │     │  │  │  ├─ common.py
│     │        │  │     │  │  │  ├─ engine.py
│     │        │  │     │  │  │  └─ sync.py
│     │        │  │     │  │  └─ plugin.py
│     │        │  │     │  └─ serialization.py
│     │        │  │     ├─ repository
│     │        │  │     │  ├─ __init__.py
│     │        │  │     │  ├─ __pycache__
│     │        │  │     │  │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  │  ├─ _async.cpython-310.pyc
│     │        │  │     │  │  ├─ _sync.cpython-310.pyc
│     │        │  │     │  │  ├─ _util.cpython-310.pyc
│     │        │  │     │  │  └─ types.cpython-310.pyc
│     │        │  │     │  ├─ _async.py
│     │        │  │     │  ├─ _sync.py
│     │        │  │     │  ├─ _util.py
│     │        │  │     │  └─ types.py
│     │        │  │     └─ types.py
│     │        │  ├─ controller.py
│     │        │  ├─ data_extractors.py
│     │        │  ├─ datastructures
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cookie.cpython-310.pyc
│     │        │  │  │  ├─ headers.cpython-310.pyc
│     │        │  │  │  ├─ multi_dicts.cpython-310.pyc
│     │        │  │  │  ├─ response_header.cpython-310.pyc
│     │        │  │  │  ├─ state.cpython-310.pyc
│     │        │  │  │  ├─ upload_file.cpython-310.pyc
│     │        │  │  │  └─ url.cpython-310.pyc
│     │        │  │  ├─ cookie.py
│     │        │  │  ├─ headers.py
│     │        │  │  ├─ multi_dicts.py
│     │        │  │  ├─ response_header.py
│     │        │  │  ├─ state.py
│     │        │  │  ├─ upload_file.py
│     │        │  │  └─ url.py
│     │        │  ├─ di.py
│     │        │  ├─ dto
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ interface.cpython-310.pyc
│     │        │  │  │  └─ types.cpython-310.pyc
│     │        │  │  ├─ factory
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ abc.cpython-310.pyc
│     │        │  │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  │  ├─ data_structures.cpython-310.pyc
│     │        │  │  │  │  ├─ exc.cpython-310.pyc
│     │        │  │  │  │  ├─ field.cpython-310.pyc
│     │        │  │  │  │  ├─ types.cpython-310.pyc
│     │        │  │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  │  ├─ _backends
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ abc.cpython-310.pyc
│     │        │  │  │  │  │  ├─ types.cpython-310.pyc
│     │        │  │  │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  │  │  ├─ abc.py
│     │        │  │  │  │  ├─ msgspec
│     │        │  │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  │  ├─ backend.cpython-310.pyc
│     │        │  │  │  │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  │  │  │  ├─ backend.py
│     │        │  │  │  │  │  └─ utils.py
│     │        │  │  │  │  ├─ pydantic
│     │        │  │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  │  ├─ backend.cpython-310.pyc
│     │        │  │  │  │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  │  │  │  ├─ backend.py
│     │        │  │  │  │  │  └─ utils.py
│     │        │  │  │  │  ├─ types.py
│     │        │  │  │  │  └─ utils.py
│     │        │  │  │  ├─ abc.py
│     │        │  │  │  ├─ config.py
│     │        │  │  │  ├─ data_structures.py
│     │        │  │  │  ├─ exc.py
│     │        │  │  │  ├─ field.py
│     │        │  │  │  ├─ stdlib
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  └─ dataclass.cpython-310.pyc
│     │        │  │  │  │  └─ dataclass.py
│     │        │  │  │  ├─ types.py
│     │        │  │  │  └─ utils.py
│     │        │  │  ├─ interface.py
│     │        │  │  └─ types.py
│     │        │  ├─ enums.py
│     │        │  ├─ events
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ emitter.cpython-310.pyc
│     │        │  │  │  └─ listener.cpython-310.pyc
│     │        │  │  ├─ emitter.py
│     │        │  │  └─ listener.py
│     │        │  ├─ exceptions
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base_exceptions.cpython-310.pyc
│     │        │  │  │  ├─ http_exceptions.cpython-310.pyc
│     │        │  │  │  └─ websocket_exceptions.cpython-310.pyc
│     │        │  │  ├─ base_exceptions.py
│     │        │  │  ├─ http_exceptions.py
│     │        │  │  └─ websocket_exceptions.py
│     │        │  ├─ file_system.py
│     │        │  ├─ handlers
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asgi_handlers.cpython-310.pyc
│     │        │  │  │  └─ base.cpython-310.pyc
│     │        │  │  ├─ asgi_handlers.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ http_handlers
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  └─ decorators.cpython-310.pyc
│     │        │  │  │  ├─ _utils.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  └─ decorators.py
│     │        │  │  └─ websocket_handlers
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ _utils.cpython-310.pyc
│     │        │  │     │  ├─ listener.cpython-310.pyc
│     │        │  │     │  └─ route_handler.cpython-310.pyc
│     │        │  │     ├─ _utils.py
│     │        │  │     ├─ listener.py
│     │        │  │     └─ route_handler.py
│     │        │  ├─ logging
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  ├─ picologging.cpython-310.pyc
│     │        │  │  │  └─ standard.cpython-310.pyc
│     │        │  │  ├─ _utils.py
│     │        │  │  ├─ config.py
│     │        │  │  ├─ picologging.py
│     │        │  │  └─ standard.py
│     │        │  ├─ middleware
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  │  ├─ allowed_hosts.cpython-310.pyc
│     │        │  │  │  ├─ authentication.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ compression.cpython-310.pyc
│     │        │  │  │  ├─ cors.cpython-310.pyc
│     │        │  │  │  ├─ csrf.cpython-310.pyc
│     │        │  │  │  ├─ logging.cpython-310.pyc
│     │        │  │  │  └─ rate_limit.cpython-310.pyc
│     │        │  │  ├─ _utils.py
│     │        │  │  ├─ allowed_hosts.py
│     │        │  │  ├─ authentication.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ compression.py
│     │        │  │  ├─ cors.py
│     │        │  │  ├─ csrf.py
│     │        │  │  ├─ exceptions
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _debug_response.cpython-310.pyc
│     │        │  │  │  │  └─ middleware.cpython-310.pyc
│     │        │  │  │  ├─ _debug_response.py
│     │        │  │  │  ├─ middleware.py
│     │        │  │  │  └─ templates
│     │        │  │  │     ├─ body.html
│     │        │  │  │     ├─ frame.html
│     │        │  │  │     ├─ scripts.js
│     │        │  │  │     └─ styles.css
│     │        │  │  ├─ logging.py
│     │        │  │  ├─ rate_limit.py
│     │        │  │  └─ session
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ base.cpython-310.pyc
│     │        │  │     │  ├─ client_side.cpython-310.pyc
│     │        │  │     │  └─ server_side.cpython-310.pyc
│     │        │  │     ├─ base.py
│     │        │  │     ├─ client_side.py
│     │        │  │     └─ server_side.py
│     │        │  ├─ openapi
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  ├─ controller.cpython-310.pyc
│     │        │  │  │  └─ datastructures.cpython-310.pyc
│     │        │  │  ├─ config.py
│     │        │  │  ├─ controller.py
│     │        │  │  ├─ datastructures.py
│     │        │  │  └─ spec
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ base.cpython-310.pyc
│     │        │  │     │  ├─ callback.cpython-310.pyc
│     │        │  │     │  ├─ components.cpython-310.pyc
│     │        │  │     │  ├─ contact.cpython-310.pyc
│     │        │  │     │  ├─ discriminator.cpython-310.pyc
│     │        │  │     │  ├─ encoding.cpython-310.pyc
│     │        │  │     │  ├─ enums.cpython-310.pyc
│     │        │  │     │  ├─ example.cpython-310.pyc
│     │        │  │     │  ├─ external_documentation.cpython-310.pyc
│     │        │  │     │  ├─ header.cpython-310.pyc
│     │        │  │     │  ├─ info.cpython-310.pyc
│     │        │  │     │  ├─ license.cpython-310.pyc
│     │        │  │     │  ├─ link.cpython-310.pyc
│     │        │  │     │  ├─ media_type.cpython-310.pyc
│     │        │  │     │  ├─ oauth_flow.cpython-310.pyc
│     │        │  │     │  ├─ oauth_flows.cpython-310.pyc
│     │        │  │     │  ├─ open_api.cpython-310.pyc
│     │        │  │     │  ├─ operation.cpython-310.pyc
│     │        │  │     │  ├─ parameter.cpython-310.pyc
│     │        │  │     │  ├─ path_item.cpython-310.pyc
│     │        │  │     │  ├─ paths.cpython-310.pyc
│     │        │  │     │  ├─ reference.cpython-310.pyc
│     │        │  │     │  ├─ request_body.cpython-310.pyc
│     │        │  │     │  ├─ response.cpython-310.pyc
│     │        │  │     │  ├─ responses.cpython-310.pyc
│     │        │  │     │  ├─ schema.cpython-310.pyc
│     │        │  │     │  ├─ security_requirement.cpython-310.pyc
│     │        │  │     │  ├─ security_scheme.cpython-310.pyc
│     │        │  │     │  ├─ server.cpython-310.pyc
│     │        │  │     │  ├─ server_variable.cpython-310.pyc
│     │        │  │     │  ├─ tag.cpython-310.pyc
│     │        │  │     │  └─ xml.cpython-310.pyc
│     │        │  │     ├─ base.py
│     │        │  │     ├─ callback.py
│     │        │  │     ├─ components.py
│     │        │  │     ├─ contact.py
│     │        │  │     ├─ discriminator.py
│     │        │  │     ├─ encoding.py
│     │        │  │     ├─ enums.py
│     │        │  │     ├─ example.py
│     │        │  │     ├─ external_documentation.py
│     │        │  │     ├─ header.py
│     │        │  │     ├─ info.py
│     │        │  │     ├─ license.py
│     │        │  │     ├─ link.py
│     │        │  │     ├─ media_type.py
│     │        │  │     ├─ oauth_flow.py
│     │        │  │     ├─ oauth_flows.py
│     │        │  │     ├─ open_api.py
│     │        │  │     ├─ operation.py
│     │        │  │     ├─ parameter.py
│     │        │  │     ├─ path_item.py
│     │        │  │     ├─ paths.py
│     │        │  │     ├─ reference.py
│     │        │  │     ├─ request_body.py
│     │        │  │     ├─ response.py
│     │        │  │     ├─ responses.py
│     │        │  │     ├─ schema.py
│     │        │  │     ├─ security_requirement.py
│     │        │  │     ├─ security_scheme.py
│     │        │  │     ├─ server.py
│     │        │  │     ├─ server_variable.py
│     │        │  │     ├─ tag.py
│     │        │  │     └─ xml.py
│     │        │  ├─ pagination.py
│     │        │  ├─ params.py
│     │        │  ├─ partial.py
│     │        │  ├─ plugins.py
│     │        │  ├─ py.typed
│     │        │  ├─ response
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ file.cpython-310.pyc
│     │        │  │  │  ├─ redirect.cpython-310.pyc
│     │        │  │  │  ├─ streaming.cpython-310.pyc
│     │        │  │  │  └─ template.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ file.py
│     │        │  │  ├─ redirect.py
│     │        │  │  ├─ streaming.py
│     │        │  │  └─ template.py
│     │        │  ├─ router.py
│     │        │  ├─ routes
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asgi.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ http.cpython-310.pyc
│     │        │  │  │  └─ websocket.cpython-310.pyc
│     │        │  │  ├─ asgi.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ http.py
│     │        │  │  └─ websocket.py
│     │        │  ├─ security
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ base.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  └─ session_auth
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ auth.cpython-310.pyc
│     │        │  │     │  └─ middleware.cpython-310.pyc
│     │        │  │     ├─ auth.py
│     │        │  │     └─ middleware.py
│     │        │  ├─ serialization.py
│     │        │  ├─ static_files
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  └─ config.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  └─ config.py
│     │        │  ├─ status_codes.py
│     │        │  ├─ stores
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ file.cpython-310.pyc
│     │        │  │  │  ├─ memory.cpython-310.pyc
│     │        │  │  │  ├─ redis.cpython-310.pyc
│     │        │  │  │  └─ registry.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ file.py
│     │        │  │  ├─ memory.py
│     │        │  │  ├─ redis.py
│     │        │  │  └─ registry.py
│     │        │  ├─ template
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  └─ config.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  └─ config.py
│     │        │  ├─ testing
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ helpers.cpython-310.pyc
│     │        │  │  │  ├─ life_span_handler.cpython-310.pyc
│     │        │  │  │  ├─ request_factory.cpython-310.pyc
│     │        │  │  │  ├─ transport.cpython-310.pyc
│     │        │  │  │  └─ websocket_test_session.cpython-310.pyc
│     │        │  │  ├─ client
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ async_client.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  └─ sync_client.cpython-310.pyc
│     │        │  │  │  ├─ async_client.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  └─ sync_client.py
│     │        │  │  ├─ helpers.py
│     │        │  │  ├─ life_span_handler.py
│     │        │  │  ├─ request_factory.py
│     │        │  │  ├─ transport.py
│     │        │  │  └─ websocket_test_session.py
│     │        │  ├─ types
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asgi_types.cpython-310.pyc
│     │        │  │  │  ├─ builtin_types.cpython-310.pyc
│     │        │  │  │  ├─ callable_types.cpython-310.pyc
│     │        │  │  │  ├─ composite_types.cpython-310.pyc
│     │        │  │  │  ├─ empty.cpython-310.pyc
│     │        │  │  │  ├─ file_types.cpython-310.pyc
│     │        │  │  │  ├─ helper_types.cpython-310.pyc
│     │        │  │  │  ├─ internal_types.cpython-310.pyc
│     │        │  │  │  ├─ protocols.cpython-310.pyc
│     │        │  │  │  └─ serialization.cpython-310.pyc
│     │        │  │  ├─ asgi_types.py
│     │        │  │  ├─ builtin_types.py
│     │        │  │  ├─ callable_types.py
│     │        │  │  ├─ composite_types.py
│     │        │  │  ├─ empty.py
│     │        │  │  ├─ file_types.py
│     │        │  │  ├─ helper_types.py
│     │        │  │  ├─ internal_types.py
│     │        │  │  ├─ protocols.py
│     │        │  │  └─ serialization.py
│     │        │  ├─ typing.py
│     │        │  └─ utils
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ compat.cpython-310.pyc
│     │        │     │  ├─ dataclass.cpython-310.pyc
│     │        │     │  ├─ deprecation.cpython-310.pyc
│     │        │     │  ├─ helpers.cpython-310.pyc
│     │        │     │  ├─ path.cpython-310.pyc
│     │        │     │  ├─ predicates.cpython-310.pyc
│     │        │     │  ├─ scope.cpython-310.pyc
│     │        │     │  ├─ sequence.cpython-310.pyc
│     │        │     │  ├─ signature.cpython-310.pyc
│     │        │     │  ├─ sync.cpython-310.pyc
│     │        │     │  ├─ typing.cpython-310.pyc
│     │        │     │  ├─ version.cpython-310.pyc
│     │        │     │  └─ warnings.cpython-310.pyc
│     │        │     ├─ compat.py
│     │        │     ├─ dataclass.py
│     │        │     ├─ deprecation.py
│     │        │     ├─ helpers.py
│     │        │     ├─ path.py
│     │        │     ├─ predicates.py
│     │        │     ├─ scope.py
│     │        │     ├─ sequence.py
│     │        │     ├─ signature.py
│     │        │     ├─ sync.py
│     │        │     ├─ typing.py
│     │        │     ├─ version.py
│     │        │     └─ warnings.py
│     │        ├─ litestar-2.0.0b2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ entry_points.txt
│     │        ├─ mako
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _ast_util.cpython-310.pyc
│     │        │  │  ├─ ast.cpython-310.pyc
│     │        │  │  ├─ cache.cpython-310.pyc
│     │        │  │  ├─ cmd.cpython-310.pyc
│     │        │  │  ├─ codegen.cpython-310.pyc
│     │        │  │  ├─ compat.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ filters.cpython-310.pyc
│     │        │  │  ├─ lexer.cpython-310.pyc
│     │        │  │  ├─ lookup.cpython-310.pyc
│     │        │  │  ├─ parsetree.cpython-310.pyc
│     │        │  │  ├─ pygen.cpython-310.pyc
│     │        │  │  ├─ pyparser.cpython-310.pyc
│     │        │  │  ├─ runtime.cpython-310.pyc
│     │        │  │  ├─ template.cpython-310.pyc
│     │        │  │  └─ util.cpython-310.pyc
│     │        │  ├─ _ast_util.py
│     │        │  ├─ ast.py
│     │        │  ├─ cache.py
│     │        │  ├─ cmd.py
│     │        │  ├─ codegen.py
│     │        │  ├─ compat.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ ext
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ autohandler.cpython-310.pyc
│     │        │  │  │  ├─ babelplugin.cpython-310.pyc
│     │        │  │  │  ├─ beaker_cache.cpython-310.pyc
│     │        │  │  │  ├─ extract.cpython-310.pyc
│     │        │  │  │  ├─ linguaplugin.cpython-310.pyc
│     │        │  │  │  ├─ preprocessors.cpython-310.pyc
│     │        │  │  │  ├─ pygmentplugin.cpython-310.pyc
│     │        │  │  │  └─ turbogears.cpython-310.pyc
│     │        │  │  ├─ autohandler.py
│     │        │  │  ├─ babelplugin.py
│     │        │  │  ├─ beaker_cache.py
│     │        │  │  ├─ extract.py
│     │        │  │  ├─ linguaplugin.py
│     │        │  │  ├─ preprocessors.py
│     │        │  │  ├─ pygmentplugin.py
│     │        │  │  └─ turbogears.py
│     │        │  ├─ filters.py
│     │        │  ├─ lexer.py
│     │        │  ├─ lookup.py
│     │        │  ├─ parsetree.py
│     │        │  ├─ pygen.py
│     │        │  ├─ pyparser.py
│     │        │  ├─ runtime.py
│     │        │  ├─ template.py
│     │        │  ├─ testing
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _config.cpython-310.pyc
│     │        │  │  │  ├─ assertions.cpython-310.pyc
│     │        │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  ├─ exclusions.cpython-310.pyc
│     │        │  │  │  ├─ fixtures.cpython-310.pyc
│     │        │  │  │  └─ helpers.cpython-310.pyc
│     │        │  │  ├─ _config.py
│     │        │  │  ├─ assertions.py
│     │        │  │  ├─ config.py
│     │        │  │  ├─ exclusions.py
│     │        │  │  ├─ fixtures.py
│     │        │  │  └─ helpers.py
│     │        │  └─ util.py
│     │        ├─ markdown_it
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _compat.cpython-310.pyc
│     │        │  │  ├─ _punycode.cpython-310.pyc
│     │        │  │  ├─ main.cpython-310.pyc
│     │        │  │  ├─ parser_block.cpython-310.pyc
│     │        │  │  ├─ parser_core.cpython-310.pyc
│     │        │  │  ├─ parser_inline.cpython-310.pyc
│     │        │  │  ├─ renderer.cpython-310.pyc
│     │        │  │  ├─ ruler.cpython-310.pyc
│     │        │  │  ├─ token.cpython-310.pyc
│     │        │  │  ├─ tree.cpython-310.pyc
│     │        │  │  └─ utils.cpython-310.pyc
│     │        │  ├─ _compat.py
│     │        │  ├─ _punycode.py
│     │        │  ├─ cli
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ parse.cpython-310.pyc
│     │        │  │  └─ parse.py
│     │        │  ├─ common
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ entities.cpython-310.pyc
│     │        │  │  │  ├─ html_blocks.cpython-310.pyc
│     │        │  │  │  ├─ html_re.cpython-310.pyc
│     │        │  │  │  ├─ normalize_url.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  ├─ entities.py
│     │        │  │  ├─ html_blocks.py
│     │        │  │  ├─ html_re.py
│     │        │  │  ├─ normalize_url.py
│     │        │  │  └─ utils.py
│     │        │  ├─ helpers
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ parse_link_destination.cpython-310.pyc
│     │        │  │  │  ├─ parse_link_label.cpython-310.pyc
│     │        │  │  │  └─ parse_link_title.cpython-310.pyc
│     │        │  │  ├─ parse_link_destination.py
│     │        │  │  ├─ parse_link_label.py
│     │        │  │  └─ parse_link_title.py
│     │        │  ├─ main.py
│     │        │  ├─ parser_block.py
│     │        │  ├─ parser_core.py
│     │        │  ├─ parser_inline.py
│     │        │  ├─ port.yaml
│     │        │  ├─ presets
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ commonmark.cpython-310.pyc
│     │        │  │  │  ├─ default.cpython-310.pyc
│     │        │  │  │  └─ zero.cpython-310.pyc
│     │        │  │  ├─ commonmark.py
│     │        │  │  ├─ default.py
│     │        │  │  └─ zero.py
│     │        │  ├─ py.typed
│     │        │  ├─ renderer.py
│     │        │  ├─ ruler.py
│     │        │  ├─ rules_block
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ blockquote.cpython-310.pyc
│     │        │  │  │  ├─ code.cpython-310.pyc
│     │        │  │  │  ├─ fence.cpython-310.pyc
│     │        │  │  │  ├─ heading.cpython-310.pyc
│     │        │  │  │  ├─ hr.cpython-310.pyc
│     │        │  │  │  ├─ html_block.cpython-310.pyc
│     │        │  │  │  ├─ lheading.cpython-310.pyc
│     │        │  │  │  ├─ list.cpython-310.pyc
│     │        │  │  │  ├─ paragraph.cpython-310.pyc
│     │        │  │  │  ├─ reference.cpython-310.pyc
│     │        │  │  │  ├─ state_block.cpython-310.pyc
│     │        │  │  │  └─ table.cpython-310.pyc
│     │        │  │  ├─ blockquote.py
│     │        │  │  ├─ code.py
│     │        │  │  ├─ fence.py
│     │        │  │  ├─ heading.py
│     │        │  │  ├─ hr.py
│     │        │  │  ├─ html_block.py
│     │        │  │  ├─ lheading.py
│     │        │  │  ├─ list.py
│     │        │  │  ├─ paragraph.py
│     │        │  │  ├─ reference.py
│     │        │  │  ├─ state_block.py
│     │        │  │  └─ table.py
│     │        │  ├─ rules_core
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ block.cpython-310.pyc
│     │        │  │  │  ├─ inline.cpython-310.pyc
│     │        │  │  │  ├─ linkify.cpython-310.pyc
│     │        │  │  │  ├─ normalize.cpython-310.pyc
│     │        │  │  │  ├─ replacements.cpython-310.pyc
│     │        │  │  │  ├─ smartquotes.cpython-310.pyc
│     │        │  │  │  ├─ state_core.cpython-310.pyc
│     │        │  │  │  └─ text_join.cpython-310.pyc
│     │        │  │  ├─ block.py
│     │        │  │  ├─ inline.py
│     │        │  │  ├─ linkify.py
│     │        │  │  ├─ normalize.py
│     │        │  │  ├─ replacements.py
│     │        │  │  ├─ smartquotes.py
│     │        │  │  ├─ state_core.py
│     │        │  │  └─ text_join.py
│     │        │  ├─ rules_inline
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ autolink.cpython-310.pyc
│     │        │  │  │  ├─ backticks.cpython-310.pyc
│     │        │  │  │  ├─ balance_pairs.cpython-310.pyc
│     │        │  │  │  ├─ emphasis.cpython-310.pyc
│     │        │  │  │  ├─ entity.cpython-310.pyc
│     │        │  │  │  ├─ escape.cpython-310.pyc
│     │        │  │  │  ├─ fragments_join.cpython-310.pyc
│     │        │  │  │  ├─ html_inline.cpython-310.pyc
│     │        │  │  │  ├─ image.cpython-310.pyc
│     │        │  │  │  ├─ link.cpython-310.pyc
│     │        │  │  │  ├─ linkify.cpython-310.pyc
│     │        │  │  │  ├─ newline.cpython-310.pyc
│     │        │  │  │  ├─ state_inline.cpython-310.pyc
│     │        │  │  │  ├─ strikethrough.cpython-310.pyc
│     │        │  │  │  └─ text.cpython-310.pyc
│     │        │  │  ├─ autolink.py
│     │        │  │  ├─ backticks.py
│     │        │  │  ├─ balance_pairs.py
│     │        │  │  ├─ emphasis.py
│     │        │  │  ├─ entity.py
│     │        │  │  ├─ escape.py
│     │        │  │  ├─ fragments_join.py
│     │        │  │  ├─ html_inline.py
│     │        │  │  ├─ image.py
│     │        │  │  ├─ link.py
│     │        │  │  ├─ linkify.py
│     │        │  │  ├─ newline.py
│     │        │  │  ├─ state_inline.py
│     │        │  │  ├─ strikethrough.py
│     │        │  │  └─ text.py
│     │        │  ├─ token.py
│     │        │  ├─ tree.py
│     │        │  └─ utils.py
│     │        ├─ markdown_it_py-3.0.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ LICENSE.markdown-it
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ entry_points.txt
│     │        ├─ markupsafe
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  └─ _native.cpython-310.pyc
│     │        │  ├─ _native.py
│     │        │  ├─ _speedups.c
│     │        │  ├─ _speedups.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ _speedups.pyi
│     │        │  └─ py.typed
│     │        ├─ mdurl
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _decode.cpython-310.pyc
│     │        │  │  ├─ _encode.cpython-310.pyc
│     │        │  │  ├─ _format.cpython-310.pyc
│     │        │  │  ├─ _parse.cpython-310.pyc
│     │        │  │  └─ _url.cpython-310.pyc
│     │        │  ├─ _decode.py
│     │        │  ├─ _encode.py
│     │        │  ├─ _format.py
│     │        │  ├─ _parse.py
│     │        │  ├─ _url.py
│     │        │  └─ py.typed
│     │        ├─ mdurl-0.1.2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ msgspec
│     │        │  ├─ __init__.py
│     │        │  ├─ __init__.pyi
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _json_schema.cpython-310.pyc
│     │        │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  ├─ inspect.cpython-310.pyc
│     │        │  │  ├─ json.cpython-310.pyc
│     │        │  │  ├─ msgpack.cpython-310.pyc
│     │        │  │  ├─ structs.cpython-310.pyc
│     │        │  │  ├─ toml.cpython-310.pyc
│     │        │  │  └─ yaml.cpython-310.pyc
│     │        │  ├─ _core.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ _json_schema.py
│     │        │  ├─ _utils.py
│     │        │  ├─ _version.py
│     │        │  ├─ inspect.py
│     │        │  ├─ json.py
│     │        │  ├─ json.pyi
│     │        │  ├─ msgpack.py
│     │        │  ├─ msgpack.pyi
│     │        │  ├─ py.typed
│     │        │  ├─ structs.py
│     │        │  ├─ structs.pyi
│     │        │  ├─ toml.py
│     │        │  └─ yaml.py
│     │        ├─ msgspec-0.16.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ multidict
│     │        │  ├─ __init__.py
│     │        │  ├─ __init__.pyi
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _abc.cpython-310.pyc
│     │        │  │  ├─ _compat.cpython-310.pyc
│     │        │  │  ├─ _multidict_base.cpython-310.pyc
│     │        │  │  └─ _multidict_py.cpython-310.pyc
│     │        │  ├─ _abc.py
│     │        │  ├─ _compat.py
│     │        │  ├─ _multidict.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ _multidict_base.py
│     │        │  ├─ _multidict_py.py
│     │        │  └─ py.typed
│     │        ├─ multidict-6.0.4.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ mypy_extensions-1.0.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ mypy_extensions.py
│     │        ├─ packaging
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _elffile.cpython-310.pyc
│     │        │  │  ├─ _manylinux.cpython-310.pyc
│     │        │  │  ├─ _musllinux.cpython-310.pyc
│     │        │  │  ├─ _parser.cpython-310.pyc
│     │        │  │  ├─ _structures.cpython-310.pyc
│     │        │  │  ├─ _tokenizer.cpython-310.pyc
│     │        │  │  ├─ markers.cpython-310.pyc
│     │        │  │  ├─ metadata.cpython-310.pyc
│     │        │  │  ├─ requirements.cpython-310.pyc
│     │        │  │  ├─ specifiers.cpython-310.pyc
│     │        │  │  ├─ tags.cpython-310.pyc
│     │        │  │  ├─ utils.cpython-310.pyc
│     │        │  │  └─ version.cpython-310.pyc
│     │        │  ├─ _elffile.py
│     │        │  ├─ _manylinux.py
│     │        │  ├─ _musllinux.py
│     │        │  ├─ _parser.py
│     │        │  ├─ _structures.py
│     │        │  ├─ _tokenizer.py
│     │        │  ├─ markers.py
│     │        │  ├─ metadata.py
│     │        │  ├─ py.typed
│     │        │  ├─ requirements.py
│     │        │  ├─ specifiers.py
│     │        │  ├─ tags.py
│     │        │  ├─ utils.py
│     │        │  └─ version.py
│     │        ├─ packaging-23.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ LICENSE.APACHE
│     │        │  ├─ LICENSE.BSD
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ passlib
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ apache.cpython-310.pyc
│     │        │  │  ├─ apps.cpython-310.pyc
│     │        │  │  ├─ context.cpython-310.pyc
│     │        │  │  ├─ exc.cpython-310.pyc
│     │        │  │  ├─ hash.cpython-310.pyc
│     │        │  │  ├─ hosts.cpython-310.pyc
│     │        │  │  ├─ ifc.cpython-310.pyc
│     │        │  │  ├─ pwd.cpython-310.pyc
│     │        │  │  ├─ registry.cpython-310.pyc
│     │        │  │  ├─ totp.cpython-310.pyc
│     │        │  │  └─ win32.cpython-310.pyc
│     │        │  ├─ _data
│     │        │  │  └─ wordsets
│     │        │  │     ├─ bip39.txt
│     │        │  │     ├─ eff_long.txt
│     │        │  │     ├─ eff_prefixed.txt
│     │        │  │     └─ eff_short.txt
│     │        │  ├─ apache.py
│     │        │  ├─ apps.py
│     │        │  ├─ context.py
│     │        │  ├─ crypto
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _md4.cpython-310.pyc
│     │        │  │  │  ├─ des.cpython-310.pyc
│     │        │  │  │  └─ digest.cpython-310.pyc
│     │        │  │  ├─ _blowfish
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _gen_files.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  └─ unrolled.cpython-310.pyc
│     │        │  │  │  ├─ _gen_files.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  └─ unrolled.py
│     │        │  │  ├─ _md4.py
│     │        │  │  ├─ des.py
│     │        │  │  ├─ digest.py
│     │        │  │  └─ scrypt
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ _builtin.cpython-310.pyc
│     │        │  │     │  ├─ _gen_files.cpython-310.pyc
│     │        │  │     │  └─ _salsa.cpython-310.pyc
│     │        │  │     ├─ _builtin.py
│     │        │  │     ├─ _gen_files.py
│     │        │  │     └─ _salsa.py
│     │        │  ├─ exc.py
│     │        │  ├─ ext
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  └─ django
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ models.cpython-310.pyc
│     │        │  │     │  └─ utils.cpython-310.pyc
│     │        │  │     ├─ models.py
│     │        │  │     └─ utils.py
│     │        │  ├─ handlers
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ argon2.cpython-310.pyc
│     │        │  │  │  ├─ bcrypt.cpython-310.pyc
│     │        │  │  │  ├─ cisco.cpython-310.pyc
│     │        │  │  │  ├─ des_crypt.cpython-310.pyc
│     │        │  │  │  ├─ digests.cpython-310.pyc
│     │        │  │  │  ├─ django.cpython-310.pyc
│     │        │  │  │  ├─ fshp.cpython-310.pyc
│     │        │  │  │  ├─ ldap_digests.cpython-310.pyc
│     │        │  │  │  ├─ md5_crypt.cpython-310.pyc
│     │        │  │  │  ├─ misc.cpython-310.pyc
│     │        │  │  │  ├─ mssql.cpython-310.pyc
│     │        │  │  │  ├─ mysql.cpython-310.pyc
│     │        │  │  │  ├─ oracle.cpython-310.pyc
│     │        │  │  │  ├─ pbkdf2.cpython-310.pyc
│     │        │  │  │  ├─ phpass.cpython-310.pyc
│     │        │  │  │  ├─ postgres.cpython-310.pyc
│     │        │  │  │  ├─ roundup.cpython-310.pyc
│     │        │  │  │  ├─ scram.cpython-310.pyc
│     │        │  │  │  ├─ scrypt.cpython-310.pyc
│     │        │  │  │  ├─ sha1_crypt.cpython-310.pyc
│     │        │  │  │  ├─ sha2_crypt.cpython-310.pyc
│     │        │  │  │  ├─ sun_md5_crypt.cpython-310.pyc
│     │        │  │  │  └─ windows.cpython-310.pyc
│     │        │  │  ├─ argon2.py
│     │        │  │  ├─ bcrypt.py
│     │        │  │  ├─ cisco.py
│     │        │  │  ├─ des_crypt.py
│     │        │  │  ├─ digests.py
│     │        │  │  ├─ django.py
│     │        │  │  ├─ fshp.py
│     │        │  │  ├─ ldap_digests.py
│     │        │  │  ├─ md5_crypt.py
│     │        │  │  ├─ misc.py
│     │        │  │  ├─ mssql.py
│     │        │  │  ├─ mysql.py
│     │        │  │  ├─ oracle.py
│     │        │  │  ├─ pbkdf2.py
│     │        │  │  ├─ phpass.py
│     │        │  │  ├─ postgres.py
│     │        │  │  ├─ roundup.py
│     │        │  │  ├─ scram.py
│     │        │  │  ├─ scrypt.py
│     │        │  │  ├─ sha1_crypt.py
│     │        │  │  ├─ sha2_crypt.py
│     │        │  │  ├─ sun_md5_crypt.py
│     │        │  │  └─ windows.py
│     │        │  ├─ hash.py
│     │        │  ├─ hosts.py
│     │        │  ├─ ifc.py
│     │        │  ├─ pwd.py
│     │        │  ├─ registry.py
│     │        │  ├─ tests
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __main__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  │  ├─ _test_bad_register.cpython-310.pyc
│     │        │  │  │  ├─ backports.cpython-310.pyc
│     │        │  │  │  ├─ test_apache.cpython-310.pyc
│     │        │  │  │  ├─ test_apps.cpython-310.pyc
│     │        │  │  │  ├─ test_context.cpython-310.pyc
│     │        │  │  │  ├─ test_context_deprecated.cpython-310.pyc
│     │        │  │  │  ├─ test_crypto_builtin_md4.cpython-310.pyc
│     │        │  │  │  ├─ test_crypto_des.cpython-310.pyc
│     │        │  │  │  ├─ test_crypto_digest.cpython-310.pyc
│     │        │  │  │  ├─ test_crypto_scrypt.cpython-310.pyc
│     │        │  │  │  ├─ test_ext_django.cpython-310.pyc
│     │        │  │  │  ├─ test_ext_django_source.cpython-310.pyc
│     │        │  │  │  ├─ test_handlers.cpython-310.pyc
│     │        │  │  │  ├─ test_handlers_argon2.cpython-310.pyc
│     │        │  │  │  ├─ test_handlers_bcrypt.cpython-310.pyc
│     │        │  │  │  ├─ test_handlers_cisco.cpython-310.pyc
│     │        │  │  │  ├─ test_handlers_django.cpython-310.pyc
│     │        │  │  │  ├─ test_handlers_pbkdf2.cpython-310.pyc
│     │        │  │  │  ├─ test_handlers_scrypt.cpython-310.pyc
│     │        │  │  │  ├─ test_hosts.cpython-310.pyc
│     │        │  │  │  ├─ test_pwd.cpython-310.pyc
│     │        │  │  │  ├─ test_registry.cpython-310.pyc
│     │        │  │  │  ├─ test_totp.cpython-310.pyc
│     │        │  │  │  ├─ test_utils.cpython-310.pyc
│     │        │  │  │  ├─ test_utils_handlers.cpython-310.pyc
│     │        │  │  │  ├─ test_utils_md4.cpython-310.pyc
│     │        │  │  │  ├─ test_utils_pbkdf2.cpython-310.pyc
│     │        │  │  │  ├─ test_win32.cpython-310.pyc
│     │        │  │  │  ├─ tox_support.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  ├─ _test_bad_register.py
│     │        │  │  ├─ backports.py
│     │        │  │  ├─ sample1.cfg
│     │        │  │  ├─ sample1b.cfg
│     │        │  │  ├─ sample1c.cfg
│     │        │  │  ├─ sample_config_1s.cfg
│     │        │  │  ├─ test_apache.py
│     │        │  │  ├─ test_apps.py
│     │        │  │  ├─ test_context.py
│     │        │  │  ├─ test_context_deprecated.py
│     │        │  │  ├─ test_crypto_builtin_md4.py
│     │        │  │  ├─ test_crypto_des.py
│     │        │  │  ├─ test_crypto_digest.py
│     │        │  │  ├─ test_crypto_scrypt.py
│     │        │  │  ├─ test_ext_django.py
│     │        │  │  ├─ test_ext_django_source.py
│     │        │  │  ├─ test_handlers.py
│     │        │  │  ├─ test_handlers_argon2.py
│     │        │  │  ├─ test_handlers_bcrypt.py
│     │        │  │  ├─ test_handlers_cisco.py
│     │        │  │  ├─ test_handlers_django.py
│     │        │  │  ├─ test_handlers_pbkdf2.py
│     │        │  │  ├─ test_handlers_scrypt.py
│     │        │  │  ├─ test_hosts.py
│     │        │  │  ├─ test_pwd.py
│     │        │  │  ├─ test_registry.py
│     │        │  │  ├─ test_totp.py
│     │        │  │  ├─ test_utils.py
│     │        │  │  ├─ test_utils_handlers.py
│     │        │  │  ├─ test_utils_md4.py
│     │        │  │  ├─ test_utils_pbkdf2.py
│     │        │  │  ├─ test_win32.py
│     │        │  │  ├─ tox_support.py
│     │        │  │  └─ utils.py
│     │        │  ├─ totp.py
│     │        │  ├─ utils
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ binary.cpython-310.pyc
│     │        │  │  │  ├─ decor.cpython-310.pyc
│     │        │  │  │  ├─ des.cpython-310.pyc
│     │        │  │  │  ├─ handlers.cpython-310.pyc
│     │        │  │  │  ├─ md4.cpython-310.pyc
│     │        │  │  │  └─ pbkdf2.cpython-310.pyc
│     │        │  │  ├─ binary.py
│     │        │  │  ├─ compat
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  └─ _ordered_dict.cpython-310.pyc
│     │        │  │  │  └─ _ordered_dict.py
│     │        │  │  ├─ decor.py
│     │        │  │  ├─ des.py
│     │        │  │  ├─ handlers.py
│     │        │  │  ├─ md4.py
│     │        │  │  └─ pbkdf2.py
│     │        │  └─ win32.py
│     │        ├─ passlib-1.7.4.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ top_level.txt
│     │        │  └─ zip-safe
│     │        ├─ pathspec
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _meta.cpython-310.pyc
│     │        │  │  ├─ gitignore.cpython-310.pyc
│     │        │  │  ├─ pathspec.cpython-310.pyc
│     │        │  │  ├─ pattern.cpython-310.pyc
│     │        │  │  └─ util.cpython-310.pyc
│     │        │  ├─ _meta.py
│     │        │  ├─ gitignore.py
│     │        │  ├─ pathspec.py
│     │        │  ├─ pattern.py
│     │        │  ├─ patterns
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ gitwildmatch.cpython-310.pyc
│     │        │  │  └─ gitwildmatch.py
│     │        │  ├─ py.typed
│     │        │  └─ util.py
│     │        ├─ pathspec-0.11.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ pip
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pip-runner__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  └─ __pip-runner__.cpython-310.pyc
│     │        │  ├─ _internal
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ build_env.cpython-310.pyc
│     │        │  │  │  ├─ cache.cpython-310.pyc
│     │        │  │  │  ├─ configuration.cpython-310.pyc
│     │        │  │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  │  ├─ main.cpython-310.pyc
│     │        │  │  │  ├─ pyproject.cpython-310.pyc
│     │        │  │  │  ├─ self_outdated_check.cpython-310.pyc
│     │        │  │  │  └─ wheel_builder.cpython-310.pyc
│     │        │  │  ├─ build_env.py
│     │        │  │  ├─ cache.py
│     │        │  │  ├─ cli
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ autocompletion.cpython-310.pyc
│     │        │  │  │  │  ├─ base_command.cpython-310.pyc
│     │        │  │  │  │  ├─ cmdoptions.cpython-310.pyc
│     │        │  │  │  │  ├─ command_context.cpython-310.pyc
│     │        │  │  │  │  ├─ main.cpython-310.pyc
│     │        │  │  │  │  ├─ main_parser.cpython-310.pyc
│     │        │  │  │  │  ├─ parser.cpython-310.pyc
│     │        │  │  │  │  ├─ progress_bars.cpython-310.pyc
│     │        │  │  │  │  ├─ req_command.cpython-310.pyc
│     │        │  │  │  │  ├─ spinners.cpython-310.pyc
│     │        │  │  │  │  └─ status_codes.cpython-310.pyc
│     │        │  │  │  ├─ autocompletion.py
│     │        │  │  │  ├─ base_command.py
│     │        │  │  │  ├─ cmdoptions.py
│     │        │  │  │  ├─ command_context.py
│     │        │  │  │  ├─ main.py
│     │        │  │  │  ├─ main_parser.py
│     │        │  │  │  ├─ parser.py
│     │        │  │  │  ├─ progress_bars.py
│     │        │  │  │  ├─ req_command.py
│     │        │  │  │  ├─ spinners.py
│     │        │  │  │  └─ status_codes.py
│     │        │  │  ├─ commands
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ cache.cpython-310.pyc
│     │        │  │  │  │  ├─ check.cpython-310.pyc
│     │        │  │  │  │  ├─ completion.cpython-310.pyc
│     │        │  │  │  │  ├─ configuration.cpython-310.pyc
│     │        │  │  │  │  ├─ debug.cpython-310.pyc
│     │        │  │  │  │  ├─ download.cpython-310.pyc
│     │        │  │  │  │  ├─ freeze.cpython-310.pyc
│     │        │  │  │  │  ├─ hash.cpython-310.pyc
│     │        │  │  │  │  ├─ help.cpython-310.pyc
│     │        │  │  │  │  ├─ index.cpython-310.pyc
│     │        │  │  │  │  ├─ inspect.cpython-310.pyc
│     │        │  │  │  │  ├─ install.cpython-310.pyc
│     │        │  │  │  │  ├─ list.cpython-310.pyc
│     │        │  │  │  │  ├─ search.cpython-310.pyc
│     │        │  │  │  │  ├─ show.cpython-310.pyc
│     │        │  │  │  │  ├─ uninstall.cpython-310.pyc
│     │        │  │  │  │  └─ wheel.cpython-310.pyc
│     │        │  │  │  ├─ cache.py
│     │        │  │  │  ├─ check.py
│     │        │  │  │  ├─ completion.py
│     │        │  │  │  ├─ configuration.py
│     │        │  │  │  ├─ debug.py
│     │        │  │  │  ├─ download.py
│     │        │  │  │  ├─ freeze.py
│     │        │  │  │  ├─ hash.py
│     │        │  │  │  ├─ help.py
│     │        │  │  │  ├─ index.py
│     │        │  │  │  ├─ inspect.py
│     │        │  │  │  ├─ install.py
│     │        │  │  │  ├─ list.py
│     │        │  │  │  ├─ search.py
│     │        │  │  │  ├─ show.py
│     │        │  │  │  ├─ uninstall.py
│     │        │  │  │  └─ wheel.py
│     │        │  │  ├─ configuration.py
│     │        │  │  ├─ distributions
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ installed.cpython-310.pyc
│     │        │  │  │  │  ├─ sdist.cpython-310.pyc
│     │        │  │  │  │  └─ wheel.cpython-310.pyc
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ installed.py
│     │        │  │  │  ├─ sdist.py
│     │        │  │  │  └─ wheel.py
│     │        │  │  ├─ exceptions.py
│     │        │  │  ├─ index
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ collector.cpython-310.pyc
│     │        │  │  │  │  ├─ package_finder.cpython-310.pyc
│     │        │  │  │  │  └─ sources.cpython-310.pyc
│     │        │  │  │  ├─ collector.py
│     │        │  │  │  ├─ package_finder.py
│     │        │  │  │  └─ sources.py
│     │        │  │  ├─ locations
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _distutils.cpython-310.pyc
│     │        │  │  │  │  ├─ _sysconfig.cpython-310.pyc
│     │        │  │  │  │  └─ base.cpython-310.pyc
│     │        │  │  │  ├─ _distutils.py
│     │        │  │  │  ├─ _sysconfig.py
│     │        │  │  │  └─ base.py
│     │        │  │  ├─ main.py
│     │        │  │  ├─ metadata
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _json.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  └─ pkg_resources.cpython-310.pyc
│     │        │  │  │  ├─ _json.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ importlib
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ _compat.cpython-310.pyc
│     │        │  │  │  │  │  ├─ _dists.cpython-310.pyc
│     │        │  │  │  │  │  └─ _envs.cpython-310.pyc
│     │        │  │  │  │  ├─ _compat.py
│     │        │  │  │  │  ├─ _dists.py
│     │        │  │  │  │  └─ _envs.py
│     │        │  │  │  └─ pkg_resources.py
│     │        │  │  ├─ models
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ candidate.cpython-310.pyc
│     │        │  │  │  │  ├─ direct_url.cpython-310.pyc
│     │        │  │  │  │  ├─ format_control.cpython-310.pyc
│     │        │  │  │  │  ├─ index.cpython-310.pyc
│     │        │  │  │  │  ├─ installation_report.cpython-310.pyc
│     │        │  │  │  │  ├─ link.cpython-310.pyc
│     │        │  │  │  │  ├─ scheme.cpython-310.pyc
│     │        │  │  │  │  ├─ search_scope.cpython-310.pyc
│     │        │  │  │  │  ├─ selection_prefs.cpython-310.pyc
│     │        │  │  │  │  ├─ target_python.cpython-310.pyc
│     │        │  │  │  │  └─ wheel.cpython-310.pyc
│     │        │  │  │  ├─ candidate.py
│     │        │  │  │  ├─ direct_url.py
│     │        │  │  │  ├─ format_control.py
│     │        │  │  │  ├─ index.py
│     │        │  │  │  ├─ installation_report.py
│     │        │  │  │  ├─ link.py
│     │        │  │  │  ├─ scheme.py
│     │        │  │  │  ├─ search_scope.py
│     │        │  │  │  ├─ selection_prefs.py
│     │        │  │  │  ├─ target_python.py
│     │        │  │  │  └─ wheel.py
│     │        │  │  ├─ network
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ auth.cpython-310.pyc
│     │        │  │  │  │  ├─ cache.cpython-310.pyc
│     │        │  │  │  │  ├─ download.cpython-310.pyc
│     │        │  │  │  │  ├─ lazy_wheel.cpython-310.pyc
│     │        │  │  │  │  ├─ session.cpython-310.pyc
│     │        │  │  │  │  ├─ utils.cpython-310.pyc
│     │        │  │  │  │  └─ xmlrpc.cpython-310.pyc
│     │        │  │  │  ├─ auth.py
│     │        │  │  │  ├─ cache.py
│     │        │  │  │  ├─ download.py
│     │        │  │  │  ├─ lazy_wheel.py
│     │        │  │  │  ├─ session.py
│     │        │  │  │  ├─ utils.py
│     │        │  │  │  └─ xmlrpc.py
│     │        │  │  ├─ operations
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ check.cpython-310.pyc
│     │        │  │  │  │  ├─ freeze.cpython-310.pyc
│     │        │  │  │  │  └─ prepare.cpython-310.pyc
│     │        │  │  │  ├─ build
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ build_tracker.cpython-310.pyc
│     │        │  │  │  │  │  ├─ metadata.cpython-310.pyc
│     │        │  │  │  │  │  ├─ metadata_editable.cpython-310.pyc
│     │        │  │  │  │  │  ├─ metadata_legacy.cpython-310.pyc
│     │        │  │  │  │  │  ├─ wheel.cpython-310.pyc
│     │        │  │  │  │  │  ├─ wheel_editable.cpython-310.pyc
│     │        │  │  │  │  │  └─ wheel_legacy.cpython-310.pyc
│     │        │  │  │  │  ├─ build_tracker.py
│     │        │  │  │  │  ├─ metadata.py
│     │        │  │  │  │  ├─ metadata_editable.py
│     │        │  │  │  │  ├─ metadata_legacy.py
│     │        │  │  │  │  ├─ wheel.py
│     │        │  │  │  │  ├─ wheel_editable.py
│     │        │  │  │  │  └─ wheel_legacy.py
│     │        │  │  │  ├─ check.py
│     │        │  │  │  ├─ freeze.py
│     │        │  │  │  ├─ install
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ editable_legacy.cpython-310.pyc
│     │        │  │  │  │  │  └─ wheel.cpython-310.pyc
│     │        │  │  │  │  ├─ editable_legacy.py
│     │        │  │  │  │  └─ wheel.py
│     │        │  │  │  └─ prepare.py
│     │        │  │  ├─ pyproject.py
│     │        │  │  ├─ req
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ constructors.cpython-310.pyc
│     │        │  │  │  │  ├─ req_file.cpython-310.pyc
│     │        │  │  │  │  ├─ req_install.cpython-310.pyc
│     │        │  │  │  │  ├─ req_set.cpython-310.pyc
│     │        │  │  │  │  └─ req_uninstall.cpython-310.pyc
│     │        │  │  │  ├─ constructors.py
│     │        │  │  │  ├─ req_file.py
│     │        │  │  │  ├─ req_install.py
│     │        │  │  │  ├─ req_set.py
│     │        │  │  │  └─ req_uninstall.py
│     │        │  │  ├─ resolution
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  └─ base.cpython-310.pyc
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ legacy
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  └─ resolver.cpython-310.pyc
│     │        │  │  │  │  └─ resolver.py
│     │        │  │  │  └─ resolvelib
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     ├─ __pycache__
│     │        │  │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │  │     │  ├─ base.cpython-310.pyc
│     │        │  │  │     │  ├─ candidates.cpython-310.pyc
│     │        │  │  │     │  ├─ factory.cpython-310.pyc
│     │        │  │  │     │  ├─ found_candidates.cpython-310.pyc
│     │        │  │  │     │  ├─ provider.cpython-310.pyc
│     │        │  │  │     │  ├─ reporter.cpython-310.pyc
│     │        │  │  │     │  ├─ requirements.cpython-310.pyc
│     │        │  │  │     │  └─ resolver.cpython-310.pyc
│     │        │  │  │     ├─ base.py
│     │        │  │  │     ├─ candidates.py
│     │        │  │  │     ├─ factory.py
│     │        │  │  │     ├─ found_candidates.py
│     │        │  │  │     ├─ provider.py
│     │        │  │  │     ├─ reporter.py
│     │        │  │  │     ├─ requirements.py
│     │        │  │  │     └─ resolver.py
│     │        │  │  ├─ self_outdated_check.py
│     │        │  │  ├─ utils
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _jaraco_text.cpython-310.pyc
│     │        │  │  │  │  ├─ _log.cpython-310.pyc
│     │        │  │  │  │  ├─ appdirs.cpython-310.pyc
│     │        │  │  │  │  ├─ compat.cpython-310.pyc
│     │        │  │  │  │  ├─ compatibility_tags.cpython-310.pyc
│     │        │  │  │  │  ├─ datetime.cpython-310.pyc
│     │        │  │  │  │  ├─ deprecation.cpython-310.pyc
│     │        │  │  │  │  ├─ direct_url_helpers.cpython-310.pyc
│     │        │  │  │  │  ├─ egg_link.cpython-310.pyc
│     │        │  │  │  │  ├─ encoding.cpython-310.pyc
│     │        │  │  │  │  ├─ entrypoints.cpython-310.pyc
│     │        │  │  │  │  ├─ filesystem.cpython-310.pyc
│     │        │  │  │  │  ├─ filetypes.cpython-310.pyc
│     │        │  │  │  │  ├─ glibc.cpython-310.pyc
│     │        │  │  │  │  ├─ hashes.cpython-310.pyc
│     │        │  │  │  │  ├─ inject_securetransport.cpython-310.pyc
│     │        │  │  │  │  ├─ logging.cpython-310.pyc
│     │        │  │  │  │  ├─ misc.cpython-310.pyc
│     │        │  │  │  │  ├─ models.cpython-310.pyc
│     │        │  │  │  │  ├─ packaging.cpython-310.pyc
│     │        │  │  │  │  ├─ setuptools_build.cpython-310.pyc
│     │        │  │  │  │  ├─ subprocess.cpython-310.pyc
│     │        │  │  │  │  ├─ temp_dir.cpython-310.pyc
│     │        │  │  │  │  ├─ unpacking.cpython-310.pyc
│     │        │  │  │  │  ├─ urls.cpython-310.pyc
│     │        │  │  │  │  ├─ virtualenv.cpython-310.pyc
│     │        │  │  │  │  └─ wheel.cpython-310.pyc
│     │        │  │  │  ├─ _jaraco_text.py
│     │        │  │  │  ├─ _log.py
│     │        │  │  │  ├─ appdirs.py
│     │        │  │  │  ├─ compat.py
│     │        │  │  │  ├─ compatibility_tags.py
│     │        │  │  │  ├─ datetime.py
│     │        │  │  │  ├─ deprecation.py
│     │        │  │  │  ├─ direct_url_helpers.py
│     │        │  │  │  ├─ egg_link.py
│     │        │  │  │  ├─ encoding.py
│     │        │  │  │  ├─ entrypoints.py
│     │        │  │  │  ├─ filesystem.py
│     │        │  │  │  ├─ filetypes.py
│     │        │  │  │  ├─ glibc.py
│     │        │  │  │  ├─ hashes.py
│     │        │  │  │  ├─ inject_securetransport.py
│     │        │  │  │  ├─ logging.py
│     │        │  │  │  ├─ misc.py
│     │        │  │  │  ├─ models.py
│     │        │  │  │  ├─ packaging.py
│     │        │  │  │  ├─ setuptools_build.py
│     │        │  │  │  ├─ subprocess.py
│     │        │  │  │  ├─ temp_dir.py
│     │        │  │  │  ├─ unpacking.py
│     │        │  │  │  ├─ urls.py
│     │        │  │  │  ├─ virtualenv.py
│     │        │  │  │  └─ wheel.py
│     │        │  │  ├─ vcs
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ bazaar.cpython-310.pyc
│     │        │  │  │  │  ├─ git.cpython-310.pyc
│     │        │  │  │  │  ├─ mercurial.cpython-310.pyc
│     │        │  │  │  │  ├─ subversion.cpython-310.pyc
│     │        │  │  │  │  └─ versioncontrol.cpython-310.pyc
│     │        │  │  │  ├─ bazaar.py
│     │        │  │  │  ├─ git.py
│     │        │  │  │  ├─ mercurial.py
│     │        │  │  │  ├─ subversion.py
│     │        │  │  │  └─ versioncontrol.py
│     │        │  │  └─ wheel_builder.py
│     │        │  ├─ _vendor
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ six.cpython-310.pyc
│     │        │  │  │  └─ typing_extensions.cpython-310.pyc
│     │        │  │  ├─ cachecontrol
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _cmd.cpython-310.pyc
│     │        │  │  │  │  ├─ adapter.cpython-310.pyc
│     │        │  │  │  │  ├─ cache.cpython-310.pyc
│     │        │  │  │  │  ├─ compat.cpython-310.pyc
│     │        │  │  │  │  ├─ controller.cpython-310.pyc
│     │        │  │  │  │  ├─ filewrapper.cpython-310.pyc
│     │        │  │  │  │  ├─ heuristics.cpython-310.pyc
│     │        │  │  │  │  ├─ serialize.cpython-310.pyc
│     │        │  │  │  │  └─ wrapper.cpython-310.pyc
│     │        │  │  │  ├─ _cmd.py
│     │        │  │  │  ├─ adapter.py
│     │        │  │  │  ├─ cache.py
│     │        │  │  │  ├─ caches
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ file_cache.cpython-310.pyc
│     │        │  │  │  │  │  └─ redis_cache.cpython-310.pyc
│     │        │  │  │  │  ├─ file_cache.py
│     │        │  │  │  │  └─ redis_cache.py
│     │        │  │  │  ├─ compat.py
│     │        │  │  │  ├─ controller.py
│     │        │  │  │  ├─ filewrapper.py
│     │        │  │  │  ├─ heuristics.py
│     │        │  │  │  ├─ serialize.py
│     │        │  │  │  └─ wrapper.py
│     │        │  │  ├─ certifi
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __main__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  │  │  └─ core.cpython-310.pyc
│     │        │  │  │  ├─ cacert.pem
│     │        │  │  │  └─ core.py
│     │        │  │  ├─ chardet
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ big5freq.cpython-310.pyc
│     │        │  │  │  │  ├─ big5prober.cpython-310.pyc
│     │        │  │  │  │  ├─ chardistribution.cpython-310.pyc
│     │        │  │  │  │  ├─ charsetgroupprober.cpython-310.pyc
│     │        │  │  │  │  ├─ charsetprober.cpython-310.pyc
│     │        │  │  │  │  ├─ codingstatemachine.cpython-310.pyc
│     │        │  │  │  │  ├─ codingstatemachinedict.cpython-310.pyc
│     │        │  │  │  │  ├─ cp949prober.cpython-310.pyc
│     │        │  │  │  │  ├─ enums.cpython-310.pyc
│     │        │  │  │  │  ├─ escprober.cpython-310.pyc
│     │        │  │  │  │  ├─ escsm.cpython-310.pyc
│     │        │  │  │  │  ├─ eucjpprober.cpython-310.pyc
│     │        │  │  │  │  ├─ euckrfreq.cpython-310.pyc
│     │        │  │  │  │  ├─ euckrprober.cpython-310.pyc
│     │        │  │  │  │  ├─ euctwfreq.cpython-310.pyc
│     │        │  │  │  │  ├─ euctwprober.cpython-310.pyc
│     │        │  │  │  │  ├─ gb2312freq.cpython-310.pyc
│     │        │  │  │  │  ├─ gb2312prober.cpython-310.pyc
│     │        │  │  │  │  ├─ hebrewprober.cpython-310.pyc
│     │        │  │  │  │  ├─ jisfreq.cpython-310.pyc
│     │        │  │  │  │  ├─ johabfreq.cpython-310.pyc
│     │        │  │  │  │  ├─ johabprober.cpython-310.pyc
│     │        │  │  │  │  ├─ jpcntx.cpython-310.pyc
│     │        │  │  │  │  ├─ langbulgarianmodel.cpython-310.pyc
│     │        │  │  │  │  ├─ langgreekmodel.cpython-310.pyc
│     │        │  │  │  │  ├─ langhebrewmodel.cpython-310.pyc
│     │        │  │  │  │  ├─ langhungarianmodel.cpython-310.pyc
│     │        │  │  │  │  ├─ langrussianmodel.cpython-310.pyc
│     │        │  │  │  │  ├─ langthaimodel.cpython-310.pyc
│     │        │  │  │  │  ├─ langturkishmodel.cpython-310.pyc
│     │        │  │  │  │  ├─ latin1prober.cpython-310.pyc
│     │        │  │  │  │  ├─ macromanprober.cpython-310.pyc
│     │        │  │  │  │  ├─ mbcharsetprober.cpython-310.pyc
│     │        │  │  │  │  ├─ mbcsgroupprober.cpython-310.pyc
│     │        │  │  │  │  ├─ mbcssm.cpython-310.pyc
│     │        │  │  │  │  ├─ resultdict.cpython-310.pyc
│     │        │  │  │  │  ├─ sbcharsetprober.cpython-310.pyc
│     │        │  │  │  │  ├─ sbcsgroupprober.cpython-310.pyc
│     │        │  │  │  │  ├─ sjisprober.cpython-310.pyc
│     │        │  │  │  │  ├─ universaldetector.cpython-310.pyc
│     │        │  │  │  │  ├─ utf1632prober.cpython-310.pyc
│     │        │  │  │  │  ├─ utf8prober.cpython-310.pyc
│     │        │  │  │  │  └─ version.cpython-310.pyc
│     │        │  │  │  ├─ big5freq.py
│     │        │  │  │  ├─ big5prober.py
│     │        │  │  │  ├─ chardistribution.py
│     │        │  │  │  ├─ charsetgroupprober.py
│     │        │  │  │  ├─ charsetprober.py
│     │        │  │  │  ├─ cli
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  └─ chardetect.cpython-310.pyc
│     │        │  │  │  │  └─ chardetect.py
│     │        │  │  │  ├─ codingstatemachine.py
│     │        │  │  │  ├─ codingstatemachinedict.py
│     │        │  │  │  ├─ cp949prober.py
│     │        │  │  │  ├─ enums.py
│     │        │  │  │  ├─ escprober.py
│     │        │  │  │  ├─ escsm.py
│     │        │  │  │  ├─ eucjpprober.py
│     │        │  │  │  ├─ euckrfreq.py
│     │        │  │  │  ├─ euckrprober.py
│     │        │  │  │  ├─ euctwfreq.py
│     │        │  │  │  ├─ euctwprober.py
│     │        │  │  │  ├─ gb2312freq.py
│     │        │  │  │  ├─ gb2312prober.py
│     │        │  │  │  ├─ hebrewprober.py
│     │        │  │  │  ├─ jisfreq.py
│     │        │  │  │  ├─ johabfreq.py
│     │        │  │  │  ├─ johabprober.py
│     │        │  │  │  ├─ jpcntx.py
│     │        │  │  │  ├─ langbulgarianmodel.py
│     │        │  │  │  ├─ langgreekmodel.py
│     │        │  │  │  ├─ langhebrewmodel.py
│     │        │  │  │  ├─ langhungarianmodel.py
│     │        │  │  │  ├─ langrussianmodel.py
│     │        │  │  │  ├─ langthaimodel.py
│     │        │  │  │  ├─ langturkishmodel.py
│     │        │  │  │  ├─ latin1prober.py
│     │        │  │  │  ├─ macromanprober.py
│     │        │  │  │  ├─ mbcharsetprober.py
│     │        │  │  │  ├─ mbcsgroupprober.py
│     │        │  │  │  ├─ mbcssm.py
│     │        │  │  │  ├─ metadata
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  └─ languages.cpython-310.pyc
│     │        │  │  │  │  └─ languages.py
│     │        │  │  │  ├─ resultdict.py
│     │        │  │  │  ├─ sbcharsetprober.py
│     │        │  │  │  ├─ sbcsgroupprober.py
│     │        │  │  │  ├─ sjisprober.py
│     │        │  │  │  ├─ universaldetector.py
│     │        │  │  │  ├─ utf1632prober.py
│     │        │  │  │  ├─ utf8prober.py
│     │        │  │  │  └─ version.py
│     │        │  │  ├─ colorama
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ ansi.cpython-310.pyc
│     │        │  │  │  │  ├─ ansitowin32.cpython-310.pyc
│     │        │  │  │  │  ├─ initialise.cpython-310.pyc
│     │        │  │  │  │  ├─ win32.cpython-310.pyc
│     │        │  │  │  │  └─ winterm.cpython-310.pyc
│     │        │  │  │  ├─ ansi.py
│     │        │  │  │  ├─ ansitowin32.py
│     │        │  │  │  ├─ initialise.py
│     │        │  │  │  ├─ tests
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ ansi_test.cpython-310.pyc
│     │        │  │  │  │  │  ├─ ansitowin32_test.cpython-310.pyc
│     │        │  │  │  │  │  ├─ initialise_test.cpython-310.pyc
│     │        │  │  │  │  │  ├─ isatty_test.cpython-310.pyc
│     │        │  │  │  │  │  ├─ utils.cpython-310.pyc
│     │        │  │  │  │  │  └─ winterm_test.cpython-310.pyc
│     │        │  │  │  │  ├─ ansi_test.py
│     │        │  │  │  │  ├─ ansitowin32_test.py
│     │        │  │  │  │  ├─ initialise_test.py
│     │        │  │  │  │  ├─ isatty_test.py
│     │        │  │  │  │  ├─ utils.py
│     │        │  │  │  │  └─ winterm_test.py
│     │        │  │  │  ├─ win32.py
│     │        │  │  │  └─ winterm.py
│     │        │  │  ├─ distlib
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ compat.cpython-310.pyc
│     │        │  │  │  │  ├─ database.cpython-310.pyc
│     │        │  │  │  │  ├─ index.cpython-310.pyc
│     │        │  │  │  │  ├─ locators.cpython-310.pyc
│     │        │  │  │  │  ├─ manifest.cpython-310.pyc
│     │        │  │  │  │  ├─ markers.cpython-310.pyc
│     │        │  │  │  │  ├─ metadata.cpython-310.pyc
│     │        │  │  │  │  ├─ resources.cpython-310.pyc
│     │        │  │  │  │  ├─ scripts.cpython-310.pyc
│     │        │  │  │  │  ├─ util.cpython-310.pyc
│     │        │  │  │  │  ├─ version.cpython-310.pyc
│     │        │  │  │  │  └─ wheel.cpython-310.pyc
│     │        │  │  │  ├─ compat.py
│     │        │  │  │  ├─ database.py
│     │        │  │  │  ├─ index.py
│     │        │  │  │  ├─ locators.py
│     │        │  │  │  ├─ manifest.py
│     │        │  │  │  ├─ markers.py
│     │        │  │  │  ├─ metadata.py
│     │        │  │  │  ├─ resources.py
│     │        │  │  │  ├─ scripts.py
│     │        │  │  │  ├─ t32.exe
│     │        │  │  │  ├─ t64-arm.exe
│     │        │  │  │  ├─ t64.exe
│     │        │  │  │  ├─ util.py
│     │        │  │  │  ├─ version.py
│     │        │  │  │  ├─ w32.exe
│     │        │  │  │  ├─ w64-arm.exe
│     │        │  │  │  ├─ w64.exe
│     │        │  │  │  └─ wheel.py
│     │        │  │  ├─ distro
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __main__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  │  │  └─ distro.cpython-310.pyc
│     │        │  │  │  └─ distro.py
│     │        │  │  ├─ idna
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ codec.cpython-310.pyc
│     │        │  │  │  │  ├─ compat.cpython-310.pyc
│     │        │  │  │  │  ├─ core.cpython-310.pyc
│     │        │  │  │  │  ├─ idnadata.cpython-310.pyc
│     │        │  │  │  │  ├─ intranges.cpython-310.pyc
│     │        │  │  │  │  ├─ package_data.cpython-310.pyc
│     │        │  │  │  │  └─ uts46data.cpython-310.pyc
│     │        │  │  │  ├─ codec.py
│     │        │  │  │  ├─ compat.py
│     │        │  │  │  ├─ core.py
│     │        │  │  │  ├─ idnadata.py
│     │        │  │  │  ├─ intranges.py
│     │        │  │  │  ├─ package_data.py
│     │        │  │  │  └─ uts46data.py
│     │        │  │  ├─ msgpack
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  │  │  ├─ ext.cpython-310.pyc
│     │        │  │  │  │  └─ fallback.cpython-310.pyc
│     │        │  │  │  ├─ exceptions.py
│     │        │  │  │  ├─ ext.py
│     │        │  │  │  └─ fallback.py
│     │        │  │  ├─ packaging
│     │        │  │  │  ├─ __about__.py
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __about__.cpython-310.pyc
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _manylinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _musllinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _structures.cpython-310.pyc
│     │        │  │  │  │  ├─ markers.cpython-310.pyc
│     │        │  │  │  │  ├─ requirements.cpython-310.pyc
│     │        │  │  │  │  ├─ specifiers.cpython-310.pyc
│     │        │  │  │  │  ├─ tags.cpython-310.pyc
│     │        │  │  │  │  ├─ utils.cpython-310.pyc
│     │        │  │  │  │  └─ version.cpython-310.pyc
│     │        │  │  │  ├─ _manylinux.py
│     │        │  │  │  ├─ _musllinux.py
│     │        │  │  │  ├─ _structures.py
│     │        │  │  │  ├─ markers.py
│     │        │  │  │  ├─ requirements.py
│     │        │  │  │  ├─ specifiers.py
│     │        │  │  │  ├─ tags.py
│     │        │  │  │  ├─ utils.py
│     │        │  │  │  └─ version.py
│     │        │  │  ├─ pkg_resources
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  └─ __pycache__
│     │        │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  ├─ platformdirs
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __main__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  │  │  ├─ android.cpython-310.pyc
│     │        │  │  │  │  ├─ api.cpython-310.pyc
│     │        │  │  │  │  ├─ macos.cpython-310.pyc
│     │        │  │  │  │  ├─ unix.cpython-310.pyc
│     │        │  │  │  │  ├─ version.cpython-310.pyc
│     │        │  │  │  │  └─ windows.cpython-310.pyc
│     │        │  │  │  ├─ android.py
│     │        │  │  │  ├─ api.py
│     │        │  │  │  ├─ macos.py
│     │        │  │  │  ├─ unix.py
│     │        │  │  │  ├─ version.py
│     │        │  │  │  └─ windows.py
│     │        │  │  ├─ pygments
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __main__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  │  │  ├─ cmdline.cpython-310.pyc
│     │        │  │  │  │  ├─ console.cpython-310.pyc
│     │        │  │  │  │  ├─ filter.cpython-310.pyc
│     │        │  │  │  │  ├─ formatter.cpython-310.pyc
│     │        │  │  │  │  ├─ lexer.cpython-310.pyc
│     │        │  │  │  │  ├─ modeline.cpython-310.pyc
│     │        │  │  │  │  ├─ plugin.cpython-310.pyc
│     │        │  │  │  │  ├─ regexopt.cpython-310.pyc
│     │        │  │  │  │  ├─ scanner.cpython-310.pyc
│     │        │  │  │  │  ├─ sphinxext.cpython-310.pyc
│     │        │  │  │  │  ├─ style.cpython-310.pyc
│     │        │  │  │  │  ├─ token.cpython-310.pyc
│     │        │  │  │  │  ├─ unistring.cpython-310.pyc
│     │        │  │  │  │  └─ util.cpython-310.pyc
│     │        │  │  │  ├─ cmdline.py
│     │        │  │  │  ├─ console.py
│     │        │  │  │  ├─ filter.py
│     │        │  │  │  ├─ filters
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ formatter.py
│     │        │  │  │  ├─ formatters
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ _mapping.cpython-310.pyc
│     │        │  │  │  │  │  ├─ bbcode.cpython-310.pyc
│     │        │  │  │  │  │  ├─ groff.cpython-310.pyc
│     │        │  │  │  │  │  ├─ html.cpython-310.pyc
│     │        │  │  │  │  │  ├─ img.cpython-310.pyc
│     │        │  │  │  │  │  ├─ irc.cpython-310.pyc
│     │        │  │  │  │  │  ├─ latex.cpython-310.pyc
│     │        │  │  │  │  │  ├─ other.cpython-310.pyc
│     │        │  │  │  │  │  ├─ pangomarkup.cpython-310.pyc
│     │        │  │  │  │  │  ├─ rtf.cpython-310.pyc
│     │        │  │  │  │  │  ├─ svg.cpython-310.pyc
│     │        │  │  │  │  │  ├─ terminal.cpython-310.pyc
│     │        │  │  │  │  │  └─ terminal256.cpython-310.pyc
│     │        │  │  │  │  ├─ _mapping.py
│     │        │  │  │  │  ├─ bbcode.py
│     │        │  │  │  │  ├─ groff.py
│     │        │  │  │  │  ├─ html.py
│     │        │  │  │  │  ├─ img.py
│     │        │  │  │  │  ├─ irc.py
│     │        │  │  │  │  ├─ latex.py
│     │        │  │  │  │  ├─ other.py
│     │        │  │  │  │  ├─ pangomarkup.py
│     │        │  │  │  │  ├─ rtf.py
│     │        │  │  │  │  ├─ svg.py
│     │        │  │  │  │  ├─ terminal.py
│     │        │  │  │  │  └─ terminal256.py
│     │        │  │  │  ├─ lexer.py
│     │        │  │  │  ├─ lexers
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ _mapping.cpython-310.pyc
│     │        │  │  │  │  │  └─ python.cpython-310.pyc
│     │        │  │  │  │  ├─ _mapping.py
│     │        │  │  │  │  └─ python.py
│     │        │  │  │  ├─ modeline.py
│     │        │  │  │  ├─ plugin.py
│     │        │  │  │  ├─ regexopt.py
│     │        │  │  │  ├─ scanner.py
│     │        │  │  │  ├─ sphinxext.py
│     │        │  │  │  ├─ style.py
│     │        │  │  │  ├─ styles
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ token.py
│     │        │  │  │  ├─ unistring.py
│     │        │  │  │  └─ util.py
│     │        │  │  ├─ pyparsing
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ actions.cpython-310.pyc
│     │        │  │  │  │  ├─ common.cpython-310.pyc
│     │        │  │  │  │  ├─ core.cpython-310.pyc
│     │        │  │  │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  │  │  ├─ helpers.cpython-310.pyc
│     │        │  │  │  │  ├─ results.cpython-310.pyc
│     │        │  │  │  │  ├─ testing.cpython-310.pyc
│     │        │  │  │  │  ├─ unicode.cpython-310.pyc
│     │        │  │  │  │  └─ util.cpython-310.pyc
│     │        │  │  │  ├─ actions.py
│     │        │  │  │  ├─ common.py
│     │        │  │  │  ├─ core.py
│     │        │  │  │  ├─ diagram
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  └─ __pycache__
│     │        │  │  │  │     └─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ exceptions.py
│     │        │  │  │  ├─ helpers.py
│     │        │  │  │  ├─ results.py
│     │        │  │  │  ├─ testing.py
│     │        │  │  │  ├─ unicode.py
│     │        │  │  │  └─ util.py
│     │        │  │  ├─ requests
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ __version__.cpython-310.pyc
│     │        │  │  │  │  ├─ _internal_utils.cpython-310.pyc
│     │        │  │  │  │  ├─ adapters.cpython-310.pyc
│     │        │  │  │  │  ├─ api.cpython-310.pyc
│     │        │  │  │  │  ├─ auth.cpython-310.pyc
│     │        │  │  │  │  ├─ certs.cpython-310.pyc
│     │        │  │  │  │  ├─ compat.cpython-310.pyc
│     │        │  │  │  │  ├─ cookies.cpython-310.pyc
│     │        │  │  │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  │  │  ├─ help.cpython-310.pyc
│     │        │  │  │  │  ├─ models.cpython-310.pyc
│     │        │  │  │  │  ├─ packages.cpython-310.pyc
│     │        │  │  │  │  ├─ sessions.cpython-310.pyc
│     │        │  │  │  │  ├─ status_codes.cpython-310.pyc
│     │        │  │  │  │  ├─ structures.cpython-310.pyc
│     │        │  │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  │  ├─ __version__.py
│     │        │  │  │  ├─ _internal_utils.py
│     │        │  │  │  ├─ adapters.py
│     │        │  │  │  ├─ api.py
│     │        │  │  │  ├─ auth.py
│     │        │  │  │  ├─ certs.py
│     │        │  │  │  ├─ compat.py
│     │        │  │  │  ├─ cookies.py
│     │        │  │  │  ├─ exceptions.py
│     │        │  │  │  ├─ help.py
│     │        │  │  │  ├─ models.py
│     │        │  │  │  ├─ packages.py
│     │        │  │  │  ├─ sessions.py
│     │        │  │  │  ├─ status_codes.py
│     │        │  │  │  ├─ structures.py
│     │        │  │  │  └─ utils.py
│     │        │  │  ├─ resolvelib
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ providers.cpython-310.pyc
│     │        │  │  │  │  ├─ reporters.cpython-310.pyc
│     │        │  │  │  │  ├─ resolvers.cpython-310.pyc
│     │        │  │  │  │  └─ structs.cpython-310.pyc
│     │        │  │  │  ├─ compat
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  └─ collections_abc.cpython-310.pyc
│     │        │  │  │  │  └─ collections_abc.py
│     │        │  │  │  ├─ providers.py
│     │        │  │  │  ├─ reporters.py
│     │        │  │  │  ├─ resolvers.py
│     │        │  │  │  └─ structs.py
│     │        │  │  ├─ rich
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __main__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  │  │  ├─ _cell_widths.cpython-310.pyc
│     │        │  │  │  │  ├─ _emoji_codes.cpython-310.pyc
│     │        │  │  │  │  ├─ _emoji_replace.cpython-310.pyc
│     │        │  │  │  │  ├─ _export_format.cpython-310.pyc
│     │        │  │  │  │  ├─ _extension.cpython-310.pyc
│     │        │  │  │  │  ├─ _fileno.cpython-310.pyc
│     │        │  │  │  │  ├─ _inspect.cpython-310.pyc
│     │        │  │  │  │  ├─ _log_render.cpython-310.pyc
│     │        │  │  │  │  ├─ _loop.cpython-310.pyc
│     │        │  │  │  │  ├─ _null_file.cpython-310.pyc
│     │        │  │  │  │  ├─ _palettes.cpython-310.pyc
│     │        │  │  │  │  ├─ _pick.cpython-310.pyc
│     │        │  │  │  │  ├─ _ratio.cpython-310.pyc
│     │        │  │  │  │  ├─ _spinners.cpython-310.pyc
│     │        │  │  │  │  ├─ _stack.cpython-310.pyc
│     │        │  │  │  │  ├─ _timer.cpython-310.pyc
│     │        │  │  │  │  ├─ _win32_console.cpython-310.pyc
│     │        │  │  │  │  ├─ _windows.cpython-310.pyc
│     │        │  │  │  │  ├─ _windows_renderer.cpython-310.pyc
│     │        │  │  │  │  ├─ _wrap.cpython-310.pyc
│     │        │  │  │  │  ├─ abc.cpython-310.pyc
│     │        │  │  │  │  ├─ align.cpython-310.pyc
│     │        │  │  │  │  ├─ ansi.cpython-310.pyc
│     │        │  │  │  │  ├─ bar.cpython-310.pyc
│     │        │  │  │  │  ├─ box.cpython-310.pyc
│     │        │  │  │  │  ├─ cells.cpython-310.pyc
│     │        │  │  │  │  ├─ color.cpython-310.pyc
│     │        │  │  │  │  ├─ color_triplet.cpython-310.pyc
│     │        │  │  │  │  ├─ columns.cpython-310.pyc
│     │        │  │  │  │  ├─ console.cpython-310.pyc
│     │        │  │  │  │  ├─ constrain.cpython-310.pyc
│     │        │  │  │  │  ├─ containers.cpython-310.pyc
│     │        │  │  │  │  ├─ control.cpython-310.pyc
│     │        │  │  │  │  ├─ default_styles.cpython-310.pyc
│     │        │  │  │  │  ├─ diagnose.cpython-310.pyc
│     │        │  │  │  │  ├─ emoji.cpython-310.pyc
│     │        │  │  │  │  ├─ errors.cpython-310.pyc
│     │        │  │  │  │  ├─ file_proxy.cpython-310.pyc
│     │        │  │  │  │  ├─ filesize.cpython-310.pyc
│     │        │  │  │  │  ├─ highlighter.cpython-310.pyc
│     │        │  │  │  │  ├─ json.cpython-310.pyc
│     │        │  │  │  │  ├─ jupyter.cpython-310.pyc
│     │        │  │  │  │  ├─ layout.cpython-310.pyc
│     │        │  │  │  │  ├─ live.cpython-310.pyc
│     │        │  │  │  │  ├─ live_render.cpython-310.pyc
│     │        │  │  │  │  ├─ logging.cpython-310.pyc
│     │        │  │  │  │  ├─ markup.cpython-310.pyc
│     │        │  │  │  │  ├─ measure.cpython-310.pyc
│     │        │  │  │  │  ├─ padding.cpython-310.pyc
│     │        │  │  │  │  ├─ pager.cpython-310.pyc
│     │        │  │  │  │  ├─ palette.cpython-310.pyc
│     │        │  │  │  │  ├─ panel.cpython-310.pyc
│     │        │  │  │  │  ├─ pretty.cpython-310.pyc
│     │        │  │  │  │  ├─ progress.cpython-310.pyc
│     │        │  │  │  │  ├─ progress_bar.cpython-310.pyc
│     │        │  │  │  │  ├─ prompt.cpython-310.pyc
│     │        │  │  │  │  ├─ protocol.cpython-310.pyc
│     │        │  │  │  │  ├─ region.cpython-310.pyc
│     │        │  │  │  │  ├─ repr.cpython-310.pyc
│     │        │  │  │  │  ├─ rule.cpython-310.pyc
│     │        │  │  │  │  ├─ scope.cpython-310.pyc
│     │        │  │  │  │  ├─ screen.cpython-310.pyc
│     │        │  │  │  │  ├─ segment.cpython-310.pyc
│     │        │  │  │  │  ├─ spinner.cpython-310.pyc
│     │        │  │  │  │  ├─ status.cpython-310.pyc
│     │        │  │  │  │  ├─ style.cpython-310.pyc
│     │        │  │  │  │  ├─ styled.cpython-310.pyc
│     │        │  │  │  │  ├─ syntax.cpython-310.pyc
│     │        │  │  │  │  ├─ table.cpython-310.pyc
│     │        │  │  │  │  ├─ terminal_theme.cpython-310.pyc
│     │        │  │  │  │  ├─ text.cpython-310.pyc
│     │        │  │  │  │  ├─ theme.cpython-310.pyc
│     │        │  │  │  │  ├─ themes.cpython-310.pyc
│     │        │  │  │  │  ├─ traceback.cpython-310.pyc
│     │        │  │  │  │  └─ tree.cpython-310.pyc
│     │        │  │  │  ├─ _cell_widths.py
│     │        │  │  │  ├─ _emoji_codes.py
│     │        │  │  │  ├─ _emoji_replace.py
│     │        │  │  │  ├─ _export_format.py
│     │        │  │  │  ├─ _extension.py
│     │        │  │  │  ├─ _fileno.py
│     │        │  │  │  ├─ _inspect.py
│     │        │  │  │  ├─ _log_render.py
│     │        │  │  │  ├─ _loop.py
│     │        │  │  │  ├─ _null_file.py
│     │        │  │  │  ├─ _palettes.py
│     │        │  │  │  ├─ _pick.py
│     │        │  │  │  ├─ _ratio.py
│     │        │  │  │  ├─ _spinners.py
│     │        │  │  │  ├─ _stack.py
│     │        │  │  │  ├─ _timer.py
│     │        │  │  │  ├─ _win32_console.py
│     │        │  │  │  ├─ _windows.py
│     │        │  │  │  ├─ _windows_renderer.py
│     │        │  │  │  ├─ _wrap.py
│     │        │  │  │  ├─ abc.py
│     │        │  │  │  ├─ align.py
│     │        │  │  │  ├─ ansi.py
│     │        │  │  │  ├─ bar.py
│     │        │  │  │  ├─ box.py
│     │        │  │  │  ├─ cells.py
│     │        │  │  │  ├─ color.py
│     │        │  │  │  ├─ color_triplet.py
│     │        │  │  │  ├─ columns.py
│     │        │  │  │  ├─ console.py
│     │        │  │  │  ├─ constrain.py
│     │        │  │  │  ├─ containers.py
│     │        │  │  │  ├─ control.py
│     │        │  │  │  ├─ default_styles.py
│     │        │  │  │  ├─ diagnose.py
│     │        │  │  │  ├─ emoji.py
│     │        │  │  │  ├─ errors.py
│     │        │  │  │  ├─ file_proxy.py
│     │        │  │  │  ├─ filesize.py
│     │        │  │  │  ├─ highlighter.py
│     │        │  │  │  ├─ json.py
│     │        │  │  │  ├─ jupyter.py
│     │        │  │  │  ├─ layout.py
│     │        │  │  │  ├─ live.py
│     │        │  │  │  ├─ live_render.py
│     │        │  │  │  ├─ logging.py
│     │        │  │  │  ├─ markup.py
│     │        │  │  │  ├─ measure.py
│     │        │  │  │  ├─ padding.py
│     │        │  │  │  ├─ pager.py
│     │        │  │  │  ├─ palette.py
│     │        │  │  │  ├─ panel.py
│     │        │  │  │  ├─ pretty.py
│     │        │  │  │  ├─ progress.py
│     │        │  │  │  ├─ progress_bar.py
│     │        │  │  │  ├─ prompt.py
│     │        │  │  │  ├─ protocol.py
│     │        │  │  │  ├─ region.py
│     │        │  │  │  ├─ repr.py
│     │        │  │  │  ├─ rule.py
│     │        │  │  │  ├─ scope.py
│     │        │  │  │  ├─ screen.py
│     │        │  │  │  ├─ segment.py
│     │        │  │  │  ├─ spinner.py
│     │        │  │  │  ├─ status.py
│     │        │  │  │  ├─ style.py
│     │        │  │  │  ├─ styled.py
│     │        │  │  │  ├─ syntax.py
│     │        │  │  │  ├─ table.py
│     │        │  │  │  ├─ terminal_theme.py
│     │        │  │  │  ├─ text.py
│     │        │  │  │  ├─ theme.py
│     │        │  │  │  ├─ themes.py
│     │        │  │  │  ├─ traceback.py
│     │        │  │  │  └─ tree.py
│     │        │  │  ├─ six.py
│     │        │  │  ├─ tenacity
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _asyncio.cpython-310.pyc
│     │        │  │  │  │  ├─ _utils.cpython-310.pyc
│     │        │  │  │  │  ├─ after.cpython-310.pyc
│     │        │  │  │  │  ├─ before.cpython-310.pyc
│     │        │  │  │  │  ├─ before_sleep.cpython-310.pyc
│     │        │  │  │  │  ├─ nap.cpython-310.pyc
│     │        │  │  │  │  ├─ retry.cpython-310.pyc
│     │        │  │  │  │  ├─ stop.cpython-310.pyc
│     │        │  │  │  │  ├─ tornadoweb.cpython-310.pyc
│     │        │  │  │  │  └─ wait.cpython-310.pyc
│     │        │  │  │  ├─ _asyncio.py
│     │        │  │  │  ├─ _utils.py
│     │        │  │  │  ├─ after.py
│     │        │  │  │  ├─ before.py
│     │        │  │  │  ├─ before_sleep.py
│     │        │  │  │  ├─ nap.py
│     │        │  │  │  ├─ retry.py
│     │        │  │  │  ├─ stop.py
│     │        │  │  │  ├─ tornadoweb.py
│     │        │  │  │  └─ wait.py
│     │        │  │  ├─ tomli
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _parser.cpython-310.pyc
│     │        │  │  │  │  ├─ _re.cpython-310.pyc
│     │        │  │  │  │  └─ _types.cpython-310.pyc
│     │        │  │  │  ├─ _parser.py
│     │        │  │  │  ├─ _re.py
│     │        │  │  │  └─ _types.py
│     │        │  │  ├─ typing_extensions.py
│     │        │  │  ├─ urllib3
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _collections.cpython-310.pyc
│     │        │  │  │  │  ├─ _version.cpython-310.pyc
│     │        │  │  │  │  ├─ connection.cpython-310.pyc
│     │        │  │  │  │  ├─ connectionpool.cpython-310.pyc
│     │        │  │  │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  │  │  ├─ fields.cpython-310.pyc
│     │        │  │  │  │  ├─ filepost.cpython-310.pyc
│     │        │  │  │  │  ├─ poolmanager.cpython-310.pyc
│     │        │  │  │  │  ├─ request.cpython-310.pyc
│     │        │  │  │  │  └─ response.cpython-310.pyc
│     │        │  │  │  ├─ _collections.py
│     │        │  │  │  ├─ _version.py
│     │        │  │  │  ├─ connection.py
│     │        │  │  │  ├─ connectionpool.py
│     │        │  │  │  ├─ contrib
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  ├─ _appengine_environ.cpython-310.pyc
│     │        │  │  │  │  │  ├─ appengine.cpython-310.pyc
│     │        │  │  │  │  │  ├─ ntlmpool.cpython-310.pyc
│     │        │  │  │  │  │  ├─ pyopenssl.cpython-310.pyc
│     │        │  │  │  │  │  ├─ securetransport.cpython-310.pyc
│     │        │  │  │  │  │  └─ socks.cpython-310.pyc
│     │        │  │  │  │  ├─ _appengine_environ.py
│     │        │  │  │  │  ├─ _securetransport
│     │        │  │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  │  ├─ bindings.cpython-310.pyc
│     │        │  │  │  │  │  │  └─ low_level.cpython-310.pyc
│     │        │  │  │  │  │  ├─ bindings.py
│     │        │  │  │  │  │  └─ low_level.py
│     │        │  │  │  │  ├─ appengine.py
│     │        │  │  │  │  ├─ ntlmpool.py
│     │        │  │  │  │  ├─ pyopenssl.py
│     │        │  │  │  │  ├─ securetransport.py
│     │        │  │  │  │  └─ socks.py
│     │        │  │  │  ├─ exceptions.py
│     │        │  │  │  ├─ fields.py
│     │        │  │  │  ├─ filepost.py
│     │        │  │  │  ├─ packages
│     │        │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  └─ six.cpython-310.pyc
│     │        │  │  │  │  ├─ backports
│     │        │  │  │  │  │  ├─ __init__.py
│     │        │  │  │  │  │  ├─ __pycache__
│     │        │  │  │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  │  │  └─ makefile.cpython-310.pyc
│     │        │  │  │  │  │  └─ makefile.py
│     │        │  │  │  │  └─ six.py
│     │        │  │  │  ├─ poolmanager.py
│     │        │  │  │  ├─ request.py
│     │        │  │  │  ├─ response.py
│     │        │  │  │  └─ util
│     │        │  │  │     ├─ __init__.py
│     │        │  │  │     ├─ __pycache__
│     │        │  │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │  │     │  ├─ connection.cpython-310.pyc
│     │        │  │  │     │  ├─ proxy.cpython-310.pyc
│     │        │  │  │     │  ├─ queue.cpython-310.pyc
│     │        │  │  │     │  ├─ request.cpython-310.pyc
│     │        │  │  │     │  ├─ response.cpython-310.pyc
│     │        │  │  │     │  ├─ retry.cpython-310.pyc
│     │        │  │  │     │  ├─ ssl_.cpython-310.pyc
│     │        │  │  │     │  ├─ ssl_match_hostname.cpython-310.pyc
│     │        │  │  │     │  ├─ ssltransport.cpython-310.pyc
│     │        │  │  │     │  ├─ timeout.cpython-310.pyc
│     │        │  │  │     │  ├─ url.cpython-310.pyc
│     │        │  │  │     │  └─ wait.cpython-310.pyc
│     │        │  │  │     ├─ connection.py
│     │        │  │  │     ├─ proxy.py
│     │        │  │  │     ├─ queue.py
│     │        │  │  │     ├─ request.py
│     │        │  │  │     ├─ response.py
│     │        │  │  │     ├─ retry.py
│     │        │  │  │     ├─ ssl_.py
│     │        │  │  │     ├─ ssl_match_hostname.py
│     │        │  │  │     ├─ ssltransport.py
│     │        │  │  │     ├─ timeout.py
│     │        │  │  │     ├─ url.py
│     │        │  │  │     └─ wait.py
│     │        │  │  ├─ vendor.txt
│     │        │  │  └─ webencodings
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ labels.cpython-310.pyc
│     │        │  │     │  ├─ mklabels.cpython-310.pyc
│     │        │  │     │  ├─ tests.cpython-310.pyc
│     │        │  │     │  └─ x_user_defined.cpython-310.pyc
│     │        │  │     ├─ labels.py
│     │        │  │     ├─ mklabels.py
│     │        │  │     ├─ tests.py
│     │        │  │     └─ x_user_defined.py
│     │        │  └─ py.typed
│     │        ├─ pip-23.1.2.dist-info
│     │        │  ├─ AUTHORS.txt
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.txt
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ pip_tools-6.14.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ piptools
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ cache.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ locations.cpython-310.pyc
│     │        │  │  ├─ logging.cpython-310.pyc
│     │        │  │  ├─ resolver.cpython-310.pyc
│     │        │  │  ├─ subprocess_utils.cpython-310.pyc
│     │        │  │  ├─ sync.cpython-310.pyc
│     │        │  │  ├─ utils.cpython-310.pyc
│     │        │  │  └─ writer.cpython-310.pyc
│     │        │  ├─ _compat
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ pip_compat.cpython-310.pyc
│     │        │  │  └─ pip_compat.py
│     │        │  ├─ cache.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ locations.py
│     │        │  ├─ logging.py
│     │        │  ├─ py.typed
│     │        │  ├─ repositories
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ local.cpython-310.pyc
│     │        │  │  │  └─ pypi.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ local.py
│     │        │  │  └─ pypi.py
│     │        │  ├─ resolver.py
│     │        │  ├─ scripts
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ compile.cpython-310.pyc
│     │        │  │  │  └─ sync.cpython-310.pyc
│     │        │  │  ├─ compile.py
│     │        │  │  └─ sync.py
│     │        │  ├─ subprocess_utils.py
│     │        │  ├─ sync.py
│     │        │  ├─ utils.py
│     │        │  └─ writer.py
│     │        ├─ pkg_resources
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  └─ __init__.cpython-310.pyc
│     │        │  ├─ _vendor
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ appdirs.cpython-310.pyc
│     │        │  │  │  └─ pyparsing.cpython-310.pyc
│     │        │  │  ├─ appdirs.py
│     │        │  │  ├─ packaging
│     │        │  │  │  ├─ __about__.py
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __about__.cpython-310.pyc
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _manylinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _musllinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _structures.cpython-310.pyc
│     │        │  │  │  │  ├─ markers.cpython-310.pyc
│     │        │  │  │  │  ├─ requirements.cpython-310.pyc
│     │        │  │  │  │  ├─ specifiers.cpython-310.pyc
│     │        │  │  │  │  ├─ tags.cpython-310.pyc
│     │        │  │  │  │  ├─ utils.cpython-310.pyc
│     │        │  │  │  │  └─ version.cpython-310.pyc
│     │        │  │  │  ├─ _manylinux.py
│     │        │  │  │  ├─ _musllinux.py
│     │        │  │  │  ├─ _structures.py
│     │        │  │  │  ├─ markers.py
│     │        │  │  │  ├─ requirements.py
│     │        │  │  │  ├─ specifiers.py
│     │        │  │  │  ├─ tags.py
│     │        │  │  │  ├─ utils.py
│     │        │  │  │  └─ version.py
│     │        │  │  └─ pyparsing.py
│     │        │  ├─ extern
│     │        │  │  ├─ __init__.py
│     │        │  │  └─ __pycache__
│     │        │  │     └─ __init__.cpython-310.pyc
│     │        │  └─ tests
│     │        │     └─ data
│     │        │        └─ my-test-package-source
│     │        │           ├─ __pycache__
│     │        │           │  └─ setup.cpython-310.pyc
│     │        │           └─ setup.py
│     │        ├─ platformdirs
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ android.cpython-310.pyc
│     │        │  │  ├─ api.cpython-310.pyc
│     │        │  │  ├─ macos.cpython-310.pyc
│     │        │  │  ├─ unix.cpython-310.pyc
│     │        │  │  ├─ version.cpython-310.pyc
│     │        │  │  └─ windows.cpython-310.pyc
│     │        │  ├─ android.py
│     │        │  ├─ api.py
│     │        │  ├─ macos.py
│     │        │  ├─ py.typed
│     │        │  ├─ unix.py
│     │        │  ├─ version.py
│     │        │  └─ windows.py
│     │        ├─ platformdirs-3.8.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ licenses
│     │        │     └─ LICENSE
│     │        ├─ pluggy
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _callers.cpython-310.pyc
│     │        │  │  ├─ _manager.cpython-310.pyc
│     │        │  │  ├─ _result.cpython-310.pyc
│     │        │  │  ├─ _tracing.cpython-310.pyc
│     │        │  │  └─ _version.cpython-310.pyc
│     │        │  ├─ _callers.py
│     │        │  ├─ _manager.py
│     │        │  ├─ _result.py
│     │        │  ├─ _tracing.py
│     │        │  └─ _version.py
│     │        ├─ pluggy-1.2.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ polyfactory
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ constants.cpython-310.pyc
│     │        │  │  ├─ decorators.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ field_meta.cpython-310.pyc
│     │        │  │  ├─ fields.cpython-310.pyc
│     │        │  │  ├─ persistence.cpython-310.pyc
│     │        │  │  └─ pytest_plugin.cpython-310.pyc
│     │        │  ├─ constants.py
│     │        │  ├─ decorators.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ factories
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ beanie_odm_factory.cpython-310.pyc
│     │        │  │  │  ├─ dataclass_factory.cpython-310.pyc
│     │        │  │  │  ├─ msgspec_factory.cpython-310.pyc
│     │        │  │  │  ├─ odmantic_odm_factory.cpython-310.pyc
│     │        │  │  │  ├─ pydantic_factory.cpython-310.pyc
│     │        │  │  │  └─ typed_dict_factory.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ beanie_odm_factory.py
│     │        │  │  ├─ dataclass_factory.py
│     │        │  │  ├─ msgspec_factory.py
│     │        │  │  ├─ odmantic_odm_factory.py
│     │        │  │  ├─ pydantic_factory.py
│     │        │  │  └─ typed_dict_factory.py
│     │        │  ├─ field_meta.py
│     │        │  ├─ fields.py
│     │        │  ├─ persistence.py
│     │        │  ├─ py.typed
│     │        │  ├─ pytest_plugin.py
│     │        │  ├─ utils
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ helpers.cpython-310.pyc
│     │        │  │  │  └─ predicates.cpython-310.pyc
│     │        │  │  ├─ helpers.py
│     │        │  │  └─ predicates.py
│     │        │  └─ value_generators
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ complex_types.cpython-310.pyc
│     │        │     │  ├─ constrained_collections.cpython-310.pyc
│     │        │     │  ├─ constrained_dates.cpython-310.pyc
│     │        │     │  ├─ constrained_numbers.cpython-310.pyc
│     │        │     │  ├─ constrained_path.cpython-310.pyc
│     │        │     │  ├─ constrained_strings.cpython-310.pyc
│     │        │     │  ├─ constrained_url.cpython-310.pyc
│     │        │     │  ├─ constrained_uuid.cpython-310.pyc
│     │        │     │  ├─ primitives.cpython-310.pyc
│     │        │     │  └─ regex.cpython-310.pyc
│     │        │     ├─ complex_types.py
│     │        │     ├─ constrained_collections.py
│     │        │     ├─ constrained_dates.py
│     │        │     ├─ constrained_numbers.py
│     │        │     ├─ constrained_path.py
│     │        │     ├─ constrained_strings.py
│     │        │     ├─ constrained_url.py
│     │        │     ├─ constrained_uuid.py
│     │        │     ├─ primitives.py
│     │        │     └─ regex.py
│     │        ├─ polyfactory-2.5.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ py
│     │        │  ├─ __init__.py
│     │        │  ├─ __init__.pyi
│     │        │  ├─ __metainfo.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __metainfo.cpython-310.pyc
│     │        │  │  ├─ _builtin.cpython-310.pyc
│     │        │  │  ├─ _error.cpython-310.pyc
│     │        │  │  ├─ _std.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  ├─ _xmlgen.cpython-310.pyc
│     │        │  │  └─ test.cpython-310.pyc
│     │        │  ├─ _builtin.py
│     │        │  ├─ _code
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _assertionnew.cpython-310.pyc
│     │        │  │  │  ├─ _assertionold.cpython-310.pyc
│     │        │  │  │  ├─ _py2traceback.cpython-310.pyc
│     │        │  │  │  ├─ assertion.cpython-310.pyc
│     │        │  │  │  ├─ code.cpython-310.pyc
│     │        │  │  │  └─ source.cpython-310.pyc
│     │        │  │  ├─ _assertionnew.py
│     │        │  │  ├─ _assertionold.py
│     │        │  │  ├─ _py2traceback.py
│     │        │  │  ├─ assertion.py
│     │        │  │  ├─ code.py
│     │        │  │  └─ source.py
│     │        │  ├─ _error.py
│     │        │  ├─ _io
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ capture.cpython-310.pyc
│     │        │  │  │  ├─ saferepr.cpython-310.pyc
│     │        │  │  │  └─ terminalwriter.cpython-310.pyc
│     │        │  │  ├─ capture.py
│     │        │  │  ├─ saferepr.py
│     │        │  │  └─ terminalwriter.py
│     │        │  ├─ _log
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ log.cpython-310.pyc
│     │        │  │  │  └─ warning.cpython-310.pyc
│     │        │  │  ├─ log.py
│     │        │  │  └─ warning.py
│     │        │  ├─ _path
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cacheutil.cpython-310.pyc
│     │        │  │  │  ├─ common.cpython-310.pyc
│     │        │  │  │  ├─ local.cpython-310.pyc
│     │        │  │  │  ├─ svnurl.cpython-310.pyc
│     │        │  │  │  └─ svnwc.cpython-310.pyc
│     │        │  │  ├─ cacheutil.py
│     │        │  │  ├─ common.py
│     │        │  │  ├─ local.py
│     │        │  │  ├─ svnurl.py
│     │        │  │  └─ svnwc.py
│     │        │  ├─ _process
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cmdexec.cpython-310.pyc
│     │        │  │  │  ├─ forkedfunc.cpython-310.pyc
│     │        │  │  │  └─ killproc.cpython-310.pyc
│     │        │  │  ├─ cmdexec.py
│     │        │  │  ├─ forkedfunc.py
│     │        │  │  └─ killproc.py
│     │        │  ├─ _std.py
│     │        │  ├─ _vendored_packages
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ apipkg
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  └─ version.cpython-310.pyc
│     │        │  │  │  └─ version.py
│     │        │  │  ├─ apipkg-2.0.0.dist-info
│     │        │  │  │  ├─ INSTALLER
│     │        │  │  │  ├─ LICENSE
│     │        │  │  │  ├─ METADATA
│     │        │  │  │  ├─ RECORD
│     │        │  │  │  ├─ REQUESTED
│     │        │  │  │  ├─ WHEEL
│     │        │  │  │  └─ top_level.txt
│     │        │  │  ├─ iniconfig
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __init__.pyi
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  │  └─ py.typed
│     │        │  │  └─ iniconfig-1.1.1.dist-info
│     │        │  │     ├─ INSTALLER
│     │        │  │     ├─ LICENSE
│     │        │  │     ├─ METADATA
│     │        │  │     ├─ RECORD
│     │        │  │     ├─ REQUESTED
│     │        │  │     ├─ WHEEL
│     │        │  │     └─ top_level.txt
│     │        │  ├─ _version.py
│     │        │  ├─ _xmlgen.py
│     │        │  ├─ error.pyi
│     │        │  ├─ iniconfig.pyi
│     │        │  ├─ io.pyi
│     │        │  ├─ path.pyi
│     │        │  ├─ py.typed
│     │        │  ├─ test.py
│     │        │  └─ xml.pyi
│     │        ├─ py-1.11.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ py.py
│     │        ├─ pycparser
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _ast_gen.cpython-310.pyc
│     │        │  │  ├─ _build_tables.cpython-310.pyc
│     │        │  │  ├─ ast_transforms.cpython-310.pyc
│     │        │  │  ├─ c_ast.cpython-310.pyc
│     │        │  │  ├─ c_generator.cpython-310.pyc
│     │        │  │  ├─ c_lexer.cpython-310.pyc
│     │        │  │  ├─ c_parser.cpython-310.pyc
│     │        │  │  ├─ lextab.cpython-310.pyc
│     │        │  │  ├─ plyparser.cpython-310.pyc
│     │        │  │  └─ yacctab.cpython-310.pyc
│     │        │  ├─ _ast_gen.py
│     │        │  ├─ _build_tables.py
│     │        │  ├─ _c_ast.cfg
│     │        │  ├─ ast_transforms.py
│     │        │  ├─ c_ast.py
│     │        │  ├─ c_generator.py
│     │        │  ├─ c_lexer.py
│     │        │  ├─ c_parser.py
│     │        │  ├─ lextab.py
│     │        │  ├─ ply
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ cpp.cpython-310.pyc
│     │        │  │  │  ├─ ctokens.cpython-310.pyc
│     │        │  │  │  ├─ lex.cpython-310.pyc
│     │        │  │  │  ├─ yacc.cpython-310.pyc
│     │        │  │  │  └─ ygen.cpython-310.pyc
│     │        │  │  ├─ cpp.py
│     │        │  │  ├─ ctokens.py
│     │        │  │  ├─ lex.py
│     │        │  │  ├─ yacc.py
│     │        │  │  └─ ygen.py
│     │        │  ├─ plyparser.py
│     │        │  └─ yacctab.py
│     │        ├─ pycparser-2.21.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ pydantic
│     │        │  ├─ __init__.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _hypothesis_plugin.cpython-310.pyc
│     │        │  │  ├─ annotated_types.cpython-310.pyc
│     │        │  │  ├─ class_validators.cpython-310.pyc
│     │        │  │  ├─ color.cpython-310.pyc
│     │        │  │  ├─ config.cpython-310.pyc
│     │        │  │  ├─ dataclasses.cpython-310.pyc
│     │        │  │  ├─ datetime_parse.cpython-310.pyc
│     │        │  │  ├─ decorator.cpython-310.pyc
│     │        │  │  ├─ env_settings.cpython-310.pyc
│     │        │  │  ├─ error_wrappers.cpython-310.pyc
│     │        │  │  ├─ errors.cpython-310.pyc
│     │        │  │  ├─ fields.cpython-310.pyc
│     │        │  │  ├─ generics.cpython-310.pyc
│     │        │  │  ├─ json.cpython-310.pyc
│     │        │  │  ├─ main.cpython-310.pyc
│     │        │  │  ├─ mypy.cpython-310.pyc
│     │        │  │  ├─ networks.cpython-310.pyc
│     │        │  │  ├─ parse.cpython-310.pyc
│     │        │  │  ├─ schema.cpython-310.pyc
│     │        │  │  ├─ tools.cpython-310.pyc
│     │        │  │  ├─ types.cpython-310.pyc
│     │        │  │  ├─ typing.cpython-310.pyc
│     │        │  │  ├─ utils.cpython-310.pyc
│     │        │  │  ├─ validators.cpython-310.pyc
│     │        │  │  └─ version.cpython-310.pyc
│     │        │  ├─ _hypothesis_plugin.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ _hypothesis_plugin.py
│     │        │  ├─ annotated_types.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ annotated_types.py
│     │        │  ├─ class_validators.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ class_validators.py
│     │        │  ├─ color.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ color.py
│     │        │  ├─ config.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ config.py
│     │        │  ├─ dataclasses.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ dataclasses.py
│     │        │  ├─ datetime_parse.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ datetime_parse.py
│     │        │  ├─ decorator.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ decorator.py
│     │        │  ├─ env_settings.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ env_settings.py
│     │        │  ├─ error_wrappers.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ error_wrappers.py
│     │        │  ├─ errors.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ errors.py
│     │        │  ├─ fields.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ fields.py
│     │        │  ├─ generics.py
│     │        │  ├─ json.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ json.py
│     │        │  ├─ main.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ main.py
│     │        │  ├─ mypy.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ mypy.py
│     │        │  ├─ networks.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ networks.py
│     │        │  ├─ parse.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ parse.py
│     │        │  ├─ py.typed
│     │        │  ├─ schema.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ schema.py
│     │        │  ├─ tools.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ tools.py
│     │        │  ├─ types.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ types.py
│     │        │  ├─ typing.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ typing.py
│     │        │  ├─ utils.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ utils.py
│     │        │  ├─ validators.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ validators.py
│     │        │  ├─ version.cpython-310-x86_64-linux-gnu.so
│     │        │  └─ version.py
│     │        ├─ pydantic-1.10.11.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ pygments
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ cmdline.cpython-310.pyc
│     │        │  │  ├─ console.cpython-310.pyc
│     │        │  │  ├─ filter.cpython-310.pyc
│     │        │  │  ├─ formatter.cpython-310.pyc
│     │        │  │  ├─ lexer.cpython-310.pyc
│     │        │  │  ├─ modeline.cpython-310.pyc
│     │        │  │  ├─ plugin.cpython-310.pyc
│     │        │  │  ├─ regexopt.cpython-310.pyc
│     │        │  │  ├─ scanner.cpython-310.pyc
│     │        │  │  ├─ sphinxext.cpython-310.pyc
│     │        │  │  ├─ style.cpython-310.pyc
│     │        │  │  ├─ token.cpython-310.pyc
│     │        │  │  ├─ unistring.cpython-310.pyc
│     │        │  │  └─ util.cpython-310.pyc
│     │        │  ├─ cmdline.py
│     │        │  ├─ console.py
│     │        │  ├─ filter.py
│     │        │  ├─ filters
│     │        │  │  ├─ __init__.py
│     │        │  │  └─ __pycache__
│     │        │  │     └─ __init__.cpython-310.pyc
│     │        │  ├─ formatter.py
│     │        │  ├─ formatters
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _mapping.cpython-310.pyc
│     │        │  │  │  ├─ bbcode.cpython-310.pyc
│     │        │  │  │  ├─ groff.cpython-310.pyc
│     │        │  │  │  ├─ html.cpython-310.pyc
│     │        │  │  │  ├─ img.cpython-310.pyc
│     │        │  │  │  ├─ irc.cpython-310.pyc
│     │        │  │  │  ├─ latex.cpython-310.pyc
│     │        │  │  │  ├─ other.cpython-310.pyc
│     │        │  │  │  ├─ pangomarkup.cpython-310.pyc
│     │        │  │  │  ├─ rtf.cpython-310.pyc
│     │        │  │  │  ├─ svg.cpython-310.pyc
│     │        │  │  │  ├─ terminal.cpython-310.pyc
│     │        │  │  │  └─ terminal256.cpython-310.pyc
│     │        │  │  ├─ _mapping.py
│     │        │  │  ├─ bbcode.py
│     │        │  │  ├─ groff.py
│     │        │  │  ├─ html.py
│     │        │  │  ├─ img.py
│     │        │  │  ├─ irc.py
│     │        │  │  ├─ latex.py
│     │        │  │  ├─ other.py
│     │        │  │  ├─ pangomarkup.py
│     │        │  │  ├─ rtf.py
│     │        │  │  ├─ svg.py
│     │        │  │  ├─ terminal.py
│     │        │  │  └─ terminal256.py
│     │        │  ├─ lexer.py
│     │        │  ├─ lexers
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _ada_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _asy_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _cl_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _cocoa_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _csound_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _css_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _julia_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _lasso_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _lilypond_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _lua_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _mapping.cpython-310.pyc
│     │        │  │  │  ├─ _mql_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _mysql_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _openedge_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _php_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _postgres_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _qlik_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _scheme_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _scilab_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _sourcemod_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _stan_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _stata_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _tsql_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _usd_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _vbscript_builtins.cpython-310.pyc
│     │        │  │  │  ├─ _vim_builtins.cpython-310.pyc
│     │        │  │  │  ├─ actionscript.cpython-310.pyc
│     │        │  │  │  ├─ ada.cpython-310.pyc
│     │        │  │  │  ├─ agile.cpython-310.pyc
│     │        │  │  │  ├─ algebra.cpython-310.pyc
│     │        │  │  │  ├─ ambient.cpython-310.pyc
│     │        │  │  │  ├─ amdgpu.cpython-310.pyc
│     │        │  │  │  ├─ ampl.cpython-310.pyc
│     │        │  │  │  ├─ apdlexer.cpython-310.pyc
│     │        │  │  │  ├─ apl.cpython-310.pyc
│     │        │  │  │  ├─ archetype.cpython-310.pyc
│     │        │  │  │  ├─ arrow.cpython-310.pyc
│     │        │  │  │  ├─ arturo.cpython-310.pyc
│     │        │  │  │  ├─ asc.cpython-310.pyc
│     │        │  │  │  ├─ asm.cpython-310.pyc
│     │        │  │  │  ├─ automation.cpython-310.pyc
│     │        │  │  │  ├─ bare.cpython-310.pyc
│     │        │  │  │  ├─ basic.cpython-310.pyc
│     │        │  │  │  ├─ bdd.cpython-310.pyc
│     │        │  │  │  ├─ berry.cpython-310.pyc
│     │        │  │  │  ├─ bibtex.cpython-310.pyc
│     │        │  │  │  ├─ boa.cpython-310.pyc
│     │        │  │  │  ├─ business.cpython-310.pyc
│     │        │  │  │  ├─ c_cpp.cpython-310.pyc
│     │        │  │  │  ├─ c_like.cpython-310.pyc
│     │        │  │  │  ├─ capnproto.cpython-310.pyc
│     │        │  │  │  ├─ carbon.cpython-310.pyc
│     │        │  │  │  ├─ cddl.cpython-310.pyc
│     │        │  │  │  ├─ chapel.cpython-310.pyc
│     │        │  │  │  ├─ clean.cpython-310.pyc
│     │        │  │  │  ├─ comal.cpython-310.pyc
│     │        │  │  │  ├─ compiled.cpython-310.pyc
│     │        │  │  │  ├─ configs.cpython-310.pyc
│     │        │  │  │  ├─ console.cpython-310.pyc
│     │        │  │  │  ├─ cplint.cpython-310.pyc
│     │        │  │  │  ├─ crystal.cpython-310.pyc
│     │        │  │  │  ├─ csound.cpython-310.pyc
│     │        │  │  │  ├─ css.cpython-310.pyc
│     │        │  │  │  ├─ d.cpython-310.pyc
│     │        │  │  │  ├─ dalvik.cpython-310.pyc
│     │        │  │  │  ├─ data.cpython-310.pyc
│     │        │  │  │  ├─ dax.cpython-310.pyc
│     │        │  │  │  ├─ devicetree.cpython-310.pyc
│     │        │  │  │  ├─ diff.cpython-310.pyc
│     │        │  │  │  ├─ dotnet.cpython-310.pyc
│     │        │  │  │  ├─ dsls.cpython-310.pyc
│     │        │  │  │  ├─ dylan.cpython-310.pyc
│     │        │  │  │  ├─ ecl.cpython-310.pyc
│     │        │  │  │  ├─ eiffel.cpython-310.pyc
│     │        │  │  │  ├─ elm.cpython-310.pyc
│     │        │  │  │  ├─ elpi.cpython-310.pyc
│     │        │  │  │  ├─ email.cpython-310.pyc
│     │        │  │  │  ├─ erlang.cpython-310.pyc
│     │        │  │  │  ├─ esoteric.cpython-310.pyc
│     │        │  │  │  ├─ ezhil.cpython-310.pyc
│     │        │  │  │  ├─ factor.cpython-310.pyc
│     │        │  │  │  ├─ fantom.cpython-310.pyc
│     │        │  │  │  ├─ felix.cpython-310.pyc
│     │        │  │  │  ├─ fift.cpython-310.pyc
│     │        │  │  │  ├─ floscript.cpython-310.pyc
│     │        │  │  │  ├─ forth.cpython-310.pyc
│     │        │  │  │  ├─ fortran.cpython-310.pyc
│     │        │  │  │  ├─ foxpro.cpython-310.pyc
│     │        │  │  │  ├─ freefem.cpython-310.pyc
│     │        │  │  │  ├─ func.cpython-310.pyc
│     │        │  │  │  ├─ functional.cpython-310.pyc
│     │        │  │  │  ├─ futhark.cpython-310.pyc
│     │        │  │  │  ├─ gcodelexer.cpython-310.pyc
│     │        │  │  │  ├─ gdscript.cpython-310.pyc
│     │        │  │  │  ├─ go.cpython-310.pyc
│     │        │  │  │  ├─ grammar_notation.cpython-310.pyc
│     │        │  │  │  ├─ graph.cpython-310.pyc
│     │        │  │  │  ├─ graphics.cpython-310.pyc
│     │        │  │  │  ├─ graphviz.cpython-310.pyc
│     │        │  │  │  ├─ gsql.cpython-310.pyc
│     │        │  │  │  ├─ haskell.cpython-310.pyc
│     │        │  │  │  ├─ haxe.cpython-310.pyc
│     │        │  │  │  ├─ hdl.cpython-310.pyc
│     │        │  │  │  ├─ hexdump.cpython-310.pyc
│     │        │  │  │  ├─ html.cpython-310.pyc
│     │        │  │  │  ├─ idl.cpython-310.pyc
│     │        │  │  │  ├─ igor.cpython-310.pyc
│     │        │  │  │  ├─ inferno.cpython-310.pyc
│     │        │  │  │  ├─ installers.cpython-310.pyc
│     │        │  │  │  ├─ int_fiction.cpython-310.pyc
│     │        │  │  │  ├─ iolang.cpython-310.pyc
│     │        │  │  │  ├─ j.cpython-310.pyc
│     │        │  │  │  ├─ javascript.cpython-310.pyc
│     │        │  │  │  ├─ jmespath.cpython-310.pyc
│     │        │  │  │  ├─ jslt.cpython-310.pyc
│     │        │  │  │  ├─ jsonnet.cpython-310.pyc
│     │        │  │  │  ├─ julia.cpython-310.pyc
│     │        │  │  │  ├─ jvm.cpython-310.pyc
│     │        │  │  │  ├─ kuin.cpython-310.pyc
│     │        │  │  │  ├─ lilypond.cpython-310.pyc
│     │        │  │  │  ├─ lisp.cpython-310.pyc
│     │        │  │  │  ├─ macaulay2.cpython-310.pyc
│     │        │  │  │  ├─ make.cpython-310.pyc
│     │        │  │  │  ├─ markup.cpython-310.pyc
│     │        │  │  │  ├─ math.cpython-310.pyc
│     │        │  │  │  ├─ matlab.cpython-310.pyc
│     │        │  │  │  ├─ maxima.cpython-310.pyc
│     │        │  │  │  ├─ meson.cpython-310.pyc
│     │        │  │  │  ├─ mime.cpython-310.pyc
│     │        │  │  │  ├─ minecraft.cpython-310.pyc
│     │        │  │  │  ├─ mips.cpython-310.pyc
│     │        │  │  │  ├─ ml.cpython-310.pyc
│     │        │  │  │  ├─ modeling.cpython-310.pyc
│     │        │  │  │  ├─ modula2.cpython-310.pyc
│     │        │  │  │  ├─ monte.cpython-310.pyc
│     │        │  │  │  ├─ mosel.cpython-310.pyc
│     │        │  │  │  ├─ ncl.cpython-310.pyc
│     │        │  │  │  ├─ nimrod.cpython-310.pyc
│     │        │  │  │  ├─ nit.cpython-310.pyc
│     │        │  │  │  ├─ nix.cpython-310.pyc
│     │        │  │  │  ├─ oberon.cpython-310.pyc
│     │        │  │  │  ├─ objective.cpython-310.pyc
│     │        │  │  │  ├─ ooc.cpython-310.pyc
│     │        │  │  │  ├─ other.cpython-310.pyc
│     │        │  │  │  ├─ parasail.cpython-310.pyc
│     │        │  │  │  ├─ parsers.cpython-310.pyc
│     │        │  │  │  ├─ pascal.cpython-310.pyc
│     │        │  │  │  ├─ pawn.cpython-310.pyc
│     │        │  │  │  ├─ perl.cpython-310.pyc
│     │        │  │  │  ├─ phix.cpython-310.pyc
│     │        │  │  │  ├─ php.cpython-310.pyc
│     │        │  │  │  ├─ pointless.cpython-310.pyc
│     │        │  │  │  ├─ pony.cpython-310.pyc
│     │        │  │  │  ├─ praat.cpython-310.pyc
│     │        │  │  │  ├─ procfile.cpython-310.pyc
│     │        │  │  │  ├─ prolog.cpython-310.pyc
│     │        │  │  │  ├─ promql.cpython-310.pyc
│     │        │  │  │  ├─ python.cpython-310.pyc
│     │        │  │  │  ├─ q.cpython-310.pyc
│     │        │  │  │  ├─ qlik.cpython-310.pyc
│     │        │  │  │  ├─ qvt.cpython-310.pyc
│     │        │  │  │  ├─ r.cpython-310.pyc
│     │        │  │  │  ├─ rdf.cpython-310.pyc
│     │        │  │  │  ├─ rebol.cpython-310.pyc
│     │        │  │  │  ├─ resource.cpython-310.pyc
│     │        │  │  │  ├─ ride.cpython-310.pyc
│     │        │  │  │  ├─ rita.cpython-310.pyc
│     │        │  │  │  ├─ rnc.cpython-310.pyc
│     │        │  │  │  ├─ roboconf.cpython-310.pyc
│     │        │  │  │  ├─ robotframework.cpython-310.pyc
│     │        │  │  │  ├─ ruby.cpython-310.pyc
│     │        │  │  │  ├─ rust.cpython-310.pyc
│     │        │  │  │  ├─ sas.cpython-310.pyc
│     │        │  │  │  ├─ savi.cpython-310.pyc
│     │        │  │  │  ├─ scdoc.cpython-310.pyc
│     │        │  │  │  ├─ scripting.cpython-310.pyc
│     │        │  │  │  ├─ sgf.cpython-310.pyc
│     │        │  │  │  ├─ shell.cpython-310.pyc
│     │        │  │  │  ├─ sieve.cpython-310.pyc
│     │        │  │  │  ├─ slash.cpython-310.pyc
│     │        │  │  │  ├─ smalltalk.cpython-310.pyc
│     │        │  │  │  ├─ smithy.cpython-310.pyc
│     │        │  │  │  ├─ smv.cpython-310.pyc
│     │        │  │  │  ├─ snobol.cpython-310.pyc
│     │        │  │  │  ├─ solidity.cpython-310.pyc
│     │        │  │  │  ├─ sophia.cpython-310.pyc
│     │        │  │  │  ├─ special.cpython-310.pyc
│     │        │  │  │  ├─ spice.cpython-310.pyc
│     │        │  │  │  ├─ sql.cpython-310.pyc
│     │        │  │  │  ├─ srcinfo.cpython-310.pyc
│     │        │  │  │  ├─ stata.cpython-310.pyc
│     │        │  │  │  ├─ supercollider.cpython-310.pyc
│     │        │  │  │  ├─ tal.cpython-310.pyc
│     │        │  │  │  ├─ tcl.cpython-310.pyc
│     │        │  │  │  ├─ teal.cpython-310.pyc
│     │        │  │  │  ├─ templates.cpython-310.pyc
│     │        │  │  │  ├─ teraterm.cpython-310.pyc
│     │        │  │  │  ├─ testing.cpython-310.pyc
│     │        │  │  │  ├─ text.cpython-310.pyc
│     │        │  │  │  ├─ textedit.cpython-310.pyc
│     │        │  │  │  ├─ textfmts.cpython-310.pyc
│     │        │  │  │  ├─ theorem.cpython-310.pyc
│     │        │  │  │  ├─ thingsdb.cpython-310.pyc
│     │        │  │  │  ├─ tlb.cpython-310.pyc
│     │        │  │  │  ├─ tnt.cpython-310.pyc
│     │        │  │  │  ├─ trafficscript.cpython-310.pyc
│     │        │  │  │  ├─ typoscript.cpython-310.pyc
│     │        │  │  │  ├─ ul4.cpython-310.pyc
│     │        │  │  │  ├─ unicon.cpython-310.pyc
│     │        │  │  │  ├─ urbi.cpython-310.pyc
│     │        │  │  │  ├─ usd.cpython-310.pyc
│     │        │  │  │  ├─ varnish.cpython-310.pyc
│     │        │  │  │  ├─ verification.cpython-310.pyc
│     │        │  │  │  ├─ web.cpython-310.pyc
│     │        │  │  │  ├─ webassembly.cpython-310.pyc
│     │        │  │  │  ├─ webidl.cpython-310.pyc
│     │        │  │  │  ├─ webmisc.cpython-310.pyc
│     │        │  │  │  ├─ wgsl.cpython-310.pyc
│     │        │  │  │  ├─ whiley.cpython-310.pyc
│     │        │  │  │  ├─ wowtoc.cpython-310.pyc
│     │        │  │  │  ├─ wren.cpython-310.pyc
│     │        │  │  │  ├─ x10.cpython-310.pyc
│     │        │  │  │  ├─ xorg.cpython-310.pyc
│     │        │  │  │  ├─ yang.cpython-310.pyc
│     │        │  │  │  └─ zig.cpython-310.pyc
│     │        │  │  ├─ _ada_builtins.py
│     │        │  │  ├─ _asy_builtins.py
│     │        │  │  ├─ _cl_builtins.py
│     │        │  │  ├─ _cocoa_builtins.py
│     │        │  │  ├─ _csound_builtins.py
│     │        │  │  ├─ _css_builtins.py
│     │        │  │  ├─ _julia_builtins.py
│     │        │  │  ├─ _lasso_builtins.py
│     │        │  │  ├─ _lilypond_builtins.py
│     │        │  │  ├─ _lua_builtins.py
│     │        │  │  ├─ _mapping.py
│     │        │  │  ├─ _mql_builtins.py
│     │        │  │  ├─ _mysql_builtins.py
│     │        │  │  ├─ _openedge_builtins.py
│     │        │  │  ├─ _php_builtins.py
│     │        │  │  ├─ _postgres_builtins.py
│     │        │  │  ├─ _qlik_builtins.py
│     │        │  │  ├─ _scheme_builtins.py
│     │        │  │  ├─ _scilab_builtins.py
│     │        │  │  ├─ _sourcemod_builtins.py
│     │        │  │  ├─ _stan_builtins.py
│     │        │  │  ├─ _stata_builtins.py
│     │        │  │  ├─ _tsql_builtins.py
│     │        │  │  ├─ _usd_builtins.py
│     │        │  │  ├─ _vbscript_builtins.py
│     │        │  │  ├─ _vim_builtins.py
│     │        │  │  ├─ actionscript.py
│     │        │  │  ├─ ada.py
│     │        │  │  ├─ agile.py
│     │        │  │  ├─ algebra.py
│     │        │  │  ├─ ambient.py
│     │        │  │  ├─ amdgpu.py
│     │        │  │  ├─ ampl.py
│     │        │  │  ├─ apdlexer.py
│     │        │  │  ├─ apl.py
│     │        │  │  ├─ archetype.py
│     │        │  │  ├─ arrow.py
│     │        │  │  ├─ arturo.py
│     │        │  │  ├─ asc.py
│     │        │  │  ├─ asm.py
│     │        │  │  ├─ automation.py
│     │        │  │  ├─ bare.py
│     │        │  │  ├─ basic.py
│     │        │  │  ├─ bdd.py
│     │        │  │  ├─ berry.py
│     │        │  │  ├─ bibtex.py
│     │        │  │  ├─ boa.py
│     │        │  │  ├─ business.py
│     │        │  │  ├─ c_cpp.py
│     │        │  │  ├─ c_like.py
│     │        │  │  ├─ capnproto.py
│     │        │  │  ├─ carbon.py
│     │        │  │  ├─ cddl.py
│     │        │  │  ├─ chapel.py
│     │        │  │  ├─ clean.py
│     │        │  │  ├─ comal.py
│     │        │  │  ├─ compiled.py
│     │        │  │  ├─ configs.py
│     │        │  │  ├─ console.py
│     │        │  │  ├─ cplint.py
│     │        │  │  ├─ crystal.py
│     │        │  │  ├─ csound.py
│     │        │  │  ├─ css.py
│     │        │  │  ├─ d.py
│     │        │  │  ├─ dalvik.py
│     │        │  │  ├─ data.py
│     │        │  │  ├─ dax.py
│     │        │  │  ├─ devicetree.py
│     │        │  │  ├─ diff.py
│     │        │  │  ├─ dotnet.py
│     │        │  │  ├─ dsls.py
│     │        │  │  ├─ dylan.py
│     │        │  │  ├─ ecl.py
│     │        │  │  ├─ eiffel.py
│     │        │  │  ├─ elm.py
│     │        │  │  ├─ elpi.py
│     │        │  │  ├─ email.py
│     │        │  │  ├─ erlang.py
│     │        │  │  ├─ esoteric.py
│     │        │  │  ├─ ezhil.py
│     │        │  │  ├─ factor.py
│     │        │  │  ├─ fantom.py
│     │        │  │  ├─ felix.py
│     │        │  │  ├─ fift.py
│     │        │  │  ├─ floscript.py
│     │        │  │  ├─ forth.py
│     │        │  │  ├─ fortran.py
│     │        │  │  ├─ foxpro.py
│     │        │  │  ├─ freefem.py
│     │        │  │  ├─ func.py
│     │        │  │  ├─ functional.py
│     │        │  │  ├─ futhark.py
│     │        │  │  ├─ gcodelexer.py
│     │        │  │  ├─ gdscript.py
│     │        │  │  ├─ go.py
│     │        │  │  ├─ grammar_notation.py
│     │        │  │  ├─ graph.py
│     │        │  │  ├─ graphics.py
│     │        │  │  ├─ graphviz.py
│     │        │  │  ├─ gsql.py
│     │        │  │  ├─ haskell.py
│     │        │  │  ├─ haxe.py
│     │        │  │  ├─ hdl.py
│     │        │  │  ├─ hexdump.py
│     │        │  │  ├─ html.py
│     │        │  │  ├─ idl.py
│     │        │  │  ├─ igor.py
│     │        │  │  ├─ inferno.py
│     │        │  │  ├─ installers.py
│     │        │  │  ├─ int_fiction.py
│     │        │  │  ├─ iolang.py
│     │        │  │  ├─ j.py
│     │        │  │  ├─ javascript.py
│     │        │  │  ├─ jmespath.py
│     │        │  │  ├─ jslt.py
│     │        │  │  ├─ jsonnet.py
│     │        │  │  ├─ julia.py
│     │        │  │  ├─ jvm.py
│     │        │  │  ├─ kuin.py
│     │        │  │  ├─ lilypond.py
│     │        │  │  ├─ lisp.py
│     │        │  │  ├─ macaulay2.py
│     │        │  │  ├─ make.py
│     │        │  │  ├─ markup.py
│     │        │  │  ├─ math.py
│     │        │  │  ├─ matlab.py
│     │        │  │  ├─ maxima.py
│     │        │  │  ├─ meson.py
│     │        │  │  ├─ mime.py
│     │        │  │  ├─ minecraft.py
│     │        │  │  ├─ mips.py
│     │        │  │  ├─ ml.py
│     │        │  │  ├─ modeling.py
│     │        │  │  ├─ modula2.py
│     │        │  │  ├─ monte.py
│     │        │  │  ├─ mosel.py
│     │        │  │  ├─ ncl.py
│     │        │  │  ├─ nimrod.py
│     │        │  │  ├─ nit.py
│     │        │  │  ├─ nix.py
│     │        │  │  ├─ oberon.py
│     │        │  │  ├─ objective.py
│     │        │  │  ├─ ooc.py
│     │        │  │  ├─ other.py
│     │        │  │  ├─ parasail.py
│     │        │  │  ├─ parsers.py
│     │        │  │  ├─ pascal.py
│     │        │  │  ├─ pawn.py
│     │        │  │  ├─ perl.py
│     │        │  │  ├─ phix.py
│     │        │  │  ├─ php.py
│     │        │  │  ├─ pointless.py
│     │        │  │  ├─ pony.py
│     │        │  │  ├─ praat.py
│     │        │  │  ├─ procfile.py
│     │        │  │  ├─ prolog.py
│     │        │  │  ├─ promql.py
│     │        │  │  ├─ python.py
│     │        │  │  ├─ q.py
│     │        │  │  ├─ qlik.py
│     │        │  │  ├─ qvt.py
│     │        │  │  ├─ r.py
│     │        │  │  ├─ rdf.py
│     │        │  │  ├─ rebol.py
│     │        │  │  ├─ resource.py
│     │        │  │  ├─ ride.py
│     │        │  │  ├─ rita.py
│     │        │  │  ├─ rnc.py
│     │        │  │  ├─ roboconf.py
│     │        │  │  ├─ robotframework.py
│     │        │  │  ├─ ruby.py
│     │        │  │  ├─ rust.py
│     │        │  │  ├─ sas.py
│     │        │  │  ├─ savi.py
│     │        │  │  ├─ scdoc.py
│     │        │  │  ├─ scripting.py
│     │        │  │  ├─ sgf.py
│     │        │  │  ├─ shell.py
│     │        │  │  ├─ sieve.py
│     │        │  │  ├─ slash.py
│     │        │  │  ├─ smalltalk.py
│     │        │  │  ├─ smithy.py
│     │        │  │  ├─ smv.py
│     │        │  │  ├─ snobol.py
│     │        │  │  ├─ solidity.py
│     │        │  │  ├─ sophia.py
│     │        │  │  ├─ special.py
│     │        │  │  ├─ spice.py
│     │        │  │  ├─ sql.py
│     │        │  │  ├─ srcinfo.py
│     │        │  │  ├─ stata.py
│     │        │  │  ├─ supercollider.py
│     │        │  │  ├─ tal.py
│     │        │  │  ├─ tcl.py
│     │        │  │  ├─ teal.py
│     │        │  │  ├─ templates.py
│     │        │  │  ├─ teraterm.py
│     │        │  │  ├─ testing.py
│     │        │  │  ├─ text.py
│     │        │  │  ├─ textedit.py
│     │        │  │  ├─ textfmts.py
│     │        │  │  ├─ theorem.py
│     │        │  │  ├─ thingsdb.py
│     │        │  │  ├─ tlb.py
│     │        │  │  ├─ tnt.py
│     │        │  │  ├─ trafficscript.py
│     │        │  │  ├─ typoscript.py
│     │        │  │  ├─ ul4.py
│     │        │  │  ├─ unicon.py
│     │        │  │  ├─ urbi.py
│     │        │  │  ├─ usd.py
│     │        │  │  ├─ varnish.py
│     │        │  │  ├─ verification.py
│     │        │  │  ├─ web.py
│     │        │  │  ├─ webassembly.py
│     │        │  │  ├─ webidl.py
│     │        │  │  ├─ webmisc.py
│     │        │  │  ├─ wgsl.py
│     │        │  │  ├─ whiley.py
│     │        │  │  ├─ wowtoc.py
│     │        │  │  ├─ wren.py
│     │        │  │  ├─ x10.py
│     │        │  │  ├─ xorg.py
│     │        │  │  ├─ yang.py
│     │        │  │  └─ zig.py
│     │        │  ├─ modeline.py
│     │        │  ├─ plugin.py
│     │        │  ├─ regexopt.py
│     │        │  ├─ scanner.py
│     │        │  ├─ sphinxext.py
│     │        │  ├─ style.py
│     │        │  ├─ styles
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ abap.cpython-310.pyc
│     │        │  │  │  ├─ algol.cpython-310.pyc
│     │        │  │  │  ├─ algol_nu.cpython-310.pyc
│     │        │  │  │  ├─ arduino.cpython-310.pyc
│     │        │  │  │  ├─ autumn.cpython-310.pyc
│     │        │  │  │  ├─ borland.cpython-310.pyc
│     │        │  │  │  ├─ bw.cpython-310.pyc
│     │        │  │  │  ├─ colorful.cpython-310.pyc
│     │        │  │  │  ├─ default.cpython-310.pyc
│     │        │  │  │  ├─ dracula.cpython-310.pyc
│     │        │  │  │  ├─ emacs.cpython-310.pyc
│     │        │  │  │  ├─ friendly.cpython-310.pyc
│     │        │  │  │  ├─ friendly_grayscale.cpython-310.pyc
│     │        │  │  │  ├─ fruity.cpython-310.pyc
│     │        │  │  │  ├─ gh_dark.cpython-310.pyc
│     │        │  │  │  ├─ gruvbox.cpython-310.pyc
│     │        │  │  │  ├─ igor.cpython-310.pyc
│     │        │  │  │  ├─ inkpot.cpython-310.pyc
│     │        │  │  │  ├─ lilypond.cpython-310.pyc
│     │        │  │  │  ├─ lovelace.cpython-310.pyc
│     │        │  │  │  ├─ manni.cpython-310.pyc
│     │        │  │  │  ├─ material.cpython-310.pyc
│     │        │  │  │  ├─ monokai.cpython-310.pyc
│     │        │  │  │  ├─ murphy.cpython-310.pyc
│     │        │  │  │  ├─ native.cpython-310.pyc
│     │        │  │  │  ├─ nord.cpython-310.pyc
│     │        │  │  │  ├─ onedark.cpython-310.pyc
│     │        │  │  │  ├─ paraiso_dark.cpython-310.pyc
│     │        │  │  │  ├─ paraiso_light.cpython-310.pyc
│     │        │  │  │  ├─ pastie.cpython-310.pyc
│     │        │  │  │  ├─ perldoc.cpython-310.pyc
│     │        │  │  │  ├─ rainbow_dash.cpython-310.pyc
│     │        │  │  │  ├─ rrt.cpython-310.pyc
│     │        │  │  │  ├─ sas.cpython-310.pyc
│     │        │  │  │  ├─ solarized.cpython-310.pyc
│     │        │  │  │  ├─ staroffice.cpython-310.pyc
│     │        │  │  │  ├─ stata_dark.cpython-310.pyc
│     │        │  │  │  ├─ stata_light.cpython-310.pyc
│     │        │  │  │  ├─ tango.cpython-310.pyc
│     │        │  │  │  ├─ trac.cpython-310.pyc
│     │        │  │  │  ├─ vim.cpython-310.pyc
│     │        │  │  │  ├─ vs.cpython-310.pyc
│     │        │  │  │  ├─ xcode.cpython-310.pyc
│     │        │  │  │  └─ zenburn.cpython-310.pyc
│     │        │  │  ├─ abap.py
│     │        │  │  ├─ algol.py
│     │        │  │  ├─ algol_nu.py
│     │        │  │  ├─ arduino.py
│     │        │  │  ├─ autumn.py
│     │        │  │  ├─ borland.py
│     │        │  │  ├─ bw.py
│     │        │  │  ├─ colorful.py
│     │        │  │  ├─ default.py
│     │        │  │  ├─ dracula.py
│     │        │  │  ├─ emacs.py
│     │        │  │  ├─ friendly.py
│     │        │  │  ├─ friendly_grayscale.py
│     │        │  │  ├─ fruity.py
│     │        │  │  ├─ gh_dark.py
│     │        │  │  ├─ gruvbox.py
│     │        │  │  ├─ igor.py
│     │        │  │  ├─ inkpot.py
│     │        │  │  ├─ lilypond.py
│     │        │  │  ├─ lovelace.py
│     │        │  │  ├─ manni.py
│     │        │  │  ├─ material.py
│     │        │  │  ├─ monokai.py
│     │        │  │  ├─ murphy.py
│     │        │  │  ├─ native.py
│     │        │  │  ├─ nord.py
│     │        │  │  ├─ onedark.py
│     │        │  │  ├─ paraiso_dark.py
│     │        │  │  ├─ paraiso_light.py
│     │        │  │  ├─ pastie.py
│     │        │  │  ├─ perldoc.py
│     │        │  │  ├─ rainbow_dash.py
│     │        │  │  ├─ rrt.py
│     │        │  │  ├─ sas.py
│     │        │  │  ├─ solarized.py
│     │        │  │  ├─ staroffice.py
│     │        │  │  ├─ stata_dark.py
│     │        │  │  ├─ stata_light.py
│     │        │  │  ├─ tango.py
│     │        │  │  ├─ trac.py
│     │        │  │  ├─ vim.py
│     │        │  │  ├─ vs.py
│     │        │  │  ├─ xcode.py
│     │        │  │  └─ zenburn.py
│     │        │  ├─ token.py
│     │        │  ├─ unistring.py
│     │        │  └─ util.py
│     │        ├─ pytest
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  └─ __main__.cpython-310.pyc
│     │        │  └─ py.typed
│     │        ├─ pytest-7.4.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ pytest_asyncio
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  ├─ plugin.cpython-310-pytest-7.4.0.pyc
│     │        │  │  └─ plugin.cpython-310.pyc
│     │        │  ├─ _version.py
│     │        │  ├─ plugin.py
│     │        │  └─ py.typed
│     │        ├─ pytest_asyncio-0.21.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ pytest_html
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __version.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ __version.cpython-310.pyc
│     │        │  │  ├─ extras.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ extras.cpython-310.pyc
│     │        │  │  ├─ html_report.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ html_report.cpython-310.pyc
│     │        │  │  ├─ outcome.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ outcome.cpython-310.pyc
│     │        │  │  ├─ plugin.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ plugin.cpython-310.pyc
│     │        │  │  ├─ result.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ result.cpython-310.pyc
│     │        │  │  ├─ util.cpython-310-pytest-7.4.0.pyc
│     │        │  │  └─ util.cpython-310.pyc
│     │        │  ├─ __version.py
│     │        │  ├─ extras.py
│     │        │  ├─ html_report.py
│     │        │  ├─ outcome.py
│     │        │  ├─ plugin.py
│     │        │  ├─ resources
│     │        │  │  ├─ main.js
│     │        │  │  └─ style.css
│     │        │  ├─ result.py
│     │        │  └─ util.py
│     │        ├─ pytest_html-3.2.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ pytest_metadata
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __version.cpython-310.pyc
│     │        │  │  ├─ plugin.cpython-310-pytest-7.4.0.pyc
│     │        │  │  └─ plugin.cpython-310.pyc
│     │        │  ├─ __version.py
│     │        │  ├─ ci
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ appveyor.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ appveyor.cpython-310.pyc
│     │        │  │  │  ├─ bitbucket.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ bitbucket.cpython-310.pyc
│     │        │  │  │  ├─ circleci.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ circleci.cpython-310.pyc
│     │        │  │  │  ├─ gitlab_ci.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ gitlab_ci.cpython-310.pyc
│     │        │  │  │  ├─ jenkins.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ jenkins.cpython-310.pyc
│     │        │  │  │  ├─ taskcluster.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  ├─ taskcluster.cpython-310.pyc
│     │        │  │  │  ├─ travis_ci.cpython-310-pytest-7.4.0.pyc
│     │        │  │  │  └─ travis_ci.cpython-310.pyc
│     │        │  │  ├─ appveyor.py
│     │        │  │  ├─ bitbucket.py
│     │        │  │  ├─ circleci.py
│     │        │  │  ├─ gitlab_ci.py
│     │        │  │  ├─ jenkins.py
│     │        │  │  ├─ taskcluster.py
│     │        │  │  └─ travis_ci.py
│     │        │  └─ plugin.py
│     │        ├─ pytest_metadata-3.0.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ licenses
│     │        │     ├─ AUTHORS
│     │        │     └─ LICENSE
│     │        ├─ pytest_mock
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _util.cpython-310-pytest-7.4.0.pyc
│     │        │  │  ├─ _util.cpython-310.pyc
│     │        │  │  ├─ _version.cpython-310.pyc
│     │        │  │  ├─ plugin.cpython-310-pytest-7.4.0.pyc
│     │        │  │  └─ plugin.cpython-310.pyc
│     │        │  ├─ _util.py
│     │        │  ├─ _version.py
│     │        │  ├─ plugin.py
│     │        │  └─ py.typed
│     │        ├─ pytest_mock-3.11.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ python_dateutil-2.8.2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ top_level.txt
│     │        │  └─ zip-safe
│     │        ├─ python_decouple-3.8.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ python_dotenv-1.0.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ rich
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ _cell_widths.cpython-310.pyc
│     │        │  │  ├─ _emoji_codes.cpython-310.pyc
│     │        │  │  ├─ _emoji_replace.cpython-310.pyc
│     │        │  │  ├─ _export_format.cpython-310.pyc
│     │        │  │  ├─ _extension.cpython-310.pyc
│     │        │  │  ├─ _fileno.cpython-310.pyc
│     │        │  │  ├─ _inspect.cpython-310.pyc
│     │        │  │  ├─ _log_render.cpython-310.pyc
│     │        │  │  ├─ _loop.cpython-310.pyc
│     │        │  │  ├─ _null_file.cpython-310.pyc
│     │        │  │  ├─ _palettes.cpython-310.pyc
│     │        │  │  ├─ _pick.cpython-310.pyc
│     │        │  │  ├─ _ratio.cpython-310.pyc
│     │        │  │  ├─ _spinners.cpython-310.pyc
│     │        │  │  ├─ _stack.cpython-310.pyc
│     │        │  │  ├─ _timer.cpython-310.pyc
│     │        │  │  ├─ _win32_console.cpython-310.pyc
│     │        │  │  ├─ _windows.cpython-310.pyc
│     │        │  │  ├─ _windows_renderer.cpython-310.pyc
│     │        │  │  ├─ _wrap.cpython-310.pyc
│     │        │  │  ├─ abc.cpython-310.pyc
│     │        │  │  ├─ align.cpython-310.pyc
│     │        │  │  ├─ ansi.cpython-310.pyc
│     │        │  │  ├─ bar.cpython-310.pyc
│     │        │  │  ├─ box.cpython-310.pyc
│     │        │  │  ├─ cells.cpython-310.pyc
│     │        │  │  ├─ color.cpython-310.pyc
│     │        │  │  ├─ color_triplet.cpython-310.pyc
│     │        │  │  ├─ columns.cpython-310.pyc
│     │        │  │  ├─ console.cpython-310.pyc
│     │        │  │  ├─ constrain.cpython-310.pyc
│     │        │  │  ├─ containers.cpython-310.pyc
│     │        │  │  ├─ control.cpython-310.pyc
│     │        │  │  ├─ default_styles.cpython-310.pyc
│     │        │  │  ├─ diagnose.cpython-310.pyc
│     │        │  │  ├─ emoji.cpython-310.pyc
│     │        │  │  ├─ errors.cpython-310.pyc
│     │        │  │  ├─ file_proxy.cpython-310.pyc
│     │        │  │  ├─ filesize.cpython-310.pyc
│     │        │  │  ├─ highlighter.cpython-310.pyc
│     │        │  │  ├─ json.cpython-310.pyc
│     │        │  │  ├─ jupyter.cpython-310.pyc
│     │        │  │  ├─ layout.cpython-310.pyc
│     │        │  │  ├─ live.cpython-310.pyc
│     │        │  │  ├─ live_render.cpython-310.pyc
│     │        │  │  ├─ logging.cpython-310.pyc
│     │        │  │  ├─ markdown.cpython-310.pyc
│     │        │  │  ├─ markup.cpython-310.pyc
│     │        │  │  ├─ measure.cpython-310.pyc
│     │        │  │  ├─ padding.cpython-310.pyc
│     │        │  │  ├─ pager.cpython-310.pyc
│     │        │  │  ├─ palette.cpython-310.pyc
│     │        │  │  ├─ panel.cpython-310.pyc
│     │        │  │  ├─ pretty.cpython-310.pyc
│     │        │  │  ├─ progress.cpython-310.pyc
│     │        │  │  ├─ progress_bar.cpython-310.pyc
│     │        │  │  ├─ prompt.cpython-310.pyc
│     │        │  │  ├─ protocol.cpython-310.pyc
│     │        │  │  ├─ region.cpython-310.pyc
│     │        │  │  ├─ repr.cpython-310.pyc
│     │        │  │  ├─ rule.cpython-310.pyc
│     │        │  │  ├─ scope.cpython-310.pyc
│     │        │  │  ├─ screen.cpython-310.pyc
│     │        │  │  ├─ segment.cpython-310.pyc
│     │        │  │  ├─ spinner.cpython-310.pyc
│     │        │  │  ├─ status.cpython-310.pyc
│     │        │  │  ├─ style.cpython-310.pyc
│     │        │  │  ├─ styled.cpython-310.pyc
│     │        │  │  ├─ syntax.cpython-310.pyc
│     │        │  │  ├─ table.cpython-310.pyc
│     │        │  │  ├─ terminal_theme.cpython-310.pyc
│     │        │  │  ├─ text.cpython-310.pyc
│     │        │  │  ├─ theme.cpython-310.pyc
│     │        │  │  ├─ themes.cpython-310.pyc
│     │        │  │  ├─ traceback.cpython-310.pyc
│     │        │  │  └─ tree.cpython-310.pyc
│     │        │  ├─ _cell_widths.py
│     │        │  ├─ _emoji_codes.py
│     │        │  ├─ _emoji_replace.py
│     │        │  ├─ _export_format.py
│     │        │  ├─ _extension.py
│     │        │  ├─ _fileno.py
│     │        │  ├─ _inspect.py
│     │        │  ├─ _log_render.py
│     │        │  ├─ _loop.py
│     │        │  ├─ _null_file.py
│     │        │  ├─ _palettes.py
│     │        │  ├─ _pick.py
│     │        │  ├─ _ratio.py
│     │        │  ├─ _spinners.py
│     │        │  ├─ _stack.py
│     │        │  ├─ _timer.py
│     │        │  ├─ _win32_console.py
│     │        │  ├─ _windows.py
│     │        │  ├─ _windows_renderer.py
│     │        │  ├─ _wrap.py
│     │        │  ├─ abc.py
│     │        │  ├─ align.py
│     │        │  ├─ ansi.py
│     │        │  ├─ bar.py
│     │        │  ├─ box.py
│     │        │  ├─ cells.py
│     │        │  ├─ color.py
│     │        │  ├─ color_triplet.py
│     │        │  ├─ columns.py
│     │        │  ├─ console.py
│     │        │  ├─ constrain.py
│     │        │  ├─ containers.py
│     │        │  ├─ control.py
│     │        │  ├─ default_styles.py
│     │        │  ├─ diagnose.py
│     │        │  ├─ emoji.py
│     │        │  ├─ errors.py
│     │        │  ├─ file_proxy.py
│     │        │  ├─ filesize.py
│     │        │  ├─ highlighter.py
│     │        │  ├─ json.py
│     │        │  ├─ jupyter.py
│     │        │  ├─ layout.py
│     │        │  ├─ live.py
│     │        │  ├─ live_render.py
│     │        │  ├─ logging.py
│     │        │  ├─ markdown.py
│     │        │  ├─ markup.py
│     │        │  ├─ measure.py
│     │        │  ├─ padding.py
│     │        │  ├─ pager.py
│     │        │  ├─ palette.py
│     │        │  ├─ panel.py
│     │        │  ├─ pretty.py
│     │        │  ├─ progress.py
│     │        │  ├─ progress_bar.py
│     │        │  ├─ prompt.py
│     │        │  ├─ protocol.py
│     │        │  ├─ py.typed
│     │        │  ├─ region.py
│     │        │  ├─ repr.py
│     │        │  ├─ rule.py
│     │        │  ├─ scope.py
│     │        │  ├─ screen.py
│     │        │  ├─ segment.py
│     │        │  ├─ spinner.py
│     │        │  ├─ status.py
│     │        │  ├─ style.py
│     │        │  ├─ styled.py
│     │        │  ├─ syntax.py
│     │        │  ├─ table.py
│     │        │  ├─ terminal_theme.py
│     │        │  ├─ text.py
│     │        │  ├─ theme.py
│     │        │  ├─ themes.py
│     │        │  ├─ traceback.py
│     │        │  └─ tree.py
│     │        ├─ rich-13.4.2.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ rich_click
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ cli.cpython-310.pyc
│     │        │  │  ├─ rich_click.cpython-310.pyc
│     │        │  │  ├─ rich_command.cpython-310.pyc
│     │        │  │  └─ rich_group.cpython-310.pyc
│     │        │  ├─ cli.py
│     │        │  ├─ py.typed
│     │        │  ├─ rich_click.py
│     │        │  ├─ rich_command.py
│     │        │  └─ rich_group.py
│     │        ├─ rich_click-1.6.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ ruff
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  └─ __pycache__
│     │        │     ├─ __init__.cpython-310.pyc
│     │        │     └─ __main__.cpython-310.pyc
│     │        ├─ ruff-0.0.277.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ license_files
│     │        │     └─ LICENSE
│     │        ├─ setuptools
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _deprecation_warning.cpython-310.pyc
│     │        │  │  ├─ _imp.cpython-310.pyc
│     │        │  │  ├─ archive_util.cpython-310.pyc
│     │        │  │  ├─ build_meta.cpython-310.pyc
│     │        │  │  ├─ config.cpython-310.pyc
│     │        │  │  ├─ dep_util.cpython-310.pyc
│     │        │  │  ├─ depends.cpython-310.pyc
│     │        │  │  ├─ dist.cpython-310.pyc
│     │        │  │  ├─ errors.cpython-310.pyc
│     │        │  │  ├─ extension.cpython-310.pyc
│     │        │  │  ├─ glob.cpython-310.pyc
│     │        │  │  ├─ installer.cpython-310.pyc
│     │        │  │  ├─ launch.cpython-310.pyc
│     │        │  │  ├─ monkey.cpython-310.pyc
│     │        │  │  ├─ msvc.cpython-310.pyc
│     │        │  │  ├─ namespaces.cpython-310.pyc
│     │        │  │  ├─ package_index.cpython-310.pyc
│     │        │  │  ├─ py34compat.cpython-310.pyc
│     │        │  │  ├─ sandbox.cpython-310.pyc
│     │        │  │  ├─ unicode_utils.cpython-310.pyc
│     │        │  │  ├─ version.cpython-310.pyc
│     │        │  │  ├─ wheel.cpython-310.pyc
│     │        │  │  └─ windows_support.cpython-310.pyc
│     │        │  ├─ _deprecation_warning.py
│     │        │  ├─ _distutils
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _msvccompiler.cpython-310.pyc
│     │        │  │  │  ├─ archive_util.cpython-310.pyc
│     │        │  │  │  ├─ bcppcompiler.cpython-310.pyc
│     │        │  │  │  ├─ ccompiler.cpython-310.pyc
│     │        │  │  │  ├─ cmd.cpython-310.pyc
│     │        │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  ├─ core.cpython-310.pyc
│     │        │  │  │  ├─ cygwinccompiler.cpython-310.pyc
│     │        │  │  │  ├─ debug.cpython-310.pyc
│     │        │  │  │  ├─ dep_util.cpython-310.pyc
│     │        │  │  │  ├─ dir_util.cpython-310.pyc
│     │        │  │  │  ├─ dist.cpython-310.pyc
│     │        │  │  │  ├─ errors.cpython-310.pyc
│     │        │  │  │  ├─ extension.cpython-310.pyc
│     │        │  │  │  ├─ fancy_getopt.cpython-310.pyc
│     │        │  │  │  ├─ file_util.cpython-310.pyc
│     │        │  │  │  ├─ filelist.cpython-310.pyc
│     │        │  │  │  ├─ log.cpython-310.pyc
│     │        │  │  │  ├─ msvc9compiler.cpython-310.pyc
│     │        │  │  │  ├─ msvccompiler.cpython-310.pyc
│     │        │  │  │  ├─ py35compat.cpython-310.pyc
│     │        │  │  │  ├─ py38compat.cpython-310.pyc
│     │        │  │  │  ├─ spawn.cpython-310.pyc
│     │        │  │  │  ├─ sysconfig.cpython-310.pyc
│     │        │  │  │  ├─ text_file.cpython-310.pyc
│     │        │  │  │  ├─ unixccompiler.cpython-310.pyc
│     │        │  │  │  ├─ util.cpython-310.pyc
│     │        │  │  │  ├─ version.cpython-310.pyc
│     │        │  │  │  └─ versionpredicate.cpython-310.pyc
│     │        │  │  ├─ _msvccompiler.py
│     │        │  │  ├─ archive_util.py
│     │        │  │  ├─ bcppcompiler.py
│     │        │  │  ├─ ccompiler.py
│     │        │  │  ├─ cmd.py
│     │        │  │  ├─ command
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ bdist.cpython-310.pyc
│     │        │  │  │  │  ├─ bdist_dumb.cpython-310.pyc
│     │        │  │  │  │  ├─ bdist_msi.cpython-310.pyc
│     │        │  │  │  │  ├─ bdist_rpm.cpython-310.pyc
│     │        │  │  │  │  ├─ bdist_wininst.cpython-310.pyc
│     │        │  │  │  │  ├─ build.cpython-310.pyc
│     │        │  │  │  │  ├─ build_clib.cpython-310.pyc
│     │        │  │  │  │  ├─ build_ext.cpython-310.pyc
│     │        │  │  │  │  ├─ build_py.cpython-310.pyc
│     │        │  │  │  │  ├─ build_scripts.cpython-310.pyc
│     │        │  │  │  │  ├─ check.cpython-310.pyc
│     │        │  │  │  │  ├─ clean.cpython-310.pyc
│     │        │  │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  │  ├─ install.cpython-310.pyc
│     │        │  │  │  │  ├─ install_data.cpython-310.pyc
│     │        │  │  │  │  ├─ install_egg_info.cpython-310.pyc
│     │        │  │  │  │  ├─ install_headers.cpython-310.pyc
│     │        │  │  │  │  ├─ install_lib.cpython-310.pyc
│     │        │  │  │  │  ├─ install_scripts.cpython-310.pyc
│     │        │  │  │  │  ├─ py37compat.cpython-310.pyc
│     │        │  │  │  │  ├─ register.cpython-310.pyc
│     │        │  │  │  │  ├─ sdist.cpython-310.pyc
│     │        │  │  │  │  └─ upload.cpython-310.pyc
│     │        │  │  │  ├─ bdist.py
│     │        │  │  │  ├─ bdist_dumb.py
│     │        │  │  │  ├─ bdist_msi.py
│     │        │  │  │  ├─ bdist_rpm.py
│     │        │  │  │  ├─ bdist_wininst.py
│     │        │  │  │  ├─ build.py
│     │        │  │  │  ├─ build_clib.py
│     │        │  │  │  ├─ build_ext.py
│     │        │  │  │  ├─ build_py.py
│     │        │  │  │  ├─ build_scripts.py
│     │        │  │  │  ├─ check.py
│     │        │  │  │  ├─ clean.py
│     │        │  │  │  ├─ config.py
│     │        │  │  │  ├─ install.py
│     │        │  │  │  ├─ install_data.py
│     │        │  │  │  ├─ install_egg_info.py
│     │        │  │  │  ├─ install_headers.py
│     │        │  │  │  ├─ install_lib.py
│     │        │  │  │  ├─ install_scripts.py
│     │        │  │  │  ├─ py37compat.py
│     │        │  │  │  ├─ register.py
│     │        │  │  │  ├─ sdist.py
│     │        │  │  │  └─ upload.py
│     │        │  │  ├─ config.py
│     │        │  │  ├─ core.py
│     │        │  │  ├─ cygwinccompiler.py
│     │        │  │  ├─ debug.py
│     │        │  │  ├─ dep_util.py
│     │        │  │  ├─ dir_util.py
│     │        │  │  ├─ dist.py
│     │        │  │  ├─ errors.py
│     │        │  │  ├─ extension.py
│     │        │  │  ├─ fancy_getopt.py
│     │        │  │  ├─ file_util.py
│     │        │  │  ├─ filelist.py
│     │        │  │  ├─ log.py
│     │        │  │  ├─ msvc9compiler.py
│     │        │  │  ├─ msvccompiler.py
│     │        │  │  ├─ py35compat.py
│     │        │  │  ├─ py38compat.py
│     │        │  │  ├─ spawn.py
│     │        │  │  ├─ sysconfig.py
│     │        │  │  ├─ text_file.py
│     │        │  │  ├─ unixccompiler.py
│     │        │  │  ├─ util.py
│     │        │  │  ├─ version.py
│     │        │  │  └─ versionpredicate.py
│     │        │  ├─ _imp.py
│     │        │  ├─ _vendor
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ ordered_set.cpython-310.pyc
│     │        │  │  │  └─ pyparsing.cpython-310.pyc
│     │        │  │  ├─ more_itertools
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ more.cpython-310.pyc
│     │        │  │  │  │  └─ recipes.cpython-310.pyc
│     │        │  │  │  ├─ more.py
│     │        │  │  │  └─ recipes.py
│     │        │  │  ├─ ordered_set.py
│     │        │  │  ├─ packaging
│     │        │  │  │  ├─ __about__.py
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __about__.cpython-310.pyc
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _manylinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _musllinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _structures.cpython-310.pyc
│     │        │  │  │  │  ├─ markers.cpython-310.pyc
│     │        │  │  │  │  ├─ requirements.cpython-310.pyc
│     │        │  │  │  │  ├─ specifiers.cpython-310.pyc
│     │        │  │  │  │  ├─ tags.cpython-310.pyc
│     │        │  │  │  │  ├─ utils.cpython-310.pyc
│     │        │  │  │  │  └─ version.cpython-310.pyc
│     │        │  │  │  ├─ _manylinux.py
│     │        │  │  │  ├─ _musllinux.py
│     │        │  │  │  ├─ _structures.py
│     │        │  │  │  ├─ markers.py
│     │        │  │  │  ├─ requirements.py
│     │        │  │  │  ├─ specifiers.py
│     │        │  │  │  ├─ tags.py
│     │        │  │  │  ├─ utils.py
│     │        │  │  │  └─ version.py
│     │        │  │  └─ pyparsing.py
│     │        │  ├─ archive_util.py
│     │        │  ├─ build_meta.py
│     │        │  ├─ cli-32.exe
│     │        │  ├─ cli-64.exe
│     │        │  ├─ cli-arm64.exe
│     │        │  ├─ cli.exe
│     │        │  ├─ command
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ alias.cpython-310.pyc
│     │        │  │  │  ├─ bdist_egg.cpython-310.pyc
│     │        │  │  │  ├─ bdist_rpm.cpython-310.pyc
│     │        │  │  │  ├─ build_clib.cpython-310.pyc
│     │        │  │  │  ├─ build_ext.cpython-310.pyc
│     │        │  │  │  ├─ build_py.cpython-310.pyc
│     │        │  │  │  ├─ develop.cpython-310.pyc
│     │        │  │  │  ├─ dist_info.cpython-310.pyc
│     │        │  │  │  ├─ easy_install.cpython-310.pyc
│     │        │  │  │  ├─ egg_info.cpython-310.pyc
│     │        │  │  │  ├─ install.cpython-310.pyc
│     │        │  │  │  ├─ install_egg_info.cpython-310.pyc
│     │        │  │  │  ├─ install_lib.cpython-310.pyc
│     │        │  │  │  ├─ install_scripts.cpython-310.pyc
│     │        │  │  │  ├─ py36compat.cpython-310.pyc
│     │        │  │  │  ├─ register.cpython-310.pyc
│     │        │  │  │  ├─ rotate.cpython-310.pyc
│     │        │  │  │  ├─ saveopts.cpython-310.pyc
│     │        │  │  │  ├─ sdist.cpython-310.pyc
│     │        │  │  │  ├─ setopt.cpython-310.pyc
│     │        │  │  │  ├─ test.cpython-310.pyc
│     │        │  │  │  ├─ upload.cpython-310.pyc
│     │        │  │  │  └─ upload_docs.cpython-310.pyc
│     │        │  │  ├─ alias.py
│     │        │  │  ├─ bdist_egg.py
│     │        │  │  ├─ bdist_rpm.py
│     │        │  │  ├─ build_clib.py
│     │        │  │  ├─ build_ext.py
│     │        │  │  ├─ build_py.py
│     │        │  │  ├─ develop.py
│     │        │  │  ├─ dist_info.py
│     │        │  │  ├─ easy_install.py
│     │        │  │  ├─ egg_info.py
│     │        │  │  ├─ install.py
│     │        │  │  ├─ install_egg_info.py
│     │        │  │  ├─ install_lib.py
│     │        │  │  ├─ install_scripts.py
│     │        │  │  ├─ launcher manifest.xml
│     │        │  │  ├─ py36compat.py
│     │        │  │  ├─ register.py
│     │        │  │  ├─ rotate.py
│     │        │  │  ├─ saveopts.py
│     │        │  │  ├─ sdist.py
│     │        │  │  ├─ setopt.py
│     │        │  │  ├─ test.py
│     │        │  │  ├─ upload.py
│     │        │  │  └─ upload_docs.py
│     │        │  ├─ config.py
│     │        │  ├─ dep_util.py
│     │        │  ├─ depends.py
│     │        │  ├─ dist.py
│     │        │  ├─ errors.py
│     │        │  ├─ extension.py
│     │        │  ├─ extern
│     │        │  │  ├─ __init__.py
│     │        │  │  └─ __pycache__
│     │        │  │     └─ __init__.cpython-310.pyc
│     │        │  ├─ glob.py
│     │        │  ├─ gui-32.exe
│     │        │  ├─ gui-64.exe
│     │        │  ├─ gui-arm64.exe
│     │        │  ├─ gui.exe
│     │        │  ├─ installer.py
│     │        │  ├─ launch.py
│     │        │  ├─ monkey.py
│     │        │  ├─ msvc.py
│     │        │  ├─ namespaces.py
│     │        │  ├─ package_index.py
│     │        │  ├─ py34compat.py
│     │        │  ├─ sandbox.py
│     │        │  ├─ script (dev).tmpl
│     │        │  ├─ script.tmpl
│     │        │  ├─ unicode_utils.py
│     │        │  ├─ version.py
│     │        │  ├─ wheel.py
│     │        │  └─ windows_support.py
│     │        ├─ setuptools-59.6.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ six-1.16.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ six.py
│     │        ├─ sniffio
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _impl.cpython-310.pyc
│     │        │  │  └─ _version.cpython-310.pyc
│     │        │  ├─ _impl.py
│     │        │  ├─ _tests
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ test_sniffio.cpython-310.pyc
│     │        │  │  └─ test_sniffio.py
│     │        │  ├─ _version.py
│     │        │  └─ py.typed
│     │        ├─ sniffio-1.3.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ LICENSE.APACHE2
│     │        │  ├─ LICENSE.MIT
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ sqlalchemy
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ events.cpython-310.pyc
│     │        │  │  ├─ exc.cpython-310.pyc
│     │        │  │  ├─ inspection.cpython-310.pyc
│     │        │  │  ├─ log.cpython-310.pyc
│     │        │  │  ├─ schema.cpython-310.pyc
│     │        │  │  └─ types.cpython-310.pyc
│     │        │  ├─ connectors
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ pyodbc.cpython-310.pyc
│     │        │  │  └─ pyodbc.py
│     │        │  ├─ cyextension
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ collections.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ collections.pyx
│     │        │  │  ├─ immutabledict.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ immutabledict.pxd
│     │        │  │  ├─ immutabledict.pyx
│     │        │  │  ├─ processors.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ processors.pyx
│     │        │  │  ├─ resultproxy.cpython-310-x86_64-linux-gnu.so
│     │        │  │  ├─ resultproxy.pyx
│     │        │  │  ├─ util.cpython-310-x86_64-linux-gnu.so
│     │        │  │  └─ util.pyx
│     │        │  ├─ dialects
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ mssql
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ information_schema.cpython-310.pyc
│     │        │  │  │  │  ├─ json.cpython-310.pyc
│     │        │  │  │  │  ├─ provision.cpython-310.pyc
│     │        │  │  │  │  ├─ pymssql.cpython-310.pyc
│     │        │  │  │  │  └─ pyodbc.cpython-310.pyc
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ information_schema.py
│     │        │  │  │  ├─ json.py
│     │        │  │  │  ├─ provision.py
│     │        │  │  │  ├─ pymssql.py
│     │        │  │  │  └─ pyodbc.py
│     │        │  │  ├─ mysql
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ aiomysql.cpython-310.pyc
│     │        │  │  │  │  ├─ asyncmy.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ cymysql.cpython-310.pyc
│     │        │  │  │  │  ├─ dml.cpython-310.pyc
│     │        │  │  │  │  ├─ enumerated.cpython-310.pyc
│     │        │  │  │  │  ├─ expression.cpython-310.pyc
│     │        │  │  │  │  ├─ json.cpython-310.pyc
│     │        │  │  │  │  ├─ mariadb.cpython-310.pyc
│     │        │  │  │  │  ├─ mariadbconnector.cpython-310.pyc
│     │        │  │  │  │  ├─ mysqlconnector.cpython-310.pyc
│     │        │  │  │  │  ├─ mysqldb.cpython-310.pyc
│     │        │  │  │  │  ├─ provision.cpython-310.pyc
│     │        │  │  │  │  ├─ pymysql.cpython-310.pyc
│     │        │  │  │  │  ├─ pyodbc.cpython-310.pyc
│     │        │  │  │  │  ├─ reflection.cpython-310.pyc
│     │        │  │  │  │  ├─ reserved_words.cpython-310.pyc
│     │        │  │  │  │  └─ types.cpython-310.pyc
│     │        │  │  │  ├─ aiomysql.py
│     │        │  │  │  ├─ asyncmy.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ cymysql.py
│     │        │  │  │  ├─ dml.py
│     │        │  │  │  ├─ enumerated.py
│     │        │  │  │  ├─ expression.py
│     │        │  │  │  ├─ json.py
│     │        │  │  │  ├─ mariadb.py
│     │        │  │  │  ├─ mariadbconnector.py
│     │        │  │  │  ├─ mysqlconnector.py
│     │        │  │  │  ├─ mysqldb.py
│     │        │  │  │  ├─ provision.py
│     │        │  │  │  ├─ pymysql.py
│     │        │  │  │  ├─ pyodbc.py
│     │        │  │  │  ├─ reflection.py
│     │        │  │  │  ├─ reserved_words.py
│     │        │  │  │  └─ types.py
│     │        │  │  ├─ oracle
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ cx_oracle.cpython-310.pyc
│     │        │  │  │  │  ├─ dictionary.cpython-310.pyc
│     │        │  │  │  │  ├─ oracledb.cpython-310.pyc
│     │        │  │  │  │  ├─ provision.cpython-310.pyc
│     │        │  │  │  │  └─ types.cpython-310.pyc
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ cx_oracle.py
│     │        │  │  │  ├─ dictionary.py
│     │        │  │  │  ├─ oracledb.py
│     │        │  │  │  ├─ provision.py
│     │        │  │  │  └─ types.py
│     │        │  │  ├─ postgresql
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _psycopg_common.cpython-310.pyc
│     │        │  │  │  │  ├─ array.cpython-310.pyc
│     │        │  │  │  │  ├─ asyncpg.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ dml.cpython-310.pyc
│     │        │  │  │  │  ├─ ext.cpython-310.pyc
│     │        │  │  │  │  ├─ hstore.cpython-310.pyc
│     │        │  │  │  │  ├─ json.cpython-310.pyc
│     │        │  │  │  │  ├─ named_types.cpython-310.pyc
│     │        │  │  │  │  ├─ operators.cpython-310.pyc
│     │        │  │  │  │  ├─ pg8000.cpython-310.pyc
│     │        │  │  │  │  ├─ pg_catalog.cpython-310.pyc
│     │        │  │  │  │  ├─ provision.cpython-310.pyc
│     │        │  │  │  │  ├─ psycopg.cpython-310.pyc
│     │        │  │  │  │  ├─ psycopg2.cpython-310.pyc
│     │        │  │  │  │  ├─ psycopg2cffi.cpython-310.pyc
│     │        │  │  │  │  ├─ ranges.cpython-310.pyc
│     │        │  │  │  │  └─ types.cpython-310.pyc
│     │        │  │  │  ├─ _psycopg_common.py
│     │        │  │  │  ├─ array.py
│     │        │  │  │  ├─ asyncpg.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ dml.py
│     │        │  │  │  ├─ ext.py
│     │        │  │  │  ├─ hstore.py
│     │        │  │  │  ├─ json.py
│     │        │  │  │  ├─ named_types.py
│     │        │  │  │  ├─ operators.py
│     │        │  │  │  ├─ pg8000.py
│     │        │  │  │  ├─ pg_catalog.py
│     │        │  │  │  ├─ provision.py
│     │        │  │  │  ├─ psycopg.py
│     │        │  │  │  ├─ psycopg2.py
│     │        │  │  │  ├─ psycopg2cffi.py
│     │        │  │  │  ├─ ranges.py
│     │        │  │  │  └─ types.py
│     │        │  │  ├─ sqlite
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ aiosqlite.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ dml.cpython-310.pyc
│     │        │  │  │  │  ├─ json.cpython-310.pyc
│     │        │  │  │  │  ├─ provision.cpython-310.pyc
│     │        │  │  │  │  ├─ pysqlcipher.cpython-310.pyc
│     │        │  │  │  │  └─ pysqlite.cpython-310.pyc
│     │        │  │  │  ├─ aiosqlite.py
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ dml.py
│     │        │  │  │  ├─ json.py
│     │        │  │  │  ├─ provision.py
│     │        │  │  │  ├─ pysqlcipher.py
│     │        │  │  │  └─ pysqlite.py
│     │        │  │  └─ type_migration_guidelines.txt
│     │        │  ├─ engine
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _py_processors.cpython-310.pyc
│     │        │  │  │  ├─ _py_row.cpython-310.pyc
│     │        │  │  │  ├─ _py_util.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ characteristics.cpython-310.pyc
│     │        │  │  │  ├─ create.cpython-310.pyc
│     │        │  │  │  ├─ cursor.cpython-310.pyc
│     │        │  │  │  ├─ default.cpython-310.pyc
│     │        │  │  │  ├─ events.cpython-310.pyc
│     │        │  │  │  ├─ interfaces.cpython-310.pyc
│     │        │  │  │  ├─ mock.cpython-310.pyc
│     │        │  │  │  ├─ processors.cpython-310.pyc
│     │        │  │  │  ├─ reflection.cpython-310.pyc
│     │        │  │  │  ├─ result.cpython-310.pyc
│     │        │  │  │  ├─ row.cpython-310.pyc
│     │        │  │  │  ├─ strategies.cpython-310.pyc
│     │        │  │  │  ├─ url.cpython-310.pyc
│     │        │  │  │  └─ util.cpython-310.pyc
│     │        │  │  ├─ _py_processors.py
│     │        │  │  ├─ _py_row.py
│     │        │  │  ├─ _py_util.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ characteristics.py
│     │        │  │  ├─ create.py
│     │        │  │  ├─ cursor.py
│     │        │  │  ├─ default.py
│     │        │  │  ├─ events.py
│     │        │  │  ├─ interfaces.py
│     │        │  │  ├─ mock.py
│     │        │  │  ├─ processors.py
│     │        │  │  ├─ reflection.py
│     │        │  │  ├─ result.py
│     │        │  │  ├─ row.py
│     │        │  │  ├─ strategies.py
│     │        │  │  ├─ url.py
│     │        │  │  └─ util.py
│     │        │  ├─ event
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ api.cpython-310.pyc
│     │        │  │  │  ├─ attr.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ legacy.cpython-310.pyc
│     │        │  │  │  └─ registry.cpython-310.pyc
│     │        │  │  ├─ api.py
│     │        │  │  ├─ attr.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ legacy.py
│     │        │  │  └─ registry.py
│     │        │  ├─ events.py
│     │        │  ├─ exc.py
│     │        │  ├─ ext
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ associationproxy.cpython-310.pyc
│     │        │  │  │  ├─ automap.cpython-310.pyc
│     │        │  │  │  ├─ baked.cpython-310.pyc
│     │        │  │  │  ├─ compiler.cpython-310.pyc
│     │        │  │  │  ├─ horizontal_shard.cpython-310.pyc
│     │        │  │  │  ├─ hybrid.cpython-310.pyc
│     │        │  │  │  ├─ indexable.cpython-310.pyc
│     │        │  │  │  ├─ instrumentation.cpython-310.pyc
│     │        │  │  │  ├─ mutable.cpython-310.pyc
│     │        │  │  │  ├─ orderinglist.cpython-310.pyc
│     │        │  │  │  └─ serializer.cpython-310.pyc
│     │        │  │  ├─ associationproxy.py
│     │        │  │  ├─ asyncio
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  │  ├─ engine.cpython-310.pyc
│     │        │  │  │  │  ├─ exc.cpython-310.pyc
│     │        │  │  │  │  ├─ result.cpython-310.pyc
│     │        │  │  │  │  ├─ scoping.cpython-310.pyc
│     │        │  │  │  │  └─ session.cpython-310.pyc
│     │        │  │  │  ├─ base.py
│     │        │  │  │  ├─ engine.py
│     │        │  │  │  ├─ exc.py
│     │        │  │  │  ├─ result.py
│     │        │  │  │  ├─ scoping.py
│     │        │  │  │  └─ session.py
│     │        │  │  ├─ automap.py
│     │        │  │  ├─ baked.py
│     │        │  │  ├─ compiler.py
│     │        │  │  ├─ declarative
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  └─ extensions.cpython-310.pyc
│     │        │  │  │  └─ extensions.py
│     │        │  │  ├─ horizontal_shard.py
│     │        │  │  ├─ hybrid.py
│     │        │  │  ├─ indexable.py
│     │        │  │  ├─ instrumentation.py
│     │        │  │  ├─ mutable.py
│     │        │  │  ├─ mypy
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ apply.cpython-310.pyc
│     │        │  │  │  │  ├─ decl_class.cpython-310.pyc
│     │        │  │  │  │  ├─ infer.cpython-310.pyc
│     │        │  │  │  │  ├─ names.cpython-310.pyc
│     │        │  │  │  │  ├─ plugin.cpython-310.pyc
│     │        │  │  │  │  └─ util.cpython-310.pyc
│     │        │  │  │  ├─ apply.py
│     │        │  │  │  ├─ decl_class.py
│     │        │  │  │  ├─ infer.py
│     │        │  │  │  ├─ names.py
│     │        │  │  │  ├─ plugin.py
│     │        │  │  │  └─ util.py
│     │        │  │  ├─ orderinglist.py
│     │        │  │  └─ serializer.py
│     │        │  ├─ future
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ engine.cpython-310.pyc
│     │        │  │  └─ engine.py
│     │        │  ├─ inspection.py
│     │        │  ├─ log.py
│     │        │  ├─ orm
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _orm_constructors.cpython-310.pyc
│     │        │  │  │  ├─ _typing.cpython-310.pyc
│     │        │  │  │  ├─ attributes.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ bulk_persistence.cpython-310.pyc
│     │        │  │  │  ├─ clsregistry.cpython-310.pyc
│     │        │  │  │  ├─ collections.cpython-310.pyc
│     │        │  │  │  ├─ context.cpython-310.pyc
│     │        │  │  │  ├─ decl_api.cpython-310.pyc
│     │        │  │  │  ├─ decl_base.cpython-310.pyc
│     │        │  │  │  ├─ dependency.cpython-310.pyc
│     │        │  │  │  ├─ descriptor_props.cpython-310.pyc
│     │        │  │  │  ├─ dynamic.cpython-310.pyc
│     │        │  │  │  ├─ evaluator.cpython-310.pyc
│     │        │  │  │  ├─ events.cpython-310.pyc
│     │        │  │  │  ├─ exc.cpython-310.pyc
│     │        │  │  │  ├─ identity.cpython-310.pyc
│     │        │  │  │  ├─ instrumentation.cpython-310.pyc
│     │        │  │  │  ├─ interfaces.cpython-310.pyc
│     │        │  │  │  ├─ loading.cpython-310.pyc
│     │        │  │  │  ├─ mapped_collection.cpython-310.pyc
│     │        │  │  │  ├─ mapper.cpython-310.pyc
│     │        │  │  │  ├─ path_registry.cpython-310.pyc
│     │        │  │  │  ├─ persistence.cpython-310.pyc
│     │        │  │  │  ├─ properties.cpython-310.pyc
│     │        │  │  │  ├─ query.cpython-310.pyc
│     │        │  │  │  ├─ relationships.cpython-310.pyc
│     │        │  │  │  ├─ scoping.cpython-310.pyc
│     │        │  │  │  ├─ session.cpython-310.pyc
│     │        │  │  │  ├─ state.cpython-310.pyc
│     │        │  │  │  ├─ state_changes.cpython-310.pyc
│     │        │  │  │  ├─ strategies.cpython-310.pyc
│     │        │  │  │  ├─ strategy_options.cpython-310.pyc
│     │        │  │  │  ├─ sync.cpython-310.pyc
│     │        │  │  │  ├─ unitofwork.cpython-310.pyc
│     │        │  │  │  ├─ util.cpython-310.pyc
│     │        │  │  │  └─ writeonly.cpython-310.pyc
│     │        │  │  ├─ _orm_constructors.py
│     │        │  │  ├─ _typing.py
│     │        │  │  ├─ attributes.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ bulk_persistence.py
│     │        │  │  ├─ clsregistry.py
│     │        │  │  ├─ collections.py
│     │        │  │  ├─ context.py
│     │        │  │  ├─ decl_api.py
│     │        │  │  ├─ decl_base.py
│     │        │  │  ├─ dependency.py
│     │        │  │  ├─ descriptor_props.py
│     │        │  │  ├─ dynamic.py
│     │        │  │  ├─ evaluator.py
│     │        │  │  ├─ events.py
│     │        │  │  ├─ exc.py
│     │        │  │  ├─ identity.py
│     │        │  │  ├─ instrumentation.py
│     │        │  │  ├─ interfaces.py
│     │        │  │  ├─ loading.py
│     │        │  │  ├─ mapped_collection.py
│     │        │  │  ├─ mapper.py
│     │        │  │  ├─ path_registry.py
│     │        │  │  ├─ persistence.py
│     │        │  │  ├─ properties.py
│     │        │  │  ├─ query.py
│     │        │  │  ├─ relationships.py
│     │        │  │  ├─ scoping.py
│     │        │  │  ├─ session.py
│     │        │  │  ├─ state.py
│     │        │  │  ├─ state_changes.py
│     │        │  │  ├─ strategies.py
│     │        │  │  ├─ strategy_options.py
│     │        │  │  ├─ sync.py
│     │        │  │  ├─ unitofwork.py
│     │        │  │  ├─ util.py
│     │        │  │  └─ writeonly.py
│     │        │  ├─ pool
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ events.cpython-310.pyc
│     │        │  │  │  └─ impl.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  ├─ events.py
│     │        │  │  └─ impl.py
│     │        │  ├─ py.typed
│     │        │  ├─ schema.py
│     │        │  ├─ sql
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ _dml_constructors.cpython-310.pyc
│     │        │  │  │  ├─ _elements_constructors.cpython-310.pyc
│     │        │  │  │  ├─ _orm_types.cpython-310.pyc
│     │        │  │  │  ├─ _py_util.cpython-310.pyc
│     │        │  │  │  ├─ _selectable_constructors.cpython-310.pyc
│     │        │  │  │  ├─ _typing.cpython-310.pyc
│     │        │  │  │  ├─ annotation.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  ├─ cache_key.cpython-310.pyc
│     │        │  │  │  ├─ coercions.cpython-310.pyc
│     │        │  │  │  ├─ compiler.cpython-310.pyc
│     │        │  │  │  ├─ crud.cpython-310.pyc
│     │        │  │  │  ├─ ddl.cpython-310.pyc
│     │        │  │  │  ├─ default_comparator.cpython-310.pyc
│     │        │  │  │  ├─ dml.cpython-310.pyc
│     │        │  │  │  ├─ elements.cpython-310.pyc
│     │        │  │  │  ├─ events.cpython-310.pyc
│     │        │  │  │  ├─ expression.cpython-310.pyc
│     │        │  │  │  ├─ functions.cpython-310.pyc
│     │        │  │  │  ├─ lambdas.cpython-310.pyc
│     │        │  │  │  ├─ naming.cpython-310.pyc
│     │        │  │  │  ├─ operators.cpython-310.pyc
│     │        │  │  │  ├─ roles.cpython-310.pyc
│     │        │  │  │  ├─ schema.cpython-310.pyc
│     │        │  │  │  ├─ selectable.cpython-310.pyc
│     │        │  │  │  ├─ sqltypes.cpython-310.pyc
│     │        │  │  │  ├─ traversals.cpython-310.pyc
│     │        │  │  │  ├─ type_api.cpython-310.pyc
│     │        │  │  │  ├─ util.cpython-310.pyc
│     │        │  │  │  └─ visitors.cpython-310.pyc
│     │        │  │  ├─ _dml_constructors.py
│     │        │  │  ├─ _elements_constructors.py
│     │        │  │  ├─ _orm_types.py
│     │        │  │  ├─ _py_util.py
│     │        │  │  ├─ _selectable_constructors.py
│     │        │  │  ├─ _typing.py
│     │        │  │  ├─ annotation.py
│     │        │  │  ├─ base.py
│     │        │  │  ├─ cache_key.py
│     │        │  │  ├─ coercions.py
│     │        │  │  ├─ compiler.py
│     │        │  │  ├─ crud.py
│     │        │  │  ├─ ddl.py
│     │        │  │  ├─ default_comparator.py
│     │        │  │  ├─ dml.py
│     │        │  │  ├─ elements.py
│     │        │  │  ├─ events.py
│     │        │  │  ├─ expression.py
│     │        │  │  ├─ functions.py
│     │        │  │  ├─ lambdas.py
│     │        │  │  ├─ naming.py
│     │        │  │  ├─ operators.py
│     │        │  │  ├─ roles.py
│     │        │  │  ├─ schema.py
│     │        │  │  ├─ selectable.py
│     │        │  │  ├─ sqltypes.py
│     │        │  │  ├─ traversals.py
│     │        │  │  ├─ type_api.py
│     │        │  │  ├─ util.py
│     │        │  │  └─ visitors.py
│     │        │  ├─ testing
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ assertions.cpython-310.pyc
│     │        │  │  │  ├─ assertsql.cpython-310.pyc
│     │        │  │  │  ├─ asyncio.cpython-310.pyc
│     │        │  │  │  ├─ config.cpython-310.pyc
│     │        │  │  │  ├─ engines.cpython-310.pyc
│     │        │  │  │  ├─ entities.cpython-310.pyc
│     │        │  │  │  ├─ exclusions.cpython-310.pyc
│     │        │  │  │  ├─ fixtures.cpython-310.pyc
│     │        │  │  │  ├─ pickleable.cpython-310.pyc
│     │        │  │  │  ├─ profiling.cpython-310.pyc
│     │        │  │  │  ├─ provision.cpython-310.pyc
│     │        │  │  │  ├─ requirements.cpython-310.pyc
│     │        │  │  │  ├─ schema.cpython-310.pyc
│     │        │  │  │  ├─ util.cpython-310.pyc
│     │        │  │  │  └─ warnings.cpython-310.pyc
│     │        │  │  ├─ assertions.py
│     │        │  │  ├─ assertsql.py
│     │        │  │  ├─ asyncio.py
│     │        │  │  ├─ config.py
│     │        │  │  ├─ engines.py
│     │        │  │  ├─ entities.py
│     │        │  │  ├─ exclusions.py
│     │        │  │  ├─ fixtures.py
│     │        │  │  ├─ pickleable.py
│     │        │  │  ├─ plugin
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ bootstrap.cpython-310.pyc
│     │        │  │  │  │  ├─ plugin_base.cpython-310.pyc
│     │        │  │  │  │  └─ pytestplugin.cpython-310.pyc
│     │        │  │  │  ├─ bootstrap.py
│     │        │  │  │  ├─ plugin_base.py
│     │        │  │  │  └─ pytestplugin.py
│     │        │  │  ├─ profiling.py
│     │        │  │  ├─ provision.py
│     │        │  │  ├─ requirements.py
│     │        │  │  ├─ schema.py
│     │        │  │  ├─ suite
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ test_cte.cpython-310.pyc
│     │        │  │  │  │  ├─ test_ddl.cpython-310.pyc
│     │        │  │  │  │  ├─ test_deprecations.cpython-310.pyc
│     │        │  │  │  │  ├─ test_dialect.cpython-310.pyc
│     │        │  │  │  │  ├─ test_insert.cpython-310.pyc
│     │        │  │  │  │  ├─ test_reflection.cpython-310.pyc
│     │        │  │  │  │  ├─ test_results.cpython-310.pyc
│     │        │  │  │  │  ├─ test_rowcount.cpython-310.pyc
│     │        │  │  │  │  ├─ test_select.cpython-310.pyc
│     │        │  │  │  │  ├─ test_sequence.cpython-310.pyc
│     │        │  │  │  │  ├─ test_types.cpython-310.pyc
│     │        │  │  │  │  ├─ test_unicode_ddl.cpython-310.pyc
│     │        │  │  │  │  └─ test_update_delete.cpython-310.pyc
│     │        │  │  │  ├─ test_cte.py
│     │        │  │  │  ├─ test_ddl.py
│     │        │  │  │  ├─ test_deprecations.py
│     │        │  │  │  ├─ test_dialect.py
│     │        │  │  │  ├─ test_insert.py
│     │        │  │  │  ├─ test_reflection.py
│     │        │  │  │  ├─ test_results.py
│     │        │  │  │  ├─ test_rowcount.py
│     │        │  │  │  ├─ test_select.py
│     │        │  │  │  ├─ test_sequence.py
│     │        │  │  │  ├─ test_types.py
│     │        │  │  │  ├─ test_unicode_ddl.py
│     │        │  │  │  └─ test_update_delete.py
│     │        │  │  ├─ util.py
│     │        │  │  └─ warnings.py
│     │        │  ├─ types.py
│     │        │  └─ util
│     │        │     ├─ __init__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ _collections.cpython-310.pyc
│     │        │     │  ├─ _concurrency_py3k.cpython-310.pyc
│     │        │     │  ├─ _has_cy.cpython-310.pyc
│     │        │     │  ├─ _py_collections.cpython-310.pyc
│     │        │     │  ├─ compat.cpython-310.pyc
│     │        │     │  ├─ concurrency.cpython-310.pyc
│     │        │     │  ├─ deprecations.cpython-310.pyc
│     │        │     │  ├─ langhelpers.cpython-310.pyc
│     │        │     │  ├─ preloaded.cpython-310.pyc
│     │        │     │  ├─ queue.cpython-310.pyc
│     │        │     │  ├─ tool_support.cpython-310.pyc
│     │        │     │  ├─ topological.cpython-310.pyc
│     │        │     │  └─ typing.cpython-310.pyc
│     │        │     ├─ _collections.py
│     │        │     ├─ _concurrency_py3k.py
│     │        │     ├─ _has_cy.py
│     │        │     ├─ _py_collections.py
│     │        │     ├─ compat.py
│     │        │     ├─ concurrency.py
│     │        │     ├─ deprecations.py
│     │        │     ├─ langhelpers.py
│     │        │     ├─ preloaded.py
│     │        │     ├─ queue.py
│     │        │     ├─ tool_support.py
│     │        │     ├─ topological.py
│     │        │     └─ typing.py
│     │        ├─ tomli
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _parser.cpython-310.pyc
│     │        │  │  ├─ _re.cpython-310.pyc
│     │        │  │  └─ _types.cpython-310.pyc
│     │        │  ├─ _parser.py
│     │        │  ├─ _re.py
│     │        │  ├─ _types.py
│     │        │  └─ py.typed
│     │        ├─ tomli-2.0.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  └─ WHEEL
│     │        ├─ typing_extensions-4.7.1.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  └─ WHEEL
│     │        ├─ typing_extensions.py
│     │        ├─ uvicorn
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ _subprocess.cpython-310.pyc
│     │        │  │  ├─ _types.cpython-310.pyc
│     │        │  │  ├─ config.cpython-310.pyc
│     │        │  │  ├─ importer.cpython-310.pyc
│     │        │  │  ├─ logging.cpython-310.pyc
│     │        │  │  ├─ main.cpython-310.pyc
│     │        │  │  ├─ server.cpython-310.pyc
│     │        │  │  └─ workers.cpython-310.pyc
│     │        │  ├─ _subprocess.py
│     │        │  ├─ _types.py
│     │        │  ├─ config.py
│     │        │  ├─ importer.py
│     │        │  ├─ lifespan
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ off.cpython-310.pyc
│     │        │  │  │  └─ on.cpython-310.pyc
│     │        │  │  ├─ off.py
│     │        │  │  └─ on.py
│     │        │  ├─ logging.py
│     │        │  ├─ loops
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asyncio.cpython-310.pyc
│     │        │  │  │  ├─ auto.cpython-310.pyc
│     │        │  │  │  └─ uvloop.cpython-310.pyc
│     │        │  │  ├─ asyncio.py
│     │        │  │  ├─ auto.py
│     │        │  │  └─ uvloop.py
│     │        │  ├─ main.py
│     │        │  ├─ middleware
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ asgi2.cpython-310.pyc
│     │        │  │  │  ├─ message_logger.cpython-310.pyc
│     │        │  │  │  ├─ proxy_headers.cpython-310.pyc
│     │        │  │  │  └─ wsgi.cpython-310.pyc
│     │        │  │  ├─ asgi2.py
│     │        │  │  ├─ message_logger.py
│     │        │  │  ├─ proxy_headers.py
│     │        │  │  └─ wsgi.py
│     │        │  ├─ protocols
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  ├─ http
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ auto.cpython-310.pyc
│     │        │  │  │  │  ├─ flow_control.cpython-310.pyc
│     │        │  │  │  │  ├─ h11_impl.cpython-310.pyc
│     │        │  │  │  │  └─ httptools_impl.cpython-310.pyc
│     │        │  │  │  ├─ auto.py
│     │        │  │  │  ├─ flow_control.py
│     │        │  │  │  ├─ h11_impl.py
│     │        │  │  │  └─ httptools_impl.py
│     │        │  │  ├─ utils.py
│     │        │  │  └─ websockets
│     │        │  │     ├─ __init__.py
│     │        │  │     ├─ __pycache__
│     │        │  │     │  ├─ __init__.cpython-310.pyc
│     │        │  │     │  ├─ auto.cpython-310.pyc
│     │        │  │     │  ├─ websockets_impl.cpython-310.pyc
│     │        │  │     │  └─ wsproto_impl.cpython-310.pyc
│     │        │  │     ├─ auto.py
│     │        │  │     ├─ websockets_impl.py
│     │        │  │     └─ wsproto_impl.py
│     │        │  ├─ py.typed
│     │        │  ├─ server.py
│     │        │  ├─ supervisors
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ basereload.cpython-310.pyc
│     │        │  │  │  ├─ multiprocess.cpython-310.pyc
│     │        │  │  │  ├─ statreload.cpython-310.pyc
│     │        │  │  │  ├─ watchfilesreload.cpython-310.pyc
│     │        │  │  │  └─ watchgodreload.cpython-310.pyc
│     │        │  │  ├─ basereload.py
│     │        │  │  ├─ multiprocess.py
│     │        │  │  ├─ statreload.py
│     │        │  │  ├─ watchfilesreload.py
│     │        │  │  └─ watchgodreload.py
│     │        │  └─ workers.py
│     │        ├─ uvicorn-0.22.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ licenses
│     │        │     └─ LICENSE.md
│     │        ├─ uvloop
│     │        │  ├─ __init__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ _noop.cpython-310.pyc
│     │        │  │  ├─ _testbase.cpython-310.pyc
│     │        │  │  └─ _version.cpython-310.pyc
│     │        │  ├─ _noop.py
│     │        │  ├─ _testbase.py
│     │        │  ├─ _version.py
│     │        │  ├─ cbhandles.pxd
│     │        │  ├─ cbhandles.pyx
│     │        │  ├─ dns.pyx
│     │        │  ├─ errors.pyx
│     │        │  ├─ handles
│     │        │  │  ├─ async_.pxd
│     │        │  │  ├─ async_.pyx
│     │        │  │  ├─ basetransport.pxd
│     │        │  │  ├─ basetransport.pyx
│     │        │  │  ├─ check.pxd
│     │        │  │  ├─ check.pyx
│     │        │  │  ├─ fsevent.pxd
│     │        │  │  ├─ fsevent.pyx
│     │        │  │  ├─ handle.pxd
│     │        │  │  ├─ handle.pyx
│     │        │  │  ├─ idle.pxd
│     │        │  │  ├─ idle.pyx
│     │        │  │  ├─ pipe.pxd
│     │        │  │  ├─ pipe.pyx
│     │        │  │  ├─ poll.pxd
│     │        │  │  ├─ poll.pyx
│     │        │  │  ├─ process.pxd
│     │        │  │  ├─ process.pyx
│     │        │  │  ├─ stream.pxd
│     │        │  │  ├─ stream.pyx
│     │        │  │  ├─ streamserver.pxd
│     │        │  │  ├─ streamserver.pyx
│     │        │  │  ├─ tcp.pxd
│     │        │  │  ├─ tcp.pyx
│     │        │  │  ├─ timer.pxd
│     │        │  │  ├─ timer.pyx
│     │        │  │  ├─ udp.pxd
│     │        │  │  └─ udp.pyx
│     │        │  ├─ includes
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ compat.h
│     │        │  │  ├─ consts.pxi
│     │        │  │  ├─ debug.h
│     │        │  │  ├─ debug.pxd
│     │        │  │  ├─ flowcontrol.pxd
│     │        │  │  ├─ fork_handler.h
│     │        │  │  ├─ python.pxd
│     │        │  │  ├─ stdlib.pxi
│     │        │  │  ├─ system.pxd
│     │        │  │  └─ uv.pxd
│     │        │  ├─ loop.c
│     │        │  ├─ loop.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ loop.pxd
│     │        │  ├─ loop.pyi
│     │        │  ├─ loop.pyx
│     │        │  ├─ lru.pyx
│     │        │  ├─ pseudosock.pyx
│     │        │  ├─ py.typed
│     │        │  ├─ request.pxd
│     │        │  ├─ request.pyx
│     │        │  ├─ server.pxd
│     │        │  ├─ server.pyx
│     │        │  ├─ sslproto.pxd
│     │        │  └─ sslproto.pyx
│     │        ├─ uvloop-0.17.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE-APACHE
│     │        │  ├─ LICENSE-MIT
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ validate_pyproject
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ api.cpython-310.pyc
│     │        │  │  ├─ cli.cpython-310.pyc
│     │        │  │  ├─ error_reporting.cpython-310.pyc
│     │        │  │  ├─ errors.cpython-310.pyc
│     │        │  │  ├─ extra_validations.cpython-310.pyc
│     │        │  │  ├─ formats.cpython-310.pyc
│     │        │  │  └─ types.cpython-310.pyc
│     │        │  ├─ api.py
│     │        │  ├─ cli.py
│     │        │  ├─ error_reporting.py
│     │        │  ├─ errors.py
│     │        │  ├─ extra_validations.py
│     │        │  ├─ formats.py
│     │        │  ├─ plugins
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ distutils.schema.json
│     │        │  │  └─ setuptools.schema.json
│     │        │  ├─ pre_compile
│     │        │  │  ├─ NOTICE.template
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __main__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  │  └─ cli.cpython-310.pyc
│     │        │  │  ├─ api-notice.template
│     │        │  │  ├─ cli-notice.template
│     │        │  │  ├─ cli.py
│     │        │  │  └─ main_file.template
│     │        │  ├─ project_metadata.schema.json
│     │        │  ├─ py.typed
│     │        │  ├─ pyproject_toml.schema.json
│     │        │  ├─ types.py
│     │        │  └─ vendoring
│     │        │     ├─ __init__.py
│     │        │     ├─ __main__.py
│     │        │     ├─ __pycache__
│     │        │     │  ├─ __init__.cpython-310.pyc
│     │        │     │  ├─ __main__.cpython-310.pyc
│     │        │     │  └─ cli.cpython-310.pyc
│     │        │     └─ cli.py
│     │        ├─ validate_pyproject-0.13.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.txt
│     │        │  ├─ METADATA
│     │        │  ├─ NOTICE.txt
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ top_level.txt
│     │        ├─ watchfiles
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ cli.cpython-310.pyc
│     │        │  │  ├─ filters.cpython-310.pyc
│     │        │  │  ├─ main.cpython-310.pyc
│     │        │  │  ├─ run.cpython-310.pyc
│     │        │  │  └─ version.cpython-310.pyc
│     │        │  ├─ _rust_notify.abi3.so
│     │        │  ├─ _rust_notify.pyi
│     │        │  ├─ cli.py
│     │        │  ├─ filters.py
│     │        │  ├─ main.py
│     │        │  ├─ py.typed
│     │        │  ├─ run.py
│     │        │  └─ version.py
│     │        ├─ watchfiles-0.19.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  ├─ entry_points.txt
│     │        │  └─ license_files
│     │        │     └─ LICENSE
│     │        ├─ websockets
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ auth.cpython-310.pyc
│     │        │  │  ├─ client.cpython-310.pyc
│     │        │  │  ├─ connection.cpython-310.pyc
│     │        │  │  ├─ datastructures.cpython-310.pyc
│     │        │  │  ├─ exceptions.cpython-310.pyc
│     │        │  │  ├─ frames.cpython-310.pyc
│     │        │  │  ├─ headers.cpython-310.pyc
│     │        │  │  ├─ http.cpython-310.pyc
│     │        │  │  ├─ http11.cpython-310.pyc
│     │        │  │  ├─ imports.cpython-310.pyc
│     │        │  │  ├─ protocol.cpython-310.pyc
│     │        │  │  ├─ server.cpython-310.pyc
│     │        │  │  ├─ streams.cpython-310.pyc
│     │        │  │  ├─ typing.cpython-310.pyc
│     │        │  │  ├─ uri.cpython-310.pyc
│     │        │  │  ├─ utils.cpython-310.pyc
│     │        │  │  └─ version.cpython-310.pyc
│     │        │  ├─ auth.py
│     │        │  ├─ client.py
│     │        │  ├─ connection.py
│     │        │  ├─ datastructures.py
│     │        │  ├─ exceptions.py
│     │        │  ├─ extensions
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ base.cpython-310.pyc
│     │        │  │  │  └─ permessage_deflate.cpython-310.pyc
│     │        │  │  ├─ base.py
│     │        │  │  └─ permessage_deflate.py
│     │        │  ├─ frames.py
│     │        │  ├─ headers.py
│     │        │  ├─ http.py
│     │        │  ├─ http11.py
│     │        │  ├─ imports.py
│     │        │  ├─ legacy
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ async_timeout.cpython-310.pyc
│     │        │  │  │  ├─ auth.cpython-310.pyc
│     │        │  │  │  ├─ client.cpython-310.pyc
│     │        │  │  │  ├─ compatibility.cpython-310.pyc
│     │        │  │  │  ├─ framing.cpython-310.pyc
│     │        │  │  │  ├─ handshake.cpython-310.pyc
│     │        │  │  │  ├─ http.cpython-310.pyc
│     │        │  │  │  ├─ protocol.cpython-310.pyc
│     │        │  │  │  └─ server.cpython-310.pyc
│     │        │  │  ├─ async_timeout.py
│     │        │  │  ├─ auth.py
│     │        │  │  ├─ client.py
│     │        │  │  ├─ compatibility.py
│     │        │  │  ├─ framing.py
│     │        │  │  ├─ handshake.py
│     │        │  │  ├─ http.py
│     │        │  │  ├─ protocol.py
│     │        │  │  └─ server.py
│     │        │  ├─ protocol.py
│     │        │  ├─ py.typed
│     │        │  ├─ server.py
│     │        │  ├─ speedups.c
│     │        │  ├─ speedups.cpython-310-x86_64-linux-gnu.so
│     │        │  ├─ streams.py
│     │        │  ├─ sync
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ client.cpython-310.pyc
│     │        │  │  │  ├─ compatibility.cpython-310.pyc
│     │        │  │  │  ├─ connection.cpython-310.pyc
│     │        │  │  │  ├─ messages.cpython-310.pyc
│     │        │  │  │  ├─ server.cpython-310.pyc
│     │        │  │  │  └─ utils.cpython-310.pyc
│     │        │  │  ├─ client.py
│     │        │  │  ├─ compatibility.py
│     │        │  │  ├─ connection.py
│     │        │  │  ├─ messages.py
│     │        │  │  ├─ server.py
│     │        │  │  └─ utils.py
│     │        │  ├─ typing.py
│     │        │  ├─ uri.py
│     │        │  ├─ utils.py
│     │        │  └─ version.py
│     │        ├─ websockets-11.0.3.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ top_level.txt
│     │        ├─ wheel
│     │        │  ├─ __init__.py
│     │        │  ├─ __main__.py
│     │        │  ├─ __pycache__
│     │        │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  ├─ __main__.cpython-310.pyc
│     │        │  │  ├─ _setuptools_logging.cpython-310.pyc
│     │        │  │  ├─ bdist_wheel.cpython-310.pyc
│     │        │  │  ├─ macosx_libfile.cpython-310.pyc
│     │        │  │  ├─ metadata.cpython-310.pyc
│     │        │  │  ├─ util.cpython-310.pyc
│     │        │  │  └─ wheelfile.cpython-310.pyc
│     │        │  ├─ _setuptools_logging.py
│     │        │  ├─ bdist_wheel.py
│     │        │  ├─ cli
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  ├─ convert.cpython-310.pyc
│     │        │  │  │  ├─ pack.cpython-310.pyc
│     │        │  │  │  ├─ tags.cpython-310.pyc
│     │        │  │  │  └─ unpack.cpython-310.pyc
│     │        │  │  ├─ convert.py
│     │        │  │  ├─ pack.py
│     │        │  │  ├─ tags.py
│     │        │  │  └─ unpack.py
│     │        │  ├─ macosx_libfile.py
│     │        │  ├─ metadata.py
│     │        │  ├─ util.py
│     │        │  ├─ vendored
│     │        │  │  ├─ __init__.py
│     │        │  │  ├─ __pycache__
│     │        │  │  │  └─ __init__.cpython-310.pyc
│     │        │  │  ├─ packaging
│     │        │  │  │  ├─ __init__.py
│     │        │  │  │  ├─ __pycache__
│     │        │  │  │  │  ├─ __init__.cpython-310.pyc
│     │        │  │  │  │  ├─ _elffile.cpython-310.pyc
│     │        │  │  │  │  ├─ _manylinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _musllinux.cpython-310.pyc
│     │        │  │  │  │  ├─ _parser.cpython-310.pyc
│     │        │  │  │  │  ├─ _structures.cpython-310.pyc
│     │        │  │  │  │  ├─ _tokenizer.cpython-310.pyc
│     │        │  │  │  │  ├─ markers.cpython-310.pyc
│     │        │  │  │  │  ├─ requirements.cpython-310.pyc
│     │        │  │  │  │  ├─ specifiers.cpython-310.pyc
│     │        │  │  │  │  ├─ tags.cpython-310.pyc
│     │        │  │  │  │  ├─ utils.cpython-310.pyc
│     │        │  │  │  │  └─ version.cpython-310.pyc
│     │        │  │  │  ├─ _elffile.py
│     │        │  │  │  ├─ _manylinux.py
│     │        │  │  │  ├─ _musllinux.py
│     │        │  │  │  ├─ _parser.py
│     │        │  │  │  ├─ _structures.py
│     │        │  │  │  ├─ _tokenizer.py
│     │        │  │  │  ├─ markers.py
│     │        │  │  │  ├─ requirements.py
│     │        │  │  │  ├─ specifiers.py
│     │        │  │  │  ├─ tags.py
│     │        │  │  │  ├─ utils.py
│     │        │  │  │  └─ version.py
│     │        │  │  └─ vendor.txt
│     │        │  └─ wheelfile.py
│     │        ├─ wheel-0.40.0.dist-info
│     │        │  ├─ INSTALLER
│     │        │  ├─ LICENSE.txt
│     │        │  ├─ METADATA
│     │        │  ├─ RECORD
│     │        │  ├─ REQUESTED
│     │        │  ├─ WHEEL
│     │        │  └─ entry_points.txt
│     │        └─ yaml
│     │           ├─ __init__.py
│     │           ├─ __pycache__
│     │           │  ├─ __init__.cpython-310.pyc
│     │           │  ├─ composer.cpython-310.pyc
│     │           │  ├─ constructor.cpython-310.pyc
│     │           │  ├─ cyaml.cpython-310.pyc
│     │           │  ├─ dumper.cpython-310.pyc
│     │           │  ├─ emitter.cpython-310.pyc
│     │           │  ├─ error.cpython-310.pyc
│     │           │  ├─ events.cpython-310.pyc
│     │           │  ├─ loader.cpython-310.pyc
│     │           │  ├─ nodes.cpython-310.pyc
│     │           │  ├─ parser.cpython-310.pyc
│     │           │  ├─ reader.cpython-310.pyc
│     │           │  ├─ representer.cpython-310.pyc
│     │           │  ├─ resolver.cpython-310.pyc
│     │           │  ├─ scanner.cpython-310.pyc
│     │           │  ├─ serializer.cpython-310.pyc
│     │           │  └─ tokens.cpython-310.pyc
│     │           ├─ _yaml.cpython-310-x86_64-linux-gnu.so
│     │           ├─ composer.py
│     │           ├─ constructor.py
│     │           ├─ cyaml.py
│     │           ├─ dumper.py
│     │           ├─ emitter.py
│     │           ├─ error.py
│     │           ├─ events.py
│     │           ├─ loader.py
│     │           ├─ nodes.py
│     │           ├─ parser.py
│     │           ├─ reader.py
│     │           ├─ representer.py
│     │           ├─ resolver.py
│     │           ├─ scanner.py
│     │           ├─ serializer.py
│     │           └─ tokens.py
│     └─ pyvenv.cfg
└─ client
   ├─ .eslintignore
   ├─ .eslintrc.cjs
   ├─ .npmrc
   ├─ .prettierignore
   ├─ .prettierrc
   ├─ .vscode
   │  └─ settings.json
   ├─ README.md
   ├─ orval.config.ts
   ├─ package-lock.json
   ├─ package.json
   ├─ playwright.config.ts
   ├─ postcss.config.cjs
   ├─ schema.yml
   ├─ src
   │  ├─ app.d.ts
   │  ├─ app.html
   │  ├─ app.postcss
   │  ├─ index.test.ts
   │  ├─ lib
   │  │  ├─ api
   │  │  │  ├─ codegen
   │  │  │  │  ├─ accounts
   │  │  │  │  │  ├─ accounts.msw.ts
   │  │  │  │  │  └─ accounts.ts
   │  │  │  │  ├─ auth
   │  │  │  │  │  ├─ auth.msw.ts
   │  │  │  │  │  └─ auth.ts
   │  │  │  │  └─ verdanTechAPI.schemas.ts
   │  │  │  ├─ customAxios.ts
   │  │  │  └─ utils.ts
   │  │  ├─ components
   │  │  │  ├─ forms
   │  │  │  │  └─ FormError.svelte
   │  │  │  ├─ graphics
   │  │  │  │  └─ logo.svelte
   │  │  │  ├─ layout
   │  │  │  │  ├─ AuthenticatedBar.svelte
   │  │  │  │  ├─ AuthenticatedRail.svelte
   │  │  │  │  └─ UnauthenticatedAppBar.svelte
   │  │  │  └─ security
   │  │  │     └─ EnsureCSRF.svelte
   │  │  └─ stores.ts
   │  ├─ routes
   │  │  ├─ +layout.svelte
   │  │  ├─ +page.svelte
   │  │  ├─ app
   │  │  │  ├─ +page.svelte
   │  │  │  └─ [garden_slug]
   │  │  │     ├─ +page.svelte
   │  │  │     ├─ dashboard
   │  │  │     │  └─ +page.svelte
   │  │  │     ├─ planner
   │  │  │     │  └─ +page.svelte
   │  │  │     ├─ plants
   │  │  │     │  └─ page.svelte
   │  │  │     └─ workspaces
   │  │  │        └─ page.svelte
   │  │  ├─ donate
   │  │  │  └─ +page.svelte
   │  │  ├─ guides
   │  │  │  └─ +page.svelte
   │  │  ├─ login
   │  │  │  ├─ +page.svelte
   │  │  │  ├─ LoginForm.svelte
   │  │  │  └─ reset
   │  │  │     ├─ +page.svelte
   │  │  │     ├─ ResetForm.svelte
   │  │  │     └─ [user_id]
   │  │  │        └─ [token]
   │  │  │           ├─ +page.svelte
   │  │  │           └─ ResetConfirmForm.svelte
   │  │  ├─ project
   │  │  │  └─ +page.svelte
   │  │  ├─ register
   │  │  │  ├─ +page.svelte
   │  │  │  ├─ RegisterForm.svelte
   │  │  │  ├─ resend
   │  │  │  │  ├─ +page.svelte
   │  │  │  │  └─ VerifyResendForm.svelte
   │  │  │  └─ verify
   │  │  │     └─ [key]
   │  │  │        └─ +page.svelte
   │  │  └─ users
   │  │     ├─ +page.svelte
   │  │     └─ [username]
   │  │        └─ page.svelte
   │  └─ theme-garden.postcss
   ├─ static
   │  └─ favicon.ico
   ├─ svelte.config.js
   ├─ tailwind.config.cjs
   ├─ tests
   │  └─ test.ts
   ├─ tsconfig.json
   └─ vite.config.ts

```