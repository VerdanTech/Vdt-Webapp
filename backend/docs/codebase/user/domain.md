# User Domain

## Entities
### ::: src.user.domain.models.User
    options:
      show_root_heading: true

## Value Objects
### ::: src.user.domain.models.Email
    options:
      show_root_heading: true
### ::: src.user.domain.models.EmailConfirmation
    options:
      show_root_heading: true
### ::: src.user.domain.models.PasswordResetConfirmation
    options:
      show_root_heading: true
### ::: src.user.domain.models.BaseConfirmation
    options:
      show_root_heading: true

## Commands
### ::: src.user.domain.commands.UserCreateCommand
    options:
      show_root_heading: true
### ::: src.user.domain.commands.UserUpdateCommand
    options:
      show_root_heading: true
### ::: src.user.domain.commands.UserRequestEmailConfirmationCommand
    options:
      show_root_heading: true
### ::: src.user.domain.commands.UserConfirmEmailConfirmationCommand
    options:
      show_root_heading: true
### ::: src.user.domain.commands.UserRequestPasswordResetCommand
    options:
      show_root_heading: true
### ::: src.user.domain.commands.UserConfirmPasswordResetCommand
    options:
      show_root_heading: true

## Events
### ::: src.user.domain.events.UserCreatedEvent
    options:
      show_root_heading: true
### ::: src.user.domain.events.EmailPendingConfirmationEvent
    options:
      show_root_heading: true
### ::: src.user.domain.events.PasswordPendingResetEvent
    options:
      show_root_heading: true
### ::: src.user.domain.events.EmailConfirmationCreatedEvent
    options:
      show_root_heading: true
### ::: src.user.domain.events.PasswordResetConfirmationCreatedEvent
    options:
      show_root_heading: true