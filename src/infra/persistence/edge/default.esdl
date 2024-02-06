type User {
    required username: str;
    multi emails: Email;
    required _password_hash: str
    required is_active: bool
    required is_superuser: bool
    optional password_reset_contirmation: PasswordResetConfirmation 
}

type Email {
    required address: str;
    required verified: bool;
    required primary: bool;
    optional confirmation: EmailConfirmation
    optional verified_at: datetime 
}

abstract type BaseConfirmation {
    required key: str
    required created_at: datetime
}

type PasswordResetConfirmation extending BaseConfirmation {

}

type EmailConfirmation extending BaseConfirmation {

}