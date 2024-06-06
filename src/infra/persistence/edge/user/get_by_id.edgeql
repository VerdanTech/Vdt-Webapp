SELECT User {
    **,
    emails := (
        SELECT User.emails {
            **
        }
    )
    }
FILTER .id = <uuid>$id
