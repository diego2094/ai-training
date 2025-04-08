# Endpoint A: /api/users (Documentation-First)

**Method**: GET  
**Query Params**:

- `page` (integer, optional, default=1)
- `limit` (integer, optional, default=10)

**Response**:

- JSON array of users, paginated
- A `totalCount` field indicating the total number of users

**Behavior**:

- If `page` or `limit` are not provided, defaults are used (page=1, limit=10).
- Returns HTTP 200 on success.
- You can include any validations or example responses as needed.
