# API client guide

`src/api/bookstore_client.py` wraps DemoQA's public Book Store REST API
with the `requests` library -- no Selenium involved, since API-level
scenarios should never pay for a browser they don't need.

## BookStoreClient

| Method | Endpoint | Notes |
|---|---|---|
| `create_account(user)` | `POST /Account/v1/User` then `POST /Account/v1/GenerateToken` | Returns a `BookStoreAccount` (user id + bearer token); raises if either call fails or no token comes back |
| `add_book(account, isbn)` | `POST /BookStore/v1/Books` | Bearer-authenticated |
| `get_books(account)` | `GET /BookStore/v1/Books?UserId=...` | Bearer-authenticated |
| `delete_account(account)` | `DELETE /Account/v1/User/{id}` | Treats 404 as already-cleaned-up, not a failure -- any other non-2xx still raises |

Every method raises a plain `RuntimeError` with the response status and
body on failure rather than returning `None`/an empty result -- a failed
API call should never look identical to "nothing to assert on" in a step
definition.

## Why account cleanup tolerates 404

If a scenario fails between account creation and the explicit cleanup
step, or if two runs race, the account may already be gone by the time
`delete_account` runs. Only `404` is treated as "already handled"; every
other status still raises so a genuine cleanup failure is visible.
