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
  <a href="https://github.com/Verdagraph">
    <img src="https://github.com/Verdagraph/.github/blob/main/profile/graphics/logo.png" alt="Logo" width="200" height="200">
  </a>

<h3 align="center">Verdagraph - Web Application</h3>

  <p align="center">
    A garden productivity tool, agro-ecology model, and IoT platform
    for a sustainable and cooperative future.
    <br />
    <!-- 
    <a href=""><strong>Try it yourself »</strong></a>
    <br />
    -->
    <br />
    <a href="https://verdagraph.org">Documentation</a>
    <!-- 
    ·
    <a href="https://youtu.be/jGFHhRVdxRM">YouTube</a>
    ·
    <a href="">Donate</a>
    --> 
    <br />
  </p>
</div>

See the [documentation](https://verdagraph.org) for background on this repository.

This repository is a monorepo using [Turbo](https://turborepo.com/) on top of PNPM and contains the following components:

- `packages` This folder contains all reusable library code. It contains the following packages:
  - `typescript-config`, `eslint-config`, `tailwind-config` Common configuration files.
  - `models` Contains the database schemas, validation logic, and associated business logic for the domain models of the application.
  - `ui` Contains all reusable components used across the other projects.

- `apps` This folder contains the following applications:
  - `docs` The landing page and documentation site.
  - `demo` A minimal version of the client application for demonstrating functionality.
  - `web` The client application.
  - `server` A backend process, used currently for authentication.

- `design` This folder contains domain models & wireframes, and is used to plan features before implementation.

The database in use is the [Triplit](https://www.triplit.dev/) project, which provides a full-stack database with built-in multi-client sync and real-time queries. The frontend is a statically built SvelteKit application. The backend is a Fastisy server.

The key dependencies of the project are:

- [Triplit](https://www.triplit.dev/) as a full-stack database.
- [SvelteKit](https://kit.svelte.dev/) as a javascript framework.
- [Fastify](https://fastify.dev/) for the backend service.
- [Orval](https://orval.dev/) for client SDK generation.
- [Tailwind](https://tailwindcss.com/) for styling.
- [Shadcn-svelete](https://www.shadcn-svelte.com/) along with related libraries for components.
- [Konva](https://konvajs.org/) for canvas related features.
- [Radix Colors](https://www.radix-ui.com/colors) for optimized color palettes.

# Contributing

See the [contributing](./contributing.md) for instructions on contributing and setting up the development environment.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- IN-REPO -->

[version-shield]: https://img.shields.io/badge/version-0.0.1-blue?style=for-the-badge
[version-url]: https://github.com/Verdagraph/Webapp/releases
[issues-shield]: https://img.shields.io/github/issues/Verdagraph/Webapp.svg?style=for-the-badge
[issues-url]: https://github.com/Verdagraph/Webapp/issues
[prs-shield]: https://img.shields.io/github/issues-pr/Verdagraph/Webapp.svg?style=for-the-badge
[prs-url]: https://github.com/Verdagraph/Webapp/pulls
[license-shield]: https://img.shields.io/github/license/Verdagraph/Webapp.svg?style=for-the-badge
[license-url]: https://github.com/Verdagraph/Webapp/LICENSE.txt
