# Background

Welcome to the documentation for the backend of VerdanTech. This documentation was made using mkdocs, and can be viewed as html by running `venv/bin/mkdocs serve`, or with `make docs.` 

## Documentation structure

- [Setup](setup.md) - Installation instructions for development and production builds.
- [Changelog](changelog.md) - Version history.
- [Roadmap](roadmap.md) - Future features.
- [Architecture](architecture.md) - Key software principles and their application in this project.
- [Codebase](codebase/overview.md) - Direct documentation of the codebase.
- [Contributing](contributing.md) - Guide for contributing
- [Release Notes](release_notes.md) - Release notes
- [Community](community.md) - Community

## Background

In short, this backend is an asynchronous HTTP and websocket application in Python. It was designed with a few key goals in mind:

- *Extensibility* - The maximial ability to add new features with the minimum amount of friction. Clean architecture that fulills min coupling max cohesion, and the use of python as a general purpose easy to understand language to do it.
- *Performance* - Using litestar, mongo


# Contributing