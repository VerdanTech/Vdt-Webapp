---
status: This document roughly matches the implementation when it comes to the layout, but is ahead when it comes to everything else.
---

# Planner - Wireframes

The Planner pages are split into two groups:

- _Verdagraph_: a complex view of the data model through its spatial and temporal aspects, made primarily for manipulating the state of Plants.
- _Workbook_: a calendar-like view of Actions optimized for assigning Actions among Users and using as a reference when carrying out tasks more conveninent than the Verdagraph.

# Verdagraph

The Verdagraph is split into three main views into the model state:

- _Tree_: Displays model attributes into a directory-like tree structure, with the goal of simplicity and easy keyboard navigability.
- _Calendar_: Displays model attributes into a grid-like temporal view, where models are organized as rows, and days are organized as columns.
- _Layout_: Displays model attributes according to their spatial layout.

All three of these windows are toggleable. They are supported by the following additional UI elements:

- _Timeline Selector_: Allows selecting a range of dates easily with the mouse and keyboard. This range dictates which model elements are visible in the Tree and Calendar, with a value within the range being the "focused day" which controls the day displayed in the Layout.
- _Toolbar_: A horizontal toolbar.
- _Toolbox_ A reusable component for storing a list of active tools (ex. "Add Plant", "Record Observation"), allowing the resuse of functionality between Tree, Calendar, and Layout.

![Verdagraph Structure Wireframe](./wireframes/verdagraphStructure.excalidraw.png)

## Tree

Using the [Tree](https://melt-ui.com/docs/builders/tree) component from Melt UI, Plants, PlantingWindows, an Actions are displayed in scrollable windows.

The range of objects displayed is controlled by the TimelineSelector, with the selected day being highlighted.

Buttons:

1. PlantingWindow window toggle button
2. Plants window toggle button
3. Actions window toggle button
4. Sorting menu. The options for sorting are intended to adapt to whatever different use cases emerge. These are the options so far:

| PlantingWindows                     | Plants         | Actions    |
| ----------------------------------- | -------------- | ---------- |
| Cultivar>Environment>PlantingWindow | Cultivar>Plant | ActionType |

![Tree Wireframe](./wireframes/tree.excalidraw.png)

## Calendar

![Calendar Wireframe](./wireframes/calendar.excalidraw.png)

## Layout

![Layout Wireframe](./wireframes/layout.excalidraw.png)

## Timeline Selector

![Timeline Selector Wireframe](./wireframes/timeline_selector.excalidraw.png)

## Toolbox Tools

### Add Plants

# Workbook

The Workbook is a view of the Actions used as references when completing tasks and updating the model day-to-day.