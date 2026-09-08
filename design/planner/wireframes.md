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

A Plant's row renders its `expectedLifespan` and `recordedLifespan` as visually distinct spans across the day columns, e.g. the recorded portion solid and the expected portion dashed or outlined, so it's clear at a glance which of its dates are still projections and which have actually happened.

## Layout

![Layout Wireframe](./wireframes/layout.excalidraw.png)

A Plant's shape reflects whichever of `expectedLifespan` or `recordedLifespan` is driving its current rendering, and changes style depending on which one that is, so it's visually clear whether the plant's current state is a projection or something that's actually been recorded. This is separate from, and stacks with, the "ghost" styling used for drafted plants (see [Add Plants](#add-plants)).

## Timeline Selector

![Timeline Selector Wireframe](./wireframes/timeline_selector.excalidraw.png)

## Toolbox Tools

Toolbox tools are opened from the Toolbar and rendered in a panel docked alongside the Tree, Calendar, and Layout windows. Each tool defines its own form and interaction model, but shares the Timeline Selector's focused day and the Layout's spatial cursor when relevant.

### Add Plants

Adds new Plants to the model. The tool window is split into two resizable sections:

- **Form (top)**: builds a temporary "stamp" describing the plant(s) the user is about to place, according to the active mode.
- **To Create (bottom)**: a nested tree of every plant staged for creation so far, styled as closely as possible to the [Tree](#tree) window (grouped by Cultivar, then by individual plant). Entries can be inspected and removed individually before the bucket is committed.

Placing a stamp appends the plants it describes to the To Create bucket. All modes append to the same bucket, so a user may freely switch modes mid-session to build up one arrangement (e.g. a Single plant added alongside a Group of another Cultivar).

#### Drafts are persisted, not local state

The To Create bucket is not transient client state: it is backed by Triplit as a **DraftBucket** (see [Plants model](../plants/models.md#draftbucket)) so it survives navigation and syncs like the rest of the model. Staged plants are ordinary `Plant` rows referencing that DraftBucket — there's no separate draft-shaped entity, since a staged plant is already indistinguishable from a freshly-planned one (neither has recorded data yet).

"Uncommitted" refers specifically to belonging to an open DraftBucket. It's unrelated to whether a Plant has recorded data: a Plant that isn't part of any DraftBucket is real, official garden state from the moment it's created, whether or not its `recordedLifespan` has been filled in (see [Calendar](#calendar) and [Layout](#layout) for how that's shown instead).

Because a staged Plant is a real row, committing a DraftBucket is just deleting the bucket — its Plants don't change, they simply stop being excluded from official reads (Action generation, yield totals, and anything else that shouldn't see a plan still under consideration) the moment nothing references it as a draft anymore.

More than one DraftBucket may exist at once, one per plan under consideration, each with its own creator — useful for seeing what a collaborator is currently drafting, not just your own plans.

Selecting an entry in the To Create tree opens it for the same editing available on any Plant, including `recordedLifespan` fields — useful for retroactively drafting a plant that's already in the ground before formally committing it. Ordinarily, though, a Plant staged this way is expected to carry only projected data; nothing about being in a DraftBucket changes how a Plant behaves otherwise.

#### Visualizing drafts against the existing model

Because a DraftBucket's Plants and the garden's official Plants render together, they must be unambiguous at a glance. A Plant not in any DraftBucket renders normally; one that is renders as a distinct "ghost" style (e.g. translucent fill, dashed outline) everywhere Plants are drawn, starting with the Layout.

Each DraftBucket's ghosts are toggleable independently of the others, so the user can show or hide one plan's drafts to compare its effect against the current model state, or against another plan's drafts, without committing anything.

#### Exporting as a Pattern

Instead of committing, the To Create bucket can be exported as a Pattern: this captures every one of its Plants' spatial position and planting day as offsets relative to one origin in the bucket, into a shareable JSON template, without touching the model.

The Patterns Toolbox tool used to author and manage saved Pattern templates is this same bucket editor, disconnected from the live Layout and Timeline Selector: it edits an unattached DraftBucket using relative coordinates and days instead of absolute ones, and saves rather than commits.

#### Placement

Each stamp is anchored in two dimensions:

- **Temporal**: the focused day of the Timeline Selector. Placing a stamp always stages it at that day; there is no independent date picker within the tool.
- **Spatial**: a visible cursor over the Layout, positioned either by dragging the cursor directly or by entering coordinates in the form. Its position is shared with the Layout's other spatial tools.

A stamp is placed in one of two ways:

- Clicking the Layout or Timeline anchors the stamp at the click location (Layout) or at the clicked day (Timeline), updating the cursor/focused day and staging the stamp in the same action.
- A keyboard-only method stages the stamp at the current cursor position and focused day, for users who prefer not to leave the keyboard.

#### Modes

The form's mode determines what kind of stamp it produces:

- **Single**: one plant of one Cultivar.
- **Group**: several plants of one Cultivar, arranged with a simple repeatable spatial and temporal pattern (e.g. a grid of a fixed spacing, repeated every N days).
- **Pattern**: an arbitrary, pre-saved spatio-temporal template covering possibly multiple Cultivars and lifecycles, applied via the same relative-offset mechanism used to export one (see above). Selecting a Pattern here only applies it; it does not edit the saved template.

### Observe

Records what has actually happened to existing Plants: seeding, germination, entering or exiting dormancy, expiry, transplanting, and harvests. Unlike Add Plants, an observation describes a fact about the real world, not a plan, so there's no draft/commit step — submitting the form writes straight onto the selected Plants' recorded data.

For a type with a matching Task type (Seed, Germinate, Transplant, Harvest, Expire), recording an observation here also completes that Plant's open Task of the same type — see [Actions models](../actions/models.md#completed).

The tool window is split the same way as Add Plants:

- **Form (top)**: a type selector (Seed, Germinate, Enter Dormancy, Exit Dormancy, Transplant, Harvest, Expire) swaps in the fields for that type — a date for most types, a destination Location/Geometry for Transplant, and mass, units, and quality for Harvest. The date defaults to the Timeline Selector's focused day. These are the values applied to the whole selection by default.
- **To Record (bottom)**: a tree of the Plants the observation will apply to, driven by the Layout/Tree/Calendar's shared plant selection (the same `pointer`/`group` box-select used elsewhere), not a separate picker.

Every entry in the tree can be expanded to override that one plant's values, including its date, independent of the rest of the batch — not just for Harvest. This makes the common case fast (select 40 seedlings, mark them all germinated today in one submission) without losing the ability to correct a single plant's mass or backdate one plant's date differently from the rest.

### Translate

Adjusts the planned position of existing Plants: a precise, numeric complement to the free-hand dragging the Layout already supports for repositioning a single Plant by hand. Like Observe and Delete, it has no picker of its own — it acts on the shared plant selection.

Translate only ever edits `expectedLifespan`'s Location/Geometry. It's for correcting or replanning where a Plant is meant to go, not for recording that a move actually happened in the garden — that's Observe's Transplant type (see above). Splitting it this way keeps exactly one place, Observe, responsible for anything that touches recorded data.

- An exact destination coordinate, for repositioning one plant precisely.
- A numeric offset (Δx, Δy), applied to every plant in the selection at once, for shifting a whole group without disturbing its arrangement relative to itself — the case free-hand dragging handles worst.

### Delete

Deletes existing Plants from the model. Like Observe, it has no picker of its own — it acts on whatever's in the shared plant selection (the same `pointer`/`group` selection used across Layout, Tree, and Calendar).

Deletion is destructive and there's no undo, so submitting requires an explicit confirmation naming the number of Plants about to be deleted. Deleting a Plant deletes its Actions and Tasks along with it, since an Action tied to a Plant that no longer exists wouldn't mean anything.

### Patterns

Authors and manages the library of saved Pattern templates used by Add Plants' Pattern mode.

- **Library**: a list of saved Patterns, each with a name and an owner — a User or a Garden — following the same visibility model as CultivarCollections (see [Cultivars models](../cultivars/models.md#cultivar-collection)): a HIDDEN pattern is visible only to its owner, or, for a garden-owned pattern, to those with read access to that garden.
- **Editor**: selecting a Pattern opens the same Form / To Create bucket editor Add Plants uses, but disconnected from the live Layout and Timeline Selector. A Pattern isn't tied to a real Workspace or date, so its spatial canvas and timeline both work in offsets relative to one origin in the bucket (e.g. the first plant drafted), rather than absolute coordinates and dates.
- **Sharing**: a Pattern can be exported to a JSON file and imported from one, independent of the visibility/ownership above, so it can move between Gardens or be shared outside the app entirely.

# Workbook

The Workbook is a view of the Actions used as references when completing tasks and updating the model day-to-day. See the [Actions wireframes](../actions/wireframes.md) for its layout, assignment, and task-completion workflow.