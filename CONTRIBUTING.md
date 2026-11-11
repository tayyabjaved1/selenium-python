# Contributing

1. Read `README.md`, `docs/ARCHITECTURE.md`, `docs/DATA_FACTORY_GUIDE.md` and `docs/TEST_AUTHORING_GUIDE.md` before adding tests.
2. Follow the layer dependency rules in the architecture guide -- step definitions call page objects/API clients, page objects never import `behave`.
3. Generate fresh data through existing generators/factories; do not duplicate random-data logic in step files.
4. Add a dataclass for new domain data and use factory overrides for scenario variations.
5. Keep scenarios isolated and safe to run in any order -- no scenario should depend on another having run first.
6. Use page objects for page interactions; no raw Selenium calls in a step definition.
7. Add API setup/teardown only when supported by the target application, and make it self-cleaning on both pass and fail.
8. Run `pytest` and the relevant `behave` tags/features before submitting changes.
9. Never commit `.env`, credentials, tokens, generated reports (`allure-results/`, `allure-report/`) or `.artifacts/`.

When a new module is added, update `docs/MODULE_CATALOG.md`'s summary table and add its section. Do not edit global `behave.ini`/CI configuration unless the new requirement is truly cross-cutting (for example, a new tag convention or reporter).

## Documentation is part of the change

Follow the [Documentation as Code policy](docs/DOCUMENTATION_POLICY.md) and [change impact matrix](docs/CHANGE_IMPACT_MATRIX.md). Update the relevant guides and catalogs in the same PR as the code. The PR template contains the required checklist. Run `python scripts/check_docs_changes.py` before submitting. This automated check is a guardrail; reviewers must still verify that the documentation accurately describes the implementation.
