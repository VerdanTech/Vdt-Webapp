# VerdanTech Conceptual Outline

The purpose of this folder is to define high-level, abstract designs of application features. Ideally, it should serve as a prototyping space common to backend developers, frontend developers, and users.

## Document Types

Each subfolder contains one or more design documents. Currently, these documents can include:
- **models.md** - A markdown document containing specifications for domain models. A domain model is a conceptual model designed to be intuitive by mirroring ways the users think about the problem space the application is trying to solve. See the [Backend Background](../README.md#background-1) section of the main readme for further explanation of what domain models are. Model descriptions should roughly pseudocode the required attributes of the Python implementations, and contain general descriptions of the behaviours, including relationships with other models.
- **dto.md - Still deciding whether to include this** - A markdown document containing specifications for data transfer objects. Data transfer objects are the datastructures that bridge the frontend and backend of the application. DTO descriptions should roughly pseudocode the required attributes of the Python DTO implementations, OpenAPI spec, and generated Typescript client.
- **wireframes.md** - A markdown document containing descriptions of wireframes and the interactions between them.
- **wireframes/** - Wireframes are rough sketches of the user interface. Currently, the Excalidraw application is used for its ability to save editable files directly into PNG format. The recommended way to edit these files is to use the [Visual Studio extension](https://marketplace.visualstudio.com/items?itemName=pomdtr.excalidraw-editor) in VS Code or in the browser. For collaborative editing, the [web version](https://excalidraw.com/) can be used.

## Feature Categories

Each subfolder represents a feature category. Obviously, most features overlap, so the categorization is intended to be loose and only assist in grouping together similar concepts in the application.

| Category     | Description |
|--------------|-------------|
| [App Shell](app-shell/README.md) | Wireframes of app-wide navigation bars. |
| [Static Pages](static-pages/README.md) | Website pages that are not part of the application, including the landing page, project description page, donation page, etc. |
| [User](user/README.md) | User management system including email management, password management, authentication, etc.  | 
| [Garden](gardens/README.md) | Gardens are containers for multiple Workspaces, as well as general environments for all other model state, and a space to connect users. |
| [Workspace](workspaces/README.md) | Workspaces are containers which give spatial context to objects such as plants, planting containers, and devices. |
| [Cultivars](cultivars/README.md) | Cultivars are collections of attribute models defining the expected behaviours of plant species. |
| [Plants](plants/README.md) | Plants are physical instances of plants with known locations in space and time, and a reference to a Cultivar. |
| [Planner](planner/README.md) | Planner models are tools for describing past, present, and planned plant instances together, as well as generating plans based on constraints and objectives.
| [Differential Synchronization](differential-synchronization/README.md) | The differential synchronization algorithm is used to allow smooth collaborative editing between multiple clients. |
| [Environment](environment/README.md) | Collections of inputs to the model state including temperatures, rainfall, and pictures. |
| [Actions](actions/README.md) | Collections of outputs from the model state including lists of tasks to be performed. |
| [Devices, Controllers, and Sensors](devices/README.md) | Devices are containers of Controllers and Sensors, which are tools to interface with external APIs. |