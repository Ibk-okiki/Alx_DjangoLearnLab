# Permissions & Groups Setup

## Custom Permissions
Defined on `Book` model in `bookshelf/models.py`:

- `can_view`: View book listings
- `can_create`: Create new books
- `can_edit`: Edit book details
- `can_delete`: Delete books

## User Groups
Created via admin or script:
- **Viewers**: `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: All permissions

## How It Works
Views are protected with `@permission_required()` decorators.

- Only users with `can_create` can access book creation.
- Unauthorized users receive `403 Forbidden`.

## Testing
Create users and assign them to groups from Django Admin. Log in and test permissions by visiting book views.
