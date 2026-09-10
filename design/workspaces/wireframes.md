---
status: This document is behind the implementation.
---

# Workspaces - Wireframes

The Workspace wireframes allow:

- Viewing all the workspaces in a garden
- Creating a new workspace
- Editing a workspace, including adding/updating PlantingAreas, using two views: the Tree and Layout

## Viewing workspaces

![Workspaces Wireframes](./wireframes/workspaces.excalidraw.png)

## Creating workspaces

![Create Workspace Wireframe](./wireframes/create.excalidraw.png)

## Viewing/Editing a workspace

![Workspace Wireframe](./wireframes/workspace.excalidraw.png)

The editor's Toolbox includes tools for adding PlantingAreas and Environments (`plantingAreaCreate`/`environmentCreate`), translating and deleting them, an Expire tool, and Layout Config - see [Environment wireframes](../environment/wireframes.md) for why Environment editing lives here rather than as its own page. Add is mostly done as-is; this domain still needs two things existing tools don't cover:

- **Moving a Workspace itself**, as opposed to `translate`'s job of moving a PlantingArea/Environment within one - reading "moving workspaces" as repositioning a Workspace's own spatial reference rather than something inside it. This is also what the Planner's [multiple-workspace tiling](../planner/wireframes.md#multiple-workspaces) will eventually need, to arrange which Workspace sits where relative to the others.
- **Recording Environment observations** (a measured temperature, a frost event) - mirroring Plant's Observe, but for Environments. Also reachable from the [Planner](../planner/wireframes.md#environment-observations), not just here.
