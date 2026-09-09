---
status: This document describes planned functionality; no Workbook implementation exists yet.
---

# Actions - Wireframes

The Workbook is the primary interface for Actions and Tasks: a shared, real-time view for assigning work among a Garden's Users, and for referencing while carrying it out - see the [Planner wireframes](../planner/wireframes.md#workbook) for how it fits alongside the Verdagraph.

## Layout

- **Scope toggle**: My Tasks (assigned to the current User) vs. All Tasks (every Task in the Garden). Defaults to My Tasks.
- **Agenda**: Tasks grouped by date, then by assignee - unlike the Verdagraph Calendar's row-per-Plant spans, a Task is a point in time to act on, not a duration to visualize.
- **Unassigned bucket**: Tasks with no assignee get their own always-visible section, separate from the dated agenda, so nothing auto-generated goes unnoticed.

## Assignment

A Task can be assigned in either direction:

- A User with edit access can assign a Task to another User.
- Any User can self-claim an open Task directly from the Unassigned bucket.

## Completing a Task

Every Task completes with a single tap, regardless of type:

- For a type with a matching Observe type (Seed, Germinate, Flower, Transplant, Harvest, Expire - see [Actions models](models.md#completed)), completing it writes a minimal observation onto its Plant with today's date and no further detail, the same as Observe would. The row can be expanded inline to fill in the same fields Observe shows for that type (e.g. mass for a Harvest), without leaving the Workbook.
- For a type with no matching Observe type (Thin, Harden, Prune, Cover a planting area, Weed a planting area, Till a planting area, Tidy a workspace, Apply fertilizer, Irrigate, Other), completing it is a plain toggle - there's no Plant data to write.
- If the matching observation is recorded through Observe first instead, the Task completes on its own and just shows as already done.

An Action has no completion state of its own - it's done when every one of its Tasks is.

## Real-time collaboration

Because a Garden's Tasks are shared, live Triplit state, a Task completed by one User disappears from everyone else's agenda immediately. This matters most when more than one person is working the same Garden at once - it's what keeps two people from independently harvesting, or watering, the same bed.
