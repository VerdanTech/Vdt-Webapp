# 

Welcome to the documentation for the backend of VerdanTech. This documentation was made using mkdocs, and can be viewed as html by running `make docs.` 

## Contents

- [Setup](setup.md) - Installation instructions for development and production builds.
- [Changelog](changelog.md) - Version history.
- [Codebase](codebase/overview.md) - Architecture and implementation documentation.
- [Contributing](contributing.md) - Guide for contributing
- [Community](community.md) - Community

## Background

In short, this backend is an asynchronous HTTP and websocket application in Python. It was designed with a few key goals in mind:

- *Extensibility* - The maximial ability to add new features with the minimum amount of friction. Clean architecture that fulills min coupling max cohesion, and the use of python as a general purpose easy to understand language to do it.
- *Performance* - Using async, litestar, postgres, redis

![Architecture Diagram](architecture.excalidraw.png)

# Contributing


Notes:
- In domain models, avoid assigning collections back into themselves. Instead of:

self.emails = [
    email.make_unprimary()
    for email in self.emails
    if email != new_primary_email
]

use:
for index, email in enumerate(self.emails):
    if email != new_primary_email:
        self.emails[index] = email.make_unprimary()

This is because SqlAlchemy has proven to be a slightly leaky abstraction when mapping domain objects, as it messes with assignment of collections.
- Prefer to use mocker.patch.object over mocker.patch