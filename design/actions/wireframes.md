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

Every Task completes with a single tap, regardless of type - what that tap actually does, and which types can be completed another way instead, is [Actions models](models.md#completed)'s rule, not restated here. The only thing specific to this view: a tapped row can expand inline to fill in a type's extra fields (e.g. mass for a Harvest) before confirming, without leaving the Workbook.

## Real-time collaboration

Because a Garden's Tasks are shared, live Triplit state, a Task completed by one User disappears from everyone else's agenda immediately. This matters most when more than one person is working the same Garden at once - it's what keeps two people from independently harvesting, or watering, the same bed.
