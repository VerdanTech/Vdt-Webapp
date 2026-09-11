---
status: The page structure (Tree/Calendar/Layout/Timeline Selector/Toolbar/Toolbox) roughly matches the implementation. Nearly everything else - the Layout window's rendering rules, Calendar's info-point popups, and every Toolbox Tool except Add Plants' Single mode - is ahead of the implementation.
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
- _Toolbar_: A horizontal toolbar. Includes a Workspaces control based on the one already built for the Workspace Editor (`(config)/workspaces/+layout.svelte`'s "Workspaces" menu: up to 10 workspaces listed directly, plus a "See All" link), extended from single-select to a toggle per workspace - defaulting to just `defaultSelectedWorkspaceId` enabled - so the same control covers both switching to a different single workspace and enabling more than one at once (see [Layout](#multiple-workspaces)). No "Create" option here, unlike the Workspace Editor's version: creating a workspace means setting up its PlantingAreas/Environments before it's useful, which is the Workspace Editor's job, not something to start from a Planner toggle - "See All" is the escape hatch to get there.
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
| Environment>Cultivar>PlantingWindow | Cultivar>Plant | ActionType |

Environment leads rather than Cultivar because a PlantingWindow's actual date range is derived from its Environment's frost dates, not its Cultivar - and a garden typically has only a handful of distinct Environments, so grouping by the thing that determines the window, rather than the thing with the most variety, keeps the tree shallow where it matters.

![Tree Wireframe](./wireframes/tree.excalidraw.png)

## Calendar

![Calendar Wireframe](./wireframes/calendar.excalidraw.png)

A nested tree of horizontal date-range bars, one pane each for Plants, PlantingWindows, and Actions. Its visible range is the Timeline Selector's - the same relationship [Add Plants](#add-plants) and [Observe](#observe) have with its focused day, just applied to a range instead of a point. Independent zoom/pan is a deliberate future direction, not built now - anchoring to the Timeline Selector this way leaves room to layer that in later without restructuring.

#### Plants pane

Nested Cultivar → Plant, matching [Tree](#tree)'s sort order - a garden can easily have more Plants than fit on screen, and collapsing a Cultivar's group is what keeps that manageable structurally, rather than relying on selection alone to narrow things down.

Each Plant is one row, collapsed by default to a single bar blending its `expectedLifespan` and `recordedLifespan` (recorded portion solid, expected portion dashed or outlined - see [Layout](#layout)). Expanding the row - the same expand/collapse used throughout the tree - splits it into two child bars, one per Lifespan, for comparing the full plan against the full recorded reality side by side.

Info points mark a Plant's observations along its bar (one per `PlantObservation` - see [Plants models](../plants/models.md#observations)), and now also its open Tasks, reusing the same marker rather than requiring a separate lookup in the Actions pane. When more than one info point falls on the same day, they shrink and pack into the same space rather than collapse into a single count: up to 2-3 actual icons side by side, and only beyond that a "+N" badge - enough to still see at a glance that a harvest and a task landed on the same day, without the space needed growing unbounded on a crowded day. Either way, clicking opens a popover listing each one individually.

Narrowing a long list stacks three ways: collapsing Cultivar groups (structural), the shared selection (show only what's selected), and an explicit filter by `PlantGroup` tag - independent of selection, for a named subset like "everything in Bed 3" regardless of what's currently clicked.

Selection is Plant-granular: clicking anywhere on a Plant's row, or either of its expanded children, selects the whole Plant - matching Tree and Layout, with no separate "just the Expected span" selection.

A Plant belonging to an open DraftBucket renders with the same "ghost" styling as Layout, governed by the same per-DraftBucket visibility toggle shared across all three views (see [Add Plants](#add-plants)).

#### PlantingWindows pane

Nested Environment → Cultivar → PlantingWindow, matching [Tree](#tree)'s sort order - Environment leads because it's what a PlantingWindow's date range is actually derived from (frost dates), and a garden typically has few distinct Environments to begin with.

#### Environment observations

Recording an Environment observation (e.g. a measured temperature, a frost event) isn't limited to the Workspace Editor - it's reachable from here too, as a quick-action on an Environment's group header in this pane (and the equivalent row in Tree), the same way a Plant's info point popup is a shortcut into Observe rather than a trip to a separate page. This is what eventually makes `TemperatureProfile` (see [Cultivars models](../cultivars/models.md#temperature)) useful: comparing a Cultivar's expected range against what's actually been recorded for the Environment it's planted in.

#### Actions pane

Grouped by target entity (Plant/PlantingArea/Workspace/Garden, per `Action.targetType`) to start. Each Action is one row: a bar spanning its earliest to latest Task date, with each Task as an info point along it - the same marker mechanism as Plant observations, not a new visual language.

Narrowing stacks the same way as the Plants pane: the shared selection narrows to Actions targeting whatever's selected, and an independent filter set - the same My/All Tasks scope Workbook has, plus by assignee, TaskType, and completed/incomplete - narrows regardless of selection.

#### Info point popups

Every info point opens a popup for viewing and acting on the thing it represents, varying by what the point is:

- **Expected observation** (a projection): record it for real, at either the current date or the date it was expected for - both write through the same minimal-observation path Observe uses, just choosing which date to stamp it with. Also reschedulable (the existing move-by-day/week buttons, plus a direct date edit for larger jumps), and deletable for the edge case where a Cultivar-generated projection doesn't apply to this particular Plant.
- **Recorded observation** (a fact): editable (date and type-specific fields, e.g. a Harvest's mass/quality) and deletable (undoing an accidental entry). Never converts back to expected.
- **Task due date**: completes in one tap (the same minimal-write-or-plain-toggle behavior as the Workbook), expandable inline to fill in detail first, reassignable or self-claimable, and reschedulable (setting `dateOverridden` same as anywhere else). Not deletable here - Tasks are mostly system-maintained off an Action, so removing one piecemeal risks drifting out of sync with whatever's maintaining it.
- **Same-day cluster** (more info points on one day than fit as individual icons - see [Calendar](#plants-pane)): clicking the "+N" overflow, or any of the shrunk icons shown alongside it, opens a plain routing list, one line per point, each opening straight into its own popup as above - not a new interaction surface of its own.

A few rules apply across all of these:

- Every action here calls the same write path Observe/Workbook already use - these are shortcuts into that system, not a third way to record the same data.
- Scope is always the one Plant an info point belongs to. Batch operations remain Observe/Workbook's job.
- Action buttons only render under the same `ADMIN`/`EDITOR` editing check used elsewhere in the Verdagraph; a viewer gets a read-only popup.
- Each popup includes an "open in Observe" / "open in Workbook" link for anything beyond these quick actions.

## Layout

![Layout Wireframe](./wireframes/layout.excalidraw.png)

A 2D grid showing every Plant as an icon, positioned and shaped by its active Geometry, blending expected and recorded model state into one picture rather than two separate views of it.

#### Which Geometry is active

For the Timeline Selector's focused day, a Plant renders using the latest `recordedLifespan` Geometry/Location entry dated on or before that day if one exists, otherwise the corresponding `expectedLifespan` entry - the same recorded-over-expected rule used in [Calendar](#calendar). Rendering snaps discretely to whichever entry applies; smoothly interpolating between entries (animating growth instead of jumping between snapshots) is a deliberate future enhancement, not in scope now, but this rule is written to leave room for it later.

A Plant's shape also changes style depending on which Lifespan is driving it, so it's visually clear whether its current state is a projection or something that's actually been recorded. This is separate from, and stacks with, the "ghost" styling used for a Plant in an open DraftBucket (see [Add Plants](#add-plants)).

#### Default icon

Absent a Cultivar `iconPackId`, a Plant renders as its active Geometry's shape (an ellipse, for most plants) filled with the Cultivar's `baseColor`, stroked with `outlineColor`, and labeled in the center with the Cultivar's `abbreviation` in `textColor` (see [Cultivars models](../cultivars/models.md#color)). The shape scales and reshapes with whichever Geometry entry is active, growing over the Plant's life the same way its Geometry does.

#### Icon packs

A Cultivar may instead reference an IconPack (see [Cultivars models](../cultivars/models.md#iconpack-provisional)): a shareable, importable set of SVGs, one per [GrowthStage](../plants/models.md#growthstage), rendered within the same Geometry-driven bounding shape in place of the default fill-plus-abbreviation. A pack needn't cover every stage - any it doesn't provide falls back to the default icon - and the default icon remains the permanent baseline for every Cultivar without a pack, not a placeholder awaiting one.

#### Aggregate plants

A Plant with `aggregate` set typically has a rectangular or polygonal Geometry describing an area rather than one plant's footprint. It renders as that Geometry filled with the Cultivar's color, with a fixed-size icon centered on it - unscaled, unlike a single plant's icon - and a number badge showing its `quantity`, the count of real plants it represents.

#### Interplanting

A Cultivar's `minimumDistance` (see [Cultivars models](../cultivars/models.md#interplanting-provisional)) is visualized as a dotted line around a Plant's icon at that radius, shown for a selected or hovered Plant rather than every Plant at once, to avoid cluttering the grid.

#### Selection

Clicking a Plant highlights it, adds it to the shared plant selection (the same one Observe/Translate/Delete act on), and opens a popup - the same one regardless of how many Plants end up selected, but what it offers changes with that count, since unlike an info point in the Calendar, a clicked Plant icon isn't already tied to one specific observation or Task.

**One Plant selected** behaves like a [Calendar info point](#info-point-popups): instant, single-tap actions, no hand-off needed.

- **Record an observation**: defaults to whichever type its current [GrowthStage](../plants/models.md#growthstage) implies comes next (e.g. a seed-stage Plant defaults to "Record Germination"), with a secondary menu for any other type - the same list Observe itself offers, just pre-defaulted for speed.
- **Complete a Task**: if it has open ones, lists them individually, with the same single-tap-or-expand-for-detail behavior as a Calendar Task info point.
- **Delete**: opens the Delete tool pre-scoped to this Plant rather than deleting inline, so its confirmation step stays intact.

**More than one Plant selected** shows a condensed summary (count, Cultivars represented) instead of one Plant's full detail, and every action becomes a hand-off instead of an inline tap: "Record an observation..." opens Observe pre-scoped to the selection, so its per-plant-override tree does the batching work rather than the popup trying to replicate it; completing a Task in bulk hands off to Workbook the same way; Delete hands off to the Delete tool already scoped to the selection. Same escape-hatch principle as Calendar's popups, just drawing the line at selection size instead of action complexity.

A drag-box selects by intersection: a Plant is included if the box touches its shape at all, not only if fully enclosed. It combines with the existing selection using the conventions common to editors like this - a plain drag replaces the selection, Shift adds to it, Alt subtracts from it, and Shift+Alt intersects it.

Selection is shared with Tree and Calendar, which both highlight whatever's selected. Whether selecting in one view also scrolls the others to reveal it is a separate toggle, off by default - forcing a scroll on every click would be disruptive when working across multiple windows at once.

#### Multiple workspaces

The Layout currently shows one Workspace at a time. The motivating case for showing more than one is dragging a Plant directly between them to transplant it - e.g. from an indoor seed-starting Workspace into an outdoor bed - rather than only via Translate's numeric entry or Observe's Transplant type.

Enabling a Workspace is the Toolbar's Workspaces toggle described above, defaulting to just `defaultSelectedWorkspaceId`. Each enabled Workspace gets its own resizable pane in the Layout - the same `Resizable.Pane` mechanism already used to split Tree/Calendar/Layout themselves, not a new docking system. Calendar's and the Layout's own underlying Plant/PlantingWindow queries simply broaden to every enabled Workspace rather than just the one.

`locationHistory` already supports the actual transplant data-wise (each Location is already scoped to a `workspaceId`, so a Plant having locations across two Workspaces is nothing new). What's still open is the cross-pane drag itself - hit-testing a drag that crosses from one pane's canvas into another's. The Konva→SVG migration (see `AGENTS.md`) is complete, which already makes this considerably more tractable than converting pointer coordinates between separate Konva Stages would have been - each Workspace pane becoming its own positioned `<g>`/nested `<svg>` turns that hit-testing into ordinary DOM geometry. The cross-pane drag and multi-pane layout themselves are still unbuilt.

## Timeline Selector

![Timeline Selector Wireframe](./wireframes/timeline_selector.excalidraw.png)

A three-thumb range slider - begin, focus, end - over a scrollable slider window wider than the selection itself, plus a row of three direct date pickers (one per thumb) and translate buttons (±1 day/week/month). The focus thumb is what sets the Layout's displayed day; begin/end set the range visible in Tree and Calendar.

- **Zoom window**: `beginSlider`/`endSlider` bound the date range actually drawn on the slider, starting two weeks past each side of the selection and expanding automatically as a thumb nears either edge, so the visible window scrolls to keep up with a thumb being dragged toward it rather than needing a separate manual pan.
- **Offset bounds**: the focus day must stay between 1 day and 4 years from each of `beginSelection`/`endSelection` - a range can't collapse to nothing, and can't run unreasonably long either.
- **Reset actions**: one resets just the zoom window back to its two-week-past-each-side default; the other resets the whole selection (range and focus) back to today's default.

#### Dragging focus should translate the range, not shrink it

Dragging the focus thumb is meant to move the whole selection together - begin, focus, and end all shift by the same amount, preserving both the range's length and the focus-to-edge distances. The current implementation (`timelineSelection.svelte.ts`'s `updateSlider`) doesn't quite do this: it clamps the new begin and end values independently against the slider's own min/max bounds, rather than clamping the translation itself. The effect matches a real bug report - once the end of the range reaches the edge of the slider, it gets pinned there while focus keeps moving, so continuing to drag focus shortens the range instead of stopping the translation.

The fix is to clamp once, on the delta, not twice, on each endpoint: compute how far focus moved, reduce that delta if applying it to _either_ begin or end would exceed the slider's bounds, then apply the same (possibly reduced) delta to begin, focus, and end together. The range stops translating cleanly at the boundary - it never shrinks.

## Toolbox Tools

Toolbox tools are opened from the Toolbar and rendered in a panel docked alongside the Tree, Calendar, and Layout windows. Each tool defines its own form and interaction model, but shares the Timeline Selector's focused day and the Layout's spatial cursor when relevant.

### Add Plants

Adds new Plants to the model. The tool window is split into two resizable sections:

- **Form (top)**: builds a temporary "stamp" describing the plant(s) the user is about to place, according to the active mode.
- **To Create (bottom)**: a nested tree of every plant staged for creation so far, styled as closely as possible to the [Tree](#tree) window (grouped by Cultivar, then by individual plant). Entries can be inspected and removed individually before the bucket is committed.

Placing a stamp appends the plants it describes to the To Create bucket. All modes append to the same bucket, so a user may freely switch modes mid-session to build up one arrangement (e.g. a Single plant added alongside a Group of another Cultivar).

#### Drafts are persisted, not local state

The To Create bucket is not transient client state: it is backed by Triplit as a **DraftBucket** (see [Plants model](../plants/models.md#draftbucket)) so it survives navigation and syncs like the rest of the model. Staged plants are ordinary `Plant` rows referencing that DraftBucket - there's no separate draft-shaped entity, since a staged plant is already indistinguishable from a freshly-planned one (neither has recorded data yet).

"Uncommitted" refers specifically to belonging to an open DraftBucket. It's unrelated to whether a Plant has recorded data: a Plant that isn't part of any DraftBucket is real, official garden state from the moment it's created, whether or not its `recordedLifespan` has been filled in (see [Calendar](#calendar) and [Layout](#layout) for how that's shown instead).

Because a staged Plant is a real row, committing a DraftBucket is just deleting the bucket - its Plants don't change, they simply stop being excluded from official reads (Action generation, yield totals, and anything else that shouldn't see a plan still under consideration) the moment nothing references it as a draft anymore.

More than one DraftBucket may exist at once, one per plan under consideration, each with its own creator - useful for seeing what a collaborator is currently drafting, not just your own plans.

Selecting an entry in the To Create tree opens it for the same editing available on any Plant, including `recordedLifespan` fields - useful for retroactively drafting a plant that's already in the ground before formally committing it. Ordinarily, though, a Plant staged this way is expected to carry only projected data; nothing about being in a DraftBucket changes how a Plant behaves otherwise.

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

Records what has actually happened to existing Plants: seeding, germination, flowering or fruiting, entering or exiting dormancy, expiry, transplanting, and harvests. Unlike Add Plants, an observation describes a fact about the real world, not a plan, so there's no draft/commit step - submitting the form writes straight onto the selected Plants' recorded data.

For a type with a matching Task type (Seed, Germinate, Flower, Transplant, Harvest, Expire), recording an observation here also completes that Plant's open Task of the same type - see [Actions models](../actions/models.md#completed).

The tool window is split the same way as Add Plants:

- **Form (top)**: a type selector (Seed, Germinate, Flower, Enter Dormancy, Exit Dormancy, Transplant, Harvest, Expire) swaps in the fields for that type - a date for most types, a destination Location/Geometry for Transplant, and mass, units, and quality for Harvest. The date defaults to the Timeline Selector's focused day. These are the values applied to the whole selection by default.
- **To Record (bottom)**: a tree of the Plants the observation will apply to, driven by the Layout/Tree/Calendar's shared plant selection (the same `pointer`/`group` box-select used elsewhere), not a separate picker.

Every entry in the tree can be expanded to override that one plant's values, including its date, independent of the rest of the batch - not just for Harvest. This makes the common case fast (select 40 seedlings, mark them all germinated today in one submission) without losing the ability to correct a single plant's mass or backdate one plant's date differently from the rest.

### Translate

Adjusts the planned position of existing Plants: a precise, numeric complement to the free-hand dragging the Layout already supports for repositioning a single Plant by hand. Like Observe and Delete, it has no picker of its own - it acts on the shared plant selection.

Translate only ever edits `expectedLifespan`'s Location/Geometry. It's for correcting or replanning where a Plant is meant to go, not for recording that a move actually happened in the garden - that's Observe's Transplant type (see above). Splitting it this way keeps exactly one place, Observe, responsible for anything that touches recorded data.

- An exact destination coordinate, for repositioning one plant precisely.
- A numeric offset (Δx, Δy), applied to every plant in the selection at once, for shifting a whole group without disturbing its arrangement relative to itself - the case free-hand dragging handles worst.

### Delete

Deletes existing Plants from the model. Like Observe, it has no picker of its own - it acts on whatever's in the shared plant selection (the same `pointer`/`group` selection used across Layout, Tree, and Calendar).

Deletion is destructive and there's no undo, so submitting requires an explicit confirmation naming the number of Plants about to be deleted. Deleting a Plant deletes its Actions and Tasks along with it, since an Action tied to a Plant that no longer exists wouldn't mean anything.

### Patterns

Authors and manages the library of saved Pattern templates used by Add Plants' Pattern mode.

- **Library**: a list of saved Patterns, each with a name and an owner - a User or a Garden - following the same visibility model as CultivarCollections (see [Cultivars models](../cultivars/models.md#cultivar-collection)): a HIDDEN pattern is visible only to its owner, or, for a garden-owned pattern, to those with read access to that garden.
- **Editor**: selecting a Pattern opens the same Form / To Create bucket editor Add Plants uses, but disconnected from the live Layout and Timeline Selector. A Pattern isn't tied to a real Workspace or date, so its spatial canvas and timeline both work in offsets relative to one origin in the bucket (e.g. the first plant drafted), rather than absolute coordinates and dates.
- **Sharing**: a Pattern can be exported to a JSON file and imported from one, independent of the visibility/ownership above, so it can move between Gardens or be shared outside the app entirely.

### Generators

A form closely mirroring the `Generator`/`GeneratorObjective` models ([Planner models](models.md#generator)), rather than introducing its own shape:

- **Horizon**: a number input, in days.
- **Strategy**: a select. Simulated Annealing is the only option for now, but it's a select rather than being hardcoded since the model already anticipates more.
- **Objective**: a repeatable list of rows, each an objective type (PlantPercentages, Calories, NutrientProfile, Biodiversity, PollinatorStrength, MinimalLabour) paired with a weight - matching `GeneratorObjective`'s `objectives` map directly, one row per key.
- **Include/Exclude Plants**: two multi-select combo-boxes of Cultivar names, matching `includePlants`/`excludePlants`.

Running a Generator doesn't write to the model directly - it produces a new DraftBucket (see [Add Plants](#drafts-are-persisted-not-local-state)), authored with this Generator's configuration as its creator's intent, and hands off to the same To Create view Add Plants uses. A generated plan is reviewed, ghost-compared, edited, and committed or discarded exactly like a manually-built one - the generator is just a different way of populating a bucket, not a separate commit path.

### Layout Config

The same tool as the Workspace Editor's `layoutConfig` (`packages/ui/src/components/workspaces/editor/tools/LayoutConfigForm.svelte`) - shared, not redesigned separately, since both are configuring the same kind of rendering surface. Whatever settings land there (grid/snapping, units, default zoom, and similar display options) apply here unchanged.

# Workbook

The Workbook is a view of the Actions used as references when completing tasks and updating the model day-to-day. See the [Actions wireframes](../actions/wireframes.md) for its layout, assignment, and task-completion workflow.
