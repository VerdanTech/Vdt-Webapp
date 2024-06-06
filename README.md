<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables  
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Version][version-shield]][version-url]
[![Issues][issues-shield]][issues-url]
[![Pull Requests][prs-shield]][prs-url]

<!-- PROJECT LOGO -->
<div align="center">

<h3 align="center">VerdanTech-Backend</h3>

<p align="center">
A garden productivity API built with async Python. 
<br />
<a href="https://github.com/VerdanTech/VerdanTech-Deployment"><strong>Deploy it yourself »</strong></a>
<br />

<a href="https://github.com/github_username/repo_name">Report Bug</a>
·
<a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
·
<a href="link to discord">Discord</a>
·
<a href="https://youtu.be/jGFHhRVdxRM">YouTube</a>
<br />
</p>

</div>

The python backend implements a clean architecture pattern, meaning that the functions of the application are segregated in a way that minimizes coupling. Quick summaries for the layers:
- The domain layer holds the core business logic and is made up of four components: Entities, which are objects with IDs and individuality that represent concepts in the problem space, RootEntities which are entities that make up Collections of documents or SQL tables in the database, meaning they represent consistency boundaries of data, value objects, which are ID-less and immutable, and represent individual-less states, and services, which encapsulate core logic in the problem domain that can't be relegated to any of the other options. All these concepts are implemented using native Python dataclasses. The domain layer also holds interfaces that are relied upon by the domain layer and application layer
- The application layer orchestrates the domain layer and connects it to implementations of the interfaces. The application layer has two parts: the operaions sections, which are high level application functions and make up the main API (are-one to one with http API routes), and the services sections, which comprise more granular orchestrations of the domain logic and are called in the operations.
- The infrastrure contains implementations of the domain service interfaces, such as database implementations of the repository interface. The only repository in use so far is a MongoDB Motor (async pymongo) implementation. The repository abstraction makes it possible to use different implementations in the future, but I havent investigated the potential compatibility with a sql database (plan to stick with mongo)
- The API layer is the http and websocket wrapping around the application layer, and is implemented using the Litestar 

Why repository and data mappers ? https://shawnmc.cool/active-record-how-we-got-persistence-perfectly-wrong


# Development

## Environment

The current workflow for setting up development environments is standardized to use [Development Containers](https://containers.dev/). This allows testing with real service dependencies while maximizing reproduceability with minimal effort It comes at the cost of requiring the VSCode IDE and Docker. Currently there only exists one instruction set for use with Windows, but more will be added as needed.

### Windows Devcontainer

1. Install the [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install). This may require changing Windows or Bios settings for virtualization.
2. Install Docker Engine through [Docker Desktop](https://www.docker.com/products/docker-desktop/) Start Docker Engine.
3. Install [VSCode](https://code.visualstudio.com/) and [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
3. Run command `Clone repository into container volume.` and enter the name of the repository: `VerdanTech/VerdanTech-Backend`. Cloning the repository into the container brings optimal performance, but if that doesn't work,clone the repository into a Windows foldew and run `Run folder in container.`
4. Copy .env-default into .env.
5. Run `make migrate`.

## Documentation

## Contributing




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- IN-REPO -->
[version-shield]: https://img.shields.io/badge/version-0.0.1-blue?style=for-the-badge
[version-url]: https://github.com/nathanielarking/Autonomous-Agriculture/releases
[issues-shield]: https://img.shields.io/github/issues/nathanielarking/VerdanTech.svg?style=for-the-badge
[issues-url]: https://github.com/nathanielarking/VerdanTech/issues
[prs-shield]: https://img.shields.io/github/issues-pr/nathanielarking/VerdanTech.svg?style=for-the-badge
[prs-url]: https://github.com/nathanielarking/VerdanTech/pulls
[license-shield]: https://img.shields.io/github/license/nathanielarking/VerdanTech.svg?style=for-the-badge
[license-url]: https://github.com/nathanielarking/VerdanTech/LICENSE.txt
