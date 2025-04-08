# User Management Specification

**Endpoint**: `POST /api/users`

## Request Body

- `username` (string, required)
- `email` (string, required)
- `password` (string, required)

## Behavior

- Returns `201 Created` on success, with a JSON response containing the new user's info.
- Returns `400 Bad Request` if any required field is missing.
- Stores user data in an in-memory array for now (simple prototype).
