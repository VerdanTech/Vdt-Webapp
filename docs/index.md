# 

Welcome to the documentation for the backend of VerdanTech. This documentation was made using mkdocs, and can be viewed as html by running `venv/bin/mkdocs serve`, or with `make docs.` 

## Contents

- [Setup](setup.md) - Installation instructions for development and production builds.
- [Changelog](changelog.md) - Version history.
- [Roadmap](roadmap.md) - Future features.
- [Codebase](codebase/overview.md) - Architecture and implementation documentation.
- [Contributing](contributing.md) - Guide for contributing
- [Release Notes](release_notes.md) - Release notes
- [Community](community.md) - Community

## Background

In short, this backend is an asynchronous HTTP and websocket application in Python. It was designed with a few key goals in mind:

- *Extensibility* - The maximial ability to add new features with the minimum amount of friction. Clean architecture that fulills min coupling max cohesion, and the use of python as a general purpose easy to understand language to do it.
- *Performance* - Using async, litestar, postgres, redis

``` mermaid
classDiagram
direction RL
Operation1 --> Domain : Depends on
Operation2 --> Domain : Depends on
Operation3 --> Domain : Depends on

Endpoint1 --> Operation1 : Depends on
Endpoint2 --> Operation2 : Depends on
Endpoint3 --> Operation3 : Depends on

Domain --> Interfaces: Depends on
Operation1 --> Interfaces : Depends on
Operation2 --> Interfaces : Depends on
Operation3 --> Interfaces : Depends on

Interfaces --> Infrastructure : Implemented by

Infrastructure --> Dependencies : Instantiated by

Dependencies --> Endpoint1 : Injected into
Dependencies --> Endpoint2 : Injected into
Dependencies --> Endpoint3 : Injected into

class Domain {
    Entities
    Value Objects
    Services
}
namespace Application-Operations {
    class Operation1
    class Operation2
    class Operation3
}
namespace Asgi-Shell {
    class Endpoint1
    class Endpoint2
    class Endpoint3
}
class Interfaces
class Infrastructure
class Dependencies
```

# Contributing


Notes on testing: 
- Prefer to use mocker.patch.object over mocker.patch