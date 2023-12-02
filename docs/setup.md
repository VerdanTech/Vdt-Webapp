# Environment Variables

The environment configuration for the default development environment is contained in `.env-default`. During the build process of the default development environment, this file is copied to create a `.env` file that is accessed by python and other scripts.

- POSTGRES_DB_URI: URI of the postgres database. Name in URI must match `POSTGRES_DB_NAME` if using the development environment.
- POSTGRES_DB_NAME: Name to assign to a postgresql server when creating a development build
- POSTGRES_DB_USER: Username to assign to client that connects to development postgres server. User is granted all permissions.
- POSTGRES_DB_PASSWORD: Password to assign to client that connects to development postgres server.

# methods

## Manual

### requirements
Linux (use WSL if on windows)

### Steps

1. If you don't have access to linux, install WSL
2. Create a folder for the repo
3. Clone the repo using `git clone https://github.com/nathanielarking/VerdanTech.git`
4. Change to the backend directory using `cd api`
5. Add repository with required python version sudo `add-apt-repository ppa:deadsnakes/ppa`
6. Update sudo apt list with `sudo apt-get update && sudo apt-get upgrade`
7. Install python version `sudo apt-get install python3.12 && sudo apt-get install python3.12-dev && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12`
8. Install PDM `python3.12 -m pip install pdm`
9. Install packages `python3.12 -m pdm sync --clean --lockfile requirements/.pdm-lock`