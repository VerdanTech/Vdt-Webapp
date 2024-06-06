module Garden {

    scalar type VisibilityEnum extending enum<PRIVATE, UNLISTED, PUBLIC>;
    scalar type RoleEnum extending enum<ADMIN, EDITOR, VIEWER>;

    type Garden extending RootEntity {
        required key: str;
        required name: str
        optional creator_ref: Ref;
        required visibility: VisibilityEnum;
        optional attributes_ref: Ref;
        multi memberships: GardenMembership {
            constraint exclusive;
            on source delete delete target;
        }
        optional description: str;
        required expired: bool;
    }

    type GardenMembership extending ValueObject {
        required user_ref: Ref;
        optional inviter_ref: Ref;
        required role: RoleEnum;
        required accepted: bool;
        required favorite: bool;
        required created_at: datetime;
    }

}