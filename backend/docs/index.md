# Introduction

Welcome to the documentation for the backend of VerdanTech. This documentation was made using *mkdocs*. If you plan to run this documentation locally, that can achieved by running `make docs` in the backend development environment. 

## Contents

- [Architecture](architecture.md) - Software architecture and design principles used in the project.
- [Changelog](changelog.md) - Version history.
- [Makefile](makefile.md) - Contains descriptions of the development scripts within `makefile`.
- [Environment Variables](environment_vars.md) - Contains descriptions of the environment variables in use.
- [Settings](settings.md) - Contains a list of settings defined within `src/settings`.
- [Resources](resources.md) - Contains a list of tutorials, blogs, and other resources relevant to development.
- [Codebase](./codebase/index.md) - Implementation documentation.

## Background

In short, this backend is an asynchronous HTTP and websocket application in Python. It was designed with a few key goals in mind:

- *Simple at its Core*: The core domain / "business logic" is written in plain python with a domain-driven architecture, meaning this logic does not depend on any other details of the application. This allows the core logic to be as close as possible to non-technical descriptions of the problem domain. In theory, this reduces the impedance between agro-ecological knowledge and the digital world.
- *Low Coupling, High Cohesion*: Application logic is dependent upon abstract interfaces, allowing the implementation details of infrastructure to be changed independently from the domain logic. This increases the adaptability of the project to different technologies.
- *Free, Open Software*: All libraries and services used are open-source and self-hostable, allowing the application itself to be self-hosted. 

Some things that are not as important:

- *Performance*: While the use of the peformant async API framework *Litestar* goes a long way towards improving performance, Python is limited in this regard. Performance is not likely to become a concern until the application scales significantly.