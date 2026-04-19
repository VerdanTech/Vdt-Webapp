# Gardens Schema Reference

Domain model for the Gardens feature. Defines CoValues, enums, and field constraints.

---

## Enums

### `GardenVisibilityEnumOptions`

Controls the visibility of the garden.

| Value      | Description                                                 |
| ---------- | ----------------------------------------------------------- |
| `HIDDEN`   | Visible only to members. Not accessible without membership. |
| `UNLISTED` | Visible to anyone with a direct link. Not listed publicly.  |
| `PUBLIC`   | Publicly visible and searchable.                            |

> **Note:** `HIDDEN` is enforced at the Jazz Group level (no `"everyone"` member). `UNLISTED` and `PUBLIC` both grant `"everyone": "reader"` on the Group — the distinction is whether the garden appears in the public index CoValue.

---

### `GardenMembershipRoleEnumOptions`

Controls the level of access granted by a membership.

| Value    | Jazz Group Role | Description                                                                |
| -------- | --------------- | -------------------------------------------------------------------------- |
| `ADMIN`  | `manager`       | Routine and configuration changes. Can manage members below manager level. |
| `EDITOR` | `writer`        | Routine model changes (e.g. adding plants). No configuration access.       |
| `VIEWER` | `reader`        | Read-only access.                                                          |

> **Note:** The garden creator holds Jazz `admin` (not mapped to any app role). Only the creator or a server worker co-admin can elevate members to `manager`.

---

### `GardenMembershipStatusEnumOptions`

Indicates the acceptance status of a membership invite.

| Value      | Description                                  |
| ---------- | -------------------------------------------- |
| `CREATED`  | Invite created but no notification sent yet. |
| `PENDING`  | Notification sent, awaiting acceptance.      |
| `ACCEPTED` | Membership accepted.                         |

---

## CoValues

### `GardenMembershipSchema`

Stores per-member metadata alongside Jazz Group membership. Jazz Group membership controls access; this CoValue stores supplementary state.

```ts
co.map({
	user: co.account(),
	role: z.enum(['ADMIN', 'EDITOR', 'VIEWER']),
	status: z.enum(['CREATED', 'PENDING', 'ACCEPTED']),
	acceptedAt: z.date(),
	favorite: z.boolean()
});
```

| Field        | Type           | Description                                                |
| ------------ | -------------- | ---------------------------------------------------------- |
| `user`       | `co.account()` | Reference to the Jazz account of the member.               |
| `role`       | enum           | App-level role. Must be kept in sync with Jazz Group role. |
| `status`     | enum           | Invite acceptance state.                                   |
| `acceptedAt` | `Date`         | When the invite was accepted.                              |
| `favorite`   | `boolean`      | Whether the user has marked this garden as a favourite.    |

---

### `GardenContextSchema`

Placeholder for garden-scoped content. All feature modules (workspaces, cultivar collections, environments, etc.) attach here rather than directly to `GardenSchema`, keeping the garden root stable as features expand.

```ts
co.map({});
```

> Currently empty. New domain areas add a field here, not to `GardenSchema`.

---

### `GardenSchema`

Root CoValue for a garden. Owned by a Jazz Group whose membership mirrors the app-level role system.

```ts
co.map({
	context: GardenContextSchema,
	id: z.string(), // URL slug, alphanumeric + hyphens, 4–21 chars
	name: z.string(),
	description: co.plainText(),
	memberships: co.list(GardenMembershipSchema)
});
```

| Field         | Type                              | Description                                                   |
| ------------- | --------------------------------- | ------------------------------------------------------------- |
| `context`     | `GardenContextSchema`             | Container for all feature-specific content.                   |
| `id`          | `string`                          | URL-friendly slug. Alphanumeric and hyphens, 4–21 characters. |
| `name`        | `string`                          | Display name. Non-unique.                                     |
| `description` | `co.plainText()`                  | Collaborative rich text description.                          |
| `memberships` | `co.list(GardenMembershipSchema)` | Ordered list of membership metadata records.                  |

---

### `GardenIndexSchema`

Public index of all `PUBLIC` gardens. Owned by the server worker group with `"everyone": "reader"`. Used for discovery — gardens do not appear here unless `visibility = PUBLIC`.

```ts
co.record(gardenIdField, GardenSchema);
// Well-known ID: GLOBAL_PUBLIC_GARDEN_INDEX_ID = 'global-public-gardens'
```

| Key             | Value                    | Description                                                                              |
| --------------- | ------------------------ | ---------------------------------------------------------------------------------------- |
| Garden URL slug | `GardenSchema` reference | Entry added when visibility set to `PUBLIC`, removed when set to `UNLISTED` or `HIDDEN`. |

---

## Exported Types

```ts
type Garden = co.loaded<typeof GardenSchema>;
type GardenMembership = co.loaded<typeof GardenMembershipSchema>;
type GardenIndex = co.loaded<typeof GardenIndexSchema>;
```

---

## Field Constraints

Defined in `fields.ts`. Used in command schemas for form validation — not enforced at the CoValue layer.

| Field                         | Constraint                                                  |
| ----------------------------- | ----------------------------------------------------------- |
| `gardenIdField`               | `string`, trimmed, lowercase, 4–21 chars, `/[0-9A-Za-z-]+/` |
| `gardenNameField`             | Inherited from `commonFields.nameSchema`                    |
| `gardenDescriptionField`      | Inherited from `commonFields.descriptionSchema`             |
| `gardenVisibilityField`       | `z.enum(GardenVisibilityEnumOptions)`                       |
| `gardenMembershipRoleField`   | `z.enum(GardenMembershipRoleEnumOptions)`                   |
| `gardenMembershipStatusField` | `z.enum(GardenMembershipStatusEnumOptions)`                 |
| `usernameInvitesListField`    | Array of username strings, max 10 items                     |

---

## Visibility Enforcement

Visibility is enforced at two layers that must be kept in sync:

| Visibility | Jazz Group `"everyone"` role | In `GardenIndexSchema` |
| ---------- | ---------------------------- | ---------------------- |
| `HIDDEN`   | None                         | No                     |
| `UNLISTED` | `reader`                     | No                     |
| `PUBLIC`   | `reader`                     | Yes                    |

When visibility changes, both layers must be updated atomically by the controller.
