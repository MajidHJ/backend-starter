# Users API Contract (v1)

## Endpoints (CRUD)

| Method | Path              | Success | Description        |
|-------:|-------------------|:-------:|--------------------|
| POST   | /v1/users         | 201     | Create user        |
| GET    | /v1/users         | 200     | List users         |
| GET    | /v1/users/{id}    | 200     | Get user by id     |
| PUT    | /v1/users/{id}    | 200     | Update user        |
| DELETE | /v1/users/{id}    | 204     | Delete user        |

## Data Contract (Conceptual)

### Create (POST /v1/users)
- Request body: { email, name }
- Response body (201): { id, email, name }

### List (GET /v1/users)
- Query params:
  - page: int (default=1, min=1)
  - size: int (default=20, min=1, max=100)
- Response body (200): Page[UserResponse]
  - { items: [ { id, email, name }, ... ], total: int }
- Semantics:
  - total = total number of users across all pages
  - items length <= size


### Get (GET /v1/users/{id})
- Success (200): { id, email, name }
- Not found (404): ErrorResponse

### Update (PUT /v1/users/{id})
- Request body: { name }  (email is immutable)
- Success (200): { id, email, name }
- Not found (404): ErrorResponse

### Delete (DELETE /v1/users/{id})
- Success (204): empty body
- Not found (404): ErrorResponse

## Error Contract (Minimum)
- 404 USER_NOT_FOUND
