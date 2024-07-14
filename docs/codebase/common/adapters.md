# Common Adapters

## Persistence

### Common

#### ::: src.common.adapters.persistence.common.repository.StandardRepositoryContainer
    options:
      show_root_heading: true
#### ::: src.common.adapters.persistence.common.uow.StandardUow
    options:
      show_root_heading: true
#### ::: src.common.adapters.persistence.common.clients.DatabaseClients
    options:
      show_root_heading: true
#### ::: src.common.adapters.persistence.common.mapper.AbstractMapper
    options:
      show_root_heading: true

### Sqlalchemy

#### ::: src.common.adapters.persistence.sqlalchemy.repository.BaseAlchemyRepository
    options:
      show_root_heading: true
#### ::: src.common.adapters.persistence.sqlalchemy.litestar_lifespan.get_alchemy_client
    options:
      show_root_heading: true
#### ::: src.common.adapters.persistence.sqlalchemy.litestar_lifespan.litestar_alchemy_client_lifespan
    options:
      show_root_heading: true
#### ::: src.common.adapters.persistence.sqlalchemy.client.AlchemyClient
    options:
      show_root_heading: true

## Email

#### ::: src.common.adapters.email.common.BaseEmailClient
    options:
      show_root_heading: true