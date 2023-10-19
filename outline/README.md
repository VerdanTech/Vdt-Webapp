# VerdanTech Conceptual Outline

The purpose of this folder is to define high-level, abstract designs of application features. Ideally, it should serve as a prototyping space common to backend developers, frontend developers, and users.

## Document Types

Each subfolder contains one or more design documents. Currently, these documents can include:
- **models.md** - A markdown document containing specifications for domain models. A domain model is a conceptual model designed to be intuitive by mirroring ways the users think about the problem space the application is trying to solve. See the [Backend Background](../README.md#background-1) section of the main readme for further explanation of what domain models are. Model descriptions should roughly pseudocode the required attributes of the Python implementations, and contain general descriptions of the behaviours, including relationships with other models.
- **dto.md** - A markdown document containing specifications for data transfer objects. Data transfer objects are the datastructures that bridge the frontend and backend of the application. DTO descriptions should roughly pseudocode the required attributes of the Python DTO implementations, OpenAPI spec, and generated Typescript client.
- **wireframes/** - One or more wireframe documents. Wireframes are rough sketches of the user interface.
- **use-flows.md** - A markdown document containing flowchart diagrams detailing the path between various wireframes and application states.

## Feature Categories

Each subfolder represents a feature category. Obviously, most features overlap, so the categorization is intended to be loose and only assist in grouping together similar concepts in the application.

| Category     | Description |
|--------------|-------------|
| [Static Pages](static-pages/README.md) | Website pages that are not part of the application, including the landing page, project description page, donation page, etc. |
| [User](user/README.md) | User management system including email management, password management, authentication, etc.  | 
| [Garden](gardens/README.md) | Gardens are containers for multiple Workspaces, as well as general environments for all other model state, and a connection between users to interact with it. |
| [Plant](plants/README.md) | Plants are represented in two ways: as collections of attribute models defining expected behaviours of plant species, and as instances of those species with known locations in space and time. |
| [Workspace](workspaces/README.md) | Workspaces are containers which give spatial context to objects such as plants, planting containers, and devices. |
| [Planner](planner/README.md) | Planner models are tools for describing past, present, and planned plant instances together, as well as generating plans based on constraints and objectives.
| [Differential synchronization](differential-synchronization/README.md) | The differential synchronization algorithm is used to allow smooth collaborative editing between multiple clients. |
| [Actions](/README.md) | . |
| [Devices](/README.md) | . |