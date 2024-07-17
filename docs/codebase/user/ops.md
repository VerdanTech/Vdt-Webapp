# User Operations

## Command Handlers

### ::: src.user.ops.commands.create_user
    options:
      show_root_heading: true
### ::: src.user.ops.commands.update_user
    options:
      show_root_heading: true
### ::: src.user.ops.commands.request_email_confirmation
    options:
      show_root_heading: true
### ::: src.user.ops.commands.confirm_email_confirmation
    options:
      show_root_heading: true
### ::: src.user.ops.commands.request_password_reset
    options:
      show_root_heading: true
### ::: src.user.ops.commands.confirm_password_reset
    options:
      show_root_heading: true

## Event Handlers

### ::: src.user.ops.events.process_email_confirmation
    options:
      show_root_heading: true
### ::: src.user.ops.events.process_password_reset
    options:
      show_root_heading: true
### ::: src.user.ops.events.send_email_confirmation
    options:
      show_root_heading: true
### ::: src.user.ops.events.send_password_reset
    options:
      show_root_heading: true

## Queries

### QueryResults

#### ::: src.user.ops.queries.EmailSchema
    options:
      show_root_heading: true
#### ::: src.user.ops.queries.UserFullSchema
    options:
      show_root_heading: true
#### ::: src.user.ops.queries.UserPublicSchema
    options:
      show_root_heading: true
#### ::: src.user.ops.queries.PasswordVerificationResult
    options:
      show_root_heading: true

### Queries

#### ::: src.user.ops.queries.UserPasswordVerificationQuery
    options:
      show_root_heading: true
#### ::: src.user.ops.queries.UserPublicProfilesQuery
    options:
      show_root_heading: true

### Query Handlers

#### ::: src.user.ops.queries.verify_password
    options:
      show_root_heading: true
#### ::: src.user.ops.queries.public_profiles
    options:
      show_root_heading: true
#### ::: src.user.ops.queries.client_profile
    options:
      show_root_heading: true