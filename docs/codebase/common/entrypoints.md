# Common Entrypoint Definitions

## Litestar ASGI

### ::: src.common.entrypoints.litestar.app.create_app
    options:
      show_root_heading: true
### ::: src.common.entrypoints.litestar.auth.retrieve_user_handler
    options:
      show_root_heading: true
### ::: src.common.entrypoints.litestar.auth.jwt_cookie_auth
    options:
      show_root_heading: true
### ::: src.common.entrypoints.litestar.channels_backend.NatsChannelsBackend
    options:
      show_root_heading: true

## Taskiq Task Backend

### ::: src.common.entrypoints.taskiq.app.process_event
    options:
      show_root_heading: true
### ::: src.common.entrypoints.taskiq.app.main
    options:
      show_root_heading: true