# Data factory guide

Three layers, matching `demoqa-playwright-framework`'s `src/data/`:

- **Generators** (`src/data/generators/common_generator.py`) -- shared
  primitives (`id`, `email`, `password`, `address`, `date_of_birth`, ...).
  Factories compose these instead of each reaching for `Faker()`/`random`
  directly, so a change to "what a generated email looks like" happens in
  one place.
- **Factories** (`src/data/factories/`) -- one factory per data shape
  (`UserFactory`, `StudentFactory`, `BookFactory`, `FormFactory`). Every
  `create()`/static method takes an `overrides: dict | None` so a scenario
  can pin exactly the field it cares about and let everything else be
  randomly generated.
- **Builders** (`src/data/builders/`) -- fluent wrappers over a factory for
  scenarios that override several fields together
  (`StudentBuilder().with_gender(...).with_address(...).build()`).

## Why overrides are a dict, not keyword arguments

```python
StudentFactory.create({"gender": "Female"})
```

A dict lets a factory forward `**overrides` onto the generated base dict
before constructing the dataclass, without every factory method needing to
declare every field as an optional keyword argument. The dataclass itself
(`StudentData`, `UserData`, ...) still validates the complete, final shape.

## Adding a new factory

1. Add the dataclass next to whatever consumes it (a page object, or
   `src/api/` for API-only data) -- not a separate shared types module,
   since this repo's three dataclasses each have exactly one consumer.
2. Add the factory in `src/data/factories/`, composing `CommonGenerator`.
3. Add a unit test in `tests/unit/test_factories.py` asserting uniqueness
   across two calls and that overrides actually take effect -- this is the
   fast, no-browser feedback loop for the data layer; see
   `docs/FACTORY_CATALOG.md`.
