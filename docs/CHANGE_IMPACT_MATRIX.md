# Change impact matrix

What `scripts/check_docs_changes.py` enforces. If you change files matching
the left column, the right column's docs must change in the same PR.

| Changed path | Required docs |
|---|---|
| `features/**/*.feature` | `docs/TEST_CATALOG.md`, `docs/TRACEABILITY.md` |
| `features/steps/**`, `features/environment.py` | `docs/TEST_AUTHORING_GUIDE.md` |
| `src/data/{factories,generators,builders}/**` | `docs/DATA_FACTORY_GUIDE.md`, `docs/FACTORY_CATALOG.md` |
| `src/pages/**` | `docs/MODULE_CATALOG.md` |
| `src/api/**` | `docs/API_GUIDE.md` |
| `src/core/**` | `docs/ARCHITECTURE.md` |
| `behave.ini`, `pytest.ini`, `requirements.txt`, `.env.example`, `.github/workflows/**` | `README.md`, `docs/CONFIGURATION.md` |
