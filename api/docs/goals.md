USER_LIST
Filter users by list of ids, usernames, membership in a garden, username starting with
calls:
Application layer(user_list)

USER_DETAIL
Filter users by id, or username. Returns more details for self
calls:
Application layer(user_detail)

USER_CHECK_USERNAME
Filtes by username. True if available and valid
calls:
Application layer(check_username(username_validator, etc))

USER_CREATE
Creates a new user. Sends email verification
calls:
Application layer(user_create) ->
validate fields
generate hashed password
generate key
create new user
send email
persist

USER_CHANGE
Change username, password
calls:
Application layer(user_change) ->
validate fields
query
hash password
change object
persist

USER_CHANGE_EMAIL
Request email change
calls:
Application layer(email_change_request) ->
validate fields
query
generate_key
remove old email
change object
send email
persist


USER_EMAIL_VERIFICATION_REQUEST
USER_EMAIL_VERIFICATION_CONFIRM

USER_PASSWORD_RESET_REQUEST
USER_PASSWORD_RESET_CONFIRM

USER_DELETE_REQUEST
Request a deletion
calls:
Application layer(user_delete_request) ->
query
generate key
update object
send email
persist

USER_DELETE_CONFIRM
Confirm a deletion
calls:
Application layer(user_delete_confirm) ->
query

USER_LOGIN
USER_LOGOUT