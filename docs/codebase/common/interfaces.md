# Common Interface Definitions

## Persistence

### ::: src.common.interfaces.persistence.repository.AbstractRepository
    options:
      show_root_heading: true
### ::: src.common.interfaces.persistence.uow.AbstractRepositoryContainer
    options:
      show_root_heading: true
### ::: src.common.interfaces.persistence.uow.AbstractUow
    options:
      show_root_heading: true

### Exceptions

#### ::: src.common.interfaces.persistence.exceptions.RepositoryError
    options:
      show_root_heading: true
#### ::: src.common.interfaces.persistence.exceptions.RoutineRepositoryError
    options:
      show_root_heading: true
#### ::: src.common.interfaces.persistence.exceptions.FatalRepositoryError
    options:
      show_root_heading: true
#### ::: src.common.interfaces.persistence.exceptions.InterfaceRepositoryError
    options:
      show_root_heading: true
#### ::: src.common.interfaces.persistence.exceptions.ObjectNotFound
    options:
      show_root_heading: true
#### ::: src.common.interfaces.persistence.exceptions.ObjectAlreadyExists
    options:
      show_root_heading: true

## Events

### ::: src.common.interfaces.events.node.AbstractEventNode
    options:
      show_root_heading: true

## Email

### ::: src.common.interfaces.email.client.AbstractEmailClient
    options:
      show_root_heading: true

## Security

### ::: src.common.interfaces.security.passwords.AbstractPasswordCrypt
    options:
      show_root_heading: true

###