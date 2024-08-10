# Environment Setup

The development environment of the backend contains the ASGI application process, task backend application process, and external services, including Postgres server, NATs server, etc. This allows the execution of tests against live versions of services, and is achieved using Docker containers.

The current workflow for setting up development environments is standardized to use [Development Containers](https://containers.dev/). This makes reproduction of the environment very easy. The cost is that while the devcontainer tool is an open standard, IDE support on IDEs other than VSCode is minimal. If you wish to use an IDE other than VSCode, manual installation instructions will need to be created.

# Devcontainer

[Development Containers](https://containers.dev/) allows the use of Docker containers as full-featured development environments. This makes reproduction of the environment very easy. The cost is that while the devcontainer tool is an open standard, IDE support on IDEs other than VSCode is minimal. Neovim is an open-source editor which has some support, but no setup exists for that yet.

If you wish to use an IDE other than VSCode, manual installation instructions will follow, but will be created as necessary.

Note that there are two commands that run after the container is created:
1. The .env-default file, containing default environment variables for development, is copied into .env.
2. The makefile command `make migrate` is run, applying the SQL schema to the postgres database.

## Windows, VSCode

1. Install the [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install). This may require changing Windows or Bios settings for virtualization.
2. Install Docker Engine through [Docker Desktop](https://www.docker.com/products/docker-desktop/). Start Docker Engine.
3. Install [VSCode](https://code.visualstudio.com/) and [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
4. Run command `Clone repository into container volume.` and enter the name of the repository: `VerdanTech/VerdanTech-Backend`. Cloning the repository into the container brings optimal performance, but if that doesn't work, clone the repository into a Windows folder and run `Run folder in container.`

The container should display a terminal with no errors.

### Troubleshooting
- Is Docker Engine running?

## Windows

Instructions for the use of Devcontainers on Linux should be simpler than on Windows, but the instructions have not been created yet. If you follow this path, please update this document.

# Non-devcontainer

Instructions for manual setup of the environment have not yet been created. If you follow this path, please update this document.

Some differences from the devcontainer setup to keep in mind:
1. The devcontainer setup does not make use of virtual environments. If setting up without a container, virtual environments can be created with the *uv* package.