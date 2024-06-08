module User {

    type User extending RootEntity {
        required username: str;
        multi emails: Email {
            constraint exclusive;
            on source delete delete target;
        };
        required _password_hash: str;
        required is_active: bool;
        required is_superuser: bool;
        optional password_reset_confirmation: PasswordResetConfirmation; 
    }

    type Email extending ValueObject {
        required address: str;
        required verified: bool;
        required primary: bool;
        optional confirmation: EmailConfirmation;
        optional verified_at: datetime;
    }

    abstract type BaseConfirmation extending ValueObject {
        required key: str;
        required created_at: datetime;
    }

    type PasswordResetConfirmation extending BaseConfirmation {

    }

    type EmailConfirmation extending BaseConfirmation {

    }


    type Garden extending RootEntity {
        required key: str;
        required name: str;
        optional creator: User;  
    }
}