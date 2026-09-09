---
status: This document is behind of the implementation.
---

# Plants - Models

```mermaid
---
title: Plants Domain Model
---
classDiagram

    Lifespan --> LocationHistory : refers to one
    Lifespan --> GeometryHistory : refers to one
    Lifespan --> Harvest : refers to N
    Plant --> Lifespan : refers to two
    PlantGroup --> Plant : refers to N
    DraftBucket --> Plant : refers to N

    class Lifespan{
        origin: OriginEnum
        locationHistory: LocationHistory
        geometryHistory: GeometryHistory
        seedDate: date
        germDate: date
        floweringDates: set of Date
        expiryDate: date
        dormancyDates: set of Date
        growthDates: set of Date
        harvests: set of Harvest
    }
    class Harvest {
        date: date
        mass: number
        units: number
        quality: HarvestQualityEnum
    }
    class Plant {
        cultivarName: string
        name: string
        recordedLifespan: Lifespan
        expectedLifespan: Lifespan
        aggregate: boolean
    }
    class PlantGroup {
        name: string
        plants: set of Plant
    }
    class DraftBucket {
        name: string
        creator: User
        plants: set of Plant
    }
    class LocationHistory {
        Category: Workspace
    }
    class GeometryHistory {
        Category: Workspace
    }
```

# Lifespan

The lifespan stores all data about a plant which may differ from expected to real behaviour.

## origin

The origin stores how the plant was created. Options are:

- directSeed: A seed is sown directly into the area it will reach maturity in.
- seedToTransplant: A seed is sown in one area and then transplanted into the area it will reach maturity in.
- seedlingToTransplant: A seedling is transplanted directly into the area it will reach maturity in.

In direct seed mode, most plants will have one location: the one they were seeded in. In seed to transplant mode, a plant will have at least two locations: the one where it was seeded, usually in a dedicated seed starting area, and where it is transplanted. Both should be defined when the plant is created. In the seedling to transplant mode, the plant starts as a seedling, for example, when seedlings are sourced from a nursery.

## locationHistory and geometryHistory

Both location and geometry may vary over time, as plants move around or grow.

## seedDate, germDate, floweringDates, expiryDate, dormancyDates, growthDates

Stores the key dates for the plants.

- seedDate: The date at which the plant is seeded.
- germDate: The date at which the seed germinated.
- floweringDates: A set, not a single date - a biennial/perennial plant flowers or fruits once per cycle, same as it enters and exits dormancy once per cycle, so one date per year is expected rather than one ever. For an annual this will typically hold zero or one date. Optional - not every cultivar is grown past this point (e.g. root and leaf crops are typically harvested before it would ever occur), so it's left empty for those.
- expiryDate: The date at which the plant is removed from the space.
- dormancyDates: This is defined only for biennial or perennial plants. A set of dates which the plant became dormant until the following year. For example, includes the dates a berry bush has stopped producing fruit and vegetation.
- growthDates: This is defined only for biennial or perennial plants. A set of dates which the plant exited dormancy for the year. For example, includes the dates a berry bush has begun vegetative growth again.

## harvests

A variable number of harvests may be assigned to a plant. For plants which have a zero `AnnualLifecycleProfile.firstToLastHarvest` this should include only one harvest, but this may be overridden. Each harvest contains the following attributes:

- date: The date of the harvest.
- mass: The mass of the harvest, in kg.
- quality: The quality of the harvest. May be defective, passable, average, or exceptional
- units: The number of units. This may differ in meaning depending on the plant. For example, for carrots, it could mean the number of roots. For lettuce, it could mean the number of leaves.

# GrowthStage

Not a stored field: a Plant's growth stage is computed from whichever Lifespan is active for a given day (recorded if present, otherwise expected - see the [Planner wireframes](../planner/wireframes.md#layout)). It's what selects an icon pack's SVG variant in the Layout. The stages, bounded by the dates below, are:

- **seed**: `seedDate` to `germDate`. Occurs once, ever.
- **vegetative**: cycle start to the earliest `floweringDates` entry in the current cycle, or straight through to the first-harvest milestone if this Plant's Cultivar has no `germToFlowering` set.
- **flowering-or-fruiting**: that `floweringDates` entry to the first-harvest milestone. Skipped entirely for cultivars with no `germToFlowering` (e.g. most root and leaf crops).
- **harvesting**: the first-harvest milestone to either `expiryDate` or the next `dormancyDates` entry, whichever comes first, covering the last-harvest milestone in between without a separate icon transition at that point.
- **dormant**: biennial/perennial plants only, from a `dormancyDates` entry to the matching `growthDates` entry.
- **expired**: after `expiryDate`.

"Cycle start" is `germDate` for the first cycle, and the most recent `growthDates` entry on or before the focused day for every cycle after - see below.

## Relationship to annual cycles (biennials/perennials)

A plant that flowers and fruits every year doesn't re-germinate each year - it exits dormancy and repeats vegetative → flowering-or-fruiting → harvesting before going dormant again. So for a cycle after the first, the stage boundaries above are computed relative to that cycle's `growthDates` entry instead of `germDate`, using the same Cultivar durations (`germToFlowering`, `germToFirstHarvest`, `firstToLastHarvest`) re-anchored to it, and matched against whichever `floweringDates` entry falls within that cycle's window. This is why `floweringDates`, like `dormancyDates`/`growthDates`, is a set: one entry per cycle, not one ever. The sequence for a long-lived perennial is `seed` once, then `[vegetative → flowering-or-fruiting → harvesting → dormant]` repeating once per year, ending in `expired` only when the Plant is actually removed - `harvesting` never runs into `expired` directly for these, since dormancy intervenes first.

## Relationship to origin

A Plant whose `origin` is `seedToTransplant` or `seedlingToTransplant` may have no `seedDate`/`germDate` of its own - that happened before this Plant's own history began (e.g. at a nursery). Stage computation degrades gracefully for these: it starts at whichever stage the earliest date actually present implies, rather than assuming every earlier stage happened on this Plant's own timeline.

## Relationship to transplanting

Transplanting is deliberately not a growth stage. It's a location/geometry event - recorded via Observe's Transplant type and tracked entirely through `locationHistory`/`geometryHistory` - not a change in the plant's biological appearance. A transplant doesn't advance or reset GrowthStage on its own.

## Relationship to Cultivar's ExpectedGeometryProfile

A Cultivar's `ExpectedGeometryProfile` (see [Cultivars models](../cultivars/models.md#expected-geometry)) scales geometry at the same milestones GrowthStage is bounded by - seedling, flowering, firstHarvest, lastHarvest, expiry, enterDormancy, exitDormancy - used to generate a Plant's default `expectedLifespan.geometryHistory` at creation. The two are deliberately the same set of boundaries read by two different consumers (sizing vs. icon selection), not two parallel vocabularies that happen to overlap - a milestone added for one should be added for the other.

# Plant

A plant represents a physical instance of a plant, or, if that level of granularity is not desired, a group of plants. The purpose of Plant models is:

1. To represent the spatial and temporal extent of plants during the planning phase, so that the can be planned around each other. For example, the more accurate of a model we have of how long a plant is going to last in a particular environment, the better we can plan to replace it with another, maximizing usage of space.
2. To represent the status of a plant in-real-life, for the purposes of tracking its progress, shifting the plan around this progress, and managing Actions associated with cultivating it.

## cultivarName

The plant model may store the name associated with a Cultivar, correlating with the `name` attribute in the Cultivar model. This is preferred to storing a direct reference to a Cultivar entity, as this allows flexibility in changing the CultivarCollection of a Garden without messing with the Plant model instances. When the attributes of a Cultivar are required, the name set on the Plant is used to search through the CultivarCollections set on the Garden.

## recordedLifespan and expectedLifespan

The purpose of storing two Lifespan objects is to clearly delineate between the attributes in the Plant model which have been planned with the software, and those which have been recorded from real life. When a Plant is created, its expectedLifespan is populated based on its Cultivar and any user-provided settings, while its recordedLifespan starts empty and is filled in incrementally as the user records what actually happens to the plant, for example that it has germinated or been harvested. Both are always present on the same Plant instance; there is no separate state or term for a Plant that only has expected data so far. How the two are told apart visually is described in the [Planner wireframes](../planner/wireframes.md#layout).

## aggregate

If true, the model represents several different plants in real life. In this mode, less attention is paid to, for example, how geometry changes over time as plants grow, because the same model represents multiple plants. Instead of tracking individual carrots, we can use one model instance to track a square foot of space which has carrots in it, all planted at the same time.

# PlantGroup

PlantGroups are simple collections of references to Plants which serve to group them together for organizational purposes, e.g. tagging every Plant that belongs to a particular bed, or a particular season. A Plant may belong to any number of PlantGroups.

# DraftBucket

A DraftBucket groups the Plants that make up one unconfirmed plan, so several such plans can be built and compared before any of them are decided on. This is the persisted form of the Add Plants tool's "To Create" bucket described in the [Planner wireframes](../planner/wireframes.md#add-plants): a Plant belongs to at most one DraftBucket, and while it does, it's excluded from official reads of the garden's Plants (Action generation, yield totals, and similar), even though it's an ordinary Plant row and renders in the Layout, Tree, and Calendar like any other. Discarding a plan is an ordinary deletion of every Plant in its DraftBucket; accepting one is just deleting the DraftBucket itself, leaving its Plants in place as ordinary, non-draft Plants.

## creator

The User who started the plan. Since a DraftBucket's Plants are visible to other users of the Garden as an optional overlay rather than official state, `creator` is what lets the UI label whose plan is whose when more than one is visible at once.
