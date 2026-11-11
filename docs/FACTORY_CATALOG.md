# Factory catalog

| Factory | Produces | Composed from | Consumers |
|---|---|---|---|
| `UserFactory` | `UserData` | `CommonGenerator` | `StudentFactory`, bookstore scenarios |
| `StudentFactory` | `StudentData` (practice form) | `CommonGenerator` | `StudentBuilder`, Forms feature |
| `StudentBuilder` | `StudentData`, fluently overridden | `StudentFactory` | Forms feature (scenario-specific overrides) |
| `BookFactory` | `BookData` | fixed DemoQA catalog | Bookstore API feature |
| `FormFactory` | `TextBoxData` | `CommonGenerator` | Elements feature |

Unit-tested in `tests/unit/test_factories.py` (no browser, no network --
pure data-shape and uniqueness assertions). Run with:

```bash
pytest
```
