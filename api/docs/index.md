# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.


# Domains
## User

### Entities

User

### Values

Email
EmailConfirmation
PasswordConfirmation

## Garden

### Entities

Garden
GardenMembership

### Values

## Plants

### Entities

PlantSet
PlantType
PlantAttributeProfile

### Values

PlantAttribute

## Workspaces

### Entities

Workspace
PlantingArea
Trellis


## Planner

### Entities

PlantingSchema
PlantInstance

``` mermaid
classDiagram
  Person <|-- Student
  Person <|-- Professor
  Person : +String name
  Person : +String phoneNumber
  Person : +String emailAddress
  Person: +purchaseParkingPass()
  Address "1" <-- "0..1" Person:lives at
  class Student{
    +int studentNumber
    +int averageMark
    +isEligibleToEnrol()
    +getSeminarsTaken()
  }
  class Professor{
    +int salary
  }
  class Address{
    +String street
    +String city
    +String state
    +int postalCode
    +String country
    -validate()
    +outputAsLabel()  
  }
```

``` mermaid
erDiagram
  USER }o..o{ GARDEN : "N-N"
  GARDEN ||..|{ PLANTSET : "1-N"
  PLANTSET ||--|{ PLANT_TYPE : "1-N"
  PLANT_TYPE ||--|{ PLANT_ATTRIBUTE_PROFILE : "1-N"
  GARDEN ||..|{ WORKSPACE : "1-N"
  WORKSPACE ||--|{ PLANTING_AREA: "1-N"
  WORKSPACE ||..o{ PLANTING_SCHEMA : "1-N"
  PLANTING_SCHEMA ||..o{ PLANT_INSTANCE : "1-N"
```

