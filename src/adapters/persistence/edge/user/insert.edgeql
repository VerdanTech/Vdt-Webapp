WITH
  user := <json>$json
INSERT User {
  username := <str>user['username'],
  emails := (
    FOR email IN std::json_array_unpack(user['emails'])
    UNION (
        INSERT Email {
            address := <str>email['address'],
            verified := <bool>email['verified'],
            primary := <bool>email['primary'],
            confirmation := (
                INSERT EmailConfirmation {
                    key := <str>email['confirmation']['key'],
                    created_at := <datetime>email['confirmation']['created_at']
                }
            )
        }
    )
  ),
  _password_hash := <str>user['_password_hash'],
  is_active := <bool>user['is_active'],
  is_superuser := <bool>user['is_superuser'],
  password_reset_confirmation := (
    INSERT PasswordResetConfirmation {
        key := <str>user['password_reset_confirmation']['key'],
        created_at := <datetime>user['password_reset_confirmation']['created_at']
    }
  )
};