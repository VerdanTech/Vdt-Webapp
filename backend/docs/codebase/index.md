# Codebase Overview

This section of the documentation covers the implementation details of the codebase. All of the docs is auto-generated using `mkdocstrings`.

The codebase is technically a monolith, with all code ultimately running on the same ASGI process. The files are structured in a vertical slice but layered fashion, where each feature/domain category gets a folder with all the components of the architecture specific to that category. 

## Contents

- Common:
    - [Domain](./common/domain.md)
    - [Operations](./common/ops.md)
    - [Interfaces](./common/interfaces.md)
    - [Adapters](./common/adapters.md)
    - [Entrypoints](./common/entrypoints.md)
- User
    - [Domain](./user/domain.md)
    - [Operations](./user/ops.md)
    - [Interfaces](./user/interfaces.md)
