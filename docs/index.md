# Introduction

Welcome to the documentation for the backend of VerdanTech. This documentation was made using *mkdocs*. If you plan to run this documentation locally, that can achieved by running `make docs` in the backend development environment. 

## Contents

- [Setup](setup.md) - Installation instructions for development and production builds.
- [Changelog](changelog.md) - Version history.
- [Codebase](codebase/overview.md) - Architecture and implementation documentation.

## Background

In short, this backend is an asynchronous HTTP and websocket application in Python. It was designed with a few key goals in mind:

- *Simple at its Core*: The core domain / "business logic" is written in plain python with a domain-driven architecture, meaning this logic does not depend on any other details of the application. This allows the core logic to be as close as possible to non-technical descriptions of the problem domain. In theory, this reduces the impedance between the ecological knowledge of people and the digital world.
- *Low Coupling, High Cohesion*: Application logic is dependent upon abstract interfaces, allowing the implementation details of infrastructure to be changed independently from the domain logic.
- *Free, Open Software*: All libraries and services used should be open-source and self-hostable, allowing the application itself to be self-hosted. 

Some things that are not as important:

- *Performance*: While the use of the peformant async API framework *Litestar* goes a long way towards improving performance, Python is limited in this regard. Performance is not likely to become a concern until the application scales significantly.

# Contributing

First, join the [discord server](https://discord.gg/XH4kQcpz9p). If you have an idea for a contribution to make, talk to other contributors first to establish what the contribution should look like.

A [Github Project](https://github.com/orgs/VerdanTech/projects/1) is used to organize tickets for the web app. Tickets are automatically assigned issues when connected to a repository. Generally, tickets should be made such that we can maintain one branch per ticket and they can be done independently. 

Code review is required by other contributors before a feature can be merged.

CI including commit hooks and Github Actions has not been done yet, but there is a ticket for it.

A specific versioning system has not yet been put in place, but will sometime before production.