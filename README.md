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
<br />
<div align="center">
  <a href="https://github.com/VerdanTech">
    <img src="https://github.com/VerdanTech/.github/blob/main/profile/graphics/logo.png" alt="Logo" width="200" height="200">
  </a>

<h3 align="center">VerdanTech - Web Application</h3>

  <p align="center">
    A garden productivity tool, agro-ecology model, and IoT platform
    for a sustainable and cooperative future.
    <br />
    <!-- 
    <a href=""><strong>Try it yourself »</strong></a>
    <br />
    -->
    <br />
    <a href="https://discord.gg/U8ps6YCc">Discord</a>
    <!-- 
    ·
    <a href="https://youtu.be/jGFHhRVdxRM">YouTube</a>
    ·
    <a href="">Donate</a>
    --> 
    <br />
  </p>
</div>

See the [main project readme](https://github.com/VerdanTech) for background on this repository.

This repository contains the backend server and frontend application of the VerdanTech web application.

The backend is an async Python HTTP and (eventually) websocket API implemented with a domain-driven architecture. From a technical perspective, the main goal of the backend is to be transparent and extensible to the end of adequately capturing the field of agro-ecology within digital models usable for contextualized application. Python is chosen for its ease of use and wide ecosystem.

The frontend is a statically built SvelteKit application. 

The key dependencies of the backend are:
- [Litestar](https://litestar.dev/) as an ASGI framework
- [Taskiq](https://taskiq-python.github.io/) as a task backend
- [Sqlalchemy](https://www.sqlalchemy.org/) + [Alembic](https://alembic.sqlalchemy.org/en/latest/) + [Postgres](https://www.postgresql.org/) for persistence
- [NATS](https://nats.io/) as an event stream
- [Shapely](https://shapely.readthedocs.io/en/stable/) for geometry
- [Attrs](https://www.attrs.org/en/stable/), [Cattrs](https://catt.rs/en/stable/), and [Pydantic](https://docs.pydantic.dev/latest/) for object modelling
- [Passlib](https://pypi.org/project/passlib/) for encryption

The key dependencies of the frontend are:
- [SvelteKit](https://kit.svelte.dev/) as a javascript framework.
- [Svelte Query](https://sveltequery.vercel.app/) as an async state manager.
- [Orval](https://orval.dev/) for client SDK generation.
- [Tailwind](https://tailwindcss.com/) for styling.
- [Shadcn-svelete](https://www.shadcn-svelte.com/) along with related libraries for components.
- [Konva](https://konvajs.org/) for canvas related features.
- [Radix Colors](https://www.radix-ui.com/colors) for optimized color palettes.

# Contributing

See the [contributing](./contributing.md) for instructions on contributing and setting up the development environment. The [backend README](./backend/README.md) and [frontend README](./frontend/README.md) contain instructions for how to view each project's documentation.

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
