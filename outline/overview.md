# VerdanTech Conceptual Outline

The purpose of this folder is to define high-level, abstract designs of application features. Ideally, it should serve as a prototyping space common to backend developers, frontend developers, and users.

## Document Types

Each subfolder contains one or more design documents. Currently, these documents can include:
- **models.md** - A markdown document containing specifications for domain models. See the [Backend Background](../README.md#background-1) section of the main readme for an explanation of what domain models are. Model descriptions should roughly pseudocode the required attributes of the Python implementations, and contain general descriptions of the behaviours, including relationships with other models.
- **dto.md** - A markdown document containing specifications for data transfer objects. Data transfer objects are the datastructures that bridge the frontend and backend of the application. DTO descriptions should roughly pseudocode the required attributes of the Python implementations and OpenAPI spec.
- **wireframes/** - One or more wireframe documents. Wireframes are rough sketches of the user interface.
- **use-flows.md** - A markdown documents containing flowchart diagrams detailing the path between various wireframes and application states.

## Feature Categories

Each subfolder represents a feature category. Obviously, most features overlap, so the categorization is intended to be loose and only assist in grouping together similar concepts in the application.

| Category     | Description |
|--------------|-------------|
| [Static Pages](static-pages/overview.md) | Website pages that are not part of the application, including the landing page, project description page, donation page, etc. |
| [User](user/overview.md) | User management system including email management, password management, authentication, etc.  | 
| [Garden](garden/overview.md) | Gardens are containers for multiple Workspaces, as well as general environments for all other model state, and the users to interact with it. |